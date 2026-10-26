<h1 align="center">Project Maya</h1>

<p align="center"><b>GLM-5.3-Flash (321 B) and DeepSeek-V4.1-Flash-1017 (748 B) on your own GPU</b><br>
private and fast · one NVIDIA GPU or up to 16 · AMD and Windows (experimental) · chat, pictures, OpenAI- and
Anthropic-compatible API · several requests at once</p>

<p align="center">
<a href="https://huggingface.co/peasantsmith/GLM-5.3-Flash-Maya-GGUF"><img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fmodels%2Fpeasantsmith%2FGLM-5.3-Flash-Maya-GGUF%3Fexpand%3DdownloadsAllTime&amp;query=%24.downloadsAllTime&amp;label=GLM-5.3-Flash%20Maya%20downloads" alt="GLM-5.3-Flash Maya downloads"></a>
<a href="https://huggingface.co/peasantsmith/GLM-5.3-Flash-Maya-M-Derisked-IQ2_S-GGUF"><img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fmodels%2Fpeasantsmith%2FGLM-5.3-Flash-Maya-M-Derisked-IQ2_S-GGUF%3Fexpand%3DdownloadsAllTime&amp;query=%24.downloadsAllTime&amp;label=Maya-M-Derisked%20downloads" alt="Maya-M-Derisked downloads"></a>
<a href="https://huggingface.co/peasantsmith/DeepSeek-V4.1-Flash-1017-Maya-GGUF"><img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fmodels%2Fpeasantsmith%2FDeepSeek-V4.1-Flash-1017-Maya-GGUF%3Fexpand%3DdownloadsAllTime&amp;query=%24.downloadsAllTime&amp;label=DeepSeek-V4.1-Flash%20Maya%20downloads" alt="DeepSeek-V4.1-Flash Maya downloads"></a>
</p>

<p align="center">Created and led by <b>Peasant Smith</b> (<a href="https://github.com/mw00">@mw00</a>), co-maintained
with <b><a href="https://github.com/needmorevram">@needmorevram</a></b></p>

<p align="center"><a href="https://buymeacoffee.com/peasantsmith"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50"></a><br>
<sub>Project Maya is free. If it runs well on your PC, a coffee keeps the work on it going.</sub></p>

Models this size usually need a datacenter. Maya runs **[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)**
(zai-org, MIT license; 321 B parameters, about 18 B active per token, a context of up to 1 M tokens) and
**[DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)** (DeepSeek, MIT license;
748 B parameters) on the hardware you already have. Each model has an engine built for it. It keeps the experts your
conversation uses most on the GPU, the next ones in RAM and the rest on your NVMe SSD, and moves them as you chat. It
measures your GPUs, CPU, RAM and SSD and tunes itself to them. Nothing leaves your machine.

- **Fast:** up to 124 tokens/s on two H100s, 118 on four RTX 4090s, 81 on one RTX PRO 6000, 30+ on a single RTX 5090. Real numbers from
  real users below.
- **Close to the original:** Maya's own quants of GLM-5.3-Flash keep 97.7-99.2% of the FP8 model's zero-shot
  accuracy; Maya-S of DeepSeek-V4.1-Flash-1017 picks the same next token as the original 92.6% of the time.
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

### DeepSeek-V4.1-Flash-1017 (new)

The setup also offers **[DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)**
(DeepSeek, MIT license; 748 B parameters) on an engine of its own (`maya-ds4`): `./setup.sh --setup` and pick it, or
`./setup.sh --model DeepSeek-V4.1-Flas