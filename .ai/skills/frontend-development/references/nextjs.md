# Frontend Development – Next.js (App Router) and React

> Áp dụng cho: Next.js 16.x App Router, React 19.2+.

Project conventions (api-design, security-standards, cache-rules, Design System) win over anything here.

## 1. Next.js 16 version differences (steps 2, 3)

AI often writes Next.js 13–15 code. In 16:
- `cookies()`, `headers()`, `draftMode()` and the `params`/`searchParams` props are async only (typed `Promise<…>`); synchronous access is removed. Use `await`, or `use()` in a client component.
- `middleware.ts` is deprecated, renamed to `proxy.ts`; proxy always runs on Node.js (no `edge`, not configurable). Code needing `edge` stays in `middleware`; follow what the codebase uses.
- `revalidateTag(tag)` without the second `cacheLife` profile argument is deprecated (type error). For read-your-writes in a Server Action use `updateTag`.
- Every parallel-route slot needs an explicit `default.js`, otherwise the build fails.
- Removed: `next lint` (run ESLint/Biome directly; `next build` no longer lints), `serverRuntimeConfig`/`publicRuntimeConfig` (use env vars), `experimental.dynamicIO` (now top-level `cacheComponents`), AMP.
- Before writing an API you are unsure of, read `node_modules/next/dist/docs/` of the installed version.

## 2. Server and client boundary (steps 3, 5)

- Module scope on the server is shared by all concurrent requests: never store request or user data in a module-level variable in RSC/SSR code; pass it through props.
- Everything passed from a server to a client component is serialized into the HTML/RSC payload: pass only the fields the client uses, never a whole DB/ORM entity (leaks fields, bloats the page). Mark server-only modules with `import 'server-only'`.
- Server-to-client serialization deduplicates by reference: passing both `list` and `list.filter(…)` sends the data twice; derive on the client unless the transform is expensive.
- Only `NEXT_PUBLIC_*` env vars reach the client; never give a secret that prefix.

## 3. Data fetching without waterfalls (step 5)

- Independent awaits run in sequence by default: start promises first, then `Promise.all`; in Route Handlers and Server Actions start auth and config fetches together.
- Do not `await` at the top of a page when only part of it needs the data: move the fetch into the async child and wrap it in `<Suspense>`, or pass the un-awaited promise and read it with `use()`.
- `React.cache()` dedupes non-`fetch` work (DB call, auth check) within one request only; arguments are compared with `Object.is`, so an inline object argument never hits. `fetch` GET is already memoized per render, but not in Route Handlers.
- Next.js caching (`'use cache'`, `cacheLife`/`cacheTag`, `revalidateTag`, `unstable_cache`) is a data cache subject to cache-rules; add it only where the plan or design states it.
- `after()` runs work after the response, and also runs when the response errored, redirected or called `notFound`. Inside `after()` a Server Component cannot call `cookies()`/`headers()`; read them before and pass the values in.

## 4. Server Actions and Route Handlers (steps 4, 6)

- A `'use server'` function is a public POST endpoint reachable without the UI: inside **each** action validate input, authenticate and authorize. A check in proxy, layout or page, or hiding the form, is not a security boundary.
- A Route Handler gets the same checks as any API endpoint, per api-design and security-standards.

## 5. Rendering and hydration (step 3)

- Server and first client render must match: do not read `window`/`localStorage`, `Date.now()`, random values or locale formatting during render. `suppressHydrationWarning` only for an expected mismatch on one element, never to hide a bug.
- `{count && <X/>}` renders `0` when `count` is 0; use a ternary or a boolean condition.
- Never declare a component inside another component: it remounts on every render (inputs lose focus, state resets). Hoist it and pass props.
- Derive values from props/state during render; do not copy them into state via `useEffect`.
- Do not put the function returned by `useEffectEvent` in an effect's dependency array.
- If React Compiler is enabled (`reactCompiler` in `next.config`), do not add manual `memo`/`useMemo`/`useCallback`; follow what the codebase does.

## 6. Bundle (step 3)

- Heavy, below-the-fold or rarely used client components: `next/dynamic`.
- Barrel imports from large libraries load the whole package; common ones (`lucide-react`, `date-fns`, `@mui/material`, `lodash-es`…) are already optimized by default. For others, prefer `experimental.optimizePackageImports` over deep import paths, which may lack types; changing `next.config` needs the plan.
- `import()` and `fs` paths must be static literals or an explicit map, so the bundle and file tracing do not include every possible file.
