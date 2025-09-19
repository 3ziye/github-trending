#!/bin/bash

# GitHub 热门项目自动获取和报告生成脚本
# 作者: GitHub Trending Reporter
# 版本: 1.0.0

set -e  # 遇到错误立即退出

# 配置变量
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="${SCRIPT_DIR}/data"
REPORTS_DIR="${SCRIPT_DIR}/reports"
LOGS_DIR="${SCRIPT_DIR}/logs"
CONFIG_FILE="${SCRIPT_DIR}/config.conf"

# 默认配置
DEFAULT_LANGUAGE=""j
DEFAULT_TIME_RANGE="daily"
DEFAULT_COUNT=10
DEFAULT_TOKEN=""
DEFAULT_AUTO_COMMIT=false

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 日志函数
log() {
    echo -e "${GREEN}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1" >&2
}

warn() {
    echo -e "${YELLOW}[$(date '+%Y-%m-%d %H:%M:%S')] WARNING:${NC} $1" >&2
}

error() {
    echo -e "${RED}[$(date '+%Y-%m-%d %H:%M:%S')] ERROR:${NC} $1" >&2
}

info() {
    echo -e "${BLUE}[$(date '+%Y-%m-%d %H:%M:%S')] INFO:${NC} $1" >&2
}

# 帮助信息
show_help() {
    cat << EOF
GitHub 热门项目自动获取和报告生成工具

用法: $0 [选项]

选项:
    -l, --language LANG     指定编程语言 (如: python, javascript, go)
    -t, --time-range RANGE  时间范围 (daily, weekly, monthly, year, triennial)
    -c, --count COUNT       获取项目数量 (默认: 10)
    -o, --output DIR        输出目录 (默认: reports)
    --token TOKEN           GitHub Personal Access Token
    --title TITLE           报告标题
    --auto-commit           自动提交到 Git 仓库
    --schedule              设置定时任务
    -h, --help              显示帮助信息

示例:
    $0 -l python -t weekly -c 20
    $0 --language javascript --count 15 --auto-commit
    $0 --daemon

配置文件:
    配置文件位置: ${CONFIG_FILE}
    可以在配置文件中设置默认值，命令行参数优先级更高。

环境变量:
    GITHUB_TOKEN            GitHub Personal Access Token
    GITHUB_TRENDING_CONFIG  配置文件路径

EOF
}

# 创建必要目录
create_directories() {
    for dir in "$DATA_DIR" "$REPORTS_DIR" "$LOGS_DIR"; do
        if [[ ! -d "$dir" ]]; then
            mkdir -p "$dir"
            log "创建目录: $dir"
        fi
    done
}

# 加载配置文件
load_config() {
    if [[ -f "$CONFIG_FILE" ]]; then
        log "加载配置文件: $CONFIG_FILE"
        source "$CONFIG_FILE"
    else
        log "配置文件不存在，使用默认配置"
    fi
}

# 创建默认配置文件
create_default_config() {
    cat > "$CONFIG_FILE" << EOF
# GitHub 热门项目获取配置文件
# 所有设置都可以通过命令行参数覆盖

# 基本设置
LANGUAGE="$DEFAULT_LANGUAGE"
TIME_RANGE="$DEFAULT_TIME_RANGE"
COUNT=$DEFAULT_COUNT
GITHUB_TOKEN="$DEFAULT_TOKEN"

# 报告设置
REPORT_TITLE="热门项目报告"
AUTO_COMMIT=$DEFAULT_AUTO_COMMIT

# Git 设置 (当 AUTO_COMMIT=true 时)
GIT_REMOTE="origin"
GIT_BRANCH="main"
GIT_COMMIT_MESSAGE="📊 Update GitHub trending report"

# 日志设置
LOG_LEVEL="INFO"
LOG_RETENTION_DAYS=30
EOF
    log "已创建默认配置文件: $CONFIG_FILE"
}

