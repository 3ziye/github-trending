# VMPrint

> [!IMPORTANT]
> **The VMPrint ecosystem is now modular.**  
> Core components have been decoupled into standalone repositories for independent development and distribution. You can find the specialized packages here:
> - **Draft2Final**: [github.com/cosmiciron/draft2final.git](https://github.com/cosmiciron/draft2final.git)
> - **Transmuters**: [github.com/cosmiciron/vmprint-transmuters.git](https://github.com/cosmiciron/vmprint-transmuters.git)
> - **Font Managers**: [github.com/cosmiciron/vmprint-font-managers.git](https://github.com/cosmiciron/vmprint-font-managers.git)
> - **Contexts**: [github.com/cosmiciron/vmprint-contexts.git](https://github.com/cosmiciron/vmprint-contexts.git)
> - **Contracts**: [github.com/cosmiciron/vmprint-contracts.git](https://github.com/cosmiciron/vmprint-contracts.git)

> **VMPrint now ships with a browser preview demo.**  
> Render real VMPrint documents in-browser with multilingual layout, pagination, and high-fidelity canvas preview.  
> The demo is a static, self-contained page you can open directly from a local folder, and its four core runtime bundles (shared fontkit + engine + web font manager + canvas context) weigh about **0.89 MiB** total minified.  
> [Open the canvas demo](https://cosmiciron.github.io/vmprint/examples/ast-to-canvas-webfonts/index.html) | [Browse all examples](https://cosmiciron.github.io/vmprint/examples/index.html) | [Quickstart](QUICKSTART.md)

You've been here before.

The HTML/CSS pipeline got you 80% of the way. Then the tables started fighting the page breaks. You needed the header to say "Page 1 of 12" — but you can't know it's 12 until you've finished laying out the whole document, and by then it's too late. You tried a second pass. The second pass introduced new problems. Someone suggested spinning up a headless Chromium. It worked, mostly, except on the edge runtime, and the Lambda with the tight memory limit, and that one machine where the fonts came out wrong.

The stack stopped making sense. You kept patching.

---

VMPrint exists for that moment. Here is what it actually produces:

**325 pages. 80,000 words. Markdown to publication-standard PDF. 2.32 seconds. Surface Pro 11 tablet, running on battery. No browser. No second pass. No auxiliary files.**

Not because VMPrint is faster at doing what those tools do. Because it does something different.

---

![VMPrint Specimen Blueprint - Actor-Based Spatial Simulation Engine](documents/readme-assets/blueprint-1.png)

> Every element arrived through collision — geometry negotiated in a deterministic sweep. Each block, glyph, and inline span is an actor reporting its own origin and extent.
> *All images in this README — including annotations, measurement guides, overlays, and script direction markers — are rendered entirely by VMPrint.*

---

## A Different Kind of Engine

VMPrint is a deterministic spatial simulation engine. Pages are bounded arenas. Document elements are autonomous actors with geometries. Layout is the process of reaching a stable world state.

There is no DOM underneath. No browser. No HTML. No CSS box model. The engine doesn't know what a browser is. It knows what a constraint field is. It knows what a collision is. It knows what a snapshot is, what a rollback is, and what it means for a world to settle.

This isn't a metaphor. It is the literal architecture.

A drop cap isn't a character. It's an actor with rules about how nearby text must respond. A table isn't a grid. It's a formation that holds together across boundaries, splits under constraint, and reconstructs itself on the other side. Derived regions are runtime participants too — observing, reacting, growing, and settling with the rest of the document world.

What this gives you is not just "better PDFs." It gives you a different substrate:

- a document runtime that behaves identically on a Cloudflare Worker, a laptop, a Lambda, and a phone
- a layout engine you can inspect, instrument, and participate in
- a pagination model that is not approximate — the same input produces the same output, always, everywhere
- a rendering output that is a flat, absolutely-positioned geometry list — no DOM, no layout re-traversal, just draw calls — and the right shape for GPU-accelerated rendering
- a foundation for tools the web made people forget were possible

Here is the part that makes the rest of this possible. When you hand the engine a document, each element — paragraph, table, heading, drop cap — gets compiled into a live actor. Think Lego Batman standing on the board. When Batman approaches a page boundary and doesn't fully fit, he doesn't get clipped and he doesn't get deferred. He disassembles into blocks. The blocks that fit commit to the current page. The remaining blocks reconstitute on the next page as the same Batman — same identity, same memory, same relationships — picking up exactly where he left off. A table that spans three pages is one actor that has split and reformed twice. A drop cap is a