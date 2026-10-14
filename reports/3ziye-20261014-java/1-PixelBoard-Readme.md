# PixelBoard

<div align="center">

**Supercharged Gboard Mod featuring Google Pixel 11 series's Rambler Voice Typing, AI Writing Assistant & Writing Tools V2 [No Root].**

<p>
  <a href="https://github.com/Akshayykadam/PixelBoard/releases/download/v18.4.1-Stable/PixelBoard-18.4.1.apk">
    <img src="https://img.shields.io/badge/📥_Direct_Download-v18.4.1_Stable_(127_MB)-00C853?style=for-the-badge&logo=android&logoColor=white" height="42" alt="Download PixelBoard Stable APK"/>
  </a>
  &nbsp;&nbsp;
  <a href="https://www.apkmirror.com/apk/google-inc/gboard/gboard-the-google-keyboard-18-4-1-985164140-release/">
    <img src="https://img.shields.io/badge/🌐_Stock_Base_APK-APKMirror_(v18.4.1)-FF6F00?style=for-the-badge&logo=google&logoColor=white" height="42" alt="Download Stock Gboard Base APK from APKMirror"/>
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/Akshayykadam/PixelBoard/raw/main/patches/PixelBoard.mpp">
    <img src="https://img.shields.io/badge/📦_Patch_Bundle-PixelBoard.mpp_(1.5_MB)-2979FF?style=for-the-badge&logo=android&logoColor=white" height="42" alt="Download PixelBoard Patch Bundle"/>
  </a>
</p>

<p>
  <img src="https://img.shields.io/badge/Android-10%20to%2016%20Preview-3DDC84?style=flat-square&logo=android&logoColor=white" alt="Android Support"/>
  <img src="https://img.shields.io/badge/Architecture-arm64--v8a-blue?style=flat-square" alt="Arch Support"/>
  <img src="https://img.shields.io/badge/Base%20App-Gboard%20v18.4.1-orange?style=flat-square&logo=google" alt="Base Gboard"/>
  <img src="https://img.shields.io/badge/Root-Not%20Required-success?style=flat-square" alt="No Root"/>
  <img src="https://img.shields.io/badge/License-GPL--3.0-lightgrey?style=flat-square" alt="License"/>
</p>

</div>

---

## Visual Tour & Screenshots

<div align="center">
  <img src="docs/images/showcase.png" alt="PixelBoard Feature Showcase - Rambler Voice Typing, AI Writing Tools & Advanced Settings" width="100%" />
</div>

---

## Overview

**PixelBoard** is a sleek, ultra-clean enhancement of Google's flagship keyboard. Tailored for pure productivity, PixelBoard strips away unnecessary bloatware and focuses strictly on powerhouse capabilities: **Gemini Rambler Natural Voice Dictation**, **AI Writing Assistant**, **Writing Tools V2 Gating**, **Device-Gated Inference Backend Selection**, and **Automatic Zero-Restart Instant Activation**.

PixelBoard is engineered with an independent coexistence package ID (`com.akshaykadam.pixelboard`), allowing you to install and use it **side-by-side with your factory Gboard** without replacing, uninstalling, or risking system keyboard stability.

---

## Key Features

### 1. Gemini "Rambler" Natural Voice Typing
Traditional voice-to-text transcribes every hesitation literally. PixelBoard unlocks Google's state-of-the-art **Rambler** model:
- **Speech Cleanup**: Speak naturally — stutters, false starts, and filler words (*"um"*, *"ah"*, *"like"*, *"you know"*) are filtered out in real-time.
- **Thought Completion**: Seamlessly fixes self-corrections on the fly (e.g., *"let's meet at two no, three PM"* &rarr; *"Let's meet at 3:00 PM"*).
- **Auto-Punctuation & Capitalization**: Adds context-aware periods, commas, and proper noun capitalization without requiring voice commands.
- **Multilingual Fluidity**: Mix and match languages seamlessly in a single sentence.
- **Battery-Friendly Lifecycle**: Cleanly releases speech recognition bindings (`GoogleAsrService`) as soon as the keyboard is hidden, eliminating screen-off battery drain ([#3](https://github.com/Akshayykadam/PixelBoard/issues/3)).
- **Cold Boot & Direct Boot Readiness**: Powered by Device-Protected Storage (DE), ensuring Rambler voice typing is ready immediately after device reboots without needing manual Gboard restarts ([#4](https://github.com/Akshayykadam/PixelBoard/issues/4)).

### 2. In-Line AI Writing Assistant
Access Google's Gemini-driven writing suite directly above your keys across any app:
- **One-Tap Proofread**: Correct spelling, grammatical quirks, and punctuation in an instant.
- **Tone & Style Switcher**: Rephrase sentences into *Professional*, *Casual*, *Concise*, or *Emotive* tones.
- **Smart Edit**: Context-aware editing and quick rephrasing tailored to your conversation.
- **Universal Support**: Works across all keyboard languages and input modes.

### 3. Writing Tools V2 Gating (New in v18.4)
- **Suggested Style Chips & Prompt Bar**: Unlocks Google's modern "Suggested" style chips and the freeform "Describe your edit" prompt bar.
- **Intelligent Hardware Gating**: Integrated with hardware/model eligibility checks to prevent unexpected errors or crashes on unsupported devices.
- **Dedicated In-App Control**: Toggle Writing Tools V2 on/off directly inside Advanced Settings with a clean Material You **BETA** badge.

### 4. Device-Gated AI Inference Backend Selector (New in v18.4)
On supported devices (such as Google Pixel 8 Pro / 9 series), choose your preferred inference pipeline directly under