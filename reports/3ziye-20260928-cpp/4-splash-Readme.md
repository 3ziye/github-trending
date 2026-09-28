# Splash

[![CI](https://github.com/incoai/splash/actions/workflows/ci.yml/badge.svg)](https://github.com/incoai/splash/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Apple%20silicon-black.svg)](#quick-start)

**A local inference engine for Apple silicon, built around the model.**

Splash runs coding agents and OpenAI or Anthropic compatible applications on
one Mac. It combines [DFlash 2](https://inco.ai/blog/dflash2/) speculative
decoding, specialized Metal kernels, and automatic memory planning, with
vision, tool calling, and a built-in chat page.
It reuses cached prefixes and batches concurrent requests automatically.

## Quick start

Apple M3 or newer, macOS 26.4 or later, and [Homebrew](https://brew.sh).
The 4-bit examples need at least 36 GB of unified memory (48 GB recommended);
24 GB Macs can use [smaller GGUF variants](#models).

```bash
brew install incoai/tap/splash
splash serve --model unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_M
```

The first run downloads the model and its matching draft, prepares the
weights, and starts serving on `127.0.0.1:8000`. Later starts reuse them.
Leave room on disk for both the downloads and prepared weights
([storage requirements](DEVELOPMENT.md#model-storage)).

Once it prints `Ready`, leave this terminal open. Open <http://127.0.0.1:8000>
in your browser, or run an installed coding agent from another terminal:

```bash
splash opencode    # or: splash claude / splash codex / splash hermes / splash pi
```

Press Ctrl+C in the server terminal to stop Splash.
For LM Studio Bionic, follow its [Splash setup guide](https://lmstudio.ai/blog/splash-engine).

## Use the API

OpenAI Chat Completions and Responses, and Anthropic Messages, with streaming,
tool calls, JSON Schema output, images, and inline PDFs:

```bash
curl http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_M",
    "messages": [{"role": "user", "content": "Explain speculative decoding in one sentence."}]
  }'
```

Reasoning follows the model default; `"reasoning_effort": "none"` turns it off.
[Reasoning settings](DEVELOPMENT.md#default-reasoning-effort) ·
[API details](DEVELOPMENT.md#code-and-api-boundaries)

## Models

Splash supports these model families, with a matching DFlash2 draft selected
automatically:

| Model | GGUF example | MLX 4-bit |
| --- | --- | --- |
| Qwen3.8-27B | `unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_M` | `mlx-community/Qwen3.8-27B-4bit` |
| Qwen3.6-35B-A3B | `unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_M` | `mlx-community/Qwen3.6-35B-A3B-4bit` |

Unsloth GGUF variants span **1–8 bits**, including mixed-precision UD formats;
`UD-Q8_K_XL` and BF16 targets are not supported.
[Prism ML Ternary Bonsai 2](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)
is also supported in PQ2_0 (7.2 GB), including vision. Pass `OWNER/REPO:VARIANT`
to `--model`, as in the quick start. Smaller variants run on
[24 GB Macs](docs/performance.md#smaller-ggufs-on-24-gb-macs).
[27B variants](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/tree/main) ·
[35B variants](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF/tree/main)

Vision and the tokenizer come from the target model's source.
[Model loading and compatibility](DEVELOPMENT.md#upstream-model-loading) ·
[Supported formats](DEVELOPMENT.md#gguf-targets)

## Settings

Memory and context are sized automatically, up to the model's native context
window. To set your own limits or cache options, add these to `splash serve`:

| Option | Purpose |
| --- | --- |
| `--max-memory 28G` | Cap Metal memory use. |
| `--max-context 100K` | Set the context limit. |
| `--language-only` | Skip vision; serve text only. |
| `--kv-format bf16` | Use BF16 KV cache. Default: 8-bit (INT8). |
| `--max-cache-disk 16G` | Offload KV cache and GDN states to SSD as needed. Off by default. |

On a Mac you also use for other work, `--max-memory` leaves room for other
applications.
The server listens on localhost without authentication by default. For LAN
access, authentication, and other options, see
[server configuration](DEVELOPMENT.md#server-configuration) or
`splash serve --help`.
[KV precision](DEVELOPMENT.md#kv-cache-precision) ·
[SSD cache](DEVELOPMENT.md#disk-cache)

## Performance

Measured on an M5 Pro (16-core GPU, 48 GB), using the Splash
packages and selected SPEED-Bench coding prompts over HTTP. Ratios compare
with the next-fastest engine measured in that benchmark.

| Metric | Qwen3.6-35B-A3B | Qwen3.8-27B |
| --- | ---: | ---: |
| Decode · short prompt | 210 tok/s (1.7×) | 74 tok/s (2.0×) |
| Prefill · 32K prompt | 2,011 tok/s (1.3×) | 363 tok/s (1.2×) |
| Cached time to first token · 32K replay | 123 ms (6.6×) | 282 ms (7.3×) |
| Aggregate decode · 4 concurrent short prompts | 357 tok/s (2.0×) | 170 tok/s (3.9×) |

[Launch benchmarks](https://inco.ai/blog/splash/) ·
[Measurement details]