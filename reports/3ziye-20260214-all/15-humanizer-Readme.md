# Humanizer

A Claude Code skill that removes signs of AI-generated writing from text, making it sound more natural and human.

## Installation

### Recommended (clone directly into Claude Code skills directory)

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/blader/humanizer.git ~/.claude/skills/humanizer
```

### Manual install/update (only the skill file)

If you already have this repo cloned (or you downloaded `SKILL.md`), copy the skill file into Claude Code’s skills directory:

```bash
mkdir -p ~/.claude/skills/humanizer
cp SKILL.md ~/.claude/skills/humanizer/
```

## Usage

In Claude Code, invoke the skill:

```
/humanizer

[paste your text here]
```

Or ask Claude to humanize text directly:

```
Please humanize this text: [your text]
```

## Overview

Based on [Wikipedia's "Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide, maintained by WikiProject AI Cleanup. This comprehensive guide comes from observations of thousands of instances of AI-generated text.

### Key Insight from Wikipedia

> "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

## 24 Patterns Detected (with Before/After Examples)

### Content Patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 1 | **Significance inflation** | "marking a pivotal moment in the evolution of..." | "was established in 1989 to collect regional statistics" |
| 2 | **Notability name-dropping** | "cited in NYT, BBC, FT, and The Hindu" | "In a 2024 NYT interview, she argued..." |
| 3 | **Superficial -ing analyses** | "symbolizing... reflecting... showcasing..." | Remove or expand with actual sources |
| 4 | **Promotional language** | "nestled within the breathtaking region" | "is a town in the Gonder region" |
| 5 | **Vague attributions** | "Experts believe it plays a crucial role" | "according to a 2019 survey by..." |
| 6 | **Formulaic challenges** | "Despite challenges... continues to thrive" | Specific facts about actual challenges |

### Language Patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 7 | **AI vocabulary** | "Additionally... testament... landscape... showcasing" | "also... remain common" |
| 8 | **Copula avoidance** | "serves as... features... boasts" | "is... has" |
| 9 | **Negative parallelisms** | "It's not just X, it's Y" | State the point directly |
| 10 | **Rule of three** | "innovation, inspiration, and insights" | Use natural number of items |
| 11 | **Synonym cycling** | "protagonist... main character... central figure... hero" | "protagonist" (repeat when clearest) |
| 12 | **False ranges** | "from the Big Bang to dark matter" | List topics directly |

### Style Patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 13 | **Em dash overuse** | "institutions—not the people—yet this continues—" | Use commas or periods |
| 14 | **Boldface overuse** | "**OKRs**, **KPIs**, **BMC**" | "OKRs, KPIs, BMC" |
| 15 | **Inline-header lists** | "**Performance:** Performance improved" | Convert to prose |
| 16 | **Title Case Headings** | "Strategic Negotiations And Partnerships" | "Strategic negotiations and partnerships" |
| 17 | **Emojis** | "🚀 Launch Phase: 💡 Key Insight:" | Remove emojis |
| 18 | **Curly quotes** | `said “the project”` | `said "the project"` |

### Communication Patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 19 | **Chatbot artifacts** | "I hope this helps! Let me know if..." | Remove entirely |
| 20 | **Cutoff disclaimers** | "While details are limited in available sources..." | Find sources or remove |
| 21 | **Sycophantic tone** | "Great question! You're absolutely right!" | Respond directly |

### Filler and Hedging

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 22 | **Filler phrases** | "In order to", "Due to the fact that" | "To", "Because" |
| 23 | **Excessive hedging** | "could potentially possibly" | "may" |
| 24 | **Generic conclusions** | "The future looks bright" | Specific plans or facts |

## Full Example

**Before (AI-sounding):**
> Great question! Here is an essay on this topic. I hope this helps!
>
> AI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolution of software development. In today's rapidly evolving technological landscape, these groundbreaking tools—nestled at the intersection of research and practice—are reshaping how engineers ideate, iterate, and deliver, underscoring their vital role in modern workflows.
>
> At its core, the value proposition is clear: streamlining processes, enhancing collaboration, and fostering alignment. It's not just about autocomplete; it's about unlocking creativity at scale, ensuring that organizations can remain agile while delivering seamless, intuitive, and powerful experiences to u