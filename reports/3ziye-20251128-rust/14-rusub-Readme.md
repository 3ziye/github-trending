<div align="center">

# rusub

🚀 高速、智能的子域枚举工具 (Rust)

[![Rust](https://img.shields.io/badge/rust-1.70%2B-orange.svg)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

</div>

## 📋 目录
1. [快速开始](#1-快速开始)
2. [配置参数](#2-配置参数)
3. [实用示例](#3-实用示例)
4. [输出格式](#4-输出格式)
5. [技术原理](#5-技术原理)
6. [作为库使用](#6-作为库使用)
7. [许可与免责声明](#7-许可与免责声明)

## 1. 快速开始

### 核心特性

- **🧠 启发式扫描**：默认智能生成 512 个候选子域，无需字典
- **📚 字典扫描**：10 万+ 词表已内置，支持自定义字典
- **💾 断点续传**：自动保存进度，中断后可继续
- **⚡ 高性能**：异步并发（默认 500），支持速率控制
- **📊 多格式输出**：JSONL / TXT / JSON / CSV，可选 gzip 压缩
- **🛡️ 泛解析过滤**：自动检测并过滤泛解析记录
- **🌐 跨平台 DNS**：自动读取系统 DNS 配置（Windows/Linux/macOS）

### 安装

```bash
git clone https://github.com/adysec/rusub.git
cd rusub
cargo build --release

# 可选：安装到系统
cargo install --path .
```

**编译后的二进制文件（约 4.7 MB）：**
- ✅ 10 万+ 子域词表已内置
- ✅ 无外部依赖
- ✅ 可在任意目录运行

### 基本用法

```bash
# 默认扫描（启发式 512 候选，JSONL 输出）
rusub enum example.com

# 深度扫描（1024 候选）
rusub enum example.com --heuristic-max 1024

# 使用自定义字典
rusub enum example.com -f wordlist.txt

# 多域名扫描
rusub enum -d target.com -d example.com
```

## 2. 配置参数

### 🎯 基础参数

| 参数 | 说明 | 默认值 | 示例 |
|------|------|--------|------|
| `-d, --domain` | 目标域名（可重复） | - | `-d example.com -d test.com` |
| `--stdin` | 从标准输入读取域名 | - | `cat domains.txt \| rusub enum --stdin` |
| `-f, --filename` | 字典文件路径 | 内置 | `-f wordlist.txt` |
| `--domain-list` | 域名列表文件 | - | `--domain-list domains.txt` |

### 📊 输出参数

| 参数 | 说明 | 默认值 | 示例 |
|------|------|--------|------|
| `-o, --output` | 输出文件路径 | stdout | `-o results.jsonl` |
| `--output-type` | 输出格式 | jsonl | `txt / json / jsonl / csv` |
| `--gzip` | 启用 gzip 压缩 | auto¹ | `--gzip` |
| `--not-print` | 不打印到终端 | false | `--not-print` |
| `--pure-output` | 纯净输出（仅结果）| auto² | `--pure-output` |
| `--only-alive` | 仅输出存活域名 | auto² | `--only-alive` |

> ¹ 输出文件以 `.gz` 结尾时自动启用  
> ² json/jsonl 格式自动启用

### ⚡ 性能参数

| 参数 | 说明 | 默认值 | 示例 |
|------|------|--------|------|
| `-b, --band` | 速率限制 | 3m | `-b 10M` 或 `-b 5000` |
| `-c, --concurrency` | 并发数 | 500 | `-c 1000` |
| `--timeout` | 查询超时（秒） | 6 | `--timeout 10` |
| `--retry` | 失败重试次数 | 3 | `--retry 5` |
| `-r, --resolvers` | DNS 解析器（可重复） | 系统³ | `-r 8.8.8.8 -r 1.1.1.1` |

> ³ **DNS 自动配置（跨平台）：**
> - 🔧 自动读取系统配置（Windows/Linux/macOS）
> - 🛡️ 过滤本地回环（127.*）和 IPv6 地址
> - 🌐 无系统配置时回退到 1.1.1.1 / 8.8.8.8
> - ✏️ 使用 `-r` 可覆盖默认配置

### 🧠 启发式参数

| 参数 | 说明 | 默认值 | 推荐值 |
|------|------|--------|--------|
| `--heuristic-max` | 候选子域数量 | 512 | 256 / 512 / 1024 / 2048 |

**扫描方案：**
- 🚀 **轻量**（256）：快速验证
- ⚖️ **标准**（512）：日常使用，默认
- 🔍 **深度**（1024）：更全面
- 💎 **全面**（2048）：最大覆盖

### 🔧 其他参数

| 参数 | 说明 | 默认值 | 可选值 |
|------|------|--------|--------|
| `--log-level` | 日志级别 | info | error / warn / info / debug / silent |

## 3. 实用示例

### 📌 基础扫描

```bash
# 启发式扫描 - 标准（512 候选，默认）
rusub enum target.com

# 启发式扫描 - 深度（1024 候选）
rusub enum target.com --heuristic-max 1024

# 启发式扫描 - 全面（2048 候选）
rusub enum target.com --heuristic-max 2048

# 启发式扫描 - 轻量（256 候选）
rusub enum target.com --heuristic-max 256

# 使用自定义字典
rusub enum target.com -f custom.txt

# 多域名扫描
rusub enum -d target.com -d example.com -d test.com

# 从文件读取域名列表
rusub enum --domain-list domains.txt

# 从标准输入读取
cat domains.txt | rusub enum --stdin
```

### 📊 输出控制

```bash
# JSONL 格式（默认）
rusub enum target.com -o results.jsonl

# JSON 格式
rusub enum target.com --output-type json -o results.json

# CSV 格式
rusub enum target.com --output-type csv -o results.csv

# TXT 格式
rusub enum target.com --output-type txt -o results.txt

# 自动压缩
rusub enum target.com -o results.jsonl.gz

# 提取子域名
rusub enum target.com | jq -r '.subdomain'

# 提取 IP 地址
rusub enum target.com | jq -r '.answers[]'

# 过滤特定子域
rusub enum target.com | grep -E "admin|api|dev"
```

### 🎯 DNS 配置

```bash
# 使用系统 DNS（默认）
rusub enum target.com

# 指定单个 DNS
rusub enum target.com -r 8.8.8.8

# 指定多个 DNS
rusub enum target.com -r 8.8.8.8 -r 1.1.1.1 -r 1.0.0.1

# 使用国内 DNS
rusub enum target.com -r 114.114.114.114 -r 223.5.5.5
```

### ⚡ 性能调优

```bash
# 快速扫描（低并发）
rusub enum target.com -c 200 --timeout 3

# 标准扫描（默认）
rusub enum target.com -c 500 --timeout 6

# 高速扫描（高并发）
rusub enum target.com -c 2000 -b 50M --timeout 3

# 极速扫描（适合内网）
rusub enum target.com -c 5000 -b 100M --timeout 2 --retry 1
```

### 🔄 实用技巧

```bash
# 实时监控 + 保存结果
rusub enum target.com | tee results.jsonl

# 静默模式（无日志）
rusub enum target.com --log-level silent

# 断点续传（自动）
rusub enum target.com -f big-wordlist.txt -o results.jsonl
# 中断后重新运行相同命令即可继续

# 批量处理
for domain in $(cat targets.txt); do
    rusub enum $domain -o ${domain}.jsonl
done

# 工具链结合
rusub enum target.com | jq -r '.subdomain' | httpx -silent | grep "200"

# 过滤并提取活跃子域
rusub enum target.com | jq -r 'select(.answers != null) | .subdomain'
```

## 4. 输出格式

### 📊 JSONL（默认）

流式 JSON，每行一个记录：

```json
{"subdomain":"www.example.com","answers":["93.184.216.34"],"records":[{"rtype":"A","data":"93.184.216.34"}]}
{"subdomain":"api.example.com","answers":["10.0.0.1","10.0.0.2"],"records":[{"rtype":"A","data":"10.0.0.1"},{"rtype":"A","data":"10.0.0.2"}]}
```

*