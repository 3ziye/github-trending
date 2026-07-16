# Hermes Browser Extension

Browser-native side panel for [Hermes Agent](https://hermes-agent.nousresearch.com/docs) — connect active web context through a local gateway, Hermes Cloud, or a self-hosted remote gateway.

> Created by **Jon Komet** (`@abundantbeing`). Community extension for Hermes Agent by Nous Research.

<p align="center">
  <img src="./assets/readme/hermes-browser-demo.gif" alt="Hermes Browser Extension demo showing the side panel reading browser context and composing a Hermes prompt" width="100%" />
</p>

<p align="center">
  <strong>Public alpha v0.1.11 · Load unpacked · Local / Hermes Cloud / Remote · Full Hermes runtime tools</strong><br />
  Not on the Chrome Web Store yet.
</p>

## What it is

Hermes Browser Extension is not a browser chatbot. It is a Chrome/Edge/Chromium side panel for the real Hermes Agent runtime. Choose a local gateway, attach to a signed-in Hermes Cloud agent tab, or connect to a self-hosted remote API/dashboard. Local and remote API connections can use the models, tools, skills, sessions, memory, and MCP servers already configured in Hermes; Cloud and dashboard-ticket connections are intentionally Chat-only.

This repo is specifically for the **Hermes Browser Extension**: the Chrome/Edge/Chromium side-panel integration for Hermes Agent.

## Visual tour

| Side panel | Theme settings | Local agents |
| --- | --- | --- |
| <img src="./assets/readme/hermes-browser-sidepanel.png" alt="Hermes Browser Extension side panel in Mono theme" width="300" /> | <img src="./assets/readme/hermes-browser-theme-picker-v017.png" alt="Hermes Browser Extension appearance settings with color mode and theme picker" width="300" /> | <img src="./assets/readme/hermes-browser-local-agents-v017.png" alt="Hermes Browser Extension settings with connected local agent picker" width="300" /> |
| Browser behavior | Page-only context | Hermes compatibility |
| <img src="./assets/readme/hermes-browser-browser-behavior.png" alt="Hermes Browser Extension browser behavior settings for auto naming, prompt context, and tab-attached panels" width="300" /> | <img src="./assets/readme/hermes-browser-context-scope.png" alt="Hermes Browser Extension context scope menu with Chat only, Follow active tab, and Page only controls" width="300" /> | <img src="./assets/readme/hermes-browser-compatibility.png" alt="Hermes Browser Extension compatibility panel showing fallback modes and connection security" width="300" /> |

### Hermes Web

Open the extension's full view for canonical Hermes sessions, model/runtime control, rich messages, generated media, and accurate session context telemetry in a browser-native workspace.

Hermes Web Alpha currently uses token-backed **Local or Remote API** connections. Hermes Cloud Preview and ticketed remote-dashboard transports remain Chat-only in the side panel; live full-view dashboard handoff is not shipped yet.

<p align="center">
  <img src="./assets/readme/hermes-web-new-session.png" alt="Hermes Web in Nous Light mode showing a connected new-session workspace with session rail, composer, and context inspector" width="100%" />
</p>

<p align="center"><strong>Start a fresh canonical Hermes Web session</strong></p>

<p align="center">
  <img src="./assets/readme/hermes-web-settings-nine-themes.png" alt="Hermes Web settings in Nous Light mode showing all nine appearance themes" width="100%" />
</p>

<p align="center"><strong>Choose from nine themes with Light and Dark modes</strong></p>

<p align="center">
  <img src="./assets/readme/hermes-web-rich-chat.png" alt="Hermes Web in Nous Light mode showing user messages on the right, Hermes messages on the left, rich Markdown, a table, session rail, composer, and context meter" width="100%" />
</p>

<p align="center"><strong>Read rich Hermes responses while canonical history stays attached</strong></p>

## Highlights

- Adds **Hermes Web Alpha**, a full-page browser workspace for canonical Hermes sessions with a session rail, user-right/Hermes-left messages, safe rich Markdown, model/runtime controls, tools, skills, attachments, voice, active-run steering, generated media, and a context/activity/diagnostics inspector.
- Chrome/Edge/Chromium MV3 side panel powered by the Side Panel API.
- Matches Hermes Desktop's three connection choices: **Local gateway**, **Hermes Cloud**, and **Remote gateway**.
- Connects to a configurable local or self-hosted remote Hermes API server. Default: `http://127.0.0.1:8642`.
- Uses **Trusted Dashboard Attach** for Hermes Cloud: an explicitly selected, signed-in HTTPS agent tab mints a short-lived, single-use WebSocket ticket. Tickets stay memory-only and Cloud remains Chat-only.
- Supports the same ticketed WebSocket path for a self-hosted remote dashboard when Remote gateway is selected with no API key.
- Auto-syncs connected Hermes providers/models, profiles, skills, sessions, and capabilities.
- Keeps runtime plugins available in the same Hermes session. For example, a connected social or messaging