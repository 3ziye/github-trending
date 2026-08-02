<p align="center">
  <img src="https://raw.githubusercontent.com/reflex-dev/xy/main/spec/assets/xy-sdf-binned-scatter.png" alt="XY-shaped probability field shown as a binned scatter chart." width="521">
</p>

<p align="center">
  <a href="https://github.com/reflex-dev/xy/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/reflex-dev/xy/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://app.codspeed.io/reflex-dev/xy?utm_source=badge"><img alt="CodSpeed" src="https://img.shields.io/endpoint?url=https://codspeed.io/badge.json"></a>
  <a href="pyproject.toml"><img alt="Python 3.11+" src="https://img.shields.io/badge/python-3.11%2B-3776ab?logo=python&logoColor=white"></a>
  <a href="https://reflex.dev/docs/xy/" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/docs-reflex.dev-blue" alt="Docs" /></a>
  <a href="https://mybinder.org/v2/gh/reflex-dev/xy/main?urlpath=lab/tree/examples" target="_blank" rel="noopener noreferrer"><img src="https://mybinder.org/badge_logo.svg" alt="Launch the examples on Binder" /></a>
</p>

XY is an extremely fast, interactive, customizable Python charting library for
the web, notebooks, and static exports.

Charts are composed declaratively or through matplotlib conventions. You can
fully customize them with Python, CSS, or Tailwind.

With small charts, every point is sent to the browser. For large charts, the
Rust core computes only what the screen needs to display, based on its
resolution. Pan, zoom, hover, and selection can show full details by running the
same process for the new range, and a selection returns the original rows.

With XY we rendered the entirety of OpenStreetMap — a **10,000,000,000 point** dataset. [See the example →](https://github.com/reflex-dev/xy/tree/main/examples/osm)

> [!IMPORTANT]
> **XY is in alpha** and is receiving frequent enhancements.
> ⭐️ Star the repo to follow the progress.

## Is XY right for me?

XY is for Python users who want one flexible charting library for everything
from everyday plots to custom application visuals and large datasets. Build a
chart once, then use it in notebooks and web apps or export it as HTML, PNG,
SVG, or PDF.

## Installation

```bash
pip install xy

# or, with uv
uv add xy
```

## Getting started

A chart is a container plus the marks inside it. Any sequence works; NumPy is
optional.

```python
import xy

chart = xy.line_chart(xy.line([1, 2, 3, 4, 5], [120, 180, 165, 240, 310]))
# chart.to_html("chart.html")
# chart.to_png("chart.png")
# chart.to_svg("chart.svg")
chart  # notebooks render it
```

The same API scales to a hundred million points as a density surface:

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/reflex-dev/xy/main/spec/assets/xy-density-100m-dark.gif">
    <img src="https://raw.githubusercontent.com/reflex-dev/xy/main/spec/assets/xy-density-100m-light.gif" alt="A hundred-million-point spiral rendered as a density surface, then zoomed until the surface resolves into individual points." width="780">
  </picture>
</p>

```python
import numpy as np

import xy

rng = np.random.default_rng(7)
n = 100_000_000

r = 6.0 * rng.beta(1.2, 3.0, n)
theta = 2.9 * np.log1p(r) + rng.integers(0, 4, n) * (np.pi / 2) + rng.normal(0, 0.045 + 0.016 * r, n)

chart = xy.scatter_chart(
    xy.scatter(
        r * np.cos(theta),
        r * np.sin(theta),
        color=np.exp(-r / 2.2),
        colormap="magma_r",
        density=True,
        opacity=0.85,
        # Grow and solidify markers once a view drills through to real rows.
        size=2.5,
        zoom_size_factor=2.6,
        zoom_opacity=0.95,
    ),
    xy.theme(
        background="#ffffff", plot_background="#ffffff", grid_color="#e6e6e1",
        axis_color="#c3c2b7", text_color="#0b0b0b",
    ),
    title="100 million points",
)
chart
```

### Coming from matplotlib

For common pyplot workflows, change the import and keep the plotting code:

```python
import numpy as np
import xy.pyplot as plt

x = np.linspace(0, 10, 200)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), "r--", label="signal")
ax.legend()
plt.show()
```

See the [compatibility guide](https://github.com/reflex-dev/xy/blob/main/spec/matplotlib/compat.md); not all charts and
functionality are supported yet.

## Customize every layer

Use Python to control the chart, from marks and axes to interactions and layout.

- **Marks:** Control color, size, opacity, symbols, gradients, strokes, curves,
  and colormaps.
- **Guides:** Customize axes, ticks, grids, annotations, legends, colorbars, and
  tooltips.
- **Interaction:** Add pan, zoom, hover, selections, crosshairs, callbacks, and
  linked charts.
- **Layout:** Create layers and facets, set responsive dimensions, and apply
  themes.

```python
chart = xy.line_chart(
    xy.line(x, y, color="#7c3aed", width=3),
    class_name="rounded-xl bg-white",
    class_names={"tooltip": "rounded-lg bg-zinc-900 text-white"},
)
```

See 