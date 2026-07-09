# Hermes Browser Extension

Browser-native side panel for [Hermes Agent](https://hermes-agent.nousresearch.com/docs) — connect active web context to your local or remote Hermes runtime.

> Created by **Jon Komet** (`@abundantbeing`). Community extension for Hermes Agent by Nous Research.

<p align="center">
  <img src="./assets/readme/hermes-browser-demo.gif" alt="Hermes Browser Extension demo showing the side panel reading browser context and composing a Hermes prompt" width="100%" />
</p>

<p align="center">
  <strong>Public alpha v0.1.10 · Load unpacked · Local/remote Hermes API · Full Hermes runtime tools</strong><br />
  Not on the Chrome Web Store yet.
</p>

## What it is

Hermes Browser Extension is not a browser chatbot. It is a Chrome/Edge/Chromium side panel for the real Hermes Agent runtime. It talks to your Hermes Gateway/API server — local by default, remote when you configure a reachable URL — so it can use the models, tools, skills, sessions, memory, and MCP servers already configured in Hermes.

This repo is specifically for the **Hermes Browser Extension**: the Chrome/Edge/Chromium side-panel integration for Hermes Agent.

## Visual tour

| Side panel | Theme settings | Local agents |
| --- | --- | --- |
| <img src="./assets/readme/hermes-browser-sidepanel.png" alt="Hermes Browser Extension side panel in Mono theme" width="300" /> | <img src="./assets/readme/hermes-browser-theme-picker-v017.png" alt="Hermes Browser Extension appearance settings with color mode and theme picker" width="300" /> | <img src="./assets/readme/hermes-browser-local-agents-v017.png" alt="Hermes Browser Extension settings with connected local agent picker" width="300" /> |
| Browser behavior | Page-only context | Hermes compatibility |
| <img src="./assets/readme/hermes-browser-browser-behavior.png" alt="Hermes Browser Extension browser behavior settings for auto naming, prompt context, and tab-attached panels" width="300" /> | <img src="./assets/readme/hermes-browser-context-scope.png" alt="Hermes Browser Extension context scope menu with Chat only, Follow active tab, and Page only controls" width="300" /> | <img src="./assets/readme/hermes-browser-compatibility.png" alt="Hermes Browser Extension compatibility panel showing fallback modes and connection security" width="300" /> |

## Highlights

- Chrome/Edge/Chromium MV3 side panel powered by the Side Panel API.
- Connects to a configurable local or remote Hermes API server. Default: `http://127.0.0.1:8642`.
- Supports dashboard WebSocket mode when you have a signed-in remote Hermes dashboard tab and no API key.
- Auto-syncs connected Hermes providers/models, profiles, skills, sessions, and capabilities.
- Keeps runtime plugins available in the same Hermes session. For example, a connected social or messaging plugin can add account, post, and trend context while the extension supplies browser-page context.
- Shows a Hermes compatibility panel so older gateways degrade into explicit fallback/manual modes instead of broken route errors.
- Adds **Copy Diagnostics** for v0.1.10 support reports: browser family, version/build, extension origin, gateway origin, capability flags, context mode, selected model/provider, and last visible error with tokens/page content stripped.
- Adds an optional **Hermes Browser Companion Plugin** that passively caches sanitized Browser Context Protocol metadata for Hermes tools/hooks without browser control, network calls, or API-server routes.
- Adds `/meta` / `/metadata` / `/head` for truthful captured-page metadata analysis: it reports only what the Browser context actually contains and explicitly calls out metadata classes that were not captured.
- Adds session controls for Browser work: create/switch sessions, copy session IDs, rename sessions, smart first-message titles, and compact on-brand session actions.
- Adds Browser-scoped model control: Browser model choices and per-session bindings stay inside the extension and do not mutate Hermes global defaults.
- Sends active tab/browser context into a persisted Hermes session, or switches to Chat only when you do not want browser context attached.
- Adds a composer-header context menu for Chat only, following the active tab, pinning a specific tab, and choosing which open tabs appear in the prompt.
- Opens as a tab-attached side panel by default, with a setting to keep the panel global across tabs.
- Opens with a keyboard shortcut (`Alt+H` by default, customizable at `chrome://extensions/shortcuts`).
- Keeps pinned-tab conversations isolated with per-tab local history and Hermes session bindings.
- Adds quick commands for common browser-context work, including `/summarize`, `/explain`, `/rewrite`, `/tabs`, and `/action-items`.
- Adds a collapsible “What Hermes saw” receipt after each sent turn for transparent context/debugging.
- Shows a live Tool Activity Strip while Hermes streams, so tool calls appear as structured runtime activity instead of raw `[tool]` markdown appended into answer