# BootUI

[![Build](https://github.com/jdubois/boot-ui/actions/workflows/build.yml/badge.svg)](https://github.com/jdubois/boot-ui/actions/workflows/build.yml)
[![CodeQL](https://github.com/jdubois/boot-ui/actions/workflows/codeql.yml/badge.svg)](https://github.com/jdubois/boot-ui/actions/workflows/codeql.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-4.0.x-6db33f?logo=springboot&logoColor=white)](https://spring.io/projects/spring-boot)
[![Java](https://img.shields.io/badge/Java-17-orange?logo=openjdk&logoColor=white)](https://openjdk.org/projects/jdk/17/)

BootUI is a **Spring Boot 4 starter** that adds an embedded, local-only developer console to your application.

It is served by the host application at `/bootui/`, uses internal `/bootui/api/**` endpoints, and packages the browser
UI into the starter so consuming applications do not need Node.js or npm.

![BootUI overview](docs/images/bootui-overview.png)

## Features

BootUI exposes these panels in the same grouped order as the application menu. See the
[feature details guide](docs/FEATURES.md) for explanations and screenshots for every panel.

| Group           | Feature                                                                 | What it helps with                                                                                                                      |
| --------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Overview        | [Overview](docs/FEATURES.md#overview)                                   | See runtime identity, versions, ports, active profiles, activation reason, and safety state.                                            |
| Runtime         | [Health](docs/FEATURES.md#health)                                       | Explore the Actuator health tree and contributor details, with setup guidance when health is unavailable or only defaults are reported. |
| Runtime         | [Metrics](docs/FEATURES.md#metrics)                                     | Browse Micrometer meters, tags, measurements, and a local live chart for selected metrics.                                              |
| Runtime         | [Memory](docs/FEATURES.md#memory)                                       | Review live JVM heap, non-heap, and memory pool usage.                                                                                  |
| Runtime         | [Tuning Advisor](docs/FEATURES.md#tuning-advisor)                       | Calculate fixed bare-metal JVM options, percentage-based Kubernetes JVM settings, probes, and detected virtual-thread sizing from live JVM context. |
| Runtime         | [Heap Dump](docs/FEATURES.md#heap-dump)                                 | Capture local JVM heap dumps on demand and analyze a value-free class histogram of memory usage.                                        |
| Runtime         | [Startup Timeline](docs/FEATURES.md#startup-timeline)                   | Inspect Spring Boot startup steps and durations when startup data is available.                                                         |
| Configuration   | [Configuration](docs/FEATURES.md#configuration)                         | Inspect effective configuration values, metadata, masking, and local runtime overrides.                                                 |
| Configuration   | [Profile Diff](docs/FEATURES.md#profile-diff)                           | Compare profile-specific property sources and values while preserving secret masking.                                                   |
| Configuration   | [Loggers](docs/FEATURES.md#loggers)                                     | Inspect and change logger levels at runtime through the Actuator loggers endpoint.                                                      |
| Configuration   | [Beans](docs/FEATURES.md#beans)                                         | Search Spring beans by name, type, and BootUI classification with server-side paging.                                                   |
| Configuration   | [Conditions](docs/FEATURES.md#conditions)                               | Understand why auto-configuration classes matched, did not match, or were unconditional.                                                |
| Configuration   | [Mappings](docs/FEATURES.md#mappings)                                   | Review HTTP routes, handlers, methods, patterns, and produces/consumes metadata.                                                        |
| Services        | [Scheduled Tasks](docs/FEATURES.md#scheduled-tasks)                     | View registered scheduled tasks and their trigger metadata.                                                                             |
| Services        | [Database Connection Pools](docs/FEATURES.md