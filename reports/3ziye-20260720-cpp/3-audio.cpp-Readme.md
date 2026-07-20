# audio.cpp

`audio.cpp` is a high-performance C++ audio inference framework built on top of `ggml`, designed to make modern local audio models practical, portable, and fast.

Tired of juggling a dozen Conda environments, hundreds of Python packages, and dependency conflicts just to try a few audio models? audio.cpp gives those paths a shared native runtime instead.

> [!IMPORTANT]
> **CUDA performance headline:** multiple TTS paths already run **1.8x-5.0x faster than their Python reference paths** while cutting end-to-end latency by **45%-80%**.
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
- **Portability.** A portable native stack centered on `ggml`, with CLI and server entry points instead of Python-only deployment paths.
- **Pipelines.** Experimental JSON pipeline support for higher-level multi-step workflows.
- **Audio Utilities.** Built-in denoise, enhancement, resampling, and STFT/ISTFT utilities for real production-style task paths.

<p><strong><span style="font-size:1.1em;">The goal of the framework is to provide highly optimized, reusable building blocks for audio-related models, so new model integrations can be brought up faster, shared components can be improved once and benefit many families, and real end-to-end inference paths can stay efficient, maintainable, and portable.</span></strong></p>

audio.cpp would not be moving this quickly without generous contributors bringing in real fixes, new capabilities, and careful polish. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute and for a shout-out to the people already helping shape the project.

> [!TIP]
> **Contribution focus:** the most helpful contributions right now are improvements to the UI, API server, and pipeline/workflow subsystems. These areas make the existing model surface easier to use, serve, compose, and validate. See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.
>
> **New model PRs:** before starting a new model port, **please check the supported model table because several families are already implemented or under testing**. If you do add a model, follow the validation style in [PR #19](https://github.com/0xShug0/audio.cpp/pull/19): include exact build/run commands, model paths or package ids, generated outputs, parity or path-test results, and relevant performance or memory notes.

## News

> [!IMPORTANT]
> **2026-07-18 - Voxtral Realtime ASR:** Voxtral is now released in audio.cpp with offline and streaming ASR paths. On warmed normal requests, BF16 GGUF runs at **RTF 0.089** (**11.2x realtime**) and Q8_0 at **RTF 0.064** (**15.7x realtime**); CUDA streaming TTFT is about **209 ms** with BF16 and **171 ms** with Q8_0.
>
> **2026-07-14 - Release 0.3:** This release expands audio.cpp with five new TTS families: IndexTTS2, Irodori-TTS, MOSS-TTS-Nano, MOSS-TTS-Local (thanks to [@justinjohn0306](https://github.com/justinjohn0306)), and Supertonic 3. Chatterbox also gains voice-conversion support, extending the existing TTS/voice-cloning path into a fuller speech workflow.
>
> **GGUF support:** audio.cpp now has reusable GGUF loading and conversion support, with tested GGUF paths for multiple ASR and TTS models. Some models can run up to 2× faster with Q8 GGUF, without any parity drift. See [docs/gguf.md](docs/gguf.md) for the current support status. Huge thanks to [@mirek190](https://github.com/mirek190) for driving the core GGUF work and model support forward.

**2026-06-25 to 2026-07-08:** audio.cpp grew from the first released model wave into broad TTS, ASR, music generation, source separation, VAD, diarization, codec, and voice-conversion coverage, with VibeVoice 1.5B/7B, LoRA adapter loading, initial streaming support, and major CUDA Conv1DTransp speedups.

## Supported Models

| Family | T