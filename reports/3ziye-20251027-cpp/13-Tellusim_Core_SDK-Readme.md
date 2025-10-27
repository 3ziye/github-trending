# Tellusim Core SDK

Tellusim Core SDK is the foundational layer of the Tellusim Engine, providing low-level functionality for high-performance graphics, compute, and application development across multiple platforms and devices. It offers a unified C++ API designed to abstract hardware and OS differences, enabling developers to write portable and scalable applications in graphics, simulation, visualization, and AI.

The SDK includes comprehensive support for meshes, images, user interfaces, and GPU-accelerated algorithms such as radix sort, bounding volume hierarchies (BVH), fast Fourier transforms (FFT), and GPU-driven computational graph framework for machine learning and advanced data processing.

In addition to C++, the SDK provides bindings and interoperability for other languages such as C#, Rust, Swift, Python, Java, and JavaScript, making it suitable for use in native mobile and desktop applications as well as game and graphics engines.

Happy coding, and have fun creating with Tellusim!

## Licensing

* *Tellusim Core SDK* is free for educational use by students, teachers, and academic institutions.
* *Tellusim Core SDK* is free for non-commercial research by individuals or non-profit organizations.
* *Tellusim Core SDK* is free for individuals and companies with total annual revenue under USD $200,000.
* *Tellusim Core SDK* is free for evaluation, testing, learning, and other non-commercial experimentation.
* *Tellusim Core SDK* is free for open-source, non-commercial projects distributed under OSI-approved licenses (MIT, BSD, GPL, LGPL, or Apache 2.0), provided such projects generate no revenue and do not sell, license, or otherwise monetize software built with the Tellusim Core SDK.
* *Tellusim Core SDK* may be redistributed unmodified, along with binaries built with it, as part of free or open-source projects, provided the SDK itself is not sold, sublicensed, or rented for a fee.
* Any other use, including production deployment, commercial projects, or client-facing demonstrations, requires a Tellusim Commercial License.

For full license terms, see the [Tellusim Core SDK LICENSE](https://github.com/Tellusim/Tellusim_Core_SDK?tab=License-1-ov-file#readme)

For inquiries, visit: [Tellusim Services](https://tellusim.com/services/)

## Documentation and Support

* [Tellusim Core SDK Documentation](https://docs.tellusim.com/core)
* [Discord Channel](https://discord.gg/WmCGx6pvqY)
* [Support Forum](https://forum.tellusim.com/)

## Platforms

Please choose the correct branch for your platform:

| Platform      | Branch |
|---------------|--------|
| Windows x64   | [Windows x64 Branch](https://github.com/Tellusim/Tellusim_Core_SDK/tree/windows_x64) |
| Windows arm64 | [Windows arm64 Branch](https://github.com/Tellusim/Tellusim_Core_SDK/tree/windows_arm64) |
| Linux x64     | [Linux x64 Branch](https://github.com/Tellusim/Tellusim_Core_SDK/tree/linux_x64) |
| Linux arm64   | [Linux arm64 Branch](https://github.com/Tellusim/Tellusim_Core_SDK/tree/linux_arm64) |
| macOS x64     | [macOS x64 Branch](https://github.com/Tellusim/Tellusim_Core_SDK/tree/macos_x64) |
| macOS arm64   | [macOS arm64 Branch](https://github.com/Tellusim/Tellusim_Core_SDK/tree/macos_arm64) |
| Android       | [Android Branch](https://github.com/Tellusim/Tellusim_Core_SDK/tree/android) |
| iOS           | [iOS Branch](https://github.com/Tellusim/Tellusim_Core_SDK/tree/ios) |
| tvOS          | [tvOS Branch](https://github.com/Tellusim/Tellusim_Core_SDK/tree/tvos) |
| Web           | [Web Branch](https://github.com/Tellusim/Tellusim_Core_SDK/tree/emscripten) |

# Graphics

## [Clustered Lights](https://github.com/Tellusim/Tellusim_Core_SDK/tree/main/samples/graphics/lights/)

Forward shading with 16384 dynamic lights. This algorithm is compatible with deferred shading and transparent objects.

[![Clustered Lights](utils/browser/images/graphics/graphics_lights.jpg)](https://github.com/Tellusim/Tellusim_Core_SDK/tree/main/samples/graphics/lights/)

---

## [Meshlet Render](https://github.com/Tellusim/Tellusim_Core_SDK/tree/main/samples/graphics/meshlet/)

A massive meshlets rendering example with Mesh Shader for hardware and Compute Shader for software rasterization.  
'1' activates Instancing mode.  
'2' activates Mesh Shader mode.  
'3' activates Compute rasterization mode.

[![Meshlet Render](utils/browser/images/graphics/graphics_meshlet.jpg)](https://github.com/Tellusim/Tellusim_Core_SDK/tree/main/samples/graphics/meshlet/)

---

## [Mesh RayTracing](https://github.com/Tellusim/Tellusim_Core_SDK/tree/main/samples/graphics/traversal/)

Traversal class for the simple raytracing pipeline access. Vulkan or Direct3D12 API is required.

[![Mesh RayTracing](utils/browser/images/graphics/graphics_traversal.jpg)](https://github.com/Tellusim/Tellusim_Core_SDK/tree/main/samples/graphics/traversal/)

---

## [Mesh RayQuery](https://github.com/Tellusim/Tellusim_Core_SDK/tree/main/samples/graphics/tracing/)

Ray Query raytracing of animated sc