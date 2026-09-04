<p align="center">
  <img width="360" alt="Dalaran" src="docs/assets/dalaran-wordmark.svg" />
</p>

<p align="center">
  <a href="https://pypi.org/project/dalaran-sdk/"><img alt="PyPI" src="https://img.shields.io/pypi/v/dalaran-sdk.svg"></a>
  <a href="https://crates.io/crates/dalaran"><img alt="crates.io" src="https://img.shields.io/crates/v/dalaran.svg"></a>
  <a href="LICENSE"><img alt="Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-blue.svg"></a>
</p>

# Dalaran

**Dalaran is an Apache-2.0, robotics-first observability and visualization stack
for multimodal time-series data — ROS 2 topics, LiDAR sweeps, camera streams,
IMU, and TF transforms, recorded and replayed on one timeline.**

You log data from your robot, your simulator, or an offline pipeline; Dalaran
stores it in an Arrow-backed columnar chunk store, renders it in a 3D/2D viewer
that stays in sync across every sensor, and hands the same data back to you as
dataframes when you want to compute on it instead of look at it.

---

## 60-second quickstart

### Python

```sh
pip install dalaran-sdk
```

```python
import dalaran as dl
import numpy as np

dl.init("dalaran_example_app", spawn=True)  # spawn a viewer process and stream to it

positions = np.random.default_rng(0).normal(size=(1000, 3)).astype(np.float32)
colors = np.random.default_rng(1).integers(0, 255, size=(1000, 3), dtype=np.uint8)

for frame in range(100):
    dl.set_time("frame", sequence=frame)
    dl.log("world/points", dl.Points3D(positions + frame * 0.01, colors=colors))
```

Write to a file instead of a live viewer with `dl.save("session.dlr")`, then
open it later with `dalaran session.dlr`.

### Rust

```sh
cargo add dalaran
```

```rust
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let rec = dalaran::RecordingStreamBuilder::new("dalaran_example_app").spawn()?;

    let positions: Vec<_> = (0..1000)
        .map(|i| ((i % 10) as f32, ((i / 10) % 10) as f32, (i / 100) as f32))
        .collect();

    rec.set_time_sequence("frame", 0);
    rec.log("world/points", &dalaran::Points3D::new(positions))?;

    Ok(())
}
```

### C++

Fetch the SDK in your `CMakeLists.txt` and link against `dalaran_sdk`:

```cmake
include(FetchContent)
FetchContent_Declare(dalaran_sdk URL
  https://github.com/Flaminis/Dalaran/releases/latest/download/dalaran_cpp_sdk.zip)
FetchContent_MakeAvailable(dalaran_sdk)
target_link_libraries(your_target PRIVATE dalaran_sdk)
```

```cpp
#include <dalaran.hpp>

int main() {
    const auto rec = dalaran::RecordingStream("dalaran_example_app");
    rec.spawn().exit_on_failure();

    rec.set_time_sequence("frame", 0);
    rec.log("world/points", dalaran::Points3D({{0.0f, 0.0f, 0.0f}, {1.0f, 1.0f, 1.0f}}));
}
```

### The viewer and CLI

The `dalaran` binary is both the viewer and the CLI. It ships with the Python
wheel, or you can install it on its own:

```sh
cargo install dalaran-cli --locked
dalaran --help
dalaran session.dlr        # open a recording
dalaran --serve            # serve a web viewer
```

Recordings are `.dlr` files and saved blueprints are `.dbl` files. Live streams
and remote catalogs are addressed with `dalaran://` URIs.

---

## Why Dalaran

Everything below is what Dalaran adds for robotics teams specifically, and
everything below works today — it is code in this repository with tests, not a
roadmap. What is *not* built yet lives in [ROADMAP.md](ROADMAP.md).

- **`dalaran.robot`, a high-level robotics logging API** — one handle that knows
  about a robot: joint states, base pose, sensor frames, and URDF-driven link
  transforms, so you log `robot.log_joint_states(...)` instead of hand-rolling a
  dozen entity paths and quaternion conversions. Point it at a URDF and joint
  limits, joint axes and `<mimic>` joints are honoured for you.
- **ROS 2 bridge and rosbag2 replay** — subscribe to live ROS 2
  topics or replay a rosbag2 into Dalaran, backed by an **extensible message
  registry** so you can teach it your own `.msg` types without patching the
  core. Today the repository already ingests MCAP and a set of common ROS
  message schemas.
- **ROS axis-convention helpers** — REP-103/REP-105 conventions (`x`-forward
  `z`-up, ENU vs. NED for positions *and* orientations, `map`/`odom`/`base_link`
  frame semantics that make the direction hard to get backwards) as first-class
  helpers, because silently mismatched axis conventions are the single most
  common way a robotics visualization ends up wrong.
- **Occupancy grids and costmaps** — `nav_msgs/OccupancyGrid`, `nav2_msgs/Costmap`
  and nav2's `/global_costmap` and `/local_costmap` topics land on the `GridMap`
  archetype with proper origin/resolution handling, instead of being flattened
  into an untyped image. nav2's cost semantics are modelled properly, so
  `INSCRIBED_INFLATED_OBSTACLE` and `LETHAL_OBSTACLE` are drawn as the categories
  they are rather than as points on the cost gradient, a costmap's layers stack
  as separate entities with their own draw ord