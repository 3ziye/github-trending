![CodexLoom visual identity: long-lived threads woven into an agent organization](docs/assets/codexloom-vi-direction.png)

# CodexLoom

> **Loom your Codex.**

**A working environment for long-running Codex Agents.**

**English** · [简体中文](README.zh-CN.md)

> Owner-facing product language is reviewed in Simplified Chinese first. The
> [Chinese Owner Guide](docs/owner-guide.zh-CN.md) is canonical; this English
> README and Guide are translations and must not introduce independent product
> meaning.

Give each Agent a durable Domain responsibility, organize them into a governed
Team, and deliver mature capabilities to customers, communities, and
collaborators through Interface Agents.

Inside, continuously govern a long-running Agent Team. Outside, provide one
clear service surface while the responsible Domain Agents complete professional
work within explicit identity, Conversation, authorization, and information
boundaries.

[Website](https://codexloom.ai/en/) · [中文官网](https://codexloom.ai/zh-cn/) · [Owner guide（简体中文，canonical）](docs/owner-guide.zh-CN.md) · [English guide](docs/owner-guide.md) · [Get started](#quick-start) · [Community](#community) · [Documentation](#documentation)

## What Is CodexLoom

CodexLoom is built on Codex. It does not reimplement the agent runtime or
duplicate thread history. Instead, it turns a Codex thread into the continuing
workspace of a long-running Domain Agent, then adds durable identity, Profile,
Team relationships, bounded coordination, human governance, and governed
external delivery.

In CodexLoom, an Agent has a stable ID, name, Profile, and primary Thread. The
same Agent can resume its current work through Codex Desktop, Mobile, or the
CodexLoom WebUI. Other Agents collaborate through bounded Messages and Topics
and consume explicit managed Artifact handoffs; they do not resume that Agent's
primary Thread. External collaborators can work through governed Interface
Agents from existing environments such as Feishu (Lark), Slack, and Parall.

Start with one long-lived Agent for a continuing responsibility. When repeated
work reveals stable load, context, or professional judgment boundaries, the
Owner can divide that responsibility among additional Agents and declare how
they collaborate. When the team needs to participate in an external
organization, the Owner can give an Agent a governed identity and a different
role in each conversation. Lead, Internal Agent, and Interface Agent are useful
organization patterns, not hard-coded Agent types.

> **Codex provides the threads; CodexLoom weaves them into an agent organization.**

The name `Loom` describes this organizing process: every thread keeps its own history and direction while responsibilities and relationships weave it into a larger collaborative structure.

## What You Can Do Today

- **Long-lived agents:** Maintain a stable identity, editable name, primary thread, Profile, and model configuration for each agent.
- **One thread, multiple surfaces:** Work on the same thread from Codex Desktop, Mobile, the WebUI, and the CLI, with live message and status synchronization.
- **Agent-to-agent communication:** Send, queue, and reply to Messages while preserving delivery state, response relationships, and complete history.
- **Bounded coordination and human decisions:** Coordinate cross-Agent work
  through Topics, request explicit Owner decisions through Needs You, and hand
  off final files through managed Artifacts.
- **Team structure:** Separate draggable Organization, Collaboration, and Activity maps keep formal responsibility, declared cross-domain work, and Message evidence distinct; Directory remains the precise view of every Agent.
- **Overview and governance evidence:** Inspect current Status, Daily Activity,
  Capacity signals, and token/context/cache/model usage without treating them as
  performance scores or automatic organization decisions.
- **Governed external delivery:** Manage external identities, Conversation
  Memberships, Inbox, and Outbox through Feishu (Lark), Slack, and Parall, with
  Interface Agents acting as explicit organizational boundaries.
- **Continuous operations:** Run Schedules, resume existing work through durable external Triggers, inspect global runtime state, create backups on demand, and restart gracefully after active turns finish.

Lead, Internal Agent, and Interface Agent are currently expressed through Profiles, declared relationships, Messages, and Conversation Memberships. Dedicated hierarchical messaging policies and organization templates are still being modeled.

## Who Is It For

### Advanced Individuals and One Person Company Owners

- Maintain several specialized agents over the long term.
- Use the Codex app for daily work.
- Let agents responsible for different domains collaborate directly.
- Bring agents into work groups and communities they already use.
- Let colleagues collaborate with a governed Agent through Feishu or Slack,
  reusing professional capability the Ow