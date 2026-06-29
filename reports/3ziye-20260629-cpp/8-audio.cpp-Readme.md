# audio.cpp

`audio.cpp` is a high-performance C++ audio inference framework built on top of `ggml`, designed to make modern local audio models practical, portable, and fast.

> [!NOTE]
> **CUDA performance headline:** multiple TTS paths already run **1.8x-5.0x faster than their Python reference paths** while cutting end-to-end latency by **45%-80%**.

It is built for real end-to-end execution rather than one-off model demos: the same runtime powers TTS, voice cloning, voice conversion, ASR, diarization, VAD, source separation, alignment, codec-style models, and higher-level workflows through a common framework surface.

Highlights:

- **Parity.** Strong parity tooling against Python reference paths.
- **Performance.** Performance-focused execution, reusable sessions, and batch-style offline inference. **Optimized for CUDA**.
- **Portability.** A portable native stack centered on `ggml`, with CLI and server entry points instead of Python-only deployment paths.
- **Pipelines.** Experimental JSON pipeline support for higher-level multi-step workflows.
- **Audio Utilities.** Built-in denoise, enhancement, resampling, and STFT/ISTFT utilities for real production-style task paths.

<p><strong><span style="font-size:1.1em;">The goal of the framework is to provide highly optimized, reusable building blocks for audio-related models, so new model integrations can be brought up faster, shared components can be improved once and benefit many families, and real end-to-end inference paths can stay efficient, maintainable, and portable.</span></strong></p>

## Supported Models

Current model status in the framework:

- `released`: The model is fully wired into the broader framework surface and ready for normal use.
- `integration`: The model is end-to-end working and optimized, but not yet fully wired into the broader framework surface. Those models are expected to be added to the broader framework surface gradually over time.
- `optimization`: The model is end-to-end working, but still needs more optimization work before it should be treated like a released or integration-level path.

### News

| Release date | Released models |
|---|---|
| 2026-06-26 | `citrinet_asr`, `marblenet_vad`, `sortformer_diar` |
| 2026-06-25 | `chatterbox`, `miocodec`, `miotts`, `omnivoice`, `pocket_tts`, `qwen3_asr`, `qwen3_forced_aligner`, `qwen3_tts`, `seed_vc`, `silero_vad`, `vevo2`, `voxcpm2` |

| Family | Task | Supported language(s) | Supported variant(s) in this repo | Release status |
|---|---|---|---|---|
| **chatterbox** | TTS, voice cloning | ar, da, de, el, en, es, fi, fr, hi, it, ko, ms, nl, no, pl, pt, sv, sw, tr | Chatterbox with 0.5B backbone | **released** |
| **citrinet_asr** | ASR | en | Citrinet-256 | **released** |
| **marblenet_vad** | VAD | lang agnostic | MarbleNet VAD | **released** |
| **miocodec** | audio codec, voice conversion backend | lang agnostic | MioCodec v2, 25 Hz, 44.1 kHz | **released** |
| **miotts** | TTS, voice cloning | en, ja | MioTTS-1.7B | **released** |
| **omnivoice** | TTS, voice cloning, voice design | 646+ langs | OmniVoice, Qwen3-0.6B based | **released** |
| **pocket_tts** | TTS, voice cloning | en, fr, de, it, pt, es | PocketTTS-100M | **released** |
| **qwen3_asr** | ASR | zh, en, yue, ar, de, fr, es, pt, id, it, ko, ru, th, vi, ja, tr, hi, ms, nl, sv, da, fi, pl, cs, fil, fa, el, ro, hu, mk | Qwen3-ASR-0.6B | **released** |
| **qwen3_forced_aligner** | forced alignment | zh, yue, en, de, es, fr, it, pt, ru, ko, ja | Qwen3-ForcedAligner-0.6B | **released** |
| **qwen3_tts** | TTS, voice cloning, voice design | zh, en, fr, de, it, ja, ko, pt, ru, es | Qwen3-TTS-12Hz-0.6B-Base, Qwen3-TTS-12Hz-1.7B-Base, Qwen3-TTS-12Hz-1.7B-CustomVoice, Qwen3-TTS-12Hz-1.7B-VoiceDesign | **released** |
| **seed_vc** | voice conversion | lang agnostic | SeedVC XLS-R + HiFT, SeedVC Whisper-small + BigVGAN | **released** |
| **silero_vad** | VAD | lang agnostic | Silero VAD | **released** |
| **sortformer_diar** | diarization | en | Sortformer-4spk-v1 | **released** |
| **vevo2** | TTS, singing generation, voice conversion, singing conversion, editing | en, zh | Vevo2 with Qwen2.5-0.5B AR model | **released** |
| **voxcpm2** | TTS, voice cloning, voice design | ar, da, de, el, en, es, fi, fr, he, hi, id, it, ja, km, ko, lo, ms, my, nl, no, pl, pt, ru, sv, sw, th, tl, tr, vi, zh | VoxCPM2-2B, 48 kHz | **released** |
| ace_step | music generation | 50+ langs | ACE-Step 1.5 with acestep-5Hz-lm-1.7B | integration |
| audio_flamingo_next | audio understanding, ASR, audio captioning, audio QA | en, multilingual audio understanding | Audio Flamingo Next Instruct, Qwen2-7B based | optimization |
| demucs | source separation | lang agnostic | HTDemucs, HTDemucs_ft | integration |
| heartmula | music generation | zh, en, ja, ko, es | HeartMuLa-oss-3B with HeartCodec-oss | integration |
| higgs_tts | TTS, voice cloning, expressive speech | 100+ languages | Higgs Audio v3 TTS 4B | integration |
| kokoro_tts | TTS | en-us, en