# audio.cpp

`audio.cpp` is a high-performance C++ audio inference framework built on top of `ggml`, designed to make modern local audio models practical, portable, and fast.

Tired of juggling a dozen Conda environments, hundreds of Python packages, and dependency conflicts just to try a few audio models? audio.cpp gives those paths a shared native runtime instead.

> [!IMPORTANT]
> **CUDA performance headline:** multiple TTS paths already run **1.8x-5.0x faster than their Python reference paths** while cutting end-to-end latency by **45%-80%**.
> **VibeVoice 1.5B:** generates a **93.9-minute podcast in 18.2 minutes** with **10 diffusion steps** and without quantization, running about **5.15x faster than real time**.

It is built for real end-to-end execution rather than one-off model demos: the same runtime powers TTS, voice cloning, voice conversion, ASR, diarization, VAD, source separation, alignment, codec-style models, and higher-level workflows through a common framework surface.

Highlights:

- **Parity.** Strong parity tooling against Python reference paths.
- **Performance.** Performance-focused execution, reusable sessions, and batch-style offline inference. **Optimized for CUDA**.
- **Portability.** A portable native stack centered on `ggml`, with CLI and server entry points instead of Python-only deployment paths.
- **Pipelines.** Experimental JSON pipeline support for higher-level multi-step workflows.
- **Audio Utilities.** Built-in denoise, enhancement, resampling, and STFT/ISTFT utilities for real production-style task paths.

<p><strong><span style="font-size:1.1em;">The goal of the framework is to provide highly optimized, reusable building blocks for audio-related models, so new model integrations can be brought up faster, shared components can be improved once and benefit many families, and real end-to-end inference paths can stay efficient, maintainable, and portable.</span></strong></p>

> [!TIP]
> **Contribution focus:** the most helpful contributions right now are improvements to the UI, API server, and pipeline/workflow subsystems. These areas make the existing model surface easier to use, serve, compose, and validate. See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.
>
> **New model PRs:** before starting a new model port, **please check the supported model table because several families are already implemented or under testing**. If you do add a model, follow the validation style in [PR #19](https://github.com/0xShug0/audio.cpp/pull/19): include exact build/run commands, model paths or package ids, generated outputs, parity or path-test results, and relevant performance or memory notes.

## News

> [!IMPORTANT]
> **2026-07-03:** Conv1DTransp module CUDA optimization: VibeVoice reaches **5.15x realtime** on **93.9-minute long-form generation**. Overall, VibeVoice inference time was reduced by **73.17%**, PocketTTS by **35.32%**, Chatterbox by **33.56%**, Qwen3-TTS by **30.60%**, HeartMuLa by **17.03%**, and VoxCPM2 by **14.7%** compared with the previous release.

> [!IMPORTANT]
> **2026-07-02:** Music generation and source separation expanded in the released framework surface: ACE-Step 1.5 Turbo/Base, HeartMuLa, Stable Audio 3 Small Music/SFX and Medium, Mel-Band RoFormer, and HTDemucs are now available through the normal audio.cpp CLI/framework paths.

- **2026-07-02:** VibeVoice 7B joins the 1.5B model, and full fine-tune adapters — language-model LoRA plus fine-tuned diffusion head and acoustic/semantic connectors — can now be merged at load time through `--load-option vibevoice.lora`.
- **2026-06-30:** VibeVoice 1.5B is now released in the framework, bringing long-form, multi-speaker dialogue TTS into the normal audio.cpp model surface.
- **2026-06-30:** More detailed usage documentation is now available in [docs/usage.md](docs/usage.md), covering model setup, CLI usage, server usage, and common workflows.
- **2026-06-26:** The speech intelligence side grew with released Citrinet ASR, MarbleNet VAD, and Sortformer diarization paths.
- **2026-06-25:** The first release wave landed with TTS, voice cloning, voice conversion, alignment, VAD, codec, and multilingual generation support across Chatterbox, MioCodec, MioTTS, OmniVoice, PocketTTS, Qwen3, SeedVC, Silero VAD, Vevo2, and VoxCPM2.

## Supported Models

Current model status in the framework:

- `released`: The model is fully wired into the broader framework surface and ready for normal use.
- `testing`: The model is implemented and working in this repo, and is still being validated, polished, or promoted into the broader released surface.
- `optimization`: The model is end-to-end working, but still needs more optimization work before it should be treated like a released or testing-level path.

| Family | Task | Supported language(s) | Supported variant(s) in this repo | Release status |
|---|---|---|---|---|
| **ace_step** | music generation, music editing | 50+ langs | ACE-Step 1.5 Turbo and Base with acestep-5Hz-lm