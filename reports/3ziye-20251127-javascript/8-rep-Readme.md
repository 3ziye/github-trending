<p align="center">
  <!-- Chrome Supported -->
  <img src="https://img.shields.io/badge/Chrome-Supported-4285F4?logo=googlechrome&logoColor=white" alt="Chrome Supported">

  <!-- AppSec Tool -->
  <img src="https://img.shields.io/badge/AppSec-Tool-blueviolet" alt="AppSec Tool">

  <!-- Bug Bounty Friendly -->
  <img src="https://img.shields.io/badge/Bug%20Bounty-Friendly-orange" alt="Bug Bounty Friendly">

  <!-- Stars -->
  <a href="https://github.com/bscript/rep/stargazers">
    <img src="https://img.shields.io/github/stars/bscript/rep?style=social" alt="GitHub Stars">
  </a>

   <!-- Discord -->
  <a href="https://discord.gg/rMcKHSbG">
        <img src="https://img.shields.io/discord/1442955541293961429.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2" alt="Discord">
  </a>

  <!-- Sponsor -->
  <a href="https://github.com/sponsors/bscript">
    <img src="https://img.shields.io/badge/Sponsor-%F0%9F%92%96-ea4aaa?style=flat-square" alt="Sponsor">
  </a>
</p>

# rep+

rep+ is a lightweight Chrome DevTools extension inspired by Burp Suite's Repeater, now supercharged with AI. I often need to poke at a few requests without spinning up the full Burp stack, so I built this extension to keep my workflow fast, focused, and intelligent with integrated LLM support.

[![Watch Demo](https://img.shields.io/badge/Demo-Video-red?style=for-the-badge&logo=youtube)](https://video.twimg.com/amplify_video/1992382891196571648/pl/zE5-oOXgVua1ZBQn.m3u8?tag=14)

## What it does

- **No Proxy Setup**: Works directly in Chrome. No need to configure system proxies or install CA certificates like in Burp Suite.
- **Capture & Replay**: Captures every HTTP request you trigger while testing. Replay any request and freely manipulate the raw method, path, headers, or body to probe endpoints.
- **Multi-tab Capture**: Captures network requests from **all open tabs**, not just the inspected one.
  - **Global Visibility**: Monitor traffic across your entire browser session.
  - **Visual Indicators**: Requests from other tabs are marked with a globe icon 🌍 for easy distinction.
  - **Smart Filtering**: Automatically deduplicates requests to keep your workspace clean.
  - **Privacy First (Optional Permissions)**: Broad permissions (`webRequest`, `<all_urls>`) are **NOT** granted by default. They are requested at **runtime** only when you explicitly click the globe icon to enable this feature. This ensures rep+ remains lightweight and respects your privacy until you need the extra power.
- **Filters & Regex**: Powerful search across URL, headers, and body. Toggle **Regex Mode** for advanced pattern matching (e.g., finding specific tokens or IDs).
- **Converters**: Right-click context menu to instantly encode/decode data:
  - Base64
  - URL Encode/Decode
  - JWT Decode (view payload instantly)
  - Hex / UTF-8
- **Screenshots**: Built-in screenshot tool to capture the request/response pair for bug reports.
- **History & Navigation**: Undo/redo support for edits and history navigation for selected requests.
- **Starring**: Pin important requests to keep them at the top of your list.
- **Clear Workspace**: Instantly clear all captured requests with a single click to start a fresh session.
- **Export & Import**: Export requests as JSON to share findings with teammates or import them later. Perfect for rep+ ↔ rep+ workflows.
- **Bulk Replay**: Burp Suite Intruder-style attacks with four attack modes:
  - **Sniper**: Tests each position independently with its own payloads
  - **Battering Ram**: All positions receive the same payload
  - **Pitchfork**: Zips payloads across positions (index-wise)
  - **Cluster Bomb**: Tests all combinations (Cartesian product)
  
  Mark multiple parameters with `§`, choose your attack type, configure payloads (List or Numbers) for each position, and inspect detailed results for every attempt. Includes pause/resume functionality for long-running attacks.
  - **Response Diff**: Git-style diff view to highlight changes between the baseline response and each attack result. Toggle "Diff View" to see additions (green) and deletions (red) at a glance.
- **Unified Extractor**: A powerful tool to analyze JavaScript files, combining two key features:
  - **Secret Scanner**: Automatically scans captured JS files for hardcoded secrets (API keys, tokens, private keys).
    - **Smart Detection**: Uses entropy analysis and advanced filtering to minimize false positives.
    - **Confidence Scores**: Flags findings as High, Medium, or Low confidence.
  - **Endpoint Extractor**: Extracts API endpoints, URLs, and paths from JS files.
    - **Smart Extraction**: Finds full URLs, relative paths, and GraphQL endpoints.
    - **Method Detection**: Guesses HTTP methods (GET, POST, etc.) from context.
    - **One-Click Copy**: Instantly copy relative paths as full URLs (reconstructs the base URL automatically).
- **Theme Support**: Auto-detects system theme (Light/Dark) and includes a quick toggle button ☀️/🌙 in the UI.
-