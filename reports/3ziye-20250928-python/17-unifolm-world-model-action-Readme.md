# UnifoLM-WMA-0: A World-Model-Action (WMA) Framework under UnifoLM Family
<p style="font-size: 1.2em;">
    <a href="https://unigen-x.github.io/unifolm-world-model-action.github.io"><strong>Project Page</strong></a> | 
    <a href="https://huggingface.co/collections/unitreerobotics/unifolm-wma-0-68ca23027310c0ca0f34959c"><strong>Models</strong></a> |
    <a href="https://huggingface.co/unitreerobotics/datasets"><strong>Dataset</strong></a> 
  </p>
<div align="center">
  <p align="right">
    <span> 🌎English </span> | <a href="README_cn.md"> 🇨🇳中文 </a>
  </p>
</div>
<div align="justify">
    <b>UnifoLM-WMA-0</b> is Unitree‘s open-source world-model–action architecture spanning multiple types of robotic embodiments, designed specifically for general-purpose robot learning. Its core component is a world-model capable of understanding the physical interactions between robots and the environments. This world-model provides two key functions: (a) <b>Simulation Engine</b> – operates as an interactive simulator to generate synthetic data for robot learning; (b) <b>Policy Enhancement</b> – connects with an action head and, by predicting future interaction processes with the world-model, further optimizes decision-making performance.
</div>

## 🦾 Real-Robot Demonstrations
| <img src="assets/gifs/real_z1_stackbox.gif" style="border:none;box-shadow:none;margin:0;padding:0;" /> | <img src="assets/gifs/real_dual_stackbox.gif" style="border:none;box-shadow:none;margin:0;padding:0;" /> |
|:---:|:---:|
| <img src="assets/gifs/real_cleanup_pencils.gif" style="border:none;box-shadow:none;margin:0;padding:0;" /> | <img src="assets/gifs/real_g1_pack_camera.gif" style="border:none;box-shadow:none;margin:0;padding:0;" /> |

**Note: the top-right window shows the world model’s prediction of future action videos.**

## 🔥 News

* Sep 22, 2025: 🚀 We released the deployment code for assisting experiments with [Unitree](https://www.unitree.com/) robots.
* Sep 15, 2025: 🚀 We released the training and inference code along with the model weights of [**UnifoLM-WMA-0**](https://huggingface.co/collections/unitreerobotics/unifolm-wma-0-68ca23027310c0ca0f34959c).

## 📑 Opensource Plan
- [x] Training 
- [x] Inference
- [x] Checkpoints
- [x] Deployment

## ⚙️  Installation
```
conda create -n unifolm-wma python==3.10.18
conda activate unifolm-wma

conda install pinocchio=3.2.0 -c conda-forge -y
conda install ffmpeg=7.1.1 -c conda-forge

git clone --recurse-submodules https://github.com/unitreerobotics/unifolm-world-model-action.git

# If you already downloaded the repo:
cd unifolm-world-model-action
git submodule update --init --recursive

pip install -e .

cd external/dlimp
pip install -e .
```
## 🧰 Model Checkpoints
| Model | Description | Link|
|---------|-------|------|
|$\text{UnifoLM-WMA-0}_{Base}$| Fintuned on [Open-X](https://robotics-transformer-x.github.io/) dataset. | [HuggingFace](https://huggingface.co/unitreerobotics/UnifoLM-WMA-0-Base)|
|$\text{UnifoLM-WMA-0}_{Dual}$| Fintuned on five [Unitree opensource dataset](https://huggingface.co/collections/unitreerobotics/g1-dex1-datasets-68bae98bf0a26d617f9983ab) in both decision-making and simulation modes. | [HuggingFace](https://huggingface.co/unitreerobotics/UnifoLM-WMA-0-Dual)|

## 🛢️ Dataset
In our experiments, we consider the following three opensource dataset:
| Dataset | Robot | Link |
|---------|-------|------|
|Z1_StackBox| [Unitree Z1](https://www.unitree.com/z1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/Z1_StackBox_Dataset/tree/v2.1)|
|Z1_DualArm_StackBox|[Unitree Z1](https://www.unitree.com/z1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/Z1_Dual_Dex1_StackBox_Dataset/tree/v2.1)|
|Z1_DualArm_StackBox_V2|[Unitree Z1](https://www.unitree.com/z1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/Z1_Dual_Dex1_StackBox_Dataset_V2/tree/v2.1)|
|Z1_DualArm_Cleanup_Pencils|[Unitree Z1](https://www.unitree.com/z1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/Z1_Dual_Dex1_CleanupPencils_Dataset/tree/v2.1)|
|G1_Pack_Camera|[Unitree G1](https://www.unitree.com/g1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/G1_Dex1_MountCameraRedGripper_Dataset/tree/v2.1)|

To train on your own dataset, first to have the data following the [Huggingface LeRobot V2.1](https://github.com/huggingface/lerobot) dataset format. Assume the dataset’s source directory structure is as follows:
```
source_dir/
    ├── dataset1_name
    ├── dataset2_name
    ├── dataset3_name
    └── ...
```
Then, convert a dataset to the required format using the command below:
```python
cd prepare_data
python prepare_training_data.py \
    --source_dir /path/to/your/source_dir \
    --target_dir /path/to/save/the/converted/data \
    --dataset_name "dataset1_name" \
    --robot_name "a tag of the robot in the dataset" # e.g, Unitree Z1 Robot Arm or Unitree G1 Robot with Gripper.
```
The resulting data structure (Note: model training only supports in