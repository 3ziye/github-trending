<div align="center">

<img src="https://raw.githubusercontent.com/SoMarkAI/image_bed/main/OXR_README/assets/header.png" alt="" />

<h1>SoMark｜O<span style="color: #DE7802;">X</span>R</h1>

An open-source document parsing model with SOTA accuracy and speed, using an RSI loop during post-training.

---

**Turn documents into Agent-Friendly data.**

[🌐 Online Demo](https://free-oxr.somark.ai) ｜ [🔥 🆓 Free API](#free-api)

[![GitHub | OXR](https://img.shields.io/badge/GitHub-OXR-181717?style=flat-square&logo=github)](https://github.com/SoMarkAI/OXR)   [![Hugging Face | OXR-1.0](https://img.shields.io/badge/Hugging%20Face-OXR--1.0-F59E0B?style=flat-square)](https://huggingface.co/SoMarkAI/OXR-1.0)   [![ModelScope | OXR-1.0](https://img.shields.io/badge/ModelScope-OXR--1.0-624AFF?style=flat-square)](https://modelscope.cn/models/SoMark/OXR-1.0)
![arXiv | Coming Soon](https://img.shields.io/badge/arXiv-Coming%20Soon-B31B1B?style=flat-square)

**English** · [简体中文](README_CN.md)

</div>

OXR (Optical Everything Recognition) is an open-source model from the SoMark team. It turns PDFs and document images into Agent-Friendly data in Markdown or JSON, with layout coordinates included.

Pretrained from scratch, OXR uses a recursive self-improvement (RSI) loop during post-training—a first in document parsing. With just 1.3B parameters, OXR ranks #1 on olmOCR-Bench, OmniDocBench, and DocParsingBench while delivering industry-leading parsing speed.

OXR is the first to make its layout analysis module independent and pluggable. This design accelerates parsing and supports replacing the built-in layout model with a custom one. OXR continues to handle content recognition and reading order, enabling adaptation across diverse scenarios with minimal integration effort.

![](https://raw.githubusercontent.com/SoMarkAI/image_bed/main/OXR_README/assets/three-benchmark-leaderboards-olm-main.png)

![](https://raw.githubusercontent.com/SoMarkAI/image_bed/main/OXR_README/assets/speed-score-overview.png)

---

> If this project helps you, please click ⭐ Star in the top-right corner to support us. It's the best encouragement you can give the developers!



## Why OXR?

- 🎯 SOTA Accuracy. #1 Across Three Benchmarks.

  - OXR ranks 🏆#1 on olmOCR-Bench, OmniDocBench, and DocParsingBench, with a particularly wide lead in table parsing.
  - OXR can recognize 13 document element types, from formulas and tables to chemical equations, chemical structures, and code blocks, with bounding box coordinates included. It also performs well on challenging documents and layouts, including A3 exam papers, newspapers, vertical text, and handwriting.
  - See [docs/benchmark.md](docs/benchmark.md) for the full results and instructions to reproduce the evaluations.
- 🚀 1.3B Parameters. Top-Tier Parsing Speed.

  - With only 1.3B parameters, OXR ranks 🏆#1 among open-source document parsing models in speed tests on the RTX PRO 6000.
  - OXR redesign its processing architecture at the task level to improve parsing speed while maintaining accuracy.
  - See [docs/benchmark.md](docs/benchmark.md) for the full results and instructions to reproduce the evaluations.
- 🧩 Pluggable Layout Analysis. Document Structure on Your Terms.

  - Layout analysis requirements vary widely across domains. Even for the same document, element types, region boundaries, and grouping rules can differ depending on the business use case.
  - OXR is the first to make layout analysis independent and pluggable. Its built-in layout model can be replaced while retaining OXR’s recognition and reading order capabilities, enabling adaptation across document scenarios with minimal integration effort.
  - See the [How it works](#how-to-works) section below for details.


<details>
<summary>Expand to see all 13 element types</summary>

| Name | JSON type value | Content or output format |
|-|-|-|
| Caption | Caption | Plain text |
| Footnote | Footnote | Plain text |
| Formula | Formula | LaTeX |
| Text | Text | Plain text |
| Footer | Page-footer | Plain text (filtered out by default) |
| Header | Page-header | Plain text (filtered out by default) |
| Figure | Picture | Image |
| Title | Title | Plain text |
| Table | Table | HTML / Markdown |
| Stamp | Stamp | Plain text / Image |
| Chemical Equation | Chemical Equation | LaTeX (starting with \ce, using mhchem syntax) |
| Code Block | Code Block | Markdown code block |
| Chemical Structure | Chemical Structure | SMILES / Image |


</details>


## Parsing Examples

The animation shows OXR's parsing process.

![Animated OXR parsing example](https://raw.githubusercontent.com/SoMarkAI/image_bed/main/OXR_README/assets/oxr_parsing_demo.gif)

The examples below show OXR parsing different document types. Click an image to view the original.

<table>
  <tr>
    <td align="center" valign="top"><strong>A3 Exam Paper</strong><br/><a href="https://raw.githubusercontent.com/SoMarkAI/image_bed/main/OXR_README/assets/parsing_examples/a3_exam_paper.png"><img src="https