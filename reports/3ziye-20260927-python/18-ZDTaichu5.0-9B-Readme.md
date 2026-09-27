# ZDTaichu5.0-9B

English | [简体中文](README_zh.md)

[Blog](https://taichu-ai.github.io/ZDTaichu5.0-9B/) | [ModelScope](https://www.modelscope.cn/models/TaichuAI/ZDTaichu5.0-9B) | [Hugging Face](https://huggingface.co/TaichuAI/ZDTaichu5.0-9B)

## Model Downloads

| Model | Hugging Face | ModelScope |
| --- | --- | --- |
| ZDTaichu5.0-9B | [Hugging Face](https://huggingface.co/TaichuAI/ZDTaichu5.0-9B) | [ModelScope](https://www.modelscope.cn/models/TaichuAI/ZDTaichu5.0-9B) |
| ZDTaichu5.0-9B-FP8 | [Hugging Face](https://huggingface.co/TaichuAI/ZDTaichu5.0-9B-FP8) | [ModelScope](https://www.modelscope.cn/models/TaichuAI/ZDTaichu5.0-9B-FP8) |
| ZDTaichu5.0-9B-NVFP4 | [Hugging Face](https://huggingface.co/TaichuAI/ZDTaichu5.0-9B-NVFP4) | [ModelScope](https://www.modelscope.cn/models/TaichuAI/ZDTaichu5.0-9B-NVFP4) |
| ZDTaichu5.0-9B-DSpark | [Hugging Face](https://huggingface.co/TaichuAI/ZDTaichu5.0-9B-DSpark) | [ModelScope](https://www.modelscope.cn/models/TaichuAI/ZDTaichu5.0-9B-DSpark) |

## Introduction

ZDTaichu5.0-9B is a multimodal foundation model for general visual understanding, spatial reasoning, agentic tool use, and embodied-AI research. It combines a Qwen3.5-9B language backbone with a C-RADIOv4-H vision encoder, supports text, images and videos with any-resolution visual input.

Within the 10B-scale general-purpose VLMs compared in this release blog, ZDTaichu5.0-9B retains first-tier general visual understanding while supporting spatial reasoning, high-level embodied VLM reasoning, and agent tasks under the reported evaluation settings. Rather than trading broad visual competence for specialization, it layers a more comprehensive spatial, embodied, and agent capability profile on top of a strong general-vision foundation.

The model accepts text, one or more images, and video. It is designed for:

- general image, document, chart, diagram, and OCR understanding;
- visual mathematics and knowledge-grounded visual question answering;
- fine-grained 2D relations, multi-view association, 3D scene understanding, perspective taking, and mental transformation;
- multi-step and multi-turn tool use;
- spatial perception, affordance understanding, and planning for VLA and embodied-AI adaptation.

More demos and showcases are provided at 
[Blog](https://taichu-ai.github.io/ZDTaichu5.0-9B/).

## Highlights

- **Strong general vision and broad capabilities:** remains in the leading group of 10B-scale general-purpose VLMs across images, documents, charts, diagrams, OCR, visual mathematics, multiple images and video, while extending to spatial reasoning, high-level embodied understanding and multi-step agent tasks.
- **Leading spatial reasoning and embodied understanding:** leads spatial capability among the compared 10B-scale general-purpose VLMs, with strong results on SparBench, ViewSpatial, MMSI-Bench and MindCube-tiny. Scores of 48 on ERQA and 56 on RoboSpatial cover scene reasoning, affordances and interaction-oriented understanding.
- **Strongest agent capability among the compared 10B-scale general-purpose VLMs:** leads the reported TAU2-Bench (87.7) and Claw-Eval (71.4) comparisons, and reaches 93.7 on IFEval.
- **Entropy-Gated Adaptive Recurrent Reasoning:** Dynamically allocates additional recurrent refinement steps in latent space to more challenging tokens, enabling greater computational depth where needed and improving reasoning performance on complex tasks. Details could be found [Here](https://github.com/Taichu-AI/ZDTaichu5.0-9B/blob/main/recurrent_reasoning/README.md)

## Benchmark Results

The two figures compare ZDTaichu5.0-9B with open and closed models across general visual understanding, spatial and embodied capabilities, and agent and text capabilities.

**Comparison with open models**

![ZDTaichu5.0-9B benchmark comparison with open models](docs/assets/taichu-release-benchmark-comparison.svg)

**Comparison with closed models**

![ZDTaichu5.0-9B benchmark comparison with closed models](docs/assets/taichu-vs-closed-models.svg)

### Spatial and embodied reasoning

<table>
  <thead>
    <tr>
      <th align="left">Area</th>
      <th align="left">Benchmark</th>
      <th align="right">ZDTaichu5.0-9B</th>
      <th align="right">Qwen3.5-9B</th>
      <th align="right">STEP3-VL-10B</th>
      <th align="right">gemma4-8B-E4B</th>
      <th align="right">Gemini 3 Pro</th>
      <th align="right">Grok 4</th>
      <th align="right">GPT-5.2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3" align="left" valign="middle">Basic spatial perception</td>
      <td align="left">CV-Bench</td>
      <td align="right">86.82</td>
      <td align="right"><strong>87.19</strong></td>
      <td align="right">83.49</td>
      <td align="right">68.10</td>
      <td align="right"><ins>90.07</ins></td>
      <td align="right">—</td>
      <td align="right">86.84</td>
    </tr>
    <tr>
      <td align="left">3DSRBench</td>
      <td align="right"><strong>60.96</strong></td>
      <td align="right">56.78<