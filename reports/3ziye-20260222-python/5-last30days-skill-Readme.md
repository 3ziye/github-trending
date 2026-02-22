# /last30days v2.1

**The AI world reinvents itself every month. This skill keeps you current.** /last30days researches your topic across Reddit, X, YouTube, and the web from the last 30 days, finds what the community is actually upvoting, sharing, and saying on camera, and writes you a prompt that works today, not six months ago. Whether it's Seedance 2.0 access, Suno music prompts, or the latest Nano Banana Pro techniques, you'll prompt like someone who's been paying attention.

**New in V2.1  - three headline features:**

1. **Open-class skill with watchlists.** Add any topic to a watchlist  - your competitors, specific people, emerging technologies  - and /last30days re-researches it on demand or via cron. Designed for always-on environments like [Open Claw](https://github.com/openclaw/openclaw) where a bot can run research on a schedule and accumulate findings over time.
2. **YouTube transcripts as a 4th source.** When yt-dlp is installed, /last30days automatically searches YouTube, grabs view counts, and extracts auto-generated transcripts from the top videos. A 20-minute review contains 10x the signal of a single post - now the skill reads it. Inspired by [@steipete](https://x.com/steipete)'s yt-dlp + [summarize](https://github.com/steipete/summarize) toolchain.
3. **Works in OpenAI Codex CLI.** Same skill, same engine. Install to `~/.agents/skills/last30days` and invoke with `$last30days`. Claude Code and Codex users get the same research.

**New in V2:** Dramatically better search results. Smarter query construction finds posts that V1 missed entirely, and a new two-phase search automatically discovers key @handles and subreddits from initial results, then drills deeper. Free X search (no xAI key needed), `--days=N` for flexible lookback, and automatic model fallback. [Full changelog below.](#whats-new-in-v2)

**The tradeoff:** V2 finds way more content but takes longer - typically 2-8 minutes depending on how niche your topic is. The old V1 was faster but regularly missed results (like returning 0 X posts on trending topics). We think the depth is worth the wait, but if you'd use a faster "quick mode" that trades some depth for speed, let us know: [@mvanhorn](https://x.com/mvanhorn) / [@slashlast30days](https://x.com/slashlast30days).

**Best for prompt research**: discover what prompting techniques actually work for any tool (ChatGPT, Midjourney, Claude, Figma AI, etc.) by learning from real community discussions and best practices.

**But also great for anything trending**: music, culture, news, product recommendations, viral trends, or any question where "what are people saying right now?" matters.

## Installation

```bash
# Clone the repo
git clone https://github.com/mvanhorn/last30days-skill.git ~/.claude/skills/last30days

# Add your API keys
mkdir -p ~/.config/last30days
cat > ~/.config/last30days/.env << 'EOF'
OPENAI_API_KEY=sk-...
XAI_API_KEY=xai-...       # optional  - cookie auth is default for X search
EOF
chmod 600 ~/.config/last30days/.env
```

### X Search Authentication

X search reads your existing browser cookies  - no API keys or login commands needed.

**Safari (recommended on Mac):** Just be logged into x.com. No setup needed.

**Chrome:** Works, but macOS will prompt you to allow Keychain access the first time. Click "Allow" (or "Always Allow" to stop future prompts).

**Firefox:** Just be logged into x.com. No setup needed.

**Manual fallback:** If cookie auto-detection doesn't work, set these env vars (grab them from your browser's dev tools → Application → Cookies → x.com):
```bash
export AUTH_TOKEN=your_auth_token
export CT0=your_ct0_token
```

**Verify it's working:**
```bash
node ~/.claude/skills/last30days/scripts/lib/vendor/bird-search/bird-search.mjs --whoami
```

**Requirements:** Node.js 22+ (for the vendored Twitter GraphQL client).

### Codex CLI

This skill also works in OpenAI Codex CLI. Install to the Codex skills directory instead:

```bash
git clone https://github.com/mvanhorn/last30days-skill.git ~/.agents/skills/last30days
```

Same SKILL.md, same Python engine, same scripts. The `agents/openai.yaml` provides Codex-specific discovery metadata. Invoke with `$last30days` or through the `/skills` menu.

### Open Variant (Watchlist + Briefings)  - For Always-On Bots

**Designed for [Open Claw](https://github.com/openclaw/openclaw) and similar always-on AI environments.** Add your competitors, specific people, or any topic to a watchlist. When paired with a cron job or always-on bot, /last30days re-researches them on a schedule and accumulates findings in a local SQLite database. Ask for a briefing anytime.

**Important:** The watchlist stores schedules as metadata, but nothing triggers runs automatically. You need an external scheduler (cron, launchd, or an always-on bot like Open Claw) to call `watchlist.py run-all` on a timer. In plain Claude Code, you can run `watch run-one` and `watch run-all` manually, but there's no background scheduling.

```bash
# Ena