# ts-rust (aka tsc-rs)

I wanted to see if LLMs could port the TypeScript compiler, checker and lsp to Rust. Turns out they can.

It [cost over $420,000](#how-did-this-go) in tokens to do it, but you could probably have done it for ~$20k (see below).

## Benchmark: T3 Code with Effect diagnostics

Full type check of [T3 Code](https://github.com/pingdotgg/t3code) with Effect diagnostics on.\*
Time is the sum of the medians for its five checked projects. Lower is faster. Bar length is
in proportion to time. See [Benchmark: T3 Code](#benchmark-t3-code) for the method and the run
without Effect diagnostics.

| Checker | Time | Relative time | Speed vs tsc 7 |
| --- | ---: | --- | ---: |
| `tsc-rs --fast` | 9.77s | █ | 4.35× |
| `tsc-rs` | 14.30s | ██ | 2.98× |
| `tsc` 7 | 42.55s | █████ | baseline |
| `bun check` | 59.24s | ███████ | 0.72× |
| `tsc` 6 | 191.00s | ████████████████████████ | 0.22× |

\* `tsc-rs` is 0.6.0 with Effect diagnostics built in. `tsc` 7 is from `@effect/tsgo`. The
`bun check` time adds a separate `effect-tsgo diagnostics` run. `tsc` 6 uses the JavaScript
Effect plugin.

## Motivations

- Test model capabilities
- Make a fast TypeScript type checker
- Make a ts checker that can work in WASM with high performance
- Memes

## Warnings

**This is an early release.** It has 100% compatibility in every real world project we have
tested. It should work as a drop in
replacement for the vast majority of apps. See [Known problems](#known-problems).

Also worth mentioning: I've never read a line of this code.

## Install

Be warned, I have no idea if this will actually work.

```sh
npm install -D tsc-rs
npx tsc-rs -p tsconfig.json
```

## How did this go?

I used a lot of OpenAI models to try and complete this port. In total I did **over $400,000 in API priced tokens with GPT-5.6 Sol and GPT 6 Astra**. They wrote over 1.3m lines of Rust over multiple months of /goal loops and never got past like 84% compat.

When I saw how little my Claude Code limits were burning, I figured it'd be fun to throw Opus 5.5 at this. It had a working v0 in 10 hours.

I assumed it kept using the code the Codex models wrote. I was wrong. **Opus 5.5 started from scratch. It got further than Astra in 1/10th the time.**

I let it keep going, and it definitely did. Total token spend was **~$24,047 of API spend over 2 weeks**. I was using my Claude accounts, and it worked out to somewhere between **925% and 983% of my $200 plan weekly limits**.

Expensive, for sure, but not that bad considering how much work has gone into typescript-go.

# "The Slop Line"

Everything below this was written by my LLMs, not me. 

## What actually is this?

ts-rust is a direct port of Microsoft's native TypeScript compiler, which is written in Go
([microsoft/TypeScript](https://github.com/microsoft/TypeScript), formerly
[typescript-go](https://github.com/microsoft/typescript-go)). It keeps Go's algorithms and
behavior and has the same command line (`tsc`), language server and API.

## Install

```sh
npm install -D tsc-rs
npx tsc-rs -p tsconfig.json
```

`tsc-rs` takes the same options as `tsc`. The npm package is `tsc-rs` so that it does not clash
with the `typescript` package. To use tsc-rs as the `typescript` package (its `tsc` bin, its JS API
and the TypeScript 7 VS Code extension), install
[@tsc-rs/typescript](npm/typescript-readme.md) under that name (from the first release after
0.7.0):

```json
{ "devDependencies": { "typescript": "npm:@tsc-rs/typescript@<version>" } }
```

Each [release](https://github.com/pingdotgg/ts-rust/releases) also has a standalone archive per
platform: the `tsc` binary with the lib files next to it.

Platforms: Linux x64 and arm64 (static, any distribution), macOS arm64, and (from the first
release after 0.2.0) macOS x64, Windows x64 and Windows arm64.

To use it in VS Code, see [@tsc-rs/typescript](npm/typescript-readme.md#vs-code).

## Effect diagnostics

`tsc-rs` has the [Effect](https://effect.website) language service diagnostics built in (codes
377xxx), so an Effect project needs no second compiler. They come from the same check as the
TypeScript diagnostics, and the language server shows them too. They run only when the tsconfig has
the plugin, as with `@effect/language-service`:

```json
{ "compilerOptions": { "plugins": [{ "name": "@effect/language-service" }] } }
```

The rules, options and `@effect-diagnostics` comments are a port of
[Effect-TS/tsgo](https://github.com/Effect-TS/tsgo) 0.51.1. The language server also has its editor
features: the Effect hover (with the Layer summary), inlay hints, the auto-import style, quick fixes,
document symbols, completions and refactors. All the editor features of 0.51.1 are ported. The lightbulb,
the quick fix menu and the editor's Refactor menu show the Effect refactors: as in 0.51.1, the server lists
`refactor.rewrite` in its code action kinds.

The API stability rules of 0.51.1 read the `@stability` JSDoc tags of Effect 4.
`unstableApiUsage` (TS377136) and `ex