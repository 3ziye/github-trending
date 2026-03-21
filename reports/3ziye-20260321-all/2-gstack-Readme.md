# gstack

Hi, I'm [Garry Tan](https://x.com/garrytan). I'm President & CEO of [Y Combinator](https://www.ycombinator.com/), where I've worked with thousands of startups including Coinbase, Instacart, and Rippling when the founders were just one or two people in a garage — companies now worth tens of billions of dollars. Before YC, I designed the Palantir logo and was one of the first eng manager/PM/designers there. I cofounded Posterous, a blog platform we sold to Twitter. I built Bookface, YC's internal social network, back in 2013. I've been building products as a designer, PM, and eng manager for a long time.

And right now I am in the middle of something that feels like a new era entirely.

In the last 60 days I have written **over 600,000 lines of production code** — 35% tests — and I am doing **10,000 to 20,000 usable lines of code per day** as a part-time part of my day while doing all my duties as CEO of YC. That is not a typo. My last `/retro` (developer stats from the last 7 days) across 3 projects: **140,751 lines added, 362 commits, ~115k net LOC**. The models are getting dramatically better every week. We are at the dawn of something real — one person shipping at a scale that used to require a team of twenty.

**2026 — 1,237 contributions and counting:**

![GitHub contributions 2026 — 1,237 contributions, massive acceleration in Jan-Mar](docs/images/github-2026.png)

**2013 — when I built Bookface at YC (772 contributions):**

![GitHub contributions 2013 — 772 contributions building Bookface at YC](docs/images/github-2013.png)

Same person. Different era. The difference is the tooling.

**gstack is how I do it.** It is my open source software factory. It turns Claude Code into a virtual engineering team you actually manage — a CEO who rethinks the product, an eng manager who locks the architecture, a designer who catches AI slop, a paranoid reviewer who finds production bugs, a QA lead who opens a real browser and clicks through your app, and a release engineer who ships the PR. Fifteen specialists and six power tools, all as slash commands, all Markdown, **all free, MIT license, available right now.**

I am learning how to get to the edge of what agentic systems can do as of March 2026, and this is my live experiment. I am sharing it because I want the whole world on this journey with me.

Fork it. Improve it. Make it yours. Don't player hate, appreciate.

**Who this is for:**
- **Founders and CEOs** — especially technical ones who still want to ship. This is how you build like a team of twenty.
- **First-time Claude Code users** — gstack is the best way to start. Structured roles instead of a blank prompt.
- **Tech leads and staff engineers** — bring rigorous review, QA, and release automation to every PR

## Quick start: your first 10 minutes

1. Install gstack (30 seconds — see below)
2. Run `/office-hours` — describe what you're building. It will reframe the problem before you write a line of code.
3. Run `/plan-ceo-review` on any feature idea
4. Run `/review` on any branch with changes
5. Run `/qa` on your staging URL
6. Stop there. You'll know if this is for you.

Expect first useful run in under 5 minutes on any repo with tests already set up.

**If you only read one more section, read this one.**

## Install — takes 30 seconds

**Requirements:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Git](https://git-scm.com/), [Bun](https://bun.sh/) v1.0+, [Node.js](https://nodejs.org/) (Windows only)

### Step 1: Install on your machine

Open Claude Code and paste this. Claude does the rest.

> Install gstack: run **`git clone https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`** then add a "gstack" section to CLAUDE.md that says to use the /browse skill from gstack for all web browsing, never use mcp\_\_claude-in-chrome\_\_\* tools, and lists the available skills: /office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review, /design-consultation, /review, /ship, /browse, /qa, /qa-only, /design-review, /setup-browser-cookies, /retro, /investigate, /document-release, /codex, /careful, /freeze, /guard, /unfreeze, /gstack-upgrade. Then ask the user if they also want to add gstack to the current project so teammates get it.

### Step 2: Add to your repo so teammates get it (optional)

> Add gstack to this project: run **`cp -Rf ~/.claude/skills/gstack .claude/skills/gstack && rm -rf .claude/skills/gstack/.git && cd .claude/skills/gstack && ./setup`** then add a "gstack" section to this project's CLAUDE.md that says to use the /browse skill from gstack for all web browsing, never use mcp\_\_claude-in-chrome\_\_\* tools, lists the available skills: /office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review, /design-consultation, /review, /ship, /browse, /qa, /qa-only, /design-review, /setup-browser-cookies, /retro, /investigate, /document-release, /codex, /careful, /freeze, /guard, /unfreeze, /gstack-upgrade