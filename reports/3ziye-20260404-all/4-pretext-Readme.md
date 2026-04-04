# Pretext

Pure JavaScript/TypeScript library for multiline text measurement & layout. Fast, accurate & supports all the languages you didn't even know about. Allows rendering to DOM, Canvas, SVG and soon, server-side.

Pretext side-steps the need for DOM measurements (e.g. `getBoundingClientRect`, `offsetHeight`), which trigger layout reflow, one of the most expensive operations in the browser. It implements its own text measurement logic, using the browsers' own font engine as ground truth (very AI-friendly iteration method).

## Installation

```sh
npm install @chenglou/pretext
```

## Demos

Clone the repo, run `bun install`, then `bun start`, and open the `/demos` in your browser (no trailing slash. Bun devserver bugs on those)
Alternatively, see them live at [chenglou.me/pretext](https://chenglou.me/pretext/). Some more at [somnai-dreams.github.io/pretext-demos](https://somnai-dreams.github.io/pretext-demos/)

## API

Pretext serves 2 use cases:

### 1. Measure a paragraph's height _without ever touching DOM_

```ts
import { prepare, layout } from '@chenglou/pretext'

const prepared = prepare('AGI 春天到了. بدأت الرحلة 🚀‎', '16px Inter')
const { height, lineCount } = layout(prepared, textWidth, 20) // pure arithmetics. No DOM layout & reflow!
```

`prepare()` does the one-time work: normalize whitespace, segment the text, apply glue rules, measure the segments with canvas, and return an opaque handle. `layout()` is the cheap hot path after that: pure arithmetic over cached widths. Do not rerun `prepare()` for the same text and configs; that'd defeat its precomputation. For example, on resize, only rerun `layout()`.

If you want textarea-like text where ordinary spaces, `\t` tabs, and `\n` hard breaks stay visible, pass `{ whiteSpace: 'pre-wrap' }` to `prepare()`:

```ts
const prepared = prepare(textareaValue, '16px Inter', { whiteSpace: 'pre-wrap' })
const { height } = layout(prepared, textareaWidth, 20)
```

On the current checked-in benchmark snapshot:
- `prepare()` is about `19ms` for the shared 500-text batch
- `layout()` is about `0.09ms` for that same batch

We support all the languages you can imagine, including emojis and mixed-bidi, and caters to specific browser quirks

The returned height is the crucial last piece for unlocking web UI's:
- proper virtualization/occlusion without guesstimates & caching
- fancy userland layouts: masonry, JS-driven flexbox-like implementations, nudging a few layout values without CSS hacks (imagine that), etc.
- _development time_ verification (especially now with AI) that labels on e.g. buttons don't overflow to the next line, browser-free
- prevent layout shift when new text loads and you wanna re-anchor the scroll position

### 2. Lay out the paragraph lines manually yourself

Switch out `prepare` with `prepareWithSegments`, then:

- `layoutWithLines()` gives you all the lines at a fixed width:

```ts
import { prepareWithSegments, layoutWithLines } from '@chenglou/pretext'

const prepared = prepareWithSegments('AGI 春天到了. بدأت الرحلة 🚀', '18px "Helvetica Neue"')
const { lines } = layoutWithLines(prepared, 320, 26) // 320px max width, 26px line height
for (let i = 0; i < lines.length; i++) ctx.fillText(lines[i].text, 0, i * 26)
```

- `walkLineRanges()` gives you line widths and cursors without building the text strings:

```ts
let maxW = 0
walkLineRanges(prepared, 320, line => { if (line.width > maxW) maxW = line.width })
// maxW is now the widest line — the tightest container width that still fits the text! This multiline "shrink wrap" has been missing from web
```

- `layoutNextLine()` lets you route text one row at a time when width changes as you go:

```ts
let cursor = { segmentIndex: 0, graphemeIndex: 0 }
let y = 0

// Flow text around a floated image: lines beside the image are narrower
while (true) {
  const width = y < image.bottom ? columnWidth - image.width : columnWidth
  const line = layoutNextLine(prepared, cursor, width)
  if (line === null) break
  ctx.fillText(line.text, 0, y)
  cursor = line.end
  y += 26
}
```

This usage allows rendering to canvas, SVG, WebGL and (eventually) server-side.

If your manual layout needs a small helper for mixed inline runs, atomic pills, and browser-like boundary whitespace collapse, there is an experimental alpha sidecar at `@chenglou/pretext/inline-flow`. It stays inline-only and `white-space: normal`-only on purpose:

```ts
import { prepareInlineFlow, walkInlineFlowLines } from '@chenglou/pretext/inline-flow'

const prepared = prepareInlineFlow([
  { text: 'Ship ', font: '500 17px Inter' },
  { text: '@maya', font: '700 12px Inter', break: 'never', extraWidth: 22 },
  { text: "'s rich-note", font: '500 17px Inter' },
])

walkInlineFlowLines(prepared, 320, line => {
  // each fragment keeps its source item index, text slice, gapBefore, and cursors
})
```

It is intentionally narrow:
- raw text in, including boundary spaces
- caller-owned `extraWidth` for padding/border chrome
- `break: 'never'` for atomic item