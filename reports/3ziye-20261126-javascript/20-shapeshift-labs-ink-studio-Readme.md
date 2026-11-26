# @shapeshift-labs/ink-studio

A JavaScript toolkit for sculpting signed-distance solids, baking them into pixel-art Gaussian splats, and making them move, react, break, grow and remember what happened to them. Use it from Node, drive it through the `ink-studio` command, or embed the source bundle in an Inkwell or browser application.

The package includes geometry, materials, lighting, animation, character controls, particles, physics, procedural generation, and retained authoring. Write scenes in JavaScript or JSON, render images through the CPU-based Node and CLI tools, or draw into a canvas with the default WebGL 2 browser renderer. Browser hosts supply the editor UI and advance the scene.

## Contents

- [Install and run](#install-and-run)
- [First sculpted scene](#first-sculpted-scene)
- [Using the library in Node](#using-the-library-in-node)
- [Scene lifecycle and splat data](#scene-lifecycle-and-splat-data)
- [Geometry and materials](#geometry-and-materials)
- [Scenes as JSON](#scenes-as-json)
- [Animation and puppets](#animation-and-puppets)
- [Particles and interaction](#particles-and-interaction)
- [Physics and persistent effects](#physics-and-persistent-effects)
- [Importing meshes](#importing-meshes)
- [Exporting GLB models](#exporting-glb-models)
- [Importing depth maps](#importing-depth-maps)
- [Procedural worlds](#procedural-worlds)
- [Retained authoring](#retained-authoring)
- [Editable 3D drawing](#editable-3d-drawing)
- [Headless world simulation](docs/headless-worlds.md)
- [Playable and editable Inkwell Rebirth scenes](examples/inkwell-rebirth/README.md)
- [Searchable effect recipes](docs/effect-recipes.md)
- [Shared PBR materials](docs/pbr-materials.md)
- [Material-aware secondary emission](docs/secondary-emission.md)
- [Material pickup and transfer](docs/material-response.md#pick-up-and-transfer-material)
- [Editable starter recipes](examples/starter-recipes/README.md)
- [Rendering and command reference](#rendering-and-command-reference)
- [Searchable public reference](docs/reference/index.md)
- [View-dependent surface materials](#view-dependent-surface-materials)
- [Projected and procedural effects](#projected-and-procedural-effects)
- [Reflections, ripples and atmosphere](#reflections-ripples-and-atmosphere)
- [Embedding and custom scene collections](#embedding-and-custom-scene-collections)
- [Browser renderer](#browser-renderer)
- [Live show control](#live-show-control)
- [CLI patch tooling](#cli-patch-tooling)
- [Story documents](docs/story-documents.md)
- [Event-driven visual effects](docs/event-visual-effects.md)
- [Persistent visual consequences](docs/visual-consequences.md)
- [Adaptive story audio](docs/adaptive-story-audio.md)
- [Directional captions from playback](docs/directional-captions.md)
- [Seeded sound recipes](docs/seeded-sound-recipes.md)
- [Editable story picture and audio](docs/story-editorial-handoff.md)
- [Configurable story presentation packs](docs/story-presentation-pack.md)
- [Interactive story installation inputs](docs/story-installation-inputs.md)
- [Story-aware rehearsal reports](docs/story-rehearsal.md)
- [Search for hard-to-stage routes](docs/staging-route-search.md)
- [Blind audiovisual review](docs/blind-av-review.md)
- [Video codec round-trip approval](docs/video-round-trip.md)
- [Flash and flicker review](docs/flash-flicker-review.md)
- [Beat-level live performance captures](docs/beat-performance-captures.md)
- [Ambisonic ambience export](docs/ambisonic-ambience.md)
- [Compressed-audio round-trip approval](docs/audio-round-trip.md)
- [Playback translation through measured devices](docs/playback-translation.md)
- [Display and speaker latency calibration](docs/output-latency.md)
- [WebGPU graphs and Gaussian splat import](#webgpu-graphs-and-gaussian-splat-import)
- [Screen transitions](#screen-transitions)
- [Module reference](#module-reference)
- [Validation and development](#validation-and-development)

## Install and run

Requires **Node 18 or later**. There are no declared runtime dependencies. The package is available from GitHub.

From a checkout:

```sh
node cli/ink-studio.js help
node cli/ink-studio.js scenes
node cli/ink-studio.js render watcher --t 2.6
node cli/ink-studio.js render watcher --t 2.6 --colored
npm test
```

Install from GitHub:

```sh
npm install github:siliconjungle/shapeshift-labs-ink-studio
npx ink-studio help
```

To install a local checkout into another project:

```sh
npm install /absolute/path/to/ink-studio
npx ink-studio help
npx ink-studio render watcher --colored
```

The installed package is named `@shapeshift-labs/ink-studio`, and its executable is `ink-studio`. The `private` setting prevents accidental registry publication.

Generated pictures normally go into `studio/out/`. Image baselines go into `studio/snaps/`. Use `--out file.png` for an explicit output path, or configure the directories with `ink-studio.config.js`.

The examples below use `npx ink-studio` from a consuming project. In this checkout, replace that