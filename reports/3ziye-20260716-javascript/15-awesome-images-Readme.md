# Flatkey Image Prompt Library

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [Español](README_es.md) | [Português](README_pt.md) | [Tiếng Việt](README_vi.md)

Image Buddy is a commercial prompt library and CLI for generating useful marketing images with [Flatkey.ai](https://flatkey.ai?utm_source=skill). Flatkey can be about 40% cheaper than common direct image API routes, and this repo makes it easier to turn that lower cost into usable product images, ads, avatars, app visuals, and ecommerce creatives.

Get API key: <https://flatkey.ai?utm_source=skill>

## What You Get

- **Lower generation cost**: use Flatkey.ai for image generation, often around 40% cheaper than common direct API routes.
- **Commercial prompts that work**: templates are written for product, ecommerce, social ads, UI screenshots, avatars, posters, game assets, and edits.
- **Fast generation demo**: use `image-buddy web` to open a local demo gallery and generate images with a Flatkey key.
- **CLI-first workflow**: onboard once, then generate from a short sentence or a template hint.

## Includes

**Skill**: a copy-paste prompt for your AI agent. The agent installs and uses Image Buddy for you, backed by the CLI.

Paste this into your AI assistant:

```text
Install and use the Flatkey Image Buddy skill from https://github.com/flatkey-ai/awesome-images.
When I ask for an image, use image-buddy CLI with Flatkey. First run image-buddy onboard if needed, then generate the image from my short prompt or from a template hint. Do not stop at suggesting prompts.
```

**CLI**: one command-line tool for onboarding and generation.

- `image-buddy onboard`: save your Flatkey API key locally.
- `image-buddy generate --prompt "..."`: generate from a plain sentence.
- `image-buddy generate avatar-pack "地雷妹"`: generate from a template plus hint.
- `image-buddy web`: open the optional demo gallery.

## Quickstart

Generate an image with no local install:

```bash
npx @flatkey-ai/image-buddy onboard
npx @flatkey-ai/image-buddy generate --prompt "premium product hero image for an AI image API CLI"
```

Use a template with a short hint:

```bash
npx @flatkey-ai/image-buddy generate avatar-pack "地雷妹"
```

Open the optional web gallery:

```bash
npx @flatkey-ai/image-buddy web
```

No API key yet? Create one at <https://console.flatkey.ai/keys>. The CLI reads the saved key, `FLATKEY_IMAGE_API_KEY`, or `FLATKEY_API_KEY`.

## Why This Exists

- **Lower activation friction**: users start from proven templates instead of a blank prompt box.
- **Increase API conversion**: every template card sends users to Flatkey API key registration.
- **Cover common commercial use cases**: product marketing, ecommerce images, social ads, infographics, avatars, app screenshots, game assets, and image edits.
- **Support batch workflows**: templates use `{{variable}}` placeholders, so apps can replace values before sending final prompts to an API.
- **Work as marketing content**: useful as a prompt gallery, tutorial page, landing page, or onboarding resource.

## Included Templates

This library currently includes 12 high-frequency image prompt templates:

- Premium product hero visual
- White-background ecommerce main image
- UGC ad cover frame
- Liquid glass Bento infographic
- Founder quote card
- Consistent avatar pack
- App Store screenshot poster
- YouTube thumbnail
- Event poster key visual
- Game prop concept sheet
- Subject-preserving background replacement
- Fashion lookbook collage

Each template includes:

- Title and use case
- Category and recommended model
- Replaceable variables
- Full prompt text
- API use-case note
- Copy prompt button
- Flatkey API key registration link

## Demo Gallery

The web gallery ships with 20 generated demo images. These are included in the npm package and shown by `image-buddy web`.

| Product | Ecommerce | Social Ad | App |
|---|---|---|---|
| ![SaaS Hero Phone](assets/saas-hero-phone.png)<br>**SaaS Hero Phone** | ![Skincare Product](assets/ecommerce-skincare.png)<br>**Skincare Product** | ![UGC Coffee Ad](assets/ugc-coffee-ad.png)<br>**UGC Coffee Ad** | ![Fitness App](assets/fitness-app.png)<br>**Fitness App** |

| Poster | Infographic | Fashion | Game Asset |
|---|---|---|---|
| ![AI Agent Poster](assets/ai-agent-poster.png)<br>**AI Agent Poster** | ![Liquid Bento](assets/liquid-bento.png)<br>**Liquid Bento** | ![Streetwear Lookbook](assets/streetwear-lookbook.png)<br>**Streetwear Lookbook** | ![Crystal Game Prop](assets/game-prop-crystal.png)<br>**Crystal Game Prop** |

| Food | Travel | Portrait | Real Estate |
|---|---|---|---|
| ![Dessert Hero](assets/food-dessert.png)<br>**Dessert Hero** | ![Travel Map](assets/travel-map.png)<br>**Travel Map** | ![Cyber Portrait](assets/cyber-portrait.png)<br>**Cyber Portrait** | ![Interior Render](assets/real-estate-interior.png)<br>**Interior Render** |

| Entertainment | Education | Finance | Beauty |
|---|---|---|---|
| ![Music Cover](assets/music-cover.png)<br>**Music Cove