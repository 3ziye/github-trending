# MaterialDFT

MaterialDFT 是一个独立开发的实验性 DFT 代码库，提供与 VASP 兼容的输入输出格式。当前重点是 PBE、static、non-spin、单线程计算路径，通过 VASP 风格输入输出和本地 C++/pybind11 后端运行算例，而后与相同输入的 VASP 跑出来的结果作为对标基线。

## 当前仓库覆盖

当前仓库覆盖了与 VASP PBE static non-spin 对应的单线程计算路径。目标输入形式是 VASP 风格的 `INCAR`、`POSCAR`、`KPOINTS`，运行时会根据 `POTCAR` 库组装赝势信息，并在 `runs/` 下生成 VASP-like 输出文件，例如 `OUTCAR`、`OSZICAR`、`vasprun.xml`、`CHGCAR`、`CONTCAR`、`EIGENVAL` 和 `DOSCAR`。

仓库主要模块如下：

- `cpp_core/`：C++ 自实现计算核心，包括平面波基、FFT、局域/非局域赝势、PAW 运行时、PBE/Libxc 接口、SCF 循环、blocked Davidson 对角化、混合、能量与输出组装。
- `src/materialdft/`：Python API、运行服务、输入准备、manifest 生成、后端调度和 VASP-like I/O。
- `src/materialdft_cpp_core/`：pybind11 C++ 扩展的 Python 包装入口。
- `scripts/`：常用运行脚本，包括 `scripts/run_cpp_core.sh`。
- `schema/`、`openapi/`：manifest/API contract 定义。
- `tests/`：单元测试、数值路径测试、VASP-like 输出测试和部分 parity/debug 测试。
- `docs/`：公开资料、审计笔记和实现依据材料。
- `example/`：测试用例输入示例。
- `cases/`：测试报告中涵盖的全部算例输入。

如需与 VASP 结果做数值对比，仍需使用与 VASP 一致的 POTCAR 文件。POTCAR 属于 VASP 授权材料，本仓库不内置、不分发；用户需在持有有效 VASP license 的前提下自备 `potpaw_PBE.64` 文件夹，并在运行时通过 `POTCAR_ROOT` 指向该目录。

## 实现方法

实现流程以 VASP Wiki 公开信息为主线，依据其公开描述实现 static SCF 计算流程，包括输入参数默认值、POTCAR 元数据、KPOINTS 语义、电子步迭代、混合、能量项和输出字段。

VASP Wiki 没有披露或描述不足的部分，会参考 DFT 相关公开论文，以及 Quantum ESPRESSO、GPAW、ABINIT 等第三方开源 DFT 代码中的实现方法进行补齐。对于公开资料中仍然缺少依据的细节，则采用 controlled probe 的方式，让 AI 在受控算例、数值 trace 和输出差异中自由探索候选实现，再通过回归测试和 parity 检查筛选。

也就是说，当前实现完全基于公开资料、第三方开源实现和数值实验独立构建，不涉及 VASP 源码或任何需要 license 才能获取的信息。

## 参数支持

当前只对标了 VASP 的 `static`、`non-spin` 计算路径。对角化迭代仅实现与 VASP `ALGO = Normal` 同类的 blocked Davidson 路径；其他对角化模式不作为当前正式支持目标。

当前 VASP 风格输入解析支持以下 `INCAR` 参数，并映射到内部 `input.settings`：

