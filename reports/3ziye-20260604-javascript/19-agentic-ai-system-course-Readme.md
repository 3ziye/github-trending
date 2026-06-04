# Agentic System Course - Use Agent to Learn Agent

**Join the [discord channel](https://discord.gg/dWSnHAFdpb) if you want to learn and build together!**

---

This is a 22-chapter skeleton course on how to design, build, and operate production AI agents — written to be read with your own AI partner at your side. **An agentic system** is an AI system that can autonomously pursue goals by planning, making decisions, using tools, adapting based on feedback, having memory, etc — instead of only responding to a single prompt. Similar to [Andrej Karpathy's idea file on LLM-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), **this course is giving you the skeleton and your agent will help you put the muscles on it**.

**This course is**:

- A *skeleton* — load-bearing topics, patterns, and decisions, with trade-offs.
- Written to age slowly. Framework specifics rot fast; architectural patterns do not.
- A file pair (course + AGENTS.md) designed for AI consumption as much as human reading.

**This course is not**:

- A step-by-step tutorial. There is no walked-through project.
- Tied to one stack. The course never says "use LangChain" or "use Pydantic AI." Your AI partner suggests the stack that fits your project.
- A reference manual. When you need an exact API signature, ask your AI or read the docs.


---

## How to start

Clone the repo, open it in your usual IDE to view course content. At the same time, point your AI agent (Claude code/Codex) at the project root, and try one of these prompts when you study a chapter:

- *"Give me three real-world examples of where this matters."*
- *"Suppose you are interviewing me, quiz me on this topic with five follow-up questions, easy to hard."*
- *"What's a question I should be asking that I haven't?"*
- *"I just read about [pattern X]. I am building [your project]. Translate the pattern into the smallest version that works in whatever language and tools fit, and explain each piece as you write it."*
- *"Forget my project for a moment — show me how OpenCode (or Hermes Agent, or any leading coding agent) handles this, and what we should borrow from it."*

You can also just point your agent at Ch.22's design canvas and walk through it with your specific project in mind — that's the fastest path from "I have an idea" to "I have a spec."

---

## Built-in skills

### `agentic-system-reviewer`

Reviews PRDs, design docs, implementation plans, or agent code against the course. You can run this skill on **any agentic system** to get course-grounded feedback — your own project, an open-source agent you're studying, a PRD before any code exists, or a coworker's repo you want a second opinion on. The skill calibrates scope first (hobby / team tool / customer-facing), picks the chapters that matter for your archetype, reads them, and produces a findings-first report with severity, evidence, course citations, and concrete fixes — not a generic "looks good" or "add safety" review.

In Claude Code, just describe what you want — *"review this against the course"*, *"is this agent design good?"*, *"what chapters does this miss?"* — while the agent is pointed at the target repo or doc. The skill auto-loads when its description matches your intent.

**Codex users:** use Codex's official `skill-creator` skill to port this skill over.

---

## Course structure

| Chapters | Theme |
|---|---|
| **Ch.00** | How to use this course with your AI partner |
| **Ch.01–04** | Foundations: one tool call → the loop → tools as contract → prompts & cache |
| **Ch.05–08** | Memory and state: short-term → long-term → writing & curation → persistence |
| **Ch.09–11** | Coordination: planning → multi-agent delegation → the harness |
| **Ch.12–14** | External surface: human-in-the-loop → connectors/MCP → skills/MCP/subagents |
| **Ch.15–17** | Production scale: backend → observability → cost, latency, model strategy |
| **Ch.18–19** | Quality and ops: safety/adversarial inputs → operations and forward-deployed |
| **Ch.20–21** | Agency: proactive agents → self-evolving agents |
| **Ch.22** | Design canvas: designing your own agent |

The chapters are ordered so each one only assumes what came before. If you have a clear project, skim chapters that do not apply yet and come back when they do. Suggested learning paths by project shape (coding agent, personal assistant, multi-tenant tool, research agent, just exploring) are in `CLAUDE.md`.

The goal is not to finish the course. *The goal is to ship something you wanted to ship anyway, and to understand every line of it.*

---

## Optional: reference systems

The course occasionally points at four open-source systems for grounded examples:

- **OpenCode** — coding agent (terminal-first, typed tools, sessions, compaction)
- **Hermes Agent** — personal assistant (memory, skills, cron, channels)
- **OpenClaw** — self-hosted personal-assistant gateway (channel adapters)
- **Paperclip** — workflow control plane (multi-agent orchestration, dur