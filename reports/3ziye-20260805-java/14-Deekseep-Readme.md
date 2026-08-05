# Deekseep LSPosed

An independent LSPosed/Xposed module that adds account, chat, image, interface, and local API tools to the official DeepSeek Android app.

English | [简体中文](README_CN.md)

[![Latest Release](https://img.shields.io/github/v/release/lllucccian/Deekseep?display_name=tag&sort=semver)](https://github.com/lllucccian/Deekseep/releases/latest)
[![GitHub Downloads](https://img.shields.io/github/downloads/lllucccian/Deekseep/total?label=Downloads)](https://github.com/lllucccian/Deekseep/releases)
[![Android 7.0+](https://img.shields.io/badge/Android-7.0%2B-3ddc84)](#requirements)
[![Xposed API 82–102](https://img.shields.io/badge/Xposed_API-82%20%7C%20100%20%7C%20101%20%7C%20102-2f6feb)](#requirements)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> [!NOTE]
> Deekseep is an independent enhancement module. Check that the APK matches
> your DeepSeek version, and back up important data before using chat, account,
> or experimental tools.

## Compatibility at a glance

> [!TIP]
> Deekseep LSPosed 1.7.3 has exactly two APK downloads: one for Mainland
> China DeepSeek and one for Google Play DeepSeek. Both are multi-API builds.

- Mainland China official build: DeepSeek 2.2.2 (`versionCode 233`) and 2.3.0 (`versionCode 237`).
- Google Play build: only DeepSeek 2.2.2 (`versionCode 236`). The latest Google Play DeepSeek is not supported yet.
- Android: 7.0 or newer (API 24+).
- Xposed interfaces: API 82 / 100 / 101 / 102 in the same universal APK.
- Module scope: `com.deepseek.chat` only.

## Recommended downloads

### [Mainland China — download Deekseep 1.7.3 multi-API](https://github.com/lllucccian/Deekseep/releases/download/v1.7.3/deekseep-mainland-universal-api82-100-101-102-v1.7.3.apk)

For Mainland China DeepSeek 2.2.2 (`233`) or 2.3.0 (`237`).

### [Google Play — download Deekseep 1.7.3 multi-API](https://github.com/lllucccian/Deekseep/releases/download/v1.7.3/deekseep-google-play-universal-api82-100-101-102-v1.7.3.apk)

For Google Play DeepSeek 2.2.2 (`236`) only. The two channel APKs are not interchangeable. Dedicated API 102, Legacy, test, and diagnostic APKs are no longer current release choices.

## Screenshot

<p align="center">
  <img src="docs/images/Screenshot_2026-07-22-22-49-55-25_7614e48627b7380b17b386d382d1b2ef.jpg" alt="Deekseep LSPosed project preview" width="360">
</p>

The screenshot shows the English in-app settings for prompt injection, response-replacement prevention, chat multi-select, and native sign-in entry restoration.

<details>
<summary>More project screenshots</summary>

| Data tools, language, and module information | Experimental features and usage note |
|---|---|
| <img src="docs/images/data-tools-preview.jpg" alt="Deekseep LSPosed data tools and module information" width="320"> | <img src="docs/images/experimental-features-preview.jpg" alt="Deekseep LSPosed Experimental Features page" width="320"> |

</details>

## What is Deekseep LSPosed?

Deekseep LSPosed runs inside the official DeepSeek Android app through a compatible LSPosed/Xposed environment. It adds local conversation and account tools, prompt and interface controls, image workflows, and an optional developer-facing API gateway.

This is an independent third-party project. It is not part of, affiliated with, endorsed by, or supported by DeepSeek.

## Features

### Chat tools

- Import a system prompt and inject it into outgoing requests without changing the visible input box.
- Edit local conversation titles, user messages, model responses, reasoning text, reasoning duration, and message images. Create local conversations and search across prompts, answers, and reasoning.
- Import images as chat wallpaper or stickers. Wallpaper controls include continuous or exact scaling, horizontal/vertical framing, rotation, opacity, display range, fit/crop/stretch, and chat/sidebar/settings binding. Stickers can be moved, resized, rotated, layered, or faded; one-tap offline cutout can save a transparent sticker, with manual erasing as a fallback.
- Export conversations as Markdown, view local statistics, create manual and rotating automatic database backups, and optionally batch-select conversations for deletion.
- Preserve text already delivered to the device when the known client-side `CONTENT_FILTER` replacement event occurs. This cannot recover text the server never sent.

### Account tools

- Save multiple account slots and explicitly add, switch, remove, import, or export selected account records with validation before imported credentials are stored.
- Optionally restore DeepSeek's native Google sign-in entry on the mainland login page, or its native WeChat and SMS entries on overseas login pages. Server-side account, region, and risk checks still apply.

### Image tools

- Reuse or replace images attached to locally edited messages while keeping durable private copies for later rendering.
- Experimentally relay expert-mode image requests through temporary vision sessions and pr