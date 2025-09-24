# 🚀 Job Recommendation System

An intelligent job recommendation system that provides location-based job search with personalized recommendations, built with Java, MySQL, Redis, and modern web technologies.

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Development](#-development)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### Core Functionality
- **🌍 Location-Based Search**: Find jobs near any geographic location
- **⭐ Smart Favorites**: Save and manage favorite job listings
- **🔍 Keyword Extraction**: Automatic job keyword extraction using AI
- **📊 Personalized Recommendations**: AI-powered job recommendations
- **⚡ Redis Caching**: High-performance caching for improved response times

### Security & Performance
- **🔐 Secure Authentication**: MD5-hashed passwords with session management
- **🛡️ Input Validation**: Comprehensive input sanitization and validation
- **📝 Structured Logging**: Centralized logging with multiple levels
- **⚙️ Environment Configuration**: Flexible configuration management
- **🚦 Error Handling**: Structured exception handling with user-friendly messages

### User Experience
- **💻 Responsive Web Interface**: Modern, mobile-friendly UI
- **🔄 Real-time Updates**: Dynamic content loading with AJAX
- **📱 Cross-platform Compatibility**: Works on desktop, tablet, and mobile
- **🎨 Professional Design**: Clean, intuitive user interface

## 🏗️ Architecture

### System Components

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │   External APIs │
│                 │    │                 │    │                 │
│ • HTML/CSS/JS   │◄──►│ • Java Servlets │◄──►│ • SerpAPI       │
│ • Bootstrap     │    │ • REST APIs     │    │ • EdenAI        │
│ • AJAX          │    │ • Business Logic│    │ • GeoConverter  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │   Data Layer    │    │     Cache       │
                       │                 │    │                 │
                       │ • MySQL DB      │◄──►│ • Redis         │
                       │ • Connection    │    │ • Session Store │
                       │   Pooling       │    │ • Search Cache  │
                       └─────────────────┘    └─────────────────┘
```

### Technology Stack

**Backend:**
- Java 11+ with Servlet API
- Maven for dependency management
- MySQL 8.0+ for data persistence
- Redis for caching and session management

**Frontend:**
- HTML5, CSS3, JavaScript (ES6+)
- Bootstrap for responsive design
- AJAX for asynchronous communication

**External Services:**
- **SerpAPI**: Google Jobs search integration
- **EdenAI**: AI-powered keyword extraction
- **GeoConverter**: Coordinate to location code conversion

**Development & Deployment:**
- JUnit 5 for unit testing
- Apache Tomcat 9+ as servlet container
- Environment-based configuration
- Comprehensive logging system

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Java Development Kit (JDK) 11 or higher**
- **Apache Maven 3.6+**
- **MySQL 8.0+**
- **Redis 6.0+**
- **Apache Tomcat 9.0+**

### Required API Keys
- **SerpAPI Key**: [Get your key here](https://serpapi.com/)
- **EdenAI Key**: [Get your key here](https://www.edenai.co/)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/job-recommendation-system.git
cd job-recommendation-system
```

### 2. Database Setup

```bash
# Start MySQL server
# Create database and user
mysql -u root -p

# Run the initialization script
mysql -u root -p < scripts/init-database.sql
```

### 3. Redis Setup

```bash
# Start Redis server
redis-server

# Test Redis connection
redis-cli ping
```

### 4. Environment Configuration

Run the setup script to configure environment variables:

```bash
# Windows
scripts\setup-env.bat

# Or manually set environment variables:
set DB_HOST=localhost
set DB_PORT=3306
set DB_NAME=jobrec
set DB_USERNAME=admin
set DB_PASSWORD=your_password
set REDIS_HOST=localhost
set REDIS_PORT=6379
set REDIS_PASSWORD=your_redis_password
set SERPAPI_KEY=your_serpapi_key
set EDENAI_KEY=your_edenai_key
set APP_ENVIRONMENT=dev
```

### 5. Build the Application

```bash
mvn clean compile package
```

### 6. Deploy to Tomcat

```bash
# Copy WAR file to Tomcat webapps directory
cp target/JobSearch-1.0-SNAPSHOT.war $TOMCAT_HOME/webapps/jobrec.war

# Start Tomcat
$TOMCAT_HOME/bin/startup.sh  # Linux/Mac
# or
%TOMCAT_HOME%\bin\startup.bat  # Windows
```

## ⚙️ Configuration

### Application Properties

The application supports e