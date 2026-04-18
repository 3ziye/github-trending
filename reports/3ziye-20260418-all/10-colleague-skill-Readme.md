<div align="center">

# colleague.skill

> *"You AI guys are traitors to the codebase — you've already killed frontend, now you're coming for backend, QA, ops, infosec, chip design, and eventually yourselves and all of humanity"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?logo=discord&logoColor=white)](https://discord.gg/2bbP2a7f)

<br>

Your colleague quit, leaving behind a mountain of unmaintained docs?<br>
Your intern left, nothing but an empty desk and a half-finished project?<br>
Your mentor graduated, taking all the context and experience with them?<br>
Your partner transferred, and the chemistry you built reset to zero overnight?<br>
Your predecessor handed over, trying to condense three years into three pages?<br>

**Turn cold goodbyes into warm Skills — welcome to cyber-immortality!**

<br>

Provide source materials (Feishu messages, DingTalk docs, Slack messages, emails, screenshots)<br>
plus your subjective description of the person<br>
and get an **AI Skill that actually works like them**

[Supported Sources](#supported-data-sources) · [Install](#install) · [Usage](#usage) · [Demo](#demo) · [Detailed Install](INSTALL.md) · [💬 Discord](https://discord.gg/2bbP2a7f)

[**中文**](docs/lang/README_ZH.md) · [**Español**](docs/lang/README_ES.md) · [**Deutsch**](docs/lang/README_DE.md) · [**日本語**](docs/lang/README_JA.md) · [**Русский**](docs/lang/README_RU.md) · [**Português**](docs/lang/README_PT.md) · [**한국어**](docs/lang/README_KO.md)

</div>

---

> 🆕 **2026.04.17 Update** — **WeChat group 4 is live!** Come hang out with the dot-skill community — share skills, discuss features, trade tips.
>
> <img src="docs/assets/wechat-group-qr-4.png" alt="dot-skill WeChat group QR" width="240">
>
> QR refreshes every 7 days (expires 2026-04-23) — if expired, ping me on Discord.

> 🆕 **2026.04.13 Update** — **dot-skill Roadmap is live!** colleague.skill is evolving into **dot-skill** — distill anyone, not just colleagues. Multimodal output, skill ecosystems, and more on the way.
>
> 👉 **[Read the full Roadmap](ROADMAP.md)** · **[💬 Discord](https://discord.gg/2bbP2a7f)**
>
> We've also cleaned up Issues, added Milestones, and set up a [public project board](https://github.com/users/titanwings/projects/1). Community contributions welcome — check `good-first-issue` labels!

> 🆕 **2026.04.07 Update** — The community's enthusiasm for dot-skill remixes has been incredible! I've built a community gallery — PRs welcome!
>
> Share any skill or meta-skill, and drive traffic directly to your own GitHub repo. No middleman.
>
> 👉 **[titanwings.github.io/colleague-skill-site](https://titanwings.github.io/colleague-skill-site/)**
>
> Now listed: 户晨风.skill · 峰哥亡命天涯.skill · 罗翔.skill and more

---

Created by [@titanwings](https://github.com/titanwings) | Powered by Shanghai AI Lab · AI Safety Center

## Supported Data Sources

> This is still a beta version of colleague.skill — more sources coming soon, stay tuned!

| Source | Messages | Docs / Wiki | Spreadsheets | Notes |
|--------|:--------:|:-----------:|:------------:|-------|
| Feishu (auto) | ✅ API | ✅ | ✅ | Just enter a name, fully automatic |
| DingTalk (auto) | ⚠️ Browser | ✅ | ✅ | DingTalk API doesn't support message history |
| Slack (auto) | ✅ API | — | — | Requires admin to install Bot; free plan limited to 90 days |
| WeChat chat history | ✅ SQLite | — | — | Currently unstable, recommend using open-source tools below |
| PDF | — | ✅ | — | Manual upload |
| Images / Screenshots | ✅ | — | — | Manual upload |
| Feishu JSON export | ✅ | ✅ | — | Manual upload |
| Email `.eml` / `.mbox` | ✅ | — | — | Manual upload |
| Markdown | ✅ | ✅ | — | Manual upload |
| Paste text directly | ✅ | — | — | Manual input |

### Recommended WeChat Chat Export Tools

These are independent open-source projects — this project does not include their code, but our parsers are compatible with their export formats. WeChat auto-decryption is currently unstable, so we recommend using these open-source tools to export chat history, then paste or import into this project:

| Tool | Platform | Description |
|------|----------|-------------|
| [WeChatMsg](https://github.com/LC044/WeChatMsg) | Windows | WeChat chat history export, supports multiple formats |
| [PyWxDump](https://github.com/xaoyaoo/PyWxDump) | Windows | WeChat database decryption & export |
| [留痕 (Liuhen)](https://github.com/greyovo/留痕) | macOS | WeChat chat history export (recommended for Mac users) |

> Tool recommendations from [@therealXiaomanChu](https://github.com/therealXiaomanChu). Thanks to all the open-source authors — together for cybe