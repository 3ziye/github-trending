<p align="center">
  <a href="https://droidline.dev"><img src="docs/media/banner-en.jpg" alt="Droidline: Android automation, one line at a time." width="100%"></a>
</p>

<p align="center">
  <b>Automate real Android phones from your code.</b><br>
  Test your apps, script the tasks you repeat, run a shelf of phones, or let an AI agent use one.<br>
  Python, Node.js, the shell or HTTP. No ADB, no USB cable, no root.
</p>

<p align="center">
  <a href="https://droidline.dev"><b>Website</b></a> ·
  <a href="https://droidline.dev/docs/"><b>Docs</b></a> ·
  <a href="https://github.com/KnifeLemon/Droidline/releases/latest"><b>Download</b></a> ·
  <a href="https://github.com/sponsors/KnifeLemon"><b>Sponsor</b></a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#use-it-from-your-language">Languages</a> ·
  <a href="#documentation">Guides</a>
</p>

<p align="center">
  <a href="https://github.com/KnifeLemon/Droidline/actions/workflows/ci.yml"><img src="https://github.com/KnifeLemon/Droidline/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/KnifeLemon/Droidline/releases/latest"><img src="https://img.shields.io/github/v/release/KnifeLemon/Droidline?color=FF6B21&label=release" alt="Latest release"></a>
  <img src="https://img.shields.io/badge/Android-9%2B-15803D" alt="Android 9 or later">
  <img src="https://img.shields.io/badge/PC-Windows%20%7C%20macOS%20%7C%20Linux-1C202B" alt="Windows, macOS and Linux">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-B53A07" alt="MIT license"></a>
</p>

<p align="center"><b>English</b> · <a href="README.ko.md">한국어</a> · <a href="README.zh-CN.md">简体中文</a></p>

<table>
  <tr>
    <td width="33%" valign="top"><b>No ADB, no cable</b><br>Install one app on the phone, turn on its permissions and pair it with a QR code. No developer options, no USB debugging, no root.</td>
    <td width="33%" valign="top"><b>The same command everywhere</b><br><code>touch</code> is <code>touch</code> in Python, Node.js, the CLI, HTTP and as an MCP tool, all generated from one spec.</td>
    <td width="33%" valign="top"><b>Phones anywhere</b><br>The phone connects out to your PC, so it works on the same Wi-Fi or on mobile data through a tunnel or a relay you run. Every line is encrypted end to end.</td>
  </tr>
</table>

## What people use it for

* **Testing your own app** on real phones, including flows that cross into other apps, such as a login with a code from a text message.
* **A shelf of phones** running the same routine every day, each through its own network or proxy.
* **Giving an AI agent hands**: through MCP, Claude, ChatGPT, Cursor and other agents can look at a phone screen and act on it.
* **Small personal automations**, such as turning Wi-Fi off at night or collecting a value from an app every hour.

Droidline uses only permissions an ordinary app can get, so a few things are out of reach: see [What it cannot do](#what-it-cannot-do).

## See it in action

<p align="center">
  <a href="https://droidline.dev"><img src="docs/media/demo-en.webp" alt="A script sends six lines to a phone: launch the demo app, close the ad, type an email, tick Keep me signed in, tap Log in, and wait for the main screen. Each line gets a reply with how the tap was delivered, and the phone screen changes to match." width="720"></a><br>
  <sub>Try the same demo in your browser, and pick elements on a simulated screen, on <a href="https://droidline.dev">droidline.dev</a></sub>
</p>

## Quick start

You need a PC (Windows, macOS or Linux) and an Android phone with Android 9 or later, on the same Wi-Fi for a first try. The [installation guide](https://droidline.dev/docs/install/) walks through each step with screenshots.

1. **Run the server on your PC.** Download the `droidline` archive for your system from [Releases](https://github.com/KnifeLemon/Droidline/releases/latest), put `droidline` on your `PATH`, and start it. Leave it running.

   ```bash
   droidline serve
   ```

2. **Install the app on the phone.** Download `droidline-agent.apk` from the same release page and open it. On the app's **Setup** tab, turn on the accessibility service, the Droidline keyboard, notifications and unrestricted battery use. On Android 13 and later, allow **restricted settings** for the app first; the app shows where.

3. **Pair them.** Run this on the PC and scan the QR code with the app's **Pair** tab:

   ```bash
   droidline pair
   ```

   No camera? Tap **Pair on this Wi-Fi** in the app and type the 6-digit code it shows: `droidline pair 482913`.

4. **Send a command.**

   ```bash
   droidline launch com.android.settings
   droidline touch text "Network & internet"
   ```

No phone at hand? `droidline-fakephone`, included in every release, simulates one with a small demo app. The [first-script tutorial](https://droidline.dev/docs/tutorial/) builds a complete login script against it.

## Use it from your language

Every interface talks to `droidline serve` on `localho