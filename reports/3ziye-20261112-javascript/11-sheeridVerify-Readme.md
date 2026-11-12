# sheeridVerify · 教学与研究验证流程工作台

[![Tests](https://github.com/JenkinWoo/sheeridVerify/actions/workflows/ci.yml/badge.svg)](https://github.com/JenkinWoo/sheeridVerify/actions/workflows/ci.yml) [![Node.js](https://img.shields.io/badge/Node.js-%3E%3D22.15-43853d)](https://nodejs.org/) [![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](LICENSE)

**[sheeridVerify](https://github.com/JenkinWoo/sheeridVerify)** 是一个基于 Node.js 的验证流程学习项目，提供本地 Web 工作台、任务队列、浏览器表单交互及 HTTP 状态查询，供学校教学、学术研究和获得授权的流程测试使用。

> **用途说明：** 本项目仅以教学与研究为目的提供。使用真实平台前应取得必要授权，遵守适用法律和平台条款；不得伪造身份、学籍或材料，不得冒用信息、骗取权益或绕过资格审核。本项目与 SheerID 及任何学校均无官方隶属或认可关系，也不保证验证成功。详情见 [用途说明与免责声明](DISCLAIMER.md)，代码许可见 [ISC 协议](LICENSE)。

## 文档导航

- [快速开始](#快速开始)
- [工作台与接口说明](#使用)
- [Linux / Instabox 部署、更新与排错](docs/DEPLOYMENT.md)
- [浏览器流程说明](docs/browser-workflow.md)
- [贡献指南](CONTRIBUTING.md) · [安全说明](SECURITY.md) · [免责声明](DISCLAIMER.md)

## 功能

- 通过 fetch 读取验证状态，按当前步骤选择浏览器或材料处理流程。
- 在 Web 页面创建、排队、停止、恢复和删除任务；失败任务删除后可重新提交。
- 按配置限制并发，记录任务进度，提交后默认每 5 秒查询结果。
- 上传原始 PNG、JPEG、PDF 文件，不生成或修改证明材料；交互式真人验证由用户完成。
- 使用访问密码、会话 Cookie、来源检查及写请求令牌保护工作台接口。

## 快速开始

需要 **Node.js >= 22.15** 与 npm。从 GitHub 获取源码：

```bash
git clone https://github.com/JenkinWoo/sheeridVerify.git
cd sheeridVerify
```

使用下载的 ZIP 时，解压后进入其中包含 `package.json` 的目录。在项目根目录安装依赖与浏览器：

```bash
npm ci
npm run browser:install
```

首次使用时复制配置，已有个人配置请直接编辑原文件。

Windows PowerShell：

```powershell
Copy-Item config/sheerid.example.json config/sheerid.local.json
```

Linux / macOS：

```bash
cp -n config/sheerid.example.json config/sheerid.local.json
```

编辑 `config/sheerid.local.json`，设置获授权的国家、学校、`data.organization.emailDomain` 和材料来源。该文件必须是标准 JSON，**不支持 `//` 注释或尾随逗号**。网页会按姓名和配置后缀生成邮箱，仅应使用自己有权使用的真实地址与资料。`document.path` 与 `document.url` 只能填写其中一个；示例配置不包含可直接提交的真实资料。

```bash
npm run web
```

打开 **http://127.0.0.1:8787**。本地默认访问密码为 `JenkinWoo`；对外开放前必须通过 `ONE_WEB_PASSWORD` 更换密码，并配置 HTTPS 入口。Linux 有界面浏览器需要可用桌面；完整部署步骤和环境变量模板见 [部署指南](docs/DEPLOYMENT.md)。

## 测试与贡献

```bash
npm test
```

测试使用模拟接口及本地页面，不向真实验证接口提交数据。未安装 Camoufox 时会跳过浏览器相关用例；网页和浏览器改动应在安装浏览器后验证。GitHub Actions 在 Node.js 22、24 上运行不含已安装浏览器的测试。欢迎按 [贡献指南](CONTRIBUTING.md) 提交问题和改进，报告前请删除个人资料、凭据及真实验证链接。

## 协议与责任说明

项目采用 [ISC License](LICENSE)，与 `package.json` 的协议声明一致。教学与研究是项目的预期用途，不额外收窄 ISC 的开源授权范围。软件按原样提供；第三方依赖和平台分别适用自己的许可和条款。请在使用前阅读完整的 [用途说明与免责声明](DISCLAIMER.md)。

## 社区认可与致谢

本项目认可并支持 [LINUX DO 社区](https://linux.do/) 的开源分享精神，感谢社区为开发者提供技术交流、经验分享与开源项目展示的平台。欢迎在遵守社区规则的前提下交流使用体验与改进建议。

社区推广材料见 [LINUX DO 发帖草稿](docs/LINUX_DO_POST.md)，其中包含推广声明模板与 AI 辅助生成的项目介绍图片。

## 工作原理

当前命令行先用 Node.js 内置 `fetch` 查询状态，再选择执行流程：需要填写学生资料时使用 Camoufox，需要材料验证时使用纯 `fetch` 接口。材料上传保持文件原始内容，不生成或修改证明文件。

## 使用

### 本机 Web 工作台

```powershell
npm run web
```

打开 **http://127.0.0.1:8787**。页面填写验证链接、名、姓、出生日期、代理和访问密码。`url`、`firstName`、`lastName`、`birthDate` 必须由创建任务接口传入，缺少时拒绝入队。邮箱不再由前端传入，而是每次根据配置文件中的 `emailDomain` 域名后缀按 `First name + 点 + Last name @xxx.edu`（如 `first.last@xxxx.edu`）格式自动拼接生成。国家、学校、材料来源、浏览器、超时、邮箱后缀等设置，每次启动任务时从 `config/sheerid.local.json` 读取；提交值不会写回配置文件。当前配置及示例配置不再保存验证链接和个人信息。

`POST /api/jobs` 的 JSON 请求体示例（认证仍使用会话 Cookie 或 `X-Web-Password`，写请求携带 `X-Local-Token`）：

```json
{
  "url": "https://services.sheerid.com/verify/项目ID/?verificationId=验证ID",
  "firstName": "Test",
  "lastName": "Student",
  "birthDate": "2000-01-02",
  "proxy": ""
}
```

当前配置用于 Web/API 模式。若单独使用 CLI，需通过 `--config` 指定含验证链接及所需资料的独立配置；`document.url` 仍是材料下载地址，继续保留在配置中。

代理填写时使用输入的代理，留空或只有空格时强制直连，**不使用配置中的代理、系统代理或代理环境变量**。支持 HTTP/SOCKS5 URL 及 `host:port:username:password`。`AUTOMATION_URL` 也不会覆盖网页输入的链接。

点击“加入队列”后，按入队顺序自动填写、提交，并按配置继续材料流程；`browser.autoFill: false` 时遵循原有手动填写模式。材料来源沿用配置中的 `document.path` 或 `document.url`，下载查询中的姓名使用本次网页输入。点击提交后保留浏览器，只有接口确认进入 `docUpload` 且没有终止错误时，才关闭浏览器并继续上传文件。

并发上限由 `config/sheerid.local.json` 的 `web.concurrency` 控制，默认 1。例如同时执行 3 个任务：

```json
"web": { "concurrency": 3 }
```

并发数必须是正整数，服务启动和新任务入队时读取；调低上限不会中断正在运行的任务，后续等到名额足够再启动。排队任务保存入队时的配置快照。任务使用链接中的 `verificationId` 作为唯一 ID；服务本次运行期间重复提交同一 ID 只返回已有任务，不会重复执行。已停止的任务可以通过“恢复任务”明确重新加入队尾，沿用原资料、代理及配置，重复点击不会重复入队；成功或失败的任务不能通过该按钮重跑。

右侧列出队列，点击任务可查看对应进度和日志；刷新保留选中的任务。表单可连续添加不同任务。停止排队任务会立即取消；停止运行任务会终止后续操作，并在对应浏览器和连接清理完成后释放并发名额，随后才可恢复。恢复时先检查远端验证状态；尚未确认的提交继续只读查询。保留浏览器等待手动操作的任务仍占用名额。停止 Web 服务会取消所有排队和运行任务；队列与历史仅保存在服务内存中，重启后不自动恢复或重试。

Web 默认仅监听本机，不把完整配置返回前端，也不持久保存输入的个人资料和代理密码。提交后的审核等待会继续占用任务名额，直到成功、失败或手动停止。

页面选中失败、已结束或已停止的任务后，可点击“删除当前任务”，再用相同链接重新加入队列。删除最后一个任务会清空进度和活动记录，表单内容继续保留；运行中的任务需先停止并等待资源清理完成。

删除历史任务接口：`DELETE /api/jobs/:verificationId`。请求携带已验证的会话 Cookie 或 `X-Web-Password`，以及 `X-Local-Token`（先通过 `GET /api/session` 获取 `token`），无需请求体。已完成、失败或已停止且清理完资源的任务可删除，成功返回 HTTP 200 和 `{ "id": "verificationId", "deleted": true }`；排队、运行或正在停止的任务返回 HTTP 409 / `JOB_ACTIVE`，请先调用 `POST /api/jobs/:verificationId/cancel` 并等待停止完成；不存在的任务返回 HTTP 404 / `JOB_NOT_FOUND`。删除只移除本服务内存中的任务及活动记录，不撤销验证平台上的提交，也不删除磁盘运行日志。删除后相同 ID 可通过正常创建任务接口重新入队，仍先检查远端状态。

网页只在有排队、运行或正在停止的任务时自动刷新进度；全部任务结束并读取最终日志后停止轮询。加入、恢复或切换任务会重新读取状态；已停止任务不会被反复查询。空闲页面要查看其他页面新建的任务时，刷新网页即可。

首次状态分流和浏览器启动前的检查遇到网络错误、超时或 HTTP 5xx 时最多尝试 3 次