<div align='center'>
<h1>Emu3.5: Native Multimodal Models are World Learners</h1>

Emu3.5 Team, BAAI

[Project Page](https://emu.world/) | [🤗HF Models](https://huggingface.co/collections/BAAI/emu35) | [Paper](https://arxiv.org/pdf/2510.26583)
</div>


<div align='center'>
<img src="./assets/arch.png" class="interpolation-image" alt="arch." height="100%" width="100%" />
</div>


<div align='center'>
<img src="./assets/co.png" class="interpolation-image" alt="arch." height="90%" width="90%" />
</div>


|  🔹 | **Core Concept**                         | **Description**                                                                                                                            |
| :-: | :--------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
|  🧠 | **Unified World Modeling**               | Predicts the **next state jointly across vision and language**, enabling coherent **world modeling** and **generation**.              |
|  🧩 | **End-to-End Pretraining**               | Trained with a **unified next-token prediction** objective over **interleaved vision–language sequences**.                                 |
|  📚 | **Over 10T+ Multimodal Tokens**               | Pre-trained on **over 10 trillion interleaved tokens** from **video frames** and **transcripts**, capturing **spatiotemporal structure**.       |
|  🔄 | **Native Multimodal I/O**                | Processes and generates **interleaved visual–text sequences** without **modality adapters** or **task-specific heads**.                    |
|  🎯 | **RL Post-Training**                     | Large-scale **reinforcement learning** enhances **reasoning**, **compositionality**, and **generation quality**.                           |
|  ⚡  | **Discrete Diffusion Adaptation (DiDA)** | Converts **sequential decoding → bidirectional parallel prediction**, achieving **≈20× faster inference without performance loss**.      |
| 🖼️ | **Versatile Generation**                 | Excels in **long-horizon vision–language generation**, **any-to-image (X2I)** synthesis, and **text-rich image creation**.                 |
|  🌐 | **Generalizable World Modeling**         | Enables **spatiotemporally consistent world exploration**, and **open-world embodied manipulation** across diverse scenarios.          |
|  🏆 | **Performance Benchmark**                | Matches **Gemini 2.5 Flash Image (Nano Banana)** on **image generation/editing**, and **outperforms** on **interleaved generation tasks**. |



## 🔥 News

- **2025-11-19 · 🚀 vLLM Offline Inference Released** — Meet `inference_vllm.py` with a new cond/uncond batch scheduler, delivering **4–5× faster end-to-end generation** on vLLM 0.11.0 across Emu3.5 tasks. Jump to [#Run Inference with vLLM](#run-inference-with-vllm) for setup guidance and see PR [#47](https://github.com/baaivision/Emu3.5/pull/47) for full details.
- **2025-11-17 · 🎛️ Gradio Demo (Transformers Backend)** — Introduced `gradio_demo_image.py` and `gradio_demo_interleave.py` presets for the standard Transformers runtime, providing turnkey T2I/X2I and interleaved generation experiences with streaming output. Try the commands in [#Gradio Demo](#3-gradio-demo) to launch both UIs locally.

## Table of Contents

1. [Model & Weights](#1-model--weights)
2. [Quick Start](#2-quick-start)
3. [Gradio Demo](#3-gradio-demo)
4. [Schedule](#4-schedule)
5. [Citation](#5-citation)

## 1. Model & Weights

| Model name               | HF Weight |
| ------------------------ | --------- |
| Emu3.5               | [🤗 HF link](https://huggingface.co/BAAI/Emu3.5/tree/main) |
| Emu3.5-Image                | [🤗 HF link](https://huggingface.co/BAAI/Emu3.5-Image/tree/main) |
| Emu3.5-VisionTokenizer     | [🤗 HF link](https://huggingface.co/BAAI/Emu3.5-VisionTokenizer/tree/main) |


*Note:*  
- **Emu3.5** supports general-purpose multimodal predictions, including interleaved image-text generation and single-image generation (T2I/X2I) tasks.
- **Emu3.5-Image** is a model focused on T2I/X2I tasks for best performance on these scenarios.
- Both models are pure next-token predictors without DiDA acceleration (each image may take several minutes to generate).  
- ⚡ **Stay tuned for DiDA-accelerated weights.**

> 💡 **Usage tip:**  
> For **interleaved image-text generation**, use **Emu3.5**.  
> For **single-image generation** (T2I and X2I), use **Emu3.5-Image** for the best quality.



## 2. Quick Start

### Environment Setup

```bash
# Requires Python 3.12 or higher.
git clone https://github.com/baaivision/Emu3.5
cd Emu3.5
pip install -r requirements/transformers.txt
pip install flash_attn==2.8.3 --no-build-isolation
```
### Configuration

Edit `configs/config.py` to set:

- Paths: `model_path`, `vq_path`
- Task template: `task_type in {t2i, x2i, howto, story, explore, vla}`
- Input image: `use_image` (True to provide reference images, controls <|IMAGE|> tok