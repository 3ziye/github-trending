<div align="center">

<img src="assets/images/logo.png" width="120" alt="jev-chat" />

# jev-chat

### The chat decision assistant

**Read them first, then reply. Before you answer, Jev works out what the other person really means, how risky the moment is and how to respond, then drafts replies you can fill in with one tap. Whether to send is always up to you.**

[![Stars](https://img.shields.io/github/stars/jev-chat/jev-chat-jarvis?style=flat-square&logo=github&label=Stars)](https://github.com/jev-chat/jev-chat-jarvis/stargazers)
[![Platform](https://img.shields.io/badge/platform-Android%20%7C%20Windows%20%7C%20macOS%20%7C%20iOS-lightgrey?style=flat-square)](#download--installation)
[![License](https://img.shields.io/github/license/jev-chat/jev-chat-jarvis?style=flat-square)](../LICENSE)

### 🌐 Official website: **[chatjevs.com](https://chatjevs.com)**

English | [简体中文](README.zh-CN.md) | [Tiếng Việt](README.vi.md) | [Releases](https://github.com/jev-chat/jev-chat-jarvis/releases)

**[Download](#download--installation) · [Products](#products) · [How It Works](#how-it-works) · [Privacy](#privacy-and-risk) · [Community](#community-and-feedback)**

</div>

## ❤️Sponsors

> [Interested in sponsoring the project?](#community-and-feedback)

<details open>
<summary>Show or hide sponsors</summary>

<table>
<tr>
<td width="240" align="center"><a href="https://open.bocha.cn"><img src="assets/images/sponsors/bocha.png" alt="Bocha" width="200"></a></td>
<td>Thanks to <b>Bocha</b> for sponsoring this project! Bocha is a search engine for AI, giving your applications access to information from across the web with clean, accurate, high-quality results. Its services include the Web Search API, Bocha Jev API, and other search and model APIs. <a href="https://open.bocha.cn">open.bocha.cn</a></td>
</tr>
<tr>
<td width="240" align="center"><a href="https://faka.rainlanguage.top"><img src="assets/images/sponsors/xiaoyou.png" alt="Xiaoyou Store" width="200"></a></td>
<td>Thanks to <b>Xiaoyou Store</b> for sponsoring this project! Xiaoyou Store sells digital products and account services, with a selection available to users of this project. <a href="https://faka.rainlanguage.top">Visit the store</a>.</td>
</tr>
<tr>
<td width="240" align="center"><a href="https://agent.ai-tools.cn"><img src="assets/images/sponsors/vytal.jpg" alt="Vytal" width="200"></a></td>
<td>Thanks to <b>Vytal</b> for sponsoring this project! Vytal is an AI video workflow platform with reusable workflows for batch production, making video creation more accessible to content creators, training providers, and small teams. <a href="https://agent.ai-tools.cn">Visit Vytal</a>.</td>
</tr>
</table>

</details>

## Why jev-chat?

When a message lands, the hard part is not typing. It is working out what the other person really means: are they upset, testing you, or just chatting? Most AI tools skip that step and go straight to writing a reply.

**jev-chat** judges first. Its Jev judgment model reads the conversation and works out the other person's intent, the risk in the moment and the best way to respond. Only then does it draft replies, and it fills the one you pick into the message box.

- **Judge before writing** — intent, risk, what they need and the best action come before any draft
- **Checked, ranked replies** — every draft is checked against that judgment and ranked, so the best fit comes first
- **Works where you chat** — WhatsApp, QQ, Feishu and X on Android; chat windows on Windows and macOS; any app through the iOS keyboard
- **You press send** — jev-chat only fills the input box and never sends on its own
- **Your keys, no server of ours** — requests go only to the model provider you configure, with your own key
- **Open source** — MIT licensed, five apps across Android, Windows, macOS and iOS

## Products

| Platform | Product | How you use it | Status |
| :--- | :--- | :--- | :--- |
| Android | [Jev for WhatsApp](../global/README.md) (global edition) | Overlay on WhatsApp chats in English | Preview v0.1.0 |
| Android | [Jev Chat Assistant](../cn/README.en.md) (Chinese edition) | Overlay on QQ, Feishu, X and WhatsApp | v1.7 |
| Windows | [Jev for Windows](https://github.com/jev-chat/jev-chat-windows) | Sits beside your chat window and reads it with screenshots and on-device OCR | Released |
| macOS | [Jev for macOS](https://github.com/jev-chat/jev-chat-jarvis-mac) | Overlay that reads the chat on screen and judges with a local model | Released (Apple Silicon) |
| iOS | [Jev Keyboard](https://github.com/jev-chat/jev-chat-jarvis-ios) | A custom keyboard: copy a message and see intent, risk and replies on the keyboard | Source only, build it yourself |

Both Android editions live in this repository. The other platforms have their own repositories.

## Screenshots

| Global edition · analysis | Global edition · scored replies | Chinese edition · overlay |
| :---: | :---: | :---: |
| <img src="../global/docs/images/states/02-decide.png" width="230" alt="Gl