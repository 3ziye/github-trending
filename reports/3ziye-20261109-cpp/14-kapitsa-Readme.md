<picture>
  <source media="(max-width: 600px)" srcset="docs/assets/header-narrow.svg">
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/header-dark.svg">
  <img alt="Kapitsa writes 351 tok/s on Qwen3.6 35B-A3B on an M5 Max, against 138-281 for MLX, Ollama, llama.cpp, oMLX, mlx-serve and Splash." src="docs/assets/header-light.svg">
</picture>

Kapitsa is an inference engine for Apple silicon that runs Qwen, Nemotron and Recursive's Flint models locally, built for coding agents. It starts opencode, Claude Code, Codex, Pi, Hermes, aider or Goose on a local model, and serves OpenAI and Anthropic APIs.

[Quickstart](#quickstart) · [Benchmarks](#benchmarks) · [Features](#features) · [CLI](#cli) · [Models](#supported-models) · [How KFlash works](docs/kflash.md) · [Docs](docs/usage.md) · [Xcode 26 guide](docs/xcode-guide.md) · [日本語](README.ja.md)

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

The poster's numbers, and the models it leaves out, are in each Mac's table under [Models](#models). Every recorded run, with its Mac, model, prefill and decode speed, is in the [benchmark table](bench/README.md). Measure your Mac: `kapitsa bench --submit` adds it to the [community results](bench/community/RESULTS.md) and the [community leaderboard](https://kapitsa.vercel.app/leaderboard.html). Another engine faster on your Mac? `kapitsa bench compare` ranks every engine you have installed, and `--report` writes a Markdown report.

How Kapitsa's speed holds from 1K tokens of context to each model's limit, up to 512K, every model on the M5 Max (log scale; the [table](docs/benchmarks.md#m5-max)). The decode chart is the poster's 512-token coding answer written after a document of each length: with a document in front of it a drafter guesses fewer tokens right, so a drafted model's 1K point can sit well below its poster cell (the 27B: 82 against 143), while Flint, which drafts nothing, matches its cell:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/context-prefill-dark.webp">
  <img alt="Kapitsa's prefill speed in tokens per second on a MacBook Pro M5 Max, from 1K-token prompts to each model's context limit (128K to 512K), one line per model: Qwen3.6 35B-A3B 4,674 at 1K to 1,114 at 256K; Clover 35B-A3B 4,688 at 1K to 1,894 at 128K; Qwen3.8 27B 743 at 1K to 343 at 256K; Flash-Next 180B 1,511 at 1K to 1,087 at 256K; Lightning 30B 5,205 at 1K to 1,131 at 512K; Super-VL 120B 956 at 1K to 546 at 512K; Bolt 74B 916 at 1K to 746 at 256K; Dory1.0 4B 3,307 at 1K to 700 at 256K; Flint 40B 4,266 at 1K to 1,241 at 256K." src="docs/assets/context-prefill-light.webp">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/context-decode-dark.webp">
  <img alt="Kapitsa's decode speed in tokens per second on a MacBook Pro M5 Max after 1K tokens of context to each model's context limit (128K to 512K), one line per model: Qwen3.6 35B-A3B 335 at 1K to 136 at 256K; Clover 35B-A3B 294 at 1K to 181 at 128K; Qwen3.8 27B 82 at 1K to 43 at 256K; Flash-Next 180B 97 at 1K to 76 at 256K; Lightning 30B 241 at 1K to 116 at 512K; Super-VL 120B 97 at 1K to 44 at 512K; Bolt 74B 142 at 1K to 91 at 256K; Dory1.0 4B 123 at 1K to 23 at 256K; Flint 40B 258 at 1K to 62 at 256K." src="docs/assets/context-decode-light.webp">
</picture>

## 🔥 What's new

- [2026/11] ⚡ 