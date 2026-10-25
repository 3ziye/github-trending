<div align="center">

<img src="docs/logo.svg" width="128" alt="new-term-radar logo: a radar sweep catching a new blip">

# new-term-radar

**Catch the names AI people are about to search for, the day they appear, before keyword tools list them.**

[![PyPI](https://img.shields.io/pypi/v/new-term-radar?color=0ea5e9&label=PyPI)](https://pypi.org/project/new-term-radar/)
[![Python](https://img.shields.io/badge/python-3.10%2B-3776ab)](https://pypi.org/project/new-term-radar/)
[![License: MIT](https://img.shields.io/badge/license-MIT-eab308)](LICENSE)
[![Stars](https://img.shields.io/github/stars/zhuyansen/new-term-radar?logo=github&color=0f172a)](https://github.com/zhuyansen/new-term-radar/stargazers)
[![Forks](https://img.shields.io/github/forks/zhuyansen/new-term-radar?logo=github&color=0f172a)](https://github.com/zhuyansen/new-term-radar/network/members)
[![Downloads](https://img.shields.io/pepy/dt/new-term-radar?color=22c55e&label=downloads)](https://pepy.tech/projects/new-term-radar)
[![Last commit](https://img.shields.io/github/last-commit/zhuyansen/new-term-radar?color=64748b)](https://github.com/zhuyansen/new-term-radar/commits/main)

[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-io.github.zhuyansen%2Fnew--term--radar-0ea5e9)](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.zhuyansen/new-term-radar)
[![Tessl registry](https://img.shields.io/badge/Tessl-registry-22c55e)](https://tessl.io/registry/skills/github/zhuyansen/new-term-radar)
[![LobeHub](https://lobehub.com/badge/mcp/zhuyansen-new-term-radar)](https://lobehub.com/mcp/zhuyansen-new-term-radar)
[![Security-graded by Agent Skills Hub](https://agentskillshub.top/badge/zhuyansen/new-term-radar.svg)](https://agentskillshub.top/skill/zhuyansen/new-term-radar/)
[![Cursor Directory](https://img.shields.io/badge/Cursor%20Directory-new--term--radar-000000)](https://cursor.directory/plugins/new-term-radar)
[![ClawHub](https://img.shields.io/badge/ClawHub-new--term--radar-f97316)](https://clawhub.ai/skills/new-term-radar)
[![skills.sh](https://img.shields.io/badge/skills.sh-zhuyansen%2Fnew--term--radar-0f172a)](https://skills.sh/zhuyansen/new-term-radar)

⭐ **700+ stars on its first day, 1,000 in just over three** · on PyPI, the official MCP Registry, Cursor Directory, LobeHub, Tessl, ClawHub and skills.sh

[Quick start](#quick-start) · [What it reads](#what-it-reads) · [The keyword table](#the-keyword-table) · [Agents and MCP](#use-it-from-an-agent-skills-and-an-mcp-server) · [config.json](#configjson) · [中文说明](README.zh-CN.md)

</div>

A daily report of the names that are starting to surge in AI: new models, products, tools and repos, caught where they are said first, before they show up in keyword tools.

Built for people who make pages, posts or products around new terms: SEO for AI tool sites, newsletters, directories, anyone who wants to know about "Strata" or "Seedance" the day it appears and not two weeks later.

## Why

A new name leaves a trail, in this order:

1. A lab or a well-followed account says it on X; a model enters Hugging Face's trending list.
2. One GitHub repo takes off on its own.
3. Directories and competitors add pages for it; someone registers a domain for it and the site starts to rank.
4. Your own site gets its first search impressions for it.
5. Google Trends shows the curve, days or weeks later.

Keyword tools read step 5. This radar reads steps 1 to 4 every day and uses step 5 only to check itself.

One example it was built around: [Niko1221/Strata](https://github.com/Niko1221/Strata) was created on 2026-09-24 and had 7,700 stars nine days later. People were searching "niko strata" from 9/26, while no second repo carried the name and no keyword tool listed it. A single repo gaining 800 stars a day is the whole signal, and it is public.

## What it reads

![How the radar works: six signals, a name judge, the keyword table with its page-one check, a daily report and a 14-day check; used from the command line, three Agent Skills, an MCP server or the pains command. What 0.3 to 0.5 added is purple and tagged NEW](docs/radar.en.gif)

Purple, tagged NEW: what 0.3 to 0.5 added (⑥ revenue, ⑦ Reddit asks, ⑧ sellers, the page-one check, the format and ⚡ marks, the `pains` command).

| Signal | What it catches | Needs | Cost |
|---|---|---|---|
| ① X | Names the accounts in your list used for the first time in 60 days | AIsa key | $0.003 per account per run |
| ① Hugging Face | Models and Spaces (the demos people try) new to the trending top 50; quantised copies and a model's own demo grouped under the base name | nothing | free |
| ② GitHub breakout | A repo under 14 days old averaging 200+ stars a day, or +400 since yesterday; adds the search variants people use ("niko strata") | nothing (a GitHub token raises the rate limit) | free |
| ③ Sitemaps | Words that several new URLs on a site share and its older URLs rarely carried. The example config watches eight AI tool directories (toolify, aixploria,