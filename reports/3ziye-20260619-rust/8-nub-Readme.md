# Nub

An all-in-one toolkit for Node.js. One Rust binary to run your files and scripts, install dependencies, and manage Node itself — a Bun-like modern DX on top of the `node` you already have. There's no new runtime to adopt and no lock-in: every augmentation rides on Node's own public extension surfaces.

**Documentation:** https://nubjs.com/docs

```sh
# macOS / Linux
curl -fsSL https://nubjs.com/install.sh | bash

# Windows (PowerShell)
irm https://nubjs.com/install.ps1 | iex

# Or via npm (pnpm / yarn global add work too)
npm install -g --ignore-scripts=false @nubjs/nub
```

That puts `nub` and `nubx` on your `PATH`.

For GitHub Actions, use [`nubjs/setup-nub`](https://github.com/nubjs/setup-nub) in place of `actions/setup-node`:

```diff
- - uses: actions/setup-node@v4
+ - uses: nubjs/setup-nub@v1
```

It installs Nub, can pre-provision the project's Node, and can cache Nub's store.

## Quickstart

```sh
nub index.ts             # run a TypeScript file on stock Node
nub run dev              # run a package.json script (~24× faster than pnpm run)
nubx prisma generate     # run a CLI from node_modules/.bin (~19× faster than npx)
nub install              # install dependencies (pnpm-shaped, lockfile-compatible)
nub watch src/server.ts  # restart on file changes
nub pm shim              # route bare npm/pnpm/yarn through the project's pin
nub node install 22      # provision a Node version
```

## The toolkit

### File runner — `nub <file>`

A flag-for-flag drop-in for `node <file>` that also runs TypeScript and JSX directly — no tsconfig, no build step. The whole TS surface works, including non-erasable syntax (`enum`, `namespace`, parameter properties) and legacy decorators with `emitDecoratorMetadata`. Imports resolve the way your editor does (extensionless, `.js → .ts`, tsconfig `paths`), `.env*` files load automatically with `${VAR}` expansion, and data files import as parsed values:

```ts
import config from "./config.yaml";  // .yaml, .toml, .jsonc, .json5, .txt — default import
```

Modern globals are present even on older Node — `Temporal`, `URLPattern`, `WebSocket`, `EventSource`, `node:sqlite`, Web Workers, and more — each polyfilled (feature-detected, native wins) or flag-injected per Node-version band. Source maps surface in error traces. `sessionStorage` works out of the box; persistent `localStorage` is opt-in (it needs a backing file). See [Runtime](https://nubjs.com/docs/runtime).

### Script runner — `nub run`

A drop-in for `npm run` and `pnpm run`, roughly 24× faster on the cold path. Lifecycle `pre`/`post` hooks, the full `npm_*` environment, `node_modules/.bin` on `PATH`, and arg-forwarding without the `--` separator. The complete pnpm workspace surface is preserved — `-r` / `--recursive`, `--filter` (pnpm's grammar verbatim, including graph and changed-since selectors), `--parallel`, `--workspace-concurrency`, `--resume-from`, `--stream`. See [Script runner](https://nubjs.com/docs/run).

```sh
nub run build
nub run -r --filter "@org/*" test
```

### Package runner — `nubx` / `nub dlx`

A drop-in for `npx` and `pnpm dlx`, local-first with a registry fallback. It resolves `node_modules/.bin` in Rust and exec's the binary directly, so the per-call Node bootstrap that `npx` pays disappears (~19× lighter). When a bin isn't installed, `nubx` fetches and runs it. See [Package runner](https://nubjs.com/docs/nubx).

```sh
nubx eslint . --fix
nubx cowsay@1.5.0 "hi"   # fetched from the registry, then discarded
```

### Package manager — `nub install`

Nub has its own pnpm-shaped install engine (the vendored [aube](https://github.com/jdx/aube) engine, embedded as a library). The CLI follows pnpm's spellings; the lockfile stays in your project's native format — npm, pnpm, and Bun round-trip cleanly, Yarn is read-only. Nub infers the incumbent package manager and mirrors it; it never asks. Packages dedupe through a global content-addressed store and materialize by reflink/hardlink.

```sh
nub install                    # alias: nub i  ·  also: nub ci, --frozen-lockfile
nub add -D vitest              # add / remove / update / dedupe / import
nub remove lodash
```

Dependency build scripts are **deny-by-default**: a script runs only on an explicit allow (`pnpm.onlyBuiltDependencies`, `trustedDependencies`, `nub approve-builds`) or when a curated default-trust floor vouches for it under registry-provenance, advisory-vetting, and cooling-window gates. See [Package manager](https://nubjs.com/docs/install).

### Package meta-manager — `nub pm`

Corepack's job, in native Rust: provision and run the exact pnpm / npm / yarn your project pins. Nub reads the pin (`packageManager`, `devEngines`, or Yarn Berry's `yarnPath`), fetches that version integrity-verified, caches it, and runs it on the project's Node — no `corepack enable`, no baked version table.

```sh
nub pm use pnpm@9.15.4   # declare the project's PM, align the lockfile
nub pm shim              # bare npm/pnpm/yarn route through the pin
```

