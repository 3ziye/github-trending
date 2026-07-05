<div align="center">

# OOMWOO

*Open-source robot vacuum you build yourself.*

Clean well · Raspberry Pi · ROS2 · Home Assistant · 2D LiDAR · 3D printed · ESP32 · Arduino

![License](https://img.shields.io/badge/license-Apache--2.0-blue)
![Status](https://img.shields.io/badge/status-early%20development-orange)

</div>

## What is this?

OOMWOO is an *open-source home robot vacuum* you can build yourself, made for the
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

*v0 target: bare-bones build:*

- 3D-printed chassis
- ROS2 Gazebo sim
- LiDAR with manual SLAM
- ROS2 on Raspberry Pi 5 AND/OR ESP32 running micro-ROS with ROS2 on local PC - decision TBD

Open Source Deliverables:

- [x] [Software development environment](https://github.com/makerspet/oomwoo-install), robot [description package](https://github.com/makerspet/oomwoo-one/) and [tutorials](https://makerspet.com/blog/simulate-oomwoo-one-robot-vacuum-in-gazebo-with-ros-2/) (ROS2)
- [x] Placeholder real [vacuum cleaner](https://github.com/makerspet/proscenic-m6pro) and [tutorials](https://makerspet.com/blog/tutorial-connect-robot-vacuum-cleaner-to-ros-2-proscenic-m6-pro/) (temporary while OOMWOO is being designed)
- [ ] [Bill of materials (BoM)](BOM.md) (in progress)
- [ ] 3D-printable files
- [ ] Firmware
- [ ] Motor drivers and sensors [I/O PCB](https://github.com/makerspet/oomwoo-io-board)
- [ ] Build, setup, bringup and troubleshooting [instructions](BUILD_INSTRUCTIONS.md)
- [ ] Demo video(s)

## Contributing

Would you like to contribute? See [CONTRIBUTING](docs/CONTRIBUTING.md) for the full guide.

OOMWOO is organized to built by the community, massively *in parallel*.
The vacuum and its software are subdivided into [modules](#requests-for-contributions), see list below.

A volunteer picks whatever module she wants, works on that module whenever she wants,
submits her contribution as a PR under contributions/module-name/<her-github-username>.

Multiple developers are welcome to work on the same module.
The best solution for each module surfaces for over time, with the project master having the last call.

1. Pick a contribution from the [list below](#requests-for-contributions).
2. [Let us know](https://github.com/makerspet/oomwoo/discussions) you're working on it and your progress.
3. Check [ARCHITECTURE.md](docs/ARCHITECTURE.md) for the system design and interfaces.

Follow us building in public:

- [Community newsletter](https://stats.sender.net/forms/bo2rAK/view).
- [Discord](https://discord.gg/3y2JKz5T25)
- YouTube: [build-in-public channel](https://www.youtube.com/@makerspet)
- X: [@0OMWO0](https://x.com/@0OMWO0)

## Requests for Contributions

Every module below is *actionable now* — build it against the Gazebo simulation
([oomwoo-one](https://github.com/makerspet/oomwoo-one)) or a real *placeholder robot*
(a [Proscenic M6 Pro connected to ROS2](https://makerspet.com/blog/tutorial-connect-robot-vacuum-cleaner-to-ros-2-proscenic-m6-pro/)),
until OOMWOO hardware is ready. Pick one, tell us in
[Discussions](https://github.com/makerspet/oomwoo/discussions), and open a PR.

| Module | ID | Status | Notes |
|---|---|---|---|
| ROS2 URDF + Gazebo sim | [urdf-gazebo-sim](./contributions/urdf-gazebo-sim) | In progress | Placeholder URDF + Gazebo sim (reference: [oomwoo-one](https://github.com/makerspet/oomwoo-one); [@alvarosamudio](./contributions/urdf-gazebo-sim/alvarosamudio) merged), refined when hardware lands |
| First clean: coverage + mapping + exploration | [clean-and-map](./contributions/clean-and-map) | Ready to start work | Coverage cleaning while SLAM-mapping and exploring |
| Localization & navigation on a known map | [nav-localize](./contributions/nav-localize) | Ready to start work | Nav2 nav, AMCL localization, relocalize when lost,