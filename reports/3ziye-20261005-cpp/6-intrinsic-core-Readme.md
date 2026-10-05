# Intrinsic Core
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Documentation](https://img.shields.io/badge/Intrinsic%20developer%20community-Join%20us-blue.svg)](https://developer.intrinsic.ai)
[![ROS2 Compatibility](https://img.shields.io/badge/ROS2_Compatible-brightgreen.svg)](https://www.ros.org/)

Intrinsic Core™ provides an open, local runtime, SDK, and hardware agnostic, real-time control framework for industrial robotics. The goal is to make it easier and faster to build AI-enabled robotics applications by providing open, foundational building blocks—from simulation and 6-DoF perception to hardware execution.

- A pre-configured, local runtime that standardizes setup, with core robotics capabilities and services integrated to work together.
- Pre-built robotics capabilities, including grasp planning, AI perception, a native digital twin and more - ready to use out of the box.
- Seamless ROS 2 interoperability that bridges modern C++/Bazel development with the broader ROS ecosystem.
- A hardware-agnostic, real-time control framework with a unified hardware abstraction layer to swap robot arms and grippers without driver rewrites.
- An open reference solution built on Intrinsic Core, providing a functional machine tending template with a zero-refactor path from prototype to deployment. [Open Machine Tending Solution](https://github.com/intrinsic-ai/intrinsic-omts)

## Installation and setup

See the [Getting Started guide](https://github.com/intrinsic-ai/intrinsic-core/tree/main/developer_resources/learn/tutorials/getting_started.md) for full installation and setup instructions.

## Intrinsic Core Architecture
![Intrinsic Core Architecture](developer_resources/img/intrinsic_core_architecture.png)

## Intrinsic Core modules

- **intrinsic_runtime**: A pre-configured local execution engine for Intrinsic Core. Packaged as a native k3s containerized environment, it manages process life cycle, event scheduling, and application state synchronization out of the box—giving developers a stable, deterministic execution layer on top of ROS 2 without the need to manually configure low-level system plumbing.

- **intrinsic_control (ICON)**: The real-time motion and hardware coordination engine. It combines kinematics solvers and trajectory interpolation with a deterministic control loop capable of switching controllers within a single cycle based on live sensor feedback. Backed by a standardized Hardware Abstraction Layer (HAL), it enables sensor-driven control across arms, grippers, and fieldbus I/O without hardware lock-in.
- **intrinsic_motion_planning**: The collision-free path generation engine for Intrinsic Core. It provides high-throughput constraint solving across both Cartesian tasks and wide-envelope C-space movements within a unified API. By combining kinematic and workspace limit enforcement with heterogeneous motion blending, it smoothly fuses multi-segment paths with differing velocity and acceleration profiles into a continuous, executable trajectory.
- **intrinsic_perception**: The sensor processing and visual understanding layer for Intrinsic Core. It standardizes camera and point-cloud interfaces while embedding out-of-the-box support for NVIDIA FoundationPose®, providing high-accuracy 6-DoF pose estimation for 3D parts. By eliminating the need to write custom perception pipeline wrappers, it enables robots to dynamically detect, locate, and manipulate un-fixtured parts straight out of the box.
- **intrinsic_inference**: The local machine learning execution engine for Intrinsic Core. It provides the hardware plumbing, model serving infrastructure, and memory management required to run accelerated inference directly on edge. By exposing standardized APIs for vision models—such as NVIDIA FoundationPose®—it streams real-time pose estimation and visual detections into downstream planning and control loops to guide robot manipulation.
- **intrinsic_sdk**: The developer toolkit for extending and building applications with Intrinsic Core. It provides base interfaces, serialization helpers, and data structures to build reusable skills, custom hardware assets, and execution nodes that integrate natively with the digital twin and runtime.
- **intrinsic_apis**: The interface definitions for Intrinsic Core.
- **intrinsic_hardware**: Hardware device drivers, manifests, and service integrations for industrial peripherals.
- **intrinsic_kinematics**: Kinematic modeling and solver library for robotic manipulators.

## Intrinsic Open Machine Tending Solution (OMTS)

Intrinsic Core also includes an open-source Machine Tending reference design [intrinsic-omts](https://github.com/intrinsic-ai/intrinsic-omts) for a real-world machine shop use case, delivering pre-configured assets, skills, and Intrinsic best practices out of the box, to jump-start the development of industrial applications.

## Prerequisites

- Operating system: Ubuntu 24.04 LTS (Noble) or Ubuntu 26.04 LTS (Ubuntu 