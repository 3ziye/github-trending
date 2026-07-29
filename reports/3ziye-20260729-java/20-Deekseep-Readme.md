# Deekseep LSPosed

An independent LSPosed/Xposed module that adds account, chat, image, interface, and local API tools to the official DeepSeek Android app.

English | [简体中文](README_CN.md)

[![Latest Release](https://img.shields.io/github/v/release/haoyangtu09-art/Deekseep?display_name=tag&sort=semver)](https://github.com/haoyangtu09-art/Deekseep/releases/latest)
[![GitHub Downloads](https://img.shields.io/github/downloads/haoyangtu09-art/Deekseep/total?label=Downloads)](https://github.com/haoyangtu09-art/Deekseep/releases)
[![Android 7.0+](https://img.shields.io/badge/Android-7.0%2B-3ddc84)](#requirements)
[![libxposed API 102](https://img.shields.io/badge/libxposed-API%20102-2f6feb)](#requirements)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> [!WARNING]
> This module modifies the behavior of the official DeepSeek Android app. Back up important data and use it at your own risk.

## Compatibility at a glance

> [!IMPORTANT]
> Deekseep LSPosed 1.7.2 is build-specific. Mainland China and Google Play packages use different obfuscation maps and are not interchangeable.

- Mainland China official build: DeepSeek 2.2.2 (`versionCode 233`) — supported by the stable API 102 and Legacy APKs.
- Google Play build: DeepSeek 2.2.2 (`versionCode 236`) — supported only by the separately labelled Google Play API 102 APK.
- Android: 7.0 or newer (API 24+).
- Recommended framework: current LSPosed with libxposed API 102.
- Traditional compatibility: Xposed API 82+ through the mainland Legacy APK.
- Module scope: `com.deepseek.chat` only.

## Download

### [Download Deekseep LSPosed 1.7.2 — recommended stable API 102](https://github.com/haoyangtu09-art/Deekseep/releases/download/v1.7.2/deekseep-stable-api102-v1.7.2.apk)

This recommended APK is for the mainland China DeepSeek 2.2.2 build (`233`) on current LSPosed. Google Play users must download `deekseep-google-play-2.2.2-v1.7.2.apk` from the [1.7.2 release](https://github.com/haoyangtu09-art/Deekseep/releases/tag/v1.7.2). Verify the DeepSeek `versionCode` before installing.

## Screenshot

<p align="center">
  <img src="docs/images/Screenshot_2026-07-22-22-49-55-25_7614e48627b7380b17b386d382d1b2ef.jpg" alt="Deekseep LSPosed project preview" width="360">
</p>

The screenshot shows the English in-app settings for prompt injection, response-replacement prevention, chat multi-select, and native sign-in entry restoration.

<details>
<summary>More project screenshots</summary>

| Data tools, language, and module information | Experimental features and risk notice |
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
- Export conversations as Markdown, view local statistics, create manual and rotating automatic database backups, and optionally batch-select conversations for deletion.
- Preserve text already delivered to the device when the known client-side `CONTENT_FILTER` replacement event occurs. This cannot recover text the server never sent.

### Account tools

- Save multiple account slots and explicitly add, switch, remove, import, or export selected account records with validation before imported credentials are stored.
- Optionally restore DeepSeek's native Google sign-in entry on the mainland login page, or its native WeChat and SMS entries on overseas login pages. Server-side account, region, and risk checks still apply.

### Image tools

- Reuse or replace images attached to locally edited messages while keeping durable private copies for later rendering.
- Experimentally relay expert-mode image requests through temporary vision sessions and preserve image metadata in local history. Availability remains dependent on the DeepSeek service.

### Developer and API tools

- Run an opt-in, Gateway-Key-protected local/trusted-LAN service that exposes OpenAI Chat Completions/Responses or Anthropic Messages-compatible endpoints through DeepSeek's native transport.
- Use streaming, tool-result continuation, Codex and Claude Code tool loops, deep-thinking parameters, native web search, and live request diagnosti