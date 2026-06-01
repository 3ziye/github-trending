# AscendFHE：面向 Atlas A2 / Ascend 910B 的 FHE 底层算子库与硬件加速方案

AscendFHE 是面向同态加密计算的 Ascend NPU 硬件加速底层算子库，当前公开支持
Atlas A2 / Ascend 910B，SOC 配置为 `ascend910b`。仓库提供 FHE 常用模运算、RNS
基转换、内积累加、自同构重排和 NTT 等算子的 Ascend C kernel、host tiling 逻辑、
算子构建片段和 `torch_npu` 调用说明。

安装并注册 AscendFHE 算子包后，这些算子通过 `torch.ops.ascend_npu_fhe.*` 暴露给
PyTorch / `torch_npu`；未安装或未注册算子包的环境只能进行源码审查、环境检查和 Notebook
入口验证。

## 当前可用状态

| 能力 | 状态 | 说明 |
| --- | --- | --- |
| Ascend C kernel | 已提供 | 位于各 `kernels/<operator>/op_kernel/`。 |
| host shape/tiling | 已提供 | 位于各 `kernels/<operator>/op_host/`。 |
| 算子级 README | 已提供 | 每个算子目录都有独立接口、入口和验证说明。 |
| Notebook 入口 | 已提供 | `notebooks/ascend_npu_fhe_quickstart.ipynb` 用于目标 NPU 环境中的交互检查。 |
| 支持设备 | 已标定 | Atlas A2 / Ascend 910B，SOC 为 `ascend910b`。 |
| `torch.ops.ascend_npu_fhe.*` API | 安装注册后支持 | 安装并注册 AscendFHE 算子包后可通过 `torch_npu` 调用。 |
| 顶层 `CMakeLists.txt` | 未提供 | 当前不能从仓库根目录直接构建完整扩展。 |

现在可以审查源码、准备 CANN 环境、使用 Notebook 做环境或注册检查；不能直接从根目录构建完整
扩展，也不能在未安装注册 AscendFHE 算子包的环境中直接调用 `torch.ops.ascend_npu_fhe.*`。

## Quick Start

这条任务流用于最快完成“拿到源码 -> 确认内容 -> 准备环境 -> 打开交互入口”。真实算子执行
依赖目标 NPU 环境中已经安装并注册 AscendFHE 算子包。

1. 获取源码并查看算子：

```bash
git clone https://github.com/BJTUpupil/AscendFHE.git
cd AscendFHE
```

2. 确认当前仓库内容：

```bash
ls
rg --files kernels
rg --files doc notebooks
```

应能看到 `kernels/`、`doc/` 和 `notebooks/`。其中 `kernels/` 存放算子源码，`doc/` 存放公开文档，
`notebooks/` 存放交互检查入口。

3. 准备 CANN 8.5.0 / Atlas A2 / Ascend 910B 环境：

```bash
conda create -n ascend-fhe python=3.10 -y
conda activate ascend-fhe
conda install ascend::cann-toolkit==8.5.0 -y
conda install ascend::cann-910b-ops==8.5.0 -y
source "${CONDA_PREFIX}/Ascend/ascend-toolkit/set_env.sh"
export ASCEND_HOME_PATH="${CONDA_PREFIX}/Ascend/ascend-toolkit"
```

驱动、固件、PyTorch 和 `torch_npu` 需要按目标 Atlas A2 / Ascend 910B 机器的实际版本安装。
完整安装路径见 [CANN 8.5.0 环境安装方法](doc/environment_install.md)。

4. 验证 NPU 运行环境：

```bash
echo "${ASCEND_HOME_PATH}"
npu-smi info
python -c "import torch, torch_npu; print(torch.npu.is_available())"
```

期望结果是 `ASCEND_HOME_PATH` 指向实际 CANN Toolkit 目录，`npu-smi info` 能识别设备，
Python 命令输出 `True`。

5. 打开交互 Notebook：

```bash
jupyter notebook notebooks/ascend_npu_fhe_quickstart.ipynb
```

Notebook 提交版本默认不执行安装、环境检查或算子调用。进入目标 NPU 环境后，可先启用环境检查：

```python
RUN_INSTALL = False
RUN_ENV_CHECK = True
RUN_OP_TESTS = False
```

6. 仅在完成算子包安装和注册后启用算子测试：

```python
RUN_OP_TESTS = True
```

`RUN_OP_TESTS=True` 只适用于已经完成 AscendFHE 算子包安装和 `torch.ops.ascend_npu_fhe.*`
注册的环境。当前仓库最快可完成的是环境检查和接口入口验证；真正的 NPU 算子执行依赖目标环境中的
算子包安装与注册。

