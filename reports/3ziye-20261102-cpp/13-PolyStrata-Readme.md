<h1 align="center">PolyStrata</h1>

**English** · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português](README.pt-BR.md)

<p align="center"><b>Run large AI models on your own PC</b><br>
Qwen3.8-Flash-Next, GLM 5.3 Flash, DeepSeek V4 Flash, LFM2.5, Flint, Qwen3.6, Clover, Ornith 1.5, Gemma 4, Tiel Coder, MiniCPM-V and Kolibri 1 · free and open source</p>

<p align="center"><img src="docs/media/speed.svg" width="820" alt="Tokens per second while writing an answer: 94 to 100 for Qwen3.6-35B-A3B on a laptop with an 8 GB card, 394 to 395 on an RTX 5090"></p>

<p align="center"><img src="docs/media/claude-code-demo.gif" width="820" alt="Claude Code in a terminal beside PolyStrata's API Monitor"><br>
<sub>Claude Code on Qwen3.6-35B-A3B UD-Q3_K_M, on the laptop with the 8 GB card, in real time: it adds a <code>--json</code> option to a small program, writes a test for it and runs the tests. The server had read Claude Code's system prompt when it started (<code>"warm_start": true</code>).</sub></p>

<p align="center"><a href="https://github.com/Niko1221/Strata/releases/download/v0.1.10/Pagoda.mp4"><img src="docs/media/pagoda-preview.webp" width="720" alt="A voxel pagoda garden the model wrote, running in the browser"></a><br>
<sub>A voxel pagoda garden, 1 shot prompt running on an RTX 5070 with <a href="https://github.com/Niko1221/Strata">Strata</a> (Qwen3.8-Flash-Next IQ3_S, 128K context) ·
<a href="https://github.com/Niko1221/Strata/releases/download/v0.1.10/Pagoda.mp4">full video (49 s)</a></sub></p>

PolyStrata runs large AI models on a normal PC, models that usually need a server. They chat, write code and work
with your apps and coding agents. Nothing leaves your PC.

It runs twelve models, on two engines:

- **[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)** on an NVIDIA or AMD graphics card with
  12 GB or more, on Windows or Linux. It also reads pictures. Its engine is the Strata project's, unchanged.

The other eleven run on an engine written for PolyStrata, with one NVIDIA card or [two](docs/MULTI_GPU.md#the-strata-poly-models): on Linux, and all but GLM 5.3 Flash and
DeepSeek V4 Flash on Windows too. They are experimental: they have run on one PC with a 32 GB card, and the eight smaller ones on a laptop
with an 8 GB card as well.

- **[GLM 5.3 Flash](docs/models/glm.md)**, the largest: a file of 79 to 114 GB, most of which stays in RAM.
- **[DeepSeek V4 Flash](docs/models/deepseek.md)**, a file of 91 GB, most of which stays in RAM too. Its memory of a
  conversation is small: a 128K context takes 0.7 GB more VRAM than 32K.
- **[LFM2.5-24B-A2B](docs/models/lfm25.md)** by Liquid AI, a file of 11 to 25 GB. Most of its layers have no attention, so a
  long conversation takes little VRAM: a 128K context takes 2 GB more than 32K. Its license allows commercial use
  only to companies with less than 10 million dollars of yearly revenue.
- **[Flint 40B-A2.5B](docs/models/flint.md)** by Recursive, made for coding agents: a file of 18 to 42 GB. Most of its layers
  look back only 513 tokens, so a long conversation takes little VRAM: a 128K context takes 2.6 GB more than 32K.
- **[Qwen3.6-35B-A3B](docs/models/qwen36.md)**, a file of 13 to 23 GB. It also reads pictures.
- **[Clover-35B-A3B-Preview](docs/models/clover.md)** by DiffuSpace, Qwen3.6-35B-A3B trained further to also write a
  block of tokens at once: a file of 13 to 21 GB. It reads text only.
- **[Ornith 1.5](docs/models/ornith.md)**, which has Qwen3.6-35B-A3B's architecture and other weights: a file of 14 to 24 GB. It
  also reads pictures.
- **[Gemma 4 26B-A4B](docs/models/gemma4.md)**, a file of 11 to 17 GB. It also reads pictures.
- **[Tiel Coder 35B-A3B](docs/models/tiel.md)**, Ornith 1.5 quantized for coding agents by peculiar-ragdoll: a file of
  14 to 23 GB. It also reads pictures.
- **[MiniCPM-V 4.7 35B-A3B](docs/models/minicpmv.md)** by OpenBMB, which has Qwen3.6-35B-A3B's architecture and weights of its
  own, made to read pictures: a file of 16 to 29 GB.
- **[Kolibri 1](docs/models/kolibri.md)** by Aleph Alpha, which writes German as well as English: a file of 29 to 48 GB,
  most of which stays in RAM beside a small card.

The server can change between installed models while it runs ([how](docs/BACKENDS.md#changing-the-model)).

PolyStrata is built on [Strata](https://github.com/Niko1221/Strata) by Niko1221.
Why it is a separate repo, AMD and smaller cards, fine-tunes and other questions: [FAQ](docs/FAQ.md).

## How fast is it?

A token is about ¾ of a word.

- **Writes answers:** how fast the reply appears in a short chat. 60 tokens per second is faster than you can read.
- **Reads your prompt:** how fast it takes in what you send (a document, code or a chat history).

The table gives the size the installer takes for each model, in tokens per second. Every size's numbers, the comparison with llama.cpp and how they were measured are on eac