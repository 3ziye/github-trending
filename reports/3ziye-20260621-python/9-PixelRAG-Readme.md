<p align="center">
  <img src="docs/assets/banner.png" alt="PixelRAG — Visual Retrieval-Augmented Generation" width="100%">
</p>
<p align="center">
  Official codebase for <b><a href="assets/pixelrag-paper.pdf">PIXELRAG: Web Screenshots Beat Text for
Retrieval-Augmented Generation</a></b>
</p>
<p align="center">
  <a href="https://yichuan-w.github.io/">Yichuan Wang</a>*,
  <a href="https://zhifei.li/">Zhifei Li</a>*,
  <a href="https://zwcolin.github.io/">Zirui Wang</a>,
  <a href="https://www.linkedin.com/in/paul-teiletche/">Paul Teiletche</a>,
  <a href="https://www.linkedin.com/in/lesheng-jin-9618b0201/">Lesheng Jin</a>
  <br>
  <a href="https://people.eecs.berkeley.edu/~matei/">Matei Zaharia</a>†,
  <a href="https://people.eecs.berkeley.edu/~jegonzal/">Joseph E. Gonzalez</a>†,
  <a href="https://www.sewonmin.com/">Sewon Min</a>†
</p>
<p align="center"><sub>* Equal contribution &nbsp; † Equal advising</sub><br><sub>Work done at <a href="https://sky.cs.berkeley.edu/">Berkeley SkyLab</a> &amp; <a href="https://bair.berkeley.edu/">BAIR</a> &amp; <a href="https://nlp.cs.berkeley.edu/">Berkeley NLP</a></sub></p>
<p align="center">Search any document by how it <em>looks</em>, not just the text it contains.</p>

<p align="center">
  <a href="https://github.com/StarTrail-org/PixelRAG/actions/workflows/ci.yml"><img src="https://github.com/StarTrail-org/PixelRAG/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://pixelrag.ai"><img src="https://img.shields.io/badge/demo-pixelrag.ai-7c3aed" alt="Live demo"></a>
  <a href="https://status.pixelrag.ai"><img src="https://img.shields.io/badge/status-live-22c55e" alt="Status"></a>
  <a href="https://join.slack.com/t/leann-e2u9779/shared_invite/zt-3ol2ww9ic-Eg_kB8omwe6xmYVd0epr4Q"><img src="https://img.shields.io/badge/Slack-join-4A154B?logo=slack&logoColor=white" alt="Slack"></a>
  <img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="License">
</p>

<p align="center">
  <a href="#what-it-is">What it is</a> &middot;
  <a href="#give-claude-eyes">Give Claude eyes</a> &middot;
  <a href="#how-it-works">How it works</a> &middot;
  <a href="#pipelines">Pipelines</a>
</p>

---

```bash
pip install pixelrag
```

The two core operations — **render** a page to screenshots, **search** a visual index:

```bash
# Render any page or document to screenshot tiles
pixelshot https://en.wikipedia.org/wiki/Python --output ./tiles

# Search a hosted index of 8.28M Wikipedia pages — no setup, runs against the live API
curl -X POST https://api.pixelrag.ai/search \
  -H "Content-Type: application/json" \
  -d '{"queries": [{"text": "What is the capital of France?"}], "n_docs": 5}'
```

> **Live, hosted endpoint** — [`https://api.pixelrag.ai`](https://api.pixelrag.ai/status) serves a
> pre-built index of **8.28M Wikipedia pages**. No setup, no API key. It even takes an image as the query
> ([visual search](https://pixelrag.ai/docs#search)) — see the **[API reference →](https://pixelrag.ai/docs)**.

Or try it in the browser at **[pixelrag.ai](https://pixelrag.ai)**, or run the demo notebook in
Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/StarTrail-org/PixelRAG/blob/main/demos/quickstart.ipynb) — it
renders a page and searches the hosted index, with the images inline.

## What it is

PixelRAG renders documents — web pages, PDFs, images — as screenshots and retrieves over the
images directly. Visual structure that HTML parsing throws away — tables, charts, layout,
infographics — stays intact, so the reader model can actually answer questions about it.
Wikipedia's 8.28M articles ship as a pre-built index; the pipeline itself is general-purpose.

## Give Claude eyes

The renderer also ships as a Claude Code plugin — the **pixelbrowse** skill. Instead of fetching
raw HTML, Claude screenshots a page with `pixelshot` and _reads the image_, so it sees
charts, diagrams, tables, and layout the way a person does.

Install it — no clone needed (`pixelshot` comes from `pip install pixelrag`):

```bash
pip install pixelrag                                # provides the pixelshot command
claude plugin marketplace add StarTrail-org/PixelRAG
claude plugin install pixelbrowse@pixelrag-plugins
```

Then just ask Claude to look at a page:

```bash
claude -p "screenshot https://news.ycombinator.com and summarize the top stories"
claude -p "screenshot https://arxiv.org/abs/2404.12387 and explain the key findings"
```

Or use the slash command in an interactive session: `/screenshot https://example.com`.
No MCP server, no backend: the skill just calls `pixelshot` (Playwright/CDP) on your machine.

## How it works

<p align="center">
  <img src="docs/assets/pipeline.png" alt="Text-based RAG parses to text and loses the table; PixelRAG renders to screenshot tiles and keeps it" width="100%">
</p>

Text-based RAG parses the page to text chunks and **loses the table** — the reader can't find the
answer. PixelRAG r