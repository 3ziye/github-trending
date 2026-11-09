<div align="center">

# 🦊 ruyiJS

### Run any site's JavaScript from Python — with the real Firefox engine.

**A new-generation, minimalist browser purpose-built for AI-driven automation.**<br>
The authentic Firefox JavaScript engine and networking stack, with no window and no renderer —<br>
made for web scraping, JS reverse engineering, data collection, and getting past bot checks.

[![PyPI](https://img.shields.io/pypi/v/ruyijs?label=pypi&color=111111&logo=pypi&logoColor=white)](https://pypi.org/project/ruyijs/) [![Downloads](https://img.shields.io/pepy/dt/ruyijs?label=downloads&color=111111&logo=pypi&logoColor=white)](https://pepy.tech/projects/ruyijs) [![Python](https://img.shields.io/badge/Python-%E2%89%A53.10-111111?logo=python&logoColor=white)](https://pypi.org/project/ruyijs/) [![License](https://img.shields.io/badge/license-AGPL--3.0%20%2B%20commercial-111111)](LICENSE) [![Windows](https://img.shields.io/badge/Windows%20x64-0078D4?logo=windows&logoColor=white)](https://pypi.org/project/ruyijs/) [![macOS](https://img.shields.io/badge/macOS%20arm64-000000?logo=apple&logoColor=white)](https://pypi.org/project/ruyijs/) [![Linux](https://img.shields.io/badge/Linux%20x86__64-FCC624?logo=linux&logoColor=black)](https://pypi.org/project/ruyijs/) [![LinuxDO](https://img.shields.io/badge/LinuxDO-community-FFB003?logo=discourse&logoColor=white)](https://linux.do/t/topic/3078486)

<sub>Sponsored by</sub>

<a href="https://www.fastaitoken.com"><img src="assets/sponsor-fastaitoken.png" height="42" alt="FastAIToken"></a>&nbsp;&nbsp;&nbsp;<a href="https://www.fastaitoken.com" title="Claude"><img src="assets/models/claude.svg" width="42" height="42" alt="Claude"></a>&nbsp;&nbsp;<a href="https://www.fastaitoken.com" title="GPT"><img src="assets/models/gpt.svg" width="42" height="42" alt="GPT"></a>&nbsp;&nbsp;<a href="https://www.fastaitoken.com" title="Grok"><img src="assets/models/grok.svg" width="42" height="42" alt="Grok"></a>&nbsp;&nbsp;<a href="https://www.fastaitoken.com" title="DeepSeek"><img src="assets/models/deepseek.svg" width="42" height="42" alt="DeepSeek"></a>&nbsp;&nbsp;<a href="https://www.fastaitoken.com" title="GLM"><img src="assets/models/glm.svg" width="42" height="42" alt="GLM"></a>

<sub>Contributors</sub>

<a href="https://github.com/Facetomyself" title="Facetomyself · #4 macOS arm64 shell, #6 QUIC profiles, #7 macOS proxy, #9 macOS Necko adapter, #14-21 DOM and layout speed, #22-29 DOM, layout and style speed"><img src="assets/contributors/Facetomyself.png" width="48" height="48" alt="Facetomyself"></a>&nbsp;&nbsp;<a href="https://github.com/Starktomy" title="Starktomy · #5 Linux runtime"><img src="assets/contributors/Starktomy.png" width="48" height="48" alt="Starktomy"></a>&nbsp;&nbsp;<a href="https://github.com/isesword" title="isesword · #8 macOS Core Text shaping and Firefox parity"><img src="assets/contributors/isesword.png" width="48" height="48" alt="isesword"></a>&nbsp;&nbsp;<a href="https://github.com/sbbbsbbb" title="sbbbsbbb · #10 macOS TLS and HTTP/2"><img src="assets/contributors/sbbbsbbb.png" width="48" height="48" alt="sbbbsbbb"></a>

**[Install](#-installation)** &nbsp;·&nbsp; **[Features](#-features)** &nbsp;·&nbsp; **[Verification systems](#-verification-systems-it-defeats)** &nbsp;·&nbsp; **[Examples](#-examples)** &nbsp;·&nbsp; **[FAQ](#-faq--troubleshooting)** &nbsp;·&nbsp; **[Contact](#-contact)** &nbsp;·&nbsp; **[LinuxDO](https://linux.do/t/topic/3078486)** &nbsp;·&nbsp; **English** · [简体中文](README.zh-CN.md)

> **⚠️ Disclaimer:** This project is for researching next-generation AI browsers. Any form of brute-force reverse engineering is strictly rejected. The source code is open source under the AGPL-3.0; closed-source or proprietary use requires a commercial license.

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-dark.svg">
  <img src="assets/architecture.svg" width="880" alt="ruyiJS architecture: your Python code drives a ruyiJS Context — an isolated process holding the SpiderMonkey JS engine, 38 browser contexts, and the Necko network stack — which talks to the target site.">
</picture>

</div>

<br>

## Is ruyiJS for you?

Headless Chrome and Playwright hand you a whole browser: a GPU-rendering, window-managing, memory-hungry process that anti-bot vendors have spent years learning to detect. ruyiJS takes the opposite path — it embeds only the Firefox internals that matter for automation and leaves the rest behind:

- **The real engine, not an impersonation.** Genuine SpiderMonkey (Firefox 159) and the Necko network stack execute a site's JavaScript, challenges, signatures, and fingerprints exactly as Firefox would.
- **Truly headless.** No window, no layout, no renderer. A pure JavaScript + Web API environment that starts fast and stays light.
- **Isolated and reproducible.** Each `Context` is its own process with a persistent JavaScript world and its own proxy, so sessions never leak into each other.
- **Offline when you 