<p align="center">
  <img src="https://nubjs.com/icon-border.svg" width="200px" align="center" alt="Nub logo" />
  <h1 align="center">Nub</h1>
  <p align="center">
    A fast all-in-one toolkit that augments Node.js instead of replacing it
  </p>
</p>

<div align="center">
  <a href="https://nubjs.com/docs">Docs</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://github.com/nubjs/nub">GitHub</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://x.com/colinhacks">𝕏</a>
  <br/><br/>
</div>

<p align="center">
<a href="https://github.com/nubjs/nub" rel="nofollow"><img src="https://nubjs.com/stars.svg" alt="stars"></a>
</p>



<br/>
<br/>

A Bun-like DX on top of stock `node`, written in Rust.


```sh
nub index.ts             # TypeScript-first Node.js runtime
nub run dev              # 24× faster pnpm run
nubx prisma generate     # 19× faster npx
nub install              # 2.5× faster pnpm install
nub watch src/server.ts  # native watch mode
nub pm shim              # built-in Corepack-style shims
nub node install 26      # Node version manager
nub upgrade              # self update
```

One tool to run your files and scripts, install dependencies, and manage Node itself. No new runtime, no vendor-specific API surface, no lock-in.

| Nub | Instead of |
|---|---|
| `nub <file>` | `node`, `tsx`, `ts-node`, `dotenv-cli` |
| `nub run <script>` | `npm run`, `pnpm run` |
| `nubx` | `npx`, `pnpm dlx / exec` |
| `nub install` | `npm`, `pnpm` |
| `nub watch` | `nodemon`, `node --watch`, `tsx watch` |
| `nub node` | `nvm`, `fnm`, `n`, `volta` |
| `nub pm` | `corepack` |

<br/>

## Install

```sh
# macOS / Linux
curl -fsSL https://nubjs.com/install.sh | bash

# Windows (PowerShell)
irm https://nubjs.com/install.ps1 | iex

# Homebrew (macOS / Linux)
brew install nubjs/tap/nub

# Or via npm (pnpm / yarn global add work too)
npm install -g --ignore-scripts=false @nubjs/nub
```

For GitHub Actions, use [`nubjs/setup-nub`](https://github.com/nubjs/setup-nub) in place of `actions/setup-node`. It's one-to-one compatible.

```diff
- - uses: actions/setup-node@v4
+ - uses: nubjs/setup-nub@v0
```

<br/>

## File runner — `nub <file>`

Run a file. Supports `.js`, `.ts`, `.mjs`, `.cjs`, `.mts`, `.cts`, `.jsx`, and `.tsx`. Flag-for-flag and var-for-var drop-in compatible with `node` (mostly via passthrough).

```sh
nub index.ts             # TypeScript, JSX, no build step
nub --watch app.ts       # same path, restart-on-change
```

It augments stock Node with some of Bun/Deno's best features:

- 🦆 Full TypeScript support, including `enum`, `namespace`
- 🧭 TypeScript-friendly resolution: extensionless imports, `tsconfig.json#paths`
- ⚛️ JSX / TSX
- 🎂 Decorators and `emitDecoratorMetadata`
- 🆕 Modern syntax like `using` (downleveled in transpiler when needed)
- 🔐 Automatic `.env*` loading — Next.js/Vite parity
- 🗂️ Built-in loaders for common data formats — `.yaml`, `.toml`, `.jsonc`, `.json5`, `.txt`
- 🌐 Polyfills for `Temporal`, `Worker`, `URLPattern` (when needed)
- 🔥 Unflags experimental features like `node:sqlite`, `vm.Module`, `localStorage`, `WebSocket`, `EventSource`
- ⚡ 2.9× faster startup than `tsx`

> **How it works** — Nub takes advantage of Node extension surfaces that mostly didn't exist when Deno and Bun were built: 
> 
> - [`--import`](https://nodejs.org/api/cli.html#--importmodule)/[`--require`](https://nodejs.org/api/cli.html#-r---require-module) preloads
> - [`module.registerHooks()`](https://nodejs.org/api/module.html#moduleregisterhooksoptions) for transpilation and resolution 
> - [N-API native addons](https://nodejs.org/api/n-api.html): Nub embeds [oxc](https://oxc.rs/) for pre-transpilation


### Node provisioning

When you run a file with nub, it infers the version of Node your project expects and auto-installs it if needed. It respects (in precedence order):

- `NODE_EXECUTABLE` (override)
- `package.json#devEngines`
- `.node-version`
- `.nvmrc`
- `package.json#engines`

This resolved version of Node is installed and your file is executed with it (with Nub's augmentations).

```sh
$ echo 26 > .node-version
$ nub hello.ts
Using Node.js 26.3.0 (resolved from .node-version)
Installed in 9.8s
Hello world!
```

### Modern APIs

Modern API work out of the box under Nub. Node.js experimental APIs are unflagged, others are auto-polyfilled (e.g. `Temporal` on Node 25 and earlier), and others are downleveled in the transpiler (`using`).

| API | How |
|---|---|
| [`Temporal`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal) | polyfilled below Node 26, native above |
| [`URLPattern`](https://developer.mozilla.org/en-US/docs/Web/API/URLPattern) | polyfilled below Node 24, native above |
| [`RegExp.escape`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/escape) | polyfilled below Node 24, native above |
| [`Error.isError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/isError) | 