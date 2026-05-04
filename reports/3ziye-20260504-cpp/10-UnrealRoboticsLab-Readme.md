[![Documentation](https://img.shields.io/badge/Documentation-blue.svg)](https://urlab-sim.github.io/UnrealRoboticsLab/)
[![arXiv](https://img.shields.io/badge/arXiv-2504.14135-b31b1b.svg)](https://arxiv.org/abs/2504.14135)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![MuJoCo](https://img.shields.io/badge/MuJoCo-3.7+-green.svg)](https://github.com/google-deepmind/mujoco)
[![Unreal Engine](https://img.shields.io/badge/Unreal_Engine-5.7+-black.svg)](https://www.unrealengine.com)

# URLab -- MuJoCo Physics in Unreal Engine

![URLab](docs/images/hero.png)

URLab (Unreal Robotics Lab) is an Unreal Engine 5 plugin that embeds the [MuJoCo](https://github.com/google-deepmind/mujoco) physics engine directly into the editor and runtime. Drag-and-drop MJCF XML import, a component-based architecture that maps 1:1 to MuJoCo elements, the full MuJoCo C API accessible from C++ and Blueprints, ZMQ networking for external control, Python policy integration, 40+ sensor types, 8 actuator types, debug visualization, and a record/replay system.

## When To Use URLab

- You need photorealistic rendering with accurate contact physics (sim-to-real transfer, synthetic data generation).
- You want to control MuJoCo robots from Python or ROS 2 while rendering in Unreal Engine.
- You want Unreal's ecosystem (Blueprints, Sequencer, Marketplace assets, Niagara) with physics-accurate robots.

## Quick Start

1. Clone into your project's `Plugins/` folder. Build third-party libraries once (`third_party/build_all.ps1`).
2. Drag an MJCF `.xml` file into the Content Browser. The importer creates a complete Articulation Blueprint.
3. Place an `AAMjManager` in your level. Place the generated Blueprint.
4. Hit Play. MuJoCo runs on an async physics thread; Unreal handles rendering.

See the [Getting Started](https://urlab-sim.github.io/UnrealRoboticsLab/getting_started/) guide for a full walkthrough.

## Key Features

- **MJCF Import** -- drag-and-drop `.xml`, builds full body/joint/actuator/sensor tree as an Articulation Blueprint.
- **Quick Convert** -- attach `UMjQuickConvertComponent` to any Static Mesh and it becomes a MuJoCo physics body. No XML needed.
- **40+ sensors, 8 actuator types, 4 joint types** -- position, velocity, motor, muscle, damper, adhesion, cylinder, general actuators; hinge, slide, ball, free joints; accelerometer, gyro, force/torque, touch, rangefinder, frame tracking, camera, and more.
- **ZMQ networking** -- stream sensor data out and receive actuator commands in via PUB/SUB sockets. Connect Python, ROS 2, or any ZMQ-speaking process.
- **Debug visualization** -- toggle contact forces, joint axes, collision geometry (articulations and Quick Convert separately), all via hotkeys.
- **Record and replay** -- capture trajectories, play back frame-by-frame, CSV import, snapshot/restore full simulation state.
- **Blueprint API** -- compile, reset, step, read sensors, set controls, capture snapshots, toggle debug drawing, all from Blueprint.
- **MjSimulate dashboard** -- in-editor widget with physics parameter tuning, actuator sliders, sensor readouts, live camera feeds.
- **Keyframe system** -- reset to named keyframes, hold keyframe poses (via ctrl or direct qpos injection), per-articulation dropdown in the dashboard.
- **Possess and walk** -- possess any articulation as a Pawn, WASD control with twist velocity commands over ZMQ.
- **Cinematic tools** -- orbit camera, keyframe camera with waypoint paths, impulse launchers for perturbation testing.
- **CoACD decomposition** -- one-click convex decomposition for non-convex meshes, cached by content hash.
- **Heightfield terrain** -- convert Unreal Landscape actors into MuJoCo heightfields.

See the [full documentation](https://urlab-sim.github.io/UnrealRoboticsLab/) for details.

## Python Integration

URLab communicates with external systems over ZMQ. The companion package [**urlab_bridge**](https://urlab-sim.github.io/UnrealRoboticsLab/guides/policy_bridge/) (separate repository, same organization) provides Python middleware for remote control, RL policy deployment, sensor monitoring, and ROS 2 bridging.

## Requirements

- **Unreal Engine 5.7+** -- Windows binary or Linux binary distribution.
- **Windows (Win64)** with **Visual Studio 2022**, or **Linux (x86_64)** with UE's bundled clang. See [Linux setup](docs/linux_setup.md) for the Linux-specific build flow.
- **MuJoCo 3.7+** -- bundled in `third_party/`, built from source.
- **CMake 3.24+** -- for building third-party libraries.
- **Python 3.11+** -- optional, for `urlab_bridge` policies.
- **[uv](https://github.com/astral-sh/uv)** -- optional, for Python dependency management.

## Installation

> **⚠️ Critical:** This is a C++ plugin. You **must** be using a C++ project. If your project is Blueprints-only, add a dummy C++ class via *Tools > New C++ Class* before starting.

### 1. Clone the Plugin
Clone this repo into your project's `Plugins` folder:
```bash
cd "YourProject/Plugins"
