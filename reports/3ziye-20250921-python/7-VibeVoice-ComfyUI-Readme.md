# VibeVoice ComfyUI Nodes

A comprehensive ComfyUI integration for Microsoft's VibeVoice text-to-speech model, enabling high-quality single and multi-speaker voice synthesis directly within your ComfyUI workflows.

## Features

### Core Functionality
- 🎤 **Single Speaker TTS**: Generate natural speech with optional voice cloning
- 👥 **Multi-Speaker Conversations**: Support for up to 4 distinct speakers
- 🎯 **Voice Cloning**: Clone voices from audio samples
- 📝 **Text File Loading**: Load scripts from text files
- 📚 **Automatic Text Chunking**: Handles long texts seamlessly with configurable chunk size
- ⏸️ **Custom Pause Tags**: Insert silences with `[pause]` and `[pause:ms]` tags (wrapper feature)
- 🔄 **Node Chaining**: Connect multiple VibeVoice nodes for complex workflows
- ⏹️ **Interruption Support**: Cancel operations before or between generations

### Model Options
- 🚀 **Three Model Variants**: 
  - VibeVoice 1.5B (faster, lower memory)
  - VibeVoice-Large (best quality, ~17GB VRAM)
  - VibeVoice-Large-Quant-4Bit (balanced, ~7GB VRAM)
- 🔧 **Flexible Configuration**: Control temperature, sampling, and guidance scale

### Performance & Optimization
- ⚡ **Attention Mechanisms**: Choose between auto, eager, sdpa, flash_attention_2 or sage
- 🎛️ **Diffusion Steps**: Adjustable quality vs speed trade-off (default: 20)
- 💾 **Memory Management**: Toggle automatic VRAM cleanup after generation
- 🧹 **Free Memory Node**: Manual memory control for complex workflows
- 🍎 **Apple Silicon Support**: Native GPU acceleration on M1/M2/M3 Macs via MPS
- 🔢 **4-Bit Quantization**: Reduced memory usage with minimal quality loss

### Compatibility & Installation
- 📦 **Self-Contained**: Embedded VibeVoice code, no external dependencies
- 🔄 **Universal Compatibility**: Adaptive support for transformers v4.51.3+
- 🖥️ **Cross-Platform**: Works on Windows, Linux, and macOS
- 🎮 **Multi-Backend**: Supports CUDA, CPU, and MPS (Apple Silicon)

## Video Demo
<p align="center">
  <a href="https://www.youtube.com/watch?v=fIBMepIBKhI">
    <img src="https://img.youtube.com/vi/fIBMepIBKhI/maxresdefault.jpg" alt="VibeVoice ComfyUI Wrapper Demo" />
  </a>
  <br>
  <strong>Click to watch the demo video</strong>
</p>

## Installation

### Automatic Installation (Recommended)
1. Clone this repository into your ComfyUI custom nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Enemyx-net/VibeVoice-ComfyUI
```

2. Restart ComfyUI - the nodes will automatically install requirements on first use

## Available Nodes

### 1. VibeVoice Load Text From File
Loads text content from files in ComfyUI's input/output/temp directories.
- **Supported formats**: .txt
- **Output**: Text string for TTS nodes

### 2. VibeVoice Single Speaker
Generates speech from text using a single voice.
- **Text Input**: Direct text or connection from Load Text node
- **Models**: VibeVoice-1.5B or VibeVoice-Large
- **Voice Cloning**: Optional audio input for voice cloning
- **Parameters** (in order):
  - `text`: Input text to convert to speech
  - `model`: VibeVoice-1.5B, VibeVoice-Large or VibeVoice-Large-Quant-4Bit
  - `attention_type`: auto, eager, sdpa, flash_attention_2 or sage (default: auto)
  - `free_memory_after_generate`: Free VRAM after generation (default: True)
  - `diffusion_steps`: Number of denoising steps (5-100, default: 20)
  - `seed`: Random seed for reproducibility (default: 42)
  - `cfg_scale`: Classifier-free guidance (1.0-2.0, default: 1.3)
  - `use_sampling`: Enable/disable deterministic generation (default: False)
- **Optional Parameters**:
  - `voice_to_clone`: Audio input for voice cloning
  - `temperature`: Sampling temperature (0.1-2.0, default: 0.95)
  - `top_p`: Nucleus sampling parameter (0.1-1.0, default: 0.95)
  - `max_words_per_chunk`: Maximum words per chunk for long texts (100-500, default: 250)

### 3. VibeVoice Multiple Speakers
Generates multi-speaker conversations with distinct voices.
- **Speaker Format**: Use `[N]:` notation where N is 1-4
- **Voice Assignment**: Optional voice samples for each speaker
- **Recommended Model**: VibeVoice-Large for better multi-speaker quality
- **Parameters** (in order):
  - `text`: Input text with speaker labels
  - `model`: VibeVoice-1.5B, VibeVoice-Large or VibeVoice-Large-Quant-4Bit
  - `attention_type`: auto, eager, sdpa, flash_attention_2 or sage (default: auto)
  - `free_memory_after_generate`: Free VRAM after generation (default: True)
  - `diffusion_steps`: Number of denoising steps (5-100, default: 20)
  - `seed`: Random seed for reproducibility (default: 42)
  - `cfg_scale`: Classifier-free guidance (1.0-2.0, default: 1.3)
  - `use_sampling`: Enable/disable deterministic generation (default: False)
- **Optional Parameters**:
  - `speaker1_voice` to `speaker4_voice`: Audio inputs for voice cloning
  - `temperature`: Sampling temperature (0.1-2.0, default: 0.95)
  - `top_p`: Nucleus sampling parameter (0.1-1.0, default: 0.95)

### 4. VibeVoice Free Memory
Manually frees 