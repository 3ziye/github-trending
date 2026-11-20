<p align="center">
  <img src="docs/assets/logo.png" width="160" height="160" alt="The rust-anything crab">
</p>

<h1 align="center">rust-anything</h1>

<p align="center"><b>Rewrite your app in Rust, and prove it still behaves the same.</b></p>

<p align="center">New in 2.0: <a href="docs/real-world.md#prettier">Prettier, ported to Rust</a>. 19x faster · 15,837 of 17,224 recorded runs fully in Rust · every run byte-identical</p>

<p align="center">
  <a href="https://crates.io/crates/rust-anything"><img src="https://img.shields.io/crates/v/rust-anything?color=E2862A&label=crates.io" alt="crates.io version"></a>
  <a href="https://www.npmjs.com/package/rust-anything"><img src="https://img.shields.io/npm/v/rust-anything?color=E2862A&label=npm" alt="npm version"></a>
  <a href="https://github.com/erkamyaman/rust-anything"><img src="https://img.shields.io/github/stars/erkamyaman/rust-anything?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/AIshihzong/awesome-reverse-engineer-anything"><img src="https://img.shields.io/badge/Featured%20in-Awesome%20REA-f0b429" alt="Featured in Awesome REA"></a>
  <a href="https://github.com/rust-unofficial/awesome-rust#development-tools"><img src="https://awesome.re/mentioned-badge.svg" alt="Mentioned in Awesome Rust"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="#languages">Languages</a> ·
  <a href="docs/real-world.md">Real-world ports</a> ·
  <a href="docs/how-it-works.md#how-it-works">How it works</a> ·
  <a href="docs/whole-apps.md#port-a-whole-app">Whole apps</a> ·
  <a href="docs/faq.md#faq">FAQ</a>
</p>

<p align="center">Made in Türkiye 🇹🇷 by <a href="https://github.com/erkamyaman">erKam Yaman</a> · <a href="LICENSE">MIT</a> · <a href="https://github.com/sponsors/erkamyaman">❤️ Sponsor me</a></p>

<p align="center">Sponsored by <a href="https://coderabbit.ai"><img src="docs/assets/brands/coderabbit.png" width="22" height="22" align="absmiddle" alt=""> <b>CodeRabbit</b></a></p>

<p align="center"><sub>English · <a href="docs/README_TR.md">Türkçe</a> · <a href="docs/README_UK.md">Українська</a> · <a href="docs/README_ZH.md">简体中文</a> · <a href="docs/README_ZH-TW.md">繁體中文</a> · <a href="docs/README_DE.md">Deutsch</a> · <a href="docs/README_FR.md">Français</a> · <a href="docs/README_RU.md">Русский</a> · <a href="docs/README_JA.md">日本語</a> · <a href="docs/README_KO.md">한국어</a> · <a href="docs/README_AZ.md">Azərbaycanca</a> · <a href="docs/README_UZ.md">Oʻzbekcha</a> · <a href="docs/README_KK.md">Қазақша</a> · <a href="docs/README_KY.md">Кыргызча</a> · <a href="docs/README_TK.md">Türkmençe</a> · <a href="docs/README_TT.md">Татарча</a> · <a href="docs/README_UG.md">ئۇيغۇرچە</a> · <a href="docs/README_PT.md">Português</a> · <a href="docs/README_VI.md">Tiếng Việt</a></sub></p>

<table>
  <tr>
    <td width="25%" valign="top">
      <b>Record</b><br>
      <code>record</code> runs the original on generated edge cases, semantic traps and your own inputs, and saves what it returns or throws.
    </td>
    <td width="25%" valign="top">
      <b>Port</b><br>
      <code>bridge</code> generates the Rust crate and a wrapper, so callers keep the original API. You or your agent write the Rust.
    </td>
    <td width="25%" valign="top">
      <b>Check</b><br>
      <code>diff</code> replays every recorded case against the Rust, and nothing ships until they all match and <code>gate</code> passes.
    </td>
    <td width="25%" valign="top">
      <b>Lift</b><br>
      When replay passes with no fallback and every unit passes gate, <code>app lift</code> makes it a pure Rust app. The original is never touched.
    </td>
  </tr>
</table>

**Rewrite your whole app in Rust, one piece at a time.** rust-anything records what your
Node.js (TypeScript/JavaScript), Python, C, Go, Ruby, Java or Kotlin app does today, then checks every piece of the
Rust rewrite against that recording before it moves on, until the app is pure Rust. CLIs, HTTP
servers and libraries; your coding agent (or you) writes the Rust. It can only catch what the
recording covers: see [What it can't catch](docs/how-it-works.md#what-it-cant-catch). Whole tools
and servers, or only the slow part, one hot path at a time:

| Real project, same output as the original | Original | With rust-anything |
| --- | ---: | ---: |
| [Prettier](docs/real-world.md#prettier) 3.6.2, 2,360 JS/TS files from the command line | 128.6 s | **6.9 s: 19x faster** |
| Prettier, 6,305 Markdown files from the command line | 352 s | **22.5 s: 15.6x faster** |
| [json-server](docs/real-world.md#json-server), a whole Node server: memory at idle | 74 MB | **3.5 MB**, one 5.3 MB binary |
| json-server, from start to first response | 79 to 85 ms | **8 to 10 ms** |
| [Fuse.js](docs/real-world.md#fusejs) search over 50,000 strings, per query | 91.2 ms | **2.8 ms: 32x faster** |

Prettier: 15,837 of 17,224 recorded runs format fully in Rust across 10 languages (JavaScript,
TypeScript, JSX, JSON, GraphQL, YAML, Ma