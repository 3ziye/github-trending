![](images/logo.png)

---

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Vue 3](https://img.shields.io/badge/vue-3.x-green.svg)](https://vuejs.org/)

# 红墨 - 小红书AI图文生成器

> 让传播不再需要门槛，让创作从未如此简单

![](images/index.gif)

<p align="center">
  <em>红墨首页</em>
</p>

<p align="center">
  <img src="images/showcase-grid.png" alt="使用红墨生成的各类小红书封面" width="600"/>
</p>

<p align="center">
  <em>使用红墨生成的各类小红书封面 - AI驱动，风格统一，文字准确</em>
</p>



## 写在前面

前段时间默子在 Linux.do 发了一个用 Nano banana Pro 做 PPT 的帖子,收获了 600 多个赞。很多人用🍌Nano banana Pro 去做产品宣传图、直接生成漫画等等。我就在想:**为什么不拿🍌2来做点更功利、更刺激的事情?**

于是就有了这个项目。一句话一张图片生成小红书图文

---

## ✨ 效果展示

### 输入一句话,就能生成完整的小红书图文

#### 提示词：秋季显白美甲（暗广一个：默子牌美甲），图片 是我的小红书主页。符合我的风格生成

#### 同时我还截图了我的小红书主页，包括我的头像，签名，背景，姓名什么的

![示例1](./images/example-1.png)

#### 然后等待10-20秒后，就会有每一页的大纲，大家可以根据的自己的需求去调整页面顺序（不建议），自定义每一个页面的内容（这个很建议）

![示例2](./images/example-2.png)

#### 首先生成的是封面页

![示例3](./images/example-3.png)

#### 然后稍等一会儿后，会生成后面的所有页面（这里是并发生成的所有页面（默认是15个），如果大家的API供应商无法支持高并发的话，记得要去改一下设置）

![示例4](./images/example-4.png)

---

## 🏗️ 技术架构

### 后端
- **语言**: Python 3.11+
- **框架**: Flask
- **AI 模型**:
  - Gemini 3 (文案生成)
  - 🍌Nano banana Pro (图片生成)
- **包管理**: uv

### 前端
- **框架**: Vue 3 + TypeScript
- **构建**: Vite
- **状态管理**: Pinia

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
- [ ] 支持更多图片格式，例如一句话生成一套PPT什么的
- [x] 历史记录管理优化
- [ ] 导出为各种格式(PDF、长图等)

---

## 更新日志

### v1.4.0 (2025-11-30)
- 🏗️ 后端架构重构：拆分单体路由为模块化蓝图（history、images、generation、outline、config）
- 🏗️ 前端组件重构：提取可复用组件（ImageGalleryModal、OutlineModal、ShowcaseBackground等）
- ✨ 优化首页设计，移除冗余内容区块
- ✨ 背景图片预加载和渐入动画，提升加载体验
- ✨ 历史记录持久化支持（Docker部署）
- 🔧 修复历史记录预览和大纲查看功能
- 🔧 优化Modal组件可见性控制
- 🧪 新增65个后端单元测试

### v1.3.0 (2025-11-26)
- ✨ 新增 Docker 支持，一键部署
- ✨ 发布官方 Docker 镜像到 Docker Hub: `histonemax/redink`
- 🔧 Flask 自动检测前端构建产物，支持单容器部署
- 🔧 Docker 镜像内置空白配置模板，保护 API Key 安全
- 📝 更新 README，添加 Docker 部署说明

### v1.2.0 (2025-11-26)
- ✨ 新增版权信息展示，所有页面显示开源协议和项目链接
- ✨ 优化图片重新生成功能，支持单张图片重绘
- ✨ 重新生成图片时保持风格一致，传递完整上下文（封面图、大纲、用户输入）
- ✨ 修复图片缓存问题，重新生成的图片立即刷新显示
- ✨ 统一文本生成客户端接口，支持 Google Gemini 和 OpenAI 兼容接口自动切换
- ✨ 新增 Web 界面配置功能，可视化管理 API 服务商
