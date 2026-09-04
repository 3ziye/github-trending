<div align="center">

<img src="assets/banner.webp" alt="Utopia" width="820">

</div>

# Utopia

<div align="center">

[Philosophy](#philosophy) · [Quick start](#quick-start) · [Features](#features) · [Roadmap](#roadmap)

[![Stars](https://img.shields.io/github/stars/deeplethe/utopia?style=flat-square&label=STARS&labelColor=161B22&color=FFC220&logo=github&logoColor=FFFFFF)](https://github.com/deeplethe/utopia/stargazers)
[![License](https://img.shields.io/badge/LICENSE-APACHE%202.0-3FB950?style=flat-square&labelColor=161B22)](LICENSE)
[![Rust](https://img.shields.io/badge/BUILT%20WITH-RUST-F74C00?style=flat-square&labelColor=161B22&logo=rust&logoColor=FFFFFF)](https://www.rust-lang.org)

[![Official site](https://img.shields.io/badge/OFFICIAL-UTOPIA.BI-FFFFFF?style=flat-square&labelColor=161B22&logo=safari&logoColor=FFFFFF)](https://utopia.bi)
[![Container](https://img.shields.io/badge/GHCR-DEEPLETHE%2FUTOPIA-2496ED?style=flat-square&labelColor=161B22&logo=docker&logoColor=FFFFFF)](https://github.com/deeplethe/utopia/pkgs/container/utopia)
[![Discussions](https://img.shields.io/badge/DISCUSSIONS-8957E5?style=flat-square&labelColor=161B22&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iI0ZGRkZGRiIgY2xhc3M9ImJpIGJpLWNoYXQtZG90cy1maWxsIiB2aWV3Qm94PSIwIDAgMTYgMTYiPgogIDxwYXRoIGQ9Ik0xNiA4YzAgMy44NjYtMy41ODIgNy04IDdhOSA5IDAgMCAxLTIuMzQ3LS4zMDZjLS41ODQuMjk2LTEuOTI1Ljg2NC00LjE4MSAxLjIzNC0uMi4wMzItLjM1Mi0uMTc2LS4yNzMtLjM2Mi4zNTQtLjgzNi42NzQtMS45NS43Ny0yLjk2NkMuNzQ0IDExLjM3IDAgOS43NiAwIDhjMC0zLjg2NiAzLjU4Mi03IDgtN3M4IDMuMTM0IDggN001IDhhMSAxIDAgMSAwLTIgMCAxIDEgMCAwIDAgMiAwbTQgMGExIDEgMCAxIDAtMiAwIDEgMSAwIDAgMCAyIDBtMyAxYTEgMSAwIDEgMCAwLTIgMSAxIDAgMCAwIDAgMiIvPgo8L3N2Zz4%3D)](https://github.com/deeplethe/utopia/discussions)
[![Built by DeepLethe](https://img.shields.io/badge/BUILT%20BY-DEEPLETHE-2D333B?style=flat-square&labelColor=161B22)](https://github.com/deeplethe)
[![中文](https://img.shields.io/badge/LANG-%E4%B8%AD%E6%96%87-DA3633?style=flat-square&labelColor=161B22)](README.zh-CN.md)

</div>

**The enterprise world model built by [DeepLethe](https://deeplethe.com).** It is the first open substrate for knowledge engineering that learns passively and governs itself. Where a knowledge graph or a vector store works to hold present knowledge, Utopia puts time awareness and ontology in the base layer: the knowledge system evolves as material arrives, and conflict detection, reasoning and decision making all run against that ontology. It deploys offline, so a company can stand up a knowledge foundation, a decision core its agents can trust, and a compliance audit trail on hardware it controls.

> Please note: we would rather this project were not framed as an open-source take on Palantir. It is **a different route to enterprise intelligence, built bottom up from knowledge governance to trustworthy decisions and simulation**.

---

<!-- Video: drop an mp4 into any issue/PR comment box, GitHub returns a
     https://github.com/user-attachments/assets/xxx link,
     paste that link on its own line here and it renders as a player. -->

<div align="center">

https://github.com/user-attachments/assets/aa226443-75de-437e-bd80-88e592ed8457

</div>

---

## Philosophy

We gave it a somewhat romantic name, **Utopia**. Ptolemy's geocentric model was taken for truth for a very long time, then falsified step by step by Copernicus, Kepler, Galileo and Newton. Looking back, what we keep is not only that heliocentrism turned out to be right; it is how that history unfolded.

Where existing vector stores and knowledge graphs work to get present knowledge right, one of Utopia's founding aims is to record the whole course of changing understanding. Engineered, that becomes a **bitemporal knowledge graph**. When a decision is reviewed later, the system can produce the full course it took and the grounds it rested on. To make this hold up in practice we have iterated at length against public corpora spanning enterprise records, education, finance, law and research. Temporality is only one facet; for how knowledge is taken in, how the future is reasoned about, and how logic bounds action, see [utopia.bi/philosophy](https://utopia.bi/philosophy).

## Features

One Rust binary and one Postgres. Full-text search is embedded in the binary, vectors go in pgvector, and the job queue is a table: nothing else to run.

| | |
|---|---|
| **A complete application** | A system console, a graph browser and an ontology workbench in one web UI. A product, not a library: install it and it works. |
| **Knowledge ingest** | Upload PDF, DOCX, PPTX, XLSX, XLS, ODS, CSV, TSV, Markdown, HTML or plain text, with legacy encodings detected on the way in. Web pages, RSS, GitHub, Jira, Notion, WebDAV and S3-compatible buckets sync on a schedule; everything else comes in through the API. |
| **Search and chat** | Full-text on Tantivy, vectors on pgvector, fused with RRF. Answers stream with inl