## 红墨官方站点上线啦，注册即送100体验积分（每日签到也会随机有40-100积分哦）

<div align="center">

### ✨ 仅开放注册 1000 名 ✨

**无需部署，立即体验红墨的强大功能！**

---

<a href="https://redink.top">
  <img src="images/redink.png" alt="红墨在线体验" width="500" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"/>
</a>

### [点击访问在线体验站 → Redink.top](https://redink.top)

<sub>💡 点击图片或链接即可访问 | 🎯 限量开放，先到先得</sub>

</div>

---

<div align="center">

# 🎨 红墨 - 小红书AI图文生成器

### 让传播不再需要门槛，让创作从未如此简单

![](images/index.gif)

<sub>*红墨首页 - 一句话开启创作之旅*</sub>

---

<img src="images/showcase-grid.png" alt="使用红墨生成的各类小红书封面" width="700" style="border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.12);"/>

<sub>*使用红墨生成的各类小红书封面 - AI驱动，风格统一，文字准确*</sub>

</div>

---

## 💭 写在前面

前段时间默子在 Linux.do 发了一个用 Nano banana Pro 做 PPT 的帖子，收获了 **600+ 点赞**。很多人用 🍌 Nano banana Pro 去做产品宣传图、直接生成漫画等等。我就在想：

> **为什么不拿 🍌2 来做点更功利、更刺激的事情？**

于是就有了这个项目：**一句话 + 一张图片 = 完整小红书图文**

---

## ✨ 效果展示

### 📝 输入一句话，生成完整图文

<table>
<tr>
<td width="50%">

#### 🎯 输入示例

**提示词**：秋季显白美甲（暗广一个：默子牌美甲）

**参考图片**：上传小红书主页截图
- ✅ 包含头像、签名、背景、姓名
- ✅ 自动学习个人风格

</td>
<td width="50%">

#### ⚡ 生成流程

1. **智能大纲** (10-20秒)
  - 自动拆分 6-9 页内容
  - 可自定义每页描述

2. **封面生成** (即时)
  - 风格统一的封面设计

3. **批量生成** (并发)
  - 最多 15 张图同时生成
  - 支持单独重新生成

</td>
</tr>
</table>

---

### 🖼️ 生成步骤展示

<details open>
<summary><b>📋 Step 1: 智能大纲生成</b></summary>

<br>

![大纲示例](./images/example-2.png)

**功能特性：**
- ✏️ 可编辑每页内容
- 🔄 可调整页面顺序（不建议）
- ✨ 自定义每页描述（强烈推荐）

</details>

<details open>
<summary><b>🎨 Step 2: 封面页生成</b></summary>

<br>

![封面示例](./images/example-3.png)

**封面亮点：**
- 🎯 符合个人风格
- 📝 文字准确无误
- 🌈 视觉统一协调

</details>

<details open>
<summary><b>📚 Step 3: 内容页批量生成</b></summary>

<br>

![内容页示例](./images/example-4.png)

**生成说明：**
- ⚡ 并发生成所有页面（默认最多 15 张）
- ⚠️ 如 API 不支持高并发，请在设置中关闭
- 🔧 支持单独重新生成不满意的页面

</details>

---

## 🏗️ 技术架构

<table>
<tr>
<td width="50%" valign="top">

### 🔧 后端技术栈

| 技术 | 说明 |
|------|------|
| **语言** | Python 3.11+ |
| **框架** | Flask |
| **包管理** | uv |
| **文案AI** | Gemini 3 |
| **图片AI** | 🍌 Nano banana Pro |

</td>
<td width="50%" valign="top">

### 🎨 前端技术栈

| 技术 | 说明 |
|------|------|
| **框架** | Vue 3 + TypeScript |
| **构建工具** | Vite |
| **状态管理** | Pinia |
| **样式** | Modern CSS |

</td>
</tr>
</table>

---

## 📦 如何自己部署

### 方式一：Docker 部署（推荐）

**最简单的部署方式，一行命令即可启动：**

```bash
docker run -d -p 12398:12398 -v ./history:/app/history -v ./output:/app/output histonemax/redink:latest
```

访问 http://localhost:12398，在 Web 界面的**设置页面**配置你的 API Key 即可使用。

**使用 docker-compose（可选）：**

