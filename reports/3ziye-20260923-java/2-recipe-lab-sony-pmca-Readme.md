<p align="center">
  <img src="dist/icon-512.png" width="96" alt="Recipe Lab icon">
</p>

<h1 align="center">Recipe Lab</h1>

<p align="center">
  Film simulations and camera looks for the <b>Sony A6000</b>, stored in the camera itself.<br>
  <sub>
    <img src="https://img.shields.io/github/v/release/voxivoid/recipe-lab-sony-pmca?label=version" alt="version"> ·
    <a href="https://github.com/voxivoid/recipe-lab-sony-pmca/releases/latest/download/RecipeLab.apk">Download the app</a> ·
    <a href="docs/SAMPLES.md">See all 77 recipes</a>
  </sub>
</p>

<p align="center">
  <a href="https://github.com/sponsors/voxivoid"><img
    src="https://img.shields.io/badge/Sponsor_this_project-%E2%9D%A4-db61a2?logo=githubsponsors&logoColor=white&style=for-the-badge"
    alt="Sponsor this project"></a>
</p>

<p align="center">
  <sub>
    The app is free and stays free. Sponsoring pays for keeping it maintained, for building new features, and for
    buying the cameras it has to be tested on — every body beyond the A6000 is one someone has to own.
  </sub>
</p>

---

**Contents**

- [What it is](#what-it-is)
- [The recipes](#the-recipes)
- [Sample frames](docs/SAMPLES.md)
- [Compatibility](#compatibility)
- [Installing](#installing)
- [Using it](#using-it)
- [What it changes](#what-it-changes)
- [Uninstalling](#uninstalling)
- [Troubleshooting](#troubleshooting)
- [FAQ](docs/FAQ.md)
- [For developers](#for-developers)
- [Credits](#credits)

---

## What it is

Recipe Lab is a small app that runs on the Sony A6000 itself. It comes with 77 colour recipes that recreate the looks
of other cameras — Fuji film simulations, Ricoh GR image controls, Leica, Hasselblad, Canon and Nikon colour, Sony's
newer Creative Looks — and of classic film stocks from Kodak, Fuji, Cinestill, Agfa and Ilford.

You turn the wheel, watch the live image change, press a button. From then on the camera shoots that way in **every
mode**, photo and video, with the app closed. Turn it off and on, it is still there.

> **Honest note.** The A6000 has no Picture Profile menu and cannot store tone curves. Every recipe is built only from
> what this camera *can* keep: Creative Style, saturation, contrast, sharpness, white balance, exposure bias, Picture
> Effect and one hidden colour setting Sony never exposed. So these are approximations of a look, not copies of another brand's colour science.

## The recipes

| brand | recipes |
|---|---|
| **Sony** | Factory (ST), PT, NT, VV, VV2, FL, IN, SH |
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

Recipes marked **PE** in the app (Acros +R, Tri-X 1600, GR Retro, GR Hi-Contrast B&W, Sony SH, Polaroid) are built on
a Picture Effect because, against the reference frames, its tone
curve gets closer than Creative Style can; everything else stays Creative Style on purpose.

Not included, because the camera simply cannot do them: log profiles (S-Log, V-Log, Blackmagic Film, Cinelike D) and
tinted black & white (selenium, cyanotype). Sony's camcorder *Cinematone* gamma exists in the firmware but the A6000's
camera layer neither lists nor accepts it, so that door is closed too.

## Compatibility

Recipe Lab has no model check in it, and every Sony body that runs PlayMemories apps has the same settings store — so
it should install and work beyond the A6000.

The catch: the setting IDs were found on an A6000 and may sit elsewhere on another body, so a recipe could land in the
wrong place. A camera gets a ✅ only once someone has stored a recipe on it and power-cycled the camera.

Tried one? File a
[compatibility report](https://github.com/voxivoid/recipe-lab-sony-pmca/issues/new?template=compatibility_report.yml).
Failures are as useful as successes.

### Cameras that run PlayMemories apps

✅ someone has run it on that body · ❔ app-capable, nobody has reported back yet

| camera | model code | status 