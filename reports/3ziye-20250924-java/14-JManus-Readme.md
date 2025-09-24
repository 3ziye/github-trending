# Spring AI Alibaba JManus

<div align="center">

[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](LICENSE)
[![Java](https://img.shields.io/badge/Java-17+-orange.svg)](https://openjdk.java.net/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.x-green.svg)](https://spring.io/projects/spring-boot)
[![GitHub Stars](https://img.shields.io/github/stars/alibaba/spring-ai-alibaba.svg)](https://github.com/alibaba/spring-ai-alibaba/stargazers)

🌍 [English](./README.md) | [中文](./README-zh.md)

📚 Developer Docs: [Quick Start (EN)](./README-dev-en.md) | [开发者快速入门 (中文)](./README-dev.md)

[About](#-about) • [Quick Start](#-quick-start) • [Contributing](#-contributing)

</div>

![image](https://github.com/user-attachments/assets/07feeb29-c410-4f56-89bf-532210bc1b63)

---

## ✨ About JManus

JManus is a Java implementation of Manus, currently used in many applications within Alibaba Group. It is primarily used for handling exploratory tasks that require a certain degree of determinism, such as quickly finding data from massive datasets and converting it into a single row in a database, or analyzing logs and issuing alerts.

JManus also provides HTTP service invocation capabilities, making it suitable for integration into existing projects. For details, please refer to the developer quick start guide.

## 🎯 JManus Product Features

### 🤖 **Pure Java Manus Implementation**: 

A pure Java multi-agent collaboration implementation that provides a complete set of HTTP call interfaces, suitable for secondary integration by Java developers.

![Image](https://github.com/user-attachments/assets/3d98c1c6-aabb-45a2-b192-7b687093a1ee)

### 🛠️ **Plan-Act Mode**: 

Allows you to precisely control every execution detail, providing extremely high execution determinism.

![Image](https://github.com/user-attachments/assets/a689791f-adf5-44b6-9ea6-151f557a26d4)

### 🔗 **MCP Integration**:

 Natively supports the Model Context Protocol (MCP) for seamless integration with external services and tools.

![Image](https://github.com/user-attachments/assets/2d3f833f-ba45-42b6-8e1b-f3e9cfd40212)

### 📜 **Web Interface for Agent Configuration**:

 Easily configure agents through an intuitive web management interface without modifying code.

![Image](https://github.com/user-attachments/assets/bb25f778-f8c3-46da-9da3-6f7ea2f0917d)

### 🌊 **Infinite Context Handling**: 

Supports precise extraction of target information from massive content without relying on specific long-context models.

![Image](https://github.com/user-attachments/assets/f23e5f27-91e1-4262-83d9-5bfbe5d644d5)


## 🚀 Quick Start

Get JManus up and running in under 5 minutes:

### Prerequisites

- 🌐 **DashScope API Key** (or alternative AI model provider)
- 🐳 **Docker** (for containerized deployment) or ☕ **Java 17+** (for source code execution)

### Method 1: Using Docker (Recommended)

#### 🐳 Using Docker Hub Image

```bash
# Pull the latest develop image
docker pull springaialibaba/jmanus:develop

# Basic startup (temporary data storage)
docker run -d \
  --name jmanus \
  -p 18080:18080 \
  -e DASHSCOPE_API_KEY=your_api_key_here \
  springaialibaba/jmanus:develop

# Or start with data persistence (recommended)
docker run -d \
  --name jmanus \
  -p 18080:18080 \
  -e DASHSCOPE_API_KEY=your_api_key_here \
  -v $(pwd)/h2-data:/app/extracted/h2-data \
  -v $(pwd)/extensions:/app/extracted/extensions \
  springaialibaba/jmanus:develop
```

#### 🇨🇳 Using Alibaba Cloud Image (China Acceleration)

```bash
# Pull Alibaba Cloud accelerated image
docker pull sca-registry.cn-hangzhou.cr.aliyuncs.com/spring-ai-alibaba/jmanus:develop

# Basic startup (temporary data storage)
docker run -d \
  --name jmanus \
  -p 18080:18080 \
  -e DASHSCOPE_API_KEY=your_api_key_here \
  sca-registry.cn-hangzhou.cr.aliyuncs.com/spring-ai-alibaba/jmanus:develop

# Or start with data persistence (recommended)
docker run -d \
  --name jmanus \
  -p 18080:18080 \
  -e DASHSCOPE_API_KEY=your_api_key_here \
  -v $(pwd)/h2-data:/app/extracted/h2-data \
  -v $(pwd)/extensions:/app/extracted/extensions \
  sca-registry.cn-hangzhou.cr.aliyuncs.com/spring-ai-alibaba/jmanus:develop
```

#### 🔧 Advanced Docker Configuration

If you need custom configuration or data persistence:

```bash
# Create data directories
mkdir -p /path/to/jmanus/h2-data
mkdir -p /path/to/jmanus/extensions

# Start with custom configuration (recommended for data persistence)
docker run -d \
  --name jmanus \
  -p 18080:18080 \
  -e DASHSCOPE_API_KEY=your_api_key_here \
  -v /path/to/jmanus/h2-data:/app/extracted/h2-data \
  -v /path/to/jmanus/extensions:/app/extracted/extensions \
  --restart unless-stopped \
  springaialibaba/jmanus:develop
```

> 📁 **Data Storage Information**:
> - **H2 Database**: `/app/extracted/h2-data` - Stores application database files
> - **Runtime Data**: `/app/extracted/extensions` - Stores extensions and runtime configurations
> - It's recommended to mount these two directories for data per