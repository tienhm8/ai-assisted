#!/usr/bin/env python3
"""Export a customer confirmation pack (Markdown + ```wireframe blocks) to one self-contained HTML
file the BA can send or print to PDF. Standard library only.

Usage (from the repo root; -I keeps Python from importing files in the repo):
  python3 -I .ai/scripts/export-pack.py <pack.md> [-o out.html] [--style wireframe|mockup|both] [--pdf] [--keep-internal]

  --style  override the style of every screen; default: each screen's own `style:` line
  --pdf    also write <out>.pdf with headless Chrome/Chromium when one is installed
  --keep-internal  keep <!-- internal:start --> ... <!-- internal:end --> blocks (default: removed)

Wireframe syntax: .ai/templates/CONFIRMATION-PACK-TEMPLATE.md, section "Cú pháp wireframe".
Exit code 1 on a syntax problem (unknown element, bad table), 2 on bad arguments.
"""
import argparse
import base64
import html
import mimetypes
import os
import re
import shutil
import subprocess
import sys

PROBLEMS = []


def problem(msg):
    PROBLEMS.append(msg)
    print("export-pack: " + msg, file=sys.stderr)


# ---------- inline markdown ----------

def inline(s, base):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)

    def img(m):
        path = os.path.join(base, m.group(2))
        if not os.path.isfile(path):
            problem("image not found: " + m.group(2))
            return m.group(0)
        mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return '<img alt="%s" src="data:%s;base64,%s">' % (m.group(1), mime, data)

    s = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", img, s)

    def link(m):
        url = m.group(2)
        if re.match(r"(https?://|mailto:|#)", url):
            return '<a href="%s">%s</a>' % (url, m.group(1))
        return m.group(1)  # relative repo links mean nothing to the customer

    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    return s.replace("&lt;br&gt;", "<br>")


def slug(text):
    t = re.sub(r"<[^>]+>", "", text).lower()
    return re.sub(r"[^\w]+", "-", t, flags=re.U).strip("-") or "muc"


# ---------- wireframe ----------

PIN = re.compile(r"\s+#(\d+)\s*$")
META = {"screen", "style", "role", "device", "id"}


def pin_of(text):
    m = PIN.search(text)
    if m:
        return text[: m.start()].rstrip(), '<span class="pin">%s</span>' % m.group(1)
    return text, ""


def e(s):
    return html.escape(s.strip(), quote=False)


def cell(c):
    c = c.strip()
    m = re.fullmatch(r"\[(x| )\]", c)
    if m:
        return '<span class="cb%s"></span>' % (" on" if m.group(1) == "x" else "")
    m = re.fullmatch(r"\[([^\]]+)\]", c)
    if m:
        return '<span class="btn sm">%s</span>' % e(m.group(1))
    m = re.fullmatch(r"\{([^}:]+)(?::(ok|warn|bad))?\}", c)
    if m:
        return '<span class="badge %s">%s</span>' % (m.group(2) or "", e(m.group(1)))
    return e(c)


def field(kind, text):
    text, pin = pin_of(text)
    value = ""
    if " = " in text:
        text, value = text.split(" = ", 1)
    auto = ""
    if "[auto]" in text:
        text = text.replace("[auto]", "")
        auto = '<span class="auto">tự điền</span>'
    req = ""
    text = text.strip()
    if text.endswith("*"):
        text, req = text[:-1].strip(), '<span class="req">*</span>'
    if kind == "textarea":
        body = '<div class="box tall">%s</div>' % (e(value) if value else "")
    elif kind == "upload":
        body = '<div class="box drop">⬆ %s</div>' % (e(value) or "Kéo thả hoặc chọn tệp")
    else:
        caret = '<span class="caret">▾</span>' if kind == "select" else ""
        if kind == "date":
            caret = '<span class="caret">▦</span>'
        body = '<div class="box"><span class="val">%s</span>%s</div>' % (e(value), caret)
    return '<div class="fld"><label>%s%s%s%s</label>%s</div>' % (e(text), req, auto, pin, body)


def button(text):
    text, pin = pin_of(text)
    kind = "sec"
    m = re.search(r"\((primary|danger)\)\s*$", text)
    if m:
        kind, text = m.group(1), text[: m.start()]
    return '<span class="btn %s">%s</span>%s' % (kind, e(text), pin)


