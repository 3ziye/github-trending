<!-- markdownlint-configure-file {
  "MD013": { "tables": false },
  "MD033": { "allowed_elements": ["p", "img"] },
  "MD041": false
} -->

<p align="center">
  <img src="assets/branding/astrlink-logo.png" alt="AstrLink" width="96" />
</p>

# AstrLink

**English** | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

**A local privacy gateway for AI agents: sensitive content is detected and
redacted locally before it reaches any model provider.**

AstrLink is an open-source desktop app for macOS, Windows, and Linux. Before a
request goes upstream, it can detect secrets, email addresses, phone numbers,
and other sensitive content locally, then warn, block, or redact it according to
configured policies. Redacted values can be restored locally in the response, so
agents keep working. It also unifies existing subscriptions and APIs, with model
routing and request records.

[Getting started](#getting-started) ·
[On-device privacy protection](#on-device-privacy-protection) ·
[User guides (Chinese)](docs/guides/README.md) ·
[Contributing (Chinese)](CONTRIBUTING.md)

## Screenshots

Simulated accounts, usage, costs, and request content. Click an image to view it
at full size.

| Overview                                                                                                                   | API providers                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [![Overview with simulated usage](assets/screenshots/overview.en.jpg)](assets/screenshots/overview.en.jpg)                 | [![Providers with simulated accounts and quotas](assets/screenshots/providers.en.jpg)](assets/screenshots/providers.en.jpg)                                  |
| **On-device privacy protection**                                                                                           | **Request details**                                                                                                                                          |
| [![Privacy dry run with a simulated support ticket](assets/screenshots/privacy.en.jpg)](assets/screenshots/privacy.en.jpg) | [![Request details with a simulated agent session and processing trace](assets/screenshots/request-detail.en.jpg)](assets/screenshots/request-detail.en.jpg) |

## Features

- **On-device privacy protection**: Detect sensitive content with local rules or
  a local privacy model. Warn, block, or redact according to your policies, and
  optionally restore placeholders in responses.
- **Subscriptions and APIs in one place**: Connect Codex, Claude, and Grok
  subscriptions, major API providers, Coding Plans, and compatible gateways such
  as New API. Manage accounts and credentials centrally.
- **Model routing**: Redirect requested model names to target models, set
  provider priorities, and configure retries and failover between providers.
- **Multiple API protocols**: Expose OpenAI Responses, Chat Completions,
  Anthropic Messages, and Gemini endpoints, with protocol conversion
  configurable according to upstream capabilities.
- **Request records and usage tracking**: Inspect requests, session traces,
  upstream attempts, and errors. Track usage and estimated costs by provider,
  model, and access token.

## On-device privacy protection

With privacy policies enabled, AstrLink can detect sensitive content, redact
requests, and restore responses locally:

1. **Detect on your device**: Use built-in rules, custom rules, or a local
   privacy model to identify sensitive content such as secrets, email addresses,
   and phone numbers. Rule-based detection requires no model download.
2. **Apply your policies**: Choose to warn, block, or redact. Redaction replaces
   detected sensitive content with placeholders. Configure detection categories
   and allowlists, then check the results with a dry run.
3. **Restore responses when needed**: Enable response restoration to replace
   placeholders returned by the model with their original values, so your agent
   can continue using the results.

The gateway, privacy detection, and redaction run on your device. Inference
requests are still sent to the upstream API providers you configure. What gets
processed depends on your enabled policies and detection results. Request body
capture is off by default and can be enabled separately for troubleshooting.

Local privacy models must be downloaded or imported; see
[Privacy model settings (Chinese)](apps/desktop/README.md#隐私模型). For
thinking signatures and encrypted continuation data, see
[Privacy detection and continuation compatibility (Chinese)](docs/guides/privacy-reasoning-continuation.md).

## Installation

AstrLink is 