<p align="center">
  <img src="assets/logo.png" alt="OpenChronicle" width="600" />
</p>

<h1 align="center">OpenChronicle</h1>

<p align="center">
  Open-source, local-first memory for any tool-capable LLM agent.
</p>

<p align="center">
  Think OpenAI Chronicle - but open, model-agnostic, inspectable, and hackable.
</p>

---

<p align="center">
  <a href="https://star-history.com/#Einsia/OpenChronicle&Date">
    <picture>
      <source
        media="(prefers-color-scheme: dark)"
        srcset="https://api.star-history.com/svg?repos=Einsia/OpenChronicle&type=Date&theme=dark"
      />
      <source
        media="(prefers-color-scheme: light)"
        srcset="https://api.star-history.com/svg?repos=Einsia/OpenChronicle&type=Date"
      />
      <img
        alt="Star History Chart"
        src="https://api.star-history.com/svg?repos=Einsia/OpenChronicle&type=Date"
      />
    </picture>
  </a>
</p>

> **Status:** v0.1.0 · macOS only · early alpha

OpenChronicle gives AI agents a local, inspectable memory built from real screen and app context.

It runs on your Mac, captures structured context from what you're doing, and turns it into persistent Markdown memory: what you're working on, what you've decided, which tools you use, and which people or projects matter.

Any agent that can call tools can use it. MCP clients work especially well today, but OpenChronicle is meant to be a general memory layer for tool-using agents - not something tied to one protocol, one model provider, or one app.

---

## Why OpenChronicle

OpenAI Chronicle points to an important future: agents that remember your real working context.

OpenChronicle is our open alternative:

- **Local-first** - memory stays on your machine
- **Model-agnostic** - use Ollama, LM Studio, OpenAI, Anthropic, or any LiteLLM-compatible provider
- **Tool-friendly** - usable by any tool-capable agent
- **Inspectable** - Markdown on disk, SQLite locally
- **Open** - MIT-licensed and built to be extended

---

## Why AX-first

OpenChronicle currently prioritizes **AX Tree / accessibility-tree context** as its primary signal, with screenshots as a secondary signal over time.

We think this is the right tradeoff for an early memory system:

- **Lower cost** - structured text is far cheaper to process than screenshot-heavy OCR / vision pipelines
- **Better intent capture** - AX is often better for active app, focused element, edited text, URL, and interaction state
- **Smaller, cleaner memory** - easier to deduplicate, normalize, index, and retain long-term
- **Better foundation** - screenshots can later enrich visual context where AX falls short

> **AX-first for accurate, compact, low-cost memory; screenshot-assisted for richer multimodal context.**

---

## OpenChronicle vs OpenAI Chronicle

|                     | OpenAI Chronicle                | **OpenChronicle**                              |
| ------------------- | ------------------------------- | ---------------------------------------------- |
| Source              | Closed                          | **MIT, open-source**                           |
| Model choice        | OpenAI-centric                  | **Your choice**                                |
| Who can use it      | Product-specific workflow       | **Any tool-capable agent**                     |
| Primary capture     | Screenshot / OCR-heavy          | **AX Tree first**, screenshot-assisted         |
| Storage             | Local generated memories        | **Markdown + SQLite on your machine**          |
| Extensibility       | Limited                         | **Hackable parsers, memory logic, integrations** |

---

## How it works

```mermaid
flowchart LR
    W[mac-ax-watcher<br/>events]
    S0["<b>S0</b> dispatcher<br/>dedup · debounce<br/>min-gap"]
    S1["<b>S1</b> parser<br/>focused_element<br/>visible_text · url"]
    BUF[(capture-buffer<br/>/*.json)]
    TL["Timeline<br/>normalizer<br/>1-min · verbatim"]
    TB[(timeline_blocks)]
    SM["Session mgr<br/>idle 5m · app-switch 3m<br/>max 2h"]
    S2["<b>S2</b> reducer"]
    ED[(event-<br/>YYYY-MM-DD.md)]
    CLF["Classifier<br/>→ user- / project- / tool- /<br/>topic- / person- / org-*.md"]
    STORE[("SQLite FTS5<br/>+ Markdown")]

    W --> S0 --> S1 --> BUF --> TL --> TB --> S2 --> ED --> CLF --> STORE
    ED --> STORE
    BUF -. pre_capture_hook<br/>(post-write · skipped on content-dedup) .-> SM
    SM -. flush 5m / on_end .-> S2
    TB -. grounding .-> CLF
```

The core idea is simple:

1. capture context
2. compress it into sessions
3. extract durable facts
4. store memory locally
5. let agents query it through tools

---

## What you get

* **Event-driven capture** from macOS AX events
* **Session-aware memory writing** instead of noisy per-snapshot logs
* **Human-readable Markdown memory**
* **Local SQLite indexing**
* **Structured memory files** like user-, project-, tool-, topic-, person-, org-, and daily event-
* **Supersede-not-delete history**
* **Local or cloud model s