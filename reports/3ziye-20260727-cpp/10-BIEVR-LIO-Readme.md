<p align="center">
  <img width=400 src="doc/bievr_final.svg">
</p>


# BIEVR-LIO: Robust LiDAR-Inertial Odometry through Bump-Image-Enhanced Voxel Maps

<p align="center">
<a href="https://patripfr.github.io/bievr-lio/"><img src="https://shieldcn.dev/badge/Project-Page-gray?size=xs" alt="Project Page" /></a>
<a href="https://arxiv.org/abs/2604.14421"><img src="https://shieldcn.dev/badge/arXiv-2604.14421-b31b1b?logo=arxiv&size=xs" alt="arXiv" /></a>
<a href="https://arxiv.org/pdf/2604.14421"><img src="https://shieldcn.dev/badge/Paper-PDF-black?size=xs" alt="Paper PDF" /></a>
<a href="LICENSE"><img src="https://shieldcn.dev/badge/License-BSD--3--Clause-green?size=xs" alt="License: BSD-3-Clause" /></a>
<a href="https://youtu.be/TsDJOdthhNk"><img src="https://shieldcn.dev/badge/YouTube-red?logo=youtube&size=xs" alt="YouTube" /></a>
</p>

<p align="center">
<a href="https://github.com/ethz-asl/BIEVR-LIO/actions/workflows/build_20_04.yaml"><img src="https://shieldcn.dev/github/ethz-asl/BIEVR-LIO/ci.svg?workflow=build_20_04.yaml&label=ROS1%20Noetic&size=xs&variant=outline&mode=light" alt="Ubuntu 20.04 + ROS Noetic Build" /></a>
<a href="https://github.com/ethz-asl/BIEVR-LIO/actions/workflows/build_22_04.yaml"><img src="https://shieldcn.dev/github/ethz-asl/BIEVR-LIO/ci.svg?workflow=build_22_04.yaml&label=ROS2%20Humble&size=xs&variant=outline&mode=light" alt="Ubuntu 22.04 + ROS Humble Build" /></a>
<a href="https://github.com/ethz-asl/BIEVR-LIO/actions/workflows/build_24_04.yaml"><img src="https://shieldcn.dev/github/ethz-asl/BIEVR-LIO/ci.svg?workflow=build_24_04.yaml&label=ROS2%20Jazzy&size=xs&variant=outline&mode=light" alt="Ubuntu 24.04 + ROS Jazzy Build" /></a>
</p>

<p align="center">
  <img width='100%' src="doc/tunnel_detail.png">
</p>

BIEVR-LIO is a robust LiDAR-Inertial Odometry framework that uses a high-resolution,
voxel-wise oriented height image map to exploit subtle geometric variations in
challenging, information-sparse environments.

<details>
<summary><b>Abstract</b></summary>
<br>
Reliable odometry is essential for mobile robots as they increasingly enter more challenging environments, which often contain little information to constrain point cloud registration, resulting in degraded LiDAR–Inertial Odometry (LIO) accuracy or even divergence. To address this, we present BIEVR-LIO, a novel approach designed specifically to exploit subtle variations in the available geometry for improved robustness. We propose a high-resolution map representation that stores surfaces as voxel-wise oriented height images. This representation can directly be used for registration without the calculation of intermediate geometric primitives while still supporting efficient updates. Since informative geometry is often sparsely distributed in the environment, we further propose a map-informed point sampling strategy to focus registration on geometrically informative regions, improving robustness in uninformative environments while reducing computational cost compared to global high-resolution sampling. Experiments across multiple sensors, platforms, and environments demonstrate state-of-the-art performance in well-constrained scenes and substantial improvements in challenging scenarios where baseline methods diverge. Additionally, we demonstrate that the fine-grained geometry captured by BIEVR-LIO can be used for downstream tasks such as elevation mapping for robot locomotion.
</details>

# Setup

The core estimator (`bievr_lio`) is a self-contained, ROS-independent library. On
top of it we provide both a **ROS1** interface (`bievr_lio_ros`) and a **ROS2**
interface (`bievr_lio_ros2`), which live side by side under `interfaces/`.

## Installation

### Dependencies

BIEVR-LIO is intentionally light on dependencies: the core estimator only needs
**[Eigen](https://eigen.tuxfamily.org)** and **[Ceres](http://ceres-solver.org)**.


Build instructions for both ROS versions are below. Each also offers an optional
Docker image for quickly trying out the system without setting up dependencies.

<details>
<summary><b>ROS1</b></summary>
<br>

### For quick testing: Docker

If you just want to try the system out without setting up dependencies, build the
image and drop into a shell inside it:

```bash
cd docker/
./run_docker_ros1.sh -b
```

The `-b` flag builds the image. On subsequent runs you can
omit it to reuse the existing image. Your `~/data` folder is mounted to
`/home/bievr/data` inside the container so you can keep datasets outside the
image.

To open another terminal inside the running container (e.g. to launch a node
and play a bag):

```bash
docker exec -it BIEVR-LIO-ROS1 /bin/bash
```

### Build

Requires [ROS Noetic](https://wiki.ros.org/noetic/Installation/Ubuntu) and
`python3-catkin-tools` (`sudo apt install python3-catkin-tools`).

Create a catkin workspace and clone BIEVR-LIO into it:

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin init
catkin config --extend /opt/ros/noetic
catkin config --cmake-args -DCMA