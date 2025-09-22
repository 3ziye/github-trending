# SplineTrajectory

SplineTrajectory is a high-performance, header-only C++ library for generating smooth, N-dimensional spline trajectories. This library provides **MINCO-equivalent** cubic、quintic and septic spline interpolation with boundary conditions support, making it ideal for robotics, path planning, and trajectory generation applications.

**English** | [中文](README_zh.md)


## Key Features

- **MINCO Equivalent**: Achieves minimum acceleration, jerk, and snap trajectories, just like MINCO.
    
- **High Performance**: Outperforms traditional methods by using a specialized **block tridiagonal matrix solver** (Thomas algorithm) instead of general LU decomposition.
    
- **Template-Based**: Fully templated for **arbitrary dimensions** (1D to ND) with compile-time optimizations.
    
- **Flexible & Efficient**: Supports multiple time specifications, optimized batch evaluation, and provides derivatives (velocity, acceleration, jerk, snap).
    
- **Eigen Integration**: Seamlessly uses the Eigen library for all linear algebra operations.
    
- **Header-Only**: Easy to integrate into any project by just including the header.

## Requirements

- C++11 or later
- Eigen 3.3 or later
- CMake 3.10+ (for building examples and tests)

## Quick Start

```bash
git clone https://github.com/Bziyue/SplineTrajectory.git
# git clone git@github.com:Bziyue/SplineTrajectory.git

cd SplineTrajectory

# Install Eigen3 (if not installed)
sudo apt install libeigen3-dev

# Build and test
mkdir build && cd build
cmake ..
make

# Run performance comparisons
./test_cubic_spline_vs_minco_nd
./test_quintic_spline_vs_minco_nd
./test_septic_spline_vs_minco_nd

# Run examples
./basic_cubic_spline
./quintic_spline_comparison
./robot_trajectory_planning
./test_with_min_jerk_3d
./test_with_min_snap_3d
```
SplineTrajectory also outperforms [large_scale_traj_optimizer](https://github.com/ZJU-FAST-Lab/large_scale_traj_optimizer) in both trajectory generation and evaluation. To see the test results, run ./test_with_min_jerk_3d.

For a complete motion planning toolkit that integrates this library, check out [ST-opt-tools](https://github.com/MarineRock10/ST-opt-tools). It's a motion planning toolkit featuring ESDF mapping, A* path planning, and L-BFGS trajectory optimization integrated with SplineTrajectory library.

## Comparison with MINCO
This library is mathematically equivalent to MINCO but implemented with more efficient algorithms.
| Feature         | SplineTrajectory                             | MINCO                      |
| --------------- | -------------------------------------------- | -------------------------- |
| **Algorithm**   | **Thomas Algorithm** (Block Tridiagonal)     | LU Decomposition           |
| **Performance** | **Faster** Generation & Evaluation           | Baseline                   |
| **Core Theory** | Classical Spline Theory (Minimum Norm)       | Minimum Control Effort     |
| **Flexibility** | Fully templated for **arbitrary dimensions** | Fixed to 3D |
| **Evaluation**  | Optimized segmented batch evaluation with coefficient caching        | Standard evaluation        |

## Spline Types & Energy Minimization
The library provides splines that are optimal solutions, minimizing the integral of the squared norm of a derivative, which has a direct physical meaning.

| Spline Type             | MINCO Equivalent     | 
| ----------------------- | -------------------- | 
| **Cubic** (3rd order)   | Minimum Acceleration | 
| **Quintic** (5th order) | Minimum Jerk         | 
| **Septic** (7th order)  | Minimum Snap         |

---
## Usage Example
Here's a concise example of how to create and evaluate a 3D trajectory.
```cpp
#include "SplineTrajectory.hpp"
#include <iostream>
#include <vector>
#include <Eigen/Dense>
#include <iomanip>

int main() {
    using namespace SplineTrajectory;

    std::cout << "=== SplineTrajectory Complete Interface Usage Example ===" << std::endl;

    // 1. Define 3D waypoints and boundary conditions
    SplineVector<SplinePoint3d> waypoints = {
        {0.0, 0.0, 0.0}, {1.0, 2.0, 1.0}, {3.0, 1.0, 2.0}, {4.0, 3.0, 0.5}, {5.0, 0.5, 1.5}
    };
    
    // Define detailed boundary conditions (including velocity, acceleration, jerk)
    BoundaryConditions<3> boundary; //default velocity、acceleration and jerk are zero
    // or BoundaryConditions<3> boundary(SplinePoint3d(0.1, 0.0, 0.0),SplinePoint3d(0.2, 0.0, 0.1)); default acceleration and jerk are zero
    boundary.start_velocity = SplinePoint3d(0.1, 0.0, 0.0); // cubic splines only use velocity 
    boundary.end_velocity = SplinePoint3d(0.2, 0.0, 0.1);
    boundary.start_acceleration = SplinePoint3d(0.0, 0.0, 0.0);// quintic use velocity and acceleration
    boundary.end_acceleration = SplinePoint3d(0.0, 0.0, 0.0);
    boundary.start_jerk = SplinePoint3d(0.0, 0.0, 0.0); // septic use velocity, acceleration and jerk
    boundary.end_jerk = SplinePoint3d(0.0, 0.0, 0.0);

    std::cout << "\n--- Construction Methods Comparison ---" << std: