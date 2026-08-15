<p align="center">
  <img src="docs/assets/turbofieldfare-logo-rounded.png" alt="TurboFieldfare logo: a fieldfare inside a segmented cache ring" width="280">
</p>

<h1 align="center">TurboFieldfare</h1>

<p align="center">
  <strong>Gemma 4 26B-A4B inference in about 2 GB of RAM</strong><br>
  A custom Swift + Metal runtime for any Apple Silicon Mac, even the 8 GB ones.
</p>

<p align="center">
  <img alt="Swift 6.2" src="https://img.shields.io/badge/Swift-6.2-F05138?logo=swift&logoColor=white">
  <img alt="Metal 4" src="https://img.shields.io/badge/Metal-4-5E5CE6">
  <img alt="macOS 26 or later" src="https://img.shields.io/badge/macOS-26%2B-000000?logo=apple&logoColor=white">
  <a href="LICENSE"><img alt="Apache 2.0 license" src="https://img.shields.io/badge/License-Apache%202.0-2ea44f"></a>
</p>

<p align="center">
  <a href="#try-it">Quick start</a> ·
  <a href="docs/OPENAI_SERVER.md">Local server</a> ·
  <a href="docs/BENCHMARKS.md">Benchmarks</a> ·
  <a href="docs/COMMUNITY_BENCHMARKS.md">Contribute results</a> ·
  <a href="docs/SYSTEM_DESIGN.md">How it works</a> ·
  <a href="docs/OPTIMIZATION_JOURNEY.md">Experiments</a> ·
  <a href="docs/IMPLEMENTATION_REFERENCES.md">References</a>
</p>

![TurboFieldfare Mac app generating text with Gemma 4 26B-A4B](docs/assets/turbofieldfare-app.webp)

Memory got expensive. So I gave a 26-billion-parameter model a ~2 GB budget.

TurboFieldfare runs the instruction-tuned
**[Gemma 4 26B-A4B](https://ai.google.dev/gemma/docs/core/model_card_4)**
without loading the entire 14.3 GB model into memory. It keeps the shared
1.35 GB core and FP16 KV cache in memory, then streams only the experts needed
for each token from SSD. This is what lets the model run on Macs with 8 GB of
RAM.

The runtime, streaming installer, CLI, and native Mac app are written in Swift
and Metal. TurboFieldfare is model-specific rather than a wrapper around MLX or
llama.cpp. The curated [experiment record](docs/experiments/EXPERIMENT_INVENTORY.md)
summarizes 103 measured results across kernels, caching, I/O, prefill, and
decode.

## Try it

```bash
git clone https://github.com/drumih/turbo-fieldfare.git
cd turbo-fieldfare
swift build -c release
.build/release/TurboFieldfareMac
```

On the first run, Swift Package Manager downloads and builds the Swift packages
required by the tokenizer. The complete release build includes the foreground
Mac app and its sibling decode-service executable.

When the app opens, choose **Download** and let TurboFieldfare fetch and repack
the pinned model (about 15 GB). Once it is ready, choose **Load Model**, type
your prompt, and press **Generate**.

## At a glance

| Metric          | Value                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Model           | Gemma 4 26B-A4B IT, 26B total parameters, about 3.88B active per token                                                   |
| Weights         | MLX affine 4-bit, group 64; 8-bit router; 4-bit shared and routed experts                                                |
| Memory          | ~2 GB of weights and 4K KV cache                                                                                         |
| Storage         | About 14.3 GB for the installed text-only model                                                                          |
| Hardware        | Apple Silicon Mac; 8 GB of RAM                                                                                            |
| Platform        | macOS 26, Metal 4, Swift 6.2                                                                                             |
| M2 measured decode | [5.1-6.3 tok/s](docs/BENCHMARKS.md#m2-measured-decode) on an 8 GB M2 MacBook Air |
| M5 measured decode | [31-35 tok/s](docs/BENCHMARKS.md#m5-measured-decode) on a 24 GB M5 Pro |
| Community Reports | [Here](docs/COMMUNITY_BENCHMARKS.md#community-results) |

The measured result is a reference point, not a performance ceiling. Prompt
length, generated length, page-cache state, and hardware all affect throughput.
See [community benchmark results](docs/COMMUNITY_BENCHMARKS.md#community-results)
from other Macs, or follow the
[community benchmark guide](docs/COMMUNITY_BENCHMARKS.md) to add your own.

## Using TurboFieldfare

TurboFieldfare provides a native Mac app, a command-line interface, and an
experimental loopback OpenAI-compatible server. They use the same `.gturbo`
model directory, but only one model-owning product should run at a time.

The Swift package exposes six products:

| Product | Purpose |
| --- | --- |
| `TurboFieldfare` | Swift library containing the runtime and Metal kernels |
| `TurboFieldfareMac` | Native Mac app for installation and generation |
| `TurboFieldfareDecodeService` | One-shot local model and Metal owner used by the Mac app |
| `Turb