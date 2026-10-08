<p align="center">
  <img src="docs/logo.svg" width="64" height="64" alt="Answer me with HTML logo">
</p>

<h1 align="center">Answer me with HTML</h1>

<p align="center">
  <b>Super Fast&nbsp;&nbsp;|&nbsp;&nbsp;ASD-STE100&nbsp;&nbsp;|&nbsp;&nbsp;Explainer Videos&nbsp;&nbsp;|&nbsp;&nbsp;One File, Offline</b>
</p>

<p align="center">
  <b>An agent skill. Ask a hard question, get a page you can actually read instead of a wall of text.<br>The model writes about 1/8 of the tokens it would need to hand-write the HTML.</b>
</p>

<p align="center">
  <a href="https://github.com/QingYunA/answer-me-with-html/releases"><img src="https://img.shields.io/github/v/release/QingYunA/answer-me-with-html?style=flat-square&logo=github&labelColor=16181d&color=2ea44f" alt="Release"></a>
  <a href="https://github.com/QingYunA/answer-me-with-html/stargazers"><img src="https://img.shields.io/github/stars/QingYunA/answer-me-with-html?style=flat-square&logo=github&labelColor=16181d&color=2ea44f" alt="Stars"></a>
  <img src="https://img.shields.io/badge/works%20with-Claude%20Code%20%C2%B7%20Codex%20%C2%B7%20Cursor%20%C2%B7%20OpenCode%20%C2%B7%20Pi-2ea44f?style=flat-square&labelColor=16181d" alt="Works with Claude Code, Codex, Cursor, OpenCode, Pi">
  <a href="https://www.theagenticleaderboard.com/alternatives/answer-me-with-html/"><img src="https://www.theagenticleaderboard.com/badges/new/answer-me-with-html.svg" alt="The New 100"></a>
</p>

<p align="center">
  <a href="https://qingyuna.github.io/answer-me-with-html/"><b>Website</b></a> · <a href="#install">Install</a> · <a href="#what-you-ask-what-you-get">Examples</a> · <a href="#explainer-videos">Videos</a> · <a href="#always-on-mode-recommended">Always-on mode</a> · <a href="docs/reference.md">Reference</a> · <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <img src="docs/images/text-vs-page.png" alt="The same TCP question answered in plain text and with the skill: a wall of terminal text on the left, one readable page with diagrams on the right" width="100%">
</p>

Once installed, ask questions the way you always do:

```
> Explain the TCP three-way handshake
> Map out how the modules in this repo fit together
> Redis or Memcached for our cache?
```

The agent writes a short Markdown draft and hands it to the CLI that ships with the skill. About 50 ms later you have a page:

https://github.com/user-attachments/assets/d3063a28-5dfd-4c44-a562-be901c49b249

<p align="center"><sub>24-second demo. Turn the sound on for the music.</sub></p>

## Why not just ask for HTML?

You can. Models write decent HTML now. But most of what they write is not content. We counted the tokens in 9 pages the model wrote by hand, 4,893 tokens on average:

| Part of the page | Share | With this skill |
| :--- | ---: | :--- |
| SVG diagrams: coordinates and paths | 47% | The CLI writes it |
| CSS | 15% | The CLI writes it |
| HTML tags | 17% | The CLI writes it |
| Text | 21% | The model writes it, as Markdown |

With this skill the model writes only a Markdown draft. For the same questions that was 612 tokens on average, **about 1/8 of the hand-written HTML**. Less to write means less to wait for (3 topics × 3 runs, medians, Claude Sonnet 5.5, a plain Claude Code setup):

| | Ask for HTML directly | Answer me with HTML | |
| :--- | ---: | ---: | :--- |
| Tokens the model writes | 4,893 | **612** | **8× fewer** |
| Time | 31 s | **12 s** | **2.6× faster** |

<p align="center">
  <img src="docs/images/plain-vs-skill.png" alt="The same TCP question answered both ways" width="100%">
</p>

<p align="center"><sub>The same question, the same model, answered both ways. Both pages are usable.</sub></p>

The token counts are saved in [bench/corpus/tokens.json](bench/corpus/tokens.json), so `node bench/corpus.mjs` gives the same numbers every time. The pages themselves are a [download](https://github.com/QingYunA/answer-me-with-html/releases/download/v0.4.14/bench-corpus-2026-10-07.zip). The bill drops less than the writing, about 15% here, because every turn also reads the system prompt, your question and the conversation, with or without the skill. See [where the cost goes](bench/README.md#where-the-cost-goes).

Explainer videos save even more: about 18× fewer output tokens and 12× faster in [a small test](bench/README.md#explainer-videos).

## Install

You need [Node.js](https://nodejs.org/) 20 or newer. There is no `npm install` step. The CLI is bundled inside the skill.

### Let your agent install it (recommended)

Paste this into Claude Code, Codex, Cursor, OpenCode or any other agent:

> Install Answer me with HTML: read https://raw.githubusercontent.com/QingYunA/answer-me-with-html/main/INSTALL.md and follow it.

[INSTALL.md](INSTALL.md) is written for agents. It installs the plugin in Claude Code and the skill in other agents, keeps an existing install, asks you nothing, and ends with one report after checking the result with the TCP three-way handshake page. If your agent cannot open links, us