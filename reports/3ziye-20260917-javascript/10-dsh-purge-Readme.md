<p align="center">
  <img src="docs/banner.svg" alt="dsh-purge" width="720">
</p>

<h1 align="center">dsh-purge</h1>

<p align="center"><strong>Version 1.3.6</strong></p>

<p align="center">
    <em>DeepSeek Harness jailbreak (破甲): every model can jailbreak; swap prompts per model. Default prompt for Chinese models — 小码酱. Please star ⭐</em>
</p>

<p align="center">
  <a href="https://github.com/YuJunZhiXue/dsh-purge/stargazers"><img src="https://img.shields.io/github/stars/YuJunZhiXue/dsh-purge?logo=github&label=Stars" alt="GitHub stars"></a>
  <a href="https://github.com/YuJunZhiXue/dsh-purge/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-65a30d?style=flat" alt="MIT license"></a>
  <a href="https://awesome-dsh-plugin.com"><img src="https://awesome-dsh-plugin.com/badge.svg" alt="awesome · DSH plugin"></a>
  <a href="https://deepseek.stream/plugins/dsh-purge"><img src="https://img.shields.io/badge/Hub-dsh--purge-1a73e8" alt="DeepSeek Harness Hub"></a>
  <a href="https://www.deepseek.com/harness/"><img src="https://img.shields.io/badge/dsh-0.1.5--rc.1-blue" alt="DSH"></a>
  <br>
  <img src="https://img.shields.io/badge/Node.js-%3E%3D22-339933?logo=node.js&logoColor=fff" alt="Node.js">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000" alt="JavaScript">
</p>

<p align="center">
  <a href="README.md">English</a> | <a href="README.zh-CN.md">中文</a>
</p>

> Aligned with **dsh 0.1.5-rc.1** (Node.js **≥18**; Windows no-flash import hooks need **Node ≥22** `registerHooks`, older Node still gets file-level `windowsHide` patches). On other versions, unmatched originals stay pending or skipped. Nothing is rewritten blindly.
>
> Also accepts the 0.1.2 community `dsh-persona text` field and `dsh-mnemon` v0 session `summary`. After install you still need **Apply + restart**.

---

## ☕ Sponsor

If dsh-purge helps you, a tip is welcome.

<p align="center">
  <img src="docs/appreciate.png" alt="WeChat appreciate" width="360">
</p>

<p align="center">
  <sub>Built by 小杨 · for DeepSeek Harness</sub>
</p>

---

## 🛡️ Why a local harness purge

Models now sit inside a local Agent / Harness. Prompts, approval gates, sandbox policy, and session migration all rewrite behavior at runtime. Asking “will the model answer” is not enough if the host layer kills a lawful eval request first.

1. **Map the host guardrail, not just the model.** Reversible patches on the installed `@deepseek-ai/*` packages show which refusals come from the model and which come from default copy, approval ladders, or session-format checks.
2. **Keep official capabilities; drop refusal locks.** No second invented identity. Persona is whatever you put in `prompt-inject.md`.
3. **Survive upgrades.** Patches re-apply after npm overwrites `node_modules`. Unmatched originals skip so a 0.1.5 tree is not smashed blindly.

This is a local Harness plugin. It is not a public scanner and not an attack kit for third-party sites.

---

> ### ⚠️ Strict Legal & Compliance Disclaimer
>
> **Zero-tolerance notice:** This project opposes and forbids any illegal activity. The authors do not support, encourage, or assist unauthorized network attacks, exploit use, data theft, unlawful access to computer systems, or generation of illegal content.
>
> 1. **Authorized, controlled scope only.** `dsh-purge` is a local DeepSeek Harness red-team research plugin and robustness-eval aid. **Do not run this project or its derived patches against targets, public online systems, or production services without the owner’s lawful written authorization.** All testing must stay on **your authorized local Harness install, offline local synthetic fixtures, authorized cyber-range / lab environments**.
> 2. **No illegal or prohibited use.** You must not use this project, directly or indirectly, to:
>    - violate the Criminal Law of the PRC, the Cybersecurity Law, the Data Security Law, the Personal Information Protection Law, or any other applicable law;
>    - conduct unauthorized intrusion, ransomware, destruction, credential stuffing, or malware distribution;
>    - induce, generate, or spread content that is illegal (national security threats, terrorism, graphic violence, pornography/gambling, fraud, privacy or IP infringement, and any other legally prohibited category);
>    - violate a model provider’s Terms of Service or Usage Policy.
> 3. **You bear all liability.** The project is provided under the MIT license **AS-IS**, with no warranty of completeness, safety, or fitness. **You alone are responsible for every download, deploy, run, modification, and redistribution, and for every input and output that follows** — civil, administrative, and criminal. Authors and contributors accept no direct, indirect, or joint liability for misuse.
> 4. **Breach terminates the license.** Anyone who uses this project for illegal attacks, malicious activity, or other violations loses the open-source license **automatically and irrevocably** from th