# ComfyUI-Qwen-TTS

English | [中文版](README_CN.md)

![Nodes Screenshot](example/example.png)

ComfyUI custom nodes for speech synthesis, voice cloning, and voice design, based on the open-source **Qwen3-TTS** project by the Alibaba Qwen team.

## 📋 Changelog

- **2026-02-04**: Feature Update: Added Global Pause Control (`QwenTTSConfigNode`) and `extra_model_paths.yaml` support ([update.md](doc/update.md))
- **2026-01-29**: Feature Update: Support for loading custom fine-tuned models & speakers ([update.md](doc/update.md))
  - *Note: Fine-tuning is currently experimental; zero-shot cloning is recommended for best results.*
- **2026-01-27**: UI Optimization: Sleek LoadSpeaker UI; fixed PyTorch 2.6+ compatibility ([update.md](doc/update.md))
- **2026-01-26**: Functional Update: New voice persistence system (SaveVoice / LoadSpeaker) ([update.md](doc/update.md))
- **2026-01-24**: Added attention mechanism selection & model memory management features ([update.md](doc/update.md))
- **2026-01-24**: Added generation parameters (top_p, top_k, temperature, repetition_penalty) to all TTS nodes ([update.md](doc/update.md))
- **2026-01-23**: Dependency compatibility & Mac (MPS) support, New nodes: VoiceClonePromptNode, DialogueInferenceNode ([update.md](doc/update.md))

## Online Workflows

- **Qwen3-TTS Multi-Role Multi-Round Dialogue Generation Workflow**:
  - [workflow](https://www.runninghub.ai/post/2014703508829769729/?inviteCode=rh-v1041)
- **Qwen3-TTS 3-in-1 (Clone, Design, Custom) Workflow**:
  - [workflow](https://www.runninghub.ai/post/2014962110224142337/?inviteCode=rh-v1041)

## Key Features

- 🎵 **Speech Synthesis**: High-quality text-to-speech conversion.
- 🎭 **Voice Cloning**: Zero-shot voice cloning from short reference audio.
- 🎨 **Voice Design**: Create custom voice characteristics based on natural language descriptions.
- 🚀 **Efficient Inference**: Supports both 12Hz and 25Hz speech tokenizer architectures.
- 🎯 **Multilingual**: Native support for 10 languages (Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, and Italian).
- ⚡ **Integrated Loading**: No separate loader nodes required; model loading is managed on-demand with global caching.
- ⏱️ **Ultra-Low Latency**: Supports high-fidelity speech reconstruction with low-latency streaming.
- 🧠 **Attention Mechanism Selection**: Choose from multiple attention implementations (sage_attn, flash_attn, sdpa, eager) with auto-detection and graceful fallback.
- 💾 **Memory Management**: Optional model unloading after generation to free GPU memory for users with limited VRAM.

## Nodes List

### 1. Qwen3-TTS Voice Design (`VoiceDesignNode`)
Generate unique voices based on text descriptions.
- **Inputs**:
  - `text`: Target text to synthesize.
  - `instruct`: Description of the voice (e.g., "A gentle female voice with a high pitch").
  - `model_choice`: Currently locked to **1.7B** for VoiceDesign features.
  - `attention`: Attention mechanism (auto, sage_attn, flash_attn, sdpa, eager).
  - `unload_model_after_generate`: Unload model from memory after generation to free GPU memory.
- **Capabilities**: Best for creating "imaginary" voices or specific character archetypes.

### 2. Qwen3-TTS Voice Clone (`VoiceCloneNode`)
Clone a voice from a reference audio clip.
- **Inputs**:
  - `ref_audio`: A short (5-15s) audio clip to clone.
  - `ref_text`: Text spoken in the `ref_audio` (helps improve quality).
  - `target_text`: The new text you want the cloned voice to say.
  - `model_choice`: Choose between **0.6B** (fast) or **1.7B** (high quality).
  - `attention`: Attention mechanism (auto, sage_attn, flash_attn, sdpa, eager).
  - `unload_model_after_generate`: Unload model from memory after generation to free GPU memory.

### 3. Qwen3-TTS Custom Voice (`CustomVoiceNode`)
Standard TTS using preset speakers.
- **Inputs**:
  - `text`: Target text.
  - `speaker`: Selection from preset voices (Aiden, Eric, Serena, etc.).
  - `instruct`: Optional style instructions.
  - `attention`: Attention mechanism (auto, sage_attn, flash_attn, sdpa, eager).
  - `unload_model_after_generate`: Unload model from memory after generation to free GPU memory.

### 4. Qwen3-TTS Role Bank (`RoleBankNode`) [New]
Collect and manage multiple voice prompts for dialogue generation.
- **Inputs**:
  - Up to 8 roles, each with:
    - `role_name_N`: Name of the role (e.g., "Alice", "Bob", "Narrator")
    - `prompt_N`: Voice clone prompt from `VoiceClonePromptNode`
- **Capabilities**: Create named voice registry for use in `DialogueInferenceNode`. Supports up to 8 different voices per bank.

### 5. Qwen3-TTS Voice Clone Prompt (`VoiceClonePromptNode`) [New]
Extract and reuse voice features from reference audio.
- **Inputs**:
  - `ref_audio`: A short (5-15s) audio clip to extract features from.
  - `ref_text`: Text spoken in the `ref_audio` (highly recommended for better quality).
  - `model_ch