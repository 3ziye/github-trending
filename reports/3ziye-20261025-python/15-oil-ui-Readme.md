English · [中文](README.zh-CN.md)

<p align="center">
  <img src="./assets/readme/hero.en.webp" width="100%" alt="oil-ui: push AI UI design to its limits. A person pins a yellow pushpin to the middle of three previews in different styles">
</p>

<p align="center">
  <a href="https://ui.oiloil.org/en/?utm_source=github&utm_medium=referral&utm_campaign=readme-en"><img src="./assets/readme/showcase.en.webp" width="100%" alt="Gallery highlights: an English learning app, a music year in review, hardware and component library websites, a project management tool, a ride-hailing app, a voice assistant, a checkout flow, and a film camera"></a>
</p>

Oil UI is an interface design skill for AI agents. It explores a few genuinely different design directions side by side, lets you choose one, then refines it against real screenshots. It works for websites, apps, dashboards, and components. See more designs at [ui.oiloil.org](https://ui.oiloil.org/en/?utm_source=github&utm_medium=referral&utm_campaign=readme-en).

## How it designs

1. **Understand what the product is.** Before drawing anything, it names the product category, finds two or three peers with the most distinctive styles, and looks at what they do and why. Then it decides what to keep and what to change.
2. **Turn “premium” and “clean” into real decisions.** Everyone uses these words, but they don't tell you what to put on the screen. It first sets the tone from the subject, audience, and brand voice, such as lively or calm, polished or raw, dense or airy. Then it turns that tone into visible choices: which typefaces, how much white space, and how much of the page uses color.
3. **Start each direction from something concrete.** That could be a material in its setting, a scene, a character, or the visual language of another field. Ideas come from the product itself, not from adjectives like “minimal” or “bold.”
4. **Decide who the first screen is for.** On pages where people browse, shop, or get work done, the first screen should be the content itself. Only pages meant to persuade need a designed opening layout, settled before the copy is written.
5. **Make the directions truly different.** Of layout, typography, color, and key imagery, any two directions may share at most one. Once the previews exist, it puts them side by side and squints at the light and dark shapes of each first screen. If two look alike, it changes the layout instead of just swapping colors.
6. **Leave one moment people remember.** Instead of pushing every part of the page, it makes one or two details exceptional, such as the response to a tap, a successful payment, AI at work, or a 404 page. Everything else stays quiet.
7. **You decide what looks right.** The previews go on one comparison page. You pick one and say what you like and dislike, and it tightens the design around your feedback before going further.
8. **Trust the real screen.** When a page is done, it opens it at desktop and mobile sizes and checks screenshots. You can also bring in a reviewer who hasn't seen the work in progress. Last comes a round of subtraction: one focal point per page, and no copy, lines, or boxes that don't help you understand it.

For more usable interfaces, existing project redesigns, or effects such as light trails and dot patterns, see [Oil UI Pro](https://ui.oiloil.org/en/pro/?utm_source=github&utm_medium=referral&utm_campaign=readme-en). The differences are listed [below](#open-source-and-pro).

## Installation

Send this to an agent that can install skills:

```text
Install this skill for me: run npx skills add oil-oil/oil-ui
```

Or run this in your terminal:

```bash
npx skills add oil-oil/oil-ui
```

It's ready to use right after installation, with nothing to configure. When a new version is out, your agent mentions it at the end of a reply; ask it to update whenever you like. If you already have Oil UI Pro, you don't need the open-source version. Installing both makes them compete for the same requests.

If you use DeepSeek Harness, install the native plugin [dsh-oil-ui](https://github.com/oil-oil/dsh-oil-ui) (`dsh plugin --profile web add github:oil-oil/dsh-oil-ui`; it includes the free edition and automatically detects a local Oil UI Pro installation).

## Usage

Tell your agent what you need, for example:

- “Use oil-ui to explore a few design directions for this course booking product and build pages I can preview.”
- “Create three designs with different typography, colors, and compositions. Put them on a comparison page so I can choose.”
- “Polish this page using the project’s existing design guidelines.”
- “Review this homepage and explain what to change and how. Leave the files untouched.”
- “Recreate this page from the screenshot and add a mobile layout too.”

Share any brand assets, screenshots, or existing project you have. It can start without references and only asks you questions when the deliverable is unclear.

Intermediate candidates, screenshots, and media caches live in the pro