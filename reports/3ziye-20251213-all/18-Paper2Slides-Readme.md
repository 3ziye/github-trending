<div align="center">

<img src="assets/paper2slides_logo.png" alt="Paper2Slides Logo" width="200"/><br>

# Paper2Slides: From Paper to Presentation in One Click

[![Python](https://img.shields.io/badge/Python-3.12+-FCE7D6.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-C1E5F5.svg)](https://opensource.org/licenses/MIT/)
[![Feishu](https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=wechat&logoColor=white)](./COMMUNICATION.md) 
[![WeChat](https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white)](./COMMUNICATION.md)

✨ **Never Build Slides from Scratch Again** ✨

| 📄 **Universal File Support** &nbsp;|&nbsp; 🎯 **RAG-Powered Precision** &nbsp;|&nbsp; 🎨 **Custom Styling** &nbsp;|&nbsp; ⚡ **Lightning Speed** |

</div>

---

## 🎯 What is Paper2Slides?

Turns your **research papers**, **reports**, and **documents** into **professional slides & posters** in **minutes**.

### ✨ Key Features
- 📄 **Universal Document Support**<br>
  Seamlessly process PDF, Word, Excel, PowerPoint, Markdown, and multiple file formats simultaneously.
  
- 🎯 **Comprehensive Content Extraction**<br>
  RAG-powered mechanism ensures every critical insight, figure, and data point is captured with precision.
  
- 🔗 **Source-Linked Accuracy**<br>
  Maintains direct traceability between generated content and original sources, eliminating information drift.
  
- 🎨 **Custom Styling Freedom**<br>
  Choose from professional built-in themes or describe your vision in natural language for custom styling.
  
- ⚡ **Lightning-Fast Generation**<br>
  Instant preview mode enables rapid experimentation and real-time refinements.
  
- 💾 **Seamless Session Management**<br>
  Advanced checkpoint system preserves all progress—pause, resume, or switch themes instantly without loss.
  
- ✨ **Professional-Grade Visuals**<br>
  Deliver polished, presentation-ready slides and posters with publication-quality design standards.

### ⚡ Easy as One Command
```bash
# One command to generate slides from a paper
python -m paper2slides --input paper.pdf --output slides --style doraemon --length medium --fast --parallel 2
```

---

## 🔥 News

- **[2025.12.09]** Added parallel slide generation (`--parallel`) for faster processing
- **[2025.12.08]** Paper2Slides is now open source!

---

## 🎨 Custom Styling Showcase

<div align="center">

<table>
<tr>
<td align="center" width="290"><img src="assets/doraemon_poster.png?v=2" width="280"/><br/><code>doraemon</code></td>
<td align="center" width="290"><img src="assets/academic_poster.png?v=2" width="280"/><br/><code>academic</code></td>
<td align="center" width="290"><img src="assets/totoro_poster.png?v=2" width="280"/><br/><code>custom</code></td>
</tr>
</table>

<table>
<tr>
<td align="center" width="290"><a href="assets/doraemon_slides.pdf"><img src="assets/doraemon_slides_preview.png?v=2" width="280"/></a><br/><code>doraemon</code></td>
<td align="center" width="290"><a href="assets/academic_slides.pdf"><img src="assets/academic_slides_preview.png?v=2" width="280"/></a><br/><code>academic</code></td>
<td align="center" width="290"><a href="assets/totoro_slides.pdf"><img src="assets/totoro_slides_preview.png?v=2" width="280"/></a><br/><code>custom</code></td>
</tr>
</table>

<sub>✨ Multiple styles available — simply modify the <code>--style</code> parameter<br/>
Examples from <a href="https://arxiv.org/abs/2512.02556">DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models</a></sub>

</div>

<details>
<summary><b>💡 Custom Style Example: Totoro Theme</b></summary>

```
--style "Studio Ghibli anime style with warm whimsical aesthetic. Use soft watercolor Morandi tones with light cream background, muted sage green and dusty pink accents. Totoro character can appear as a friendly guide relating to the content, with nature elements like soft clouds or leaves."
```

</details>

---

### 🌐 Paper2Slides Web Interface

<div align="center">
<table>
<tr>
<td><img src="assets/ui_1.png" width="420"/></td>
<td><img src="assets/ui_2.png" width="420"/></td>
</tr>
</table>
</div>

---

## 📋 Table of Contents

- [🎯 Quick Start](#-quick-start)
- [🏗️ Paper2Slides Framework](#%EF%B8%8F-paper2slides-framework)
- [🔧 Configuration](#%EF%B8%8F-configuration)
- [📁 Code Structure](#-code-structure)

---

## 🏃 Quick Start

### 1. Environment Setup

```bash
# Clone repository
git clone https://github.com/HKUDS/Paper2Slides.git
cd Paper2Slides

# Create and activate conda environment
conda create -n paper2slides python=3.12 -y
conda activate paper2slides

# Install dependencies
pip install -r requirements.txt
```

> [!NOTE]
> Create a `.env` file in `paper2slides/` directory with your API keys. Refer to `paper2slides/.env.example` for the required variables.

### 2. Command Line Usage

```bash
# Basic usage - generate slides from a paper
python -m paper2slides --input paper.pdf --output slides --length medium

# Generate poster with custom style
python -m paper2slides 