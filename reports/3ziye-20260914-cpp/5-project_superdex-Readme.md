# Project SuperDex

> A unified platform for dexterous manipulation research

**Welcome to Project SuperDex.**

SuperDex brings together a purpose-built physics engine, robotics authoring
tools, and a scalable reinforcement learning interface in a unified simulation
platform, with VR-based teleoperation and additional capabilities planned for
future releases.

Visit the [Project SuperDex website](https://projectsuperdex.com/) for more.

| Threaded Screw | Manipulation |
| :-: | :-: |
| ![Threaded Screw](https://github.com/user-attachments/assets/ddac8a5f-2f72-4ca0-b555-a090513f224a) | ![Manipulation](https://github.com/user-attachments/assets/406ea05e-6117-4b81-8d0a-0d6ae1cbaebd)|

## Building blocks

- **SuperDex Physics** — A contact-first physics engine purpose-built for tactile
  manipulation, and applicable wherever stable contact and accurate sensing
  matter. This is the simulation backbone of Project SuperDex.
- **SuperDex Robotics** — A robotics SDK that provides robot definitions and
  composition, controllers, sensors, actuators, and the framework that
  aggregates them into complete simulation configs.
- **SuperDex Studio** — A lightweight desktop GUI authoring and visualization
  application for creating, editing, and validating the simulation assets —
  robots, meshes, task prefabs, and scenes.
- **SuperDex Lab** — The simulation harness that abstracts the Markov decision
  process and dynamics-constrained-optimization underpinning RL, MPC, and
  system-ID.

---

## Gallery

The following videos were recorded in real-time using SuperDex Teleop (available in Q4 2026).

| Soft Sponge | Fruit Bag |
| :-: | :-: |
| ![Soft Sponge](https://github.com/user-attachments/assets/b19c8848-0e06-42c9-80b2-9c58d81774f7) | ![Fruit Bag](https://github.com/user-attachments/assets/09aabf80-9e43-4855-99a6-c7bcac0c974b) |
| Cereal Box | Rope Braid |
| ![Cereal Box](https://github.com/user-attachments/assets/8827c424-0062-4c93-8a73-1586854674c2) | ![Rope Braid](https://github.com/user-attachments/assets/50531ef6-1db7-48a8-aa27-f935665ed723) |
| Contact Viz | Puzzle Cube |
| ![Contact Viz](https://github.com/user-attachments/assets/03601744-fb9d-4c2e-aa1c-a25294df3274) | ![Puzzle Cube](https://github.com/user-attachments/assets/6afa67b6-787d-401e-803b-a7a713c76220) |
| Compose Bots  | Soft Fingertips |
| ![Compose Bots](https://github.com/user-attachments/assets/bca2d36d-5ddd-4aa3-9863-e4903521b6b0) | ![Soft Fingertips](https://github.com/user-attachments/assets/ed08d3ab-af15-47a2-b7e2-d9b125e61b78) |

---

## SuperDex Studio

SuperDex Studio is the desktop application where you turn raw CAD and robot descriptions into native SuperDex Assets - bots, prefabs, and scenes. This is the GUI toolkit of Project SuperDex.

Click to learn more about [SuperDex Studio](https://projectsuperdex.com/studio/).

| SuperDex Studio | Apply Forces |
| :-: | :-: |
| ![SuperDex Studio](https://github.com/user-attachments/assets/4f3ef7df-9c22-4692-bd0b-71f23b4ff3a8) | ![Apply Forces](https://github.com/user-attachments/assets/d746b626-4aab-4a0e-8bc7-98c65c29af68) |

---

## SuperDex Lab (early preview)

SuperDex Lab connects simulation and policy development through a Gymnasium-style API for reinforcement learning. It is currently in early preview and will receive substantial improvements.

Click to learn more about [SuperDex Lab](https://projectsuperdex.com/lab/).

![Reinforcement Learning](https://github.com/user-attachments/assets/87baf336-9d57-4528-a1cf-a5382fa7a0d3)

---

## Q4 2026: SuperDex Teleop

SuperDex Teleop is the next major module coming to Project SuperDex. Initial components for Unreal Engine 5 based virtual teleoperation will be available in Q4 2026.

![Ben Virtual Teleop](https://github.com/user-attachments/assets/08a742a1-b7e5-4f77-a69a-8e24a761048e)

SuperDex Teleop runs natively on-device on Quest 3. No remote PC, no streaming. Includes support for both hand tracking and controllers including mixed mode. Runs in pure C++ for low-latency, real-time, scalable virtual teleop.

![Android Teleop](https://github.com/user-attachments/assets/53639e05-5f6c-4cc6-b693-b3ae6e87ff2f)

---

## Requirements
* **OS:** Linux (x86_64), Windows (x86_64), macOS (ARM)
* **Python** 3.12
   - Pre-built wheels are currently provided only for Python3.12. More flexible abi3 wheels will be available in a future release.

## Get the Source Code and Examples

* Clone: `git clone --branch stable https://github.com/facebookresearch/project_superdex.git`
    * Note: `stable` branch always matches latest published release

## Quick Start (Python)

Project SuperDex has first-class support for Python across the board. The quickest way to get started is with `uv` and `pypi` wheels.

1. Install pre-requisites
    * [uv](https://docs.astral.sh/uv/getting-started/installation/)
    * Linux Only: `SuperDex Studio` and `SuperDex Physics Debugger` require an available X11 display (native X11 or XWayland), a graphics driver supporting OpenGL 4.1, and the fol