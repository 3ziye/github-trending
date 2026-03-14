# gstack

**gstack turns Claude Code from one generic assistant into a team of specialists you can summon on demand.**

Eight opinionated workflow skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Plan review, code review, one-command shipping, browser automation, QA testing, and engineering retrospectives — all as slash commands.

### Without gstack

- The agent takes your request literally — it never asks if you're building the right thing
- It will implement exactly what you said, even when the real product is something bigger
- "Review my PR" gives inconsistent depth every time
- "Ship this" turns into a long back-and-forth about what to do
- The agent can write code but can't see your app — it's half blind
- You still do QA by hand: open browser, click around, check pages, squint at layouts

### With gstack

| Skill | Mode | What it does |
|-------|------|--------------|
| `/plan-ceo-review` | Founder / CEO | Rethink the problem. Find the 10-star product hiding inside the request. |
| `/plan-eng-review` | Eng manager / tech lead | Lock in architecture, data flow, diagrams, edge cases, and tests. |
| `/review` | Paranoid staff engineer | Find the bugs that pass CI but blow up in production. Triages Greptile review comments. |
| `/ship` | Release engineer | Sync main, run tests, resolve Greptile reviews, push, open PR. For a ready branch, not for deciding what to build. |
| `/browse` | QA engineer | Give the agent eyes. It logs in, clicks through your app, takes screenshots, catches breakage. Full QA pass in 60 seconds. |
| `/qa` | QA lead | Systematic QA testing. On a feature branch, auto-analyzes your diff, identifies affected pages, and tests them. Also: full exploration, quick smoke test, regression mode. |
| `/setup-browser-cookies` | Session manager | Import cookies from your real browser (Comet, Chrome, Arc, Brave, Edge) into the headless session. Test authenticated pages without logging in manually. |
| `/retro` | Engineering manager | Team-aware retro: your deep-dive + per-person praise and growth opportunities for every contributor. |

## Demo: one feature, five modes

I start almost every feature in plan mode. I describe what I want to build, then use `/plan-ceo-review` to pressure-test whether I am even building the right thing. Only after the product direction is locked do I shift into engineering, review, ship, and test.

```
You:   [enter plan mode, describe the feature]
       I want to add seller photo upload to the listing app. Sellers
       should be able to upload a photo of their item and we create
       the listing from it.

You:   /plan-ceo-review

Claude: "Photo upload" is not the feature. The real job is helping sellers
        create listings that actually sell. Here's what the 10-star version
        looks like: auto-identify the product from the photo, pull specs and
        pricing comps from the web, draft the title and description, suggest
        the best hero image...

You:   /plan-eng-review

Claude: [Architecture diagram, state machine for upload → classify → enrich
        → draft pipeline, async job boundaries, failure modes, test matrix]

You:   [exit plan mode, implement the plan]

You:   /review

Claude: Race condition: two tabs can overwrite cover-photo selection.
        Trust boundary: pulling web data into draft generation creates
        a prompt injection vector. Missing: orphan cleanup for failed uploads.

You:   (fix the issues)

You:   /ship

Claude: [Syncs main, runs tests, pushes branch, opens PR — 6 tool calls, done]

You:   /qa

Claude: Analyzing branch diff... 8 files changed, 3 routes affected.
        [Tests /listings/new, /listings/:id, /api/listings against localhost:3000]
        All 3 routes working. Upload + enrichment flow passes end to end.

You:   /setup-browser-cookies staging.myapp.com

Claude: Imported 8 cookies for staging.myapp.com from Chrome.

You:   /qa https://staging.myapp.com --quick

Claude: [Smoke test: homepage + 5 pages, 30 seconds]
        Health Score: 91/100. No critical issues. 1 medium: mobile nav overlap.
```

## Who this is for

You already use Claude Code heavily and want consistent, high-rigor workflows instead of one mushy generic mode. You want to tell the model what kind of brain to use right now — founder taste, engineering rigor, paranoid review, or fast execution.

This is not a prompt pack for beginners. It is an operating system for people who ship.

## How to fly: 10 sessions at once

gstack is powerful with one Claude Code session. It is transformative with ten.

[Conductor](https://conductor.build) runs multiple Claude Code sessions in parallel — each in its own isolated workspace. That means you can have one session running `/qa` on staging, another doing `/review` on a PR, a third implementing a feature, and seven more working on other branches. All at the same time.

Each workspace gets its own isolated browser instance automatically — separate Chromium process, cookies, tabs, a