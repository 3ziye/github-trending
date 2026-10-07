<p align="center">
  <img src="dist/icon-512.png" width="96" alt="Recipe Lab icon">
</p>

<h1 align="center">Recipe Lab</h1>

<p align="center">
  Film simulations and camera looks for the <b>Sony</b> cameras that support <b>PlayMemories Camera Apps</b>, stored in the camera itself.<br>
  <sub>
    <img src="https://img.shields.io/github/v/release/voxivoid/recipe-lab-sony-pmca?label=version" alt="version"> ·
    <a href="https://github.com/voxivoid/recipe-lab-sony-pmca/releases/latest/download/RecipeLab.apk">Download the app</a> ·
    <a href="docs/SAMPLES.md">See every recipe</a>
  </sub>
</p>

<h3 align="center">Do you love this project? Sponsor it!</h3>

<p align="center">
  <a href="https://github.com/sponsors/voxivoid"><img
    src="https://img.shields.io/badge/Sponsor_on_GitHub-%E2%9D%A4-db61a2?logo=githubsponsors&logoColor=white&style=for-the-badge"
    alt="Sponsor on GitHub"></a>
  <a href="https://ko-fi.com/voxivoid"><img
    src="https://img.shields.io/badge/Tip_on_Ko--fi-%E2%98%95-ff5e5b?logo=kofi&logoColor=white&style=for-the-badge"
    alt="Tip on Ko-fi"></a>
</p>

<p align="center">
  <sub>
    The app is free and stays free. Sponsoring pays for keeping it maintained, for building new features, and for
    buying the cameras it has to be tested on — I currently only own a Sony a6000.
  </sub>
</p>

---

**Contents**

- [What it is](#what-it-is)
- [The recipes](#the-recipes)
- [Compatibility](#compatibility)
  - [Cameras that run PlayMemories apps](#cameras-that-run-playmemories-apps)
  - [Cameras that cannot run camera apps](#cameras-that-cannot-run-camera-apps)
- [Installing](#installing)
- [How to use](#how-to-use)
- [Custom recipes](#custom-recipes)
  - [Making one](#making-one)
  - [The edit buttons](#the-edit-buttons)
  - [Rename, delete, favourite](#rename-delete-favourite)
  - [Sharing](#sharing)
- [What it changes](#what-it-changes)
- [Uninstalling](#uninstalling)
- [Troubleshooting](#troubleshooting)
- [For developers](#for-developers)
- [Credits](#credits)

---

## What it is

Recipe Lab is a small app that runs on the camera itself — on Sony cameras that support PlayMemories Camera Apps, such
as the A6000, A6300, A6500 and A7 II (see [Compatibility](#compatibility)). It comes with 76 colour recipes that
recreate the looks of other cameras — Fuji film simulations, Ricoh GR image controls, Leica, Hasselblad, Canon and
Nikon colour, Sony's newer Creative Looks — and of classic film stocks from Kodak, Fuji, Cinestill, Agfa and Ilford.
You can also make your own, and share them.

You turn the wheel, watch the live image change, press a button. From then on the camera shoots that way in **every
mode**, photo and video, with the app closed. Turn it off and on, it is still there.

> **Honest note.** The A6000 has no Picture Profile menu and cannot store tone curves. Every recipe is built only from
> what this camera *can* keep: Creative Style, saturation, contrast, sharpness, white balance, exposure bias, Picture
> Effect and one hidden colour setting Sony never exposed. So these are approximations of a look, not copies of another brand's colour science.

## The recipes

| brand | recipes |
|---|---|
| **Sony** | Factory (the camera's own look), PT, NT, VV, VV2, FL, IN, SH |
| **Fuji simulations** | Provia, Velvia, Astia, Classic Chrome, Classic Negative, Nostalgic Neg, Reala Ace, Pro Neg Std / Hi, Eterna, Eterna Bleach Bypass, Acros, Acros +Ye / +R / +G, Sepia |
| **Fuji film** | Pro 400H, Fortia 50, Superia 400, C200, Natura 1600 |
| **Kodak** | Portra 160 / 400 / 800, Gold 200, Ultra Max 400, Color Plus 200, Ektar 100, Ektachrome E100, Kodachrome 64, Vision3 500T, Vision 200T (Asteroid City), Tri-X 400, Tri-X 1600 (pushed), T-Max |
| **Cine** | Cinestill 50D, Cinestill 800T, Classic Cinema, Rec709 Video |
| **Ricoh GR** | Positive Film, Negative Film, Bleach Bypass, Retro, Cross Process, Hi-Contrast B&W, Hard Monotone, Soft Monotone |
| **Leica** | Contemporary, Classic, Eternal, Monochrom |
| **Hasselblad** | HNCS Natural |
| **Canon / Nikon** | Canon Standard / Portrait / Faithful, Nikon Flat / Vivid |
| **Panasonic / Olympus** | L.Monochrome D, L.ClassicNeo, Pop Art, Pale & Light |
| **Other stocks** | Agfa Vista 200, Agfa Ultra 100, Polaroid / Instax |
| **Ilford** | HP5, FP4, Delta 100, Delta 3200, Pan F 50 |

**[See every recipe on the same subject →](docs/SAMPLES.md)** — 77 frames, one scene, one exposure, straight out of
the camera.

Recipes marked **JPEG only** in the app (Acros +R, Tri-X 1600, GR Retro, GR Hi-Contrast B&W, Sony SH, Polaroid) are
built on a Picture Effect because, against the reference frames, its tone
curve gets closer than Creative Style can; everything else stays Creative Style on purpose.

Not included, because the camera simply cannot do them: log profiles (S-Log, V-Log, Blackmagic Film, Cinelike D) and
tinted black & white (selenium, cyanotype). Sony's camcorder *Cinematone* gamma exists in the firmware but the A6000's
camera layer neither lists nor accep