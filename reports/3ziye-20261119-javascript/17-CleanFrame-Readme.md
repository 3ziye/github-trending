# CleanFrame

A quieter home screen for Samsung The Frame. Your apps, a photograph and the time, with an interface made for the TV remote.

![CleanFrame browser preview using the bundled Manrope font](docs/images/cleanframe-dock.jpg)

I built CleanFrame for one TV: my own Samsung The Frame, running Tizen. I'm sharing the code and setup notes as a starting point for other people to build on.

**Use it at your own risk.** The web launcher targets Tizen 5.0 and later for installation, with [owner reports](docs/compatibility.md) across several models. That minimum is not a promise that every device flow is verified. The TV setup scripts and native Home helpers still reflect specific computers and firmware, so adapt them and test on your own hardware.

I highly recommend forking it and building on top of it, ideally with a coding agent that can help you understand and adapt the setup. Start with the browser preview, make the interface your own, then work through TV installation when you're ready. Native Home/startup changes need particular care; the setup guide covers the risks and recovery steps.

## Try the interface

You need Node.js 22.13+ (22 LTS), or 24+, and Python 3.10+ to run the browser preview.

```sh
git clone https://github.com/nthnclrk/CleanFrame.git
cd CleanFrame
npm ci
npm run dev:public
```

Open [localhost:4795/home/](http://localhost:4795/home/). Use the arrow keys, Enter and Escape, or click the controls. App launches and Samsung screens require a TV; the preview reports that limitation when you select them.

The public preview uses the included Manrope, Geist and Newsreader fonts.

## What you can change

- Choose a List or Dock layout, with icons, names or both.
- Use a photograph, light or dark background, with a simple 12-hour clock.
- Adjust typography, focus and glass materials through the same Settings interface.
- Choose and reorder Home apps; discover installed apps on the TV.
- Select from fifteen wallpapers and save your preferences locally.
- Open Settings → Samsung → Inputs to choose a discovered HDMI source.

The glass and blur are rendered ahead of time. The TV loads the finished images and uses transforms and opacity for focus feedback.

## Use a coding agent

Open this repo in a local coding agent and give it a bounded change:

```text
Read AGENTS.md, docs/development.md and docs/interaction-behaviour.md.
Help me adapt CleanFrame. Start with the public-font browser preview.
My first change is: <describe one change>.
Preserve remote navigation, saved preferences and the ES5 runtime.
Run the source checks and relevant browser checks. Show the result.
This task is browser-only: do not connect to a TV, sign or install a
package, or change Home/startup settings.
```

See [working with an agent](docs/for-agents.md) for the TV setup prompt and the distinction between UI work, app installation and native Home changes. An agent needs local computer access for TV work; a hosted chat cannot reach your TV merely by reading this repo.

## Put it on a TV

Use the staged [Samsung The Frame setup guide](docs/agent-tv-setup-guide.md) to understand the process used on my TV and adapt it to yours. It covers the remote's Developer Mode sequence, official Samsung tools, your own certificates and app identity, installation, visible checks and recovery.

The [latest release](https://github.com/nthnclrk/CleanFrame/releases/latest) includes an unsigned, public-font widget for inspection and adaptation. For your installation, build from source using your own identity in `.local/signing.json` and sign with your own certificates. The download is not a ready-to-install signed package.

Signing supports an ignored `.local/signing.json` based on `signing.example.json`: select your SDK, existing certificate profile and your own SDK-generated app identity. See [local signing setup](docs/development.md#local-tv-tools-and-signing). The TV installation commands and native Home helper still contain reference-machine assumptions. Your agent must check the installed-app IDs and each device stage with you. Installing the app and assigning the remote Home button are separate steps.

| Area | Evidence and limits |
| --- | --- |
| Reference hardware | Samsung QA55LS03DAWXXY / LS03D, firmware 2130.0, Tizen 9.0, 32-bit ARM |
| App installation | Signed installation and launch commands succeeded through 0.6.1. Latest rendering and remote feel still need physical observation. |
| App launch and Home | Netflix/YouTube launch and physical Home from Netflix were confirmed on the reference setup. |
| Still open | Normal power-on after streaming/Art Mode, corrected Smart Hub escape and native Art Mode destinations need definite physical checks. |
| Other TVs | Web installation target: Tizen 5.0+. See the attributed [device reports](docs/compatibility.md) for tested flows and omissions. Android TV, Google TV, LG webOS and Roku need separate implementations. |

The optional [2020 LS03T profile](scripts/native-home/frame-2020/REA