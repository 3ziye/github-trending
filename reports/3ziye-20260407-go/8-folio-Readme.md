# Folio

A modern PDF library for Go — layout engine, HTML to PDF, redaction,
forms, digital signatures, barcodes, page import, and PDF/A compliance.

[![Go Reference](https://pkg.go.dev/badge/github.com/carlos7ags/folio.svg)](https://pkg.go.dev/github.com/carlos7ags/folio)
[![CI](https://github.com/carlos7ags/folio/actions/workflows/ci.yml/badge.svg)](https://github.com/carlos7ags/folio/actions)
[![Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

**[Try it live in your browser](https://playground.foliopdf.dev/)**

![Folio Playground](assets/playground.png)

---

## Install

```bash
go get github.com/carlos7ags/folio
```

Requires Go 1.25+. Two external dependencies: `golang.org/x/image` and `golang.org/x/net`.

---

## Quick Start

```go
package main

import (
    "github.com/carlos7ags/folio/document"
    "github.com/carlos7ags/folio/font"
    "github.com/carlos7ags/folio/layout"
)

func main() {
    doc := document.NewDocument(document.PageSizeA4)
    doc.Info.Title = "Hello World"
    doc.SetAutoBookmarks(true)

    doc.Add(layout.NewHeading("Hello, Folio!", layout.H1))
    doc.Add(layout.NewParagraph(
        "Generated with Folio — the modern PDF library for Go.",
        font.Helvetica, 12,
    ))

    doc.Save("hello.pdf")
}
```

---

## HTML to PDF

The fastest way to generate PDFs — paste any HTML template and get a PDF.
No Chrome, no Puppeteer, no server required.

```go
import (
    "github.com/carlos7ags/folio/document"
    "github.com/carlos7ags/folio/html"
)

doc := document.NewDocument(document.PageSizeLetter)
elems, _ := html.Convert(`
    <h1>Invoice #1042</h1>
    <p>Bill to: <strong>Acme Corp</strong></p>
    <table border="1">
        <tr><th>Item</th><th>Amount</th></tr>
        <tr><td>Consulting</td><td>$1,200</td></tr>
    </table>
`, nil)
for _, e := range elems {
    doc.Add(e)
}
doc.Save("invoice.pdf")
```

Supports 40+ HTML elements, inline and `<style>` block CSS, flexbox, CSS grid,
SVG, named/hex/rgb colors, `@page` rules, and tables with colspan.

**[Try HTML to PDF live in your browser](https://playground.foliopdf.dev/)**

---

## Layout Engine

Folio uses a plan-based layout engine — layout is a pure function with no
mutation during rendering. Elements can be laid out multiple times safely,
which makes page break splitting clean and predictable.

```go
doc := document.NewDocument(document.PageSizeLetter)
doc.Info.Title = "Quarterly Report"
doc.Info.Author = "Finance Team"
doc.SetAutoBookmarks(true)

doc.Add(layout.NewHeading("Q3 Revenue Report", layout.H1))

doc.Add(layout.NewParagraph("Revenue grew 23% year over year.",
    font.Helvetica, 12).
    SetAlign(layout.AlignJustify).
    SetSpaceAfter(10))

tbl := layout.NewTable().SetAutoColumnWidths()
h := tbl.AddHeaderRow()
h.AddCell("Product", font.HelveticaBold, 10)
h.AddCell("Units", font.HelveticaBold, 10)
h.AddCell("Revenue", font.HelveticaBold, 10)

r := tbl.AddRow()
r.AddCell("Widget A", font.Helvetica, 10)
r.AddCell("1,200", font.Helvetica, 10)
r.AddCell("$48,000", font.Helvetica, 10)
doc.Add(tbl)

doc.Save("report.pdf")
```

### Layout Elements

| Element | Description |
|---|---|
| `Paragraph` | Word-wrapped text with alignment, leading, orphans/widows |
| `Heading` | H1-H6 with preset sizes, spacing, and auto-bookmarks |
| `Table` | Borders, colspan, rowspan, header repetition, auto-column widths |
| `List` | Bullet, numbered, Roman, alpha, nested |
| `Div` | Container with borders, background, padding |
| `Flex` | Flexbox layout with direction, wrap, alignment |
| `Image` | JPEG, PNG, TIFF with aspect ratio preservation |
| `LineSeparator` | Horizontal rule (solid, dashed, dotted) |
| `TabbedLine` | Tab stops with dot leaders (for TOCs) |
| `Link` | Clickable text with URL or internal destination |
| `Float` | Left/right floating with text wrap |
| `Columns` | Multi-column layout with automatic balancing |
| `AreaBreak` | Explicit page break |
| `BarcodeElement` | Code128, QR, EAN-13 inline in layout |

---

## Styled Text

```go
p := layout.NewStyledParagraph(
    layout.NewRun("Normal text ", font.Helvetica, 12),
    layout.NewRun("bold ", font.HelveticaBold, 12),
    layout.NewRun("colored and underlined", font.Helvetica, 12).
        WithColor(layout.ColorRed).
        WithUnderline(),
)
doc.Add(p)
```

---

## Tables

```go
tbl := layout.NewTable().SetAutoColumnWidths()
// Or explicit widths:
tbl.SetColumnUnitWidths([]layout.UnitValue{
    layout.Pct(30), layout.Pct(70),
})

// Header rows repeat automatically on page breaks
h := tbl.AddHeaderRow()
h.AddCell("Name", font.HelveticaBold, 10)
h.AddCell("Value", font.HelveticaBold, 10)

r := tbl.AddRow()
cell := r.AddCell("Styled cell", font.Helvetica, 10)
cell.SetBorders(layout.AllBorders(layout.DashedBorder(1, layout.ColorBlue)))
cell.SetBackground(layout.ColorLightGray)
cell.SetVAlign(layout.VAlignMiddle)
```

---

## Barcodes

```go
import "github.com/carlos7ags/folio/barcode"

qr, _ := barcode.NewQR("https://example.com")
d