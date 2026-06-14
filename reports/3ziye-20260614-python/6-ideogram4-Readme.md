<p align="center"><a href="https://ideogram.ai/" target="_blank" rel="noopener noreferrer"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/ideogram_logo_darkmode.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/ideogram_logo.svg">
  <img src="assets/ideogram_logo.svg" alt="Ideogram" width="500">
</picture></a></p>

<p align="center"><em>Ideogram 4: Open image model at the forefront of design</em></p>

<p align="center">
  <a href="https://ideogram.ai/blog/ideogram-4.0/" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Blog-Post-orange" alt="Blog Post"></a>
  <a href="https://github.com/ideogram-oss/ideogram4" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Code-GitHub-181717?logo=github" alt="Code"></a>
  <a href="https://huggingface.co/collections/ideogram-ai/ideogram-4" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Model-HuggingFace-blue?logo=huggingface" alt="Model"></a>
  <a href="https://developer.ideogram.ai/" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/API-developer.ideogram.ai-purple" alt="API"></a>
  <a href="https://ideogram.ai/" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Official%20Site-ideogram.ai-ff69b4" alt="Official Site"></a>
</p>

<p align="center">
  <img src="assets/samples/collage_landscape.jpg" alt="A collage of Ideogram 4 samples spanning photorealism, illustration, typography, and poster design">
</p>


Ideogram 4 is **[Ideogram](https://ideogram.ai)'s first open-weight text-to-image model**. It is a **state-of-the-art foundation model trained from scratch** — not a fine-tune of any existing model. It introduces a new structured JSON prompting interface, with best-in-class multilingual text rendering, deep language understanding, explicit bounding-box layout and color-palette controls, and native 2k resolution images. The easiest way to try the model is online at **[ideogram.ai](https://ideogram.ai/)**.

We believe openness drives innovation, and we invite the research community to innovate with us on the forefront of visual intelligence.

## Table of Contents

1. [News](#news)
2. [Model Zoo](#model-zoo)
3. [Performance](#performance)
4. [Quick Start](#quick-start)
5. [Model Summary](#model-summary)
6. [Prompting Guide](#prompting-guide)
7. [Documentation](#documentation)
8. [Citation](#citation)

## News

* **[2026-06-03]** **Ideogram 4 released!** Inference code and weights
  are now public, and our [technical blog post](https://ideogram.ai/blog/ideogram-4.0/) is live. See the
  [Quick Start](#quick-start) section to generate your first image, or try the
  model online at [ideogram.ai](https://ideogram.ai/).

## Model Zoo

| Model | Params | Weight Quantization | Supported Hardware | Diffusers Support | License |
| :---  | :---:  | :---:        | :---:   | :---:   | :---:   |
| **[Ideogram 4 (nf4)](https://huggingface.co/ideogram-ai/ideogram-4-nf4)** | 9.3B | nf4 | CUDA | Yes | [Ideogram 4 Non-Commercial](model_licenses/LICENSE-IDEOGRAM-4-NON-COMMERCIAL) |
| **[Ideogram 4 (fp8)](https://huggingface.co/ideogram-ai/ideogram-4-fp8)** | 9.3B | fp8 | All | No | [Ideogram 4 Non-Commercial](model_licenses/LICENSE-IDEOGRAM-4-NON-COMMERCIAL) |

We plan to support more quantizations in the future.


## Performance

We evaluate Ideogram 4 across third-party arenas and benchmarks, standard
open-source benchmarks, and our own internal human-preference benchmark. Across
all of them, **Ideogram 4 is the best open-weight image model by far, and sits
at the frontier of design.**

### Design Arena

[Design Arena](https://www.designarena.ai/) is a third-party image Elo
leaderboard focused specifically on design-oriented generation. On the overall
board, Ideogram 4 is the top-ranked open-weight model, trailing only proprietary
GPT and Gemini models:

<p align="center">
  <img src="assets/benchmarks/design_arena.png" alt="Design Arena overall image Elo leaderboard with Ideogram 4.0 as the top open-weight model">
</p>

Filtered to open-weight models only, Ideogram 4 leads by a commanding margin,
well ahead of the next-best open model:

<p align="center">
  <img src="assets/benchmarks/design_arena2.png" alt="Design Arena open-weight image Elo leaderboard, with Ideogram 4.0 well ahead of all other open models">
</p>

### ContraLabs

[ContraLabs](https://contralabs.com/research) ran a blind typography evaluation judged by
ten professional designers from Contra's top-earning talent. Ideogram 4 leads on
first-place win rate, picked as the best of four models 47.9% of the time
overall — well ahead of Gemini 3.1 Flash Image Preview (Nano Banana 2) at 30.0%,
FLUX.2 [max] (15.5%), and Grok Imagine 1.0 (15.0%):

<p align="center">
  <img src="assets/benchmarks/contralabs_typography.png" alt="ContraLabs typography first-place win rate, with Ideogram v4 leading">
</p>

It also wins on practical usabil