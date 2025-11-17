# FUEL+PX4+gazebo

## Overview
This repository ports the **single UAV autonomous exploration** system from the original [FUEL](https://github.com/HKUST-Aerial-Robotics/FUEL) implementation to the **PX4** simulation environment. The original open-source code targeted a simplified simulator, which made direct deployment to real UAVs challenging. To bridge this gap, we **modified several ROS topics** and integrated a **PX4 flight controller** (via MAVROS), enabling realistic simulation and smoother transition to hardware.

## Key Modifications
All changes from the original implementation are **clearly annotated in the source code**, with inline comments explaining **what changed** and **why** the change was required. At a high level, modifications include:
- Remapping / replacing ROS topics to follow PX4/MAVROS conventions.
- Adding a PX4 controller interface for attitude / velocity setpoints.
- Ensuring compatibility with **PX4 + Gazebo** workflows and launch sequences.
- All modifications compared to the original code are retained **in place** with comments for traceability.

## Simulation Environment
This repository is designed for simulation in **PX4 + Gazebo**. If you want to deploy to a **real UAV**, you only need to update the relevant PX4/MAVROS topics to match your hardware setup. For example, the PX4 attitude setpoint topic used in simulation:
```bash
/mavros/setpoint_raw/attitude
```
can be redirected to the **equivalent topic** used by your real UAV setup.

## Quick Start
A one-command startup script is provided:
```bash
./start.sh
```
This script launches the simulator, MAVROS bridge, and the exploration stack in the correct order.

## Usage Guide
Detailed usage (environment setup, dependencies, calibration, example runs) will be provided soon.
> 🛠️ **Coming soon...**


## Future Work
We plan to create a separate repository that ports the **RACER** framework to the **PX4 + Gazebo** stack. This will extend the current single-UAV pipeline to multi-robot exploration in SITL.

## References
- Original research code (paper implementation):  
  - FUEL: https://github.com/HKUST-Aerial-Robotics/FUEL

## Acknowledgments
We would like to thank the following projects for inspiration and reference implementations:
- FUEL: https://github.com/HKUST-Aerial-Robotics/FUEL
- XTDrone: https://github.com/robin-shaun/XTDrone
- Fast-Exploration: https://github.com/XXLiu-HNU/Fast-Exploration


## License
This project follows the same open-source spirit as the original FUEL repository. Please refer to the original project for specific license terms. If your usage requires a different license, adapt accordingly and include a `LICENSE` file in this repository.

## Citation
If you use this work in academic research, please also cite the original FUEL paper/repository according to their instructions.