def simple(kind, text):
    if kind in ("input", "select", "textarea", "date", "upload"):
        return field(kind, text)  # field() reads its own #n pin
    text, pin = pin_of(text)
    if kind == "title":
        return "<h4>%s%s</h4>" % (e(text), pin)
    if kind == "subtitle":
        return '<p class="sub">%s%s</p>' % (e(text), pin)
    if kind == "text":
        return "<p>%s%s</p>" % (inline(text, "."), pin)
    if kind == "alert":
        return '<div class="alert">%s%s</div>' % (e(text), pin)
    if kind == "divider":
        return "<hr>"
    if kind == "spacer":
        return '<div class="spacer"></div>'
    if kind in ("checkbox", "radio"):
        m = re.match(r"\[(x| )\]\s*(.*)|\((o| )\)\s*(.*)", text)
        on = bool(m and (m.group(1) == "x" or m.group(3) == "o"))
        label = (m.group(2) if m and m.group(2) is not None else m.group(4)) if m else text
        return '<div class="chk"><span class="%s%s"></span> %s%s</div>' % (
            "cb" if kind == "checkbox" else "rd", " on" if on else "", e(label), pin)
    if kind == "button":
        return button(text) + pin
    if kind == "badge":
        m = re.match(r"(.*?)\s*\((ok|warn|bad)\)\s*$", text)
        return '<span class="badge %s">%s</span>%s' % (m.group(2) if m else "", e(m.group(1) if m else text), pin)
    return None


def render_elements(lines):
    out, table, notes, i = [], None, {}, 0

    def flush():
        nonlocal table
        if table:
            head, rows = table
            t = "<table class='wt'><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (
                "".join("<th>%s</th>" % e(c) for c in head),
                "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % cell(c) for c in r) for r in rows))
            out.append(t)
            table = None

    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("//"):
            continue
        if ":" not in line:
            problem("wireframe line without 'type:' -> " + line)
            continue
        kind, text = [x.strip() for x in line.split(":", 1)]
        if kind == "tr":
            if table is None:
                problem("'tr:' before 'table:' -> " + line)
                continue
            table[1].append([c for c in text.split("|")])
            continue
        flush()
        if kind == "table":
            table = ([c for c in text.split("|")], [])
        elif kind == "note":
            n, _, t = text.partition("|")
            notes[n.strip()] = t.strip()
        elif kind == "topbar":
            parts = [p.strip() for p in text.split(" ; ")]
            out.append('<div class="topbar"><b>%s</b><span class="sp"></span>%s</div>' % (
                e(parts[0]), "".join("<span>%s</span>" % e(p) for p in parts[1:])))
        elif kind == "tabs":
            tabs = []
            for p in [p.strip() for p in text.split(" ; ")]:
                on = p.endswith("*")
                tabs.append('<span class="tab%s">%s</span>' % (" on" if on else "", e(p.rstrip("*"))))
            out.append('<div class="tabs">%s</div>' % "".join(tabs))
        elif kind == "steps":
            st = []
            for p in [p.strip() for p in text.split(">")]:
                on = p.endswith("*")
                st.append('<span class="step%s">%s</span>' % (" on" if on else "", e(p.rstrip("*"))))
            out.append('<div class="steps">%s</div>' % "".join(st))
        elif kind == "kpi":
            cards = []
            for p in [p.strip() for p in text.split(" ; ")]:
                p, pin = pin_of(p)
                label, _, val = p.partition(" = ")
                cards.append('<div class="kpi"><small>%s</small><b>%s</b>%s</div>' % (e(label), e(val), pin))
            out.append('<div class="row">%s</div>' % "".join(cards))
        elif kind == "bar":
            parts = []
            for p in [p.strip() for p in text.split(" ; ")]:
                label, _, val = p.partition(" = ")
                try:
                    w = max(2, min(100, int(float(val.rstrip("%")))))
                except ValueError:
                    w = 10
                parts.append('<div class="bar"><span>%s</span><i style="width:%d%%"></i><em>%s</em></div>' % (
                    e(label), w, e(val)))
            out.append("".join(parts))
        elif kind == "cols":
            items = []
            for p in [p.strip() for p in text.split(" ; ")]:
                k, _, t = p.partition(":")
                html_ = simple(k.strip(), t.strip())
                if html_ is None:
                    problem("unknown element in cols -> " + k.strip())
                    continue
                items.append(html_)
            out.append('<div class="row">%s</div>' % "".join('<div class="cell">%s</div>' % x for x in items))
        elif kind in META:
            continue
        else:
            html_ = simple(kind, text)
            if html_ is None:
                problem("unknown wireframe element '%s'" % kind)
            else:
                out.append(html_)
    flush()
    return "".join(out), notes


