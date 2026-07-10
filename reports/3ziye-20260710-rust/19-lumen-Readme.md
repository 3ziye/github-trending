# lumen

A from-scratch JavaScript **engine** in Rust — std only, zero dependencies — and a
**runtime** being built on top of it, the way Node/Deno/Bun wrap a JS engine with an event
loop and host APIs. Every crate in the workspace is std-only: no `tokio`, `mio`, `libc`,
`rustyline`, `serde`, or any other third-party dependency, anywhere.

## The engine (`crates/lumen`)

A lexer, parser, and **three execution tiers**:

- a **tree-walking interpreter** — the reference oracle: the spec semantics live here, and
  every other tier must match it observably (a differential fuzzer, `lumen-difftest`, holds
  them to that);
- an opt-in **bytecode VM** — functions compile whole (or not at all — no deoptimization) to
  a stack machine with slot-homed locals, per-site inline caches for property and free-name
  access backed by object shapes (hidden classes), and dense-array element fast paths;
- an **ARM64 template JIT** (macOS/Apple Silicon) — bytecode lowers to real machine code:
  per-op templates with the interpreter as the shared slow path, inline-cache reads baked
  into the instruction stream, fused compare-and-branch, exact-`ToInt32` bitops, and numeric
  *register chains* that keep runs of arithmetic entirely in FP registers. On other
  platforms the JIT tier degrades to the bytecode VM.

Tier selection: `--tier=interp|bytecode|jit` (interp is the default). Functions tier up
after a call-count threshold — immediately if the body contains a loop.

The language surface: generators and `async`/`await` running on stackful coroutines (async
bodies suspend on the bytecode VM itself), full `RegExp` (including `\p{…}` and inline
modifiers), typed arrays, `Proxy`/`Reflect`, ES modules (top-level await, `import defer`,
source phase), `Intl`, and `Temporal`.

`Intl` (ECMA-402) and its CLDR data tables are behind the default-on `intl` cargo feature —
the largest single contributor to binary size (~3 MB of the release binary). Build with
`--no-default-features` for a small engine: the `Intl` global is absent and the `toLocale*`
methods degrade to their locale-independent forms, the way engines built without i18n do.

On dependencies and `unsafe`: the workspace stays std-only — the JIT maps executable memory
through raw `extern "C"` declarations of `mmap`/`pthread_jit_write_protect_np` rather than
libc. The interpreter and bytecode VM are safe Rust; `unsafe` is concentrated where machine
code meets the object graph (the JIT's executable pages and its templates' raw reads — every
baked offset is *measured at runtime* against the live types and fails closed to the checked
helper if anything doesn't hold) and in the N-API addon loader's `dlopen` bridge.

**Passes 100% of [tc39/test262](https://github.com/tc39/test262): 53,400/53,400** (including
annexB, intl402, and staging) — on the default tier and under `LUMEN_TIER=jit`.

Extracted from — and used by — the [lucid-softworks/browser](https://github.com/lucid-softworks/browser)
engine as its JS backend (`backend-lumen`), with full git history.

## The runtime

A curated `embed` API on the engine exposes just enough — native-function registration, a
typed host-state slot, and event-loop hooks — for a runtime layer to be assembled from
independent op crates, without leaking the interpreter's internals into the published API.
On top of that:

- **Event loop** (`lumen-runtime`) — a single loop thread owns the (`!Send`) engine; blocking
  work runs on a std thread pool and completes back over `mpsc`. No epoll/kqueue reactor
  (that would need raw syscalls); the thread-pool-plus-completion model is libuv's own fs
  strategy. Each turn drains microtasks, queued callbacks, due timers, and I/O completions,
  then blocks until the next event.
- **Timers** (`lumen-timers`) — `setTimeout`/`setInterval`/`clearTimeout`/`clearInterval`/
  `setImmediate`, plus `queueMicrotask`.
- **`console` and `process`** — streaming `console.*`; `process.argv`/`env`/`platform`/
  `cwd()`/`exit()`/`nextTick()`.
- **Filesystem** (`lumen-fs`) — synchronous ops (`readFileSync`, `writeFileSync`,
  `existsSync`, `mkdirSync`, `readdirSync`, …), file handles via a resource table
  (`openSync`/`readSync`/`writeSync`/`closeSync`), and async `fs.promises.readFile`/
  `writeFile` on the thread pool.
- **Web platform** (`lumen-web`) — a growing slice of the WinterTC Minimum Common API:
  `Event`/`EventTarget`/`CustomEvent`/`AbortController`/`AbortSignal`/`DOMException`,
  `TextEncoder`/`TextDecoder`, `atob`/`btoa`, `structuredClone`, `URL`/`URLSearchParams`,
  `performance.now()`, `crypto.getRandomValues`/`randomUUID`/`subtle.digest` (SHA-256), and
  `fetch`/`Headers`/`Request`/`Response`. See the checklist at the top of
  `crates/lumen-web/src/lib.rs` for what's implemented vs. deferred (streams, `Blob`/
  `FormData`, `URLPattern`, …).

  `fetch` speaks HTTP/1.1 over `std::net`. **`https:` is not supported**: TLS cannot be
  implemented on std alone and no third-party crate is permitted, so `https` URLs reject with
  