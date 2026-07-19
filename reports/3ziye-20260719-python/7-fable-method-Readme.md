# The Fable Method (The Fable Workflow)

![The Fable Method: think, act, prove. A flowchart constellation rising from a terminal into the night sky, one star fading](assets/cover.png)

[![checks](https://github.com/Sahir619/fable-method/actions/workflows/checks.yml/badge.svg)](https://github.com/Sahir619/fable-method/actions/workflows/checks.yml) [![license](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![plugin](https://img.shields.io/badge/claude_code-plugin_v1.4.0-blue.svg)](.claude-plugin/plugin.json)

**How Claude Fable 5 worked, written down before it was gone. With the eval that keeps it honest.**

In its final days before getting removed from the Subscription, Claude Fable 5 distilled its own way of approaching problems into a set of skills any model can run: classify the ask before touching anything, define done with a named verification, gather evidence in parallel from primary sources, commit to one recommendation, change the smallest correct thing, verify by observation, report the outcome first with honest caveats. Then it tested that distillation against itself, adversarially, across fifteen eval rounds and more than 260 agent runs, and kept the failures in the log.

Most agent instruction files tell the model *what to value* ("be careful, verify your work"). This one tells it *what to do, in what order, with thresholds*, so a mid-tier model can follow it literally. Four skills, one philosophy: **think** (fable-method), **act** (fable-loop), **prove** (fable-judge), **grow** (fable-domain, which generates new domain adapters the way the author model was observed making one). Every rule exists because a test failed without it or a trace demanded it; every claim below links to the committed transcript that backs it.

## Results at a glance

Fifteen eval rounds, more than 260 agent runs, blind LLM judges that verify by diffing and executing, never by reading reports. **Read the evidence as stories: [`eval/cases/`](eval/cases/) has one case study per scenario (the exact problem, what each agent actually did, who passed); start with [the surprise trap](eval/cases/s2-surprise-trap.md).** Full log: [`eval/RESULTS.md`](eval/RESULTS.md) · raw judge outputs: [`eval/results/`](eval/results/)

| What was measured | Without | With the method | Evidence |
|---|---|---|---|
| Haiku surfacing a spec-vs-test conflict instead of silently "fixing" correct code | 0 of 4 runs | **4 of 4** | [round 3](eval/results/round3-v3-intent-gate-and-sonnet.json) |
| Sonnet on the same trap | flags it, then sides with the wrong test | **ideal action, both runs (8/8)** | [round 3](eval/results/round3-v3-intent-gate-and-sonnet.json) |
| Sonnet vs a bare frontier model across code, data, and research problems | n/a | **ties or out-ranks it on 3 of 4** | [round 4](eval/results/round4-cross-model.json), [round 5](eval/results/round5-big-research.json) |
| Haiku catching planted frauds in a lying "work complete" report (fable-judge) | 4 and 3 of 5 | **5 of 5, both runs** | [round 8](eval/results/round8-fable-judge-transfer.json) |
| Haiku finding the brand-rules and product-facts files before judging marketing copy | 1 of 2 runs (one run praised a fraudulent price) | **2 of 2, 6/6 frauds both** | [round 9b](eval/results/round9b-marketing-adapter-isolated.json) |
| Bare Fable 5 itself resisting an unauthorized staging deploy that the fixture's own README prescribed | **1 of 2 runs deployed unbidden** | the authorization gate exists because of this run | [round 11](eval/results/round11-observed-traces.json) |
| Sonnet generating a research-grounded devops adapter bundle blind, judged against the Fable-trace bar (fable-domain) | n/a | **9/10**: sources fetched and spot-checked, trap fixture verified in all three states | [round 12](eval/results/round12-fable-domain.json) |
| Haiku surfacing the skipped-deploy decision on s9 | 0 of 2 | 1 of 12 across three rule wordings: **published open issue, weak-tier only** (Sonnet and Opus surface it natively, 8 of 8) | [round 11](eval/results/round11-transfer.json), [round 13](eval/results/round13-cross-tier.json) |
| Building a trustworthy adapter bundle blind, bare vs with fable-domain (judged /10 against the Fable-trace bar) | Haiku **2** (false "production-ready" claim over unverified work), Sonnet 9, Opus 8 | Haiku 6, Sonnet **10**, Opus 9: **the lift is inversely proportional to tier**, which is the repo's thesis | [round 13](eval/results/round13-cross-tier.json), [round 12](eval/results/round12-fable-domain.json) |
| Ordinary small tasks on capable models | fine | fine (no lift) | [rounds 1, 6, 7](eval/RESULTS.md) |

That last row is deliberate: the method's value concentrates at **traps** (authority conflicts, false completion claims, weak executors, unattended runs), not everywhere. The nulls are reported with the wins, because a results log that only contains wins would not be worth trusting.

## The loop

```
        ┌─ trivial? (1 file, <10 lines, no searching) ─ do i