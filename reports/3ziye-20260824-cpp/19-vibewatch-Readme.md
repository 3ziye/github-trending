# Vibe Watch

**English** | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

[![Firmware build](https://github.com/GOROman/vibewatch/actions/workflows/firmware.yml/badge.svg)](https://github.com/GOROman/vibewatch/actions/workflows/firmware.yml)

**A wearable, tactile control surface for AI-assisted Vibe Coding—built around the M5Stack StopWatch.**

Created for the [M5Stack Global Innovation Contest 2026](https://m5stack.com/global-innovation-contest-2026).

![Vibe Watch worn on the wrist, showing its tactile Vibe Coding action interface](docs/images/vibe-watch-hero.jpg)

## Video Demo

[![Watch the Vibe Watch video demo](https://img.youtube.com/vi/Wta_rQDcs74/maxresdefault.jpg)](https://www.youtube.com/watch?v=Wta_rQDcs74)

[Watch on YouTube](https://www.youtube.com/watch?v=Wta_rQDcs74)

## One Glance. One Action. Stay in the Flow.

Vibe Watch moves frequent AI-agent interactions away from crowded desktop UI and onto a dedicated wireless device. It keeps six agent states visible at a glance, makes approve/reject decisions physical, and puts Plan mode, assistant access, and push-to-talk on the wrist.

The goal is simple: spend less attention operating the AI and more attention creating with it.

## Why I Built It

Running multiple AI-agent sessions in parallel has become normal in Vibe Coding. That creates a new interaction problem: I want to know the instant a task finishes, select the right session, and speak the next prompt without searching across windows or returning to the keyboard.

After purchasing an [OpenAI Codex Micro](https://learn.chatgpt.com/docs/features/codex-micro), I was inspired by the idea of dedicated hardware for AI coding. I believed the experience could become even smaller, more glanceable, and more expressive by combining a round display with direct controls, motion, sound, haptics, and voice input. That idea became Vibe Watch: a wearable AI cockpit for parallel sessions.

## The Experience

The main **Agent layer** arranges six live agent indicators around the circular screen. Host-provided color, brightness, and animation communicate activity, while a fast spring motion moves the selection ring from one agent to the next.

Pressing both hardware buttons transforms the interface into the **Action layer**:

| Control | Experience |
|---|---|
| **FAST** | Triggers a quick action |
| **NG / OK** | Rejects or approves with distinct square-wave sounds and haptics |
| **PLAN** | Toggles Plan mode with a visible state change |
| **AI** | Invokes the assistant |
| **Center microphone** | Provides hold-to-talk control |

The orange left button maps to NG and the blue right button maps to OK. Colored rails visually join each physical button to its on-screen action, making the relationship understandable without instructions.

## Interface Gallery

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/images/vibe-watch-startup.jpg" alt="Vibe Watch animated startup screen with version and battery level"><br>
      <strong>Purpose-built startup</strong><br>
      A fading identity, original chiptune, and animated measured battery level.
    </td>
    <td width="50%" valign="top">
      <img src="docs/images/vibe-watch-agent-layer.jpg" alt="Vibe Watch Agent layer showing six parallel AI sessions"><br>
      <strong>Six parallel agents</strong><br>
      Live state and selection remain visible without covering the coding workspace.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/images/vibe-watch-action-layer.jpg" alt="Vibe Watch Action layer showing FAST, NG, OK, PLAN, AI, and push-to-talk"><br>
      <strong>Action layer</strong><br>
      FAST, NG, OK, PLAN, AI, and push-to-talk become immediate wrist controls.
    </td>
    <td width="50%" valign="top">
      <img src="docs/images/vibe-watch-settings.jpg" alt="Vibe Watch settings for Bluetooth pairing, sound, and vibration"><br>
      <strong>On-device settings</strong><br>
      Pairing, sound volume, vibration strength, and state-change haptics stay on the watch.
    </td>
  </tr>
</table>

## Designed as One Multisensory Interface

Vibe Watch is not a macro pad with a decorative screen. Its visual motion, audio cues, vibration, touch controls, and physical buttons all describe the same interaction state.

- A rising square-wave phrase confirms **OK**; a descending phrase confirms **NG**.
- Pairing success is acknowledged with both sound and vibration.
- Agent-state updates can signal silently through adjustable haptics.
- Sound volume, vibration strength, and state-change vibration are configurable on-device and retained after restart.

## How the M5Stack Controller Is Used

The M5Stack StopWatch is the complete product interface—not a passive display attached to another controller.

- Its **ESP32-S3** runs the UI, preferences, battery monitoring, and Bluetooth Low Energy HID communication.
- The **466 × 466 round touchscreen** presents the six-agent spatial interface and action controls.
- The 