def render_wireframe(src, force):
    meta, body = {}, []
    for raw in src.splitlines():
        m = re.match(r"\s*(screen|style|role|device|id)\s*:\s*(.*)$", raw)
        if m and m.group(1) not in meta:
            meta[m.group(1)] = m.group(2).strip()
        else:
            body.append(raw)
    styles = ["wireframe", "mockup"] if force == "both" else [force or meta.get("style", "wireframe")]
    inner, notes = render_elements(body)
    figs = []
    for st in styles:
        if st not in ("wireframe", "mockup"):
            problem("style must be wireframe or mockup, got '%s'" % st)
            st = "wireframe"
        label = "Wireframe (bản phác bố cục)" if st == "wireframe" else "Mockup (bản minh hoạ giao diện)"
        cap = "<b>%s %s</b>" % (e(meta.get("id", "")), e(meta.get("screen", "Màn hình")))
        if meta.get("role"):
            cap += " · Người dùng: " + e(meta["role"])
        cap += ' · <span class="kind">%s</span>' % label
        nl = "".join('<li value="%s"><span class="pin">%s</span> %s</li>' % (n, n, inline(t, "."))
                     for n, t in sorted(notes.items(), key=lambda kv: int(kv[0]) if kv[0].isdigit() else 99))
        figs.append(
            '<figure class="scr %s %s"><figcaption>%s</figcaption><div class="frame">%s</div>%s</figure>' % (
                "wf" if st == "wireframe" else "mk", meta.get("device", "desktop"), cap, inner,
                ('<ol class="notes">%s</ol>' % nl) if nl else ""))
    return "".join(figs)


# ---------- markdown blocks ----------

BLOCK_START = re.compile(r"^(#{1,4}\s|```|\||>|\s*([-*]|\d+\.)\s+|---+\s*$)")


def render_list(items, base):
    out, stack = [], []  # stack of (indent, tag)
    for indent, tag, text in items:
        while stack and indent < stack[-1][0]:
            out.append("</li></%s>" % stack.pop()[1])
        if stack and indent == stack[-1][0]:
            out.append("</li><li>")
        else:
            stack.append((indent, tag))
            out.append("<%s><li>" % tag)
        out.append(inline(text, base))
    while stack:
        out.append("</li></%s>" % stack.pop()[1])
    return "".join(out)


def split_row(line):
    line = line.strip().replace("\\|", "\x00")
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip().replace("\x00", "|") for c in line.split("|")]


