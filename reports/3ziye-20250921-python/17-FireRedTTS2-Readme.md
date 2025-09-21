<div align="center">
    <h1>
    FireRedTTS-2
    </h1>
    <p>
    Official PyTorch code for <br>
    <b><em>FireRedTTS-2: Towards Long Conversational Speech Generation for Podcast and Chatbot</em></b>
    </p>
    <p>
    <!-- <img src="assets/XiaoHongShu_Logo.png" alt="Institution 4" style="width: 102px; height: 48px;"> -->
    <img src="assets/FireRedTTS_Logo.png" alt="FireRedTTS_Logo" style="width: 248px; height: 68px;">
    </p>
    <p>
    </p>
    <a href="https://arxiv.org/abs/2509.02020"><img src="https://img.shields.io/badge/Paper-ArXiv-red" alt="technical report"></a>
    <a href="https://fireredteam.github.io/demos/firered_tts_2/"><img src="https://img.shields.io/badge/Demo-Page-lightgrey" alt="version"></a>
    <a href="https://huggingface.co/FireRedTeam/FireRedTTS2"><img src="https://img.shields.io/badge/Hugging%20Face-Model%20Page-yellow" alt="HF-model"></a>
    <a href="https://github.com/FireRedTeam/FireRedTTS"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="Apache-2.0"></a>
</div>

## Overview

FireRedTTS‑2 is a long-form streaming TTS system for **multi-speaker dialogue generation**, delivering stable, natural speech with reliable speaker switching and context-aware prosody.

## Highlight🔥

- **Long Conversational Speech Generation**: It currently supports 3 minutes dialogues with 4 speakers and can be easily scaled to longer conversations
with more speakers by extending training corpus.
- **Multilingual Support**: It supports multiple languages including English, Chinese, Japanese, Korean, French, German, and Russian. Support zero-shot voice cloning for cross-lingual and code-switching scenarios.
- **Ultra-Low Latency**: Building on the new **12.5Hz streaming** speech tokenizer, we employ a dual-transformer architecture that operates on a text–speech interleaved sequence, enabling flexible sentence-bysentence generation and reducing first-packet latency，Specifically, on an L20 GPU, our first-packet latency as low as 140ms while maintaining high-quality audio output.
- **Strong Stability**：Our model achieves high similarity and low WER/CER in both monologue and dialogue tests.
- **Random Timbre Generation**:Useful for creating ASR/speech interaction data.

## Demo Examples

**Random Timbre Generation & Multilingual Support**
<div align="center">

<https://github.com/user-attachments/assets/804e9e67-fb15-4557-9715-43cd46a1b3e8>

</div>

**Zero-Shot Podcast Generation**
<div align="center">

<https://github.com/user-attachments/assets/e68b1b7e-1329-47bb-a16f-8589cf227579>

</div>

**Speaker-Specific Finetuned Podcast Generation**

⚠️ Speaker voices: hosts "肥杰" and "惠子" from the podcast "肥话连篇". Use without authorization is forbidden.

⚠️ 声音来源：播客 "肥话连篇" 主播 "肥杰" 和 "惠子"，未经授权不能使用。
<div align="center">

<https://github.com/user-attachments/assets/21f626cb-eaf4-4f5c-920c-3d5d4c8cfa8b>

</div>

For more examples, see [demo page](https://fireredteam.github.io/demos/firered_tts_2/).

## News

- [2025/09/12] 🔥 **We have added a UI tool to the dialogue generation.**
- [2025/09/08] 🔥 We release the [pre-trained checkpoints](https://huggingface.co/FireRedTeam/FireRedTTS2) and inference code.
- [2025/09/02] 🔥 We release the [technical report](https://arxiv.org/abs/2509.02020) and [demo page](https://fireredteam.github.io/demos/firered_tts_2/)

## Roadmap

- [x] 2025/09
  - [x] Release the pre-trained checkpoints and inference code.
  - [x] Add web UI tool.

- [ ] 2025/10
  - [ ] Release a base model with enhanced multilingual support.
  - [ ] **Provide fine-tuning code & tutorial for specific dialogue/multilingual data.**
  - [ ] **End-to-end text-to-blog pipeline.**

## Install & Model Download

### Clone and install

- **Clone the repo**

    ``` sh
    git clone https://github.com/FireRedTeam/FireRedTTS2.git
    cd FireRedTTS2
    ```

- **Create Conda env**:

    ``` sh
    conda create --name fireredtts2 python==3.11
    conda activate fireredtts2

    # Step 1. PyTorch Installation (if required)
    pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu126

    # Step 2. Install Dependencies
    pip install -e .
    pip install -r requirements.txt
    ```

- **Model download**

    ```sh
    git lfs install
    git clone https://huggingface.co/FireRedTeam/FireRedTTS2 pretrained_models/FireRedTTS2
    ```

## Basic Usage

**Dialogue Generation with Web UI**

Generate dialogue through an easy-to-use web interface that supports both voice cloning and randomized voices.

```sh
python gradio_demo.py --pretrained-dir "./pretrained_models/FireRedTTS2"
```

<div align="center">

<p>
<img src="assets/gradio.png" alt="FireRedTTS_Logo" style="width: 997px; height: 515px;">
</p>

</div>

**Dialogue Generation**

```python
import os
import sys
import torch
import torchaudio
from fireredtts2.fireredtts2 import FireRedTTS2

device = "cuda"

fireredtts2 = FireRedTTS2(
    pretrained_dir="./pretrained_models/FireRedTTS2",
    gen_ty