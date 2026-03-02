# reblue - Blue Dragon Recompiled

> [!CAUTION]
> This project is in early development. It currently loads the main menu but immediately crashes after trying to load the new game cut scene. It appears to be a problem with the file IO, specifically how async is being handled. It requires more investigating (and hooks :))

Recompiled using the [ReXGlue SDK](https://github.com/rexglue/rexglue-sdk)

Currently with no hooks, it is crashing post-main menu.

https://github.com/user-attachments/assets/67566292-6280-446a-838c-00fcd44199a0

# Setup

1. Ensure REXSDK is set properly in your environment - see [ReXGlue SDK](https://github.com/rexglue/rexglue-sdk) for more info
1. Extract DVD1 to `assets` (full game is WIP)
1. Run cmake configure
1. Run reblue_codegen utility target from cmake
1. Run cmake build for reblue
1. Launch with first argument pointing to the assets folder