## 文档入口

公开文档位于 `doc/`：

- [文档组织方式](doc/README.md)
- [CANN 8.5.0 环境安装方法](doc/environment_install.md)
- [第三方引用与可执行交互说明](doc/third_party_or_interactive.md)
- [Notebook 一键安装、执行与测试脚本](notebooks/ascend_npu_fhe_quickstart.ipynb)

`docs/` 是本地忽略目录，不作为公开文档入口。

## 独立功能卡片

每个算子当前提供 Ascend C kernel、host tiling 逻辑和算子级 README。安装并注册 AscendFHE
算子包后，表中的调用形式即为公开 `torch_npu` API。

| 独立功能 | 目录 | 功能定位 | torch_npu 调用形式 | 输入输出 | 独立性证明 | 详情文档 |
| --- | --- | --- | --- | --- | --- | --- |
| `AddMod` | `kernels/add_mod` | 逐元素模加 | `torch.ops.ascend_npu_fhe.add_mod(a, b, q)` | 输入 `a,b,q:int32`；输出 `y:int32` | 执行 `(a + b) mod q`，与减法、乘法和变换类算子分离 | [add_mod](kernels/add_mod/README.md) |
| `SubMod` | `kernels/sub_mod` | 逐元素模减 | `torch.ops.ascend_npu_fhe.sub_mod(a, b, q)` | 输入 `a,b,q:int32`；输出 `y:int32` | 执行 `(a - b) mod q`，与模加和模乘路径分离 | [sub_mod](kernels/sub_mod/README.md) |
| `MulModShoup` | `kernels/mul_mod_shoup` | Shoup 预计算模乘 | `torch.ops.ascend_npu_fhe.mul_mod_shoup(a, W, Wprime, q)` | 输入 `a:int32` 和 3 个整数属性；输出 `y:int32` | 使用 Shoup 常量完成单输入逐元素乘法，与双输入 Montgomery 乘法分离 | [mul_mod_shoup](kernels/mul_mod_shoup/README.md) |
| `MontgomeryMul` | `kernels/montgomery_mul` | Montgomery 约减模乘 | `torch.ops.ascend_npu_fhe.montgomery_mul(x, y, q_mu, q)` | 输入 `x,y,q_mu,q:int32`；输出 `z:int32` | 基于 `q_mu` 完成双输入 Montgomery 乘法，与 Shoup 常量乘法分离 | [montgomery_mul](kernels/montgomery_mul/README.md) |
| `BConv` | `kernels/bconv` | RNS 基转换 | `torch.ops.ascend_npu_fhe.bconv(x, lhs_dense, attrs...)` | 输入 `x:int32,lhs_dense:int8`；输出 `y:int32` | 处理 RNS 源基到目标基转换，包含矩阵阶段和误差补偿 | [bconv](kernels/bconv/README.md) |
| `IP` | `kernels/ip` | RNS 内积累加 | `torch.ops.ascend_npu_fhe.ip(x, key, key_shoup, num_rns, d, poly_degree, q_array)` | 输入 `x,key,key_shoup:int32`；输出 `y:int32` | 在 RNS 和分解维度上累加，与逐元素算子和基转换算子分离 | [ip](kernels/ip/README.md) |
| `AutoOp` | `kernels/auto_op` | 自同构重排与符号归一化 | `torch.ops.ascend_npu_fhe.auto_op(x, byte_offsets_32, sign_mask, num_rns, poly_degree, k, q_array)` | 输入 `x,byte_offsets_32:int32,sign_mask:int8`；输出 `dst:int32` | 负责系数重排和模意义取反，与算术和 NTT 路径分离 | [auto_op](kernels/auto_op/README.md) |
| `NTT` | `kernels/ntt` | 五阶段数论变换 | `torch.ops.ascend_npu_fhe.ntt(a_grid, w1_soa, w2_all, qs_tensor, q_mu_tensor, w3_mm2_mat_soa)` | 混合 `int32/int8` 输入；输出 `stage5_out:int32` | 融合 NTT 五阶段计算，与基础模运算和 RNS 辅助算子分离 | [ntt](kernels/ntt/README.md) |

## 仓库结构

```text
AscendFHE/
|-- README.md
|-- LICENSE
|-- doc/
|-- notebooks/
`-- kernels/
    |-- add_mod/
    |-- sub_mod/
    |-- mul_mod_shoup/
    |-- montgomery_mul/
    |-- bconv/
 