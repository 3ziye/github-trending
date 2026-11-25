<img src="docs/img/hmg-api.png" width="120" align="right" alt="HMG-API logo">

# HMG-API

[![Support HMG-API](https://img.shields.io/badge/Support_HMG--API-%E2%9D%A4-bf3989?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/Open-HMG/HMG-API/wiki/Support)

> **HMG-API is free**, made by volunteers. If it saved you a dealer visit or made your drives nicer, please consider [supporting the people who build it](https://github.com/Open-HMG/HMG-API/wiki/Support): each maintainer has their own links there. It keeps the testing and new-car ports going.

A mod manager for Hyundai, Kia and Genesis **Gen5W** navigation head units.

Mods add features to the head unit (wireless CarPlay and Android Auto with
turn-by-turn on the cluster and HUD, buttons that do more, side panel pages, and
more) without patching its apps. HMG-API hooks the car's own software while it runs,
gives every mod a switch, settings and a log, and puts back exactly what a mod
changed when it's removed.

![The HMG-API app on a Kia EV6](docs/img/screenshots/mods.png)

| Settings | Car Report |
|---|---|
| ![Settings](docs/img/screenshots/settings.png) | ![Car Report](docs/img/screenshots/report.png) |

## Install

Download the zip for your route from [Releases](https://github.com/Open-HMG/HMG-API/releases):
a **USB stick** (no computer), **NEMESIS**, or **adb**. Step by step:
[Installing HMG-API](https://github.com/Open-HMG/HMG-API/wiki/Installing-HMG-API).

HMG-API runs on any Gen5W navigation head unit. Cars with a hook map get everything;
on others, mods still install and run, and the app's **Car Report** sends what's
needed to add your car ([Supported cars](https://github.com/Open-HMG/HMG-API/wiki/Supported-cars)).

After a firmware update, install HMG-API again: the update removes its system files,
and the install starts again from the new firmware's
([Troubleshooting](https://github.com/Open-HMG/HMG-API/wiki/Troubleshooting#after-a-firmware-update-hmg-apis-system-files-are-gone-or-uninstall-fails)).

| Car | Region | Software | Hook map |
|---|---|---|---|
| Kia EV6 | USA | 260507 | checked on a car |
| Kia EV6, Hyundai Ioniq 5 | Canada | 260206 | waiting for a Car Report |
| Hyundai Ioniq 6 | Canada | 260206 | checked on a car |
| Hyundai Ioniq 6 | USA | 260507 | from stock files, waiting for a check on a car |
| Hyundai Ioniq 5 | USA | 260507 | waiting for a Car Report |
| Hyundai Ioniq 5 | USA, Canada | 260903 | waiting for a check on a car |
| Kia Sportage, Telluride, Niro, Carnival, Forte, Soul, Seltos 2024 | USA | 260507 | from Car Reports, waiting for a check on a car |
| Hyundai Palisade | USA | 260903 | from a Car Report, waiting for a check on a car |
| Hyundai Elantra, Sonata, Santa Fe, Kona, Ioniq, Venue, Veloster N, Palisade 2020-22 | USA | 260507 | from stock files, waiting for a check on a car |
| Kia K5, Sorento, Stinger, Soul, Seltos 2021, Niro 2020-22, Cadenza, Telluride 2020-21 | USA | 260507 | from stock files, waiting for a check on a car |
| Hyundai Elantra, Sonata, Santa Fe, Kona, Ioniq, Venue, Veloster N, Palisade 2020-22 | Canada | 260206 | from stock files, waiting for a check on a car |
| Kia K5, Sorento, Stinger, Soul, Seltos 2021, Niro 2020-21, Telluride 2020-21 | Canada | 260206 | from stock files, waiting for a check on a car |
| Kia K5, Sorento, Stinger, Seltos, Soul, Niro, Mohave, K7, Morning, Ray | Korea | 260902 | from stock files, waiting for a check on a car |
| Hyundai Ioniq 5 | Korea | 260902 | from stock files, waiting for a check on a car |
| Hyundai Sonata, Sonata Hybrid, Santa Fe, Palisade | Korea | 260902 | from Car Reports, waiting for a check on a car |
| Kia Niro, Sportage, Carnival, Telluride, Forte, Soul, Seltos 2024 | Canada | 260206 | from a Car Report, waiting for a check on a car |
| Genesis G70 | USA | 260507 | from a Car Report, waiting for a check on a car |
| Genesis G70 | Korea | 260902 | from a Car Report, waiting for a check on a car |
| Hyundai Ioniq 6 | USA, Canada | 260903 | checked on a car |
| Kia EV6 | Korea | 260902 | from a Car Report, waiting for a check on a car |
| Hyundai Elantra (`CN7PE`) | USA | 260507 | from a Car Report, waiting for a check on a car |
| Hyundai Elantra N 2024 (`CN7NPE`) | USA | 260903 | from a Car Report, waiting for a check on a car |
| Hyundai Kona (`OSPE`) | USA | 260903 | from a Car Report, waiting for a check on a car |
| Kia Niro EV (`SG225EV`) | Canada | 260206 | from a Car Report, waiting for a check on a car |
| Kia K3 | Korea | 260902 | from a Car Report, waiting for a check on a car |
| Genesis G70 | Canada | 260903 | from a Car Report (3 apps not in it), waiting for a check on a car |
| Hyundai Ioniq 6 | Singapore | 260907 | from a Car Report, waiting for a check on a car |
| Hyundai Creta | India | 260430 | from a Car Report, waiting for a check on a car |

## Help and requests

[Open an issue](https://github.com/Open-HMG/HMG-API/issues/new/choose): something
doesn't work, car or firmware support (the Car Report's Q