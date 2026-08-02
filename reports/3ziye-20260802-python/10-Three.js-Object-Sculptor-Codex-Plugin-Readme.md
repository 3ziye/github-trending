# Three.js Object Sculptor

Turn the object in an attached image into a quality-gated, animation-ready procedural Three.js model built entirely with code.

Three.js Object Sculptor is a Codex plugin for rebuilding the visible object in a user-provided attachment image as a code-only Three.js model. It does not try to do photogrammetry, download an art pack, or extract a perfect mesh from one image. Instead, it guides Codex through a sculpting workflow: validate the image, describe the object precisely, decompose it into geometry and material systems, build from blockout to detail, wire an animation-friendly hierarchy, then compare the browser render against the original reference.

## Demo

### Tower Ship

[Open the live tower ship demo](https://3dship.harrysoftware.com)

![Procedural Three.js tower ship demo generated from an attached reference image](assets/tower-ship-demo.png)

This tower ship study shows the intended output shape: a browser-rendered, code-sculpted Three.js object rebuilt from an attached reference image, with procedural geometry, articulated parts, material work, and interactive controls.

### Ancient Autumn Tree

[Open the live ancient autumn tree demo](https://tree.harrysoftware.com/)

![Procedural Three.js ancient autumn tree reconstructed from an attached reference image](assets/ancient-autumn-tree-demo.png)

This botanical study reconstructs a complex ancient tree with procedural curves, deterministic branching, layered bark materials, dense autumn foliage, and an animation-ready hierarchy.

## At A Glance

- **Name:** Three.js Object Sculptor
- **Category:** Codex plugin for image-to-procedural-3D workflows
- **Input:** an attached object image, reference screenshot, or local image path
- **Output:** a code-only procedural Three.js object factory, backed by an `ObjectSculptSpec`
- **Primary goal:** recreate the target object's silhouette, component structure, materials, lighting response, and action-ready hierarchy in browser-friendly Three.js code
- **Best for:** animation-ready real-time props, game objects, scene dressing, destructible objects, product-style objects, botanical objects, mechanical parts, and stylized reference reconstructions
- **Not for:** photogrammetry, exact mesh extraction, scanned assets, downloaded art packs, or guaranteed production-perfect geometry from one image

## What It Does

- Validates whether an image is suitable for procedural 3D reconstruction.
- Integrates the pre-spec complexity assessment into the main `ObjectSculptSpec` before code generation.
- Writes an `ObjectSculptSpec` with component hierarchy, materials, lighting, pivots, sockets, animation anchors, destruction anchors, and quality targets.
- New specs use a v4 root manifest plus independently authored module specs; the highest-risk ready module is validated first and accepted modules are reused by content/interface hash.
- New visual modules require a global surface-topology decision first, so continuous forms, real assemblies, fitted shells, relief, fibers, and material-only detail are not confused with arbitrary mesh count.
- Supports compound objects through nested `assembly` groups plus geometry-bearing `part` nodes.
- Uses one geometry registry for validation and generation, including tube, lathe, extrude, curve sweep, section lofts, fitted shells, branch networks, masked surface scatter, modifiers, and bounded instancing; unsupported geometry is rejected instead of becoming a box silently.
- Supports bounded `sculpted-surface` fields that fuse irregular masses and embedded ridges/creases into one connectivity-checked welded mesh.
- Adds opt-in static approximations for organic bodies, fitted cloth/layers, trees/roots/horns, hair/fur, smooth merged forms, glass/liquid, and soft volumes through bounded special geometry and material profiles; physics simulation and raymarched volumes remain out of scope.
- Uses an adaptive pipeline: blockout, form, and lookdev always run; structure, interaction, and optimization run only when the object's complexity or intended use requires them.
- Provides one `scripts/sculpt.py` command surface while keeping the older individual scripts compatible.
- Generates a code-only Three.js factory skeleton from the current unlocked sculpt pass.
- Designs the generated object as an action-ready hierarchy, so later animation, transformation, physics, or destruction requests have real pivots and attachment points to use.
- Packages reference/render screenshots into one comparison sheet for AI vision review.
- Adds diagnostic-only silhouette IoU, framing deltas, contour overlays, and camera-first correction hints; AI vision remains the acceptance authority.
- Records self-correction reviews with overall, layer, and critical feature scores.
- Supports reference-derived procedural PBR evidence: albedo, roughness estimate, height, normal, and AO maps.
- Emits bounded rounded-box edge treatment and supported local seam/ridge/stitch/button/rivet/decal geometry i