# 检查依赖
check_dependencies() {
    local deps=("python3" "git")
    local missing_deps=()
    
    for dep in "${deps[@]}"; do
        if ! command -v "$dep" &> /dev/null; then
            missing_deps+=("$dep")
        fi
    done
    
    if [[ ${#missing_deps[@]} -gt 0 ]]; then
        error "缺少依赖: ${missing_deps[*]}"
        error "请安装缺少的依赖后重试"
        exit 1
    fi
    
    # 检查 Python 模块
    if ! python3 -c "import requests, json" &> /dev/null; then
        warn "Python requests 模块未安装，尝试自动安装..."
        pip3 install requests || {
            error "无法安装 requests 模块，请手动安装: pip3 install requests"
            exit 1
        }
    fi
}

# 获取项目数据
fetch_data() {
    local language="$1"
    local time_range="$2"
    local count="$3"
    local token="$4"
    
    local timestamp=$(date +"%Y%m%d_%H%M%S")
    local data_file="${DATA_DIR}/github_trending_${timestamp}.json"
    local log_file="${LOGS_DIR}/fetch_${timestamp}.log"
    
    log "开始获取 GitHub 热门项目数据..."
    info "语言: ${language:-全部}"
    info "时间范围: $time_range"
    info "数量: $count"
    
    local cmd="python3 ${SCRIPT_DIR}/github_fetcher.py"
    cmd="$cmd --time-range $time_range --count $count --output $data_file"
    
    if [[ -n "$language" ]]; then
        cmd="$cmd --language $language"
    fi
    
    if [[ -n "$token" ]]; then
        cmd="$cmd --token $token"
    fi
    
    # 执行获取命令
    if eval "$cmd" > "$log_file" 2>&1; then
        log "数据获取完成: $data_file"
        echo "$data_file"
    else
        error "数据获取失败，查看日志: $log_file"
        cat "$log_file"
        exit 1
    fi
}

# 生成报告
generate_report() {
    local data_file="$1"
    local title="$2"

    log  "生成报告: $data_file title: $title ..."
    
    if [[ ! -f "$data_file" ]]; then
        error "数据文件不存在: $data_file"
        exit 1
    fi
    
    local timestamp=$(date +"%Y%m%d_%H%M%S")
    local report_file="${REPORTS_DIR}/github_report_${timestamp}.md"
    local log_file="${LOGS_DIR}/report_${timestamp}.log"
    
    log "开始生成 Markdown 报告..."
    
    local cmd="python3 ${SCRIPT_DIR}/markdown_generator.py"
    cmd="$cmd $data_file --output $report_file --title '$title'"
    
    if eval "$cmd" > "$log_file" 2>&1; then
        log "报告生成完成: $report_file"
        echo "$report_file"
    else
        error "报告生成失败，查看日志: $log_file"
        cat "$log_file"
        exit 1
    fi
}

# Git 提交
git_commit_report() {
    local report_file="$1"
    
    if [[ ! -f "$report_file" ]]; then
        error "报告文件不存在: $report_file"
        return 1
    fi
    
    log "提交报告到 Git 仓库..."
    
    # 检查是否在 Git 仓库中
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        warn "当前目录不是 Git 仓库，跳过自动提交"
        return 0
    fi
    
    # 添加文件
    git add "$report_file"
    git add "$DATA_DIR"
    
    # 检查是否有变更
    if git diff --cached --quiet; then
        warn "没有变更需要提交"
        return 0
    fi
    
    # 提交
    local commit_message="${GIT_COMMIT_MESSAGE:-📊 Update GitHub trending report} - $(date '+%Y-%m-%d %H:%M')"
    if git commit -m "$commit_message"; then
        log "Git 提交完成"
        
        # 推送到远程
        if [[ -n "${GIT_REMOTE:-}" ]] && [[ -n "${GIT_BRANCH:-}" ]]; then
            if git push "${GIT_REMOTE}" "${GIT_BRANCH}"; then
                log "推送到远程仓库完成"
            else
                warn "推送到远程仓库失败"
            fi
        fi
    else
        error "Git 提交失败"
        return 1
    fi
}

# 清理旧文件
cleanup_old_files() {
    local retention_days="${LOG_RETENTION_DAYS:-30}"
    
    log "清理超过 ${retention_days} 天的旧文件..."
    
    # 清理日志文件
    find "$LOGS_DIR" -name "*.log" -mtime +${retention_days} -delete 2>/dev/null || true
    
    # 清理旧的数据文件 (保留最近的10个)
    ls -t "${DATA_DIR}"/github_trending_*.json 2>/dev/null | tail -n +11 | xargs rm -f 2>/dev/null || true
    
    log "文件清理完成"
}
# 设置定时任务
setup_schedule() {
    local cron_entry="${SCHEDULE_CRON:-0 9 * * *} $SCRIPT_DIR/$0 --daemon"
    
    log "设置定时任务..."
    
    # 检查是否已存在
    if crontab -l 2>/dev/null | grep -q "$SCRIPT_DIR/$0"; then
        warn "定时任务已存在"
        return 0
    fi
    
    # 添加到 crontab
    (crontab -l 2>/dev/null; echo "$cron_entry") | crontab -
    
    log "定时任务设置完成: $cron_entry"
}

# 主要处理流程
run_pipeline() {
    log "run_pipeline..."
    local language="$1"
    local time_range="$2"
    local count="$3"
    local token="$4"
    local title="$5"
    
    local start_time=$(date +%s)
    log "========== 开始执行 GitHub 热门项目获取流程 =========="
    
    # 获取数据
    log "获取数据"
    local data_file
    data_file=$(fetch_data "$language" "$time_range" "$count" "$token")
    
    # 生成报告
    log "生成报告"
    local report_file
    report_file=$(generate_report "$data_file" "$title")
    
    # 自动提交
    log "自动提交"
    if [[ "${AUTO_COMMIT:-false}" == "true" ]]; then
        git_commit_report "$report_file"
    fi
    
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    log "========== 流程执行完成，耗时: ${duration}秒 =========="
    log "📄 报告文件: $report_file"
}

# 解析命令行参数
parse_args() {
    local language=""
    local time_range="daily"
    local count=10
    local token=""
    local title="GitHub 热门项目报告"
    local auto_commit=false
    local schedule_mode=false
    
    while [[ $# -gt 0 ]]; do
        case $1 in
            -l|--language)
                language="$2"
                shift 2
                ;;
            -t|--time-range)
                time_range="$2"
                shift 2
                ;;
            -c|--count)
                count="$2"
                shift 2
                ;;
            --token)
                token="$2"
                shift 2
                ;;
            --title)
                title="$2"
                shift 2
                ;;
            --auto-commit)
                auto_commit=true
                shift
                ;;
            -h|--help)
                show_help
                exit 0
                ;;
            *)
                error "未知参数: $1"
                show_help
                exit 1
                ;;
        esac
    done
    
    # 环境变量覆盖
    token="${token:-${GITHUB_TOKEN:-}}"
    
    if [[ "$schedule_mode" == "true" ]]; then
        setup_schedule
        exit 0
    fi
    
    # 设置全局变量
    AUTO_COMMIT="$auto_commit"
    
    # 执行主流程
    run_pipeline "$language" "$time_range" "$count" "$token" "$title"
}

# 主函数
main() {
    # 创建必要目录
    log "创建必要目录"
    create_directories
    
    # 检查依赖
    log "检查依赖"
    check_dependencies
    
    # 创建默认配置文件 (如果不存在)
    log "创建默认配置文件 (如果不存在)"
    if [[ ! -f "$CONFIG_FILE" ]]; then
        create_default_config
    fi
    
    # 加载配置
    log "加载配置"
    load_config
    
    # 解析参数并执行
    log "解析参数并执行"
    if [[ $# -eq 0 ]]; then
        # 无参数时显示帮助
        show_help
        exit 0
    fi
    
    parse_args "$@"
}

# 信号处理
trap 'error "脚本被中断"; exit 130' INT
trap 'error "脚本被终止"; exit 143' TERM

# 执行主函数
main "$@"
