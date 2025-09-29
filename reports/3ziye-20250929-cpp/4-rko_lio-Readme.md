<div align="center">
  <h1>RKO LIO - LiDAR-Inertial Odometry<br />Without Sensor-Specific Modelling</h1>
</div>

<p align="center">
ROS Distros:
<br />
<a href="https://github.com/PRBonn/rko_lio/actions/workflows/ros_build_humble.yaml"><img src="https://github.com/PRBonn/rko_lio/actions/workflows/ros_build_humble.yaml/badge.svg?branch=master" alt="Humble" /></a>
<a href="https://github.com/PRBonn/rko_lio/actions/workflows/ros_build_jazzy.yaml"><img src="https://github.com/PRBonn/rko_lio/actions/workflows/ros_build_jazzy.yaml/badge.svg?branch=master" alt="Jazzy" /></a>
<a href="https://github.com/PRBonn/rko_lio/actions/workflows/ros_build_kilted.yaml"><img src="https://github.com/PRBonn/rko_lio/actions/workflows/ros_build_kilted.yaml/badge.svg?branch=master" alt="Kilted" /></a>
<a href="https://github.com/PRBonn/rko_lio/actions/workflows/ros_build_rolling.yaml"><img src="https://github.com/PRBonn/rko_lio/actions/workflows/ros_build_rolling.yaml/badge.svg?branch=master" alt="Rolling" /></a>
</p>

<p align="center">
Python Bindings:
<br />
<a href="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_ubuntu_2204.yaml"><img src="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_ubuntu_2204.yaml/badge.svg?branch=master" alt="Ubuntu 22.04" /></a>
<a href="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_ubuntu_2204_arm.yaml"><img src="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_ubuntu_2204_arm.yaml/badge.svg?branch=master" alt="Ubuntu 22.04 ARM" /></a>
<a href="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_ubuntu_2404.yaml"><img src="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_ubuntu_2404.yaml/badge.svg?branch=master" alt="Ubuntu 24.04" /></a>
<a href="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_ubuntu_2404_arm.yaml"><img src="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_ubuntu_2404_arm.yaml/badge.svg?branch=master" alt="Ubuntu 24.04 ARM" /></a>
<br />
<a href="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_macos_14.yaml"><img src="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_macos_14.yaml/badge.svg?branch=master" alt="macOS 14" /></a>
<a href="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_macos_15.yaml"><img src="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_macos_15.yaml/badge.svg?branch=master" alt="macOS 15" /></a>
<br />
<a href="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_windows_2022.yaml"><img src="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_windows_2022.yaml/badge.svg?branch=master" alt="Windows 2022" /></a>
<a href="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_windows_11_arm.yaml"><img src="https://github.com/PRBonn/rko_lio/actions/workflows/python_bindings_windows_11_arm.yaml/badge.svg?branch=master" alt="Windows 11 ARM" /></a>
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=NNpzXdf9XmU">
    <img src="https://raw.githubusercontent.com/PRBonn/rko_lio/refs/heads/master/docs/example_multiple_platforms.png" alt="Visualization of odometry system running on data from four different platforms in four different environments" />
  </a>
  <br />
  <em>Four different platforms, four different environments, one odometry system</em>
</p>

## Quick Start

### Python

In case you already have a rosbag (ROS1 or ROS2) which contains a TF tree, you can inspect the results of our odometry system with the following two steps

```bash
pip install rko_lio rosbags rerun-sdk
```

`rko_lio` is our odometry package, `rosbags` is required for using our rosbag dataloader, and `rerun-sdk` is what we use for our optional visualizer.
Next, run

```bash
rko_lio -v /path/to/rosbag_folder # <- has to be a directory! with either *.bag files or metadata.yaml from ROS2
```

and you should be good to go!

<details>
<summary><b>Click here for some more details on how the above works and how to use RKO LIO!</b></summary>
<br />

The `-v` flag enables visualization.

You can specify a dataloader to use with `-d`, but if you don't, we try to guess the format based on the layout of the data.

Our rosbag dataloader works with either ROS1 or ROS2 bags.
Place split ROS1 bags in a single folder and pass the folder as the data path.
Note that we don't support running RKO LIO on partial or incomplete bags, though you can try (and maybe raise an issue if you think we should support this).
ROS2 especially will need a `metadata.yaml` file.

By default, we assume there is just one IMU topic and one LiDAR topic in the bag, in which case we automatically pick up the topic names and proceed further.
If there are multiple topics per sensor, you will be prompted to select one via the `--imu` or `--lidar` flags, which you can pass to `rko_lio`.

Next, we assume there is a (static) TF tree in the bag.
If so, we take th