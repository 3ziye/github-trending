# Droy

**English** · [简体中文](README.zh-CN.md)

<p>
<a href="https://github.com/moonoops/Droy/releases/latest"><img src="https://img.shields.io/github/v/release/moonoops/Droy?style=flat-square&amp;label=Release&amp;color=6554c0" alt="Latest release" /></a>
<a href="#get-started"><img src="https://img.shields.io/badge/Android-11%2B-333333?style=flat-square" alt="Android 11 or later" /></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL--3.0--only-333333?style=flat-square" alt="AGPL-3.0-only license" /></a>
</p>

Droy is an open-source Android AI assistant for conversation, research and phone tasks.

[**Download APK**](https://github.com/moonoops/Droy/releases/latest) · [Installation guide](INSTALLATION.md) · [v0.0.3 release notes](https://github.com/moonoops/Droy/releases/tag/v0.0.3) · [Report an issue](https://github.com/moonoops/Droy/issues)

**ARM64** · Chinese / English

[![Droy Tasks, companion presets and on-screen pets](assets/readme/hero-studio.en.png)](assets/readme/hero-studio.en.png)

Talk to a companion in Messages, or ask an agent to operate your phone in Tasks. The runtime runs on your phone, so you can disconnect your computer after setup. You choose the model service; cloud models need an internet connection.

[Features](#features) · [Install and get started](#get-started) · [Permissions and data](#permissions) · [FAQ](#faq) · [Development](#development)

<a id="features"></a>

## Features

<a id="companions"></a>

### Companion chat

Choose from Kaka, Maimai, Dafeiyu and Lady Claude. A fresh installation creates Kaka, and you can add other companions whenever you want. Each has separate chat history and memory, and can use its own model.

- Change names, avatars, personalities and speaking styles.
- Choose from eight chat backgrounds or upload an image.
- Use stickers and GIFs, search online, or import sticker packs.
- Enable proactive messages and set quiet hours. The default quiet period is 22:00–09:00.

Companions can search the web, organize information and work in the background, then send the results back to the chat. Use Tasks when you want to open an app, tap or enter text on your phone.

[![Companion chat and preset companions](assets/readme/companions-studio.en.png)](assets/readme/companions-studio.en.png)

<a id="agent"></a>

### Phone tasks

Describe what you want to do in Tasks. The agent plans the steps, uses Android Use to inspect pages, tap, swipe and enter text, then checks the result. You can add attachments, use voice input, and organize work into spaces and conversations.

The agent hands sign-in, verification codes and other steps that need your input back to you. You can stop a task at any time.

[![Tasks and permission settings](assets/readme/tasks-studio.en.png)](assets/readme/tasks-studio.en.png)

<a id="pets"></a>

### On-screen pets

Choose a black cat, marmot or alpaca in Pet Studio and preview their animations. During a task, pet bubbles let you check progress, answer questions, pause, resume or stop the task.

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/pets.en.png">
  <img src="assets/readme/pets.en.gif" width="100%" alt="Black cat, marmot and alpaca animations">
</picture>

<a id="memory"></a>

### Memory

Droy extracts useful information from conversations and retrieves relevant records in later chats. Each companion's memory is kept separate, and you can turn it off in that companion's settings.

Companion memory uses MemOS modules for local storage and retrieval. Deleting a companion leaves its memory on your phone. To restore or permanently delete it, make a request in Tasks.

[![Conversation content, companion memory and later chats](assets/readme/memory.bilingual.png)](assets/readme/memory.bilingual.png)

<a id="more"></a>

### Other features

| Feature | Details |
| --- | --- |
| Voice | Hold to speak, voice conversations and reply read-aloud. |
| Notifications | Set rules for selected apps, filter ads and get reminders about important messages. |
| Native interface | Kotlin / Compose, Chinese and English, light and dark themes. Portrait only. |
| Extensions | Skills, plugins, MCP and automation in Tasks through DSH. |

<a id="get-started"></a>

## Install and get started

You need an ARM64 phone running Android 11 or later, with an up-to-date system WebView.

### Install the APK directly (recommended)

1. Download the APK from [Releases](https://github.com/moonoops/Droy/releases/latest), then open and install it on your phone.
2. Follow setup to choose a model service and enter your API key on the phone.
3. Set up the permissions you need, then start a chat in Messages or enter an instruction in Tasks.

The APK includes the runtime. When upgrading, install an APK with the same signature over the existing app.

<details>
  <summary>Or let a computer agent install it over USB</summary>

Connect your phone by USB, enable USB debugging in Developer options, and authorize the computer on your phon