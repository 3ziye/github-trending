# LeanType

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/leantype_banner_dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/leantype_banner_light.svg">
  <img alt="LeanType Banner" src="docs/images/leantype_banner_light.svg">
</picture>

[![Download](https://img.shields.io/github/v/release/LeanBitLab/HeliboardL?label=Download&style=for-the-badge&color=7C4DFF)](https://github.com/LeanBitLab/HeliboardL/releases/latest) [![Downloads](https://img.shields.io/github/downloads/LeanBitLab/HeliboardL/total?style=for-the-badge&color=7C4DFF&label=Downloads)](https://github.com/LeanBitLab/HeliboardL/releases) [![Stars](https://img.shields.io/github/stars/LeanBitLab/HeliboardL?style=for-the-badge&color=7C4DFF)](https://github.com/LeanBitLab/HeliboardL/stargazers)

**LeanType** is a fork of [HeliBoard](https://github.com/Helium314/HeliBoard) - a privacy-conscious and customizable open-source keyboard based on AOSP/OpenBoard.

This fork adds **optional AI-powered features** using Gemini, Groq, and OpenAI-compatible APIs, offering a hybrid experience: a private, offline core with opt-in cloud intelligence.

## What's New in LeanType

- **[🤖 Multi-Provider AI](docs/FEATURES.md#supported-ai-providers)** - Proofread using **Gemini**, **Groq** (Llama 3, Mixtral), or **OpenAI-compatible** providers.
- **[🛡️ Offline AI](docs/FEATURES.md#5-offline-proofreading-privacy-focused)** - Private, on-device proofreading and translation using ONNX models (Offline build only).
- **🌐 AI Translation** - Translate selected text directly using your chosen AI provider.
- **[🧠 Custom AI Keys](docs/FEATURES.md#4-custom-ai-keys--keywords)** - Assign custom prompts and personas (#editor, #proofread) to 10 customizable toolbar keys.
- **⌨️ Dual Toolbar / Split Suggestions** - Option to split suggestions and toolbar for easier access.
- **🖱️ Touchpad Mode** - Swipe spacebar up to toggle touchpad; custom sensitivity controls.
- **🎨 Modern UI** - "Squircle" key backgrounds, refined icons, and polished aesthetics.
- **🔄 Google Dictionary Import** - Easily import your personal dictionary words.
- **⚙️ Enhanced Customization** - Force auto-capitalization toggle, reorganized settings, and more.
- **🕵️ Clear Incognito Mode** - Distinct "Hat & Glasses" icon for clear visibility.
- **🔍 Clipboard Search** - Search through your clipboard history directly from the toolbar.
- **🔎 Emoji Search** - Search for emojis by name. *Requires loading an Emoji Dictionary.*
- **🔒 Privacy Choices** - Choose **Standard** (Opt-in AI), **Offline** (Hard-disabled network, offline model load), or **Offline Lite** (Minimalist, no AI) versions.

## Screenshots

<table>
  <tr>
    <td><img src="docs/images/1.png" height="500" alt="Screenshot 1"/></td>
    <td><img src="docs/images/2.png" height="500" alt="Screenshot 2"/></td>
    <td><img src="docs/images/3.png" height="500" alt="Screenshot 3"/></td>
    <td><img src="docs/images/4.png" height="500" alt="Screenshot 4"/></td>
    <td><img src="docs/images/5.png" height="500" alt="Screenshot 5"/></td>
    <td><img src="docs/images/6.png" height="500" alt="Screenshot 6"/></td>
  </tr>
</table>


## Download

You can download the latest release from the [GitHub Releases](https://github.com/LeanBitLab/HeliboardL/releases) page.

### 📦 Choose Your Version

#### 1. Standard Version (`-standard-release.apk`)
*   **Features:** Full suite including **AI Proofreading**, **AI Translation**, and **Gesture Library Downloader**.
*   **Permissions:** Request `INTERNET` permission (used *only* when you explicitly use AI features).
*   **Setup:** Use the built-in downloader for Gesture Typing. Configure AI keys in Settings.

#### 2. Offline Version (`-offline-release.apk`)
*   **Features:** All UI/UX enhancements and **Offline Neural Proofreading** (ONNX).
*   **Permissions:** **NO INTERNET PERMISSION**. Guaranteed at OS level.
*   **Best For:** Privacy purists.
*   **Manual Setup Required:**
    *   **Gesture Typing:** [Download library manually](https://github.com/erkserkserks/openboard/tree/46fdf2b550035ca69299ce312fa158e7ade36967/app/src/main/jniLibs) and load via *Settings > Gesture typing*.
    *   **Offline AI:** Download ONNX models and load via *Settings > AI Integration*. 👉 **[See Offline Setup Instructions](docs/FEATURES.md#3-offline-proofreading-privacy-focused)**

#### 3. Offline Lite Version (`-offlinelite-release.apk`)
*   **Features:** All UI/UX enhancements but **NO AI FEATURES**.
*   **Permissions:** **NO INTERNET PERMISSION**. Guaranteed at OS level.
*   **Best For:** Minimalists who want a modern keyboard without any AI components (~20MB size).
*   **Manual Setup Required:**
    *   **Gesture Typing:** [Download library manually](https://github.com/erkserkserks/openboard/tree/46fdf2b550035ca69299ce312fa158e7ade36967/app/src/main/jniLibs) and load via *Settings > Gesture typing*.

## Original HeliBoard Features

<ul>
  <li>Add dictionaries for suggestions and spell check</l