# RiskEngine

Mobile device risk identification SDK + risk operations management platform.

The client-side SDK is built on a Java / C++17 dual-layer architecture for device fingerprinting and environment risk detection, reporting data to the server over an AES-256-GCM encrypted channel. The server persists reported data, evaluates risk through a SpEL-based rule engine, and exposes a web console for device auditing and rule management.

---

## Table of Contents

- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [SDK Documentation](#riskengine-sdk)
- [Server Documentation](#riskengine-server)
- [Deployment](#deployment)
- [Encrypted Transport](#encrypted-transport)
- [License](#license)

---

## Architecture

```
┌──────────────────┐          ┌──────────────────────────────────┐
│   Android App    │          │        RiskEngineServer          │
│                  │          │                                  │
│  ┌────────────┐  │  HTTPS   │  ┌────────────┐  ┌───────────┐  │
│  │ RiskEngine │──┼─────────►│  │ Report API │──│  Report   │  │
│  │    SDK     │  │  POST    │  │ Controller │  │  Service  │  │
│  └────────────┘  │ /api/v1  │  └────────────┘  └─────┬─────┘  │
│                  │ /report  │                         │        │
│  Collector (15)  │          │  ┌──────────┐    ┌──────▼──────┐ │
│  - Java (8)      │          │  │ AES-256  │    │ Rule Engine │ │
│  - Native (7)    │          │  │   -GCM   │    │   (SpEL)   │ │
│                  │          │  └──────────┘    └──────┬─────┘ │
│  Detector (10)   │          │                   ┌──────▼─────┐ │
│  - Root/Hook     │          │                   │   MySQL    │ │
│  - Emulator      │          │                   └────────────┘ │
│  - Debug/Repack  │          │                                  │
│                  │          │  ┌────────────────────────────┐  │
│  Anti-Tamper     │          │  │     Web Admin Console      │  │
│  - CRC Check     │          │  │  (Thymeleaf + Bootstrap 5) │  │
│  - Maps Monitor  │          │  └────────────────────────────┘  │
│  - Custom JNI    │          │                                  │
└──────────────────┘          └──────────────────────────────────┘
```

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| SDK Language | Java 11+ (Android) / C++17 (NDK) |
| SDK Build | Gradle 8.13, AGP 8.13.1, CMake 3.22.1 |
| SDK Dependencies | Gson 2.11.0, OkHttp 4.12.0, HiddenApiBypass 4.3 |
| Server | Spring Boot 4.0.5, Java 17 |
| ORM | Spring Data JPA + Hibernate |
| Database | MySQL 8.0 (prod) / H2 (dev) |
| Frontend | Thymeleaf + Bootstrap 5.3.3 |
| Auth | Spring Security (Form Login + API Key) |
| Rule Engine | Spring Expression Language (SpEL) |
| Encryption | AES-256-GCM |
| Deployment | Docker + Docker Compose |

---

## Project Structure

```
RiskEngine/
├── RiskEngineSdk/                   # Android SDK
│   ├── riskengine-sdk/              #   SDK Library (AAR)
│   │   └── src/main/
│   │       ├── java/.../riskenginesdk/
│   │       │   ├── RiskEngine.java          # Entry point (Singleton)
│   │       │   ├── RiskEngineConfig.java    # Configuration
│   │       │   ├── RiskEngineCallback.java  # Async callback
│   │       │   ├── model/                   # Data models
│   │       │   ├── core/                    # Scheduling & aggregation
│   │       │   ├── collector/               # Fingerprint collectors
│   │       │   │   ├── java_layer/          #   Java (8)
│   │       │   │   └── native_layer/        #   Native (7, JNI)
│   │       │   ├── detector/                # Risk detectors (10)
│   │       │   ├── transport/               # Network & encryption
│   │       │   └── util/
│   │       └── cpp/                         # C++ Native layer
│   │           ├── collector/
│   │           ├── detector/
│   │           ├── antitamper/
│   │           └── util/                    # syscall wrapper & ELF parser
│   └── demo/                        #   Demo App
│
└── RiskEngineServer/                # Spring Boot Server
    ├── src/main/java/.../riskengineserver/
    │   ├── config/
    │   ├── controller/
    │   │   ├── api/                         # SDK reporting endpoint
    │   │   └── web/                         # Admin pages
    │   ├── dto/
    │   ├── entity/
    │   ├── repository/
    │   ├── service/
    │   └── security/
    ├── src/main/resources/
    │   ├── application.yml                  # MySQL config
    │   ├── application-dev.yml              # H2 config
    │   ├── templates/
    │   └── static/
    ├── sql/init.sql
    ├── Dockerfile
    └── docker-compose.yml
```

---

## Quick Start

A `build.sh` script is provided at the project root (macOS ARM64):

```bash
./build.sh <command>
```

| Command | Description |
|---------|-------------|
| `server` | Build Server JAR |
| `server-run` | Build and run Server in H2 mode (no MySQL required) |
| `sdk` | Build SDK AAR |
| `demo` | 