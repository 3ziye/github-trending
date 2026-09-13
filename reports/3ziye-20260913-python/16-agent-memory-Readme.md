<div align="center">

### agent-memory: the long-term memory runtime for AI agents

<a href="CLAUDE.md">Invariants</a> · <a href="skills/agent-memory/SKILL.md">Skill</a> · <a href="https://github.com/tigerless-labs/agent-memory/issues">Issues</a>

![](https://img.shields.io/badge/version-0.1.0-369eff?labelColor=black&style=flat-square)
![](https://img.shields.io/badge/python-3.12+-ffcb47?labelColor=black&style=flat-square)
![](https://img.shields.io/badge/hosts-Claude%20Code%2C%20Codex%20CLI-ff80eb?labelColor=black&style=flat-square)
![](https://img.shields.io/badge/dependencies-zero%20API%20keys-c4f042?labelColor=black&style=flat-square)

</div>

***

An agent that closes its session forgets everything it learned in it. agent-memory is the
runtime that fixes that, for any agent — not only coding ones. Markdown files in one store are
the single source of truth, the SQLite index beside them is a cache you can delete at any time,
and Claude Code, Codex CLI, and anything else that can run a shell command share that store.

Retrieval is local and ranked, and it answers with paths rather than pasted text — the agent
opens each hit only as deep as the task needs. Writes do not wait for the agent to remember to
make them: they fire at conversation boundaries. A sleep-time pass then consolidates and
forgets by value, on its own clock. None of it needs an API key.

## Two lines, one store

Agent memory has grown along two architectural lines. One builds a **retrieval engine** —
embeddings, a knowledge graph, a ranking pipeline — which finds the right thing, but hands the
agent an opaque chunk it cannot inspect and a store it cannot migrate off. The other hands the
agent a **filesystem** — markdown it reads directly, browsable with `ls` and `grep` — which is
legible and costs nothing to run, but does not rank, and stops scaling the moment the tree
outgrows a listing.

agent-memory is the two of them in one store: the retrieval engine indexes a filesystem the
agent can also just read. Relations live as links inside the memories, a local index ranks
them, and every hit resolves to a whole markdown file on disk. Recall gains the precision of a
graph and a vector search without giving up a plain directory an agent can walk — and it stays
fast, because nothing in the read path calls a model or crosses a network.

## Retrieve by path, then read by level

Recall does not paste text into your context. It answers with an L0 list — one-line abstract,
file path, anchor, score — and the agent opens what it wants at the depth the task needs:

```bash
mem recall "why files instead of a database"    # L0 list, 8 entries by default
mem read <name> --level outline                 # headings only; or abstract, or full
mem context "why files instead of a database"   # both in one call, top few expanded in full
```

Index line → abstract → full file → raw material: each rung costs an order of magnitude more
than the last, and each is a place to stop. Long files add two free rungs — the anchor that
matched, and an outline computed at read time.

## Design commitments

- **Three read tracks, so a miss on one is not a miss.** Deterministic `MEMORY.md` injection at
  session start; BM25 recall over an FTS5 index, with a vector plugin fused in by RRF when you
  want one; and the plain directory tree, reachable with `ls` and `grep` when both fail.
  Same-directory memories are a free neighbourhood, and `links` in the frontmatter carry the
  graph without a graph database under them.
- **Write coverage is the system's job, not the agent's judgement.** Distillation is triggered
  at boundaries and runs without holding up the task; the full trace is copied first, so
  "missed by the distiller" never means "lost by the system".
- **Files are the truth; every index is a rebuildable cache.** `rm -rf .index/ && mem rebuild`
  loses zero knowledge — enforced by a test, not promised in a doc. Your memory stays greppable,
  git-able, and portable off this system.
- **A real Manage layer, on its own clock.** Sleep-time consolidation with authority tiers: an
  unattended pass may add and update, deletion only ever arrives as a proposal you confirm.
  Every competitor either has no M, or buries it in the write path. Supersede leaves the chain
  intact and `recall --as-of` answers as of a date, so updating never destroys.
- **No LLM client inside the library.** Zero keys to install and no billing surface: judgement
  is borrowed from the host agent's own CLI, which keeps every write visible in your transcript.

## The store

```
$AGENT_MEMORY_STORE/
├── MEMORY.md              root index, one line per memory — the only resident injection
├── config.toml            every tunable; an unknown knob is refused at load
├── schemas/               one file per type: its key fields, the field it groups by, write mode
├── decision/              memories live at <type>/<group>/<name>.md, placed by the schema
│   └── agent-memory/        …/markdown-files-are-the-single