> 老仓库 / Legacy repository：<https://github.com/feigeCode/onetcli> · [![OnetCli Stars](https://img.shields.io/github/stars/feigeCode/onetcli?style=flat-square&logo=github&label=OnetCli%20Stars)](https://github.com/feigeCode/onetcli)

<div align="center">
  <p><img src="resources/navop-icon.png" alt="Navop" width="120" /></p>
  <h1>Navop</h1>
  <p><strong>A native, all-in-one workspace for databases, SSH, SFTP, terminals, remote desktop, monitoring, and AI.</strong></p>
  <p>Built with <a href="https://gpui.rs">GPUI</a> and Rust · GPU-accelerated rendering</p>

  <p>
    <a href="https://github.com/feigeCode/navop/releases"><img src="https://img.shields.io/github/downloads/feigeCode/navop/total?style=for-the-badge&color=blue" alt="Downloads" /></a>
    <a href="https://github.com/feigeCode/navop/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/feigeCode/navop/ci.yml?branch=main&style=for-the-badge" alt="CI" /></a>
    <a href="#license"><img src="https://img.shields.io/badge/license-Apache--2.0%20%2B%20supplementary%20terms-blue?style=for-the-badge" alt="License: Apache-2.0 plus supplementary terms" /></a>
    <a href="https://qm.qq.com/cgi-bin/qm/qr?k=&group_code=860670605"><img src="https://img.shields.io/badge/QQ%20Group-860670605-EB1923?style=for-the-badge&logo=tencentqq&logoColor=white" alt="QQ Group 860670605" /></a>
    <a href="https://docs.qq.com/doc/DVEFFd2RnSnJLcFBD"><img src="https://img.shields.io/badge/WeChat%20Group-Join-07C160?style=for-the-badge&logo=wechat&logoColor=white" alt="Join WeChat Group" /></a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white" alt="MySQL" />
    <img src="https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white" alt="PostgreSQL" />
    <img src="https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white" alt="SQLite" />
    <img src="https://img.shields.io/badge/DuckDB-FFF000?logo=duckdb&logoColor=black" alt="DuckDB" />
    <img src="https://img.shields.io/badge/ClickHouse-FFCC01?logo=clickhouse&logoColor=black" alt="ClickHouse" />
    <img src="https://img.shields.io/badge/SQL%20Server-CC2927?logo=microsoftsqlserver&logoColor=white" alt="SQL Server" />
    <img src="https://img.shields.io/badge/Oracle-F80000?logo=oracle&logoColor=white" alt="Oracle" />
    <img src="https://img.shields.io/badge/Dameng%20DM-C71D23" alt="Dameng DM" />
    <img src="https://img.shields.io/badge/KingbaseES-005BAC" alt="KingbaseES" />
    <img src="https://img.shields.io/badge/GBase%208s-1E73BE" alt="GBase 8s" />
    <img src="https://img.shields.io/badge/OceanBase-1B9A8C" alt="OceanBase" />
    <img src="https://img.shields.io/badge/openGauss-005EB8" alt="openGauss" />
    <img src="https://img.shields.io/badge/Apache%20IoTDB-1B3A6B?logo=apache&logoColor=white" alt="Apache IoTDB" />
    <img src="https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white" alt="Redis" />
    <img src="https://img.shields.io/badge/MongoDB-47A248?logo=mongodb&logoColor=white" alt="MongoDB" />
    <img src="https://img.shields.io/badge/SSH-111827?logo=gnubash&logoColor=white" alt="SSH" />
    <img src="https://img.shields.io/badge/SFTP-2563EB?logo=filezilla&logoColor=white" alt="SFTP" />
    <img src="https://img.shields.io/badge/Port%20Forwarding-0F766E" alt="Port Forwarding" />
    <img src="https://img.shields.io/badge/RDP-0078D4" alt="RDP" />
    <img src="https://img.shields.io/badge/VNC-5C2D91" alt="VNC" />
  </p>

  <p>
    <a href="README_CN.md">中文</a> ·
    <a href="#features">Features</a> ·
    <a href="#screenshots">Screenshots</a> ·
    <a href="#install">Install</a> ·
    <a href="https://github.com/feigeCode/navop/releases/latest">Latest Release</a> ·
    <a href="CONTRIBUTING.md">Contributing</a>
  </p>

  <p><img src="app1.png" alt="Navop overview" width="820" /></p>
</div>

## Features

### Databases and data tools

- Connect to MySQL, PostgreSQL, SQLite, DuckDB, SQL Server, Oracle, and ClickHouse.
- Install extension drivers for Dameng DM, KingbaseES, GBase 8s, OceanBase, openGauss, Apache IoTDB, and Oracle without Instant Client.
- Browse database objects, edit and run SQL, inspect execution plans, import or export data, compare schemas and data, and visualize relationships with ER diagrams.
- Work with Redis and MongoDB through dedicated interfaces.
- Route supported network connections through SOCKS5 or HTTP CONNECT proxies and SSH tunnels.

### Remote access and operations

- Use SSH and local terminals with draggable splits, quick commands, history, broadcast input, shell integration, and terminal AI.
- Manage remote files with SFTP uploads, downloads, search, favorites, remote editing, drag-and-drop, and server-to-server copy.
- Create reusable local, remote (`ssh -R`), and dynamic SOCKS port-forwarding connections.
- Open serial connections, monitor servers, and connect to remote desktops through installable RDP and VNC providers.

### Editing, AI, and