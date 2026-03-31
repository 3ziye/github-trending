# gpdf

[![Go Reference](https://pkg.go.dev/badge/github.com/gpdf-dev/gpdf.svg)](https://pkg.go.dev/github.com/gpdf-dev/gpdf)
[![CI](https://github.com/gpdf-dev/gpdf/actions/workflows/check-code.yml/badge.svg)](https://github.com/gpdf-dev/gpdf/actions/workflows/check-code.yml)
![coverage](https://img.shields.io/badge/coverage-86.3%25-green)
[![Go Report Card](https://goreportcard.com/badge/github.com/gpdf-dev/gpdf)](https://goreportcard.com/report/github.com/gpdf-dev/gpdf)
[![Go Version](https://img.shields.io/badge/Go-%3E%3D1.22-blue)](https://go.dev/)
[![Website](https://img.shields.io/badge/Website-gpdf.dev-blue)](https://gpdf.dev/)

**English** | [日本語](README_ja.md) | [中文](README_zh.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Português](README_pt.md)

A pure Go, zero-dependency PDF generation library with a layered architecture and declarative builder API.

## Features

- **Zero dependencies** — only the Go standard library
- **Layered architecture** — low-level PDF primitives, document model, and high-level template API
- **12-column grid system** — Bootstrap-style responsive layout
- **TrueType font support** — embed custom fonts with subsetting
- **CJK ready** — full CJK text support from day one
- **Tables** — headers, column widths, striped rows, vertical alignment
- **Headers & Footers** — consistent across all pages with page numbers
- **Lists** — bulleted and numbered lists
- **QR codes** — pure Go QR code generation with error correction levels
- **Barcodes** — Code 128 barcode generation
- **Text decorations** — underline, strikethrough, letter spacing, text indent
- **Page numbers** — automatic page number and total page count
- **Go template integration** — generate PDFs from Go templates
- **Reusable components** — pre-built Invoice, Report, and Letter templates
- **JSON schema** — define documents entirely in JSON
- **Multiple units** — pt, mm, cm, in, em, %
- **Color spaces** — RGB, Grayscale, CMYK
- **Images** — JPEG and PNG embedding with fit options
- **Absolute positioning** — place elements at exact XY coordinates on the page
- **Existing PDF overlay** — open existing PDFs and add text, images, stamps on top
- **PDF merging** — combine multiple PDFs into one with page range selection
- **Document metadata** — title, author, subject, creator
- **Encryption** — AES-256 encryption (ISO 32000-2, Rev 6) with owner/user passwords and permissions
- **PDF/A** — PDF/A-1b and PDF/A-2b conformance with ICC profiles and XMP metadata
- **Digital signatures** — CMS/PKCS#7 signatures with RSA/ECDSA keys and optional RFC 3161 timestamping

## Benchmark

Comparison with [go-pdf/fpdf](https://github.com/go-pdf/fpdf), [signintech/gopdf](https://github.com/signintech/gopdf), and [maroto v2](https://github.com/johnfercher/maroto).
Median of 5 runs, 100 iterations each. Apple M1, Go 1.25.

**Execution time** (lower is better):

| Benchmark | gpdf | fpdf | gopdf | maroto v2 |
|---|--:|--:|--:|--:|
| Single page | **13 µs** | 132 µs | 423 µs | 237 µs |
| Table (4x10) | **108 µs** | 241 µs | 835 µs | 8.6 ms |
| 100 pages | **683 µs** | 11.7 ms | 8.6 ms | 19.8 ms |
| Complex document | **133 µs** | 254 µs | 997 µs | 10.4 ms |

**Memory usage** (lower is better):

| Benchmark | gpdf | fpdf | gopdf | maroto v2 |
|---|--:|--:|--:|--:|
| Single page | **16 KB** | 1.2 MB | 1.8 MB | 61 KB |
| Table (4x10) | **209 KB** | 1.3 MB | 1.9 MB | 1.6 MB |
| 100 pages | **909 KB** | 121 MB | 83 MB | 4.0 MB |
| Complex document | **246 KB** | 1.3 MB | 2.0 MB | 2.0 MB |

### Why is gpdf fast?

- **Single page** — Single-pass build→layout→render pipeline with no intermediate data structures. Concrete struct types throughout (no `interface{}` boxing), so the document tree is built with minimal heap allocations.
- **Table** — Cell content is written directly as PDF content stream commands via a reusable `strings.Builder` buffer. No per-cell object wrapping or repeated font lookups; the font is resolved once per document.
- **100 pages** — Layout scales linearly O(n). Overflow pagination passes remaining nodes by slice reference (no deep copies). The font is parsed once and shared across all pages.
- **Complex document** — Single-pass layout without re-measurement combines all the above. Font subsetting embeds only the glyphs actually used, and Flate compression is applied by default, keeping both memory and output size small.

Run benchmarks yourself:

```bash
cd _benchmark && go test -bench=. -benchmem -count=5
```

## Architecture

```
┌─────────────────────────────────────┐
│  gpdf (entry point)                 │
├─────────────────────────────────────┤
│  template  — Builder API, Grid      │  Layer 3
├─────────────────────────────────────┤
│  document  — Nodes, Style, Layout   │  Layer 2
├─────────────────────────────────────┤
│  pdf       — Writer, Fonts, Streams │  Layer 1
└─────────────────────────────────────┘
```

## Requirements

- Go 1.22 or later

## Install

```bash
go get github.com/gpdf-dev/gpdf
```

## Q