# MC-MMD-rust

在 Minecraft 1.20.1 中实现 MMD（MikuMikuDance）模型渲染和物理模拟的 Mod。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 功能特性

- **PMX 模型加载**: 在 Minecraft 中加载和渲染 MMD 模型
- **VMD 动画播放**: 支持骨骼和表情变形的 MMD 动画播放
- **物理模拟**: 使用 原Rapier3D现Bullet3 引擎实现头发、衣物、配饰的实时物理效果
- **GPU 蒙皮**: 通过 Compute Shader 实现高性能顶点蒙皮
- **多层动画**: 支持多个动画同时混合播放

## 架构

本项目由两个主要部分组成：

1. **rust_engine**: 基于 Rust 的 MMD 物理和动画引擎
   - PMX/VMD 格式解析
   - 骨骼层次管理
   - 物理模拟（Bullet3 C FFI）
   - JNI 绑定用于 Java 交互

2. **Minecraft Mod**（Fabric/Forge）: 基于 Java 的渲染和集成
   - OpenGL 模型渲染
   - Compute Shader 蒙皮
   - Iris 光影兼容

## 使用教程

### 安装

1. 将模组 `.jar` 文件放入 `.minecraft/mods/` 目录
2. 启动游戏，模组会自动创建 `3d-skin` 资源目录
3. 将自己的模型和动画文件放入对应目录（详见下文）

### 目录结构

模组使用 `.minecraft/3d-skin/` 作为资源根目录，结构如下：

```
.minecraft/
└── 3d-skin/
    ├── EntityPlayer/          # 玩家模型目录
    │   ├── 模型A/             # 每个子文件夹是一个模型，文件夹名就是模型名
    │   │   ├── model.pmx      # 模型文件（支持 .pmx/.pmd）
    │   │   ├── *.png          # 贴图文件
    │   │   ├── anims/         # 模型专属动画子文件夹（推荐）
    │   │   │   ├── idle.vmd   # 覆盖该模型的待机动画
    │   │   │   └── walk.vmd   # 覆盖该模型的行走动画
    │   │   ├── animations.json # 动画槽位映射配置（UI 自动生成）
    │   │   ├── dance.vmd      # 根目录动画（向后兼容）
    │   │   └── smile.vpd      # 模型专属表情（可选）
    │   └── 模型B/
    │       └── ...
    ├── DefaultAnim/           # 系统预设动画（模组自动释放）
    ├── CustomAnim/            # 用户自定义动画
    ├── DefaultMorph/          # 系统预设表情
    ├── CustomMorph/           # 用户自定义表情
    └── Shader/                # 自定义着色器
```

### 文件夹详解

#### `EntityPlayer/` - 玩家模型目录

存放玩家可用的 MMD 模型。**每个模型必须放在独立的子文件夹中**。

| 文件类型 | 扩展名 | 说明 |
|---------|--------|------|
| 模型文件 | `.pmx` / `.pmd` | 必需，PMX 优先于 PMD |
| 贴图文件 | `.png` / `.jpg` / `.bmp` / `.tga` | 模型引用的贴图 |
| 专属动画 | `.vmd` | 可选，推荐放入 `anims/` 子文件夹 |
| 动画映射 | `animations.json` | 可选，通过 UI 自动生成 |
| 专属表情 | `.vpd` | 可选，仅该模型可用 |

**模型识别规则**：
- 扫描每个子文件夹，查找 `.pmx` 或 `.pmd` 文件
- 若文件夹内有多个模型文件，优先选择 `model.pmx` 或 `model.pmd`
- 若无 `model.*`，则按文件名排序选择第一个

**示例**：
```
EntityPlayer/
├── miku/
│   ├── model.pmx          # 被加载
│   ├── body.png
│   └── face.png
└── shiroha/
    ├── cirno_v2.pmx       # 被加载（文件夹内唯一 pmx）
    ├── cirno_old.pmd      # 忽略（pmx 优先）
    └── texture.png
```

#### `DefaultAnim/` - 系统预设动画

模组首次启动时自动从内置资源释放，包含游戏状态对应的基础动画：

| 动画文件名 | 触发条件 |
|-----------|----------|
| `idle.vmd` | 站立静止 |
| `walk.vmd` | 行走 |
| `sprint.vmd` | 疾跑 |
| `sneak.vmd` | 潜行 |
| `swim.vmd` | 游泳 |
| `crawl.vmd` | 匍匐 |
| `sleep.vmd` | 睡觉 |
| `die.vmd` | 死亡 |
| `elytraFly.vmd` | 鞘翅飞行 |
| `onClimbable.vmd` | 攀爬（静止） |
| `onClimbableUp.vmd` | 攀爬（上） |
| `onClimbableDown.vmd` | 攀爬（下） |
| `onHorse.vmd` / `ride.vmd` | 骑乘 |
| `lieDown.vmd` | 躺下 |
| `swingLeft.vmd` | 左手挥动 |
| `swingRight.vmd` | 右手挥动 |
| `itemActive_*.vmd` | 物品使用动画 |

