# geolibre-rust

[![npm version](https://img.shields.io/npm/v/geolibre-wasm.svg)](https://www.npmjs.com/package/geolibre-wasm)
[![PyPI version](https://img.shields.io/pypi/v/geolibre-wasm.svg)](https://pypi.org/project/geolibre-wasm/)
[![npm downloads](https://img.shields.io/npm/dm/geolibre-wasm.svg)](https://www.npmjs.com/package/geolibre-wasm)
[![CI](https://github.com/opengeos/geolibre-rust/actions/workflows/ci.yml/badge.svg)](https://github.com/opengeos/geolibre-rust/actions/workflows/ci.yml)
[![license](https://img.shields.io/npm/l/geolibre-wasm.svg)](https://github.com/opengeos/geolibre-rust#license)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/opengeos/geolibre-rust/blob/main/examples/geolibre_wasm.ipynb)

A pure-Rust geospatial toolkit for [GeoLibre](https://github.com/opengeos/GeoLibre),
built on [`opengeos/whitebox-wasm`](https://github.com/opengeos/whitebox-wasm)
(the WASM-ready fork of
[`whitebox_next_gen`](https://github.com/jblindsay/whitebox_next_gen)) and
compiled to WebAssembly. It is a **superset of `whitebox-wasm`**: everything that
package offers, plus new GeoLibre-authored tools.

The published npm package (`geolibre-wasm`) ships two layers:

- **Browser library** (`.` export, `wasm-bindgen`) -- typed in-memory APIs for
  GeoTIFF/COG read+write, projections, vector, LiDAR, and topology
  (`GeoTiffReader`, `CogBuilder`, `CogStream`, ...). Same surface as
  `whitebox-wasm`.
- **Tool runner** (`./tools` export, WASI) -- the whitebox tool registry **plus
  GeoLibre's own tools**, run over an in-memory `/work` filesystem via
  [`@bjorn3/browser_wasi_shim`](https://github.com/bjorn3/browser_wasi_shim).

No server, no GDAL, no native install. Use it from JavaScript (npm
`geolibre-wasm`) or Python (PyPI `geolibre-wasm`). New tools live in the
`geolibre-tools` crate and are registered alongside whitebox's, so GeoLibre sees
them through the same interface as the built-ins.

## Try it in the browser

`demo/index.html` is a self-contained page that loads every tool manifest,
renders a parameter form for whichever tool you pick, and runs it on a sample DEM
(or your own GeoTIFF) entirely in the browser via the WASI runner.

```bash
./build.sh          # once, to produce npm/geolibre-cli.wasm and npm/tools.mjs
./demo/serve.sh     # serve on http://localhost:8000 (pass a port to override)
```

Open the printed URL, filter the tool list, fill in the auto-generated form, and
click **Run** to see the exit code, stdout, output files, and a download link.
`serve.sh` stages the runtime (`npm/tools.mjs`, `npm/geolibre-cli.wasm`) and the
sample raster (`examples/sample.tif`) next to the page in a temp directory, so the
repo's `demo/` stays clean; Ctrl-C stops the server and cleans up.

### Self-host with Docker

The same demo ships as a container image so you can host it yourself. The image
is a static site (nginx) — every tool still runs in the visitor's browser, so
there's no server-side compute, GDAL, or database.

Pull the published image with Docker Compose:

```bash
docker compose up -d        # serves on http://localhost:8080
```

Or build and run it straight from source (needs only Docker — the Rust/WASM
toolchain lives inside the build):

```bash
docker build -t geolibre-rust .
docker run --rm -p 8080:80 geolibre-rust
```

Images are published to `ghcr.io/opengeos/geolibre-rust` on each release (and on
`v*` tags); `:latest` tracks the most recent release. To build from source via
Compose instead of pulling, uncomment `build: .` in `docker-compose.yml`.

## Architecture

```
crates/geolibre-wasm   wasm-bindgen browser library  -> geolibre_wasm{.js,_bg.wasm,.d.ts}  (npm ".")
crates/geolibre-cli    WASI tool runner              -> geolibre-cli.wasm + tools.mjs       (npm "./tools")
crates/geolibre-tools  new Tool impls (raster_normalize, ...), registered by geolibre-cli

JS (browser/Node)                WASI binary (geolibre-cli.wasm)
-----------------                --------------------------------
tools.mjs                        crates/geolibre-cli (main.rs)
  write inputs -> /work    -->     argv -> ToolArgs (JSON)
  argv ["slope", "--..."]  -->     ToolRegistry::run
  read new files from /work <--      register_default_tools (whitebox)
                                     + geolibre_tools (new tools)
                                   tool writes via std::fs to /work
```

## GeoLibre-authored tools

In addition to the whitebox suite, `geolibre-tools` ships cloud-native I/O and
rendering tools that the whitebox suite lacks (all pure-Rust, running in WASM):

| Tool id | What it does |
|---|---|
| `reproject_raster` | Reproject (warp) a raster into a target EPSG CRS, with selectable resampling. |
| `render_raster_png` | Render a raster band to a PNG through a colormap (viridis/magma/turbo/terrain/grayscale); no-data becomes transparent. |
| `raster_to_tiles` | Slice a raster into a Web Mercator (EPSG:3857) XYZ PNG tile pyramid for