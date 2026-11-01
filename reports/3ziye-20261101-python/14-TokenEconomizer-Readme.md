# TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents

<p align="center">
  Aaron J. Li<sup>1</sup>,
  Weijia Xu<sup>2</sup>,
  Chandan Singh<sup>2</sup>,
  Zixiao Chen<sup>3</sup>,
  Jeevana Priya Inala<sup>2</sup>,
  Charlotte Siska<sup>3</sup>,
  <br>
  Acar Tamersoy<sup>3</sup>,
  Bin Yu<sup>1</sup>,
  Ion Stoica<sup>1</sup>,
  Michel Galley<sup>2</sup>,
  Jianfeng Gao<sup>2</sup>
</p>
<p align="center">
  <sup>1</sup>UC Berkeley &nbsp; <sup>2</sup>Microsoft Research &nbsp; <sup>3</sup>Microsoft Security
</p>

<p align="center">
  <a href="https://arxiv.org/abs/2610.22732"><img src="https://img.shields.io/badge/arXiv-2610.22732-b31b1b.svg" alt="arXiv"></a>
  <a href="https://tokeneconomizer.github.io"><img src="https://img.shields.io/badge/project-page-2f6fb0.svg" alt="Project page"></a>
  <a href="https://x.com/aaron_jli/status/2114797313613053952"><img src="https://img.shields.io/badge/X-post-000000.svg?logo=x&logoColor=white" alt="X post"></a>
  <img src="https://img.shields.io/badge/python-3.10%2B-3776ab.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="Apache 2.0 license">
</p>

<p align="center">
  Our measurement on SWE-Bench tasks: <b>18.4–30.9% lower mean cost</b> across five agent–model
  combinations, cheaper in <b>all 30</b> repository × combination cells, and Pass@1 up in
  <b>4 of 5</b>. <a href="#results">Results</a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-reduced-motion: reduce)" srcset="docs/assets/teaser.png">
    <img src="docs/assets/teaser.gif" width="100%" alt="An animation that opens on a title card: TokenEconomizer, experience-driven black-box cost control for coding agents, with its three mechanisms (micro-skills, tool pruning, failure-loop intervention), the agents it works with (Claude Code, Codex, GitHub Copilot CLI, Pi) and the UC Berkeley and Microsoft logos. Then a schematic of six sessions in one repository, each a bar of what it cost: the work itself plus three kinds of waste, namely re-learning the repo, tools never used, and getting stuck in loops. Each of the first three sessions teaches TokenEconomizer one thing, in order: 1 micro-skills remember how the repo works (run tests with python -m pytest), 2 tool pruning skips tools never used here (Read and Edit kept, Notebook and Browser left out), and 3 failure-loop intervention spots loops and steps in (the same error three times meets a nudge to try another way). In the session after each lesson that waste shrinks, so the bars step down below a dashed line marking the cost without TokenEconomizer. It ends on results measured on SWE-Bench tasks: 18.4–30.9% lower mean cost across five agent–model combinations, cheaper than default in 30 of 30 repository × combination cells, and Pass@1 up in 4 of 5; per combination, cost 23.6% lower and Pass@1 +1.3 for Claude Code with Sonnet 5, 30.9% and −1.0 with Opus 4.8, 24.7% and +0.9 for Codex with GPT-5.6 Terra, 26.1% and +1.6 with GPT-5.6 Sol, and 18.4% and +2.6 for Copilot CLI with Sonnet 5.">
  </picture>
</p>

TokenEconomizer makes coding agents cheaper to run in the repositories you work in often,
without changing the agent itself. It learns from the sessions an agent has already run in a
repository, and uses that experience to cut waste in the sessions that follow. It has three
mechanisms:

- **Micro-skills: remember how the repository works.** Sessions keep rediscovering the same
  facts: a build step that must run first, the spelling of a command that works here
  (`python -m pytest` where `pytest` is missing, `npx tsc` where `tsc` is), an environment
  variable a command needs, where generated files live. Micro-skills learns such facts, in any
  language, from two sources: failures that repeat across sessions, and a model that reviews the
  recent sessions every *k* sessions (*k* = 3) and proposes facts. A fact is stated at the start
  of each session once three sessions have confirmed it, and dropped when later sessions
  contradict it.
- **Tool pruning: stop loading tools that go unused.** Every loaded tool's definition is sent with
  every request. A tool that goes unused over *p* prompts spread across at least *m* sessions, or
  over *s* sessions of any length (*p* = 10, *m* = 2, *s* = 5), is left out of the next sessions
  through the agent's own settings. One command brings it back.
- **Failure-loop intervention (the loop guard): step in when a turn is stuck.** When a turn (the
  agent's work on one prompt) keeps hitting the same failures, a judge model checks whether it is
  stuck. If the judge is at least *c* sure (*c* = 0.7), the agent gets a redirect (a short note,
  added to its context, to try another approach), at most *r* times per turn (*r* = 1). If the
  turn is still stuck after that, TokenEconomizer tells you how to stop it; it never stops a turn
  itself.

TokenEconomizer is a plugin for **Claude Code**, **Codex**, the **GitHub Copilot CLI** and **Pi**,
w