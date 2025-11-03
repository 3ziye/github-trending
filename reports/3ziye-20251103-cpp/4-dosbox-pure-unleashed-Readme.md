# DOSBox Pure Unleashed
DOSBox Pure is a fork of [DOSBox](https://www.dosbox.com/),
an emulator for DOS games, aiming for simplicity and ease of use.
This project is a standalone version for desktop platforms of the [libretro core](../dosbox-pure).

![Logo](images/logo.png)

## Download
You can download the latest version of DOSBox Pure on [itch.io](https://schelling.itch.io/dosbox-pure) or from the [Releases page here](https://github.com/schellingb/dosbox-pure-unleashed/releases/latest).

Just extract the ZIP file and then run DOSBoxPure.exe.

### Donations
Tips and donations are welcome, either through the [itch.io page](https://schelling.itch.io/dosbox-pure)
or the Sponsor button at the top of the [GitHub repository](https://github.com/schellingb/dosbox-pure-unleashed).

Thank you for your consideration!

## Loading Content
DOSBox Pure can load ZIP files, CD images (ISO or CUE), floppy/hard disk images (IMG/IMA/VHD/JRC), DOS executable files (EXE/BAT/COM),
legacy DOSBox .conf files or folders directly. It also loads .DOSZ files which are just .ZIP files with a different extension.

There are 3 ways to load content. After startup, you can use the "Load Content" menu option to navigate to the file you want to load.
Alternatively you can drag & drop a supported file onto the program window (after starting) or onto the program's icon (before starting).

## Hotkeys
A few system functions are bound to various F-keys, accessible while holding the hotkey modifier which by default is the Control key.
The hotkey modifier can be changed in the [System Settings](#system-settings). These are the hotkeys:

| Key | Description                                     |
|-----|-------------------------------------------------|
| F1  | Pause/Resume (F12 to step a frame while paused) |
| F2  | Slow Motion                                     |
| F3  | Fast Forward                                    |
| F5  | Save State Quick Save                           |
| F7  | Switch Full Screen and Windowed Mode            |
| F9  | Save State Quick Load                           |
| F11 | Lock Mouse to Window                            |
| F12 | Toggle On-Screen Menu                           |

Use the `General > Fast Forward/Slow Motion Mode` setting to swap between holding or toggling mode.

In addition, you can set the `General > Middle Mouse Button Open Menu` setting for easier access to the menu.

## Features

### Load Games from ZIP
DOSBox Pure can load games directly from ZIP files without the need to extract them.

### Store Modifications in Separate Save File
Changes made to a loaded ZIP file will be stored as a separate ZIP file into the saves directory.  
If a game is loaded directly without using a container like ZIP or ISO the saves directory is not used.

### Mount Disk Images from Inside ZIP Files
CD images (ISO or CUE) and floppy disk images (IMG/IMA/VHD/JRC) can be mounted directly from inside ZIP files.  
The system will automatically mount the first found disk image as the A: or D: drive.  
Additional disks can be loaded or swapped by using the [start menu](#start-menu).

### Start Menu
![Start Menu](images/startmenu.png)

This is the first screen that appears after loading a game. It offers a gamepad controllable list
with all executable files of the loaded game. In addition it can load new content and swap which floppy disk or CD is inserted.

By using the tabs at the bottom, you can view the [Gamepad Mapper](#gamepad-mapper), the [System Settings](#system-settings)
and while a game is running access the [On-Screen Keyboard](#on-screen-keyboard).

While a game is running, you can open the menu again by pressing CTRL+F12 or L3 on the gamepad (usually by pushing in the left analog stick).
The keyboard hotkey can be modified in the [System Settings](#system-settings) and the gamepad button can be changed in the [Gamepad Mapper](#gamepad-mapper).

### System Settings
By switching to the SYSTEM tab in the [start menu](#start-menu) you will find all program and emulation settings divided into various categories.
Each setting has a list of options and a detailed description next to it.

### Auto Start
While in the [start menu](#start-menu), you can press right to set an item as the default which will skip the menu the next time the same content is loaded.
By pressing right multiple times, a number of frames can be specified that will automatically be skipped on start.
This can be used to skip over loading screens or start-up sequences.  
If there is only a single choice, the menu will not show and directly run the only executable file.

### On-Screen Keyboard
![On-Screen Keyboard](images/onscreenkeyboard.png)

By pressing L3 on the gamepad (usually by pushing in the left analog stick) the menu will open.
Then you can use the L and R buttons to switch to the On-screen keyboard tab. It is also possible to use the 
`Input > Use L3 Button to Show Menu` option to default to the keyboard when first pressing L3.
The cursor on the