# 𝖒𝖆𝖋's Keyer 🎹

Firmware & goodies for making a [Keyer](https://en.wikipedia.org/wiki/Keyer) (one-handed version of a [chorded keyboard](https://en.wikipedia.org/wiki/Chorded_keyboard)).

<table>
  <tr>
    <td><img src="photos/photo1.jpg" alt="Keyer in an open hand"></td>
    <td><img src="photos/photo2.jpg" alt="Keyer held in hand"></td>
  </tr>
  <tr>
    <td><img src="photos/photo3.jpg" alt="Keyer viewed from the front"></td>
    <td><img src="photos/photo4.jpg" alt="Keyer hanging on a glove"></td>
  </tr>
  <tr>
    <td><img src="photos/photo5.jpg" alt="Keyer on a table"></td>
    <td><img src="photos/photo6.jpg" alt="Closeup of a keyer on a table"></td>
  </tr>
</table>

**Features**:

- **Minimal finger movement**: it's like typing with all the keys on your home row all the time
- **Free hand while typing**: you can use your other hand to sip tea while typing (or move the mouse - if you're not a tea drinking type)
- **Always near your hand** - keyer can be attached to a glove so you can just release it and have both of your hands free. Now you can drink your tea and move the mouse at the same time.
- **Tons of chords**: a 10-key keyer (3 keys on thumb, 2 index, 2 middle, 2 ring, 1 pinky) can express up to 215 chords (&times; 2 when counting hold-chord alternatives). With so many chords you can lose a finger and still touch type (carpenters will love it!)
- **Arpeggios**: an additional 2 &times; 78 arpeggios - rolling motion over two keys that can be executed in two directions and can be used for even more input options.
- **Multiple layers**: if the 586 shortcuts available on the base layer are somehow not enough for you
- **Rolling chords**: when two subsequent chords you're entering share some finger positions you can only move the finger that changes position. When combined with optimized layouts (see the next point) typing is like walking through the keys one finger at a time.
- **Optimized layout**: a bundled layout optimizer will perform a combinatorial search over all possible layouts to find the optimal one for typing the texts that you give it (or for your custom finger press / finger movement cost function). Then learn to type with it in the [keyer flight school🛦](https://mafik.github.io/keyer/).
- **Ergonomic layout 🖖**: did you know your fingers share the neuro-motor pathways and can't always move independently? The layout generator will avoid finger combinations that are hard to press.
- **Low-latency**: the firmware uses hardware interrupts to be more responsive than polling-based keyboards and it also does debouncing in software to be more responsive capacitor-based debouncers.
- **Power for months**: a massive 18650 battery + underclocked CPU + firmware able to sleep without losing the Bluetooth connection + hardware power switch on the board mean that you will charge it about as often as a Casio watch.
- **🕶️**: combine it with smart glasses to control your computer (or smartphone) without looking or touching. It's like [Meta EMG wristband](https://www.youtube.com/watch?v=wteFJ78qVdM) but actually working!
- **Easy to build**: did you ever play with Play-Doh? This keyer was built with modelling clay (baked in the oven for 30 minutes). No 3D printing. No custom PCBs. You can make it with parts from amazon, a hot glue gun and a soldering iron.
- **Perfect fit**: you build it yourself, literally molding it to the shape of your hand. You can't get more ergonomic than that.
- **Cheap to build**: it's less than 50 USD to make one yourself. Mechanical keyboards are a cheap hobby now. Who would have thought!

Typing video [youtube.com/watch?v=Ijwo7SQQ73Q](https://www.youtube.com/watch?v=Ijwo7SQQ73Q) (from Typeware).

## 🐾 Links (a.k.a. 💫 Awesome Keyers 🎹)

(Send me your links on Bluesky [bsky.app/profile/mrogalski.eu](https://bsky.app/profile/mrogalski.eu) so that I can add them here!)

- [Penti Chorded Keyboard](https://software-lab.de/penti.html) - A software keyer that can run on a touchscreen. Notable for its use of arpeggios.
- [ESP32-BLE-Keyboard](https://github.com/T-vK/ESP32-BLE-Keyboard/tree/master) - Excellent library for turning ESP32s into custom keyboards.

**3d-printed keyers**:

- [Keyyyyyyyys!](https://www.stavros.io/posts/keyyyyyyyys/) - Can you get scrappier than that?
- [Ignacio's keyboard](https://medium.com/@tartavull/thor-your-next-keyboard-20b9ce7dd2b1)

**Commercial products**:

- [Twiddler](https://www.mytwiddler.com/) - 19 tiny keys + touchpad for $229
- [Decatext](https://decatxt.com/) - 10 large keys + typing guide right on the device for $175 (its author also shared the promo code "Neural" for $15 off!)
- [Typeware](https://typeware.tech/) - ultra lightweight & probably the best all-around design for $273 (pre-orders only 😔)

**Memes**:

- [Mobile Text Entry Device](https://patents.google.com/patent/US20030179178A1/en) - 💩
- [I love the powerglove.](https://www.youtube.com/watch?app=desktop&v=KZErvASwdlU) - it's so bad
- [Johnny Mnemonic](https://www.youtube.com