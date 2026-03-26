# INAV Configurator

INAV Configurator is a cross-platform configuration tool for the [INAV](https://github.com/iNavFlights/inav) flight control system.

Various types of aircraft are supported by the tool and by INAV, e.g. quadcopters, hexacopters, octocopters, and fixed-wing aircraft.

# Support

INAV Configurator comes `as is`, without any warranty and support from the authors. If you find a bug, please create an issue on [GitHub](https://github.com/iNavFlights/inav-configurator/issues).

The GitHub issue tracker is reserved for bugs and other technical problems. If you do not know how to set up
everything, the hardware is not working, or you have any other _support_ problem, please consult:

* [INAV Discord Server](https://discord.gg/peg2hhbYwN)
* [INAV Official on Facebook](https://www.facebook.com/groups/INAVOfficial)
* [RC Groups Support](https://www.rcgroups.com/forums/showthread.php?2495732-Cleanflight-iNav-(navigation-rewrite)-project)
* [INAV Official on Telegram](https://t.me/iNavFlights)
* [GitHub Discussions](https://github.com/iNavFlights/inav-configurator/discussions)

## Installation

 _INAV Configurator_ is distributed as a  _standalone_ application.

### Windows

1. Visit [release page](https://github.com/iNavFlights/inav-configurator/releases)
2. Download Configurator for Windows platform (ia32 or win64 is present)
3. Install
    * Extract ZIP archive and run the INAV Configurator app from the unpacked folder
    * OR just use the setup program `INAV-Configurator_win32_arch_x.y.z.exe`, **arch** is your computer architecture (ia32 (32bit) or x64 (64bit)), **x.y.z** is the INAV Configurator version number.

4.  Configurator is not signed, so you have to allow Windows to run untrusted applications. There might be a monit for it during the first run

### Linux

1. Visit [release page](https://github.com/iNavFlights/inav-configurator/releases)
2. Download Configurator for Linux platform (only linux64 is present)
   *  **.rpm** is the Fedora installation file. Just download and install using `sudo dnf localinstall /path/to/INAV-Configurator_linux_x64-x.y.z.rpm` or open it with a package manager (e.g. via Files)
   *  **.deb** is the Debian/Ubuntu installation file. Just download and install using `sudo apt install /path/to/INAV-Configurator_linux_x64_x.y.z.deb` or open it with a package manager (e.g. via the File Manager)
   *  **.zip** is a universal archive. Download and continue with these instructions to install
3. Change to the directory containing the downloaded **zip** file
4. download [this](https://raw.githubusercontent.com/iNavFlights/inav-configurator/master/assets/linux/inav-configurator.desktop) file to the same directory. Its filename should be `inav-configurator.desktop`.
5. Extract **zip** archive
```
unzip INAV-Configurator_linux_arch_x.y.z.zip -d /tmp/
```
  **arch** is your computer architecture (x64, armv7l, ...), **x.y.z** is the INAV Configurator version number.

6. If this is the first time installing INAV Configurator, create a home for its files
```
sudo mkdir /opt/inav
sudo chown $USER /opt/inav
```
7. Move the temporary files into their home 
```
mv /tmp/INAV\ Configurator /opt/inav/inav-configurator
```
8. Update the application icon.
```
sudo mkdir /opt/inav/inav-configurator/icon
sudo cp /opt/inav/inav-configurator/resources/app/images/inav_icon_128.png /opt/inav/inav-configurator/icon
```
9. As a one-off, move the desktop file into the applications directory 
```
sudo mv inav-configurator.desktop /usr/share/applications/
```
10. Make the following files executable:
   * inav-configurator `chmod +x /opt/inav/inav-configurator/inav-configurator`
11. Run the INAV Configurator app from the unpacked folder `/opt/inav/inav-configurator/inav-configurator`

### Mac

1. Visit [release page](https://github.com/iNavFlights/inav-configurator/releases)
2. Download Configurator for the Mac platform
3. Install
    * Extract ZIP archive and run INAV Configurator
    * OR use the DMG package for installation

## Building and running INAV Configurator locally (for development)

For local development, the **node.js** build system is used.

1. Install node.js
1. From the project folder run `yarn install`
1. To build the and start the configurator:
    - Run `yarn start`.

To build the App run `yarn run make` to build for your platform.

Options:
* Architecture: --arch  - Allowed values are: "ia32", "x64", "armv7l", "arm64", "universal", or "mips64el". 

See [Electron Forge CLI Documentation](https://www.electronforge.io/cli#options-2) for details

Note: Not all architectures are available for all platforms. For example, ia32 (32bit) support is not available for Linux. 
Tested architectures:
- Windows: x64 and ia32
- Linux: x64 and armv7l
- MacOS: x64 and arm64

To build the setup program for windows, you have to install [WiX Toolset V3](https://github.com/wixtoolset/wix3/releases) and add the `bin` folder to you `PATH`, e.g.
```C:\Program Files (x86)\WiX Toolset v3.14\bin```

To bui