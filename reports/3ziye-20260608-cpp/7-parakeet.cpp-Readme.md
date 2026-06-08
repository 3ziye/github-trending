# parakeet.cpp

**Brought to you by the [LocalAI](https://github.com/mudler/LocalAI) team**, the folks behind LocalAI, the open-source AI engine that runs any model (LLMs, vision, voice, image, video) on any hardware, no GPU required.

[![Model on Hugging Face](https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-md.svg)](https://huggingface.co/mudler/parakeet-cpp-gguf)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![LocalAI](https://img.shields.io/badge/LocalAI-Run_Locally-orange)](https://github.com/mudler/LocalAI)

parakeet.cpp is a C++17 inference port of NVIDIA's [NeMo](https://github.com/NVIDIA-NeMo/NeMo) Parakeet speech-recognition models, built on [ggml](https://github.com/ggml-org/ggml). It gives you fast, dependency-light automatic speech recognition on CPU (and on GPU through ggml's backends), with no Python runtime needed at inference time.

It covers all the offline Parakeet families (CTC, RNNT, TDT, and hybrid TDT-CTC, in 0.6B/1.1B/110M sizes, English plus multilingual v3), each validated at WER 0 against NeMo on every published checkpoint. It also does **cache-aware streaming with end-of-utterance (EOU) detection** for `parakeet_realtime_eou_120m-v1`, where the streaming transcript matches NeMo's cache-aware streaming byte for byte. And it supports the **multilingual, prompt-conditioned streaming model** `nvidia/nemotron-3.5-asr-streaming-0.6b` (40+ locales): pass a target language with `--lang <locale>` (default `auto`) and both the offline and the cache-aware streaming transcripts match NeMo per language at WER 0. The full coverage matrix lives in `docs/parity.md`.

It's faster than NeMo's PyTorch runtime on both CPU and GPU, with byte-identical transcripts. The full numbers, methodology, and all the plots are in [benchmarks/BENCHMARK.md](benchmarks/BENCHMARK.md).

<p align="center">
  <a href="benchmarks/BENCHMARK.md"><img src="benchmarks/plots/speedup.png" width="49%" alt="CPU speedup vs NeMo (RTFx ratio per dtype)"></a>
  <a href="benchmarks/BENCHMARK.md"><img src="benchmarks/plots/gpu_speedup.png" width="49%" alt="GPU speedup vs NeMo on the NVIDIA GB10"></a>
</p>

It also runs circles around whisper.cpp on the same audio: the 110M Parakeet is faster than whisper base.en and far faster than large-v3-turbo, while the larger Parakeets match or beat whisper's accuracy (see [benchmarks/BENCHMARK.md](benchmarks/BENCHMARK.md)).

<p align="center">
  <a href="benchmarks/BENCHMARK.md"><img src="benchmarks/plots/vs_whisper.png" width="88%" alt="parakeet.cpp vs whisper.cpp RTFx on CPU and GPU"></a>
</p>

---

## Supported models

Every model below is validated at WER 0 against NeMo and published as GGUF (f16, q8_0, q6_k, q5_k, q4_k) in the single collection repo [mudler/parakeet-cpp-gguf](https://huggingface.co/mudler/parakeet-cpp-gguf). Convert any of them yourself with `scripts/convert_parakeet_to_gguf.py`. The per-model parity matrix is in [docs/parity.md](docs/parity.md).

| Model | Type | Size | Notes | Source |
| ----- | ---- | ---- | ----- | ------ |
| [parakeet-tdt_ctc-110m](https://huggingface.co/nvidia/parakeet-tdt_ctc-110m) | hybrid TDT+CTC | 110M | English, the small anchor checkpoint | NVIDIA |
| [parakeet-ctc-0.6b](https://huggingface.co/nvidia/parakeet-ctc-0.6b) | CTC | 0.6B | English | NVIDIA |
| [parakeet-rnnt-0.6b](https://huggingface.co/nvidia/parakeet-rnnt-0.6b) | RNNT | 0.6B | English | NVIDIA |
| [parakeet-tdt-0.6b-v2](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2) | TDT | 0.6B | English | NVIDIA |
| [parakeet-tdt-0.6b-v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) | TDT | 0.6B | multilingual (25 European languages) | NVIDIA |
| [parakeet-ctc-1.1b](https://huggingface.co/nvidia/parakeet-ctc-1.1b) | CTC | 1.1B | English | NVIDIA |
| [parakeet-rnnt-1.1b](https://huggingface.co/nvidia/parakeet-rnnt-1.1b) | RNNT | 1.1B | English | NVIDIA |
| [parakeet-tdt-1.1b](https://huggingface.co/nvidia/parakeet-tdt-1.1b) | TDT | 1.1B | English | NVIDIA |
| [parakeet-tdt_ctc-1.1b](https://huggingface.co/nvidia/parakeet-tdt_ctc-1.1b) | hybrid TDT+CTC | 1.1B | English | NVIDIA |
| [parakeet_realtime_eou_120m-v1](https://huggingface.co/nvidia/parakeet_realtime_eou_120m-v1) | RNNT, streaming | 120M | cache-aware streaming with end-of-utterance detection (`--stream`) | NVIDIA |
| [nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) | RNNT, streaming | 0.6B | multilingual (40+ locales), prompt-conditioned, offline and cache-aware streaming, pick a language with `--lang` (default `auto`). OpenMDW-1.1 | NVIDIA |

---

## Performance

parakeet.cpp is faster than NeMo's PyTorch runtime on every Parakeet model, on both CPU and GPU, and the transcripts come out byte-identical (WER 0 vs NeMo). Full methodology, all 10 models, quantization tradeoffs, and plots are in [`benchmarks/BENCHMARK.md`](benchmarks/BENCHMARK.md).

### See it run

The same clip fed to parakeet.cpp and to NeMo's own PyTorch runtim