<div align="center">
  <img src="web/public/icon-512.png" alt="" width="72" height="72">
  <h1>Memdoor</h1>
  <p><strong>The workflow harness that makes a small model beat a frontier one, on your machine.</strong><br>Five Qwen3.8-27B agents beat Fable 5 on LiveCodeBench Hard, every run published. Ollama, llama.cpp, or any key. One binary, no account.</p>
  <p>
    <a href="https://news.ycombinator.com/item?id=50320995"><img alt="Hacker News" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhacker-news.firebaseio.com%2Fv0%2Fitem%2F50320995.json&query=%24.score&label=Hacker%20News&suffix=%20points&logo=ycombinator&logoColor=white&color=ff6600"></a>
    <a href="LICENSE"><img alt="Apache 2.0" src="https://img.shields.io/badge/license-Apache%202.0-blue"></a>
    <a href="https://github.com/guregodevo/memdoor/actions/workflows/lint.yml"><img alt="CI" src="https://github.com/guregodevo/memdoor/actions/workflows/lint.yml/badge.svg"></a>
    <a href="https://github.com/guregodevo/memdoor/actions/workflows/installers.yml"><img alt="Installers" src="https://github.com/guregodevo/memdoor/actions/workflows/installers.yml/badge.svg"></a>
    <img alt="Go" src="https://img.shields.io/badge/Go-one%20static%20binary-00ADD8">
    <img alt="Platforms" src="https://img.shields.io/badge/macOS%20%C2%B7%20Linux%20%C2%B7%20Windows-lightgrey">
  </p>
</div>

> **Five Qwen3.8-27B agents beat Fable 5 on LiveCodeBench Hard, as a Memdoor workflow.**
> [GVS5H](https://github.com/slee-persis/GVS5H)'s harness rebuilt with the
> authors' exact prompts and loop. The first ten problems of their list, five
> passes each: a mean of **9.8 of 10**. The authors' own harness scored 9.6 and
> Fable 5 in a single call 8.0, the gap the authors measured on these ten
> (across their full 100: 92.4 and 90.4). All 50 runs are published: every
> request, reply, program and grader output. The workflow is YAML and names no
> model. Point it at yours, or at a local one with `memdoor connect local`
> (Ollama, llama.cpp, vLLM, LM Studio; [how to run it on an open-weight model,
> no key](https://memdoor.ai/docs/open-weight)).
> [examples/workflows/team-solve](examples/workflows/team-solve/) · [the result page](https://memdoor.ai/docs/team-solve) · [the HN thread](https://news.ycombinator.com/item?id=50320995)

Memdoor is a coding agent and workflow runner. Give the agent a task to read
files, edit code and run checks. For repeatable work, a workflow coordinates
checked steps, parallel tasks and approval gates. Run it with a local model or
a provider on your key.

On this machine:

```bash
curl -fsSL https://memdoor.ai/install.sh | bash
export OPENROUTER_API_KEY=sk-or-...    # or ANTHROPIC_API_KEY, OPENAI_API_KEY, GEMINI_API_KEY, …
# or no key: memdoor connect local    # an open-weight model on this machine — https://memdoor.ai/docs/open-weight
cd your-project && memdoor             # the first run sets the machine up
```

The install or the first run did not finish: [open an Install issue](https://github.com/guregodevo/memdoor/issues/new?template=install.md).

On a box reachable by ssh, nothing installed there:

```bash
curl -fsSL https://memdoor.ai/install.sh | bash          # here, once
memdoor --gateway ssh://you@box                           # installs memdoor on the box, starts its gateway, opens the window on it
memdoor --gateway ssh://you@box connect openrouter        # your key, kept on the box; every turn there runs on it
memdoor --gateway ssh://you@box run "fix the failing test" # the same box from a script or CI
```

<p align="center"><img src="docs/img/memdoor-window.png" alt="The window: a task typed, the files read and patched, the tests run, and the receipt line: checked, 2 files changed, tests PASS" width="880"></p>

**Decision model.** Jev (TypeSafe) answers a typed question about a turn
with a calibrated probability in under half a second. Judged reads: search,
file and log reads return what counts. Per-turn toolbox: only the tools the
turn needs are sent. Stall detection: a turn that stops making progress ends.
44 paired runs, decisions off and on: 22 of 22 passed each way; a codebase
question 54,661 to 14,367 input tokens (−74%); an edit with a test and ten
one-file fixes read the same files either way (within ±11%)
([`docs/features/DECIDE.md`](docs/features/DECIDE.md)).

**Workflows, the deterministic harness.** Say the steps; the coder writes one
YAML per step. [`mario`](https://github.com/guregodevo/mario) runs the graph.
Independent steps run in parallel. A step is done when its check passes. A
gate waits for approval with the diff. A failed run resumes at the failed
step. Started by hand, from CI or on local cron
([`docs/features/WORKFLOWS.md`](docs/features/WORKFLOWS.md)). Workflows, not
skills: [the write-up](https://guregodevo.github.io/2026/10/06/workflows-not-skills/).
Examples, each run before it was added:
[`examples/workflows/`](examples/workflows/). The nightly grade step,
`examples/workflows/nightly-rule/steps