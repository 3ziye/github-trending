<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="brand/logo-lockup-dark.png">
    <img src="brand/logo-lockup.png" alt="ClearAI" width="360">
  </picture>
</p>

<p align="center"><b>English</b> · <a href="README.zh-CN.md">中文</a></p>

<p align="center">
  <a href="https://trendshift.io/repositories/248415?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-248415" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/248415/weekly?language=JavaScript" alt="Clearailhc%2Fclearai-dsh | Trendshift" width="250" height="55"/></a>
</p>

**Your research, grown into an ontology.**

ClearAI is an **ontology discovery and exploration platform**, built on two core concepts:

- **Domain ontology** (what you get) — your project's own vocabulary, the knowledge entries established through the loop, and their graphs. At the end of a research session you hold a continuously growing knowledge structure, retrievable next round by concept.
- **Epistemic loop** (how you get it) — a disciplined seven-stage path: frame, hypothesize, plan, observe, verify, evaluate, record. Every edge is tested by evidence and independent evaluation.

> Other knowledge graphs pile up edges by extraction and assertion; here every edge has to be earned through the loop.

```bash
# Install (npm package, prebuilt — no build step, no allowBuilds prompt)
dsh plugin --profile web add clearai-dsh@0.3.1
# or in the app: Plugins → Add plugin → clearai-dsh@0.3.1
```

Restart `dsh web`, then pick **ClearAI** in the preset picker at the top of a new session. That is the whole setup. [Full install notes ↓](#install-and-use)


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/diagrams/ontology-hero-dark.png">
  <img src="docs/diagrams/ontology-hero.png" alt="The epistemic loop (left) growing a domain ontology (right)" width="1200">
</picture>

*Left: the Epistemic Loop — seven stages. Its emerald fact dot is also the first node of the domain ontology on the right. Right: the ontology graph — dark is a concept, light is a value form, emerald an instance; the instance carries two contradictory assertions — **the two readings are tinted amber**, marking that they do not agree. The system reports the conflict; retracting or keeping is a human decision.*

---

## What you get: a domain ontology

A **domain ontology** that grows as you research:

- **Vocabulary** — the language your project speaks: concepts, predicates, value forms, units. Conventions themselves carry no truth value; sentences written with them do.
- **Established entries** — knowledge that passed the loop: each with its boundary, support level, and evidence chain. Each entry states its boundary explicitly, so it can be cited safely.
- **Ontology graph and entity graph** — what your domain looks like (structure), and what you have actually verified (the state of play).
- **Conflict readings** — contradictory conclusions surface automatically; the system reports them, and retracting or keeping is your decision.

## How you get it: the Epistemic Loop

Most agent loops track one thing: whether the task is done. The Epistemic Loop also tracks **what makes a conclusion trustworthy**:

| | Task loop | Epistemic loop |
|---|---|---|
| Driving question | What next? | What do we know, and on what grounds? |
| Completion | The model declares it | The system computes it from delivered evidence |
| Verdict | Whoever did it, says so | Separated — above a level, the doer cannot judge themselves |
| Failure | Deleted, retried, forgotten | Kept: a refuted hypothesis is a result, not noise |
| What accumulates | A chat transcript | **An ontology**: every edge earned through the loop |

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/diagrams/epistemic-loop-hero-dark.png">
  <img src="docs/diagrams/epistemic-loop-hero.png" alt="The Epistemic Loop" width="1000">
</picture>

*Inside the ring is the instrument's read-out: the L0–L4 axis, the **pre-registered** threshold as a dashed line, and five observations with error bars — the supported one filled, the inconclusive drawn as a dashed circle, the refuted left in place with a slash through it (nothing is deleted). The emerald dot at the opening is the one reading that crossed the threshold and settled as a fact.*

At runtime, the seven stages compress into four beats — plan, execute, observe, reflect. State is derived from the session record with no second store; the tools the model holds contain no field in which it could declare a step complete.

ClearAI does **not** claim recursive self-improvement. It provides the epistemic substrate a self-improving system would need. See [Positioning](docs/positioning.md) and the [OpenRSI survey](docs/research-openrsi.md).

---

## Install and use

**Requirements:** DSH ≥ `0.1.7-alpha.1` — that generation introduced the composition declaration line this preset rides on. 