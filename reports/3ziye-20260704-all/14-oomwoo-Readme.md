<div align="center">

# OOMWOO

**The open-source robot vacuum you build yourself.**

Clean well · Raspberry Pi · ROS2 · Home Assistant · 2D LiDAR · 3D printed · ESP32 · Arduino

![License](https://img.shields.io/badge/license-Apache--2.0-blue)
![Status](https://img.shields.io/badge/status-early%20development-orange)

</div>

## What is this?

OOMWOO is an **open-source home robot vacuum** you can build yourself, made for the
Raspberry Pi, ROS2, Home Assistant, and 3D-printing communities. It uses an
affordable 2D LiDAR to map your home and navigate on its own. Local, no
cloud required for regular functionality, no vendor lock-in. Follow the [community newsletter](https://stats.sender.net/forms/bo2rAK/view).

Reference design images - this is approximately how the finished design will look:

![Reference robot vacuum cleaner top](./assets/vacuum_model_top.webp)
![Reference robot vacuum cleaner bottom](./assets/vacuum_model_bottom.webp)
![Reference robot vacuum cleaner - top cover removed](https://github.com/makerspet/oomwoo/blob/main/assets/vacuum-no-top-back.webp)

## Goals

- Affordable, fully open hardware, software and firmware
- Home appliance product quality - not a throwaway build
- Easy to build, with step-by-step zero-to-hero instructions
- 2D LiDAR mapping and autonomous navigation (ROS2 / Nav2)
- Native Home Assistant integration for local control
- 3D-printable, documented, and hackable chassis
- Buildable from parts you source yourself
- Local, no cloud required for regular functionality
- Optional extra functionality when connected cloud
- Apps on top of ROS2 to customize vacuum operation
- Stretch goal: App store
- Stretch goal: LeRobot integration, OpenClaw

** v0 target: bare-bones build:

- 3D-printed chassis
- ROS2 Gazebo sim
- LiDAR with manual SLAM
- ROS2 on Raspberry Pi 5 AND/OR ESP32 running micro-ROS with ROS2 on local PC - decision TBD

Open Source Deliverables:

- [ ] [Bill of materials (BoM)](BOM.md)
- [ ] 3D-printable files
- [ ] ROS2 packages
- [ ] Firmware
- [ ] Motor drivers and sensors PCB
- [ ] [Build, setup, bringup and troubleshooting instructions](BUILD_INSTRUCTIONS.md)
- [ ] Demo video(s)

## Build one

> **Status: design / RFC stage.** Step-by-step build instructions don't exist yet —
> they arrive once the first BoM and parts are validated (**first BoM targeted ~mid-July**).

- 📋 **[Bill of Materials (BoM)](BOM.md)** — work-in-progress parts list + budget target
- 🛠️ **[Build Instructions](BUILD_INSTRUCTIONS.md)** — placeholder for now; how to follow along

Full build docs and a complete BoM are on the way, with the goal that you can
source every part yourself.

## Contributing

Would you like to contribute? See [CONTRIBUTING](docs/CONTRIBUTING.md) for the full guide.

OOMWOO is organized to built by the community, massively **in parallel**.
The vacuum and its software are subdivided into [modules](#requests-for-contributions), see list below.

A volunteer picks whatever module she wants, works on that module whenever she wants,
submits her contribution as a PR under contributions/module-name/<her-github-username>.

Multiple developers are welcome to work on the same module.
The best solution for each module surfaces for over time, with the project master having the last call.

1. Pick a contribution from the [list below](#requests-for-contributions).
2. [Let us know](https://github.com/makerspet/oomwoo/discussions) you're working on it and your progress.
3. Check [ARCHITECTURE.md](docs/ARCHITECTURE.md) for the system design and interfaces.
4. Say hi on [Discord](https://discord.gg/3y2JKz5T25)

Follow us building in public:

- Reddit: build-in-public home at [r/ArduinoAndRobotics](https://www.reddit.com/r/ArduinoAndRobotics/)
- YouTube: [build-in-public channel](https://www.youtube.com/@makerspet)
- X: [@0OMWO0](https://x.com/@0OMWO0)
- [Community newsletter](https://stats.sender.net/forms/bo2rAK/view).

## How the RFCs fit together

The modules can be worked on **in parallel**, but some build on others. An arrow
**A → B means "B builds on A"** — green modules are ready now; amber modules are
unblocked once their parents land; the blue one needs real hardware; grey modules are
**on hold**. `source-3d-models` and `part-specs` are ready now; the mechanical **design**
modules (`dust-bin`, `vacuum-fan`) are on hold pending sourced parts + a 3D
reference-design sketch.

```mermaid
flowchart TD
    URDF["urdf-gazebo-sim"]

    CM["clean-and-map"]
    NL["nav-localize"]
    DC["dock-cycle"]
    RS["recovery-safety"]
    FC["floor-care"]
    CJ["cleaning-jobs"]

    LR["live-robot-bringup"]

    DB["dust-bin"]
    VF["vacuum-fan"]
    SM["source-3d-models"]
    SP["part-specs"]

    URDF --> CM
    URDF --> RS
    CM --> NL
    CM --> FC
    NL --> DC
    CM --> CJ
    NL --> CJ
    DC --> CJ
    CM --> LR
    NL --> LR
    DC --> LR
    RS --> LR
    FC --> LR
    CJ --> LR

    classDef ready fill:#d4edda,stroke:#28a745,color:#155724;
    classDef blocked fill:#fff3cd,stroke: