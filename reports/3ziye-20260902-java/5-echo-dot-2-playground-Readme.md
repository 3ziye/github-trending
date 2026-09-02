# Echo Dot 2 Playground

This is an ongoing repository with test scripts and experiments for the Amazon Echo Dot 2 (biscuit).

**Live demo:** [Watch on YouTube Shorts](https://youtube.com/shorts/GjYZxhKTk0c?feature=share)

## Getting Started

To run these scripts, you must first unblock the bootloader and gain root access on your Echo Dot 2. 

1. **Unlock & Root:** Follow the firmware unlocking guide available at [XDA Forums](https://xdaforums.com/t/unlock-root-twrp-unbrick-amazon-echo-dot-2nd-gen-2016-biscuit.4761416).
2. **Required Scripts:** You will need to flash the exploit script downloadable from [this specific post](https://xdaforums.com/t/unlock-root-twrp-unbrick-amazon-echo-dot-2nd-gen-2016-biscuit.4761416/post-90631621).

> **Note for Mac Users:** Even though the original guide focuses heavily on Linux, the scripts provided on the XDA forum also work on Mac! I was able to follow along and execute the exploit steps successfully on macOS.

## Contents

- [`test-scripts/`](./test-scripts/) - Contains shell scripts to test device I/O (buttons, LEDs, etc.) natively on the Echo Dot 2. 
  - `connect-to-wifi.sh`: Connects the Echo Dot to a Wi-Fi network by injecting credentials into `wpa_supplicant.conf` via ADB and requesting a DHCP lease via `dhcpcd`.
- [`debloat/`](../debloat/) - Contains `soft-debloat.sh`, a script to dynamically disable/hide unnecessary Amazon packages, rename bloat binaries, replace `bootanimation` with a no-op stub, and patch `/system/etc/audio_init.sh` to permanently disable the infinite spinning cyan LED ring via hardware sysfs (`is31fl3236`).
- [`custom-voice-assistant/`](./custom-voice-assistant/) - Suite containing the custom assistant (`echo-dot-assistant`) and dedicated multi-process Pryon/Alexa wake-word service (`echo-dot-wakeword`), managed by a unified parent Makefile.
- [`reverse-engineer-speech-interaction/`](./reverse-engineer-speech-interaction/) - Decompiled sources, native library JNI probes, and reverse-engineering logs for Fire OS's native speech and wake-word stack (`libwakewordserver_jni.so` + `libpryon.so`).

### Proprietary Amazon files

The repository does not include Amazon's proprietary APKs or native `.so`
libraries. They are referenced by name in the notes only. These files are
copyrighted and must not be shared or redistributed. To run the wake-word
experiments locally, pull the required files from your own rooted Echo Dot or
extract them from a firmware image you obtained yourself.

The tested firmware was
`update-kindle-csm_biscuit-272.6.8.0_user_680767620.bin`, available through the
Echo Dot 2 rooting thread on XDA. From
`reverse-engineer-speech-interaction/`, use `./pull-and-decompile.sh --find` to
locate candidate files on a connected Echo, `./pull-and-decompile.sh
--pull-native` to pull them into the ignored `local-native-libs/` directory, or
`./pull-and-decompile.sh --extract-apk SpeechInteractionManager.apk` after
obtaining the APK yourself.

## Echo Dot Custom Voice Assistant Stack

The overall architecture replaces Amazon's cloud stack with a fully local, privacy-focused pipeline running on the Echo Dot 2 (API 22, Android 5.1, `armeabi-v7a`):

1. **Wake-Word Engine (`echo-dot-wakeword`):**
   - Installed as a system app (`/system/priv-app/CustomWakeWord`) with `CAPTURE_AUDIO_HOTWORD` permissions.
   - Interfaces directly with native `libpryon.so` / `libwakewordserver_jni.so` to run low-power local wake word detection ("Alexa").
2. **Speech-to-Text (`echo-dot-assistant`):**
   - Uses native **Sherpa-ONNX** (`libsherpa-onnx-jni.so` linked against ONNX Runtime 1.14.0) for fast, offline streaming ASR.
3. **Local LLM Engine (`llama-server`):**
   - Uses an app-managed, background `llama-server` running `MobileLLM-125M-Q4_K_M.gguf`.
   - Uses prompt caching (`cache_prompt=true`) to reduce warm query latency from ~17.3s (cold `llama-cli`) down to **~2.3s**.
   - Outputs JSON-constrained function calls (e.g., `LIGHT` or `VOLUME` actions).

## Development & Automated Testing

A parent Makefile in `custom-voice-assistant/` simplifies building, deploying, and testing all components:

```bash
cd custom-voice-assistant

# Build and install both assistant and wake-word APKs
make deploy

# Run automated device test suite
make test_all     # Runs wake-word, STT, and LLM tests end-to-end
make test_stt     # Tests Sherpa-ONNX speech recognition
make test_llm     # Tests llama-server inference & command parsing
make test_wake    # Tests native Pryon wake-word service
```

### Manual ADB Pipeline Testing

You can also trigger pipeline components programmatically via ADB intents:

**Testing STT Pipeline:**
```bash
adb shell am force-stop com.custom.assistant
adb shell logcat -c
adb shell am startservice -n com.custom.assistant/.AudioService --es TEST_MODE STT
adb shell logcat -v time -s CustomAssistant AndroidRuntime
```

**Testing LLM Pipeline:**
```bash
adb shell am force-stop com.custom.assistant
adb shell logcat -c
adb shell 'am startservice -n com.custom.ass