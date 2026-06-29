# OpenRigLogic

OpenRigLogic contains the RigLogic and DNA libraries that enable you to load a MetaHuman character with the same runtime rig evaluation as Unreal Engine. Both are available as native C++ libraries with Python bindings, ready to integrate into third-party content creation tools. OpenRigLogic is maintained by Epic Games.

MetaHuman has been adopted by some of the most successful games in the world, and is quickly becoming a standard for digital characters.  The DNA and RigLogic libraries found in OpenRigLogic are released in support of this developing standard.  The [RigLogic whitepaper](https://cdn2.unrealengine.com/rig-logic-whitepaper-v2-5c9f23f7e210.pdf) describes the design, file format, and runtime evaluation strategy in more detail.

## Contents

The OpenRigLogic repository contains:

* **DNA Library**: A C++ library for reading and writing MetaHuman DNA files, with Python bindings.  
* **RigLogic**: A highly optimized C++ library providing realtime evaluation of the MetaHuman rig, with Python bindings.  
* **Documentation:** A developer’s guide to integrating the RigLogic and DNA Libraries into your platform.

Sample assets and the MetaHuman Faceboard Control Rig may be acquired separately via the [OpenRigLogic Sample Content](https://www.fab.com/listings/27a81942-69bf-498e-a41f-004d0d2db37b) listing on Fab (available under the Fab Standard License).

## MetaHuman ecosystem compatibility

The implementation of technology such as OpenRigLogic creates an ecosystem of complimentary tools and products that enable a MetaHuman character to move seamlessly between different applications. 

Existing MetaHuman tools released by Epic Games (such as [MetaHuman Creator](https://dev.epicgames.com/documentation/metahuman/metahuman-creator) and [MetaHuman Animator](https://dev.epicgames.com/documentation/metahuman/metahuman-animator) in Unreal Engine and the [MetaHuman for Maya](https://www.fab.com/listings/9e3bf55e-d4c3-44fc-a3d4-ec4cb772ec29) and [MetaHuman for Houdini](https://www.fab.com/listings/7bbdfbb5-5eaf-4aa6-b32b-b8b048ebea25) plugins) are already part of this ecosystem. Your integration of OpenRigLogic into a third-party application enables you to take part in this ecosystem, providing compatibility with any MetaHuman character and tools you use to create them.

Typically, MetaHuman characters are created using [MetaHuman Creator](https://dev.epicgames.com/documentation/metahuman/metahuman-creator) in Unreal Engine. They can be exported using the **Export > DCC Export** tool. The exported package contains a DNA file for the head and a DNA file for the body-the inputs needed to drive the character with the libraries in OpenRigLogic. The character’s textures are also included.  Groom and clothing information is not currently part of this package.

## Branching and release strategy

OpenRigLogic follows a “live main, frozen stable” approach.

| OpenRigLogic branch | Stability |
| ---- | ---- |
| `main` | Experimental |
| `5.8` | Production-Ready |

### `main` branch

Most active development happens on the `main` branch. This branch is where new features are integrated and tested. We make it available for battle-hardened developers eager to test new features or work in lock-step with us.

If you choose to work in this branch, be aware that it is likely to be ahead of the branches for the current official release and the next upcoming release. Therefore, content and code that you create to work with the `main` branch may not be compatible with public releases until we create a new branch directly for a future official release.

This branch is best for developers who want the newest OpenRigLogic features.

### Stable branches (`5.8`, …)

Numbered branches identify past and upcoming official releases. Once a stable branch is created, it reflects the validated state of the libraries at that engine release. These branches are immutable snapshots with the exception of hotfix changes for critical fixes, and are recommended for production projects-use the branch that best matches your compatibility requirements.

## Supported platforms

OpenRigLogic supports a wide range of platforms that includes console platforms and mobile devices in addition to Windows, Linux, and macOS. 

Platform independence is a critical design feature. Real-time performance on each device is equally important.

## Dependencies

### Required

* **C++ Compiler** (supporting C++11 or higher)  
* [**CMake**](https://cmake.org/documentation/) (version 3.14+)

### Optional

These are only required if you enable specific build flags (e.g., tests, benchmarks, or language bindings).

| Dependency | Required for | Notes |
| ---- | ---- | ---- |
| [**SWIG**](https://www.swig.org/) | Python wrappers | Required at build time to generate the wrapper code |
| [**Python 3**](https://www.python.org/) (with Dev headers) | Python wrappers | Required at build time to compile the module, and at runtime to use it |
| [**Google Test**](https://git