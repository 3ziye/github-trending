# MimicKit


![Teaser](images/MimicKit_teaser.gif)

This framework provides a suite of motion imitation methods for training motion controllers. A more detailed overview of MimicKit is available in the [Starter Guide](https://arxiv.org/abs/2510.13794). This codebase includes implementations of:
- [DeepMimic](https://xbpeng.github.io/projects/DeepMimic/index.html)
- [AMP](https://xbpeng.github.io/projects/AMP/index.html)
- [ASE](https://xbpeng.github.io/projects/ASE/index.html)
- [ADD](https://xbpeng.github.io/projects/ADD/index.html)

We also include the following RL algorithms:
- [PPO](https://arxiv.org/abs/1707.06347)
- [AWR](https://xbpeng.github.io/projects/AWR/index.html)

---

## Installation

Install IsaacGym: https://developer.nvidia.com/isaac-gym

Install requirements:
```
pip install -r requirements.txt
```
Download assets and motion data from [here](https://1sfu-my.sharepoint.com/:u:/g/personal/xbpeng_sfu_ca/EclKq9pwdOBAl-17SogfMW0Bved4sodZBQ_5eZCiz9O--w?e=bqXBaa), then extract the contents into [`data/`](data/).

---

## Training

To train a model, run the following command:
```
python mimickit/run.py --mode train --num_envs 4096 --env_config data/envs/deepmimic_humanoid_env.yaml --agent_config data/agents/deepmimic_humanoid_ppo_agent.yaml --visualize true --log_file output/log.txt --out_model_file output/model.pt
```
- `--mode` selects either `train` or `test` mode.
- `--num_envs` specifies the number of parallel environments used for simulation.
- `--env_config` specifies the configuration file for the environment.
- `--agent_config` specifies configuration file for the agent.
- `--visualize` enables visualization. Rendering should be disabled for faster training.
- `--log_file` specifies the output log file, which will keep track of statistics during training.
- `--out_model_file` specifies the output model file, which contains the model parameters.
- `--logger` specifies the logger used to record training stats. The options are TensorBoard `tb` or `wandb`.

Instead of specifying all arguments through the command line, arguments can also be loaded from an `arg_file`:
```
python mimickit/run.py --arg_file args/deepmimic_humanoid_ppo_args.txt --visualize true
```
The arguments in `arg_file` are treated the same as command line arguments. Arguments for all algorithms are provided in [`args/`](args/).


## Testing

To test a model, run the following command:
```
python mimickit/run.py --arg_file args/deepmimic_humanoid_ppo_args.txt --num_envs 4 --visualize true --mode test --model_file data/models/deepmimic_humanoid_spinkick_model.pt
```
- `--model_file` specifies the `.pt` file that contains the parameters of the trained model. Pretrained models are available in [`data/models/`](data/models/), and the corresponding training log files are available in [`data/logs/`](data/logs/).


## Distributed Training

To use distributed training with multi-CPU or multi-GPU:
```
python mimickit/run.py --arg_file args/deepmimic_humanoid_ppo_args.txt --num_workers 2 --device cuda:0
```
- `--num_workers` specifies the number of worker processes used to parallelize training. 
- `--device` specifies the device used for training, which can be `cpu` or `cuda:0`. When training with multiple GPUs, the number of worker processes used to parallelize training must be less than or equal to the number of GPUs available on the system.

## Visualizing Training Logs

When using the TensorBoard logger during training, a TensorBoard `events` file will be saved the same output directory as the log file. The log can be viewed with:
```
tensorboard --logdir=output/ --port=6006 --samples_per_plugin scalars=999999
```
The output log `.txt` file can also be plotted using the plotting script [`plot_log.py`](tools/plot_log/plot_log.py).

---

## Motion Data
Motion data is stored in [`data/motions/`](data/motions/). The `motion_file` field in the environment configuration file can be used to specify the reference motion clip. In addition to imitating individual motion clips, `motion_file` can also specify a dataset file, located in [`data/datasets/`](data/datasets/), which will train a model to imitate a dataset containing multiple motion clips.

The `view_motion` environment can be used to visualize motion clips:
```
python mimickit/run.py --mode test --arg_file args/view_motion_humanoid_args.txt --visualize true
```

Motion clips are represented by the `Motion` class implemented in [`motion.py`](mimickit/anim/motion.py). Each motion clip is stored in a `.pkl` file. Each frame in a motion specifies the pose of the character according to
```
[root position (3D), root rotation (3D), joint rotations]
```
where 3D rotations are specified using 3D exponential maps. Joint rotations are recorded in the order that the joints are specified in the `.xml` file (i.e. depth-first traversal of the kinematic tree). For example, in the case of [`humanoid.xml`](data/assets/humanoid.xml), each frame is represented as
```
[root position (3D), root rotatio