<div align="center">
  <img src="public/logo.png" alt="KatelyaTV Logo" width="128" />

  <h1>KatelyaTV</h1>
  <p><strong>跨平台 · 聚合搜索 · 即开即用 · 自托管影视聚合播放器</strong></p>
  <p>基于 <code>Next.js 14</code> · <code>TypeScript</code> · <code>Tailwind CSS</code> · 多源聚合 / 播放记录 / 收藏同步 / 跳过片头片尾 / PWA</p>
  
  <p>
    <a href="#-快速开始">🚀 快速开始</a> ·
    <a href="#-功能特性">✨ 功能特性</a> ·
    <a href="#-部署方案">📋 部署方案</a> ·
    <a href="#-配置说明">⚙️ 配置说明</a>
  </p>
</div>

---

## 📰 项目声明

本项目自「MoonTV」演进而来，为其二创/继承版本，持续维护与改进功能与体验。保留并致谢原作者与社区贡献者。

> **🔔 重要变更**：应用户社区建议，为确保项目长期稳定运行和合规性，内置视频源已移除。现需要用户自行配置资源站以使用完整功能。我们提供了经过测试的推荐配置文件，让您快速上手使用。

---

## ✨ 功能特性

### 🎬 核心功能

- **🔍 聚合搜索**：整合多个影视资源站，一键搜索全网内容
- **📺 高清播放**：基于 ArtPlayer 的强大播放器，支持多种格式
- **⏭️ 智能跳过**：自动检测并跳过片头片尾，手动设置跳过时间段
- **🎯 断点续播**：自动记录播放进度，跨设备同步观看位置
- **📱 响应式设计**：完美适配手机、平板、电脑各种屏幕

### 💾 数据管理

- **⭐ 收藏功能**：收藏喜欢的影视作品，支持跨设备同步
- **📖 播放历史**：自动记录观看历史，快速找回看过的内容
- **👥 多用户支持**：独立的用户系统，每个用户独享个人数据
- **🔄 数据同步**：支持多种存储后端（LocalStorage、Redis、D1、Upstash）
- **🔒 内容过滤**：智能成人内容过滤系统，默认开启安全保护

### 🚀 部署特性

- **🐳 Docker 一键部署**：提供完整的 Docker 镜像，开箱即用
- **☁️ 多平台支持**：Vercel、Docker、Cloudflare Pages 全兼容
- **🔧 灵活配置**：支持自定义资源站、代理设置、主题配置
- **📱 PWA 支持**：可安装为桌面/手机应用
- **📺 TVBox 兼容**：支持 TVBox 配置接口

---

## 🚀 快速开始

### 💡 方案选择指南

| 使用场景     | 推荐方案         | 存储类型     | 成人内容过滤 | 多用户 | 部署难度 |
| ------------ | ---------------- | ------------ | ------------ | ------ | -------- |
| **个人使用** | Docker 单容器    | localstorage | ❌           | ❌     | ⭐       |
| **家庭使用** | Docker + Redis   | redis        | ✅           | ✅     | ⭐⭐     |
| **免费部署** | Vercel + Upstash | upstash      | ✅           | ✅     | ⭐⭐⭐   |
| **生产环境** | Docker + Kvrocks | kvrocks      | ✅           | ✅     | ⭐⭐     |
| **全球加速** | Cloudflare Pages | d1           | ✅           | ✅     | ⭐⭐⭐⭐ |

> 💡 **重要提示**：成人内容过滤功能需要数据库存储支持，不支持 `localstorage` 方式

---

## 📋 部署方案

### 方案一：Docker 单容器（最简单）

**特点**：5 分钟部署，个人使用，无多用户功能

```bash
docker run -d \
  --name katelyatv \
  -p 3000:3000 \
  -e PASSWORD=your_password \
  --restart unless-stopped \
  ghcr.io/katelya77/katelyatv:latest
```

**挂载自定义配置**（可选）：

```bash
docker run -d \
  --name katelyatv \
  -p 3000:3000 \
  -e PASSWORD=your_password \
  -v $(pwd)/config.json:/app/config.json:ro \
  --restart unless-stopped \
  ghcr.io/katelya77/katelyatv:latest
```

### 方案二：Docker + Redis（推荐家庭使用）

