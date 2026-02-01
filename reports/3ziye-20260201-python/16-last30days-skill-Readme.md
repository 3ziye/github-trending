# /last30days

**The AI world reinvents itself every month. This Claude Code skill keeps you current.** /last30days researches your topic across Reddit, X, and the web from the last 30 days, finds what the community is actually upvoting and sharing, and writes you a prompt that works today, not six months ago. Whether it's Ralph Wiggum loops, Suno music prompts, or the latest Midjourney techniques, you'll prompt like someone who's been paying attention.

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
XAI_API_KEY=xai-...
EOF
chmod 600 ~/.config/last30days/.env
```

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

## Example: Legal Prompting (Hallucination Prevention)

**Query:** `/last30days prompting techniques for chatgpt for legal questions`

**Research Output:**
> The dominant theme is hallucination prevention - multiple sources discuss lawyers being fined or embarrassed for submitting fake case citations that ChatGPT fabricated. Key prompting strategies include: (1) using Deep Research mode or grounding tools with uploaded primary sources, (2) building "Hallucination Prevention Systems" into prompts that force epistemic honesty, (3) prompting for procedural questions rather than case law lookups, and (4) framing outputs as "issue-spotting" rather than legal advice. A major warning: chat logs are discoverable in litigation.

**Key patterns discovered:**
1. Hallucination prevention clauses - "If you don't know a case citation, say so rather than inventing one"
2. Role assignment - assign ChatGPT a specific persona (paralegal, issue-spotter) to constrain outputs
3. Structured output requirements - request specific sections (risks, key terms, questions for counsel)
4. Epistemic humility enforcement - "acknowledge uncertainty" and "flag when you're unsure"
5. Scope limitation - focus on procedural questions, not case law research

**Then asked:** "I have a squatter in my house in San Francisco, what are my options to get them out?"

**Generated Prompt:**

```
Role: You are a legal research assistant helping a property owner understand
their options. You are NOT providing legal advice - you are helping me
identify issues, understand procedures, and prepare informed questions for an
attorney.

Situation: I own a residential property in San Francisco, California. Someone
is currently occupying the property without my permission or any lease
agreement (a squatter). I need to understand my legal options for removing them.

Your task: Provide a structured analysis covering:

1. California/SF Legal Framework - What laws govern this situation? (Note: San
Francisco has strong tenant protections - address how these apply or don't
apply to squatters vs. tenants)
2. Key Distinctions - Help me understand: squatter vs. trespasser vs. holdover
tenant. How does the length of occupation affect my options?
3. Available Legal Remedies - What are my procedural options? (unlawful
detainer, police involvement, etc.) What is the typical process and timeline?
4. Critical Mistakes to Avoid - What actions could expose me to liability?
(self-help eviction, utility shutoffs, etc.)
5. Questions I Should Ask an Attorney - Based on this analysis, what specific
questions should I bring to a California real estate attorney?

Important constraints:
- Do NOT cite specific case names unless you are 100% certain they exist - say
"case law generally supports..." instead
- Flag any areas where you're uncertain
- Note where San Francisco local ordinances may di