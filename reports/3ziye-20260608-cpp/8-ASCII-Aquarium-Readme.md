## Meet the ASCII Aquarium ><(((°> 
<table>
  <tr>
    <td width="45%" valign="top">
<p>
  A tiny animated ASCII fish tank for the ESP32-2432S028R Cheap Yellow Display.
</p>
      <p>
      Flash it from the browser, tap to feed the fish, tune the tank, sync the clock over Wi-Fi, and let the punctuation swim.
      </p>
      <p>
        <a href="https://power-pill.github.io/ASCII-Aquarium/">
          Flash ASCII Aquarium CYD
        </a>
      </p>
      <p>
        ASCII Aquarium turns the common 320x240 CYD touchscreen into a living little
desktop aquarium with swimming ASCII fish, rising bubbles, swaying seaweed,
tap-to-feed flakes, occasional octopus and seahorse visitors, touch controls,
Wi-Fi time sync, persistent settings, and SD-card screenshot capture.
</p>
<p>
        It is not a video loop. The aquarium is rendered live on the ESP32, with fish
that wander, school, turn around, change brightness, avoid each other, and chase
food when you tap the glass.
      </p>
    </td>
    <td width="55%" valign="top">
      <img
        src="https://github.com/user-attachments/assets/34200303-25c9-45c5-a6eb-1e53a6c267d7"
        alt="ASCII Aquarium Title Screen"
        width="100%">
    </td>
  </tr>
</table>

Check out the article on Hackaday! https://hackaday.com/2026/05/24/adorable-ascii-aquarium-lives-on-your-desk

## GIFs of the ASCII AQUARIUM in Action }>{{{{• >

<table>
  <tr>
    <td width="50%" valign="top">
    <img
        src="https://github.com/user-attachments/assets/b350f4ad-5aa9-4560-84a4-927dffa96d35"
        alt="Settings"
        width="100%">
    </td>
    <td width="50%" valign="top">
      <img
        src="https://github.com/user-attachments/assets/12696457-80b7-4ba0-9382-38a2e72ea84d"
        alt="Feeding the Fish"
        width="100%">
    </td>
  </tr>
</table>

## ASCII Aquarium Web Flasher >)))'>

The easiest way to install ASCII Aquarium
 is with the browser flasher:

[Flash ASCII Aquarium CYD](https://power-pill.github.io/ASCII-Aquarium/)

You will need:

- A supported [CYD board](https://www.aliexpress.com/item/1005004971720824.html) connected by a USB data cable.
- Chrome, Edge or latest Firefox Browser on a desktop or laptop computer.
- The Arduino IDE Serial Monitor closed, if it was open.

Open the flasher page, click **Flash ASCII Aquarium**, choose the CYD serial
port, and let the installer finish.

## Supported Hardware: CYD, CYD2USB & JC3248w535
This firmware is built for the [ESP32-2432S028R "Cheap Yellow Display" board](https://www.aliexpress.com/item/1005004971720824.html):

[https://www.aliexpress.com/item/1005004971720824.html](https://www.aliexpress.com/item/1005004971720824.html)
[https://www.amazon.com/dp/B0FJQ6RK39](https://www.amazon.com/dp/B0FJQ6RK39)

- ESP32
- ILI9341 320x240 display
- XPT2046 resistive touchscreen
- Optional SD card support for BMP screenshots and frame capture

Other CYD-style boards may look similar but use different display, touch, or SD hardware.

**Support has now been added for the CYD2USB variant of the board courtesy of @mjpcomp**

Also, we have preliminary support for the much nicer [JC3248w535 board](https://www.aliexpress.com/item/1005007566332450.html)! 

**[Use the web flasher to flash either of these new firmwares to your board!](https://power-pill.github.io/ASCII-Aquarium/)**

## 3D Printed 2.8" CYD Cases ><((((>`
- [Basic Snap-fit case by PowerPill.Prints](https://makerworld.com/en/models/2835243)
- [CYD Desk Buddy by annaglyph](https://makerworld.com/en/models/2787810) 

## Features >(°)>

- Animated ASCII fish with multiple glyph species, varied colours, depth shading,
  smooth wraparound, schooling, wandering, and separation behaviuor.
- Tap-to-feed flakes that nearby fish chase down.
- Configurable fish population from 6 to 36.
- Configurable bubble count from 0 to 50.
- Animated bubbles and seaweed with adjustable sway, length, and randomness.
- Visiting octopus and seahorse characters with selectable spawn rates.
- Fish steer around visitors and each other.
- Background styles: black, blue fade, purple fade, and randomized Spongebob style flower backdrop.
- Touch settings menu with Tank, Seaweed, Clock, and Background tabs.
- Optional on-screen clock with manual time or internet time.
- 12-hour and 24-hour clock formats.
- Timezone selection, small top or bottom clock, large ASCII clock style, and clock colour picker.
- Wi-Fi panel with network scan, saved credentials, on-screen keyboard, reconnect handling, and NTP time sync.
- Persistent settings using ESP32 Preferences.
- SD-card BMP screenshots and frame sequence capture. (NOTE - in build 2.18 The CYD will need to be reset after taking screenshots or sequences)
- Hidden HUD controls for setup, capture, Wi-Fi, settings, quick creature tests, respawn, and randomize. 

## New Features in 2.20 ><((((>`

[Detailed Release Notes for 2.20 can be found here](https://github.com/POWER-PILL/ASCII-Aquarium/blob/main/ASCII_Aquarium_Release_Notes_v2.20.md).

- New Overhauled 