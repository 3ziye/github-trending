# channels-console 
[![Latest Version](https://img.shields.io/crates/v/channels-console.svg)](https://crates.io/crates/channels-console) [![GH Actions](https://github.com/pawurb/channels-console/actions/workflows/ci.yml/badge.svg)](https://github.com/pawurb/channels-console/actions)

![Console TUI Example](channels-console-tui5.gif)

A lightweight, easy-to-use tool for real-time visibility into your Rust channels. Inspect live message contents and observe how channels interact to better understand data flow. Track queue depth, delay, throughput, and memory usage to spot channel-related issues.

Supports [std::sync](https://doc.rust-lang.org/stable/std/sync/mpsc/index.html), [Tokio](https://github.com/tokio-rs/tokio), [futures-rs](https://github.com/rust-lang/futures-rs), and [crossbeam](https://github.com/crossbeam-rs/crossbeam) channels - with more on the way.

## Features

- **Zero-cost when disabled** — fully gated by a feature flag
- **Minimal configuration** - just one `instrument!` macro to start collecting metrics
- **Detailed stats** - per channel status, sent/received messages, queue capacity, and memory usage 
- **Background processing** - minimal profiling impact
- **Live monitoring** - view metrics in a clear, real-time TUI dashboard (built with [ratatui.rs](https://ratatui.rs/))

## Getting started

`Cargo.toml`

```toml
channels-console = { version = "0.3", optional = true, features=['tokio', 'futures', 'crossbeam'] }

[features]
channels-console = ["dep:channels-console"]
```

This config ensures that the lib has **zero** overhead unless explicitly enabled via a `channels-console` feature.

[std::sync](https://doc.rust-lang.org/stable/std/sync/mpsc/index.html) channels can be instrumented by default. Enable `tokio`, `futures`, or `crossbeam` features for [Tokio](https://github.com/tokio-rs/tokio), [futures-rs](https://github.com/rust-lang/futures-rs), and [crossbeam](https://github.com/crossbeam-rs/crossbeam) channels, respectively.

Next use `instrument!` macro to monitor selected channels:

```rust
let (tx1, rx1) = tokio::sync::mpsc::channel::<i32>(10);
#[cfg(feature = "channels-console")]
let (tx1, rx1) = channels_console::instrument!((tx1, rx1));

let (mut txb, mut rxb) = futures_channel::mpsc::channel::<i32>(10);
#[cfg(feature = "channels-console")]
let (mut txb, mut rxb) = channels_console::instrument!((txb, rxb), capacity = 10);
```

Futures and `std::sync` bounded channels don't provide an API exposing their size, so you have to provide `capacity` to the `instrument!` macro.

This is the only change you have to do in your codebase. `instrument!` macro returns exactly the same channel types so it remains 100% compatible.

Now, install `channels-console` TUI:

```bash
cargo install channels-console --features=tui
```

Execute your program with `--features=channels-console`:

```bash
cargo run --features=channels-console
```

In a different terminal run `channels-console` CLI to start the TUI and see live usage metrics:

```bash
channels-console
```

![Console Dashboard](console-dashboard5.png)

### Quickstart demo guide

1. Install CLI:

```bash
cargo install channels-console --features=tui
```

2. Clone this repo:

```bash
git clone git@github.com:pawurb/channels-console.git
```

3. Run `console_feed` example:

```bash
cd channels-console
cargo run --example console_feed_tokio --features=channels-console
```

4. Run TUI (in a different terminal):

```bash
channels-console
```

## How it works?

`instrument!` wraps Tokio channels with lightweight proxies that transparently forward all messages while collecting real-time statistics. Each `send` and `recv` operation passes through a monitored proxy channel that emits updates to a background metrics system.

In the background a HTTP server process exposes gathered metrics in a JSON format, allowing TUI process to display them in the interface.

### A note on accuracy

`channels-console` instruments proxy channels that wrap your actual channel instances. It observes messages as they pass through these proxies rather than when they are finally consumed. As a result, the displayed metrics are an approximation of real channel activity - useful for debugging and diagnosing flow issues, but not a 100% accurate source of truth for production monitoring.

Because of this proxy design, each bounded channel is effectively represented by three layers - the outer proxy, the original channel, and the inner proxy. In practice, this triples the total buffering capacity. For the same reason, it's currently not possible to measure the queue size of unbounded channels. Even with a slow consumer, the intermediate proxies will immediately absorb all incoming messages, masking true backlog behavior.

That said, since the proxy layer introduces virtually no overhead compared to direct channel usage, timing and delay metrics should remain accurate. Logged messages contents and ordering is also 100% accurate. 

Current design intentionally sacrifices accuracy for