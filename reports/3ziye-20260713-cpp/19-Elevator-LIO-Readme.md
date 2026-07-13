# Elevator-LIO

[中文](README.md) | [English](README_en.md)

作者：Yifan Zhang, Yudong Huang, Yuchong Zhang, Changze Li, Haoran Liu, Ming Yang, Tong Qin*

Elevator-LIO 是面向电梯非惯性运动和跨楼层定位的 LiDAR-惯性里程计。主要测试平台为 Livox MID-360，同时支持其他雷达如 Ouster、Velodyne、XT32 等，但除MID360外尚未经过大规模测试。



[![Project Page](https://img.shields.io/badge/Project-Page-blue)](https://xiaofan4122.github.io/Elevator_LIO_Page/)
[![arXiv](https://img.shields.io/badge/arXiv-2605.24495-b31b1b)](https://arxiv.org/abs/2605.24495)
[![Dataset](https://img.shields.io/badge/HuggingFace-Dataset-ffcc00)](https://huggingface.co/datasets/xiaofan0100/Elevator-LIO-Dataset)

数据集下载与使用说明见 [DATASET.md](DATASET.md)。

关闭 YAML 中的电梯模式后，Elevator-LIO 可作为普通 LIO 使用，并保留触发式更新和自适应降采样等功能。

<p align="center">
  <img src="docs/images/background.jpg" alt="Elevator-LIO overview" width="100%">
</p>

> [!WARNING]
> Elevator-LIO 允许机器人在电梯内自由移动，但建议使用 Livox MID-360 这类视场较大的 LiDAR，并采用倾斜安装，以获得尽可能多方向上的几何约束。如果您的 LiDAR 水平安装，且机器人在电梯内基本不会产生上下运动，请将 `yaml/runtime` 中的 `elevator.strong_prior_enable` 设置为 `true`。该选项会将 IMU 垂直方向加速度强约束解释为电梯加速度，使系统在此类安装条件下也能正常工作。

## 时间节点

- **2026-05-23**：[arXiv 预印本](https://arxiv.org/abs/2605.24495)公开。
- **2026-05-26**：[小红书](http://xhslink.com/o/9MTzcbzjGaQ) 公开宣传。
- **2026-06-06**：[@编程猫小渐](http://xhslink.com/o/5bhSpWqEbeO) 复现 Elevator-LIO 论文结果。
- **2026-06-20**：[Elevator-LIO 数据集](https://huggingface.co/datasets/xiaofan0100/Elevator-LIO-Dataset)公开，包含 20 条序列和 79 次电梯乘坐；额外收录 @编程猫小渐 的两条数据。
- **2026-06-22**：发布 [rosbag 管理器视频](https://www.bilibili.com/video/BV1n3jt64Eoi/?share_source=copy_web&vd_source=392db04838f1edf7d12e58a3d68775d8)，该工具随 Elevator-LIO 一同开源。
- **2026-06-26**：ROS 1 源码发布。
- **计划中**：ROS 2 源码发布。
- **计划中**：更多数据集发布，包括更多带图像的完整序列。
- **计划中**：手持采集平台软硬件源码与文档公开。

## 支持工作

欢迎参观课题组其他工作，Elevator-LIO 为以下工作提供了定位支持：

- [SCAN-Planner](https://github.com/wuyi2121/SCAN-Planner)：面向路线引导长距离四足导航的空间碰撞感知局部规划器，可为自主探索、视觉语言导航等上层任务提供底层规划基础。
- [TravExplorer](https://github.com/wuyi2121/TravExplorer)：面向跨楼层具身探索的可通行性驱动 3D 规划系统，支持单楼层与跨楼层目标导航。

## 场景展示

![Elevator-LIO 多楼层与电梯场景](docs/images/Scenarios.png)

## 方法概述

传统 LIO 假设导航坐标系为惯性系，但在运动的电梯轿厢内，IMU 会感受到电梯运动，而 LiDAR 主要观测轿厢内的相对几何，现有 LIO 方法几乎全部失效。Elevator-LIO 将机器人相对电梯的运动与电梯自身运动解耦，并通过模式相关的迭代误差状态卡尔曼滤波实现连续跨楼层定位：普通室内环境使用标准 LIO 传播，进入电梯后启用非惯性状态传播和约束更新。

![Elevator-LIO 系统总览](docs/images/system_overview.png)

系统按照时间顺序处理 IMU 和 LiDAR 数据，依次完成静态 IMU 初始化、自适应降采样、模式相关传播、IESKF LiDAR 更新、可能的退出电梯更新和增量 ikd-Tree 建图。

### 电梯模式管理

进入检测使用 LiDAR 距离统计量判断机器人是否由开放区域进入封闭轿厢；退出检测根据估计的电梯竖直运动状态及其方差判断电梯是否停稳。两种事件也可以通过 ROS 话题手动触发。

<p align="center">
  <img src="docs/images/elevator_mode_manager.png" alt="电梯模式进入与退出检测" width="70%">
</p>

### 退出电梯更新

电梯停稳后，系统施加零速度和零加速度约束，将估计的电梯竖直位移重新锚定到机器人状态，并重置电梯相关状态，从而抑制电梯运行期间累积的高度漂移。

<p align="center">
  <img src="docs/images/exit_update.png" alt="退出电梯时的事件触发更新" width="70%">
</p>

### 自适应降采样

系统在线调整体素大小，使降采样后的有效点数保持在目标值附近，在电梯轿厢内保留足够的几何信息，同时控制开放场景中的计算量。

<p align="center">
  <img src="docs/images/adaptive_downsampling.png" alt="自适应体素降采样" width="70%">
</p>

## 数据采集平台

<p align="center">
  <img src="docs/images/handheld_platform.png" alt="Elevator-LIO 手持采集设备" width="85%">
</p>

数据使用集成 Livox MID-360、工业相机和 Jetson Orin Nano 的便携式手持设备采集。

> [!NOTE]
> - [ ] 后续将开源手持设备的软硬件设计与相关文档。
>

## 🔥 设计理念

Elevator-LIO 的设计遵循开箱即用的原则，集成了许多便于使用的功能，具有完善的注释方便您进行后续开发，日志与调试系统比较完善。

小巧思包括：

- **无 Livox_ros_driver 依赖**：自定义消息在包内构建，在 ROS 系统上可直接编译使用
- **初始重力对齐**：无论雷达以何种方向放置，世界系都会初始化为水平方向
- **球形/长方体包围盒滤除**：除了指定球形滤除框，也可以指定长方体区域内点云滤除
- **预留额外的 body 系输出**：可在 yaml/sensors 中配置 `lidar_R_vehicle` 和 `lidar_t_vehicle`
- **简单的重定位功能**：支持加载 PCD 地图，然后在原点启动并运行重定位
- **协方差矩阵可视化**：可在 yaml/logging 中打开，方便调试
- **高频输出**：可在 yaml/runtime 中打开，将IMU预积分位姿也输出出来，方便下游应用

不同于主流 LIO，Elevator-LIO 没有显式打包概念，遵循“谁来谁更新”的设计理念，在框架上更适合多传感器融合；但这也带来了额外开销：状态机需要以较高频率轮询并检测是否有数据输入。


## 🛠️ 安装与运行

### 环境要求

当前代码主要在以下环境中开发和测试：

- Ubuntu 20.04
- ROS Noetic

OpenCV 目前只用于协方差矩阵和电梯状态曲线的调试窗口，默认配置中这些窗口均关闭；但源码和 CMake
仍会包含并链接 OpenCV，您可以自行修改代码取消这些依赖。

### 编译

将代码放入 `src` 目录下编译：

```bash
catkin_make
```

### 运行

直接使用 `roslaunch` 运行：

```bash
roslaunch lio start.launch
```

可以指定对应的 YAML 文件参数。默认配置为 `root_config.yaml`，也可以创建自己的配置文件：

```bash
roslaunch lio start.launch config_path:=path_to_yaml
```


### 电梯模式说明

电梯功能由统一开关控制：

```yaml
elevator:
  enable: true
```

自动进入电梯模式由门关闭检测控制：

```yaml
elevator:
  door_detector:
    enable: true
```

该检测基于点云距离分位数，在狭窄场景（如楼道）中可能误触发。可以关闭自动检测，改用话题手动触发。

进入电梯模式（通过话题触发）：

```bash
rostopic pub /LIO/set_elevator_flag std_msgs/Bool "data: true" -1
```

退出电梯模式（通过话题触发）：

```bash
rostopic pub /LIO/set_elevator_flag std_msgs/Bool "data: false" -1
```

自动退出通过下面参数控制：

```yaml
elevator:
  self_exit_detector: true # 打开时会根据估计出的电梯速度及其方差信息，自动退出电梯模式
```

程序内部的电梯状态会和 LiDAR 信息同频率发布：`/LIO/in_elevator` 保留布尔模式标志；`/LIO/elevator_state` 发布电梯模式以及估计的相对位移、速度和加速度，并供 RViz 电梯状态面板显示。

### 仿真节点

在程序开发早期，我们设计了仿真节点 `sim_node`，用于构造电梯场景并生成 LiDAR 与 IMU 消息。具体程序与配置位于 `src/sim` 中。

### 参数修改

在 `root_config.yaml` 中分别选择传感器、运行和日志配置：

```yaml title: root_config.yaml

sensor_config: "sensors/livox.yaml"
runtime_config: "runtime/mapping.yaml"
logging_config: "logging