# DuoFold for Android

[![Android](https://img.shields.io/badge/Android-10%2B-3DDC84?logo=android&logoColor=white)](https://github.com/jcx396905-gif/DuoFold-Android)
[![Shizuku](https://img.shields.io/badge/Shizuku-required-7C4DFF)](https://github.com/RikkaApps/Shizuku)
[![Release](https://img.shields.io/github/v/release/jcx396905-gif/DuoFold-Android?display_name=tag)](https://github.com/jcx396905-gif/DuoFold-Android/releases/latest)
[![License](https://img.shields.io/github/license/jcx396905-gif/DuoFold-Android)](LICENSE)
[![Stars](https://img.shields.io/github/stars/jcx396905-gif/DuoFold-Android?style=flat)](https://github.com/jcx396905-gif/DuoFold-Android/stargazers)

**A system-wide iPhone Duo-style folding illusion for regular Android phones — no foldable hardware and no root required.**

DuoFold turns the entire Android display into a motion-driven spatial surface. As you tilt your phone left/right or forward/backward, the current screen is reprojected in real time with perspective, translation, blur, lighting, and depth effects. The motion pauses when the phone stops and reverses naturally when you tilt it back.

**English** · [简体中文](#简体中文)

## Demo

<a href="https://github.com/jcx396905-gif/DuoFold-Android/releases/download/v0.4.0/DuoFold-IMG-0019.mov"><img src="media/extra-demo-cover.jpg" width="360" alt="DuoFold latest real-device demo"></a>

▶ [Watch the latest real-device demo (~23 s)](https://github.com/jcx396905-gif/DuoFold-Android/releases/download/v0.4.0/DuoFold-IMG-0019.mov)

## More test videos

<a href="https://github.com/jcx396905-gif/DuoFold-Android/releases/download/v0.4.0/DuoFold-full-test.mp4"><img src="media/full-test-cover.jpg" width="360" alt="DuoFold full test video"></a>

▶ [Watch the full test video (~30 s)](https://github.com/jcx396905-gif/DuoFold-Android/releases/download/v0.4.0/DuoFold-full-test.mp4)

<a href="https://github.com/jcx396905-gif/DuoFold-Android/releases/download/v0.4.0/DuoFold-demo-clip.mp4"><img src="media/demo-clip-cover.jpg" width="360" alt="DuoFold short demo clip"></a>

▶ [Watch the short demo clip (~6 s)](https://github.com/jcx396905-gif/DuoFold-Android/releases/download/v0.4.0/DuoFold-demo-clip.mp4)

## Screenshots

<p align="center">
  <img src="media/app-setup.jpg" width="320" alt="DuoFold setup screen">
  <img src="media/app-settings.jpg" width="320" alt="DuoFold settings and author screen">
  <img src="media/app-effects.png" width="320" alt="DuoFold 0.6.0 animation effects">
</p>

## Download

- **Android 14 and newer:** download `DuoFold-0.6.0-Android14-and-newer.apk` from the [Latest Release](https://github.com/jcx396905-gif/DuoFold-Android/releases/latest).
- **Android 10–13:** download `DuoFold-0.6.0-Android10-13.apk` from the same [Latest Release](https://github.com/jcx396905-gif/DuoFold-Android/releases/latest).

## Features

- Treats the entire active Android screen as one continuous spatial surface and applies perspective, translation, frosted blur, and lighting effects.
- Uses device motion sensors to drive the effect in real time. Stop moving the phone and the animation stops; tilt in the opposite direction and it reverses naturally.
- Left/right motion is enabled by default. Optional **Z-axis sensing · forward/back tilt** adds front/back motion, with diagonal movement blended continuously.
- Automatically adapts to portrait and landscape orientation and maps sensor axes to the current display coordinates.
- Does not modify launcher layouts or third-party app UIs; the effect is rendered over whatever interface you are currently using.
- On Android 14+, the effect can be stopped with a three-finger touch, the notification action, or by returning to DuoFold. The compatibility build uses the notification stop action.

## Animation effects (v0.6.0)

Choose a style in the app's **Animation effects** card. Changes are saved and applied immediately while the effect is running. **Classic Frosted** remains the default, and Z-axis sensing remains disabled by default in both Android builds.

| Style | Tilt and hover behavior |
| --- | --- |
| Classic Frosted · default | Original distance blur, grain, and shading; the frosted appearance remains while the phone is still. |
| Edge Fade | Keeps the anchored edge clearer while the opening edge gradually blurs and darkens. |
| Soft Depth | Uses softer weighted sampling and lighter shading for a subtle glass depth effect. |
| Hover Clear | Blurs during motion, then clears gradually after the phone has remained still for about half a second. |
| Clear Projection | Keeps the folding perspective without added blur or shading. |
| Lens Bokeh | Uses an independent 30° camera projection, a sharp near edge, quadratic far-edge blur, 16-tap disc bokeh, and continuous texture prefiltering. |

The first five styles share the classic projection. **Lens Bokeh** uses independent two-axis edge rotation and camera projection; Android 14+ touch coordinates follow that projection. Horizontal tilt is capped at 60°, forward/bac