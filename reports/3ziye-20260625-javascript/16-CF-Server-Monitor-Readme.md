# [CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor)

一个基于 Cloudflare Workers + D1 + Durable Objects 的多服务器监控探针系统，支持实时监控、历史数据查看、延迟追踪、地图展示等功能。兼容主流Linux系统，Alpine Linux，OpenWrt，Windows系统。**演示地址**：<https://tz.dashdeep.dpdns.org/>

**当前版本：V2.7.4**

<2.7.1 新增了功能，需要**升级安装脚本** 才能生效，否则无法获取丢包率
```
# Linux
curl -sL https://你的项目.你的子域.workers.dev/install.sh | bash -s install
# Alpine
curl -sL https://你的项目.你的子域.workers.dev/install-alpine.sh | sh -s install
# OpenWrt
curl -sL https://你的项目.你的子域.workers.dev/install-openwrt.sh | sh -s install
```
<= 2.6.9 版本,使用方式一部署方式，需要在Workers & Pages页面，点击 **Settings**，修改Build configuration的Deploy command为：`npx wrangler deploy --keep-vars`，否则会导致API\_SECRET丢失。旧key可用通过
```
# Linux
cat /etc/systemd/system/cf-probe.service
# OpenWrt,Alpine
cat /etc/init.d/cf-probe
# >2.6.9版本
cat /etc/config/cf-probe/config.conf
```
获取，再重新设置环境变量API\_SECRET（注意是设置顶部的变量和密钥），最后再同步数据。

<details>
<summary>更新记录</summary>

