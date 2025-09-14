#### 🛠️ 快速开始
```bash
pip install awesome-project
```

## 🔧 高级配置

### GitHub Token 设置

为避免 API 限制，建议设置 GitHub Personal Access Token:

1. 访问 [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. 生成新的 token (只需 public_repo 权限)
3. 设置环境变量或配置文件:

```bash
# 环境变量方式
export GITHUB_TOKEN="xxx"

# 或编辑配置文件
echo 'GITHUB_TOKEN="xxx"' >> config.conf
```

### Git 自动提交

配置自动提交功能:

```bash
# 启用自动提交
AUTO_COMMIT=true

# Git 设置
GIT_REMOTE="origin"
GIT_BRANCH="main"
GIT_COMMIT_MESSAGE="📊 Update GitHub trending report"
```

## 🏗️ 架构设计

### 核心组件

1. **github_fetcher.py** - GitHub API 数据获取器
   - 获取热门仓库列表
   - 获取仓库详细信息
   - 获取 README 和语言信息
   - 数据缓存和去重

2. **markdown_generator.py** - Markdown 报告生成器
   - 智能提取项目特性
   - 生成使用场景推荐
   - 格式化部署说明
   - 统计数据分析

3. **run_github_trending.sh** - 主控制脚本
   - 参数解析和配置管理
   - 流程编排和错误处理
   - 定时任务和守护进程
   - Git 集成和通知

### 数据流程

```
GitHub API → 数据获取 → 数据处理 → 报告生成 → 文件保存 → Git提交 → 通知发送
```

### 目录结构

```
github-trending/
├── github_fetcher.py      # 数据获取器
├── markdown_generator.py  # 报告生成器  
├── run_github_trending.sh # 主控制脚本
├── setup.sh              # 安装脚本
├── requirements.txt      # Python依赖
├── config.conf          # 配置文件
├── data/               # 数据目录
├── reports/           # 报告目录
└── logs/             # 日志目录
```

## 🔍 故障排除

### 常见问题

**1. API 限制错误**
```
Error: API rate limit exceeded
```
解决: 设置 GitHub Token

**2. Python 模块缺失**
```
ModuleNotFoundError: No module named 'requests'
```
解决: `pip3 install requests`

**3. 权限错误**
```
Permission denied: ./run_github_trending.sh
```
解决: `chmod +x *.sh *.py`

**4. Git 推送失败**
```
Error: failed to push to remote repository
```
解决: 检查 Git 配置和权限

### 调试模式

启用详细日志:

```bash
# 设置日志级别
export LOG_LEVEL="DEBUG"

# 查看实时日志
tail -f logs/fetch_*.log
```

## 🤝 贡献指南

欢迎贡献代码、报告问题或提出建议!

### 开发环境设置

```bash
# 克隆项目
git clone https://github.com/your-repo/github-trending.git
cd github-trending

# 安装开发依赖
pip3 install -r requirements.txt

# 运行测试
python3 -m pytest tests/

# 代码格式化
black *.py
```

### 提交规范

- feat: 新功能
- fix: 修复bug  
- docs: 文档更新
- style: 代码格式
- refactor: 重构
- test: 测试相关

## 📄 许可证

MIT License

## 🙏 致谢

- [GitHub API](https://docs.github.com/en/rest) - 提供数据源
- [Python Requests](https://requests.readthedocs.io/) - HTTP 客户端
- [Markdown](https://daringfireball.net/projects/markdown/) - 文档格式

## 📞 联系方式

- GitHub Issues: [项目问题反馈](https://github.com/your-repo/github-trending/issues)
- Email: team@3ziye.com
- 文档: [项目文档](https://your-repo.github.io/github-trending/)

---

⭐ 如果这个项目对您有帮助，请给个 Star 支持一下！