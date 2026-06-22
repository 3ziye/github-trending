<h1 align=center>
  📡 Micro Radar
</h1>
<h6 align=center>
  a tiny open-source flight radar for your desk
</h6>
<p align=center>
  <img src="https://github.com/user-attachments/assets/2ccb2063-d15c-4180-8e3c-ae3a81c814ff" alt="drawing" width="400"/>
</p>
<p align=center>
  <a href="#prerequisites">PREREQUISITES</a> - <a href="#assembly">ASSEMBLY</a> - <a href="#usage">USAGE</a>
</p>

## Prerequisites

At the core of this project is the ESP32-C3 module with an integrated 240x240 IPS screen. No soldering required. The module does all the heavy lifting.

I used dark grey PLA filament for the print, but any colour will work just fine. For the lens (optional but recommended), you'll need clear-drying epoxy to secure it (not super glue, which will fog up the lens. Ask me how I know.)

### Tools you'll need

- Small screwdriver (for M2 screws)
- Soldering iron (for setting the threaded inserts)

Set up a clean, organised workspace before you start. You'll be handling small components and epoxy, so a dedicated area helps. Keep a damp cloth nearby for cleaning if needed, and ensure your soldering iron has adequate ventilation.

### Shopping List

Everything you need is below. I've linked products I used and recommend for ease of build, though alternatives exist on Amazon and elsewhere. If you deviate from this hardware, you may need to modify the enclosure and/or code.

- [ ] [1.28" Round GC9A01 240x240 IPS Display Module with ESP32-C3 (no-touch)](https://www.aliexpress.com/item/1005008482665220.html)
- [ ] [USB-C Ribbon Extension Cable (5cm, CMUP-CFPCB-BK)](https://www.aliexpress.com/item/1005005371248824.html)
- [ ] [M2 Heat-set Threaded Inserts (+ soldering iron)](https://www.aliexpress.com/item/1005008493831823.html)
- [ ] [32.5mm Round Mineral Glass Lens (optional, recommended)](https://www.aliexpress.com/item/1005004783554496.html)
- [ ] [Gorilla Epoxy (necessary for fitting lens, useful anyway)](https://www.amazon.co.uk/Gorilla-Glue-25ml-Epoxy/dp/B009NQQJFC)

### Accounts / API

This project uses OpenSky's API for retrieving flight data.

I highly recommend making an account, as it's free, and allows the radar to make many more requests per day (400 -> 4000), which makes the live view much more accurate. However, it isn't necessary if you prefer.

You can sign up [here](https://opensky-network.org), or search "OpenSky".

Further info on what to do with the account is in the usage section.

## Assembly

Once you've got all the parts, assembly typically takes 1-2 hours (excluding print time).

**I strongly recommend reading the [Usage](#usage) section before you start assembly.** It'll help with troubleshooting if anything goes wrong. You might want to test the firmware and your hardware before closing everything up.

### Step 1: 3D Print

<img width="400" alt="FFCBBECA-6165-4138-8C84-16AB375511A2_1_105_c" src="https://github.com/user-attachments/assets/21c0753c-7d7c-425c-bdf6-0df037a8fdaa" />

Print all four STLs from `./hardware/stl/`:

- Main enclosure
- Front plate
- Bezel
- 2 spacers

### Step 2: Heat-set Threaded Inserts

**You'll need:** Soldering iron, M2 threaded inserts

Start with the front plate: insert 2mm M2 threaded inserts into the larger holes using the soldering iron.

<img width="400" alt="IMG_7882" src="https://github.com/user-attachments/assets/defcfb2c-cdff-4bf1-84b9-7fceeefb0caf" />

Next, the two spacers. These might warp slightly, that's fine. Insert 6mm M2 inserts into each.

<img width="400" alt="IMG_7887" src="https://github.com/user-attachments/assets/73b95049-5f12-4e2b-983a-5242c05f9106" />

Finally, the main enclosure. Insert 5mm M2 inserts.

<img width="400" alt="IMG_7891" src="https://github.com/user-attachments/assets/e36f3eec-31b5-468e-8451-9c428eaf9c21" />

Et voilà.

<img width="400" alt="IMG_7896" src="https://github.com/user-attachments/assets/97337223-223c-4531-90e1-f511adfb3d66" />

### Step 3 (Optional): Fitting the Lens

<img width="400" alt="IMG_7902" src="https://github.com/user-attachments/assets/e555f787-ca87-4558-b1eb-107f9071f96e" />

**You'll need:** Clear-drying epoxy, small applicator (match or cocktail stick works)

This is the fiddliest bit. Keep it neat and you'll avoid frustration:

- Apply epoxy to the front plate, not the lens
- Lower the front plate onto the lens (easier to manage excess epoxy)
- Have a cleaner ready for the edges (I used nail polish remover, your mileage may vary)
- Less is more with epoxy
- Work on a surface that won't bond to epoxy

<img width="400" alt="IMG_7911" src="https://github.com/user-attachments/assets/aa497389-efd5-45c3-84dc-c997232889ac" />

Let the epoxy cure according to its label before moving on.

### Step 4: Bezel

**You'll need:** 2x5mm M2 screws, 2x10mm M2 screws

Secure the bezel to the front plate using 2x5mm M2 screws through the threaded inserts you added earlier.

<img width="400" alt="IMG_7914" src="https://github.com/user-attachments/assets/37a3502a-83e1-4552-a399-9a914e0ec973" />

Screw 2x10mm M2 screws thro