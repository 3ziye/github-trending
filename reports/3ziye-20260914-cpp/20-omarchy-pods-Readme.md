<h1 align="center">AirPods for Omarchy</h1>

<p align="center">
  Battery for each pod and the case, the listening modes, adaptive noise level, Conversation Awareness, One-Bud ANC and ear detection, drawn in Omarchy's own panel idiom.
</p>

<p align="center">
  <a href="https://omarchyplugins.com/plugin.html?id=io.github.thisisgm.omapods"><img alt="On omarchyplugins.com" src="https://img.shields.io/badge/omarchyplugins.com-listed-8b5cf6"></a>
  <a href="https://github.com/thisisgm/omarchy-pods/tags"><img alt="Latest tag" src="https://img.shields.io/github/v/tag/thisisgm/omarchy-pods?label=version"></a>
</p>

<p align="center">
  <img src="preview.png" alt="The AirPods panel open in the Omarchy bar" width="420">
</p>

## What it shows

- **Battery** for the left pod, the right pod and the case, each with a charging
  and in-ear hint. Nothing else on a Linux box knows these numbers: BlueZ does
  not expose `org.bluez.Battery1` for AirPods.
- **Listening mode**, and only the modes the device actually has. AirPods 1, 2, 3
  and the plain AirPods 4 get no section at all, AirPods Pro 3 dropped Off, and
  Adaptive needs an H2 part that also has noise cancellation, so the panel asks
  the daemon rather than assuming four rows.
- **Adaptive noise level**, shown only while Adaptive is the active mode.
- **Conversation Awareness** on the same models that have Adaptive, and
  **One-Bud ANC** on the ones with a second bud, which is why an AirPods Max 2
  shows the first and not the second.
- **Ear detection**: pause when one pod is out, pause when both are out, or
  never pause.
- **Case lid**, when the case has broadcast its state. Lid state comes from BLE
  advertisements, and the daemon pauses that discovery while the control link is
  up, because discovery running alongside a live link is what the crackle in issue
  26 tracks. So lid state holds its last value for as long as the pods stay
  connected, and the case level may keep refreshing over the control link, as it
  does here, or hold like the lid, as the issue 26 reporter saw. Per-pod battery, ANC and ear detection keep updating
  throughout.
- **A mark that matches the hardware**: stemmed buds, AirPods Pro or AirPods Max,
  chosen from the model the daemon reports. AirPods Max carry no case, so their
  panel drops the case row and shows a single headphone battery.

## Deliberately absent

- **Volume and output device** live in the stock Audio panel, which already
  switches PipeWire sinks. Press `Tab` in this panel to walk to it.
- **Connect, disconnect and forget** live in the stock Bluetooth panel, and in
  `omarchy bluetooth device`.
- **Spatial Audio** has no renderer on Linux, so there is nothing to draw and
  no row for it.
- **Mic mode** is not an AirPods control. macOS applies Voice Isolation to the
  input stream itself, for any microphone, and the AAP protocol carries no mic
  packet. Input mute and input device live in the stock Audio panel.

## Screenshots

The panel is built from the capability keys the daemon publishes, so three
different AirPods give three different panels. Same plugin, same build, nothing
configured differently between them.

| | | |
|:---:|:---:|:---:|
| <img src="docs/panel-model-airpods4.png" alt="AirPods 4 with ANC"><br>**AirPods 4 with ANC**<br>all four modes, and One-Bud ANC to hold them with one pod in | <img src="docs/panel-model-pro3.png" alt="AirPods Pro 3"><br>**AirPods Pro 3**<br>no Off row: the Pro 3 dropped it | <img src="docs/panel-model-max2.png" alt="AirPods Max 2"><br>**AirPods Max 2**<br>one battery, no case, and no One-Bud ANC to offer |

Both AirPods 4 variants say **AirPods 4** in the title, because the name is the
family and the rows underneath are what the unit can actually do. The plain
AirPods 4 has no listening modes at all, so it gets no listening section.

Every screenshot in this section, the Pro 3 included, was made by writing one
status line by hand and photographing the panel that came back. An AirPods Pro 3
is the only pair on hand here, and it would not have posed for all of these
anyway. It works because the panel reads that file and nothing else.

### States

| | |
|:---:|:---:|
| <img src="docs/panel-noise-cancellation.png" alt="Noise Cancellation"><br>Noise Cancellation, both pods in | <img src="docs/panel-adaptive.png" alt="Adaptive"><br>Adaptive, with the noise level and Conversation Awareness on |
| <img src="docs/panel-transparency.png" alt="Transparency"><br>Transparency | <img src="docs/panel-one-bud.png" alt="One pod in the case"><br>One pod in the case, lid open, One-Bud ANC on |
| <img src="docs/panel-in-case.png" alt="Both pods in the case"><br>Both pods charging, lid closed | <img src="docs/panel-daemon-down.png" alt="Daemon not running"><br>librepods not running |

## Requirements

- **The daemon in [`daemon/`](daemon/), built and running.** It ships in this
  repository because nothing packaged will do: upstream librepods and every AUR
  package built from it carry no state fi