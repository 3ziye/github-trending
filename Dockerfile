# GitHub 热门项目获取工具 - Docker 镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    git \
    curl \
    cron \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY github_fetcher.py .
COPY markdown_generator.py .
COPY run_github_trending.sh .

# 设置权限
RUN chmod +x *.py *.sh

# 创建必要目录
RUN mkdir -p data reports logs

# 创建非 root 用户
RUN useradd -m -u 1000 github-user && \
    chown -R github-user:github-user /app
USER github-user

# 环境变量
ENV PYTHONUNBUFFERED=1
ENV LOG_LEVEL=INFO
ENV DATA_DIR=/app/data
ENV REPORTS_DIR=/app/reports
ENV LOGS_DIR=/app/logs

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python3 -c "import requests; print('OK')" || exit 1

# 暴露数据卷
VOLUME ["/app/data", "/app/reports", "/app/logs"]

# 默认命令
CMD ["./run_github_trending.sh", "--help"]

# 构建标签
LABEL maintainer="team@3ziye.com"
LABEL version="1.0.0"
LABEL description="GitHub trending projects fetcher and report generator"