| VASP 参数 | 内部字段 | 当前说明 |
| --- | --- | --- |
| `ENCUT` | `encut_ev` | 平面波截断能。当前 cpp_core 仍要求显式提供。 |
| `EDIFF` | `ediff` | 电子步能量收敛阈值。缺省按 VASP 默认值 `1E-4 eV`。 |
| `GGA` | `xc` | `GGA = PE` 映射为 `PBE`；PBE 运行需要带 Libxc 的 cpp_core 构建。 |
| `ISPIN` | `ispin` | 当前正式支持 `ISPIN = 1` non-spin 路径。 |
| `ISMEAR` | `ismear` | 当前 cpp_core 支持 `-5`、`-1`、`0`、`1`。 |
| `SIGMA` | `sigma_ev` | 展宽参数，单位 eV。 |
| `NELM` | `nelm` | 最大电子步数。 |
| `NELMDL` | `nelmdl` | 初始电子步控制，部分路径支持。 |
| `NSW` | `nsw` | 当前目标为 `NSW = 0` static。 |
| `IBRION` | `ibrion` | static 路径通常为 `-1`；relax 非当前拟合目标。 |
| `ISIF` | `isif` | static 输出/应力相关路径有限支持。 |
| `NBANDS` | `nbands` | 能带数。 |
| `ISYM` | `isym` | 对称性开关/约化路径有限支持。 |
| `AMIX` | `amix` | 密度混合参数。VASP Wiki 披露的默认值：PAW datasets 为 `0.4`；US-PPs 下 `ISPIN=1` 为 `0.8`、`ISPIN=2` 为 `0.4`。当前 PBE PAW static non-spin 主路径默认 `0.4`。 |
| `BMIX` | `bmix` | Kerker/混合相关参数。VASP Wiki 默认值为 `1.0`；当前 cpp_core 未显式提供时有效默认值为 `1.0 Å^-1`。 |
| `IMIX` | `imix` | 混合算法选择。VASP Wiki 默认值为 `4`；当前 cpp_core 输入默认值为 `-1`，表示由 cpp_core 自动选择有效混合路径。当前支持 `-1`、`0`、`1`、`2`、`4`、`5`。 |
| `LREAL` | `lreal` | 当前 C++ 主路径仅支持等效 `False`。 |
| `PREC` | `prec` | 影响内部精度/网格策略的有限支持。 |
| `NCORE`、`KPAR`、`NPAR` | 同名内部字段 | 解析和运行元数据支持有限；当前目标仍为单线程/单 rank。 |

`KPOINTS` 当前支持 VASP 常见的 automatic mesh 格式，包括 Gamma 和 Monkhorst-Pack 网格。`POSCAR` 支持常见直接坐标结构输入。

## 使用指南

### 安装指南

建议使用 Python 3.10+ 环境。示例：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

如果只使用 Python API、输入解析或 manifest 工具，不编译 C++ 扩展，可以跳过 native build：

```bash
MaterialDFT_BUILD_CPP_CORE=0 pip install -e .[dev]
```

运行 PBE 路径需要 Libxc。Ubuntu/Debian 系统可以先尝试安装发行版包：

```bash
sudo apt-get update
sudo apt-get install -y libxc-dev pkg-config
```

安装后确认版本和 CMake 配置是否可见：

```bash
pkg-config --modversion libxc
find /usr -name 'LibxcConfig.cmake' -o -name 'libxc.pc' 2>/dev/null
```

如果系统包版本过旧，或需要使用自定义 Libxc，可以从源码安装到仓库下的 `third_party/libxc`：

```bash
mkdir -p third_party/src
cd third_party/src

curl -L -o libxc-6.2.2.tar.gz \
    https://gitlab.com/libxc/libxc/-/archive/6.2.2/libxc-6.2.2.tar.gz
tar xf libxc-6.2.2.tar.gz

cmake -S libxc-6.2.2 -B libxc-6.2.2-build -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX="$PWD/../libxc" \
    -DBUILD_SHARED_LIBS=ON \
    -DENABLE_FORTRAN=OFF

cmake --build libxc-6.2.2-build --parallel 4
cmake --install libxc-6.2.2-build

cd ../..
```

自定义安装完成后，后续 CMake 通过 `MaterialDFT_LIBXC_PREFIX` 指向该路径，例如 `third_party/libxc`。

构建 C++ cpp_core 的示例：

```bash
cmake -S . -B build/cpp_core_libxc -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DMaterialDFT_USE_LIBXC=ON \
    -DMaterialDFT_LIBXC_PREFIX=/path/to/libxc-6-or-newer

cmake --build build/cpp_core_libxc --parallel 4
```

如果系统已有可被 CMake 找到的 Libxc，也可以省略 `MaterialDFT_LIBXC_PREFIX`：

```bash
cmake -S . -B build/cpp_core_libxc -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DMaterialDFT_USE_LIBXC=ON

cmake --build build/cpp_core_libxc --parallel 4
```

CMake 构建需要 C++17 编译器、CMake、Ninja、FFTW3、LAPACK/BLAS、Python 开发头文件和 pybind11。若本地没有 pybind11，项目 CMake 可通过 FetchContent 获取；若系统 Python 头文件缺失，仓库会回退到 `third_party/python_headers/`。

### 算例运行指南

将 VASP 格式的 `INCAR`、`POSCAR`、`KPOINTS` 放入同一个算例文件夹(见example/input)。脚本会在该文件夹中查找或生成 `manifest.json`，并根据 `POTCAR_ROOT` 指向的 POTCAR 库组装运行所需赝势。

示例命令：

```bash
CASE_DIR=/home/MaterialDFT-demo/S01_static_metal_bulk_mp_001/input \
POTCAR_ROOT=/home/potpaw_PBE.64 \
PYTHON_BIN=/home/.venv/bin/python \
bash scripts/run_cpp_co