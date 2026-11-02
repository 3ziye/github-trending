<picture>
  <source media="(max-width: 600px)" srcset="docs/assets/header-narrow.svg">
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/header-dark.svg">
  <img alt="Kapitsa writes 346 tok/s on Qwen3.6 35B-A3B on an M5 Max, against 138-281 for MLX, Ollama, llama.cpp, oMLX, mlx-serve and Splash." src="docs/assets/header-light.svg">
</picture>

Kapitsa is an inference engine for Apple silicon that runs Qwen, Nemotron and Recursive's Flint models locally, built for coding agents. It starts opencode, Claude Code, Codex or pi on a local model, and serves OpenAI and Anthropic APIs.

[Quickstart](#quickstart) · [Benchmarks](#benchmarks) · [Features](#features) · [CLI](#cli) · [Models](#supported-models) · [How KFlash works](docs/kflash.md) · [Docs](docs/usage.md)

## Quickstart

**Requirements:** a Mac with Apple silicon (M1 or newer) and macOS 14 Sonoma or later.

**Limits:** Apple silicon only: no Linux or Windows. Flint, the four text-only Nemotrons and the 35B's `16gb` build read text only, not images ([which models read images](docs/usage.md#images)).

```bash
brew install nace-ai/tap/kapitsa
# or: curl -fsSL https://raw.githubusercontent.com/nace-ai/kapitsa/main/install.sh | bash
```

```bash
kapitsa opencode --model 35b    # also: claude, codex, pi
```

<sub>On a 16-24 GB Mac use `--model 9b`, or `4b` for the quickest replies.</sub>

## Benchmarks

Kapitsa has the fastest decode in 33 of the 38 model and Mac pairs measured against nine engines ([how each number was measured](docs/benchmarks.md#how-the-readme-poster-was-measured)).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/benchmarks-dark.webp">
  <img alt="Poster of prefill / decode speed for Kapitsa and nine other engines on a MacBook Pro M5 Max, M5 Pro, M4 Pro, M3 Pro and M1 Pro; the numbers are in the poster and in the Models section's tables" src="docs/assets/benchmarks-light.webp">
</picture>

<sub>Each cell reads prefill / decode in tokens per second, from a 4K-token prompt and a 512-token answer at T 0.6 (Flint at its card's T 1.0). The M5 Pro's Flash-Next 180B Q2 row is a 256-token answer at T 0 on that run's own 4,074-token prompt, and its Kapitsa column is Kapitsa with KFlash against plain Splash 1.5.0: a tie, the two engines' ranges overlap ([record](bench/results/2026-10-30-m5-pro-flash-next-kflash/README.md)). Footnotes, run dates and flags: [docs/benchmarks.md](docs/benchmarks.md#how-the-readme-poster-was-measured).</sub>

The poster's numbers, and the models it leaves out, are in each Mac's table under [Models](#models). Every recorded run, with its Mac, model, prefill and decode speed, is in the [benchmark table](bench/README.md). Measure your Mac: `kapitsa bench --submit` adds it to the [community results](bench/community/RESULTS.md). Another engine faster on your Mac? `kapitsa bench compare` ranks every engine you have installed, and `--report` writes a Markdown report.

How Kapitsa's speed holds from 1K to 32K tokens of context, every model on the M5 Max (log scale; the [table](docs/benchmarks.md#m5-max)):

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/context-prefill-dark.webp">
  <img alt="Kapitsa's prefill speed in tokens per second on a MacBook Pro M5 Max, from 1K- to 32K-token prompts, one line per model: Qwen3.6 35B-A3B 4,662 at 1K to 4,015 at 32K; Clover 35B-A3B 4,572 at 1K to 3,788 at 32K; Qwen3.8 27B 672 at 1K to 762 at 32K; Flash-Next 180B 1,618 at 1K to 1,463 at 32K; Lightning 30B 5,394 at 1K to 4,790 at 32K; Super-VL 120B 941 at 1K to 1,105 at 32K; Bolt 74B 907 at 1K to 1,076 at 32K; Dory1.0 4B 2,414 at 1K to 1,800 at 32K; Flint 40B 4,280 at 1K to 3,972 at 32K." src="docs/assets/context-prefill-light.webp">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/context-decode-dark.webp">
  <img alt="Kapitsa's decode speed in tokens per second on a MacBook Pro M5 Max after 1K to 32K tokens of context, one line per model: Qwen3.6 35B-A3B 268 at 1K to 175 at 32K; Clover 35B-A3B 230 at 1K to 143 at 32K; Qwen3.8 27B 97 at 1K to 61 at 32K; Flash-Next 180B 90 at 1K to 78 at 32K; Lightning 30B 206 at 1K to 117 at 32K; Super-VL 120B 76 at 1K to 46 at 32K; Bolt 74B 114 at 1K to 79 at 32K; Dory1.0 4B 109 at 1K to 76 at 32K; Flint 40B 256 at 1K to 180 at 32K." src="docs/assets/context-decode-light.webp">
</picture>

## 🔥 What's new

- [2026/10] 🍀 **DiffuSpace's Clover-35B-A3B, a block-diffusion MoE, writes at 319 tok/s on an M5 Max**: `kapitsa serve --model clover` ([numbers](docs/benchmarks.md#diffuspace-clover-35b-a3b-m5-max-2026-10-28), [how](docs/usage.md#other-models)).
- [2026/10] 🗄️ **A 180B model runs on a 48 GB Mac**: Qwen3.8-Flash-Next's Q2_0 experts stream from the SSD ([numbers](bench/results/2026-10-28-m5-pro-flash-next-engines/README.md)).
- [2026/10] 🏆 **The fastest decode in 32 of the 38 model and Mac pairs** measured against nine engines ([poster](#benchmarks)).

## Features

- **346 tok/s on Qwen3.6 35B-