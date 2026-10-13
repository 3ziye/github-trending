<p align="center">
  <img src="logo/TECHO5_logo.png" alt="TECHO5" width="220">
</p>

<h3 align="center">Your Echo Show 5, rebuilt. Linux inside, Home Assistant in charge, no Amazon cloud.</h3>

<p align="center">
  <a href="https://github.com/HuskerMinion/techo5/releases/latest"><img src="https://img.shields.io/github/v/release/HuskerMinion/techo5?label=release&color=e9a23b" alt="Latest release"></a>
  <img src="https://img.shields.io/badge/Linux-Alpine-0D597F?logo=alpinelinux&logoColor=white" alt="Alpine Linux">
  <img src="https://img.shields.io/badge/Android-none-3a2c22" alt="No Android">
  <img src="https://img.shields.io/badge/Alexa-none-3a2c22" alt="No Alexa">
  <img src="https://img.shields.io/badge/Home%20Assistant-ESPHome%20API-41BDF5?logo=homeassistant&logoColor=white" alt="Home Assistant">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license"></a>
  <a href="https://buymeacoffee.com/huskerminion"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?logo=buymeacoffee&logoColor=black" alt="Buy Me a Coffee"></a>
</p>

<p align="center">
  <a href="#whats-new">What's new</a> ·
  <a href="#built-on-echolocal">Built on EchoLocal</a> ·
  <a href="#why-techo5">Why</a> ·
  <a href="#screenshots">Screenshots</a> ·
  <a href="#stock-vs-techo5">Stock vs TECHO5</a> ·
  <a href="#install">Install</a> ·
  <a href="#under-the-hood">Under the hood</a> ·
  <a href="#made-possible-by">Credits</a> ·
  <a href="https://github.com/HuskerMinion/techo5-dot">TECHO5 Dot</a> ·
  <a href="https://github.com/HuskerMinion/techo5-spot">TECHO5 Spot</a>
</p>

---

**TECHO5** (Tech Echo 5) is open firmware for the **Amazon Echo Show 5**. It replaces Android and
Alexa with a small Alpine Linux image and one Go daemon, turning the Show into a fast, private Home
Assistant voice satellite with a touch screen of its own.

**Every Echo that can be unlocked now runs it.** The bootloader exploit these devices are opened with,
[amonet](https://github.com/R0rt1z2/amonet), reaches five Amazon Echos. All five run the same daemon:

| Device | Model | Repository | Status |
|---|---|---|---|
| **Echo Show 5, 2nd gen** (2021, `cronos`) | C76N82 | this one | In daily use |
| **Echo Show 5, 1st gen** (2019, `checkers`) | H23K37 | this one, same binary; hardware notes in [techo5-checkers](https://github.com/HuskerMinion/techo5-checkers) | Working, tested end to end on one unit |
| **Echo Show 8, 1st gen** (2019, `crown`) | C7H6N3 | this one, same binary | Working on one unit, the newest port |
| **Echo Spot, 1st gen** (2017, `rook`) | VN94DQ | [TECHO5 Spot](https://github.com/HuskerMinion/techo5-spot) | In daily use |
| **Echo Dot, 2nd gen** (2016, `biscuit`) | RS03QR | [TECHO5 Dot](https://github.com/HuskerMinion/techo5-dot) | In daily use |

Every other device amonet opens is a Fire tablet. No Echo made after 2021 has a public unlock, so this
is the whole family as it stands, not a roadmap.

<p align="center">
  <img src="docs/screenshots/sunrise-show.gif" alt="The screen turning into a sunrise over the twenty minutes before an alarm: a dark red sky warming through orange to a pale gold, a sun climbing into it, the time readable throughout" width="560">
</p>

<p align="center">
  <em><strong>Waking to light.</strong> For up to half an hour before an alarm the screen becomes a
  dawn, on a curve that does most of its work near the end. Every frame here is drawn by the code
  the device draws with.</em>
</p>

## What's new

The bigger changes of late September and early October 2026. Every release lists the rest.

<table>
<tr>
<td width="50%"><a href="docs/screenshots/show8/dashboard-drawn.png"><img src="docs/screenshots/show8/dashboard-drawn.png" alt="A dashboard drawn by the Echo Show 8 itself: tiles for a lamp, a fan, a scene, a porch light, a lock, the heat and the weather"></a></td>
<td width="50%"><a href="docs/screenshots/show8/dashboard-streamed.png"><img src="docs/screenshots/show8/dashboard-streamed.png" alt="The same dashboard streamed to the Echo Show 8 exactly as Home Assistant draws it, with a five-day forecast"></a></td>
</tr>
<tr>
<td><strong>Drawn on the device</strong>: instant, no server</td>
<td><strong>Streamed</strong>: exactly as Home Assistant draws it</td>
</tr>
</table>

**Home Assistant dashboards on the screen** (v0.9.0). The Echo Show and the Echo Spot can show a
dashboard as a page you swipe in from the left edge of the clock (on the Spot, from the ring menu),
or in place of the clock when nothing else is on the screen. There are two ways, picked per device in
Home Assistant:

- **Drawn on the device.** The device reads the dashboard's cards and draws them itself, in your
  theme's colors: tiles you can tap or slide for brightness, position and temperature, rows with
  switches, graphs, gauges, pictures and more. Taps are instant and nothing else is needed. With no
  dashboard picked, it builds a Rooms dashboard from your Home Assistant areas.
- **Streamed.** [das