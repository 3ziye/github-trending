--[ Quick Start - The Only Way That Matters

    grab firmware from GitHub releases. flash however you want.
    
    M5 Launcher? M5 Burner? esptool? web flasher? OTA? all work now.
    pick your poison. pig doesn't judge. pig recovers.
    
        1. github.com/0ct0sec/M5PORKCHOP/releases
        2. download. flash. oink.
        3. (first timer? check IMMORTAL PIG note below. tiny scroll.)
    
    XP preserved forever. your MUDGE UNCHA1NED grind stays intact.
    
    NEW IN v0.1.7_DNKROZ: CHRISTMAS BUILD. pig delivers presents.
    
        PCAP OVERHAUL - M1 M2 M3 M4 EAPOL frames. labeled. in order.
        radiotap headers that don't lie. wpa-sec.com full compliance.
        their validator no longer cries. hashcat 22000 ready. no excuses.
        scripts/wpasec_check.py included. verify before you upload.
        
        PORKCHOP COMMANDER - dual-pane file manager. norton would weep.
        F-keys at the bottom like god intended. multi-select with space.
        copy, move, rename, delete. tab between panes. keyboard nav.
        press 'F' from IDLE. because TransFer has F in it.
        
        UNLOCKABLES - pig has secrets. SHA256 validates the worthy.
        the pig whispers through tubes. if you know, you know.
        
        SESSION CHALLENGES - three trials per boot. EASY MEDIUM HARD.
        the pig talks when bored. complete all three for bonus.
    
    IMMORTAL PIG (v0.1.6+): why flashing method doesn't matter anymore.
    
        XP backs up to SD card. automatically. every save.
        M5 Burner nukes NVS? pig recovers from SD on boot.
        full chip erase? pig recovers. OTA flash? pig recovers.
        
        THE CATCH: first install must be v0.1.6+ to create the backup.
        no backup = no recovery. install once properly, flash freely after.
        
        backup location: /xp_backup.bin on SD card root.
        device-bound. signed. tamper-resistant. earned, not copied.
    
    the pig remembers. the pig always remembers.


--[ Contents

    1 - Introduction
    2 - What the hell is this thing
    3 - Capabilities
        3.1 - OINK Mode
            3.1.1 - CHILL DONOHAM Mode
            3.1.2 - Stationary Operation Tuning
        3.2 - WARHOG Mode
        3.3 - PIGGY BLUES Mode
        3.4 - HOG ON SPECTRUM Mode
            3.4.1 - CLIENT MONITOR
        3.5 - PORKCHOP COMMANDER
        3.6 - LOOT Menu & WPA-SEC Integration
        3.7 - Machine Learning
        3.8 - Enhanced ML Mode
        3.9 - XP System
            3.9.1 - IMMORTAL PIG
        3.10 - Achievements
        3.11 - SWINE STATS
        3.12 - Session Challenges
        3.13 - Unlockables
    4 - Hardware
    5 - Building & Flashing
        5.1 - Flashing Methods & Progress Preservation
    6 - Controls
    7 - Configuration
        7.1 - Color Themes
        7.2 - API Keys Setup
    8 - ML Training Pipeline
    9 - Code Structure
    10 - Legal sh*t
    11 - Greetz
    12 - Credits
    13 - Support The Pig


--[ 1 - Introduction

    christmas eve. you're reading a readme for an ASCII pig that hunts
    WiFi. your parents wonder where they went wrong. valid.
    
    PORKCHOP. pwnagotchi meets tamagotchi. nobody asked. we shipped.
    lives in M5Cardputer. tiny keyboard. big chaos energy.
    
    we did this with a Pringles can and a laptop in 2003. now you get
    an animated pig that does the work. you're welcome. or sorry.
    depends on your threat model.
    
    the pig sniffs. yoinks. deauths. tracks targets with proximity
    arrows. paints spectrum graphs. spams BLE until phones cry.
    40 ranks. 63 achievements. mood system. we have problems.
    
    catch a handshake - pig loses its mind. go passive - pig goes zen.
    wardrive - pig navigates. idle too long - pig gets sad. we spent
    real hours on pig emotions. no regrets.
    
    this is not a vandalism kit. it's a learning tool. understand the
    networks you use. audit what you own. no unauthorized deauths.
    loot drops passively. zero TX. right place, right time.
    it's gambling with extra steps. same dopamine. cheaper.
    tools don't make choices. you do. don't be a tool.
    
    the pig is a tool. you're not. act accordingly.
    
    merry christmas. oink.


--[ 2 - What the hell is this thing

    PORKCHOP runs on M5Cardputer (ESP32-S3). 1.5MB binary. no bloat.
    the pig knows what it is.

        - passive WiFi reconnaissance (or not so passive. your call.)
        - WPA/WPA2 handshake capture (4-way EAPOL reconstruction)
        - PMKID yoink from M1 frames (clientless. surgical. quiet.)
        - CLIENT MONITOR - track individual devices by signal strength
        - proximity arrows show if target is walking toward or away from you
        - targeted deauth - disconnect specific clients, not broadcast spam
        - GPS-enabled wardriving with WiGLE export
        - BLE notification spam (Apple, Android, Samsung, Windows)
        - real-time 2.4GHz spectrum visualization with vuln indicators
        - ML-power