**特点**：完整功能，多用户支持，成人内容过滤

```bash
# 1. 下载配置文件
curl -O https://raw.githubusercontent.com/katelya77/KatelyaTV/main/docker-compose.redis.yml
curl -O https://raw.githubusercontent.com/katelya77/KatelyaTV/main/.env.redis.example

# 2. 配置环境变量
cp .env.redis.example .env
```

**编辑 .env 文件**：

```bash
# 管理员账号（必填）
USERNAME=admin
PASSWORD=your_secure_password

# 存储配置
NEXT_PUBLIC_STORAGE_TYPE=redis
REDIS_URL=redis://katelyatv-redis:6379

# 功能开关
NEXT_PUBLIC_ENABLE_REGISTER=true
```

```bash
# 3. 启动服务
docker compose -f docker-compose.redis.yml up -d
```

### 方案三：Docker + Kvrocks（生产环境）

**特点**：极高可靠性，数据持久化到磁盘，节省内存

```bash
# 1. 下载配置文件
curl -O https://raw.githubusercontent.com/katelya77/KatelyaTV/main/docker-compose.kvrocks.yml
curl -O https://raw.githubusercontent.com/katelya77/KatelyaTV/main/.env.kvrocks.example

# 2. 配置环境变量
cp .env.kvrocks.example .env
```

**编辑 .env 文件**：

```bash
# 管理员账号（必填，否则无法登录）
USERNAME=admin
PASSWORD=your_secure_password

# 存储配置
NEXT_PUBLIC_STORAGE_TYPE=kvrocks
KVROCKS_URL=redis://kvrocks:6666

# 功能开关
NEXT_PUBLIC_ENABLE_REGISTER=true
```

```bash
# 3. 启动服务
docker compose -f docker-compose.kvrocks.yml up -d
```

### 方案四：Vercel + Upstash（免费推荐）

**特点**：完全免费，自动 HTTPS，全球 CDN

#### 基础部署

1. **Fork 项目** → [GitHub 仓库](https://github.com/katelya77/KatelyaTV)
2. **部署到 Vercel**：
   - 登录 [Vercel](https://vercel.com/)
   - 导入刚 Fork 的仓库
   - 添加环境变量：`PASSWORD=your_password`
   - 点击 Deploy

#### 多用户配置

3. **创建 Upstash 数据库**：

   - 访问 [Upstash](https://upstash.com/)
   - 创建免费 Redis 数据库
   - 获取 `UPSTASH_URL` 和 `UPSTASH_TOKEN`

4. **添加环境变量**：

```bash
# 存储配置
NEXT_PUBLIC_STORAGE_TYPE=upstash
UPSTASH_URL=https://xxx.upstash.io
UPSTASH_TOKEN=your_token

# 管理员账号
USERNAME=admin
PASSWORD=your_password

# 功能开关
NEXT_PUBLIC_ENABLE_REGISTER=true
```

5. **重新部署** → Vercel Dashboard → Redeploy

### 方案五：Cloudflare Pages + D1（全球加速）

**特点**：全球 CDN，无限带宽，免费 SSL

#### 快速部署

1. **Fork 项目** → [GitHub 仓库](https://github.com/katelya77/KatelyaTV)
2. **创建 Pages 项目**：

   - 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)
   - Pages → Connect to Git → 选择仓库
   - 构建设置：
     ```
     Build command: pnpm install --frozen-lockfile && pnpm run pages:build
     Build output directory: .vercel/output/static
     ```
   - 兼容性标志：`nodejs_compat`

3. **环境变量配置**：

```bash
# 管理员账号
USERNAME=admin
PASSWORD=your_password

# 存储配置
NEXT_PUBLIC_STORAGE_TYPE=d1

# 功能开关
NEXT_PUBLIC_ENABLE_REGISTER=true
```

4. **创建 D1 数据库**（多用户支持）：

```bash
# 安装Wrangler CLI
npm install -g wrangler
wrangler auth login

# 创建数据库
wrangler d1 create katelyatv-db
# ⚠️ 重要：确保在项目根目录下运行此命令
# 如果遇到文件路径错误，请参考 D1_MIGRATION.md 排查指南
wrangler d1 execute katelyatv-db --file=./scripts/d1-init.sql
```

5. **配置数据库绑定** → 在 `wr