下载 [docker-compose.yml](https://github.com/HisMax/RedInk/blob/main/docker-compose.yml) 后：

```bash
docker-compose up -d
```

**Docker 部署说明：**
- 容器内不包含任何 API Key，需要在 Web 界面配置
- 使用 `-v ./history:/app/history` 持久化历史记录
- 使用 `-v ./output:/app/output` 持久化生成的图片
- 可选：挂载自定义配置文件 `-v ./text_providers.yaml:/app/text_providers.yaml`

---

### 方式二：本地开发部署

**前置要求：**
- Python 3.11+
- Node.js 18+
- pnpm
- uv

### 1. 克隆项目
```bash
git clone https://github.com/HisMax/RedInk.git
cd RedInk
```

### 2. 配置 API 服务

复制配置模板文件：
```bash
cp text_providers.yaml.example text_providers.yaml
cp image_providers.yaml.example image_providers.yaml
```

编辑配置文件，填入你的 API Key 和服务配置。也可以启动后在 Web 界面的**设置页面**进行配置。

### 3. 安装后端依赖
```bash
uv sync
```

### 4. 安装前端依赖
```bash
cd frontend
pnpm install
```

### 5. 启动服务

**启动后端:**
```bash
uv run python -m backend.app
```
访问: http://localhost:12398

**启动前端:**
```bash
cd frontend
pnpm dev
```
访问: http://localhost:5173

---

## 🎮 使用指南

### 基础使用
1. **输入主题**: 在首页输入想要创作的主题,如"如何在家做拿铁"
2. **生成大纲**: AI 自动生成 6-9 页的内容大纲
3. **编辑确认**: 可以编辑和调整每一页的描述
4. **生成图片**: 点击生成,实时查看进度
5. **下载使用**: 一键下载所有图片

### 进阶使用
- **上传参考图片**: 适合品牌方,保持品牌视觉风格
- **修改描述词**: 精确控制每一页的内容和构图
- **重新生成**: 对不满意的页面单独重新生成

---

## 🔧 配置说明

### 配置方式

项目支持两种配置方式：

1. **Web 界面配置（推荐）**：启动服务后，在设置页面可视化配置
2. **YAML 文件配置**：直接编辑配置文件

### 文本生成配置

配置文件: `text_providers.yaml`

```yaml
# 当前激活的服务商
active_provider: openai

providers:
  # OpenAI 官方或兼容接口
  openai:
    type: openai_compatible
    api_key: sk-xxxxxxxxxxxxxxxxxxxx
    base_url: https://api.openai.com/v1
    model: gpt-4o

  # Google Gemini（原生接口）
  gemini:
    type: google_gemini
    api_key: AIzaxxxxxxxxxxxxxxxxxxxxxxxxx
    model: gemini-2.0-flash
```

### 图片生成配置

配置文件: `image_providers.yaml`

```yaml
# 当前激活的服务商
active_provider: gemini

providers:
  # Google Gemini 图片生成
  gemini:
    type: google_genai
    api_key: AIzaxxxxxxxxxxxxxxxxxxxxxxxxx
    model: gemini-3-pro-image-preview
    high_concurrency: false  # 高并发模式

  # OpenAI 兼容接口
  openai_image:
    type: image_api
    api_key: sk-xxxxxxxxxxxxxxxxxxxx
    base_url: https://your-api-endpoint.com
    model: dall-e-3
    high_concurrency: false
```

### 高并发模式说明

- **关闭（默认）**：图片逐张生成，适合 GCP 300$ 试用账号或有速率限制的 API
- **开启**：图片并行生成（最多15张同时），速度更快，但需要 API 支持高并发

⚠️ **GCP 300$ 试用账号不建议启用高并发**，可能会触发速率限制导致生成失败。

---

## ⚠️ 注意事项

1. **API 配额限制**:
   - 注意 Gemini 和图片生成 API 的调用配额
   - GCP 试用账号建议关闭高并发模式

2. **生成时间**:
   - 图片生成需要时间,请耐心等待（不要离开页面）

---

## 🤝 参与贡献

欢迎提交 Issue 和 Pull Request!

如果这个项目对你有帮助,欢迎给个 Star ⭐

### 未来计划
- [ ] 支持更多图片格式，例如一句话生成一套PPT