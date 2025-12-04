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

<img width="1661" height="985" alt="Screenshot 2025-11-27 at 18 07 32" src="https://github.com/user-attachments/assets/3e529124-ab0c-4f8f-9e70-d10b2ce29c9e" />


[![Watch Demo](https://img.shields.io/badge/Demo-Video-red?style=for-the-badge&logo=youtube)](https://video.twimg.com/amplify_video/1992382891196571648/pl/zE5-oOXgVua1ZBQn.m3u8?tag=14)

## What it does

- **No Proxy Setup**: Works directly in Chrome. No need to configure system proxies or install CA certificates like in Burp Suite.
- **Capture & Replay**: Captures every HTTP request you trigger while testing. Replay any request and freely manipulate the raw method, path, headers, or body to probe endpoints.
- **Multi-tab Capture**: Captures network requests from **all open tabs**, not just the inspected one.
  - **Global Visibility**: Monitor traffic across your entire browser session.
  - **Visual Indicators**: Requests from other tabs are marked with a globe icon 🌍 for easy distinction.
  - **Smart Filtering**: Automatically deduplicates requests to keep your workspace clean.
  - **Privacy First (Optional Permissions)**: Broad permissions (`webRequest`, `<all_urls>`) are **NOT** granted by default. They are requested at **runtime** only when you explicitly click the globe icon to enable this feature. This ensures rep+ remains lightweight and respects your privacy until you need the extra power.
- **Hierarchical Request Grouping**: Intelligent organization of captured requests for better visibility.
  - **Page-Based Grouping**: Requests are grouped by the page that initiated them (📄 icon).
  - **Third-Party Detection**: Automatically identifies and nests third-party domains (CDNs, APIs, analytics) under the parent page (🌐 icon).
  - **Smart Ordering**: First-party requests appear at the top, followed by third-party domain groups.
  - **Collapsible Tree**: All groups start collapsed by default to keep the view clean. Use the toggle button to expand/collapse all at once.
  - **Context-Aware**: Understand which resources belong to which page, making it easier to analyze complex web applications.
  - **Group Starring**: Star an entire Page Group (📄) or Domain Group (🌐) to track it.
    - **Focused Tracking**: Starring a Page Group only stars first-party requests (same domain), ignoring third-party noise.
    - **Auto-Star**: New requests belonging to a starred group are automatically starred as they arrive.
- **Timeline Filter**: Analyze request sequences with ease.
  - **One-Click Timeline**: Click the clock icon ⏱️ on any request to see a chronological view of all requests that loaded before it.
  - **Flat View**: Removes all grouping to show requests in pure time order (newest first).
  - **Domain Badges**: Each request displays a color-coded domain badge for easy identification across different domains.
  - **Quick Context**: Instantly understand what loaded before a specific request, perfect for debugging race conditions or understanding load sequences.
  - **Toggle Off**: Click the same clock icon again to return to the grouped view.
- **Multiple View Modes**: Inspect requests and responses in different formats.
  - **Pretty View**: Syntax-highlighted JSON, XML, and HTML for easy reading.
  - **Raw View**: See the exact raw text of the request or response.
  - **Hex View**: Binary view with hex dump format, showing offset, hex bytes, and ASCII representation.
- **Layout Toggle**: Switch between horizontal and vertical split panes (↔️/↕️) to customize your workspace based on your screen size or preference.
- **Filters & Regex**: Powerful search across URL, domain, headers, and body. Toggle **Regex Mode** for advanced pattern matching (e.g., finding specific tokens or ID