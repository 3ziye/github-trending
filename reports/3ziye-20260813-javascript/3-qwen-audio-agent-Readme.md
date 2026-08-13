# Qwen Audio Agent

[中文](README_ZH.md) | [English](README.md)

[![CI](https://github.com/QwenAudio/qwen-audio-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/QwenAudio/qwen-audio-agent/actions/workflows/ci.yml)
[![npm](https://img.shields.io/npm/v/qwen-audio-agent)](https://www.npmjs.com/package/qwen-audio-agent)
[![node](https://img.shields.io/badge/node-%E2%89%A522.22.2-brightgreen)](https://nodejs.org/)
[![license](https://img.shields.io/github/license/QwenAudio/qwen-audio-agent)](LICENSE)
[![WeChat](https://img.shields.io/badge/WeChat-join_chat-07C160?logo=wechat&logoColor=white)](#community)

## Agent Presence

Real conversation should not leave you waiting after a single sentence, nor
should it grind to a halt just because the Agent is looking something up,
calling a tool, or working on a task.

Conversation should keep flowing, and the Agent should always be present.

That is why we built **qwen-audio-agent**—a realtime voice runtime that keeps
Agents talking, working, and present. Whether chatting with you, thinking
through a problem, or working on a task, your Agent remains in the
conversation. It listens, responds, and when the task is complete, naturally
tells you:

"It's ready."

## News

- **Unreleased**
  🎙️ Added Qwen3.5-Omni Realtime frontend models; 🔊 Audio and Omni can keep separate voice preferences.
- **2026-08-12 · [v1.8.3](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.8.3)**
  ✨ Refined prompts; 📉 reduced token usage; 🔧 fixed known issues.
- **2026-08-11 · [v1.8.2](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.8.2)**
  🖥️ Refreshed desktop settings with a more consistent visual experience; 🎙️ more reliable voice wake; ⏱️ long-running tasks now report progress automatically.
- **2026-08-11 · [v1.8.1](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.8.1)**
  🧠 Cleaner persona and memory boundaries; 🔧 more reliable tasks and reminders.
- **2026-08-09 · [v1.8.0](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.8.0)**
  🆕 Adds Qwen Code backend; 🔧 fixes known issues.
- **2026-08-07 · [v1.7.0](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.7.0)**
  🎨 The orb opens up custom skins — import your own look, compatible with pet packs from the [Awesome Codex Pet](https://codexpet.top/) community gallery; 🪟 improved Windows backend Agent startup.
- **2026-08-07 · [v1.6.1](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.6.1)**
  ⚡ Task delegation and permission decisions confirm instantly; 🖥️ built-in computer-use lets backend Agents operate the computer out of the box; 🎙️ more reliable wake; 📚 fully bilingual docs.
- **2026-08-06 · [v1.6.0](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.6.0)**
  🪟 Desktop app now officially supports Windows; 🧠 adds invisible memory with automatic extraction after each session.
- **2026-08-05 · [v1.5.0](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.5.0)**
  ⏰ Adds scheduled reminders and progress reporting; 🗣️ adds the voice wake word ("你好千问"); 🐧 desktop build support for Linux; the desktop app now uses a data directory isolated from the CLI.
- **2026-08-05 · [v1.4.2](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.4.2)**
  🔧 Improves desktop backend Agent installation, login, and status detection; refines long-term memory behavior.
- **2026-08-04 · [v1.4.1](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.4.1)**
  🧰 Adds one-click backend Agent install; desktop floating orb supports auto-hide and shortcut recall.
- **2026-08-04 · [v1.4.0](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.4.0)**
  🧠 Adds personalized rules and checklist management; desktop app supports auto-sleep and shortcut wake.
- **2026-08-03 · [v1.3.0](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.3.0)**
  🎙️ Adds [🤗 speech-to-speech](https://github.com/huggingface/speech-to-speech) frontend integration, supporting fully local VAD, STT, LLM, and TTS.
- **2026-08-01 · [v1.2.0](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.2.0)**
  ⚡ Desktop app adds auto-update, faster startup, and improved backend Agent detection.
- **2026-07-31 · [v1.1.0](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.1.0)**
  🤝 Adds Kimi Code CLI backend with native ACP integration.
- **2026-07-30 · [v1.0.0](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v1.0.0)**
  🚀 First stable release, introducing a macOS desktop app with a built-in Gateway.
- **2026-07-28 · [v0.9.0](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v0.9.0)**
  🌍 Project officially open-sourced; backend Agents unified under the ACP architecture.

## Conversation Continues, Tasks Too

Conversation doesn't stop for background tasks; when a task completes, the
result naturally returns to the current conversation:

https://github.com/user-attachments/assets/42022655-36d1-46b2-9c26-ff0765284000

### Core Features

- Full-dupl