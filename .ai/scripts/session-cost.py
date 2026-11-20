"""Estimate the USD cost of an AI session from its Claude Code transcript.

Use when `/cost` or Account & Usage is not available (runs.md "Dòng Phiên điều phối").
Result is an estimate from tokens, never an invoice: say so in runs.md.

Usage (-I keeps Python from importing files in the repo):
  python3 -I .ai/scripts/session-cost.py <transcript.jsonl> [--from ISO] [--to ISO] [--expect USD]

Transcripts: ~/.claude/projects/<project>/<session-id>.jsonl. Timestamps in them are UTC
(e.g. 2026-11-19T08:32:46); --from/--to cut the session to one Plan (first and last commit
of the Plan, converted to UTC). Only counts are read; conversation content is never printed.
--expect USD: calibration. Run the script on a Run whose JSON gives total_cost_usd and pass that
number: exit 1 when the estimate differs by more than 3%. Calibrate before trusting a new price table.

Rules this script encodes (each one was a real mistake):
- A message appears on several lines (one per content block) with the same usage: count it once, by message id.
- Four token kinds, each at its own price: input, output, cache read, cache write. Cache write is
  split by duration: 5 minutes (1.25x input) and 1 hour (2x input).
- Haiku 5.5 prompts over 100K tokens cost 5x. A long session almost always passes it.
"""
import argparse
import json
import sys

PRICES_DATE = "2026-11-03"   # update with the price table; runs.md names the date used
# USD per 1M tokens: input, output, cache read, cache write 5m, cache write 1h
PRICES = {
    "claude-opus-5-5": (4.0, 20.0, 0.20, 5.0, 8.0),
    "claude-sonnet-5-5": (2.0, 10.0, 0.10, 2.5, 4.0),
    "claude-haiku-5-5": (0.10, 0.50, 0.01, 0.125, 0.20),
}
HAIKU_LONG = (0.50, 2.50, 0.05, 0.625, 1.0)   # prompt over 100K tokens
LONG_PROMPT = 100_000


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("--from", dest="start", default="")
    ap.add_argument("--to", dest="end", default="~")
    ap.add_argument("--expect", type=float)
    a = ap.parse_args()

    msgs = {}
    for line in open(a.transcript, encoding="utf-8"):
        try:
            o = json.loads(line)
        except ValueError:
            continue
        m = o.get("message")
        if o.get("type") != "assistant" or not isinstance(m, dict) or not m.get("usage"):
            continue
        t = o.get("timestamp", "")
        if a.start <= t < a.end:
            msgs[m.get("id") or t] = (m.get("model"), m["usage"])

    stats, unknown = {}, set()
    for model, u in msgs.values():
        cc = u.get("cache_creation") or {}
        w1h = cc.get("ephemeral_1h_input_tokens", 0)
        v = (u.get("input_tokens", 0), u.get("output_tokens", 0), u.get("cache_read_input_tokens", 0),
             u.get("cache_creation_input_tokens", 0) - w1h, w1h)
        price = PRICES.get(model)
        if price is None:
            unknown.add(model)
            continue
        long_prompt = False
        if model == "claude-haiku-5-5" and v[0] + v[2] + v[3] + v[4] > LONG_PROMPT:
            price, long_prompt = HAIKU_LONG, True
        s = stats.setdefault(model, dict(calls=0, input=0, output=0, cache_read=0, cache_write=0, long_calls=0, usd=0.0))
        s["calls"] += 1
        s["input"] += v[0]
        s["output"] += v[1]
        s["cache_read"] += v[2]
        s["cache_write"] += v[3] + v[4]
        s["long_calls"] += long_prompt
        s["usd"] += sum(x * p for x, p in zip(v, price)) / 1e6

    total = sum(s["usd"] for s in stats.values())
    print(f"prices: Anthropic API table {PRICES_DATE}; estimate from tokens, not an invoice")
    for model, s in stats.items():
        extra = f", {s['long_calls']} calls over 100K prompt (5x)" if s["long_calls"] else ""
        print(f"{model}: {s['calls']} calls, output {s['output']}, input {s['input']}, "
              f"cache read {s['cache_read']}, cache write {s['cache_write']}{extra} -> {s['usd']:.3f} USD")
    print(f"TOTAL {total:.3f} USD")
    if unknown:
        print(f"no price for model(s) {sorted(unknown)}: not counted; add them to PRICES", file=sys.stderr)
        return 1
    if a.expect is not None:
        ok = abs(total - a.expect) <= 0.03 * a.expect
        print(f"calibration: expected {a.expect:.3f}, got {total:.3f}: {'OK' if ok else 'DIFFERS'}")
        return 0 if ok else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
