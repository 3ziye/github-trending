# ShadowAuto

English | [中文](README.zh-CN.md)

ShadowAuto is an open-source Android prototype similar to Doubao Phone. It supports any Android 10 or later device and can likewise implement background silent automation on Android phones. It starts an AI-driven shell process through `adb shell` and `app_process`, launches real Android apps inside an isolated VirtualDisplay, and lets automation run quietly in the background while the physical screen remains usable.

ShadowAuto is not just a click script. It gives the AI a phone-assistant-style loop for understanding and operating the screen: the shell process can read the UiAutomation UI node tree for the virtual display, fall back to offline OCR when accessibility nodes are missing or incomplete, and inject touch, key, clipboard, and text input events into the target display.

The Chinese product name is **隐控**.

## Key Capabilities

- Background silent automation: target apps run inside a VirtualDisplay without occupying the physical screen.
- AI tool-call control: the model repeatedly chooses tools such as tap, input, scroll, back, search, wait, and finish.
- UI node reading: UiAutomation returns windows, node trees, editable fields, and actionable targets for the target display.
- OCR visual fallback: Paddle Lite OCR reads visible text and bounding boxes on self-rendered or accessibility-opaque pages.
- Display-targeted input injection: touch, key, clipboard, and IME operations are injected into the virtual display, not the main display.
- Real-time virtual screen streaming: the VirtualDisplay is streamed to the controller app as H.264 video.
- Parallel tasks: the controller app can create multiple independent task pages, each with its own goal, screen stream, and progress log.

## Demo Video

<video src="shadowauto.mp4" controls="controls" style="max-width: 100%;"></video>

If the current page cannot play the embedded video, open [shadowauto.mp4](shadowauto.mp4).

## Technical Deep Dive

- [Android Virtual Display and AI Background Automation](docs/android-virtual-display-ai-automation.en.md)
- [Android 虚拟投屏与 AI 后台静默自动化实践](docs/android-virtual-display-ai-automation.md) (Chinese)

## Project Layout

- `android-shell`: shell-side automation process started by `app_process`. It owns VirtualDisplay creation, app launching, UI node reading, OCR fallback, input injection, clipboard operations, AI tool-call loop, JSON-RPC, logs, and H.264 virtual screen streaming.
- `controller-app`: Android app used to configure the model, enter automation goals, watch the virtual screen, read progress logs, start tasks, and stop one or all tasks.
- `web-launcher`: Svelte + TangoADB WebUSB launcher. It shows one launch button, lets the user select a device in the browser, uploads the shell APK, OCR files, and controller APK, then starts `app_process`.
- `android-stubs`: compile-only Android hidden API stubs used by the shell module.
- `scripts`: local test helpers.

## Requirements

- Any Android 10 or later device.
- ADB debugging enabled on the target device.
- Shell permission is enough; root is not required.
- JDK 17.
- Node.js and npm for the web launcher.
- Chrome or another WebUSB-capable browser for `web-launcher`.
- An OpenAI-compatible chat-completions endpoint that supports streaming and tool calls.

## Build

Build the shell and controller app:

```sh
./gradlew :android-shell:assembleDebug :controller-app:assembleDebug
```

Sync the latest shell APK and OCR runtime files into the web launcher static directory:

```sh
./gradlew :android-shell:syncWebLauncherArtifacts
```

Install the controller app:

```sh
adb install -r controller-app/build/outputs/apk/debug/controller-app-debug.apk
```

## Start The Shell Process

### Option 1: Browser Launcher

Online launcher: [https://android-notes.github.io/ShadowAuto/](https://android-notes.github.io/ShadowAuto/)

Before connecting, prepare the phone:

- Enable Developer options and USB debugging.
- Some Xiaomi phones also require USB debugging (Security settings).
- On first connection, the phone may show an Allow USB debugging prompt; tap Allow on the phone.
- When installing the controller app, tap Allow install if the phone shows an install prompt.
- After installation, configure an API key in the ShadowAuto app before using phone automation.
- Developer option references: [Xiaomi](https://jingyan.baidu.com/article/ce436649ca6c877773afd3e2.html), [Huawei](https://jingyan.baidu.com/article/a378c960e87118b3282830bc.html), [OPPO](https://jingyan.baidu.com/article/cb5d6105b0936a005d2fe052.html), [VIVO](https://jingyan.baidu.com/article/335530da406f4358cb41c3b4.html).

You can also run it locally:

```sh
cd web-launcher
npm install
npm run dev
```

Open the printed local URL in Chrome, click **Start ShadowAuto Assistant**, select the Android device, and authorize ADB if Android asks.

If the browser reports that the device is already in use, close Android Studio and kill adb, then retry:

```sh
adb kill-server
```

### Option 2