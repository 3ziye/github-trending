<h1 align="center">📚 book-to-skill</h1>

<p align="center">
  <strong>Turn any technical book or document into a Claude Code skill — ready to study, reference, and use while you work.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-Skill-blueviolet?style=for-the-badge" alt="Claude Code Skill">
  <img src="https://img.shields.io/badge/PDF%20%E2%80%A2%20EPUB%20%E2%80%A2%20DOCX%20%E2%80%A2%20MD%20%E2%80%A2%20HTML%20%E2%80%A2%20RTF%20%E2%80%A2%20MOBI-supported-green?style=for-the-badge" alt="Formats supported">
  <img src="https://img.shields.io/badge/effort-high-orange?style=for-the-badge" alt="Effort: high">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT License">
</p>

<p align="center">
  <a href="#-why">Why</a> ·
  <a href="#-what-it-generates">What it generates</a> ·
  <a href="#-usage">Usage</a> ·
  <a href="#-requirements">Requirements</a> ·
  <a href="#-how-it-works">How it works</a> ·
  <a href="#-faq">FAQ</a> ·
  <a href="#-install">Install</a>
</p>

---

## 🤔 Why

You buy a great technical book. You read it once. Three months later you can't remember chapter 7 existed.

The usual workarounds don't help:
- 📄 "Let me just search the PDF" → you get a list of pages, not answers
- 🧠 "I'll ask Claude about this book" → it either hallucinates or says it doesn't have the content
- 📝 "I'll take notes as I read" → you end up with a 200-line doc you never open again

**book-to-skill solves this by turning the book into a structured skill Claude loads on demand.**

Once installed, you just type `/your-book-slug replication` and Claude reads the right chapter and answers from the actual content. No hallucination. No digging through PDFs. The book becomes part of your workflow.

---

## 📦 What it generates

Running `/book-to-skill your-book.pdf` (or `.epub`) creates a full skill at `~/.claude/skills/<slug>/`:

| File | Purpose | Size |
|------|---------|------|
| `SKILL.md` | Core mental models + chapter index | ~4,000 tokens |
| `chapters/ch01-*.md` … | One file per chapter, loaded on-demand | ~1,000 tokens each |
| `glossary.md` | Every key term, alphabetically sorted with chapter refs | ~1,500 tokens |
| `patterns.md` | All techniques, algorithms, and design patterns | ~2,000 tokens |
| `cheatsheet.md` | Decision tables and quick-reference rules | ~1,000 tokens |

**Chapter files are loaded on-demand** — they don't count against the skill budget until you ask about that topic.

---

## 🚀 Usage

```
/book-to-skill <path-to-document> [skill-name-slug]
```

Supported document formats: PDF, EPUB, DOCX, TXT, Markdown, reStructuredText, AsciiDoc, HTML, RTF, MOBI/AZW/AZW3.

**Examples:**

```bash
# PDF — derive skill name from filename
/book-to-skill ~/Downloads/designing-data-intensive-applications.pdf

# EPUB — specify a custom slug
/book-to-skill ~/books/clean-code.epub clean-code

# Full path with explicit name
/book-to-skill /tmp/ddd-evans.pdf domain-driven-design
```

After the skill is created, use it like any other Claude Code skill:

```bash
/designing-data-intensive-apps                  # load core mental models
/designing-data-intensive-apps replication      # find and explain a topic
/designing-data-intensive-apps ch05             # dive into chapter 5
/designing-data-intensive-apps "what chapters do you have?"
```

---

## 🔧 Requirements

The extractor tries tools in order per format and uses the first available. If nothing is installed, it tells you which command to run. Plain text, Markdown, reStructuredText and AsciiDoc need no extra deps.

**PDF — choose by book type:**

| Book type | Tool | Install | Speed |
|-----------|------|---------|-------|
| Text-heavy (prose, few tables) | `pdftotext` (poppler) | `sudo apt install poppler-utils` | ⚡ instant |
| Text-heavy fallback | `PyPDF2` | `pip3 install PyPDF2` | ⚡ instant |
| Text-heavy fallback | `pdfminer.six` | `pip3 install pdfminer.six` | ⚡ instant |
| **Technical (code, tables, formulas)** | **`docling`** | `pip3 install docling` | ~1.5s/page |

> Before extraction begins, the skill asks you whether the book is **technical** or **text-heavy** and picks the right tool automatically. Docling preserves markdown tables and code blocks; pdftotext is faster for prose-only books.

**EPUB:**

| Tool | Install | Quality |
|------|---------|---------|
| `ebooklib` + `beautifulsoup4` | `pip3 install ebooklib beautifulsoup4` | ⭐⭐⭐ Best |
| stdlib `zipfile` | built-in — no install needed | ⭐⭐ Always available |

**Other formats:**

| Format | Tool | Install |
|--------|------|---------|
| DOCX | `python-docx` (fallback: stdlib ZIP/XML) | `pip3 install python-docx` |
| HTML | `beautifulsoup4` (fallback: stdlib `html.parser`) | `pip3 install beautifulsoup4` |
| RTF | `striprtf` (fallback: regex) | `pip3 install striprtf` |
| MOBI / AZW / AZW3 | Calibre `ebook-convert` (external app, not pip) | https://calibre-ebook.com/download |
| TXT / Markdown / reStructuredText / AsciiDoc | buil