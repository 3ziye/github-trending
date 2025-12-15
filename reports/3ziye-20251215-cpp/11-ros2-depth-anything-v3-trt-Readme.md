# Depth Anything V3 TensorRT ROS 2 Node


https://github.com/user-attachments/assets/d119d3b8-bba1-43a3-9f86-75db24e01235


A ROS 2 node for Depth Anything V3 depth estimation using TensorRT for real-time inference. This node subscribes to camera image and camera info topics and publishes directly both, a metric depth image and `PointCloud2` point cloud.

<!-- omit from toc -->
## Overview
- [Features](#features)
- [Dependencies](#dependencies)
- [Topics](#topics)
  - [Subscribed Topics](#subscribed-topics)
  - [Published Topics](#published-topics)
- [Parameters](#parameters)
  - [Model Configuration](#model-configuration)
  - [Sky Handling](#sky-handling)
  - [Point Cloud Configuration](#point-cloud-configuration)
  - [Debug Configuration](#debug-configuration)
- [Usage](#usage)
  - [Basic Launch](#basic-launch)
  - [With Custom Topics](#with-custom-topics)
  - [With Debug Enabled](#with-debug-enabled)
- [Model Preparation](#model-preparation)
- [Docker Image](#docker-image)
- [Building](#building)
- [Performance](#performance)
- [Architecture](#architecture)
- [Depth Postprocessing Pipeline](#depth-postprocessing-pipeline)
  - [1. Depth Extraction](#1-depth-extraction)
  - [2. Focal Length Scaling](#2-focal-length-scaling)
  - [3. Sky Handling](#3-sky-handling)
  - [4. Resolution Upscaling](#4-resolution-upscaling)
  - [5. Point Cloud Generation](#5-point-cloud-generation)
- [Troubleshooting](#troubleshooting)
  - [Common Issues](#common-issues)
  - [Debug Mode](#debug-mode)
- [License](#license)
- [Acknowledgements](#acknowledgements)



## Features

- **Real-time metric depth estimation** using Depth Anything V3 with TensorRT acceleration
- **Point cloud generation** from metric depth image
- **Debug visualization** with colormap options
- **Configurable precision** (FP16/FP32)

> [!IMPORTANT]  
> This repository is open-sourced and maintained by the [**Institute for Automotive Engineering (ika) at RWTH Aachen University**](https://www.ika.rwth-aachen.de/).  
> We cover a wide variety of research topics within our [*Vehicle Intelligence & Automated Driving*](https://www.ika.rwth-aachen.de/en/competences/fields-of-research/vehicle-intelligence-automated-driving.html) domain.  
> If you would like to learn more about how we can support your automated driving or robotics efforts, feel free to reach out to us!  
> :email: ***opensource@ika.rwth-aachen.de***


## Dependencies
- Tested with image `nvcr.io/nvidia/tensorrt:25.08-py3`
  - Ubuntu 24.04, ROS 2 Jazzy
  - CUDA 13
  - TensorRT 10.9
  
- Tested with image `nvcr.io/nvidia/tensorrt:25.03-py3`
  - Ubuntu 24.04, ROS 2 Jazzy
  - CUDA 12.8.1
  - TensorRT 10.9

Depending on your driver and CUDA version you need to select the appropriate base image.

## Topics

### Subscribed Topics

- `~/input/image` (sensor_msgs/Image): Input camera image
- `~/input/camera_info` (sensor_msgs/CameraInfo): Camera calibration info

### Published Topics  

- `~/output/depth_image` (sensor_msgs/Image): Depth image (32FC1 format)
- `~/output/point_cloud` (sensor_msgs/PointCloud2): Generated point cloud
- `~/output/depth_image_debug` (sensor_msgs/Image): Debug depth visualization (if enabled)

## Parameters

All parameters can be configured via `config/depth_anything_v3.param.yaml` or passed at launch time.

### Model Configuration

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `onnx_path` | string | `"models/DA3METRIC-LARGE.onnx"` | Path to Depth Anything V3 ONNX or TensorRT engine file |
| `precision` | string | `"fp16"` | Inference precision (`"fp16"` or `"fp32"`) |

### Sky Handling

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `sky_threshold` | double | `0.3` | Threshold for sky classification from model's sky output (lower = more sky detected) |
| `sky_depth_cap` | double | `200.0` | Maximum depth value (meters) to assign to sky pixels |

### Point Cloud Configuration

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `point_cloud_downsample_factor` | int | `2` | Publish every Nth point (1 = full resolution, 10 = every 10th point) |
| `colorize_point_cloud` | bool | `true` | Add RGB colors from input image to point cloud |

### Debug Configuration

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `enable_debug` | bool | `false` | Enable debug visualization output |
| `debug_colormap` | string | `"JET"` | Colormap for depth visualization (see below) |
| `debug_filepath` | string | `"/tmp/depth_anything_v3_debug/"` | Directory to save debug images |
| `write_colormap` | bool | `false` | Save colorized debug images to disk |
| `debug_colormap_min_depth` | double | `0.0` | Minimum depth value for colormap normalization (meters) |
| `debug_colormap_max_depth` | double | `50.0` | Maximum depth value for colormap normalization (meters) |

#### Available Colormaps
`JET`, `HOT`, `COOL`, `SPRING`, `SUMMER`, `A