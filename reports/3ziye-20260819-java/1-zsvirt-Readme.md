<div align="center">
  <a href="https://zsvirt.io">
    <img
      src="https://raw.githubusercontent.com/zsvirt/.github/main/assets/zsvirt-logo.jpg"
      alt="ZSvirt Logo"
      width="180"
    >
  </a>

  <h1 align="center">
    Open Source Virtualization
    <br>
    Enterprise Ready, Community Driven
  </h1>

  <p align="center">
    <a href="https://zsvirt.io/en">
      <img
        src="https://img.shields.io/badge/Website-0F62FE?style=flat-square&logo=googlechrome&logoColor=white"
        alt="ZSvirt Website"
      >
    </a>
    <a href="https://zsvirt.io/en/docs">
      <img
        src="https://img.shields.io/badge/Docs-7C3AED?style=flat-square&logo=readthedocs&logoColor=white"
        alt="Documentation"
      >
    </a>
    <a href="https://demo.zsvirt.io/">
      <img
        src="https://img.shields.io/badge/Live%20Demo-16A34A?style=flat-square&logo=internetcomputer&logoColor=white"
        alt="Live Demo"
      >
    </a>
    <a href="https://zsvirt.io/en/download">
      <img
        src="https://img.shields.io/badge/Download-F97316?style=flat-square&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTUgMjBoMTR2LTJINXYyem0xNC05aC00VjNIOXY4SDVsNyA3IDctN3oiLz48L3N2Zz4%3D"
        alt="Download"
      >
    </a>
  </p>

  <p>
    <strong>English</strong>
    &nbsp;&middot;&nbsp;
    <a href="./README_zh.md">简体中文</a>
  </p>
</div>

## What is ZSvirt
ZSvirt brings [ZStack](https://www.zstack-cloud.com/)'s enterprise-proven ZSphere virtualization engine into the open-source world. Backed by [ZStack](https://www.zstack-cloud.com/), a mature infrastructure leader, ZSvirt delivers a lightweight, scalable platform designed for absolute freedom—from high-performance homelabs to hyperscale infrastructure without vendor lock-in.

## Product Tour

<details open>
  <summary>
    <strong>📊 DASHBOARD — Unified Operations Overview</strong>
  </summary>

  <br>

  <p align="center">
    <a href="https://raw.githubusercontent.com/ZSvirt/.github/main/assets/zsvirt-dashboard.png">
      <img
        src="https://raw.githubusercontent.com/ZSvirt/.github/main/assets/zsvirt-dashboard.png"
        alt="ZSvirt Unified Operations Dashboard"
        width="100%"
      >
    </a>
  </p>
</details>

<br>

<details>
  <summary>
    <strong>🗂️ INVENTORY — Centralized Infrastructure Management</strong>
  </summary>

  <br>

  <p align="center">
    <a href="https://raw.githubusercontent.com/ZSvirt/.github/main/assets/zsvirt-inventory.png">
      <img
        src="https://raw.githubusercontent.com/ZSvirt/.github/main/assets/zsvirt-inventory.png"
        alt="ZSvirt Centralized Infrastructure Inventory"
        width="100%"
      >
    </a>
  </p>
</details>

<br>

<details>
  <summary>
    <strong>🔄 MIGRATION MANAGEMENT — Workload Migration</strong>
  </summary>

  <br>

  <p align="center">
    <a href="https://raw.githubusercontent.com/ZSvirt/.github/main/assets/zsvirt-migration-management.png">
      <img
        src="https://raw.githubusercontent.com/ZSvirt/.github/main/assets/zsvirt-migration-management.png"
        alt="ZSvirt Migration Management"
        width="100%"
      >
    </a>
  </p>
</details>

## Live Demo

[ZSvirt Live Demo](https://demo.zsvirt.io/) is a free hosted environment for trying ZSvirt online. No local installation is required—after registration and login, you can start exploring the platform right away.

## Architecture

ZSvirt uses a modular architecture built around virtualization resource
management, the management plane, extension services, and operational tooling.

Core capabilities include:

- **Compute virtualization**: host, cluster, virtual machine, image, and
  lifecycle management.
- **Network virtualization**: virtual networks, network services, security
  groups, and related capabilities.
- **Storage virtualization**: primary storage, backup storage, volumes,
  snapshots, and storage resource management.
- **Management plane**: API framework, permission model, events, alarms,
  auditing, and system operations.
- **Extension services**: capabilities for migration, disaster recovery,
  monitoring, quota management, access control, and enterprise operations.
- **Tools and integrations**: installation tools, diagnostics tools, migration
  tools, automation scripts, agents, CLI, and external system integrations.

At the software architecture level, ZSvirt emphasizes asynchrony, statelessness,
extensibility, and automation:

- **Asynchronous architecture**: supports asynchronous messages, asynchronous
  methods, and asynchronous HTTP calls to reduce blocking and improve system
  throughput.
- **Stateless services**: individual requests do not depend on state from other
  requests, making services easier to scale, recover, and operate.
- **Plugin-based extensibility**: supports horizontal extension of resource
  types, business capabilities, and integration capabilities through plugins.
- **Workflow