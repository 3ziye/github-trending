# Spring Microservices Blueprint

🚀 Java Spring Boot microservices with complete ecosystem: PostgreSQL, Kafka+Zookeeper, Elasticsearch+Kibana+Fluentd, JWT auth, Swagger. Two simple commands launch 10+ pre-configured services!

This project demonstrates event-driven microservices with request tracing: each request carries a correlation_id across REST calls and Kafka messages, making logging and observability easy.

## 🏗️ Multi-Module Maven Architecture

This project demonstrates **Maven Multi-Module** best practices:

```
spring-microservices-blueprint/
├── pom.xml                    # Parent POM with dependency management
├── commons/                   # Shared utilities and DTOs
│   ├── pom.xml
│   └── src/main/java/
├── account-service/           # User management microservice
│   ├── pom.xml
│   └── src/main/java/
└── product-service/           # Product management microservice
    ├── pom.xml
    └── src/main/java/
```

**Benefits:**
- **Shared Dependencies**: Common libraries managed in parent POM
- **Code Reusability**: Shared DTOs and utilities in commons module
- **Consistent Versioning**: All modules use same version from parent
- **Easy Setup & Launch**: Only two commands needed to build and start all services
- **Simplified Development**: Debugging, logging, and monitoring pre-configured for convenience

## 🔧 Prerequisites

**Required:**
- **Java 17+**
- **Maven 3.9+**
- **Docker Desktop**

**Verify installation:**
```bash
java -version    # Should show Java 17+
mvn -version     # Should show Maven 3.9+
docker --version # Should show Docker 20.10+
```

## 🚀 Quick Start (5 Minutes)

**Build and start everything:**
```bash
# Build Maven artifacts first
mvn clean install -DskipTests

# Build Docker images and start all services
docker compose up -d --build
```

**Wait for services to be ready (30-60 seconds):**
```bash
docker compose ps
```

**Test the system:**
```bash
# Test Account Service
curl http://localhost:8088/api/test/all

# Test Product Service  
curl http://localhost:8089/api/product/search
```

If both return data, you're ready! 🎉

## 📚 Complete Documentation

### 🏁 Getting Started
- **[01-Quick-Setup.md](docs/01-Quick-Setup.md)** - Get running in 5 minutes
- **[02-System-Architecture.md](docs/02-System-Architecture.md)** - Understand the design
- **[03-API-Reference.md](docs/03-API-Reference.md)** - Complete API documentation

### 🛠️ Development & Testing  
- **[04-Development-Guide.md](docs/04-Development-Guide.md)** - Local development workflow
- **[05-Testing-Guide.md](docs/05-Testing-Guide.md)** - Testing strategies and scripts
- **[06-Debugging-Guide.md](docs/06-Debugging-Guide.md)** - Debug in containers

### 🐳 Operations & Deployment
- **[07-Docker-Operations.md](docs/07-Docker-Operations.md)** - Container management
- **[08-Monitoring-Logging.md](docs/08-Monitoring-Logging.md)** - Observability setup
- **[09-Troubleshooting.md](docs/09-Troubleshooting.md)** - Common issues & solutions

### 📋 Reference Materials
- **[10-Postman-Collection.md](docs/10-Postman-Collection.md)** - API testing with Postman
- **[11-Configuration-Reference.md](docs/11-Configuration-Reference.md)** - All configuration options

## 🎯 What You'll Learn

### Core Microservices Patterns
- **Service Decomposition** - Separate services for different business domains
- **Database Per Service** - Independent data storage for each service
- **API Gateway Pattern** - Centralized entry point (future enhancement)
- **Service Discovery** - Dynamic service location (future enhancement)

### Communication Patterns
- **Synchronous Communication** - REST APIs with Feign clients
- **Asynchronous Messaging** - Event-driven architecture with Kafka
- **Request/Response** - Direct service-to-service calls
- **Publish/Subscribe** - Event broadcasting for loose coupling

### Cross-Cutting Concerns
- **Authentication & Authorization** - JWT tokens with role-based access
- **Centralized Logging** - ELK Stack for log aggregation
- **Distributed Tracing** - Correlation IDs across service calls
- **Health Monitoring** - Service health checks and metrics
- **Distributed Tracing & Logging** - request body, response body, and Kafka messages carry correlation_id, making it easy to trace interactions across services.


### Infrastructure & DevOps
- **Multi-Module Architecture** - Maven parent-child module structure
- **Containerization** - Docker for consistent environments
- **Container Orchestration** - Docker Compose for multi-service deployment
- **Configuration Management** - Environment-based configuration
- **Database Management** - PostgreSQL with proper schema design

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Client Layer                            │
│  Web Browser, Mobile App, Postman, curl, etc.             │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/REST
┌─────────────────────▼─────────────────────────