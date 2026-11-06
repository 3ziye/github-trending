<p align="center">
  <img src="https://assets.rustgis.app/images/logo.svg" alt="RustGIS logo: a rust-coloured cog framing a segmented globe with an orbit" width="160">
</p>

<h1 align="center">RustGIS</h1>

<p align="center">
  <b>A fast, free and open-source GIS in pure Rust for mapping, analyzing and sharing geospatial data.</b><br>
  Native on Windows, macOS and Linux, and in your web browser. Your data stays on your machine
  unless you send it to an AI model you choose, and every action is a command you can script.
</p>

<p align="center">
  <img alt="Written in Rust" src="https://img.shields.io/badge/written%20in-Rust-b84a2c?style=flat-square&logo=rust&logoColor=white">
  <img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square">
  <img alt="20 languages" src="https://img.shields.io/badge/languages-20-0e9384?style=flat-square">
  <a href="https://plugins.rustgis.app"><img alt="Plugins" src="https://img.shields.io/badge/plugins-registry-7c3aed?style=flat-square"></a>
  <a href="https://pypi.org/project/rustgis/"><img alt="PyPI" src="https://img.shields.io/pypi/v/rustgis?style=flat-square&logo=python&logoColor=white&label=pypi"></a>
  <a href="https://colab.research.google.com/github/opengeos/RustGIS/blob/main/apps/rustgis-python/examples/getting-started.ipynb"><img alt="Open in Colab" src="https://colab.research.google.com/assets/colab-badge.svg"></a>
  <a href="https://doi.org/10.5281/zenodo.23633281"><img alt="DOI" src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23633281-1682d4?style=flat-square"></a>
</p>

<p align="center">
  <a href="https://web.rustgis.app"><img alt="Launch the RustGIS web app" src="https://img.shields.io/badge/Launch-web%20app-b84a2c?style=for-the-badge&logo=webassembly&logoColor=white" height="36"></a>
  <a href="https://github.com/opengeos/RustGIS/releases/latest"><img alt="Download the desktop app" src="https://img.shields.io/badge/Download-desktop%20app-2563eb?style=for-the-badge&logo=github&logoColor=white" height="36"></a>
  <a href="https://rustgis.app"><img alt="Read the documentation" src="https://img.shields.io/badge/Read-the%20docs-0e9384?style=for-the-badge&logo=materialformkdocs&logoColor=white" height="36"></a>
  <a href="https://rustgis.app/videos/"><img alt="Watch the video tutorials" src="https://img.shields.io/badge/Watch-video%20tutorials-dc2626?style=for-the-badge&logo=youtube&logoColor=white" height="36"></a>
  <a href="https://apps.microsoft.com/detail/9ppjw8h561lq?mode=direct"><img alt="Get it from Microsoft" src="https://get.microsoft.com/images/en-us%20dark.svg" height="36"></a>
</p>

<p align="center">
  <img src="https://assets.rustgis.app/images/hero.webp" alt="RustGIS with the Home tab of the ribbon open. The Layers pane lists Cities, Rivers, Lakes and Countries with their legends; the map shows the world in the Equal Earth projection, countries shaded by population, sized city dots and country labels." width="100%">
</p>

## Why RustGIS

- **Fast and small.** One native program, drawn on the GPU, with no runtime to install and no
  server to run.
- **Runs everywhere.** The same app on Windows, macOS and Linux, and compiled to WebAssembly at
  [web.rustgis.app](https://web.rustgis.app) with nothing to install.
- **Local and private.** Your files are read and written on your machine, and nothing is uploaded
  on its own. The network is used only when you ask for it: web basemaps, plugins, the GeoLibre
  tools and the AI model you pick, which receives your questions and the data it reads to answer
  them.
- **Everything is a command.** Every button in the ribbon is a command with an id. Script it from
  `rustgis-cli`, chain it in notebooks and models, use completion in the Script pane, or ask the
  AI Assistant to run it for you.
- **Familiar.** A ribbon laid out in the order of the work (Home, Data, Style, Edit, Analyze,
  View, Publish), Layers and Browser panes, an attribute table, and undo for every change.
- **Extensible.** Over 1,000 GeoLibre and Whitebox tools for terrain, hydrology, LiDAR and remote sensing, and
  sandboxed WebAssembly [plugins](docs/plugins.md) that add commands, tools and ribbon tabs.

## A tour

Prefer a video? [RustGIS: A Fast, Free GIS That Runs on Your Desktop and in Your
Browser](https://youtu.be/XFhqlSiKn6U) walks through the main features, and the
[Video Tutorials](https://rustgis.app/videos/) page collects the rest of the
[playlist](https://www.youtube.com/playlist?list=PLBQuwPke8dNI).

<table>
<tr>
<td width="50%" valign="top"><img src="https://assets.rustgis.app/images/symbology-table.webp" alt="The Style tab with the Symbology pane showing graduated colours and colour schemes; the larger African countries are selected in cyan on the map and highlighted in the attribute table below" width="100%"><p align="center"><sub><b>Symbology and tables.</b> Graduated colours, with the selection synced to the table.</sub></p></td>
<td width="50%" valign="top"><img src=