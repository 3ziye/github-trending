<p align="center">
  <img src="assets/hero.png" alt="agent-vision-toolkit — Give text-only LLM agents eyes." width="100%">
</p>

<div align="center">

# agent-vision-toolkit
<a href="https://trendshift.io/repositories/99395?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-99395" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/99395/daily?language=Python" alt="Anionex%2Fagent-vision-toolkit | Trendshift" width="250" height="55"/></a>


[![X (Twitter)](https://img.shields.io/badge/-@anion__ex-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/anion_ex)
[![GitHub stars](https://img.shields.io/github/stars/Anionex/agent-vision-toolkit?style=flat-square&logo=github)](https://github.com/Anionex/agent-vision-toolkit/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Anionex/agent-vision-toolkit?style=flat-square&logo=github)](https://github.com/Anionex/agent-vision-toolkit/forks)
[![License: MIT](https://img.shields.io/github/license/Anionex/agent-vision-toolkit?style=flat-square&color=4EAA25)](https://github.com/Anionex/agent-vision-toolkit/blob/main/LICENSE)

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-green?style=flat-square)](https://agentskills.io)
[![Extensions](https://img.shields.io/badge/-Extensions-3178C6?style=flat-square)](https://github.com/Anionex/agent-vision-toolkit/tree/main/extensions)
[![Shell](https://img.shields.io/badge/-Shell-4EAA25?style=flat-square&logo=gnubash&logoColor=white)](https://github.com/Anionex/agent-vision-toolkit/tree/main/bin)

**What it thinks is what it sees — give any text-only coding agent eyes: image Q&A, long-screenshot OCR, frontend UI restoration, and GUI automation, as a vision toolkit plus a skill, with optional drop-in integration for Codex, Claude Code, Pi, Oh My Pi, and OpenCode.**

🎯 An agent's vision capability doesn't have to live in the model — it can live in the harness.

🌐 [**中文**](README_CN.md) ｜ **English**

</div>

If your agent already runs on a text-only model such as DeepSeek but is held back by the lack of multimodality — unable to see images, with every attempt to use an image tool blocked by the system — this repository provides tools, skills, and proxy integrations that let text-only models handle visual tasks on equal or even better footing. The goal is to make the experience of using a text-model agent as seamless as using a multimodal one, and ultimately let a tool-equipped text-model agent outperform a native multimodal agent that does not use this toolkit and its methods.

This repository provides two kinds of components:
1. **Vision tool CLIs** — multiple CLIs, plus a skill that teaches the agent when to use each one. Any agent that can invoke a shell can use them.
2. **Seamless integration** *(optional upgrade)* — a transparent local proxy and single-file native plugins, so **images we paste and the agent's built-in image tools both work seamlessly**, with no extra tool installation or additional prompting.

All code has been verified in real Codex + DeepSeek sessions, and the same pipeline has been live-verified end-to-end in Claude Code, Pi, Oh My Pi, and OpenCode.

> If this project helps you or gives you some inspiration, feel free to star🌟 & fork.

## ❤️ Sponsor

> Want to sponsor this project? See [FUNDING.md](FUNDING.md) or email davidyang042@gmail.com.

<details open>
<summary>Click to collapse</summary>

<table>
<tr>
<td width="220" align="center" valign="middle"><a href="https://aihubmix.com/?aff=sinZ"><img src="assets/logo_aihubmix.png" alt="AIHubMix" height="48"></a></td>
<td valign="middle">Thanks to <a href="https://aihubmix.com/?aff=sinZ">AIHubMix</a> for sponsoring this project! AIHubMix is a stable, high-concurrency AI model API gateway that connects Claude, GPT, Gemini, DeepSeek, and other mainstream models through a single API key, compatible with multiple protocols, with <b>free model options</b> available. Users in China can use it via the <a href="https://inferera.com/?aff=sinZ">China entry</a>, and users abroad via the <a href="https://aihubmix.com/?aff=sinZ">Global entry</a>.</td>
</tr>
<tr>
<td width="220" align="center" valign="middle"><a href="https://api.ewo.so/register?aff=U6PT7J"><img src="assets/logo_eapi_dark.png" alt="E-API" height="48"></a></td>
<td valign="middle">Thanks to <a href="https://api.ewo.so/register?aff=U6PT7J">E-API</a> for sponsoring this project! E-API aggregates mainstream AI models behind OpenAI-, Anthropic-, and Codex-compatible APIs, with selected Claude models up to <b>98% below official prices</b> and DeepSeek V4 models about <b>25% below official prices</b>.</td>
</tr>
</table>

</details>

## Latest Update

**2026-08-18 — Skill renamed:** the included agent skill is now `vision-skills` (formerly `vision-tools`), so the name describes the capability rather than the underlying tools.

**2026-08-13 — Native DeepSeek Harness support is now avai