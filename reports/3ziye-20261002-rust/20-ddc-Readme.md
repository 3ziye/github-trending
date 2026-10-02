# ddc — DEX → Java decompiler in Rust

**English** | [简体中文](README.zh-CN.md)

[![CI](https://github.com/ejfkdev/ddc/actions/workflows/ci.yml/badge.svg)](https://github.com/ejfkdev/ddc/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

`ddc` decompiles Android DEX bytecode back into readable Java — at
real-world app scale, queryable like a database, and **javac-verified**:
every one of the 909,689 files it emits across seven real-world APKs
parses cleanly.

## Highlights

- **Fast** — a 226 MB / 20-dex APK (weibo, 98k classes) fully
  decompiles in **~13s** at high quality, a 62 MB app (Telegram) in
  **~4.5s**; pathological classes run on deadline-bounded monitored
  threads instead of hanging the run.
- **Compiles** — the full output of all seven benchmark APKs
  (reqable, Telegram, WhatsApp, weibo, weixin, qq, lark — 0.91M
  files) passes `javac` with **zero syntax errors**; every class of
  a case-variant name pair (`X/Cua` vs `X/cua`) is preserved as
  its own file instead of the last one silently overwriting.
- **Progressive decompilation** — 20+ query subcommands (strings,
  cross-references, hierarchies, manifest, resources, per-method
  decompiles) answer in milliseconds: query metadata first, decompile
  on demand, skip the full run entirely.
- **DEX 035–041, complete** — multi-dex APKs, XAPK/APKS/APKM
  containers, invoke-custom; lambdas and string concats fold back into
  real Java (`(a) -> …`, `Cls::name`, `a + b`).
- **Readable output** — jadx-style local names (`str`, `getName() →
  name`, Kotlin `Intrinsics` parameter strings) instead of `v12`;
  IntDef literals render as their constants out of the box
  (`setVisibility(8)` → `View.GONE`; a built-in android-37 domain
  table, `--symbols` overrides); Kotlin null-check noise is elided and
  synthetic `access$NNN` bridges inline at their call sites.
- **Reproducible output** — no timestamps; two runs diff cleanly.
- **Bilingual CLI** — messages localize automatically
  (`DDC_LANG=zh|en` forces; English fallback).
- Built on [`jdc-core`](https://crates.io/crates/jdc-core), the
  machine-neutral core shared with
  [jcdc](https://github.com/ejfkdev/jcdc).

## Install

**macOS** (Homebrew):

```bash
brew install ejfkdev/tap/ddc
```

**Windows** (Scoop) — add the bucket once, then install by name (scoop
does not resolve a bare `user/repo/app` form — issue #3):

```powershell
scoop bucket add ejfkdev https://github.com/ejfkdev/scoop-bucket
scoop install ddc

# or install straight from the manifest URL, no bucket needed:
scoop install https://raw.githubusercontent.com/ejfkdev/scoop-bucket/main/bucket/ddc.json
```

**cargo-binstall** (any platform — fetches the prebuilt release binary
instead of compiling):

```bash
cargo binstall ddc-cli
```

**Binaries**: every [release](https://github.com/ejfkdev/ddc/releases)
ships raw binaries (no archives) for `linux-amd64`, `linux-arm64`,
`windows-amd64`, `windows-arm64`, `macos-amd64` and `macos-arm64` —
non-macOS builds UPX-compressed.

**From source** (Rust stable):

```bash
git clone https://github.com/ejfkdev/ddc && cd ddc
cargo build --release
```

## Usage

```bash
ddc app.apk                          # full decompile → app-out/
ddc app.apk -c com.example.Foo       # one class to stdout
ddc app.apk -o - | less              # everything to stdout

ddc info app.apk                      # app context (label via arsc, package,
                                      # version, md5) + per-dex counts
ddc mainactivity app.apk             # entry point: package + launcher
ddc findrefs app.apk string token    # every const-string "token" site
ddc getmethod app.apk Foo.toString   # one method, all overloads
ddc pkg app.apk --app -o own/        # the app's own code only
```

Full options and examples: `ddc --help` (subcommand menu grouped by
workflow). The complete reference — every option's semantics, every
subcommand's output format and behavior — lives in
[docs/cli.md](docs/cli.md) ([中文](docs/zh-CN/cli.md)).

## Performance

Seven real-world APKs, release build, 3-run averages
(Apple Silicon, 6P+12E). The 39-APK validation corpus (4.08M
decompiled files, per-APK wall time / peak RSS / javac parse gate) is
in [docs/validation.md](docs/validation.md)
([中文](docs/zh-CN/validation.md)).

<details>
<summary>Full decompile — 7 real-world APKs</summary>

| APK | Size | Full decompile | Peak RSS |
|---|---|---|---|
| reqable | 34 MB | **0.57s** | 162 MB |
| Telegram | 62 MB | **4.50s** | 786 MB |
| WhatsApp | 139 MB | **29.8s** (99,277 files — case-variant class pairs all preserved) | 970 MB |
| weibo | 226 MB | **13.5s** | 1173 MB |
| weixin | 268 MB | **32.7s** | 1401 MB |
| lark | 398 MB | **16.1s** | 2226 MB |
| qq | 374 MB | **37.1s** | 2268 MB |

</details>

Query subcommands on the same APKs (cells: time / peak RSS;
`strings -f <package> --with-locations`, `findrefs` on the package
string and method `onCreate`, `hierarchy`/`disasm`/`getclass` on each
app's launch