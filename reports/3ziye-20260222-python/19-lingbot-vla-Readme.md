<h1 align="center">LingBot-VLA: A Pragmatic VLA Foundation Model</h1>

<p align="center">
  <a href="assets/LingBot-VLA.pdf"><img src="https://img.shields.io/static/v1?label=Paper&message=PDF&color=red&logo=arxiv"></a>
  <a href="https://technology.robbyant.com/lingbot-vla"><img src="https://img.shields.io/badge/Project-Website-blue"></a>
  <a href="https://huggingface.co/collections/robbyant/lingbot-vla"><img src="https://img.shields.io/static/v1?label=%F0%9F%A4%97%20Model&message=HuggingFace&color=yellow"></a>
  <a href="https://modelscope.cn/collections/Robbyant/LingBot-VLA"><img src="https://img.shields.io/static/v1?label=%F0%9F%A4%96%20Model&message=ModelScope&color=purple"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache--2.0-green"></a>
</p>

<p align="center">
  <img src="assets/Teaser.png" width="100%">
</p>

## 🥳 We are excited to introduce **LingBot-VLA**, a pragmatic Vision-Language-Action foundation model.

**LingBot-VLA** has focused on **Pragmatic**:
- **Large-scale Pre-training Data**: 20,000 hours of real-world
data from 9 popular dual-arm robot configurations.
<p align="center">
  <img src="assets/scale_sr.png" width="45%" style="margin: 0 10px;">
  <img src="assets/scale_ps.png" width="45%" style="margin: 0 10px;">
</p>

- **Strong Performance**: Achieve clear superiority over competitors on simulation and real-world benchmarks.
- **Training Efficiency**: Represent a 1.5 ∼ 2.8× (depending on the relied VLM base model) speedup over existing VLA-oriented codebases.

## 🚀 News
- **[2026-01-27]** LingBot-VLA Technical Report is available on Arxiv.
- **[2026-01-27]** Weights and code released!


---


## 🛠️ Installation
Requirements
 - Python 3.12.3
 - Pytorch 2.8.0
 - CUDA 12.8

```bash
# Install Lerobot
pip install torch==2.8.0 torchvision==0.23.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cu128
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/huggingface/lerobot.git
cd lerobot
git checkout 0cf864870cf29f4738d3ade893e6fd13fbd7cdb5
pip install -e .
# Install flash attention
pip install /path/to/flash_attn-2.8.3+cu12torch2.8cxx11abiTRUE-cp312-cp312-linux_x86_64.whl

# Clone the repository
git clone https://github.com/robbyant/lingbot-vla.git
cd lingbot-vla/
git submodule update --remote --recursive
pip install -e .
pip install -r requirements.txt
# Install LingBot-Depth dependency
cd ./lingbotvla/models/vla/vision_models/lingbot-depth/
pip install -e . --no-deps
cd ../MoGe
pip install -e .
```

---

## 📦 Model Download
We release LingBot-VLA pre-trained weights in two configurations: depth-free version and a depth-distillated version.
- **Pretrained Checkpoints for Post-Training with and without depth**

| Model Name | Huggingface | ModelScope | Description |
| :--- | :---: | :---: | :---: |
| LingBot-VLA-4B &nbsp; | [🤗 lingbot-vla-4b](https://huggingface.co/robbyant/lingbot-vla-4b) | [🤖 lingbot-vla-4b](https://modelscope.cn/models/Robbyant/lingbot-vla-4b) | LingBot-VLA *w/o* Depth|
| LingBot-VLA-4B-Depth | [🤗 lingbot-vla-4b-depth](https://huggingface.co/robbyant/lingbot-vla-4b-depth) | [🤖 lingbot-vla-4b-depth](https://modelscope.cn/models/Robbyant/lingbot-vla-4b-depth) | LingBot-VLA *w/* Depth |




To train LingBot with our codebase, weights from [Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct), [MoGe-2-vitb-normal](https://huggingface.co/Ruicheng/moge-2-vitb-normal), and [LingBot-Depth](https://huggingface.co/robbyant/lingbot-depth-pretrain-vitl-14) also need to be prepared.
- **Run Command**:
```bash
python3 scripts/download_hf_model.py --repo_id robbyant/lingbot-vla-4b --local_dir lingbot-vla-4b 
```
---

## 💻 Post-Training Example

- **Data Preparation**:
Please follow [RoboTwin2.0 Preparation](experiment/robotwin/README.md)

- **Training Configuration**:
We provide the mixed post-training configuration in five RoboTwin 2.0 tasks ("open_microwave" "click_bell" "stack_blocks_three" "place_shoe" "put_object_cabinet").
<details>
<summary><b>Click to expand full YAML configuration</b></summary>

```yaml
model:
  model_path: "path/to/lingbot_vla_checkpoint" # Path to pre-trained VLA foundation model (w/o or w depth)
  tokenizer_path: "path/to/Qwen2.5-VL-3B-Instruct" 
  post_training: true            # Enable post-training/fine-tuning mode
  adanorm_time: true
  old_adanorm: true

data:
  datasets_type: vla
  data_name: robotwin_5_new      
  train_path: "path/to/lerobot_merged_data" # merged data from 5 robotwin2.0 tasks
  num_workers: 8
  norm_type: bounds_99_woclip
  norm_stats_file: assets/norm_stats/robotwin_50.json # file of normalization statistics

train:
  output_dir: "path/to/output"
  loss_type: L1_fm               # we apply L1 flow-matching loss in robotwin2.0 finetuning
  data_parallel_mode: fsdp2      # Use Fully Sharded Data Parallel (PyTorch FSDP2)
  enable_full_shard: false       # Don't apply reshare after forward in FSDP2
  module_fsdp_enable: true
  use_compile: true              # Acceleration