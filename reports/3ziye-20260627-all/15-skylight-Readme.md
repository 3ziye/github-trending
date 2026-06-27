<h1 align="center">Skylight</h1>

<p align="center">
  <em>Project the aircraft passing overhead onto your ceiling, in real time - an X-ray through the roof.</em>
</p>

<p align="center">
  <a href="https://skylightceiling.com"><b>🛰️ Get notified when I launch on a crowdfunding platform → skylightceiling.com</b></a>
  <br><sub>A ready-made kit is coming. Join the waitlist for early access &amp; launch pricing.</sub>
</p>

<p align="center">
  <img src="docs/skylight.png" alt="Skylight projected on a ceiling: aircraft, trails, SFO runways and the night sky" width="100%">
</p>

<p align="center">


https://github.com/user-attachments/assets/9256b0eb-cc27-4388-9a4f-0a6c05468304


</p>

Skylight decodes ADS-B from a cheap RTL-SDR radio and renders the planes physically
flying over you onto a ceiling-pointed projector. A jet you'd hear overhead glides
across your ceiling at the same moment - labeled with its airline, type, and where it's
headed. Pure-black background so the projector's rectangle disappears and only the
aircraft (and stars) are lit.

It also draws the **real sky** behind the planes - sun, moon, bright stars and
constellations, and live **satellites including the ISS** - all at their true positions
for your location and time. Tune everything from your phone.

> Reference build is centered on **San Francisco International (SFO)**, but it works
> anywhere - set your location in the control panel and import your airport's runways
> by ICAO/IATA code (worldwide, via OurAirports) and you're flying.

## Features

- **Real-time overhead aircraft** from a local RTL-SDR (sub-second), or from a free web
  API with zero code changes - handy for trying it with no radio.
- **Type-aware glyphs** in a luminous, swept-wing style: widebodies tower over regional
  jets, **helicopters spin their rotors**, turboprops and GA aircraft spin their props.
- **Smooth motion** - interpolates the ~1 Hz fixes to 60 fps by rendering slightly in
  the past and tweening between real positions (no teleporting).
- **Comet trails**, altitude-graded color, and range rings + compass for orientation.
- **The airport** (runways) drawn at its true position, so you watch departures and
  arrivals line up with the runway.
- **Window to elsewhere** - each routed flight shows its destination **city, local time
  there, and miles-to-go**, plus a faint great-circle arc toward where it's headed.
- **Live sky layer** - sun, moon (with phase), bright stars + constellation lines,
  **naked-eye planets**, and **satellites / ISS** computed from TLEs. Scrub time
  forward/back from your phone, or jump straight to the next ISS pass.
- **Phone control panel** - every setting (rotation, theme, palette, filters, sky
  toggles, …) is live-tunable over your LAN and persists across reboots.
- **Optional sky camera** - point a PTZ camera (VISCA-over-IP + RTSP) at the sky and
  Skylight **automatically films the planes it's projecting**: ADS-B-driven pointing
  with latency-compensated lead prediction, a hybrid vision system that locks the plane
  to center, and a confidence-gated zoom ladder that punches in as the lock holds.
  Includes a **TV dashboard** (`/tv.html`) with the live feed + radar inset, and a full
  **debug UI** (`/tracker.html`) with jog pad, target table, and a star-capture
  calibration wizard.
- **Vision that knows a plane from a cloud** - the camera tracker fuses three signals:
  a classical blob detector (distant specks) + a large-object detector (big overhead
  planes), **track-before-detect** that picks the target by how it *moves* through the
  world like ADS-B predicts (clouds are world-static and lose), and an **optional
  neural airplane detector** (YOLOX-Nano ONNX, downloaded at setup) for a semantic
  "is it an airplane?" confirmation. It also **continuously self-calibrates** the mount
  from every locked pass, so the aim re-squares itself over time.
- **Appliance-ready** - boots straight to a full-screen kiosk on a Raspberry Pi 5
  (dual-output: projector + TV dashboard).

## Hardware

| Part | Suggested | Notes |
|---|---|---|
| Receiver | **RTL-SDR Blog V4 + dipole** | The included dipole is plenty - planes are nearly overhead. The **V3 and V5 work identically** (same RTL2832U); if you're buying now, the V4/V5 are the current models. |
| Compute | **Raspberry Pi 5 (8 GB)** | Decode + render. Active cooling for 24/7. See [minimum specs](#minimum-specs) for lighter setups. |
| Projector | A 1080p projector pointed up | Laser (e.g. Optoma GT2100HDR) gives the deepest blacks, but it's overkill - see the budget tip below. |
| Display link | micro-HDMI → HDMI | The Pi 5 uses **micro**-HDMI (not mini). |
| Mount | Rotating 1/4-20 stand, pointed up | Lower the stand for a bigger image; tape **+ a safety tether**. |
| Sky camera *(optional)* | Any **VISCA-over-IP PTZ** with RTSP (e.g. a 4K NDI conference PTZ) | For the auto-filming tracker. **Clamp the base rigidly** - fast slews will walk an unclamped mount and ruin the aim calibrati