- V2.7.4 添加允许跨域配置，为后续版本额外功能做铺垫，前端加上跨域配置，修改成HASH模式，修改country为region，数据库自动维护
- V2.7.3.3 压缩定时任务4个为2个，避免超出免费额度
- V2.7.3.2 合并通知告警，其他代码逻辑优化
- V2.7.3.1 当request.cf返回`cf object not available`错误，导致国家/地区代码获取失败，使用request.headers获取作为备选
- V2.7.3 新增服务器到期提醒功能，调整后台设置页面布局
- V2.7.2 新增支持多分区磁盘统计功能以及其他优化，增加[图文教程](https://huilang.me/cf-server-monitor-setup/)
- V2.7.1 新增国内四线路丢包率监控与历史图表，新增GPU字段与图表展示（GPU暂未测试），后台新增 Cloudflare D1/Workers 每日额度查询功能；

- V2.7.0 将每日数据清理改为每月1号执行的表轮换任务, 删除旧表将不再扣除D1消耗,前端图表支持查看最长7天的历史数据,优化脚本一键升级功能
- V2.6.10 修复了方式一部署方式，同步后丢失API\_SECRET的问题
- V2.6.9 修复地图显示问题，重构OpenWrt安装脚本，新增OpenRC服务支持
- V2.6.8 修复网卡统计误统计非目标网卡流量的问题,修复Alpine环境UDP连接数统计错误,本次更新需要重新安装脚本才能生效
- v2.6.7 增加了月流量统计校正功能，以及首页流量统计展示
- v2.6.6 增加上报间隔，Ping方式，流量重置日入库功能
- V2.6.5 修复了部分系统启动时间获取错误的问题，TCP/UDP上报格式错误导致失败问题，新增详情页面实时网速展示
- V2.6.4 增加了 **月流量统计** 功能，升级后请在后台手动点击 **升级数据库** 来更新数据库结构。不然会导致数据库结构错误，影响正常运行。同时需要在后台设置重置日期，并重新安装脚本。
- V2.6.3 应大家需求，增加自定义Ping设置
- V2.6.0 降低了 50% 的D1写入消耗，强烈建议升级，升级后请在后台手动点击 升级数据库 或者 重建数据库 。
- V2.5.0 增加客户端上报数据后，在不占用D1消耗的情况下，前端WebSocket实时刷新数据
- V2.4.0 版本主要优化了D1读写占用，使项目消耗大大降低，以及增加了防护避免被刷。
</details>

## ✨ 功能特点

- 📊 **实时监控**：CPU、GPU、内存、磁盘、网络、进程数、连接数、负载均衡
- 📈 **历史图表**：支持7天历史数据查看
- 🌍 **全球地图**：可视化展示服务器分布
- 🔔 **离线告警**：支持 Telegram 和企业微信通知
- 📱 **响应式**：支持桌面端和移动端
- 🔄 **自动部署**：GitHub Actions 一键部署
- 🗺️ **网络质量追踪**：国内电信/联通/移动/字节延迟与丢包率监测
- 🔒 **服务器隐藏**：可设置特定服务器对非登录用户隐藏
- ↕️ **拖拽排序**：后台拖拽调整服务器显示顺序
- 🌐 **双语支持**：支持中文和英文界面自由切换
- 🧪 **本地测试**：支持本地模拟数据生成，方便开发和测试
- 🔐 **Turnstile 验证**：集成 Cloudflare Turnstile 人机验证，增强 API 安全性
- 🔑 **JWT 认证**：登录系统采用 JWT token 认证，支持自定义密钥
- 📉 **额度查询**：后台可查询 Cloudflare D1 当日读写行数与 Workers 请求量
- ⚡ **实时推送**：基于 Durable Objects + WebSocket，探针上报后页面立即刷新，无轮询延迟

## 🚀 快速开始

### 前置要求

- [Cloudflare 账户](https://dash.cloudflare.com/)
- [GitHub 账户](https://github.com/)

<details>
<summary>方式一：Cloudflare Workers 连接GitHub仓库（推荐使用，方便同步）图文教程 -> https://huilang.me/cf-server-monitor-setup/</summary>

### 第一步：Fork 项目

点击右上角 **Fork** 按钮，将项目 Fork 到你的 GitHub 账户。

### 第二步：新建 Cloudflare Workers

1. 登录 [Cloudflare 控制台](https://dash.cloudflare.com/)
2. 进入 **[Workers & Pages](https://dash.cloudflare.com/?to=/:account/workers-and-pages)**
3. 点击 **Create application**
4. 选择 Continue with GitHub（第一次使用需要连接 GitHub 账户），选择本项目
5. Project Name填写：`cf-server-monitor`
6. Build command 填写：`npm run build:frontend`
7. Deploy command 填写：`npx wrangler deploy --keep-vars`
8. 点击 **Deploy**，成功会在底部显示`✨ Success! Build completed.`

### 第三步：配置环境变量

1. 在当前Workers & Pages页面，点击 **Settings**
2. 在Variables and secrets找到API\_SECRET，点右侧编辑，填写密码（建议使用随机数,不要包含特殊字符比如%），点Deploy保存部署，等待30秒左右部署完成

</details>

<details>
<summary>方式二：GitHub Action 自动部署</summary>

### 第一步：Fork 项目

点击右上角 **Fork** 按钮，将项目 Fork 到你的 GitHub 账户。

### 第二步：创建 D1 数据库

1. 登录 [Cloudflare 控制台](https://dash.cloudflare.com/)
2. 进入 **[Workers & Pages](https://dash.cloudflare.com/?to=/:account/workers-and-pages)**  → **[D1 SQL Database](https://dash.cloudflare.com/?to=/:account/workers/d1)**
3. 点击 **Create database**
4. 数据库名称填写：`server-monitor-db`
5. 点击 **Create**
6. 记录下生成的 **Database ID**，稍后会用到

### 第三步：获取 Cloudflare 配置

#### 获取 Account ID

**方式一：从右侧面板获取**

1. 打开 [Cloudflare Dashboard](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
2. 在右侧面板找到 **Account ID**
3. 复制保存

**方式二：从 URL 中获取**

- 登录后访问任意 Cloudflare 页面，例如 [Workers & Pages](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
- URL 中 `dash.cloudflare.com/` 之后的那串字符就是 Account ID

#### 获取 API Token

1. 打开 [API Tokens 页面](https://dash.cloudflare.com/profile/api-tokens)
2. 点击 **Create Token/创建令牌**
3. 选择（**Edit Cloudflare Workers/编辑 Cloudflare Workers**）模板
4. 在 **Account Resources/帐户资源** 选择你的账户
5. 点击 **Continue to summary/继续以显示摘要**→ **Create Token/创建令牌**
6. 复制生成的 Token（只显示一次！）

### 第四步：配置 GitHub Secrets

1. 打开你 Fork 的 GitHub 仓库
2. 进入 **Settings** → **Secrets and variables** → **Actions**
3. 点击 **New repository secret**，依次添加以下 5 个密钥：

| Secret 名称        | 值                  | 说明                                     |
| ---------------- | ------------------ | -------------------------------------- |
| `CF_API_TOKEN`   | 第三步获取的 Token       | Cloudflare API 令