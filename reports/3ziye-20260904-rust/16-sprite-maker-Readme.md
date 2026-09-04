<p align="center">
  <img src="static/brand/sprite-studio-lockup.svg" alt="Sprite Studio" width="560">
</p>

<p align="center">
  A local-first AI workbench for creating, animating, testing, organizing, and exporting 2D game art.
</p>

<p align="center">
  <strong>macOS · Windows · Linux</strong>
</p>

<p align="center">
  <img src="docs/media/sprite-studio-v0.2-showcase.gif" alt="Sprite Studio creating a rabbit hop, dragon flight, centipede crawl, and coordinated nature pack" width="800">
</p>

## From a prompt to a usable game asset

Generating one attractive image is easy. A production asset also needs a stable identity, clean transparency, readable scale, consistent palette, useful file structure, and—when it moves—a mechanically complete loop.

Sprite Studio keeps that work in one desktop workspace. Describe an asset in chat, attach or paste references, inspect the result at pixel scale, generate a high-frame-count AI animation with strict identity and neighbor references, test the loop, and export a sheet without losing the source files or the conversation that produced them.

The project is open source, local first, and built with Tauri, Svelte, Rust, SQLite, and an installed Codex CLI. It does not target Android or iOS.

## The workflow

1. **Generate in chat.** Use plain language or a slash command. Every chat keeps its own style, references, quality, dimensions, frame policy, FPS, model, and reasoning settings.
2. **Review the real output.** Static images open in the full-size sprite viewer. Related animation frames appear as one playable sprite set instead of flooding the library.
3. **Describe natural movement.** “Animate this” brings the source asset back to chat and asks how it should move, with suggestions based on visible anatomy.
4. **Plan once, generate sequentially.** AI plans the complete motion, then generates one frame at a time using the source identity and neighboring accepted frames. The default 24–48 frame range favors smooth motion; users can lower it at any time.
5. **Rig it with points when you want determinism.** The Rig editor places named joint points and capsule bones on any sprite — auto-placed from an anatomy template, suggested by the AI (`/rig` or “Ask AI”), or dragged by hand. The native Rust engine derives every bone's pixels from the capsules, solves planted contacts with two-bone IK, and renders byte-identical frames with no image generation at all.
6. **Test and export.** Scrub, retime, zoom, inspect warnings, test the loop in the playground, and export a PNG sheet plus metadata.

## Rigging in Rust

The rig engine is written natively in Rust and runs instantly on the local machine:

- **Points over masks.** A rig is a set of named points (`joint`, `anchor`, `contact`, `pivot`) and capsule bones between them. The engine auto-claims every opaque pixel inside the closest capsule and assigns leftovers to the nearest bone, so nobody hand-paints masks.
- **AI-suggested points.** `Ask AI` sends the sprite to your agent CLI and gets back a `rig-suggestion` JSON block of points, bones, and optional pose frames, with confidence values. `/rig` in chat does the same and the captured rig appears in the Rig tab automatically.
- **Deterministic rendering.** Per-frame bone rotations, scales, offsets, root motion, holds, and z-layering compose through parent chains and render with nearest-neighbor inverse mapping — identical inputs always produce identical PNG bytes.
- **Planted contacts.** Feet and hands stay pinned in place while the chain bends around them using analytic two-bone IK, so walk cycles do not slide.
- **Full pipeline.** Rendered frames land in `assets/<category>/`, become normal assets, form an animation with quality analysis, and flow into sheets, the playground, and exports like any other sprite.

## Motion that understands the subject

### Rabbit: a real hop cycle

The rabbit does not simply slide upward. Its eight-pose loop compresses the haunch, pushes from the hind leg, tucks in the air, reaches with the forefeet, absorbs contact, and recovers into the opening stance. The motion planner estimates a physical envelope unless the user supplies exact speed, height, or scale.

<p align="center">
  <img src="docs/media/rabbit-hop.gif" alt="Eight-frame anatomy-aware rabbit hop generated and polished in Sprite Studio" width="960">
</p>

### Dragon: one identity through a full wingbeat

This twelve-frame loop keeps the same dragon while the near and far wings move through a forceful downstroke, folded recovery, body lift, delayed legs, and tail counterbalance.

<p align="center">
  <img src="docs/media/dragon-flight.gif" alt="Twelve-frame orange dragon flight cycle generated in Sprite Studio" width="960">
</p>

### Centipede: connected segmented motion

Creature harnesses account for morphology that a human walk template cannot handle. The centipede uses a phase-shifted head-to-tail body wave, alternating leg banks, a stable ground line, and twelve distinct crawl frame