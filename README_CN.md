<h1 align="center" style="border-bottom: none">
    <a href="" target="_blank">
        <alt="github-trending" src="" width="100" height="100">
    </a>
    <br>Github-Trending
</h1>

<div align="center" style="line-height: 2;">
  [<a href="/README.md">English</a>] | [<a href="/README_CN.md">中文(简体)</a>]
</div>

该项目包含三个核心模块：一是数据获取模块，通过 API 抓取 GitHub 热门项目（具备过滤与缓存功能）；二是报告生成模块，用于生成 Markdown 格式报告；三是Bash 脚本，负责编排工作流程（支持定时任务与 Git 自动提交功能）。


# 🎯 系统核心功能

## 1. 数据获取模块 (github_fetcher.py)

调用 GitHub API 获取热门项目
支持按语言、时间范围过滤
获取项目详细信息、README、语言统计
支持数据缓存，避免重复请求

## 2. 报告生成模块 (markdown_generator.py)

智能解析 README 内容
自动提取项目特性和部署说明
生成详细的 Markdown 报告
包含统计数据和可视化表格

## 3. 自动化脚本 (run_github_trending.sh)

Bash 脚本编排整个流程
支持定时任务和守护进程模式
Git 自动提交功能
多种通知方式支持

## 4. 完整部署方案

一键安装脚本
Docker 容器化部署
详细的配置说明文档

---


# 🚀 快速使用
基本使用流程：
进入容器后：

```
./run_github_trending.sh -l python -t weekly -c 20
```

生成的报告包含：

📊 项目统计概览（总星标数、语言分布等）
🎯 每个项目的核心特性
🎨 智能推荐的适用场景
🛠️ 从 README 提取的部署方法
📝 详细的项目信息表格

💡 系统优势

无数据库依赖 - 直接调用 GitHub API，轻量级部署
智能内容提取 - 自动分析 README，提取关键信息
灵活配置 - 支持多种参数和配置方式
完整自动化 - 从数据获取到报告生成一键完成
扩展性强 - 模块化设计，易于扩展功能

这个系统可以帮您：

定时跟踪 GitHub 技术趋势
生成专业的技术报告
自动化技术调研流程
为团队提供技术选型参考

您可以根据需要调整配置参数，比如关注特定编程语言、设置获取频率等。系统设计灵活，既可以单次使用，也可以部署为长期运行的服务