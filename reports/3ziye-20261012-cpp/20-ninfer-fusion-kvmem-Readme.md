# NInfer Fusion KVMem

**面向 Windows / NVIDIA GPU 的长上下文推理实验：用 KVMem 环、主机 KV 存储与按需检索，让设备 KV 池可以小于逻辑上下文，并在后续轮次复用已有上下文。**

本项目基于 NInfer `0.11.0-rtx3090`，发布融合后的源码、复现记录和验证工具。它是 NInfer 的**下游衍生项目**；基座与第三方算法来源见 [署名与改动声明](NOTICE.md)。

> [!WARNING]
> 这是初期实验版本，仍有未定位问题，不保证回答正确性与运行稳定性。维护者建议用于个人探索，不建议用于商用；该建议不改变 [Apache-2.0 许可](LICENSE)。使用前请读 [Bug 账本及状态复核](已知问题-初期版本.md)。

[获取引擎](https://github.com/1314521gjy/ninfer-fusion-kvmem/releases) · [编译指南](编译指南-怎么编.md) · [复现白皮书](复现白皮书-NInfer-KVMem环-20261002.md) · [实测回执](实测回执与反馈.md) · [问题反馈](https://github.com/1314521gjy/ninfer-fusion-kvmem/issues)

## 这个项目做了什么

长上下文会增加 KV 缓存占用。本项目将三个容量分别配置：

| 配置 | 含义 | 示例 |
|---|---|---|
| `--max-context` | 单序列的逻辑上下文上限 | 262,144 token |
| `--kv-capacity` | 设备端 KV 池容量 | 17,920 token（280 页） |
| `--host-kv-mib` | 主机端 KV 存储预算 | 16,384 MiB |

KVMem 环保留常驻窗口，将其他页降到主机层；需要时按内容相关性选页、搬回设备并装配注意力窗口。host-backed 复用与惰性物化让后续轮次可以继续使用主机驻留的检查点。按卡档位则为内核调度选择路由。

**小 KV 池不代表模型权重也能装进小显存**，也不代表检索与完整注意力在任意任务上质量等价。模型权重、运行工作区、投机头、CUDA Graph 和主机内存都需要单独预算。机制、容量公式与负控见 [白皮书](复现白皮书-NInfer-KVMem环-20261002.md) §2–§4。

## 从哪里开始

| 你的目标 | 入口 |
|---|---|
| 先试运行服务 | 下方“获取与启动”；先准备引擎、依赖和模型 |
| 自己编译或修改引擎 | [编译指南](编译指南-怎么编.md)与 [完整源码树](src-tree/fusion-engine-src/) |
| 重跑长上下文与复用实验 | [复现白皮书](复现白皮书-NInfer-KVMem环-20261002.md) §8–§10、[验证脚本说明](verify/README-判据与负控.md) |
| 看实测结果和反例 | [实测回执](实测回执与反馈.md)、[Bug 账本](已知问题-初期版本.md) |
| 核对项目贡献与第三方来源 | [新增能力与已解决问题](我方-新增能力与已解决问题.md)、[NOTICE](NOTICE.md) |
| **最短验收清单（照用）** | 下方“怎么确认 KVMem 与复用在工作”一节，加 [验证脚本说明](verify/README-判据与负控.md) —— 每条判据都写了**“怎么变红”**，只会变绿的判据不算判据 |

## 获取与启动

### 1. 准备引擎、依赖与模型

源码可以直接克隆；运行引擎和模型时，使用纯 ASCII 路径，例如 `D:\ninfer\`，避免已记录的中文路径读取问题。

```powershell
git clone https://github.com/1314521gjy/ninfer-fusion-kvmem.git
cd ninfer-fusion-kvmem
```

引擎有两种获取方式：从 [Releases](https://github.com/1314521gjy/ninfer-fusion-kvmem/releases) 下载，或按下方步骤编译当前源码。

截至 **2026-10-07**，公开 Release [`engine-v0.11.0-kvmem-20261003`](https://github.com/1314521gjy/ninfer-fusion-kvmem/releases/tag/engine-v0.11.0-kvmem-20261003) 提供：

| 文件 | 目标架构 | 对应显卡系列 |
|---|---|---|
| `ninfer-serve-86.exe` | `sm_86` | RTX 30 系 |
| `ninfer-serve-89.exe` | `sm_89` | RTX 40 系 |
| `ninfer-serve-120a.exe` | `sm_120a` | RTX 50 系 |
| `SHA256SUMS.txt` | — | 上述引擎的哈希清单 |

这些资产**不是完整运行套件**：该 Release 没有附带 DLL 或模型。请按对应构建的依赖准备 CUDA / FFmpeg / libcurl 运行库，将所需 DLL 放在 EXE 同目录；具体依赖与已记录的分发待办见 [NOTICE](NOTICE.md) §6–§7。可用 `Get-FileHash <引擎路径> -Algorithm SHA256` 与下载的清单对照。

**源码与 Release 要分别看**：`main` 上 2026-10-07 的修复与验证记录，不能作为 2026-10-03 引擎资产已包含这些修复的证明。测试时请记录源码提交或 EXE 哈希。

本仓库与该 Release **均不含模型权重或 `.ninfer` 模型制品**。需要另行准备兼容的 NInfer v3 模型；转换说明见 [源码树的权重转换文档](src-tree/fusion-engine-src/docs/weight-conversion.md)。从仓库根目录先做模型体检：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\自检-模型件.ps1 `
  -Model D:\ninfer\models\model.ninfer -VramGb 16
```

将路径与 `16` 替换为实际模型和显存容量。体检只读文件，不启动引擎；裸件输出 `MODELCHECK_VERDICT=BARE`、退出码 3，表示可读但没有投机头。损坏或截断的文件应先重新获取。

### 2. 启动一个文本服务

下面是 **sm_89 / RTX 40 系的参数模板**，不是所有显卡的通用配方。将引擎与模型路径替换为本机实际路径；自编译时引擎文件名为 `ninfer-serve.exe`。该示例分配 16 GiB 主机 KV 预算，需另留模型及运行工作区的显存、主机内存。

在 PowerShell 中设置环境变量并启动，变量必须由启动引擎的同一个终端传入：

```powershell
$engine = 'D:\ninfer\engine\ninfer-serve-89.exe'
$model = 'D:\ninfer\models\model.ninfer'

$env:NINFER_KV_WINDOW = '16384'
$env:NINFER_KV_RETRIEVE = '8192'
# 历史开关：新件已不再读取 NINFER_KV_RING；环的门是 NINFER_KV_WINDOW（B30）
$env:NINFER_KV_RING = '1'
$env:NINFER_HOST_PAGEABLE = '1'
$env:NINFER_KV_REUSE_HOSTBACKED = '1'
$env:NINFER_TERNARY_KVMEM_SCORE_QUERY_TAIL = '64'

& $engine $model `
  --host 127.0.0.1 --port 8091 --model-id ninfer-local `
  --max-context 262144 --kv-capacity 17920 --kv-dtype k8v4 `
  --host-kv-mib 16384 --prefill-chunk 1024 `
  --max-concurrency 1 --max-shared-prefixes 0 `
  --default-max-tokens 1024 --default-reasoning-effort none
```

模板不启用投机解码或视觉，以免假定模型含有相应组件。需要投机解码时，以模型体检输出为准：

| 模型组件 | 可用参数 |
|---|---|
| 仅 `text` | 不加 `--spec` |
| 含 `mtp` | `--spec mtp`；MTP-only 件不要加 `--lm-head-draft` |
| 含 `dflash2` 与对应 proposal head | 按模型配方使用 `--spec dflash2 --draft-tokens 4 --lm-head-draft` |

小卡还需核对权重与工作区占用，不能直接照搬大卡的 dflash2 配方。CUDA Graph 捕获失败时，可尝试 `--no-cuda-graph`，这是已记录的绕道，根因仍未定位。

### 3. 发一条真实请求

在另一个 PowerShell 终端执行：

```powershell
Invoke-RestMethod -Uri 'http://127.0.0.1:8091/v1/models'

$body = @{
  model = 'ninfer-local'
  messages = @(@{ role = 'user'; content = 'What is 17 + 25? Reply with the number only.' })
  max_tokens = 64
  stream = $false
} | ConvertTo-Json -Depth 6

$response = Invoke-RestMethod `
  -Uri 'http://127.0.0.1:8091/v1/chat/completions' `
  -Method Post -ContentType 'application/json' -Body $body
$response.choices[0].message.content
```

预期答案是 `42`。`/v1/models` 返回 200 只证明模型列表接口可访问；必须检查真实生成请求、答案与进程存活，才能判断服务是否可用。其他 API 与响应字段见 [服务文档](src-tree/fusion-engine-src/docs/serving.md)。

### 4. 控制思考（reasoning）通道（可选）

两个开关都**只在开启思考时生效**：

| 想要 | 怎么做 |
|---|---|
| 限制单轮思考长度 | 请求体加 `"thinking_budget": 1500`（OpenAI 路由，与 Anthropic 路由同义）。`0` / 省略 / `null` = 不限；**显式给小值（< 1024）会被拒**：HTTP 400 并点名 `thinking_budget` |
| 抑制思考里的逐字复读 | 启动加