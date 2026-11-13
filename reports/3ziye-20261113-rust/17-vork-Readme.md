<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/readme-header-dark.png">
  <img alt="vork by Voyager" src="docs/images/readme-header-light.png" width="800">
</picture>

<p>
  <a href="https://discord.com/invite/voyagerai"><img alt="Discord" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fdiscord.com%2Fapi%2Fv10%2Finvites%2Fvoyagerai%3Fwith_counts%3Dtrue&query=%24.approximate_presence_count&suffix=%20online&label=Discord&logo=discord&logoColor=white&color=5865F2"></a>
  <a href="https://www.npmjs.com/package/@voyager-so/vork"><img alt="npm" src="https://img.shields.io/npm/v/@voyager-so/vork?label=npm&color=black"></a>
  <a href="https://pypi.org/project/vork/"><img alt="PyPI" src="https://img.shields.io/pypi/v/vork?label=PyPI&color=black"></a>
  <a href="https://x.com/ravisparikh"><img alt="Follow @ravisparikh on X" src="https://img.shields.io/badge/X-@ravisparikh-black?logo=x&logoColor=white"></a>
</p>

**vork is a 3D and VFX engine built for AI agents.**

Agents write the whole scene as code, including their own shaders, materials,
cameras and physics, and vork renders it on the GPU. The core API fits in about
2,500 tokens.

https://github.com/user-attachments/assets/03cfa020-be40-483a-89af-1ef77467b7a0

**One million birds, each on its own path.** 192 frames at 1080p rendered in
97 seconds on a single NVIDIA L4. Blender EEVEE at the same sample count is
projected at 13–18 minutes. [How we measured](#million-birds-measured-movies-projected-blender-times) ·
[how it's made](examples/murmuration/) · [credits](examples/murmuration/CREDITS)

- **Built for agents:** a small API that agents can extend with their own GPU programs.
- **Fast:** 1.1–2.3× faster than EEVEE on default stills and movies, and about 8–11× on the bird flock.
  [Speed, with the qualifications](#speed-with-the-qualifications).
- **Native GPU engine:** written in Rust and Slang, runs on Vulkan and Metal (Linux, Windows, macOS).
- **No GPU needed:** render on Voyager's cloud GPUs with [vork cloud](https://voyager.so/vork/cloud).

## Paste this to your agent

[Install vork](#install), then paste:

> Run `vork init my-shot`, read `vork help`, render a preview and inspect the image.
> Refine the camera and lighting before rendering at final quality. Read the
> relevant help topic when you need a feature the first page doesn't explain.

vork is written in Rust and Slang, with GPU rendering through Vulkan and Metal.
An agent writes a scene,
renders it, looks at the result and revises the code. There is no editor to drive.

Most creative tools expose controls that a person can operate. An agent can also
write a shader in the middle of a shot. vork gives it geometry, ray queries and
GPU execution, then lets scene programs define materials, cameras, light
propagation, simulation and compositing. Ordinary shots need only scene data;
the programming hooks are there when the shot needs something unusual.

Source-available and free during the research preview.

## Start here

After [installing vork](#install), create a working project:

```sh
vork init my-shot
cd my-shot
vork render scene.json --out render.png
vork help
```

Open `render.png`, change a colour or camera position in `scene.json`, and render
again. The starter uses only bundled sphere, box and grid primitives: no downloads,
no GPU needed to initialize. Use `vork init my-shot --language typescript` or
`--language python` for editable `scene.ts` or `scene.py` alongside the ready-to-render
JSON. The generated README explains regeneration and SDK requirements. Existing
files are never overwritten. The default `std/final` profile is warmed by setup; use `--profile std/draft` for quicker previews.

## What you can make

The examples include code, preparation commands and credits. Large downloaded
assets and footage stay outside Git; the recipes fetch them or accept a local path.
The images here are stills from these shots. Keep each credit with its image.

### [Million birds](examples/murmuration/)

![A ribbon of starlings crossing the low sun above a lagoon](docs/images/birds-sun-ribbon.jpg)

| | |
|---|---|
| ![A foreground bird above the flock at dusk](docs/images/birds-skim.jpg) | ![The flock curving over still water, seen from above](docs/images/birds-lagoon.jpg) |

A million simulated agents steered by Slang compute programs, with a camera skimming
through the flock. The camera and nine foreground birds are authored; the simulated
million do not flap. The bird stills above come from the measured four-sample,
denoised skim and reveal movies.

Credit: based on ["Crow"](https://sketchfab.com/3d-models/crow-d5a9b0df4da3493688b63ce42c8a83e2)
by Alexei Ostapenko, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Changes: sampled flight pose, reduced distant mesh, rescaled, articulated flight
wings, extracted wings for the starling body, resized textures.
[All bird and environment credits](examples/murmuration/CREDITS).

### [Cyber car](https:/