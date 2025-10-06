# refx

**refx** is a modern header-only C++ library designed for mobile robotics and navigation. Its core philosophy is to leverage the C++ type system to provide compile-time safety for all geometric and geodetic calculations. This prevents a wide class of common and difficult-to-debug errors that arise from incorrect handling of coordinate reference frames.

> [!WARNING]
> refx is still in development (0.x.y) and API interface may change between minor revisions. Please use the releases packages for direct import or specify a commit tag if you are using refx with CMake `FetchContent`

## Documentation

Read the **[Full Documentation](https://mosaico-labs.github.io/refx-doc)**, to dive in — explore APIs and classes to help you build and contribute faster.

For a collection of practical, real-world recipes designed to help you solve common problems in robotics and navigation, read ***The refx [Cookbook](https://mosaico-labs.github.io/refx-doc/cookbook)***.

## Who is this for?

This library is intended for robotics engineers, researchers, and students working on applications that require a high degree of navigational accuracy and reliability, such as:

  * Sensor fusion for Inertial Navigation Systems (INS)
  * UAV/drone flight control and guidance
  * Autonomous ground vehicle (AGV) localization
  * Marine and sub-surface navigation
  * Geodetic surveying and mapping

## Key Features

  * **Type-Safe Frames**: Each coordinate frame (e.g., NED, ECEF, FRD) is a unique type, preventing accidental mixing of incompatible data.
  * **Mathematical Correctness**: A strict semantic distinction is enforced between absolute positions (`Coordinate3D`) and displacement vectors (`Vector3D`). Operations are designed to reflect their true mathematical meaning.
  * **High-Fidelity Models**: Includes standard geodetic models (WGS-84), gravity models, and a concrete implementation of the World Magnetic Model (WMM2020) for high-accuracy applications.
  * **Compile-Time Dispatch**: A powerful template-based system automatically selects the correct mathematical logic for linear vs. angular coordinates, ensuring correctness for geodetic calculations.

## Ecosystem Integration
refx is designed to be a self-contained, lightweight library. However, for maximum utility, it provides optional, first-class support for **Eigen3**.

## Installation

### CMake
Here's the code you'd add to your project's `CMakeLists.txt` file to import the refx library.
```cmake
include(FetchContent)
FetchContent_Declare(
  refx
  GIT_REPOSITORY https://github.com/mosaico-labs/refx.git/
  GIT_TAG        v0.1.0
)
FetchContent_MakeAvailable(refx)
```

From this point on, the `refx::refx` target is available to your project and this command can be used to to link refx.
```cmake
target_link_libraries(my_target PRIVATE refx::refx)
```

### Conan
You can install refx using Conan via the [klin](https://github.com/conan-kiln/kiln) repository.

- Set up Conan Kiln as a remote following the [instructions](https://github.com/conan-kiln/kiln#setup)
- Include `refx/[>=0.2.1 <1]` as a requirement under your `conanfile.txt` or `conanfile.py`.
- Follow the regular [instructions](https://docs.conan.io/2/tutorial.html) for integrating Conan packages into your project

Special thanks to [@valgur](https://github.com/valgur) for adding Conan support.

## Requirements
Developing with refx requires only a C++17 compatible compiler, running tests requires Google Test as dependency (downloaded automatically by CMake).

## Getting Started

Using `refx` is straightforward. The following example demonstrates the core features of the library: creating frame-aware vectors and coordinates, leveraging compile-time safety, and performing transformations.


### A Practical Example

The code below simulates a common scenario: taking a vehicle's body-frame velocity, rotating it into the world frame, and projecting a global GPS coordinate into a local navigation frame.

```cpp
//getting_started.cpp
#include <iostream>
#include <cmath>
#include <refx/geometry.h>  // for Vector3D, Coordinate3D, Rotation and YawPitchRoll
#include <refx/transformations.h> // frame_cast, frame_transform

using namespace refx;

int main() {
    // 1. Create frame-aware vectors. Types are tagged with their frame.
    Vector3D<ned> velocity_ned{10.0, -2.0, 0.5};  // {N, E, D}
    Vector3D<frd> omega_body{0.0, 0.0, 0.03};     // {F, R, D}

    std::cout << "Velocity in NED frame: " << velocity_ned << std::endl;

    // 2. COMPILE-TIME SAFETY: Mixing frames is a compiler error.
    // Uncommenting the line below will cause a compile-time error, preventing a common bug.
    // velocity_ned + thrust_in_body;  // ERROR: Incompatible frames!

    // 3. Define a rotation from the body frame to the world (NED) frame.
    // Let's assume a 45-degree yaw (pi/4 radians).
    auto yaw_pitch_roll = YawPitchRoll<double>(M_PI / 4.0, 0.0, 0.0);
    auto R_world_from_body = Rotation<ned, frd>(yaw_pitch_roll);

    // 4. Correctly tra