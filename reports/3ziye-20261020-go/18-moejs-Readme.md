<div align="center">

<img src="docs/assets/moejs-logo.svg" width="160" alt="moejs">

# moejs

A JavaScript runtime in pure Go, for running JavaScript plugins inside Go programs.

<p align="center">
  <a href="./README.zh_CN.md">简体中文</a> |
  <strong>English</strong>
</p>

</div>

moejs supports modern JavaScript, including ES modules, classes,
async/await, Proxy and BigInt, and passes all 79,385 test262 tests it runs.

On the same plugins as Sobek, another pure-Go engine, a moejs call takes
about half the time and a runtime uses about a third of the memory, so a
server can give every concurrent request its own runtime.

## Performance

<p align="center">
  <img src="docs/assets/plugin-bench.en.png" alt="moejs plugin benchmark: throughput on small task-plugin calls, 100k-token agent requests and 8 MiB image requests, and memory in use at 32 workers">
</p>

The chart runs new-api's plugin workloads on the engines a Go program can
embed: small task-plugin calls, 100k-token coding-agent requests that a plugin
rewrites for the upstream, and requests that carry an 8 MiB image. QuickJS
called straight from C is shown in grey for reference. How it was measured is
in [docs/performance.md](docs/performance.md#plugin-scenarios).

The table below times single calls on new-api's 10 task plugins and 269
recorded calls, on the Go caller's side, including converting the arguments
and the result.

| | moejs | Sobek | QuickJS pure Go (modernc) | QuickJS (quickjs-go, default settings) | V8 (v8go) |
|---|--:|--:|--:|--:|--:|
| One plugin call | 6.9 µs | 14.3 µs | 35.2 µs | 104.5 µs | 56.6 µs ¹ |
| New runtime | 1.4 µs | 2.2 µs | 180 µs | 382 µs | 1,153 µs ¹ |
| Memory per runtime with the largest plugin loaded | 81 KiB | 264 KiB | 227 KiB ³ | 348 KiB ² | 1,544 KiB ² |

¹ V8's timings varied widely on the test machine. ² The engine's own heap.
³ How much the resident set grew: modernc.org/quickjs allocates outside the
Go heap and keeps no in-use count.

Sobek and modernc.org/quickjs, which is QuickJS translated to Go, are pure-Go
engines like moejs. quickjs-go and V8 run through cgo. The test machine, the
full results and how to reproduce them are in
[docs/performance.md](docs/performance.md).

## Features

### Pure Go

moejs builds with `CGO_ENABLED=0` and cross-compiles without a C toolchain.
The engine is ordinary Go code, so pprof and the race detector see inside it.

### Passing values

Plugin functions take Go maps, slices, structs and named types, or JSON.
moejs converts a map one level at a time, as far as the plugin reads it, and
JSON text in a `json.RawMessage` the same way. Results come back as Go values
or JSON, or go straight into your own struct with the same result as
`json.Unmarshal`. A `json.RawMessage` field receives the JSON text of its part
of the result, and `DecodeOptions` caps the size of a result before anything
is decoded. Host functions are plain Go functions, and one can return a
promise and settle it later from Go.

### What a plugin can reach

A plugin sees the JavaScript standard library and the globals you install.
Every `import` and `import()` goes through a Go function you provide, and
`eval` and `new Function` can be capped in length or turned off. Builtins are
frozen and shared by every runtime, so every plugin sees the same
`Array.prototype`. Each runtime has its own globals and time zone, and a host
can give a runtime its own mutable copy of the builtins for plugins that
patch them.

### TypeScript

`CompileTS` runs a TypeScript module the way Node strips types: the parser
drops the type syntax, so errors and stack traces point into the TypeScript
source. Enums, namespaces with values and other TypeScript that changes what
the code does at run time fail with a `*SyntaxError`.

### Timers and the event loop

A bare runtime has no timers. The `eventloop` package adds `setTimeout`,
`setInterval` and `setImmediate`, and an event loop on which host functions
settle promises from other goroutines.

### Timeouts and errors

Any goroutine can interrupt a running plugin, even one stuck in an endless
loop. A JavaScript throw, a syntax error, an interrupt and a panic in a host
function each come back as their own Go error type, and a thrown `Error` has
a V8-style stack trace. A runtime stays usable after a host function panics.

### Memory limit

`Options.MemoryLimit` caps what one request's JavaScript allocates. A plugin
that goes past it stops with an error that carries its JavaScript stack, and
the script cannot catch it. `Stats` reports a runtime's allocations and other
counters.

## Quick start

```sh
go get github.com/Calcium-Ion/moejs
```

moejs needs Go 1.25 or later and depends only on the standard library (tests
use testify).

```go
package main

import (
	"context"
	"errors"
	"fmt"
	"runtime"
	"sync"
	"time"

	"github.com/Calcium-Ion/moejs"
)

const source = `
export function buildRequest(task) {
  return {
    method: "POST",
    url: "https://api.example.com/v1/tasks",
    headers: { autho