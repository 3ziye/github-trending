<p align="center">
  <a href="https://aube.en.dev">
    <img src="assets/logo.svg" alt="aube logo" width="140" height="140">
  </a>
</p>

<h1 align="center">aube</h1>

<p align="center">
  A fast Node.js package manager that drops into existing projects.
</p>

<p align="center">
  <strong>aube</strong> means dawn in French. Pronounced <code>/ob/</code>, like "ohb".
</p>

<p align="center">
  <strong><a href="https://aube.en.dev">Read the docs</a></strong>
</p>

## Why Try It

<!-- BENCH_RATIOS:START -->
**[Fast installs](https://aube.en.dev/benchmarks).** Warm installs are about 5x faster than pnpm and about 4x faster than Bun in the current benchmarks. Repeat test commands run up to 14x faster than pnpm and up to 4x faster than Bun.
<!-- BENCH_RATIOS:END -->

**[Existing lockfiles](https://aube.en.dev/package-manager/lockfiles).** Reads and writes `pnpm-lock.yaml`, `package-lock.json`, `npm-shrinkwrap.json`, `yarn.lock`, and `bun.lock` in place.

**[Cheap repeat commands](https://aube.en.dev/package-manager/scripts).** `aubr test`, `aube test`, and `aube exec vitest` auto-install when dependencies are stale, then skip that work when nothing changed. `aubx` runs one-off tools in a throwaway environment.

**[Less disk use](https://aube.en.dev/package-manager/node-modules).** A global content-addressable store lets projects share package files instead of keeping a full copy of the same dependencies in every checkout.

**[Secure defaults](https://aube.en.dev/security).** Out of the box, exotic transitive deps are blocked, lifecycle scripts wait for approval, trust downgrades fail at resolve, and brand-new releases sit in a 24h cooling window. One `paranoid: true` line adds the build jail and turns the soft gates into hard fails.

## Install

The recommended path is mise:

```sh
mise use -g aube
```

mise can also manage the [Node.js versions](https://mise.jdx.dev/lang/node.html)
your projects need. If your projects already pin Node through `package.json`
(`devEngines.runtime`), `.nvmrc`, or `.node-version`, enable mise's
idiomatic version-file support for Node:

```sh
mise settings add idiomatic_version_file_enable_tools node
```

Check that it is on your `PATH`:

```sh
aube --version
```

Inside a project, you can also pin aube with mise:

```sh
mise use aube
```

aube is also published on npm:

```sh
npm install -g --ignore-scripts=false @endevco/aube
npx --ignore-scripts=false @endevco/aube --version
```

The npm package uses an install script to fetch native binaries for
performance. The npm commands above include the flag that keeps that
working even if your npm config disables scripts. We still recommend mise
for the smoothest install and runtime management path.

Homebrew installs come from the Endev tap:

```sh
brew install endevco/tap/aube
```

See [other install methods](https://aube.en.dev/installation).

## First Run

Run aube in an existing Node.js project:

```sh
aubr test
```

`aubr` is shorthand for `aube run`. Before it starts the script, aube checks
whether `node_modules` is fresh for the current `package.json` and lockfile.
If dependencies are missing or stale, it installs them first; otherwise it
goes straight to the script.

You usually do not need a separate `aube install` in day-to-day work. Run the
script or binary you actually wanted:

```sh
aubr build
aube test
aube exec vitest
aubx cowsay hi
```

Use `aube install` when the install itself is the task: first local setup
without running a script, updating a lockfile, Docker layers, production-only
installs, or CI flows.

If the project already has a supported lockfile, aube reads it and writes updates back to the same file. That makes it easy to try aube locally without forcing the rest of the team to switch package managers first.

For a new project with no lockfile, aube creates `aube-lock.yaml`.

## Daily Commands

```sh
aube add react            # add a dependency
aube add -D vitest        # add a dev dependency
aube remove react         # remove a dependency
aube update               # update dependencies within package.json ranges
aubr build                # run a package.json script, auto-installing first if needed
aube test                 # run the test script, auto-installing first if needed
aube exec vitest          # run a local binary, auto-installing first if needed
aubx cowsay hi            # run a package in a throwaway environment
aube install              # install only, for setup or lockfile/install modes
aube ci                   # clean, frozen install for CI
```

You can also run scripts directly:

```sh
aube dev
aube build
aube lint
```

If the script exists in `package.json`, aube treats that as `aube run <script>`.

### Shortcuts: `aubr` and `aubx`

`aubr` and `aubx` are multicall shims for `aube run` and `aube dlx`. They
share a binary with `aube` and dispatch purely on `argv[0]`, so every flag
that works on the full command also works on the shim:

```sh
aubr build            # aube run build
aubx cowsay hi  