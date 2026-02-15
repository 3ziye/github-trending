# /last30days v2

**The AI world reinvents itself every month. This Claude Code skill keeps you current.** /last30days researches your topic across Reddit, X, and the web from the last 30 days, finds what the community is actually upvoting and sharing, and writes you a prompt that works today, not six months ago. Whether it's Ralph Wiggum loops, Suno music prompts, or the latest Midjourney techniques, you'll prompt like someone who's been paying attention.

**New in V2:** Dramatically better search results. Smarter query construction finds posts that V1 missed entirely, and a new two-phase search automatically discovers key @handles and subreddits from initial results, then drills deeper. Also: free X search via [Bird CLI](https://github.com/steipete/bird) (no xAI key needed), `--days=N` for flexible lookback, and automatic model fallback. [Full changelog below.](#whats-new-in-v2)

**The tradeoff:** V2 finds way more content but takes longer — typically 2-8 minutes depending on how niche your topic is. The old V1 was faster but regularly missed results (like returning 0 X posts on trending topics). We think the depth is worth the wait, but if you'd use a faster "quick mode" that trades some depth for speed, let us know: [@mvanhorn](https://x.com/mvanhorn) / [@slashlast30days](https://x.com/slashlast30days).

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
XAI_API_KEY=xai-...       # optional if using Bird CLI
EOF
chmod 600 ~/.config/last30days/.env
```

### Optional: Bird CLI for free X search

[Bird CLI](https://github.com/steipete/bird) lets you search X without an xAI API key. If installed and authenticated, /last30days uses it automatically.

```bash
npm install -g @steipete/bird
bird login
```

Bird is free and doesn't require an xAI key. If both Bird and an xAI key are available, Bird is preferred.

## Usage

```
/last30days [topic]
/last30days [topic] for [tool]
```

Examples:
- `/last30days prompting techniques for ChatGPT for legal questions`
- `/last30days iOS app mockups for Nano Banana Pro`
- `/last30days What are the best rap songs lately`
- `/last30days remotion animations for Claude Code`

## What It Does

1. **Researches** - Scans Reddit and X for discussions from the last 30 days
2. **Synthesizes** - Identifies patterns, best practices, and what actually works
3. **Delivers** - Either writes copy-paste-ready prompts for your target tool, or gives you a curated expert-level answer

### Use it for:
- **Prompt research** - "What prompting techniques work for legal questions in ChatGPT?"
- **Tool best practices** - "How are people using Remotion with Claude Code?"
- **Trend discovery** - "What are the best rap songs right now?"
- **Product research** - "What do people think of the new M4 MacBook?"
- **Viral content** - "What's the dog-as-human trend on ChatGPT?"

---

## Example: Nano Banana Pro Prompting (Image Generation)

**Query:** `/last30days nano banana pro prompting`

**Research Output:**
> JSON prompting is the dominant technique — The X community overwhelmingly uses structured JSON prompts rather than plain text. Creators like @Xmira_belle, @Cicily_aura, @RubenSalvo_, and @mahivisuals all share prompts in JSON format with nested objects for metadata, subject descriptions, lighting, camera specs, and scene composition. @realdigitaldao made a static ad "in less than 5 min" using a simple JSON prompt.
>
> Prompt adherence is Nano Banana Pro's killer advantage — JSON prompts hit 92% precision for color accuracy, lighting ratios, and composition vs ~68% for natural language prompts, per fofr.ai. @artingent directly compared it to GPT Image 1.5 and noted Nano Banana Pro has higher prompt adherence — "GPT image 1.5 ignored the Top Down instruction."
>
> Stop writing "tag soup" — act like a Creative Director — The biggest shift is away from comma-separated keyword lists toward natural language descriptions with clear structure. The ICS Framework (Image type, Content, Style) and the 5-element formula (subject, composition, action, setting, style) are the two dominant approaches, per r/nanobanana2pro.

**Key patterns discovered:**
1. JSON > plain text — Structure prompts as JSON objects with keys for subject, composition, lighting, camera, style — per @Xmira_belle, @Cicily_aura
2. The 5-element formula — Subject + Composition + Action + Setting + Style — per r/nanobanana2pro
3. Separate subjects into distinct objects — Multi-character s