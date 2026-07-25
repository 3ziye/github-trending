<div align="center">

<img src="assets/wordmark.svg" alt="OpenScience" width="440">

### The open-source AI workbench for scientific research

Give it a goal. It reads the literature, writes and runs code, runs the experiments, and writes up what it found.

<br/>

[![CI](https://github.com/synthetic-sciences/OpenScience/actions/workflows/ci.yml/badge.svg)](https://github.com/synthetic-sciences/OpenScience/actions/workflows/ci.yml)
[![npm](https://img.shields.io/npm/v/%40synsci%2Fopenscience?label=%40synsci%2Fopenscience&color=0d9488)](https://www.npmjs.com/package/@synsci/openscience)
[![license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![docs](https://img.shields.io/badge/docs-openscience.sh-0d9488.svg)](https://openscience.sh/docs)

[Install](#install) · [Quickstart](#quickstart) · [Docs](https://openscience.sh/docs) · [Atlas](#atlas)

</div>

---

OpenScience is an AI workbench for scientific research. You give it a goal, and it works through the research loop the way a capable collaborator would. It reads the papers that matter, forms a hypothesis, writes and runs code, runs experiments on real compute, queries the major scientific databases, and writes up the result. It runs as a workspace in your browser and works with any frontier or open-weight model from Anthropic, OpenAI, Google, and dozens of other providers, using your own API keys. No account is required.

It is model-agnostic, open source, and built to do real work in machine learning, biology, physics, and chemistry.

## What it does

- **Runs the whole loop.** Literature review, hypothesis, code, experiment, analysis, and write-up, in one continuous session.
- **Research agents.** A `research` agent by default, plus `biology`, `physics`, and `ml` specialists, with critique and literature-review sub-agents and a read-only plan mode.
- **290+ skills.** Training (DeepSpeed, PEFT, TRL), evaluation, dataset work, molecular and clinical biology, cheminformatics, papers and LaTeX, figures, and cloud compute (Modal, Tinker, and others).
- **Scientific databases as tools.** UniProt, PDB, Ensembl, ChEMBL, PubChem, arXiv, OpenAlex, Semantic Scholar, and around 30 more, queryable directly by the agent.
- **A real workspace.** A browser UI with a file tree, an editor, a terminal, session history, and inline rendering for molecules, structures, genomes, and plots.
- **Extensible.** LSP integration, MCP servers, plugins, custom agents and commands, and a TypeScript SDK.

## Install

Install with npm, then open the workspace:

```bash
npm install -g @synsci/openscience
openscience
```

The command is `openscience`, and it opens the workspace in your browser. The first time you run it, a short setup walks you through how to power the models — Atlas managed models, your own provider keys, or skip and start on the free demo models. If you would rather not install it globally, `npx synsci` does the same thing in a single step:

```bash
npx synsci
```

Platform binaries are also attached to [GitHub Releases](https://github.com/synthetic-sciences/OpenScience/releases); see the [changelog](CHANGELOG.md) for what's new in each version.

## Quickstart

Set an API key from any provider (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY`, and so on) and start the workspace:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
openscience
```

`openscience` opens the workspace in your browser. Your keys stay on your machine and requests go straight to the provider. You can also run `openscience keys add` to store a key from the terminal, add keys from the Credentials panel, and pick a model from the model selector. To open the workspace in a specific project:

```bash
openscience ~/code/my-project
```

## Atlas

[Atlas](https://app.syntheticsciences.ai) is Synthetic Sciences' managed platform. It gives you a curated set of frontier models billed from a prepaid wallet, so you do not need per-provider keys, plus a persistent research graph and cloud compute. OpenScience works with Atlas but never requires it.

```bash
openscience login          # connect your Atlas account
openscience wallet         # check your balance and top up
```

Bring-your-own-key usage is always free and is never gated — Atlas only meters the models it serves. Use `openscience status` to see what you are connected to, and `openscience logout` to disconnect.

## How it works

OpenScience runs a local server that hosts the workspace UI, the agent runtime, and the tool layer. The agent plans with a research harness, calls tools (shell, editor, LSP, MCP servers, scientific connectors, and skills), and streams its work back to the browser. Models are routed per request, so you can switch between providers or run local models without changing anything else. Sessions, artifacts, and provenance are stored on disk and can be shared as links.

| Path                 | Contents                                                     |
| -------------------- | -------------------------