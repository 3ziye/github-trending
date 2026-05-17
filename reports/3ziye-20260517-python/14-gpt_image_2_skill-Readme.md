<h1 align="center">GPT Image 2 Prompt Gallery + Agentic Skill + CLI</h1>
<p align="center"><em>OpenAI GPT Image 2 prompt gallery, image prompt library, agentic skill, and CLI — curated, copy-paste prompts and runnable examples for skill-capable agents.</em></p>

<p align="center">
  <a href="README.md"><strong>English</strong></a> · <a href="README.zh.md">中文</a>
</p>

<p align="center">
  <a href="https://github.com/wuyoscar/gpt_image_2_skill/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"/></a>
  <a href="https://github.com/wuyoscar/gpt_image_2_skill/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"/></a>
  <img src="https://img.shields.io/badge/model-gpt--image--2-purple.svg" alt="Model: gpt-image-2"/>
  <img src="https://img.shields.io/badge/python-%E2%89%A53.11-blue.svg" alt="Python ≥ 3.11"/>
</p>

<p align="center">
  <a href="https://oosmetrics.com/repo/wuyoscar/gpt_image_2_skill"><img src="https://img.shields.io/static/v1?label=oosmetrics&message=Top%201%20Agents&color=8AA399" alt="oosmetrics Top 1 in Agents by velocity"/></a>
  <a href="https://oosmetrics.com/repo/wuyoscar/gpt_image_2_skill"><img src="https://img.shields.io/static/v1?label=oosmetrics&message=Top%201%20LLMs&color=8798B5" alt="oosmetrics Top 1 in LLMs by velocity"/></a>
  <a href="https://oosmetrics.com/repo/wuyoscar/gpt_image_2_skill"><img src="https://img.shields.io/static/v1?label=oosmetrics&message=Top%201%20CLI&color=A58B9D" alt="oosmetrics Top 1 in CLI by velocity"/></a>
</p>

<p align="center">
  <a href="docs/assets/gptimage2skill-banner.png"><img src="docs/assets/gptimage2skill-banner.png" alt="GPTImage2Skill banner" width="100%"/></a>
</p>

---

## ✨ At a glance

<table border="1" cellspacing="0" cellpadding="6">
  <tr>
    <th align="left">Item</th>
    <th align="left">Value</th>
  </tr>
  <tr>
    <td>Gallery size</td>
    <td><strong>Small but mighty</strong> · curated for signal, not volume; README shows a selected showcase</td>
  </tr>
  <tr>
    <td>Surfaces</td>
    <td><strong>Agentic Skill + CLI</strong> — Claude Code / Codex, OpenClaw, Hermes Agent and other skill-capable agent runtimes</td>
  </tr>
  <tr>
    <td>Last update</td>
    <td><strong>2026-05-05</strong></td>
  </tr>
  <tr>
    <td>Docs</td>
    <td><strong>English + 中文</strong></td>
  </tr>
</table>

---

## 🔎 What this repo is for

Use this repo as a **GPT Image 2 prompt gallery**, **image prompt library**, **example of generation showcase**, **Codex / Claude Code agent skill**, and **gpt-image-2 CLI**. It includes reusable AI image prompts for research paper figures, posters, UI mockups, game HUDs, anime / manga, photography, typography, maps, tattoo design, and reference-image editing workflows.

> This project is not trying to collect every prompt on the internet. We keep a selected set of examples that show what GPT Image 2 can do and how to use it well. Thanks for all the love this little gallery has received 🫶 — if time allows, I will also share the automated patch/update workflow behind it later.

> [!CAUTION]
> For research figures, treat generated images as references, workflow sketches, or reproducible style targets. We do **not** recommend dropping GPT Image 2 outputs directly into a paper as-is; for academic communication, that can be misleading and is generally bad practice.

---

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md).

## 📥 Install

Before installing, check whether the skill or CLI is already available. Do not reinstall blindly, overwrite an existing skill folder, or create/replace API-key files. Use your runtime's own skill list/status command when available; global/shared installs should be an explicit user choice, not an automatic setup step.

```bash
command -v gpt-image || true
command -v uv >/dev/null && uv tool list | grep -E '^gpt-image-cli([[:space:]]|$)' || true
test -n "${OPENAI_API_KEY:-}" && echo "OPENAI_API_KEY is already set (value hidden)"
```

<details>
<summary><strong>Claude Code</strong></summary>

```text
/plugin marketplace add wuyoscar/gpt_image_2_skill
/plugin install gpt-image@wuyoscar-skills
```

</details>

<details>
<summary><strong>Codex</strong></summary>

Codex ships with built-in skill helpers such as `$skill-installer` and `$skill-creator`.
Open Codex and invoke the built-in installer with this GitHub skill-folder URL:

```text
$skill-installer
Install this skill from GitHub:
https://github.com/wuyoscar/gpt_image_2_skill/tree/main/skills/gpt-image
```

The installer downloads that GitHub folder and places it under your Codex skills directory, usually:

```bash
~/.codex/skills/gpt-image
```

Restart Codex after installation so the new `$gpt-image` skill is loaded.

If you prefer to install it manually, copy the skill folder into Codex's skills directory:

```bash
git clone https://github.com/wuyoscar/gpt_image_