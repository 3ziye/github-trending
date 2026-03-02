# χ₀

<div id="top" align="center">

[![Blog Page](https://img.shields.io/badge/Blog_Page-green)](https://mmlab.hk/research/kai0)
[![arXiv](https://img.shields.io/badge/arXiv-2602.09021-b31b1b)](https://arxiv.org/abs/2602.09021)
[![Kai0 Data](https://img.shields.io/badge/huggingface-Kai0_Data-orange?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/OpenDriveLab-org/Kai0)
[![Kai0 Model](https://img.shields.io/badge/huggingface-Kai0_Model-orange?logo=huggingface&logoColor=white)](https://huggingface.co/OpenDriveLab-org/Kai0)
[![ModelScope Data](https://img.shields.io/badge/ModelScope-Kai0_Data-purple)](https://www.modelscope.cn/datasets/OpenDriveLab/Kai0)
[![ModelScope Model](https://img.shields.io/badge/ModelScope-Kai0_Model-purple)](https://www.modelscope.cn/models/OpenDriveLab/Kai0)

<!-- [![Repo](https://img.shields.io/badge/github-repo-blue?logo=github)](https://github.com/OpenDriveLab/kai0) -->


</div>

χ₀ (**kai0**) is a resource-efficient framework for achieving production-level robustness in robotic manipulation by taming distributional inconsistencies.
<!-- This repository is built on top of [openpi](https://github.com/Physical-Intelligence/openpi), the open-source models and packages for robotics published by the [Physical Intelligence team](https://www.physicalintelligence.company/). -->

χ₀ addresses the systematic distributional shift among the human demonstration distribution ($P_\text{train}$), the inductive bias learned by the policy ($Q_\text{model}$), and the test-time execution distribution ($P_\text{test}$) through three technical modules:

- **[Model Arithmetic](#model-arithmetic)**: A weight-space merging strategy that combines models trained on different data subsets, efficiently capturing diverse knowledge without architectural complexity. **[Released]**
- **[Stage Advantage](#stage-advantage)**: A stage-aware advantage estimator that provides stable, dense progress signals for policy training. **[Released]**
- **[Train-Deploy Alignment](#train-deploy-alignment)**: Bridges the distribution gap via spatio-temporal augmentation, heuristic DAgger corrections, and temporal chunk-wise smoothing. **[Released]**

χ₀ enables two sets of dual-arm robots to collaboratively orchestrate long-horizon garment manipulation — flattening, folding, and hanging — surpassing the state-of-the-art $\pi_{0.5}$ baseline by approximately 250% in success rate, with `only 20 hours of data and 8 A100 GPUs`.

<!-- [[Paper]](https://github.com/OpenDriveLab/kai0) [[Blog]](https://mmlab.hk/research/kai0) -->

https://github.com/user-attachments/assets/3f5f0c48-ff3f-4b9b-985b-59ad0b2ea97c

## Table of Contents

- [Update](#update)
- [Acknowledgement](#acknowledgement)
- [Requirements](#requirements)
  - [Compute](#compute)
  - [Hardware](#hardware)
- [Installation](#installation)
- [Preparation](#preparation)
  - [1. Download the dataset](#1-download-the-dataset)
  - [2. Download checkpoints (optional, for testing)](#2-download-checkpoints-optional-for-testing)
  - [3. Fine-tune with normal π₀.₅](#3-fine-tune-with-normal-π₀.₅)
- [Project Overview](#project-overview)
- [Modules Overview and To-Do List](#modules-overview-and-to-do-list)
- [Model Arithmetic](#model-arithmetic)
  - [Workflow](#workflow)
  - [Quick Start](#quick-start)
- [Stage Advantage](#stage-advantage)
- [Train-Deploy Alignment](#train-deploy-alignment)
- [Citation](#licenseandcitation)
- [Troubleshooting](#troubleshooting)
- [Links and Community](#links-and-community)

## Update

- [Feb 15 2026] Stage Advantage **advantage labels** (`Task_A/advantage/`) released on [Hugging Face](https://huggingface.co/datasets/OpenDriveLab-org/Kai0) and [ModelScope](https://www.modelscope.cn/datasets/OpenDriveLab/Kai0).
- [Feb 15 2026] Release of the **Train-Deploy Alignment** module: data augmentation (time scaling, space mirroring), DAgger data collection, inference with temporal smoothing/ensembling and RTC, and HDF5-to-LeRobot conversion.
- [Feb 14 2026] Release of the **Stage Advantage** module: advantage estimator training, evaluation, GT labeling, and AWBC training pipeline.
- [Feb 10 2026] Initial release of the **Model Arithmetic** module with support for both JAX and PyTorch checkpoints (not tested thoroughly).
- [Feb 10 2026] χ₀ paper released.

## Acknowledgement

This repository is built on top of [openpi](https://github.com/Physical-Intelligence/openpi) by [Physical Intelligence](https://www.physicalintelligence.company/). We sincerely thank the Physical Intelligence team for open-sourcing their excellent π₀ and π₀.₅ models and the openpi codebase, which made this work possible. The base model training, inference pipeline, and data processing utilities all originate from openpi. Please refer to the [openpi README](https://github.com/Physical-Intelligence/openpi) for details on the base models, fine-tuning, and inference.

## Requirements

### Compute

χ₀ shares the same system requirements as openpi. You will need an NVIDIA GPU with a