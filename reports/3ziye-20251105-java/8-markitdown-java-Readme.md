# MarkItDown Java

[![Java](https://img.shields.io/badge/Java-11+-orange.svg)](https://openjdk.java.net/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Maven](https://img.shields.io/badge/Maven-3.6+-red.svg)](https://maven.apache.org/)

> **中国网络空间安全协会2025年开源安全奖励项目 - 重写赛道**
>
> 本项目是对微软开源项目 MarkItDown 的完整Java重写版本，旨在为中文用户提供更好的文档转换体验

微软 MarkItDown 的 Java 重写版本 - 将各种文档格式转换为 Markdown

## 🚀 快速开始

### 环境要求

- Java 11 或更高版本
- Maven 3.6+
- 可选: Tesseract OCR (用于图片文字识别)

### 安装使用

```bash
# 克隆项目
git clone https://github.com/DuanYan007/markitdown-java.git
cd markitdown-java

# 编译打包
mvn clean package -DskipTests

# 基本使用
java -jar target/markitdown-java.jar document.pdf

# 指定输出文件
java -jar target/markitdown-java.jar document.docx -o output.md

# 批量转换
java -jar target/markitdown-java.jar *.pdf
```

### 命令行选项

```bash
Usage: markitdown [OPTIONS] INPUT_FILES...

选项:
  -o, --output <FILE>          输出文件或目录
  --include-images            包含图片 (默认: true)
  --no-images                 排除图片
  --include-tables            包含表格 (默认: true)
  --no-tables                 排除表格
  --include-metadata          包含元数据 (默认: true)
  --no-metadata               排除元数据
  --ocr                       使用 OCR 文字识别
  --language <LANG>           OCR 语言 (默认: auto)
  --table-format <FORMAT>     表格格式: github, markdown, pipe (默认: github)
  --image-format <FORMAT>     图片格式: markdown, html, base64 (默认: markdown)
  --max-file-size <SIZE>      最大文件大小 (默认: 50MB)
  --temp-dir <DIR>            临时目录
  -v, --verbose               详细输出
  -q, --quiet                 静默模式
  -h, --help                  显示帮助
  -V, --version               显示版本信息
```

## 📋 项目简介

MarkItDown Java 是一个功能强大的文档转换工具，支持将多种文档格式转换为 Markdown 格式。这是对微软开源项目 MarkItDown 的 Java 语言重写版本，专门针对中文环境和安全合规要求进行了优化。

### 🎯 主要特性

- **多格式支持**: PDF, DOCX, PPTX, XLSX, HTML, 图片, 音频, 文本等
- **OCR 文字识别**: 支持图片文字提取（需要 Tesseract）
- **表格处理**: 智能识别和转换表格
- **元数据提取**: 保留文档元信息
- **命令行界面**: 简单易用的 CLI 工具
- **独立Markdown引擎**: 内置独立的Java对象到Markdown转换引擎
- **高性能**: 基于 Java 11+ 优化，支持并发处理
- **中文优化**: 针对中文文档处理和显示进行优化
- **文件体积优化**: 稳定优化版本，43MB 完整功能打包
- **安全编码**: 遵循安全编码规范，通过安全扫描

### 🏆 项目背景

- **参赛赛道**: 中国网络空间安全协会 2025年开源安全奖励 - 重写赛道
- **技术目标**: 将微软的 Python 原版 MarkItDown 完整重写为 Java 版本
- **安全考虑**: 在重写过程中遵循安全编码规范，确保代码质量和安全性
- **开源承诺**: 遵循 MIT 许可证，促进开源生态发展

### 📁 支持的文件格式

| 格式 | 扩展名 | 状态 | 备注 |
|------|--------|------|------|
| PDF | .pdf | ✅ 完全支持 | 支持文本和图片提取，优化的段落结构保持 |
| Microsoft Word | .docx, .doc | ✅ 完全支持 | 支持格式化文本和表格 |
| Microsoft PowerPoint | .pptx, .ppt | ✅ 完全支持 | 支持幻灯片文本和备注 |
| Microsoft Excel | .xlsx, .xls | ✅ 完全支持 | 支持多工作表处理 |
| HTML | .html, .htm | ✅ 完全支持 | 保持原有格式 |
| 图片 (OCR) | .jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp | ✅ 完全支持 | 中英文OCR识别 |
| 音频文件 | .mp3, .wav, .ogg, .flac, .m4a, .aac | ✅ 元数据支持 | 提取音频元数据信息 |
| 文本文件 | .txt, .csv, .json, .xml, .md, .log | ✅ 完全支持 | 多种编码支持 |

## 🔧 开发信息

### 项目结构

```
MarkItDown Java/
├── src/main/java/com/markitdown/
│   ├── api/                    # API 接口定义
│   ├── cli/                    # 命令行界面
│   ├── config/                  # 配置管理
│   ├── converter/               # 文档转换器
│   ├── core/                   # 核心引擎
│   ├── exception/               # 异常处理
│   └── utils/                   # 工具类
├── src/main/java/com/markdown/engine/  # 独立Markdown引擎
│   ├── config/                 # Markdown引擎配置
│   ├── context/                # 渲染上下文
│   ├── renderer/               # 类型渲染器
│   └── impl/                   # 引擎实现
└── src/test/                      # 单元测试
```

### 技术栈

- **核心框架**: Java 11+
- **命令行**: PicoCLI 4.7.5
- **PDF 处理**: Apache PDFBox 3.0.1
- **Office 文档**: Apache POI 5.2.5
- **HTML 解析**: jsoup 1.17.2
- **OCR**: Tess4J 5.8.0
- **元数据提取**: Apache Tika 2.9.1
- **JSON处理**: Jackson 2.16.1 (核心组件)
- **日志**: SLF4J + Logback
- **构建工具**: Maven 3.6+
- **打包优化**: Maven Shade + 最小化打包

### 独立Markdown引擎特性

除了文档转换功能，本项目还包含一个完全独立的Markdown引擎：

- **Java对象转Markdown**: 支持任意Java对象转换为Markdown格式
- **智能渲染**: 根据对象类型自动选择最佳渲染方式
- **可扩展架构**: 支持自定义渲染器和配置
- **流式构建**: 提供MarkdownBuilder用于程序化文档构建
- **线程安全**: 支持多线程并发使用

```java
// 使用独立Markdown引擎
MarkdownEngine engine = MarkdownEngineFactory.createEngine();
MarkdownConfig config = MarkdownConfig.builder()
    .includeTables(true)
    .tableFormat("github")
    .customOption("useEmoji", true)
    .build();

// 转换复杂Java对象
Map<String, Object> data = Map.of(
    "姓名", "张三",
    "年龄", 25,
    "技能", Arrays.asList("Java", "Python", "数据分析")
);
String markdown = engine.convertWithMetadata(data, metadata, config);
```

## 📝 使用示例

### 基础文档转换

```bash
# PDF 转 Markdown
java -jar markitdown-java-1.0.0-SNAPSHOT.jar 合同.pdf -o 合同.md

# Word 文档转换
java -jar markitdown-java-1.0.0-SNAPSHOT.jar 报告.docx -o 报告.md

# Excel 表格转换
java -jar markitdown-java-1.0.0-SNAPSHOT.jar 数据.xlsx --table-format github
```

### 高级功能

```bash
# OCR 图片识别（中文）
java -jar markitdown-java-1.0.0-SNAPSHOT.jar 扫描件.jpg --ocr --language chi_sim

# 批量处理多种格式
java -jar markitdown-java-1.0.0-SNAPSHOT.jar *.docx *.pdf *.xlsx --verbose

# 输出到指定目录
java -jar markitdown-java-1.0.0-SNAPSHOT.jar 文档夹/* -o ./输出目录/
```

## 🔄 与