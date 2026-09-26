<p align="center">
  <img src="app/icon.svg" width="72" alt="" />
</p>

<h1 align="center">M3E Canvas</h1>

<p align="center">
  <strong>Sketch Material 3 Expressive screens in the browser, link them, tap through them, and copy a prompt for your AI coding tool.</strong>
</p>

<p align="center">
  <a href="https://lnkiai.github.io/m3e-canvas/"><img alt="Live demo" src="https://img.shields.io/badge/demo-lnkiai.github.io%2Fm3e--canvas-6750A4?logo=googlechrome&logoColor=white" /></a>
  <a href="https://github.com/lnkiai/m3e-canvas/actions/workflows/deploy.yml"><img alt="Deploy" src="https://github.com/lnkiai/m3e-canvas/actions/workflows/deploy.yml/badge.svg" /></a>
  <a href="https://github.com/lnkiai/m3e-canvas/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/lnkiai/m3e-canvas?style=flat&logo=github&color=6750A4" /></a>
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-blue.svg" /></a>
  <a href="https://github.com/sponsors/lnkiai"><img alt="Sponsor" src="https://img.shields.io/badge/sponsor-%E2%9D%A4-EA4AAA?logo=githubsponsors&logoColor=white" /></a>
  <img alt="Next.js" src="https://img.shields.io/badge/Next.js-16-black?logo=nextdotjs" />
  <img alt="React" src="https://img.shields.io/badge/React-19-20232a?logo=react&logoColor=61DAFB" />
  <img alt="Material 3 Expressive" src="https://img.shields.io/badge/Material%203-Expressive-EADDFF?logo=materialdesign&logoColor=6750A4" />
  <img alt="No backend" src="https://img.shields.io/badge/backend-none%20(localStorage)-2E6A45" />
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/208608"><img alt="Trendshift: #1 repository of the day" src="https://trendshift.io/api/badge/trendshift/repositories/208608/daily" width="250" height="55" /></a>
</p>

<p align="center">
  <a href="#日本語">日本語</a> · <a href="#中文">中文</a> · <a href="#한국어">한국어</a> · <a href="https://lnkiai.github.io/m3e-canvas/">Open the app</a>
</p>

![Sketching a recipes app in M3E Canvas, changing its theme, copying the prompt, an AI coding tool building it, and the app running on Android](docs/story.gif)

<p align="center"><sub>Sketch a recipes app, retheme it, copy the prompt, hand it to an AI coding tool, and run the result on Android. (<a href="docs/story.mp4">mp4</a>)</sub></p>

Works with any AI coding tool that takes a prompt, such as Claude Code, Codex, Gemini CLI or Cursor: copy the prompt, paste it into the tool, and ask for the app.

## What it does

- **Drag-and-drop parts** – buttons, icon buttons, FABs, split buttons, FAB menus, chips, app bars, navigation bars, floating toolbars, tabs, search bars, cards, lists, dialogs, snackbars, text fields, dropdowns, switches, checkboxes, radio buttons, sliders, text, images, camera and map placeholders, badges, boxes and dividers, all drawn to Material 3 Expressive.
- **Magnetic connections** – bring two buttons or list items close and they fuse into a connected group; the corners soften as they meet.
- **Real M3 Expressive loading** – the shape-morphing Loading Indicator (ported from material-components-android) and wavy linear / circular progress indicators.
- **Phone and desktop screens** – add as many screens as you like, name them, pick a background, and drag a screen to move everything on it. Switch any screen between a 412×892 phone and a 1280×800 desktop from its label: bars stretch, the navigation bar becomes a rail (and a rail becomes a bar again on a phone), and the parts are laid out again beside it. Screens of both sizes can share one design; same-named screens are written into the prompt as one screen at two widths.
- **Tap to navigate** – give any tappable part, an app bar icon or a navigation bar destination a target screen (or "back") and a transition: slide from any of the four sides, fade, expand or none. Arrows show the flow on the canvas; the preview lets you tap through it, and back plays the transition in reverse.
- **Swipe to navigate** – a screen can open another on a left / right / up / down swipe. In the preview the screen follows your finger, and the reverse swipe goes back.
- **Toggle buttons** – any button can flip on tap, changing its icon and style.
- **Layers and groups** – a layers panel lists the z-order of each screen; drag a row to bring parts forward or send them back, and open a group or a connected run to reorder what is inside it. Select several parts and group them to keep their overlap and move them as one. The prompt describes overlaps and side-by-side rows explicitly so the generated layout keeps them.
- **Theme** – the four M3 Expressive axes in one panel. Color: seven presets or one seed color that becomes a full Material 3 scheme you can fine-tune, light / dark, three contrast levels and a dynamic-color switch (match the phone wallpaper). Shape: square, rounded or full corners for every part at once. Type: Roboto, Roboto Flex, Roboto Serif or the system font, with the emphasized styles. Motion: the standard or the express