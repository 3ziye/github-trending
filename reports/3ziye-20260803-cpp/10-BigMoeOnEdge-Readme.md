<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/logo/horizontal-ink.svg">
    <img src="docs/assets/logo/horizontal.svg" width="440" alt="BigMoeOnEdge">
  </picture>
</p>

<p align="center"><b>Run Mixture-of-Experts models bigger than your device's RAM. On a phone, on a PC, CPU only.</b></p>

<p align="center">
  <a href="https://github.com/Helldez/BigMoeOnEdge/releases/latest"><img src="https://img.shields.io/github/v/release/Helldez/BigMoeOnEdge" alt="Latest release"></a>
  <a href="https://github.com/Helldez/BigMoeOnEdge/actions/workflows/ci.yml"><img src="https://github.com/Helldez/BigMoeOnEdge/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Helldez/BigMoeOnEdge" alt="License"></a>
</p>

---

A Mixture-of-Experts model is made of many small "experts", and each generated token only uses a
few of them. BigMoeOnEdge takes that literally: it keeps the small always-needed part of the model
at hand and reads just the experts each token asks for, directly from flash storage, at the moment
they are needed. The rest of the model stays on disk. That is what lets a model several times
bigger than your RAM generate text on an ordinary phone, losslessly: the output is byte-identical
to running the same model fully resident.

It is built **on top of llama.cpp's public API**, not as a fork. Every quantization format,
tokenizer and chat template llama.cpp supports works out of the box, because llama.cpp itself is
doing that part: MXFP4 and Q4_K_M stream through the same code. Supporting a new MoE architecture
is one row in a registry, and following a new llama.cpp release is a routine submodule bump.

The most extreme thing it can do today: **DeepSeek V4 Flash 0731**, a 284B-parameter MoE
(~91 GB on disk at 2-bit expert quantization), generating on a phone with 12 GB of RAM at about
**1 tok/s**. More than seven times more model than memory, streamed from flash as the three shard
files Hugging Face ships, with no merge step and no PC in the loop.

<p align="center"><img src="docs/assets/hero-dsv4.gif" width="360" alt="DeepSeek V4 Flash 0731 (284B, ~91 GB) generating in the demo app on a 12 GB phone, with live tok/s and telemetry"></p>
<p align="center"><em>DeepSeek V4 Flash 0731: 284B parameters, ~91 GB on disk, on a 12 GB phone.
0.94 tok/s in the demo app, real time.</em></p>

It is not one model, either. Below: three of them, one after another on the same phone, each past
what it should be able to hold.

https://github.com/user-attachments/assets/f899b93f-c7c4-4ce9-9fb0-5ed1bae13761

<p align="center"><em>Left to right: gpt-oss-120b (~60 GB), Qwen3-30B-A3B (18.5 GB), Gemma-4-26B-A4B (17 GB),
recorded in the demo app on a 12 GB phone, real time, not sped up.</em></p>

## Table of contents

- [Why this exists](#why-this-exists)
- [Try it on your phone](#try-it-on-your-phone)
- [Features](#features)
- [Supported models](#supported-models)
- [Benchmarks](#benchmarks)
- [Quickstart](#quickstart)
- [How it works](#how-it-works)
- [Documentation](#documentation)
- [Prior art](#prior-art)
- [License](#license)

## Why this exists

The models people actually want to talk to keep growing faster than the RAM in the devices they
carry. MoE models offer a way out, because most of their weights sit idle on any given token, but
every mainstream runtime still insists on holding (or paging) the whole file in memory. So a 20 GB
model on a 12 GB phone either refuses to load or crawls while the OS frantically swaps.

BigMoeOnEdge treats flash storage as part of the memory hierarchy instead. Three situations where
that changes what your device can run:

**Models far past RAM.** A ~60 GB model on a 12 GB phone cannot be resident, full stop. Streamed,
it runs at usable speed. This is the headline case, but it is not the only one.

**Models just past RAM.** An 18 to 22 GB model on a 12 GB phone is where the ordinary way of
loading (mmap) turns into a fault storm: the OS evicts weights as fast as it reads them, speed
swings wildly, other apps get killed. Streamed, the same model runs stably at up to 5 tok/s,
byte-identical output, and the rest of the phone stays alive.

**Models that barely fit.** Even a model that technically fits in RAM, say an 8B class MoE on a
phone with a few GB free, benefits: loaded the ordinary way it squeezes out everything else, and
the OS claws memory back mid-generation. Streamed with a capped cache, it runs inside a budget you
choose and leaves the system alone. And this is all plain CPU inference: no GPU, no NPU, four
cores and the phone's flash storage.

The same engine builds unmodified on desktop, where a model past RAM streams from the SSD out of
the box. Phones stay the focus, because that is where memory is tightest.

## Try it on your phone

No build needed. Install the APK from the
[latest release](https://github.com/Helldez/BigMoeOnEdge/releases/latest), open the **Get a
model** card