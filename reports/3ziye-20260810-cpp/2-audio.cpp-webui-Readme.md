# audio.cpp

> [!NOTE]
> This repository is a downstream distribution of [**0xShug0/audio.cpp**](https://github.com/0xShug0/audio.cpp) (Apache-2.0, Copyright ShugoAI LLC), extended with a full-task WebUI and Windows-friendly local launcher scripts, and periodically merged with upstream. All credit for the core inference framework goes to the upstream project — please star and contribute there.

[![0xShug0/audio.cpp | Trendshift](https://trendshift.io/api/badge/trendshift/repositories/64983/daily?language=C%2B%2B)](https://trendshift.io/repositories/64983?utm_source=trendshift-badge&utm_medium=badge&utm_campaign=badge-trendshift-64983)

`audio.cpp` is a high-performance C++ audio inference framework built on top of `ggml`, designed to make modern local audio models practical, portable, and fast.

Tired of juggling a dozen Conda environments, hundreds of Python packages, and dependency conflicts just to try a few audio models? audio.cpp gives those paths a shared native runtime instead. Runs on Windows, Linux, and macOS, with support for NVIDIA, AMD, Apple Silicon, and CPU-only machines.

> [!IMPORTANT]
> **CUDA performance headline:** multiple TTS paths already run **1.8x to up to 8x faster than their Python reference paths** while cutting end-to-end latency by **45%-85%**.
>
> **GGUF performance:** all released model families support GGUF loading, and tested Q8 packages can run up to **1.53x faster** while reducing peak VRAM by up to about **37%** on routes such as Higgs Audio, Fish Audio, and Voxtral. See the [GGUF guide](docs/gguf.md) for support status and the [Q8 performance report](docs/reports/gguf_q8_performance.md) for 16-bit vs Q8 measurements.
>
> **Production deployment example:** Try Fun-ASR-Nano with audio.cpp on the FunASR platform https://www.funasr.com/en/deploy/audio-cpp.html!
>
> **VibeVoice 1.5B:** generates a **93.9-minute podcast in 18.2 minutes** with **10 diffusion steps** and without quantization, running about **5.15x faster than real time**.
>
> **Supertonic 3:** generates about **10 hours of audio in 3 minutes** on RTX5090. Up to 200x+ real-time on CUDA, 6x+ real-time on CPU, and 47 ms TTFT in CUDA streaming mode.
> [Demo: 10 hours of audio generated in 3 minutes](https://www.reddit.com/r/LocalLLaMA/comments/1uwpvt9/audiocpp_10_hours_of_audio_generated_in_3_minutes/).
>
> **Real-world ASR win:** In [TranscrIA benchmark](https://github.com/Martossien/transcria/blob/main/docs/STT_BENCHMARK_REAL_MEETINGS.md) on messy French meeting audio, audio.cpp’s Nemotron 3.5 ASR matched the same WER as other implementations while using about **1/4 of the wall time**. 

It is built for real end-to-end execution rather than one-off model demos: the same runtime powers TTS, voice cloning, voice conversion, ASR, diarization, VAD, source separation, alignment, codec-style models, and higher-level workflows through a common framework surface.

Highlights:

- **Parity.** Strong parity tooling against Python reference paths.
- **Performance.** Performance-focused execution, reusable sessions, and batch-style offline inference. **Optimized for CUDA**.
- **Portability.** A portable native stack centered on `ggml`, with CUDA, HIP/ROCm, Vulkan, Metal, and CPU backends behind shared CLI and server entry points instead of Python-only deployment paths.
- **Pipelines.** Experimental JSON pipeline support for higher-level multi-step workflows.
- **Audio Utilities.** Built-in denoise, enhancement, resampling, and STFT/ISTFT utilities for real production-style task paths.

<p><strong><span style="font-size:1.1em;">The goal of the framework is to provide highly optimized, reusable building blocks for audio-related models, so new model integrations can be brought up faster, shared components can be improved once and benefit many families, and real end-to-end inference paths can stay efficient, maintainable, and portable.</span></strong></p>

audio.cpp would not be moving this quickly without generous contributors bringing in real fixes, new capabilities, and careful polish. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute and for a shout-out to the people already helping shape the project.

> [!TIP]
> **Contribution focus:** the most helpful contributions right now are improvements to the UI, API server, and pipeline/workflow subsystems. These areas make the existing model surface easier to use, serve, compose, and validate. See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.
>
> **New model PRs:** before starting a new model port, **please check the supported model table because several families are already implemented or under testing**. New ports should start under the [community models](docs/community_models/models.md) surface, where review is lighter than core models but still needs reproducible validation. Please follow the measurement style in [PR #19](https://github.com/0xShug0/audio.cpp/pull/19) and [PR #63](https://github.com/0xShug0/audio.cpp/pull/63): exact build/run commands, model path