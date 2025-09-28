> [!IMPORTANT]
> This is a community-maintained fork of VibeVoice. Following the removal of the official VibeVoice repository, this fork serves to preserve the codebase and maintain accessibility for the community while also introducing additional functionality (such as unofficial training/fine-tuning implementations)

## 🎙️ VibeVoice: A Frontier Long Conversational Text-to-Speech Model

[![Project Page](https://img.shields.io/badge/Project-Page-blue)](https://microsoft.github.io/VibeVoice)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-Models-orange?logo=huggingface)](https://huggingface.co/vibevoice)
[![Technical Report](https://img.shields.io/badge/Technical-Report-red)](https://arxiv.org/pdf/2508.19205)
[![Colab](https://img.shields.io/badge/Colab-Demo-orange?logo=googlecolab)](https://colab.research.google.com/github/vibevoice-community/VibeVoice/blob/main/demo/VibeVoice_colab.ipynb)

## Community

**Join the unofficial Discord community: https://discord.gg/ZDEYTTRxWG** - share samples, ask questions, discuss fine-tuning, etc.

## Overview

VibeVoice is a novel framework designed for generating **expressive**, **long-form**, **multi-speaker** conversational audio, such as podcasts, from text. It addresses significant challenges in traditional Text-to-Speech (TTS) systems, particularly in scalability, speaker consistency, and natural turn-taking.

A core innovation of VibeVoice is its use of continuous speech tokenizers (Acoustic and Semantic) operating at an ultra-low frame rate of 7.5 Hz. These tokenizers efficiently preserve audio fidelity while significantly boosting computational efficiency for processing long sequences. VibeVoice employs a [next-token diffusion](https://arxiv.org/abs/2412.08635) framework, leveraging a Large Language Model (LLM) to understand textual context and dialogue flow, and a diffusion head to generate high-fidelity acoustic details.

The model can synthesize speech up to **90 minutes** long with up to **4 distinct speakers**, surpassing the typical 1-2 speaker limits of many prior models.

Fine-tuning is now supported, which is incredibly powerful. You can adapt VibeVoice to a new language or a new voice - [try it out](https://github.com/vibevoice-community/VibeVoice/blob/main/FINETUNING.md)

## [Examples](./EXAMPLES.md)

## Evaluation

<p align="left">
  <img src="Figures/MOS-preference.png" alt="MOS Preference Results" height="260px">
  <img src="Figures/VibeVoice.jpg" alt="VibeVoice Overview" height="250px" style="margin-right: 10px;">
</p>


## Updates

- **[2025-09-05]** Microsoft repo restored (without code) with statement about responsible AI use.
- **[2025-09-04]** Community backup created after Microsoft removed original repo and models.
- **[2025-08-26]** The [VibeVoice-7B](https://huggingface.co/vibevoice/VibeVoice-7B) model weights are open-sourced!
- **[2025-08-28]** [Colab Notebook](https://colab.research.google.com/github/microsoft-community/VibeVoice/blob/main/demo/VibeVoice_colab.ipynb) available. Only VibeVoice-1.5B is supported due to GPU memory limitations.

## Roadmap

- [x] Unofficial/community training code
- [ ] HF Transformers integration ([PR](https://github.com/huggingface/transformers/pull/40546))
- [ ] VibePod: End-to-end solution that creates podcasts from documents, webpages, or even a simple topic.

## Model Zoo

| Model | Context Length | Generation Length |  Weight |
|-------|----------------|----------|----------|
| VibeVoice-1.5B | 64K | ~90 min | [HF link](https://huggingface.co/vibevoice/VibeVoice-1.5B) |
| VibeVoice-Large| 32K | ~45 min | [HF link](https://huggingface.co/vibevoice/VibeVoice-7B) |

## Installation

```bash
git clone https://github.com/vibevoice-community/VibeVoice.git
cd VibeVoice/

uv pip install -e .
```

## Usage

### 🚨 Tips

We observed users may encounter occasional instability when synthesizing Chinese speech. We recommend:

- Using English punctuation even for Chinese text, preferably only commas and periods.
- Using the Large model variant, which is considerably more stable.
- If you found the generated voice speak too fast. Please try to chunk your text with multiple speaker turns with same speaker label.

We'd like to thank [PsiPi](https://huggingface.co/PsiPi) for sharing an interesting way for emotion control. Details can be found via [discussion #12](https://huggingface.co/microsoft/VibeVoice-1.5B/discussions/12).

**Option 1: Launch Gradio demo**

```bash
python demo/gradio_demo.py --model_path vibevoice/VibeVoice-1.5B --share
# or python demo/gradio_demo.py --model_path vibevoice/VibeVoice-7B --share
# optionally add --checkpoint_path path/to/checkpoint to load a fine-tuned adapter
# use the in-app "Disable voice cloning" setting (Advanced Settings) to skip speaker conditioning
```

**Option 2: Inference from files directly**

```bash
# We provide some LLM generated example scripts under demo/text_examples/ for demo
# 1 speaker
python demo/inference_from_file.py --model_path vibevoice/VibeVoi