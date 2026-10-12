<h1 align="center">Project Maya</h1>

<p align="center"><b>A 321-billion-parameter AI model on your own GPU</b><br>
GLM-5.3-Flash, private and fast · one NVIDIA GPU or up to 16 · AMD and Windows (experimental) · chat, pictures,
OpenAI- and Anthropic-compatible API · several requests at once</p>

<p align="center"><a href="https://buymeacoffee.com/peasantsmith">☕ Support Project Maya - buy me a coffee</a></p>

Models this size usually need a datacenter. Maya runs **[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**
(zai-org, MIT license) on the hardware you already have: 321 B parameters, about 18 B active per token, and a context
of up to 1 M tokens. Its engine is built for this one model. It keeps the experts your conversation uses most on the
GPU, the next ones in RAM and the rest on your NVMe SSD, and moves them as you chat. It measures your GPUs, CPU, RAM
and SSD and tunes itself to them. Nothing leaves your machine.

- **Fast:** up to 118 tokens/s on four RTX 4090s, 30+ on a single RTX 5090. Real numbers from real users below.
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

## How fast is it?

Real machines, real numbers, most of them measured with `./maya.sh --bench`. A token is about ¾ of a word.

| Machine | Model | Decode (writing the answer) | Prefill (reading your prompt) | By |
| --- | --- | ---: | ---: | --- |
| **4x RTX 4090 24 GB** (PCIe 4.0 x16), Xeon w7-3445, 62 GB RAM | Maya-S24 | **118 tokens/s** | 4129 tokens/s | @0xPreDa (v1.0.31, #89) |
| **2x NVIDIA CMP 170HX 64 GB** (PCIe Gen2 x4 each), 2x Xeon E5-2690 v4, 91 GB RAM | Maya-M, every expert in VRAM | 61.3 tokens/s | 514 tokens/s | @ZackO2o (v1.0.6, #22) |
| **2x Tesla V100 32 GB** (PCIe 3), Xeon E5-2690 v4, 30 GB RAM | Maya-S | up to 40 tokens/s | up to 670 tokens/s | maintainer |
| **RTX 5090 32 GB**, Ryzen 9 7950X, 96 GB DDR5 | Maya-M | 30+ tokens/s | ~2000 tokens/s | @siganos (#43) |
| **4x RTX 3080 20 GB**, 64 GB DDR4 | Maya-M, 512K context | 26.3 tokens/s (a day of use) | - | @CoolJohn-lab (#104) |
| **4x Tesla T4 16 GB**, Xeon E5-2660 v2, 220 GB RAM | Maya-S | 22.6 tokens/s | 416 tokens/s | @ksanislo (v1.0.16, #36) |
| **1x Tesla V100 32 GB** (PCIe 3), Core i5-12600T, 64 GB RAM | Maya-S | up to 19 tokens/s | up to 620 tokens/s | maintainer |
| **AMD Radeon 8060S** (Ryzen AI Max+ 395, 128 GB, 96 GB of it for the GPU), Windows 11 | Maya-S | 18.3 tokens/s | 320 tokens/s | @LIN-LAB-AI (v1.0.30, #102) |
| **RTX 4090 24 GB**, Ryzen 9 9950X3D, 192 GB DDR5, Windows 11 | Maya-L, 128K context | 16.4 tokens/s | 1371 tokens/s | @npc97 (v1.0.24, #63) |
| **RTX 5090 Laptop 24 GB**, Core Ultra 9 275HX, 64 GB RAM, Windows 11 (a laptop) | Maya-S24 | 14.5 tokens/s | 994 tokens/s | @klvnblst (v1.0.30, #67) |

Prefill is an 8K-token prompt. The speed holds as a conversation grows, and the first answers after a start are the
slowest while the caches fill with what you use. Share yours: `--bench`, then `--report`, in a
[GitHub issue](https://github.com/mw00/project-maya/issues).

**Several requests at once** (`--parallel`) add up: on one GPU a token of each goes through the model together, so
the dense weights are read once for all of them. In tokens per second for all of them together, against the 