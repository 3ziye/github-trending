# JLib Inspector

> **⚠️ EXPERIMENTAL - NOT PRODUCTION READY**  
> This project is currently in experimental/development phase and is **not suitable for production environments**. Use for development, testing, and evaluation purposes only.

<!-- BADGES -->
[![CI/CD Pipeline](https://github.com/brunoborges/jlib-inspector/actions/workflows/ci.yml/badge.svg)](https://github.com/brunoborges/jlib-inspector/actions/workflows/ci.yml)
[![Security & Maintenance](https://github.com/brunoborges/jlib-inspector/actions/workflows/security.yml/badge.svg)](https://github.com/brunoborges/jlib-inspector/actions/workflows/security.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Java](https://img.shields.io/badge/Java-21%2B-orange.svg)](https://openjdk.java.net/)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-green.svg)](https://nodejs.org/)
<!-- /BADGES -->

A comprehensive Java application monitoring dashboard that tracks JAR dependencies loaded during application runtime. The system consists of a Java agent, a standalone data collection server, and a modern React-based web dashboard to exemplify data visualization.

## 🎯 Why JLib Inspector?

When security vulnerabilities like **Log4Shell** strike, organizations face a critical challenge: **identifying which production systems are affected**. During the Log4j vulnerability crisis, many teams struggled with fundamental questions:

- *"Which of our production applications use Log4j?"*
- *"What version are they running?"*
- *"Are there transitive dependencies we don't know about?"*
- *"How can we quickly assess our exposure across hundreds of services?"*

**The Traditional Approach is Reactive and Error-Prone:**
- 🔍 Manual inspection of deployment artifacts
- 📂 Digging through production file systems
- 📋 Relying on outdated documentation or build scripts
- ⏰ Time-consuming emergency audits during critical security incidents
- 🎯 Missing transitive dependencies hidden deep in the dependency tree

**JLib Inspector Enables Proactive Dependency Visibility:**
- 🚀 **Real-time monitoring** of actual JAR files loaded by running JVMs
- 🎯 **Complete visibility** including transitive dependencies
- 📊 **Centralized dashboard** showing all applications and their dependencies
- 🔄 **Continuous tracking** of what's actually running vs. what's deployed
- ⚡ **Instant response** capability when new vulnerabilities are disclosed
- 🛡️ **Proactive security posture** instead of reactive emergency responses

**Production Reality Check:**
Unlike static analysis of build files, JLib Inspector shows you **exactly what JARs are loaded at runtime** - capturing the full picture including:
- JARs loaded dynamically through plugins or extensions
- Nested JARs within fat/uber JARs  
- Platform-specific dependencies loaded conditionally
- The actual classpath used by the running JVM

When the next security vulnerability emerges, you'll have immediate answers instead of emergency archaeology. 

## 🏗️ Architecture

- **Java Agent**: Instruments Java applications to track JAR loading and usage (shaded agent JAR)
- **JLib Server**: Standalone server that collects and aggregates data from instrumented applications (Port 8080, shaded server JAR)
- **Web Dashboard**: React-based frontend with real-time updates (Ports 3000 for http and 3001 for websocket)

## 📋 Prerequisites

- **Java 21+** (JDK)
- **Maven 4+** (use the included wrapper `./mvnw`)
- **Node.js 18+** and **npm**
- **PowerShell** (for Windows) or equivalent shell

## 🚀 Quick Start

### 1. Build the Project

```bash
# Clone and navigate to the project
cd jlib-inspector

# Build all components (agent + server + sample app)
./mvnw clean package
```

### 2. Start the JLib Server

The JLib Server collects data from instrumented Java applications:

```bash
# Start the data collection server on port 8080 (shaded jar)
java -jar server/target/jlib-inspector-server-1.0-SNAPSHOT-shaded.jar 8080
```

**Expected Output:**
```
JLib HTTP Server started on port 8080
Available endpoints:
  PUT /api/apps/{appId} - Register/update application
  GET /api/apps - List all applications
  GET /api/apps/{appId} - Get application details
  GET /api/apps/{appId}/jars - List application JARs
  GET /health - Health check
```

### 3. Start the Web Dashboard

The unified Express.js server serves the React frontend:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies (first time only)
npm install

# Build and start the unified server on port 3000
npm start
```

**Expected Output:**
```
> jlib-inspector-dashboard@2.0.0 start
> npm run build && node app.js

webpack 5.101.3 compiled successfully
Setting up data fetching schedule...
JLib Dashboard running on http://localhost:3000
WebSocket server running on port 3001
Connecting to JLib Server at http://localhost:8080
```

### 4. Run Java Applications with Monitoring

Instrument any Java application with the JLib Inspector agent:

**For your o