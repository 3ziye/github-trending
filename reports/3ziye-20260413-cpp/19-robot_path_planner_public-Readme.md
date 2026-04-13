<div align="center">
    <img src="./images/video.gif" width="150" alt="Program Logo GIF" />
    <br />
    <img src="./images/title.png" width="420" alt="robot_path_planner_public" />
    <img src="./images/kouhao.png" width="520" alt="PLAN BY BLOCKS — SNAP &amp; GO" />
    <br />
</div>

<p align="center">
    <a href="https://ubuntu.com/" target="_blank">
        <img alt="Ubuntu 20.04" src="https://img.shields.io/badge/Ubuntu-20.04-orange?style=flat-square&logo=ubuntu&logoColor=white" />
    </a>
    <a href="http://wiki.ros.org/noetic" target="_blank">
        <img alt="ROS Noetic" src="https://img.shields.io/badge/ROS-Noetic-blue?style=flat-square&logo=ros&logoColor=white" />
    </a>
    <a href="https://github.com/SYS-zdk/robot_path_planner_public/actions/workflows/ci-noetic.yml" target="_blank">
        <img alt="CI (Noetic)" src="https://img.shields.io/github/actions/workflow/status/SYS-zdk/robot_path_planner_public/ci-noetic.yml?branch=main&style=flat-square&logo=githubactions&logoColor=white" />
    </a>
    <a href="https://github.com/SYS-zdk/robot_path_planner_public/blob/main/LICENSE" target="_blank">
        <img alt="License" src="https://img.shields.io/github/license/SYS-zdk/robot_path_planner_public?style=flat-square" />
    </a>
    <a href="https://github.com/SYS-zdk/robot_path_planner_public/commits/main" target="_blank">
        <img alt="Last commit" src="https://img.shields.io/github/last-commit/SYS-zdk/robot_path_planner_public?style=flat-square&logo=git&logoColor=white" />
    </a>
    <a href="https://github.com/SYS-zdk/robot_path_planner_public" target="_blank">
        <img alt="Top language" src="https://img.shields.io/github/languages/top/SYS-zdk/robot_path_planner_public?style=flat-square" />
    </a>
    <a href="https://github.com/SYS-zdk/robot_path_planner_public/stargazers" target="_blank">
        <img alt="Stars" src="https://img.shields.io/github/stars/SYS-zdk/robot_path_planner_public?style=flat-square&logo=github" />
    </a>
    <a href="https://github.com/SYS-zdk/robot_path_planner_public/forks" target="_blank">
        <img alt="Forks" src="https://img.shields.io/github/forks/SYS-zdk/robot_path_planner_public?style=flat-square&logo=github" />
    </a>
    <a href="https://github.com/SYS-zdk/robot_path_planner_public/issues" target="_blank">
        <img alt="Issues" src="https://img.shields.io/github/issues/SYS-zdk/robot_path_planner_public?style=flat-square" />
    </a>
    <a href="https://github.com/SYS-zdk/robot_path_planner_public/pulls" target="_blank">
        <img alt="PRs" src="https://img.shields.io/github/issues-pr/SYS-zdk/robot_path_planner_public?style=flat-square" />
    </a>
    <a href="https://space.bilibili.com/17052261" target="_blank">
        <img alt="Bilibili" src="https://img.shields.io/badge/Bilibili-个人主页-00A1D6?style=flat-square&logo=bilibili&logoColor=white" />
    </a>
</p>

## 1. Environment Requirements

- Ubuntu 20.04 LTS (Recommended)
- ROS Noetic (Desktop-Full recommended)
- Toolchain: GCC/G++ (>=9), CMake (>=3.16), Python 3
- Package managers:
    - `rosdep` for ROS package dependencies
    - Conan (1.x) for third-party C/C++ libraries under `3rd/` (e.g., OSQP, Ceres, and transitive glog/gflags/libunwind)

> Most ROS dependencies are resolved via `rosdep install --from-paths src --ignore-src -r -y` (see Section 6).

## 2. Project Overview

<p align="center">
    <img src="./images/second.png" width="400" alt="Organization" />
  <br />
  <em>Robot</em>
</p>

> Note: This repository is developed for experiments and secondary development on top of the open-source framework [ros_motion_planning](https://github.com/ai-winter/ros_motion_planning). It is maintained in the open following community best practices and is still under active development; issues and PRs are welcome.

This repository is a modular, reproducible workspace for mobile robot navigation and motion planning (ROS1/Noetic). Its core design is **“modules as building blocks”**: global planners, local planners/controllers, costmap layers, and trajectory optimizers are packaged as interchangeable components with unified wiring, configuration templates, and simulation assets.

Instead of spending time re-implementing the same wheels (or hunting for scattered resources), you can **assemble**, **swap**, and **benchmark** algorithms inside one consistent platform:

- Build bigger systems by composing smaller modules ("LEGO-like" navigation stack assembly).
- Run apples-to-apples comparisons by changing a single ID + YAML, keeping the rest of the stack constant.
- Reproduce experiments and iterate on secondary development with less setup friction.

In addition, it includes a set of engineering-driven extensions at both the **module** level and the **system** level (see **Module Gallery** and **Core Innovations** below):

- Module-level (building blocks): multiple global planners / local planners / controllers / layers / optimizers that can be composed as needed, with implementa