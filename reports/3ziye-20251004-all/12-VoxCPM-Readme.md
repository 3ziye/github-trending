## 🎙️ VoxCPM: Tokenizer-Free TTS for Context-Aware Speech Generation and True-to-Life Voice Cloning


[![Project Page](https://img.shields.io/badge/Project%20Page-GitHub-blue)](https://github.com/OpenBMB/VoxCPM/) [![Technical Report](https://img.shields.io/badge/Technical%20Report-Arxiv-red)](https://arxiv.org/abs/2509.24650) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-OpenBMB-yellow)](https://huggingface.co/openbmb/VoxCPM-0.5B) [![ModelScope](https://img.shields.io/badge/ModelScope-OpenBMB-purple)](https://modelscope.cn/models/OpenBMB/VoxCPM-0.5B)  [![Live Playground](https://img.shields.io/badge/Live%20PlayGround-Demo-orange)](https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo) [![Samples](https://img.shields.io/badge/Audio%20Samples-Page-green)](https://openbmb.github.io/VoxCPM-demopage)



<div align="center">
  <img src="assets/voxcpm_logo.png" alt="VoxCPM Logo" width="40%">
</div>

<div align="center">

👋 Contact us on [WeChat](assets/wechat.png)

</div>

## News 
* [2025.09.30] 🔥 🔥 🔥  We Release VoxCPM [Technical Report](https://arxiv.org/abs/2509.24650)!
* [2025.09.16] 🔥 🔥 🔥  We Open Source the VoxCPM-0.5B [weights](https://huggingface.co/openbmb/VoxCPM-0.5B)!
* [2025.09.16] 🎉 🎉 🎉  We Provide the [Gradio PlayGround](https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo) for VoxCPM-0.5B, try it now! 

## Overview

VoxCPM is a novel tokenizer-free Text-to-Speech (TTS) system that redefines realism in speech synthesis. By modeling speech in a continuous space, it overcomes the limitations of discrete tokenization and enables two flagship capabilities: context-aware speech generation and true-to-life zero-shot voice cloning.

Unlike mainstream approaches that convert speech to discrete tokens, VoxCPM uses an end-to-end diffusion autoregressive architecture that directly generates continuous speech representations from text. Built on [MiniCPM-4](https://huggingface.co/openbmb/MiniCPM4-0.5B) backbone, it achieves implicit semantic-acoustic decoupling through hierachical language modeling and FSQ constraints, greatly enhancing both expressiveness and generation stability.

<div align="center">
  <img src="assets/voxcpm_model.png" alt="VoxCPM Model Architecture" width="90%">
</div>


###  🚀 Key Features
- **Context-Aware, Expressive Speech Generation** - VoxCPM comprehends text to infer and generate appropriate prosody, delivering speech with remarkable expressiveness and natural flow. It spontaneously adapts speaking style based on content, producing highly fitting vocal expression trained on a massive 1.8 million-hour bilingual corpus.
- **True-to-Life Voice Cloning** - With only a short reference audio clip, VoxCPM performs accurate zero-shot voice cloning, capturing not only the speaker’s timbre but also fine-grained characteristics such as accent, emotional tone, rhythm, and pacing to create a faithful and natural replica.
- **High-Efficiency Synthesis** - VoxCPM supports streaming synthesis with a Real-Time Factor (RTF) as low as 0.17 on a consumer-grade NVIDIA RTX 4090 GPU, making it possible for real-time applications.





##  Quick Start

### 🔧 Install from PyPI
``` sh
pip install voxcpm
```
### 1.  Model Download (Optional)
By default, when you first run the script, the model will be downloaded automatically, but you can also download the model in advance.
- Download VoxCPM-0.5B
    ```
    from huggingface_hub import snapshot_download
    snapshot_download("openbmb/VoxCPM-0.5B")
    ```
- Download ZipEnhancer and SenseVoice-Small. We use ZipEnhancer to enhance speech prompts and SenseVoice-Small for speech prompt ASR in the web demo.
    ```
    from modelscope import snapshot_download
    snapshot_download('iic/speech_zipenhancer_ans_multiloss_16k_base')
    snapshot_download('iic/SenseVoiceSmall')
    ```

### 2. Basic Usage
```python
import soundfile as sf
import numpy as np
from voxcpm import VoxCPM

model = VoxCPM.from_pretrained("openbmb/VoxCPM-0.5B")

# Non-streaming
wav = model.generate(
    text="VoxCPM is an innovative end-to-end TTS model from ModelBest, designed to generate highly expressive speech.",
    prompt_wav_path=None,      # optional: path to a prompt speech for voice cloning
    prompt_text=None,          # optional: reference text
    cfg_value=2.0,             # LM guidance on LocDiT, higher for better adherence to the prompt, but maybe worse
    inference_timesteps=10,   # LocDiT inference timesteps, higher for better result, lower for fast speed
    normalize=True,           # enable external TN tool
    denoise=True,             # enable external Denoise tool
    retry_badcase=True,        # enable retrying mode for some bad cases (unstoppable)
    retry_badcase_max_times=3,  # maximum retrying times
    retry_badcase_ratio_threshold=6.0, # maximum length restriction for bad case detection (simple but effective), it could be adjusted for slow pace speech
)

sf.write("output.wav", wav, 16000)
print("saved: output.wav")

# Streaming
chunks = []