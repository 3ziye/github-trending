<div align="center">
<picture>
  <source media="(max-width: 1239px) and (prefers-color-scheme: dark)" srcset="doc/images/banner-phone-dark.gif">
  <source media="(max-width: 1239px)" srcset="doc/images/banner-phone-light.gif">
  <source media="(prefers-color-scheme: dark)" srcset="doc/images/banner-dark.gif">
  <img alt="gitai, Git designed for AI agents. An animation: the gitai logo; a board of 50 agents racing on one branch, where git lands 100 of 250 changes and gitai lands 200; a merge conflict between two agents (one renamed get to fetch, the other added an argument) resolved by AI, tested and merged; and every change carrying the name of the agent that made it." src="doc/images/banner-light.gif" width="100%">
</picture>
<h3 align="center">Git designed for AI agents.</h3>
</div>

Anthropic built **Scion**, a faster version control system for coding agents,
and described it in
[Redesigning source control](https://www.anthropic.com/engineering/redesigning-source-control):
a server-centric system built for hundreds of agents that read, write and land
code at the same time. Scion is internal to Anthropic and is not available to
the public.

So I built **gitai**: an open-source version of that design that anyone can
run, and that the community can improve and maintain together.

MIT licensed. Vendor neutral: the server never calls a language model, and every
AI feature works with any provider, or none.

<sub>gitai is an independent implementation of the publicly described design. It is not affiliated with or endorsed by Anthropic.</sub>

---

## Why

Classic Git hosting was built for humans who clone a repository, work for hours
and push once. Coding agents work differently: thousands of short-lived tasks,
each touching a few files, each wanting to land in seconds, all on the same
branches. Full clones, merge queues and client-side history walks become the
bottleneck.

Scion's answer is to move the work to the server: clients stay online and fetch
only what they need, history questions are answered (and cached) by the server,
changes land through a compare-and-swap instead of a queue, every update is an
entry in a changeset log, and the repository state lives in a consistent
database plus object storage so servers scale out. gitai implements these
ideas, with normal Git repositories underneath.

## The Scion ideas, implemented

| Scion idea | In gitai |
|---|---|
| **Always-online clients** that fetch exactly what they need | `ObjectService` serves single objects and sparse trees; `graft clone` and `graft sparse` materialize only the paths you ask for. |
| **Source control as an API**: history runs on the server | Blame, path history, ancestry and code search run server-side and are memoized as derived data, computed once per commit. |
| **Landing without a merge queue** | `UserLand` rebases a change onto the current tip and lands it with a compare-and-swap; concurrent lands on one branch are batched into a single reference update. |
| **Automatic conflict resolution** | A conflicting land is resolved by a resolver you choose (any LLM provider, a deterministic tool, or none) through a versioned, vendor-neutral protocol. A model's resolution is only a proposal: it lands by itself only if the `verify.command` you configure passes on the exact tree that would land, and otherwise the agent gets the conflict package with the proposal. The deterministic rules you configure need no such condition of their own, and are verified on the exact tree as well when you turn the verification on (`verify.enabled`). |
| **Changeset log** | Every accepted reference update is recorded with its operation and actor in a dense, ordered log that clients list or watch live. |
| **Storage core: a database and object storage, stateless servers** | Each change is a changeset in a write-ahead log in SQLite or PostgreSQL, with a compare-and-swap per reference; packs live in object storage (file, S3, GCS, Azure). Server nodes are caches that any node can rebuild, so you add nodes to scale. |
| **Test after landing, revert the culprit** | `graft-verify` tests the tip, bisects a failure and reverts the change that broke it. |
| **Monitoring agents ("superfans")** | Agents follow the changeset stream and report what matters to each component, also through Slack. |
| **Agent-friendly review** | Reviews with semantic approval rules: a comment-only change can need fewer approvals than a logic change. |
| **Agents as first-class users** | Per-agent tokens, an RPC allowlist and branch policies decide what each agent may do. |
| **Strict cache tiers** | `graft-cache` caches immutable objects in daemon and regional tiers, verifying every object. |

## Architecture

```
        agents, CI jobs, sparse workspaces          graft CLI / Go SDK
                            |
                            v   gRPC
        +-------------------------------------------------+
        |  graft-cache (optional daemon and cache tiers)  |
        +----------------