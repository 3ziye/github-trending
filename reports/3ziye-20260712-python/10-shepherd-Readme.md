<div align="center">
<img src="https://shepherd-agents.ai/assets/logo-shepherd.png" alt="Shepherd" width="140">
<h1>Shepherd: Programmable Meta-Agents via Reversible Execution Traces</h1>

![Status: Alpha](https://img.shields.io/badge/status-alpha-orange?style=for-the-badge) [![PyPI](https://img.shields.io/pypi/v/shepherd-ai?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/shepherd-ai/) [![Python](https://img.shields.io/pypi/pyversions/shepherd-ai?style=for-the-badge&logo=python&logoColor=white&label=)](https://pypi.org/project/shepherd-ai/) [![Homepage](https://img.shields.io/badge/Homepage-4d8cd8?style=for-the-badge&logo=google-chrome&logoColor=white)](https://shepherd-agents.ai/) [![Docs](https://img.shields.io/badge/Docs-4d8cd8?style=for-the-badge&logo=materialformkdocs&logoColor=white)](https://docs.shepherd-agents.ai/) [![Paper](https://img.shields.io/badge/Paper-2605.10913-red?style=for-the-badge)](https://arxiv.org/abs/2605.10913) [![Blog](https://img.shields.io/badge/Blog-4d8cd8?style=for-the-badge)](https://shepherd-agents.ai/blog)
</div>

---

> [!IMPORTANT]
> **Shepherd is in early alpha** and under active development.
> APIs may still change between releases. Feedback and issues are very welcome!

<p align="center">
  <a href="#installation">Install</a> |
  <a href="#quickstart">Quickstart</a> |
  <a href="#permissions-the-signature-is-the-permission-surface">Permissions</a> |
  <a href="#examples">Examples</a> |
  <a href="https://docs.shepherd-agents.ai/">Docs</a> |
  <a href="#citation">Citation</a>
</p>

**Shepherd** is a runtime substrate for agent work that needs inspection,
reversibility, and supervision. It records agent runs as durable, inspectable
execution traces, with retained workspace outputs that can be reviewed before
they are selected, applied, released, or discarded.

> **Platforms.** Shepherd requires **Python 3.11+**. OS-level grant enforcement
> is executed on **both macOS** (Seatbelt) and **Linux** (Landlock, in a privileged
> container). **Windows is unsupported** (enforcement would be
> advisory-only at best) — use **WSL**.

## Installation

```bash
pip install shepherd-ai
```

Working on Shepherd itself? Install the local editable closure instead:
`python -m venv .venv && . .venv/bin/activate && pip install -r requirements-dev.txt`
(see [CONTRIBUTING.md](https://github.com/shepherd-agents/shepherd/blob/main/CONTRIBUTING.md)).

## Quickstart

Shepherd is an agent framework: a task's implementation can be a sandboxed
agent, and its work comes back as a **reviewable proposal** — nothing touches
your files until you accept it. Here the whole body of a task *is* a Claude
agent.

> Needs the `claude` CLI — signed in (a Claude subscription works) or with an
> `ANTHROPIC_API_KEY`. Neither? Jump to the
> [Offline Quickstart](#offline-quickstart) — it runs anywhere, keyless.
>
> On a subscription, a sandboxed run is most reliable with a long-lived token:
> `export CLAUDE_CODE_OAUTH_TOKEN=$(claude setup-token)`. A short-lived signed-in
> session can't be refreshed from inside the sandbox, so it may work
> interactively yet fail here — `shepherd doctor claude` (add `--probe` for a real
> auth round-trip under Shepherd's config, in the parent — not a jailed run) tells
> you which credential you have before you run. If Claude returns an org-policy
> error (HTTP 403), that's an account/organization limit, not a login problem — a
> different key or your org admin is the fix. And an outright `claude` CLI hang
> (e.g. a stale version) surfaces as a budget timeout, not an auth error.

A task is a plain Python function with **no body**; the signature and docstring
are the contract the agent fulfils at runtime — including its permissions:
`repo: sp.GitRepo` is the explicit writable workspace-handle grant that lets the
agent write the repository (see
[Permissions](#permissions-the-signature-is-the-permission-surface)):

```python
def write_program(
    repo: sp.GitRepo,
    prompt: str,
    output_path: str = "program.py",
) -> None:
    """Write a small, self-contained Python program that does what `prompt` asks.

    Save it to output_path. It must run with plain `python3`, read no input,
    and finish on its own within about ten seconds.
    """
```

Set up a scratch workspace and check the agent lane is ready:

```bash
mkdir /tmp/agent-task && cd /tmp/agent-task
shepherd init             # turn this directory into a Shepherd workspace
shepherd doctor claude    # confirm claude CLI, sign-in/key, and sandbox are ready
```

Fetch the demo and let the agent work (about a minute):

```bash
shepherd demo write agent-task > agent_task.py
python agent_task.py
```

The agent writes `donut.py` — but not into your directory. It lands as a
**retained output**: a proposal held safely to one side, which you can run
without applying anything:

```bash
shepherd run changeset --latest --read donut.py | python3 -
```

Ten seconds of spinning ASCII donut, straight out of the retain