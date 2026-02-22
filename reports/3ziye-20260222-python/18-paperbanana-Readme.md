<!-- mcp-name: io.github.llmsresearch/paperbanana -->
<table align="center" width="100%" style="border: none; border-collapse: collapse;">
  <tr>
    <td width="220" align="left" valign="middle" style="border: none;">
      <img src="https://dwzhu-pku.github.io/PaperBanana/static/images/logo.jpg" alt="PaperBanana Logo" width="180"/>
    </td>
    <td align="left" valign="middle" style="border: none;">
      <h1>PaperBanana</h1>
      <p><strong>Automated Academic Illustration for AI Scientists</strong></p>
      <p>
        <a href="https://github.com/llmsresearch/paperbanana/actions/workflows/ci.yml"><img src="https://github.com/llmsresearch/paperbanana/actions/workflows/ci.yml/badge.svg" alt="CI"/></a>
        <a href="https://pypi.org/project/paperbanana/"><img src="https://img.shields.io/pypi/dm/paperbanana?label=PyPI%20downloads&logo=pypi&logoColor=white" alt="PyPI Downloads"/></a>
        <a href="https://huggingface.co/spaces/llmsresearch/paperbanana"><img src="https://img.shields.io/badge/Demo-HuggingFace-yellow?logo=huggingface&logoColor=white" alt="Demo"/></a>
        <br/>
        <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white" alt="Python 3.10+"/></a>
        <a href="https://arxiv.org/abs/2601.23265"><img src="https://img.shields.io/badge/arXiv-2601.23265-b31b1b?logo=arxiv&logoColor=white" alt="arXiv"/></a>
        <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?logo=opensourceinitiative&logoColor=white" alt="License: MIT"/></a>
        <br/>
        <a href="https://pydantic.dev"><img src="https://img.shields.io/badge/Pydantic-v2-e92063?logo=pydantic&logoColor=white" alt="Pydantic v2"/></a>
        <a href="https://typer.tiangolo.com"><img src="https://img.shields.io/badge/CLI-Typer-009688?logo=gnubash&logoColor=white" alt="Typer"/></a>
        <a href="https://ai.google.dev/"><img src="https://img.shields.io/badge/Gemini-Free%20Tier-4285F4?logo=google&logoColor=white" alt="Gemini Free Tier"/></a>
      </p>
    </td>
  </tr>
</table>

---

> **Disclaimer**: This is an **unofficial, community-driven open-source implementation** of the paper
> *"PaperBanana: Automating Academic Illustration for AI Scientists"* by Dawei Zhu, Rui Meng, Yale Song,
> Xiyu Wei, Sujian Li, Tomas Pfister, and Jinsung Yoon ([arXiv:2601.23265](https://arxiv.org/abs/2601.23265)).
> This project is **not affiliated with or endorsed by** the original authors or Google Research.
> The implementation is based on the publicly available paper and may differ from the original system.

An agentic framework for generating publication-quality academic diagrams and statistical plots from text descriptions. Supports OpenAI (GPT-5.2 + GPT-Image-1.5), Azure OpenAI / Foundry, and Google Gemini providers.

- Two-phase multi-agent pipeline with iterative refinement
- Multiple VLM and image generation providers (OpenAI, Azure, Gemini)
- Input optimization layer for better generation quality
- Auto-refine mode and run continuation with user feedback
- CLI, Python API, and MCP server for IDE integration
- Claude Code skills for `/generate-diagram`, `/generate-plot`, and `/evaluate-diagram`

<p align="center">
  <img src="assets/img/hero_image.png" alt="PaperBanana takes paper as input and provide diagram as output" style="max-width: 960px; width: 100%; height: auto;"/>
</p>

---

## Quick Start

### Prerequisites

- Python 3.10+
- An OpenAI API key ([platform.openai.com](https://platform.openai.com/api-keys)) or Azure OpenAI / Foundry endpoint
- Or a Google Gemini API key (free, [Google AI Studio](https://makersuite.google.com/app/apikey))

### Step 1: Install

```bash
pip install paperbanana
```

Or install from source for development:

```bash
git clone https://github.com/llmsresearch/paperbanana.git
cd paperbanana
pip install -e ".[dev,openai,google]"
```

### Step 2: Get Your API Key

```bash
cp .env.example .env
# Edit .env and add your API key:
#   OPENAI_API_KEY=your-key-here
#
# For Azure OpenAI / Foundry:
#   OPENAI_BASE_URL=https://<resource>.openai.azure.com/openai/v1
```

Or use the setup wizard for Gemini:

```bash
paperbanana setup
```

### Step 3: Generate a Diagram

```bash
paperbanana generate \
  --input examples/sample_inputs/transformer_method.txt \
  --caption "Overview of our encoder-decoder architecture with sparse routing"
```

With input optimization and auto-refine:

```bash
paperbanana generate \
  --input my_method.txt \
  --caption "Overview of our encoder-decoder framework" \
  --optimize --auto
```

Output is saved to `outputs/run_<timestamp>/final_output.png` along with all intermediate iterations and metadata.

---

## How It Works

PaperBanana implements a multi-agent pipeline with up to 7 specialized agents:

**Phase 0 -- Input Optimization (optional, `--optimize`):**

0. **Input Optimizer** runs two parallel VLM calls:
   - **Context Enricher** structures raw methodology text into diagram-ready f