> **注意**：可直接替换这些文件来自定义基础动画，但建议备份原文件。

#### `CustomAnim/` - 用户自定义动画

存放用户添加的 `.vmd` 动画文件，可通过动作轮盘手动触发播放。

**命名建议**：文件名即为显示名称，建议使用有意义的名称如 `跳舞.vmd`、`打招呼.vmd`。

#### `DefaultMorph/` - 系统预设表情

存放系统预设的 `.vpd` 表情文件（如眨眼、微笑等）。

#### `CustomMorph/` - 用户自定义表情

存放用户添加的 `.vpd` 表情文件，可通过表情轮盘手动触发。

### 动画加载优先级

当需要播放动画时，模组按以下顺序查找（从高到低）：

| 优先级 | 来源 | 路径 | 说明 |
|:---:|------|------|------|
| 1 | **animations.json 映射** | `EntityPlayer/模型名/animations.json` | 用户通过 UI 显式配置 |
| 2 | **anims/ 子文件夹** | `EntityPlayer/模型名/anims/*.vmd` | 同名自动匹配 |
| 3 | **模型根目录** | `EntityPlayer/模型名/*.vmd` | 同名自动匹配（向后兼容） |
| 4 | **自定义动画目录** | `CustomAnim/*.vmd` | 全局自定义动画 |
| 5 | **默认动画目录** | `DefaultAnim/*.vmd` | 系统预设（最低） |

只需配置想要覆盖的槽位，未配置的自动 fallback 到低优先级来源。

**示例**：若 `EntityPlayer/初音未来/anims/idle.vmd` 存在，则该模型的待机动画使用此文件，而非 `DefaultAnim/idle.vmd`。

### 模型专属动画配置

为特定模型定制动画有两种方式：

#### 方式一：自动同名匹配（零配置）

在模型文件夹下创建 `anims/` 子文件夹，放入与动画槽位同名的 VMD 文件即可：

```
EntityPlayer/
└── 初音未来/
    ├── model.pmx
    └── anims/
        ├── idle.vmd      # 自动替代默认待机动画
        ├── walk.vmd      # 自动替代默认行走动画
        └── sprint.vmd    # 自动替代默认疾跑动画
```

可用的槽位名称（即文件名）：

| 槽位名 | 触发条件 | 槽位名 | 触发条件 |
|--------|----------|--------|----------|
| `idle` | 站立静止 | `walk` | 行走 |
| `sprint` | 疾跑 | `sneak` | 潜行 |
| `air` | 空中 | `swim` | 游泳 |
| `crawl` | 匍匐 | `sleep` | 睡觉 |
| `die` | 死亡 | `ride` | 骑乘 |
| `elytraFly` | 鞘翅飞行 | `onHorse` | 骑马 |
| `onClimbable` | 攀爬（静止） | `onClimbableUp` | 攀爬（上） |
| `onClimbableDown` | 攀爬（下） | `lieDown` | 趴下 |
| `swingRight` | 右手挥动 | `swingLeft` | 左手挥动 |
| `itemRight` | 右手物品 | `itemLeft` | 左手物品 |
| `ridden` | 被骑乘 | `driven` | 驾驶 |

#### 方式二：UI 映射（自定义文件名）

当 VMD 文件名与槽位名不同时（如 `我的待机动画_v3.vmd`），可通过游戏内 UI 配置映射：

1. 将 VMD 文件放入模型的 `anims/` 文件夹
2. 进入游戏，打开**模型设置** → 点击底部 **「动画」** 按钮
3. 点击槽位名称（如「待机」）→ 展开下拉列表 → 选择对应的 VMD 文件
4. 点击 **「保存」**

映射关系会自动保存到模型目录下的 `animations.json`：

```json
{
  "idle": "我的待机动画_v3.vmd",
  "walk": "走路_custom.vmd"
}
```

> **提示**：也可以手动编辑 `animations.json`，格式为 `"槽位名": "VMD文件名"`。

### 模型设置

在模型选择界面中选中模型后，可进入模型独立设置界面，包含以下功能：

| 设置项 | 说明 |
|--------|------|
| **眼球追踪** | 开启/关闭眼球追踪，调整最大转动角度 |
| **模型缩放** | 调整模型整体大小（0.5x ~ 2.0x） |
| **快捷绑定** | 将模型绑定到快捷键槽位（1~4），按键快速切换 |
| **动画配置** | 打开动画映射界面，为模型配置专属动画（详见上文） |

### 快捷键操作

#### 主配置轮盘