def render_md(text, base, force):
    lines, out, heads, i = text.split("\n"), [], [], 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        m = re.match(r"```(\w*)", ln)
        if m:
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            code = "\n".join(lines[i + 1: j])
            if m.group(1) == "wireframe":
                out.append(render_wireframe(code, force))
            else:
                out.append("<pre>%s</pre>" % html.escape(code))
            i = j + 1
            continue
        m = re.match(r"(#{1,4})\s+(.*)", ln)
        if m:
            lvl, t = len(m.group(1)), m.group(2).strip()
            heads.append((lvl, t, slug(t)))
            out.append('<h%d id="%s">%s</h%d>' % (lvl, slug(t), inline(t, base), lvl))
            i += 1
            continue
        if re.match(r"---+\s*$", ln):
            out.append("<hr>")
            i += 1
            continue
        if ln.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"\s*\|?\s*:?-{3,}", lines[i + 1]):
            head = split_row(ln)
            j, rows = i + 2, []
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                r = split_row(lines[j])
                if len(r) != len(head):
                    problem("table row has %d cells, header has %d: %s" % (len(r), len(head), lines[j][:60]))
                rows.append(r)
                j += 1
            ans = any("Trả lời" in h for h in head)
            out.append('<table%s><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (
                ' class="answer"' if ans else "",
                "".join("<th>%s</th>" % inline(h, base) for h in head),
                "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c, base) for c in r) for r in rows)))
            i = j
            continue
        if ln.startswith(">"):
            j, buf = i, []
            while j < len(lines) and lines[j].startswith(">"):
                buf.append(re.sub(r"^>\s?", "", lines[j]))
                j += 1
            inner, _ = render_md("\n".join(buf), base, force)
            out.append("<blockquote>%s</blockquote>" % inner)
            i = j
            continue
        m = re.match(r"(\s*)([-*]|\d+\.)\s+(.*)", ln)
        if m:
            items, j = [], i
            while j < len(lines):
                m = re.match(r"(\s*)([-*]|\d+\.)\s+(.*)", lines[j])
                if m:
                    items.append([len(m.group(1)) // 2 * 2, "ol" if m.group(2)[0].isdigit() else "ul", m.group(3)])
                elif lines[j].strip() and lines[j].startswith("  ") and items:
                    items[-1][2] += " " + lines[j].strip()
                else:
                    break
                j += 1
            out.append(render_list(items, base))
            i = j
            continue
        j, buf = i, []
        while j < len(lines) and lines[j].strip() and not (j > i and BLOCK_START.match(lines[j])):
            buf.append(lines[j].strip())
            j += 1
        out.append("<p>%s</p>" % inline(" ".join(buf), base))
        i = j
    return "\n".join(out), heads


CSS = """
:root{--ink:#1d2430;--mut:#5b6677;--line:#d5dae2;--acc:#1e5aa8;--bg:#fff;--soft:#f4f6f9}
*{box-sizing:border-box}body{margin:0;background:var(--soft);color:var(--ink);font:15px/1.55 system-ui,"Segoe UI",Roboto,sans-serif}
main{max-width:980px;margin:0 auto;padding:24px 16px 64px;background:var(--bg)}
h1{font-size:28px;margin:.2em 0}h2{font-size:21px;border-bottom:2px solid var(--acc);padding-bottom:4px;margin-top:2em}
h3{font-size:17px;margin-top:1.6em}h4{margin:.2em 0 .5em;font-size:15px}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:14px}th,td{border:1px solid var(--line);padding:6px 8px;vertical-align:top;text-align:left}
th{background:var(--soft)}table.answer td:last-child,table.answer td:nth-last-child(2):empty{min-width:150px;height:44px}
blockquote{margin:12px 0;padding:6px 14px;border-left:4px solid var(--acc);background:var(--soft);color:var(--mut)}
code{background:var(--soft);padding:0 4px;border-radius:3px}pre{background:var(--soft);padding:10px;overflow:auto}
img{max-width:100%}.cover{padding:32px 0 24px;border-bottom:1px solid var(--line)}
nav.toc{margin:20px 0;padding:12px 18px;background:var(--soft);border-radius:6px}nav.toc ol{margin:4px 0;padding-left:0;list-style:none}nav.toc a{color:var(--ink);text-decoration:none}
figure.scr{margin:16px 0;padding:0;break-inside:avoid}figcaption{font-size:13px;color:var(--mut);margin-bottom:6px}.kind{border:1px solid var(--line);border-radius:10px;padding:0 8px;font-size:12px}
.frame{padding:12px;border:2px solid #444;border-radius:6px;background:#fff;max-width:760px}.scr.mobile .frame{max-width:340px}
.scr .row{display:flex;gap:10px;align-items:flex-end;flex-wrap:wrap;margin:6px 0}.scr .cell{flex:1 1 120px}
.scr .fld{margin:6px 0}.scr label{display:block;font-size:12px;color:#444;margin-bottom:2px}.req{color:#b3261e}
.box{min-height:30px;border:1.5px solid #888;border-radius:4px;padding:4px 8px;display:flex;justify-content:space-between;background:#fff;color:#333}
.box.tall{min-height:70px}.box.drop{border-style:dashed;color:#666;justify-content:center}.val{font-style:italic}.caret{color:#666}
.auto{margin-left:6px;font-size:11px;background:#e7eef9;color:#1e5aa8;border-radius:8px;padding:0 6px}
.btn{display:inline-block;border:1.5px solid #666;border-radius:4px;padding:3px 12px;font-size:13px;margin:2px 4px 2px 0;background:#fff}
.btn.primary{background:#444;color:#fff;border-color:#444}.btn.danger{border-style:dashed}.btn.sm{padding:0 8px;font-size:12px}
.badge{display:inline-block;border:1px solid #888;border-radius:10px;padding:0 8px;font-size:12px;background:#eee}
.topbar{display:flex;gap:14px;align-items:center;padding:6px 10px;margin:-12px -12px 10px;background:#ddd;border-bottom:1.5px solid #666}.sp{flex:1}
.tabs{display:flex;gap:2px;border-bottom:1.5px solid #888;margin:8px 0}.tab{padding:4px 12px;border:1.5px solid #888;border-bottom:0;border-radius:4px 4px 0 0;font-size:13px}.tab.on{background:#444;color:#fff}
.steps{display:flex;gap:6px;margin:8px 0;flex-wrap:wrap}.step{padding:3px 12px;border:1.5px solid #888;border-radius:14px;font-size:12px}.step.on{background:#444;color:#fff}
.kpi{flex:1 1 120px;border:1.5px solid #888;border-radius:6px;padding:8px}.kpi small{display:block;color:#555}.kpi b{font-size:20px}
.bar{display:flex;align-items:center;gap:8px;margin:3px 0;font-size:12px}.bar span{width:130px}.bar i{display:block;height:12px;background:#999}.bar em{font-style:normal}
.alert{border:1.5px solid #888;border-left:6px solid #666;padding:6px 10px;margin:8px 0;background:#f2f2f2;font-size:13px}
.chk{margin:3px 0;font-size:14px}.cb,.rd{display:inline-block;width:14px;height:14px;border:1.5px solid #666;vertical-align:-2px;margin-right:4px}.rd{border-radius:50%}
.cb.on{background:#444}.rd.on{background:radial-gradient(#444 45%,#fff 50%)}.spacer{height:14px}
.wt{margin:8px 0;font-size:13px}.wt th{background:#e6e6e6}.sub{color:#555;margin:0 0 8px}
.pin{display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:50%;background:#d9480f;color:#fff;font-size:11px;font-weight:700;margin-left:4px}
.notes{font-size:13px;list-style:none;padding:0;margin:8px 0}.notes li{margin:3px 0}
.scr.mk .frame{border:1px solid #cfd6e0;border-radius:10px;box-shadow:0 2px 10px rgba(20,40,80,.12)}
.scr.mk .topbar{background:#1e5aa8;color:#fff;border:0}.scr.mk .box{border:1px solid #b9c3d3;border-radius:6px}
.scr.mk .btn{border:1px solid #1e5aa8;color:#1e5aa8;border-radius:6px}.scr.mk .btn.primary{background:#1e5aa8;color:#fff}
.scr.mk .btn.danger{border-color:#b3261e;color:#b3261e;border-style:solid}.scr.mk .tab.on,.scr.mk .step.on{background:#1e5aa8;border-color:#1e5aa8}
.scr.mk .badge.ok{background:#dff3e4;border-color:#7bc08c}.scr.mk .badge.warn{background:#fff1d6;border-color:#e0b251}.scr.mk .badge.bad{background:#fbe0de;border-color:#e08a84}
.scr.mk .kpi{border-color:#cfd6e0;background:#f7f9fc}.scr.mk .bar i{background:#1e5aa8}.scr.mk .wt th{background:#eaf0f9}
@media print{body{background:#fff}main{max-width:none;padding:0}@page{size:A4;margin:14mm}.cover{page-break-after:always}h2{page-break-after:avoid}tr{break-inside:avoid}}
"""


def build(text, base, force, keep_internal):
    if not keep_internal:
        text = re.sub(r"<!--\s*internal:start\s*-->.*?<!--\s*internal:end\s*-->", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    body, heads = render_md(text, base, force)
    title = next((t for lvl, t, _ in heads if lvl == 1), "Gói xác nhận yêu cầu")
    first_h2 = body.find("<h2")
    cover, rest = (body[:first_h2], body[first_h2:]) if first_h2 > 0 else (body, "")
    toc = "".join('<li><a href="#%s">%s</a></li>' % (s, html.escape(t)) for lvl, t, s in heads if lvl == 2)
    return ("<!doctype html><html lang=\"vi\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            "<title>%s</title><style>%s</style></head><body><main><section class=\"cover\">%s<nav class=\"toc\"><b>Mục lục</b><ol>%s</ol></nav></section>%s</main></body></html>"
            % (html.escape(title), CSS, cover, toc, rest))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pack")
    ap.add_argument("-o", "--out")
    ap.add_argument("--style", choices=["wireframe", "mockup", "both"])
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--keep-internal", action="store_true")
    a = ap.parse_args()
    if not os.path.isfile(a.pack):
        print("export-pack: file not found: " + a.pack, file=sys.stderr)
        return 2
    out = a.out or os.path.splitext(a.pack)[0] + ".html"
    with open(a.pack, encoding="utf-8") as f:
        text = f.read()
    doc = build(text, os.path.dirname(os.path.abspath(a.pack)), a.style, a.keep_internal)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote " + out)
    if a.pdf:
        chrome = next((shutil.which(c) for c in ("google-chrome", "chromium", "chromium-browser", "chrome") if shutil.which(c)), None)
        if not chrome:
            print("export-pack: no Chrome/Chromium found; open the HTML and print to PDF", file=sys.stderr)
        else:
            pdf = os.path.splitext(out)[0] + ".pdf"
            subprocess.run([chrome, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                            "--print-to-pdf=" + pdf, "file://" + os.path.abspath(out)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
            print("wrote " + pdf if os.path.isfile(pdf) else "export-pack: PDF was not created")
    print("problems: %d" % len(PROBLEMS))
    return 1 if PROBLEMS else 0


if __name__ == "__main__":
    sys.exit(main())
