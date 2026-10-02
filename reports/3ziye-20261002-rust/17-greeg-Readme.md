# greeg

**A grep for coding agents.** Familiar ripgrep flags. It answers from a
persistent index, knows which hits are *definitions*, ranks them, and fits the
answer in a token budget instead of dumping every match.

[![CI](https://github.com/thiagodmont/greeg/actions/workflows/ci.yml/badge.svg)](https://github.com/thiagodmont/greeg/actions/workflows/ci.yml)
[![release](https://img.shields.io/github/v/release/thiagodmont/greeg)](https://github.com/thiagodmont/greeg/releases)
[![license](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue)](#license)

---

## The problem

Your agent runs `rg isIdentifier` on the TypeScript compiler. ripgrep does its
job perfectly: **774 lines, 88,147 bytes**.

Claude Code truncates tool output at 30,000 characters. So your agent reads a
third of that wall, and the definitions it was actually after sit somewhere
past the cut.

greeg answers the same question in **2,553 bytes**, and opens with them:

```console
$ greeg isIdentifier
definitions (4 of 6)
src/compiler/factory/nodeTests.ts
  318  export function isIdentifier(node: Node): node is Identifier {
src/compiler/parser.ts
  2318  function isIdentifier(): boolean {  ‹ Parser
src/compiler/scanner.ts
  71  isIdentifier(): boolean;  ‹ Scanner
tests/cases/compiler/reverseMappedUnionInference.ts  [test]
  24  declare function isIdentifier(node: unknown): node is Identifier;
  +2 test definitions (--all)
…
14/767 hits · 8/105 files · 4 files demoted (17) · skipped 2 huge · ~745 tokens
```

Definitions first, each with the type it belongs to. Tests demoted, still
counted.

Where the `…` is, greeg prints the shape of the other 753 hits: a kind
breakdown, the directories they live in, the top call sites with the function
each one sits in, 122 import lines collapsed to a single line, and the
near-miss names (`isIdentifierText`, `isIdentifierPart`) listed off to the side
instead of competing for space. The footer says what got left out and which
flag brings it back.

Every hit is still accounted for. The answer is **ranked**.

## Why it's worth installing

**It's faster.** The index means a query opens only the files that could match,
instead of every file in the tree. On TypeScript-5.9 (74k files, 368 MB):

| query | `grep` | `rg` | `rg -j4` | **greeg** |
|---|---:|---:|---:|---:|
| `createSourceFile` | 4.29 s | 2.42 s | 672 ms | **30 ms** |
| `node` (30,445 matches) | 4.52 s | 2.33 s | 882 ms | **43 ms** |

**It's right more often.** Scored against SCIP ground truth from
`rust-analyzer`, `scip-python` and `scip-typescript`. The question being asked:
"I wanted to know where this symbol is defined. Was the first result correct?"

| corpus | **greeg** | `rg -nw` | `grep` |
|---|---:|---:|---:|
| TypeScript-5.9 | **96 %** | 28 % | 47 % |
| django | **100 %** | 24 % | 29 % |
| tokio | **96 %** | 17 % | 19 % |

**It costs fewer tokens**, and the broader the search, the bigger the gap.
Eight identifier searches across the TypeScript compiler, `rg` output against
greeg's answer: 4×, 5×, 8×, 8×, 20×, 21×, 36×, 44× smaller.

Narrow searches land closer to even. A single-file grep actually costs you a
few tokens *more*, because greeg adds the path header, the kind column and the
enclosing symbol. You can
[measure it on your own traffic](#is-it-actually-helping) instead of taking my
word for it.

Full numbers, protocol and caveats: [`references/BENCH.md`](references/BENCH.md).

## Install

macOS (arm64, x86_64) or Linux (x86_64, aarch64). You don't need ripgrep
installed.

```bash
brew install thiagodmont/greeg/greeg
```

<details>
<summary>Other ways to install</summary>

**Release tarball** (binary + man page, sha256 alongside):

```bash
v=0.10.0; t=aarch64-apple-darwin   # or x86_64-apple-darwin, x86_64-unknown-linux-gnu, aarch64-unknown-linux-gnu
curl -sSL https://github.com/thiagodmont/greeg/releases/download/v$v/greeg-$v-$t.tar.gz | tar xz
sudo install greeg-$v-$t/greeg /usr/local/bin/
```

**From source** (Rust 1.90 or newer):

```bash
cargo install --git https://github.com/thiagodmont/greeg greeg
```

</details>

Check it:

```bash
greeg --version
greeg doctor            # index location, freshness mode, languages, disk use
```

## Point your agent at it

One command installs a hook that rewrites supported simple `rg` calls to
`greeg --matching exact`, plus a skill file so the agent knows the extra verbs.
**You don't have to change how you prompt.** The agent keeps writing `rg`, and
greeg answers eligible calls.

```bash
greeg hook claude       # Claude Code   (--dry-run to preview, --uninstall to remove)
greeg hook codex        # Codex         (then run /hooks in Codex to trust it)
```

Install/uninstall recognizes exact command handlers: `greeg hook run` (also
`--agent claude`) for Claude, and `greeg hook run --agent codex` for Codex.
Uninstall removes those handlers while preserving other handlers and entry
metadata. Prefix lookalikes, wrappers and custom commands are left alone.
Newly empty entries are removed only wh