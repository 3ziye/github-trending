<div align="center">

<p>
  <img src="Tutorials/images/simart_wordmark.svg" alt="SimART" width="420">
</p>

<p><strong>An open-source software platform for all-scenario wireless communication and sensing research.</strong></p>

<p>
  <a href="https://arxiv.org/abs/2605.13309">
    <img alt="Paper" src="https://img.shields.io/badge/Paper-arXiv%202605.13309-9F1239?style=for-the-badge&logo=arxiv&logoColor=white&labelColor=0F172A">
  </a>
  <a href="https://kangyan.lat/simart/">
    <img alt="Homepage" src="https://img.shields.io/badge/Homepage-SimART-0E7490?style=for-the-badge&logo=googlechrome&logoColor=white&labelColor=0F172A">
  </a>
  <a href="https://www.bilibili.com/video/BV12e5R6BEqV/">
    <img alt="Demo Video" src="https://img.shields.io/badge/Demo-Bilibili-00A1D6?style=for-the-badge&logo=bilibili&logoColor=white&labelColor=0F172A">
  </a>
</p>

</div>

---

SimART is an open-source software platform for all-scenario wireless communication and sensing research. Built around ROS1, it integrates a C++/Qt/VTK graphical interface, Sionna-based ray tracing and link simulation, AirSim/Unreal Engine live visualization, and rosbag recording and replay tools. It helps users place base stations, visualize trajectories, inspect wireless channel observations, and evaluate beam selection workflows in 3D scenes.

It supports digital-twin scene construction, ROS-based trajectory replay, Sionna data collection, visual network planning, and communication-sensing experiments with simulators such as AirSim and Unreal Engine.

## Contents

- [System Architecture](#system-architecture)
- [Scene Construction and Map Adaptation](#scene-construction-and-map-adaptation)
- [Multimodal Data and CKM](#multimodal-data-and-ckm)
- [Key Features](#key-features)
- [Preview](#preview)
- [Tutorials](#tutorials)
- [Quick Start](#quick-start)
- [Try SimART](#try-simart)
- [Use SimART with UE4 and AirSim](#use-simart-with-ue4-and-airsim)
- [Further Exploration](#8-further-exploration)

## System Architecture

<p align="center">
  <img src="Tutorials/images/system_architecture.png" alt="SimART system architecture" width="100%">
</p>

SimART consists of four functional modules coordinated by ROS:

| Module | Role |
| --- | --- |
| Physics and Sensing Module | Provides platform motion, RGB/depth/semantic cameras, LiDAR, IMU, GPS, and ground-truth poses through ROS-compatible simulators such as AirSim, Gazebo, Isaac Sim, or CARLA. |
| Ray Tracing Module | Uses Sionna RT to compute site-specific propagation paths, delays, angles, Doppler shifts, interaction points, and channel impulse responses. |
| Link and System Module | Uses Sionna SYS to evaluate OFDM, PHY/MAC behavior, multi-antenna links, beamforming codebooks, SINR, BLER, achievable rate, and optimal beam index. |
| CKM Generator | Scans dense receiver grids to generate multi-layer channel knowledge maps for path loss, delay/angular spread, SINR, rate, and beam-selection priors. |

The ray tracing module supports online simulation, offline rosbag replay, and dense grid scan modes. This allows users to visualize propagation during a live session, reproduce experiments from recorded trajectories, or generate CKM layers over a region of interest.

## Scene Construction and Map Adaptation

SimART provides two complementary scene construction pipelines. Both produce a high-fidelity visual scene for physics/sensing and a simplified, material-aware scene for ray tracing, while preserving a shared coordinate frame.

<table>
  <tr>
    <td align="center">
      <img src="Tutorials/images/louvre_map_pipeline.png" alt="Real-world OpenStreetMap based scene construction pipeline" width="100%">
    </td>
  </tr>
  <tr>
    <td align="center"><sub>Real-world map adaptation: OpenStreetMap data are converted into aligned visual and ray-tracing assets.</sub></td>
  </tr>
  <tr>
    <td align="center">
      <img src="Tutorials/images/roadrunner_map_pipeline.png" alt="User-defined RoadRunner scene construction pipeline" width="100%">
    </td>
  </tr>
  <tr>
    <td align="center"><sub>User-defined scene interface: RoadRunner or Unreal Engine scenes are simplified into propagation-ready meshes.</sub></td>
  </tr>
</table>

| Pipeline | Workflow |
| --- | --- |
| Real-world map adaptation | OpenStreetMap extracts provide building footprints, heights, roads, and land-use polygons. OSM2World creates the visual asset for Unreal Engine/AirSim, while Blender exports a Mitsuba/Sionna RT scene with electromagnetic material annotations. |
| User-defined scene interface | RoadRunner, Unreal Engine, or other custom scene assets are imported for physics and sensing. A Blender conversion script removes fine visual details, applies mesh decimation, preserves dominant facades and ground planes, and assigns Sionna RT materials. |

## Multimodal Data and CKM

During a simulation session, every module publishes data under the shared ROS clock. A single rosbag can preserve the complete synchronized session for replay, insp