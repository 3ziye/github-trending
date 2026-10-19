<h1 align="center">Project Maya</h1>

<p align="center"><b>A 321-billion-parameter AI model on your own GPU</b><br>
GLM-5.3-Flash, private and fast · one NVIDIA GPU or up to 16 · AMD and Windows (experimental) · chat, pictures,
OpenAI- and Anthropic-compatible API · several requests at once</p>

<p align="center">Created and led by <b>Peasant Smith</b> (<a href="https://github.com/mw00">@mw00</a>), co-maintained
with <b><a href="https://github.com/needmorevram">@needmorevram</a></b></p>

<p align="center"><a href="https://buymeacoffee.com/peasantsmith">☕ Support Project Maya - buy me a coffee</a></p>

Models this size usually need a datacenter. Maya runs **[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**
(zai-org, MIT license) on the hardware you already have: 321 B parameters, about 18 B active per token, and a context
of up to 1 M tokens. Its engine is built for this one model. It keeps the experts your conversation uses most on the
GPU, the next ones in RAM and the rest on your NVMe SSD, and moves them as you chat. It measures your GPUs, CPU, RAM
and SSD and tunes itself to them. Nothing leaves your machine.

- **Fast:** up to 118 tokens/s on four RTX 4090s, 81 on one RTX PRO 6000, 30+ on a single RTX 5090. Real numbers from
  real users below.
- **Close to the original:** Maya's own quants keep 97.7-99.2% of the FP8 model's zero-shot accuracy.
- **Plugs into your tools:** OpenAI- and Anthropic-compatible API with tool calls, ready for coding agents.
- **Several requests at once:** up to 8 answered together - for agents that run several sessions, or several people
  on one PC.
- **Everything in the box:** a chat and a live monitor in the browser, pictures, thinking levels, a one-command setup.

## The models

Project Maya's own quants of GLM-5.3-Flash, made from Z.ai's FP8 release with statistics from the FP8 model. Each keeps
the model's MTP block, which drafts tokens ahead.

| Model | Size | Made for | Against the FP8 model |
| --- | ---: | --- | --- |
| **Maya-S** (default) | 96.5 GB | PCs with a smaller memory pool (RAM and VRAM together) | 97.9% of its zero-shot accuracy; the same next token 83% of the time |
| **Maya-S24** | 94.7 GB | cards of 24 GB or less: 4-bit attention leaves ~1.5 GB more of the card for experts, decode +14% | 97.7%; 83% |
| **Maya-M** | 116 GB | a bigger memory pool; more bits where they count, calibrated toward tool calls and front-end code | 97.9%; 86% |
| **Maya-M-Derisked** | 116 GB | Maya-M with a weight edit by [Blackfrost_AI](https://x.com/Blackfrost_AI) that reduces blanket refusals ([its repo](https://huggingface.co/peasantsmith/GLM-5.3-Flash-Maya-M-Derisked-IQ2_S-GGUF)); experimental | not measured yet |
| **Maya-L** | 156.3 GB | the biggest memory pools | **99.2%**; 90% |

The setup asks which one to download and recommends one for your PC. How they're made and measured: [MAYA-S](bench/results/MAYA-S.md),
[MAYA-S24](bench/results/MAYA-S24.md), [MAYA-M](bench/results/MAYA-M.md), [MAYA-L](bench/results/MAYA-L.md). On
[Hugging Face](https://huggingface.co/peasantsmith/GLM-5.3-Flash-Maya-GGUF).

<details>
<summary>Community quants that also run on Maya</summary>

| Model | Size | How | Notes |
| --- | ---: | --- | --- |
| [EXL3 3.05 bpw](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/3.05bpw) by turboderp | 125.3 GB | in the setup: `--model EXL3-3.05bpw` | NVIDIA only, experimental |
| [EXL3 4.05 bpw](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/4.05bpw) by turboderp | 165.2 GB | in the setup: `--model EXL3-4.05bpw` | NVIDIA only, experimental |

</details>

## How fast is it?

Real machines, real numbers, most of them measured with `./maya.sh --bench`. A token is about ¾ of a word.

| Machine | Model | Decode (writing the answer) | Prefill (reading your prompt) | By |
| --- | --- | ---: | ---: | --- |
| **4x RTX 4090 24 GB** (PCIe 4.0 x16), Xeon w7-3445, 62 GB RAM | Maya-S24 | **118 tokens/s** | 4129 tokens/s | @0xPreDa (v1.0.31, #89) |
| **RTX PRO 6000 Blackwell 96 GB**, Ryzen 7 9800X3D, 61 GB RAM | Maya-M, 256K context | **81.0 tokens/s** | 3102 tokens/s | @yundddd (v1.1.7, #172) |
| **2x NVIDIA CMP 170HX 64 GB** (PCIe Gen2 x4 each), 2x Xeon E5-2690 v4, 91 GB RAM | Maya-M, every expert in VRAM | 61.3 tokens/s | 514 tokens/s | @ZackO2o (v1.0.6, #22) |
| **2x RTX 5880 Ada 45 GB** (PCIe 4.0 x16), Xeon Gold 5420+, 393 GB RAM | Maya-L, 256K context | 54.5 tokens/s | 1401 tokens/s | @vjsyong (v1.1.4, #149) |
| **2x Tesla V100 32 GB** (PCIe 3.0 x16 each), 2x Xeon Gold 6138, 183 GB RAM | Maya-S24 | 54.5 tokens/s | 542 tokens/s | maintainer (v1.1.13, #226) |
| **2x RTX 3090 24 GB** (PCIe 4.0 x16, power-capped at 225 W), Threadripper 3970X, 128 GB RAM | Maya-S24 | 53.0 tokens/s | 885 tokens/s | @briepala (v1.1.2, #135) |
| **4x Tesla V100 32 GB** (PCIe 3.0 x16), 24 CPU cores, a 100 GiB RAM limit | Maya-L, 32K context | 48.3 tokens/s (after `--calibrate`) | 499 tokens/s | @areslp (v1.1.3, [#130](https://github.com/mw00/project-maya/issues/1