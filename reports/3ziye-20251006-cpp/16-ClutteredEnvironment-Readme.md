<div align="center">
  <h1> A novel MPC framework for efficient navigation of mobile robots in cluttered environments </h1>


  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>

</div>

---
This is the accompaning code of the paper titled "A novel MPC framework for efficient navigation of mobile robots in cluttered environments". 
[Read preprint on arXiv](https://arxiv.org/abs/2509.15917)


## Demo

![](./media/cluttered_mpc_sim.gif)

## Experiments

🎥 [Click to watch the experiment video](https://youtu.be/Hn_hpAmGgq0)

[![](./media/arc_screenshot_anoted.png)](https://youtu.be/Hn_hpAmGgq0)


## Prerequisites

This software is based on the Control and Robotics Software ([CRS](https://gitlab.ethz.ch/ics/crs)), an advanced control software framework to support simulations and experiments in the fields of control and robotics. CRS is built on top of the Robot Operating System (ROS) and primarily written in C++ and Python.
The CRS environment uses [Docker](https://www.docker.com) to allow cross-platform compatibility. The only requirement you have is to run an up-to-date operating system and up to 16 GB of free storage (some of it is only required during the setup). Below you find the install instructions for Ubuntu, macOS and Windows.

## Setting up the Docker Image

### Toolkit Installation
First, install the `crs-docker` tool based on your operating system:
<details>
<summary>Ubuntu (recommended)</summary>

 These instructions were tested on the following Ubuntu versions:

- 20.04 LTS
- 22.04 LTS
- 24.04 LTS

However, the instructions should apply to all recent Ubuntu versions.

#### Steps

1. Install Docker using the [offical install instructions](https://docs.docker.com/install/)   _Note: The install instructions list Ubuntu in the server section!_
2. Allow Docker execution as a non-root user; follow [these instructions](https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user)   _Note: Only do the first section "Manage Docker as a non-root user"_
3. Test your Docker installation with the following command   _Note: You might want to restart your computer at this point._

   ```sh
   docker run hello-world
   ```
4. Clone the git repository

   ```sh
   git clone https://github.com/IntelligentControlSystems/ClutteredEnvironment.git
   ```
5. Navigate to the Ubuntu setup folder

   ```sh
   cd ClutteredEnvironment/.setup/ubuntu
   ```
6. Execute the setup script

   ```sh
   ./setup.sh
   ```

</details>

<details>
<summary>Arch Linux </summary>

The Installation does not differ too much from the Ubuntu installation. There is however one caveat on Arch Linux: Running Docker containers might fill up your memory and crash your system. To prevent this, add following lines to the file `/etc/docker/daemon.json` :

```sh
{
  "default-ulimits": {
    "nofile": {
      "Name": "nofile",
      "Soft": 1024,
      "Hard": 524288
    }
  }
}
```

Do not forget to restart the docker service with `sudo systemctl restart docker`.

Alternatively, one can specify these limits in the `docker-compose.yaml` file:

```sh
version: '3'
name: "crs"
services:
  crs:

    ...

    # ADD THESE 4 LINES
    ulimits:
      nofile:
        soft: 1024
        hard: 524288

    ...
```

</details>

<details>
<summary>MacOS</summary>

These instructions were tested on **macOS Sonoma (14.4)**. However, the instructions should apply to all recent macOS versions.

#### Steps

1. Install Docker using the [offical install instructions](https://docs.docker.com/install/)
2. Test your Docker installation with the following command

   ```sh
   docker run hello-world
   ```
3. Clone the git repository   _Note: Make sure you have a SSH key set up, otherwise this doesn't work._

   ```sh
   git clone https://github.com/IntelligentControlSystems/ClutteredEnvironment.git
   ```
4. Navigate to the MacOS setup folder

   ```sh
   cd ClutteredEnvironment/.setup/macos
   ```
5. Execute the setup script

   ```sh
   ./setup.sh
   ```

</details>

<details>
<summary>Windows</summary>

 These instructions were tested on the following Windows versions:

- Windows 11

Windows 10 should work as well, but might need some slight modifications.

#### Steps

1. Install Docker using the [official install instructions](https://docs.docker.com/desktop/install/windows-install/)
2. Make sure to run Docker on WSL 2 (see [Docker Desktop WSL 2 backend on Windows](https://docs.docker.com/desktop/wsl/))
   1. Make sure you have WSL 2 installed and set Ubuntu as the default distro.
   2. Make sure to tick the boxes in the Docker Desktop as in the screenshots below.

      ![image.png](uploads/e1e86bcc006aff072295e4f96584b879/image.png){width="840" height="440"}

      ![Screenshot 2024-08-30 103945.png](uploads/94fe1a22e216189487109c874848ff56/Screenshot_2024-08-30_103945.png){width="1440" height="759"}
3. Open a PowerShell Terminal and get into your defau