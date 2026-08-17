# Matter Protocol Air Conditioner Controller for Any Brand (ESP32 + BC7215 Project)

## Key Features

- Connect virtually any air conditioner—old or new, directly to Apple Home, Google Home, or Home Assistant
- No app installation required
- No account registration required
- No touching of the air conditioner's internal circuit required

![](img/use-illustration_1280px.jpg)

Matter is a new IoT protocol that is now built into iPhones and Android phones. This means that Matter-compatible devices can be operated directly in environments such as Apple Home without installing a dedicated app.

This device is an offline air conditioner controller. The air-conditioner control function itself does not require a network connection, so it does not depend on any third-party service and does not require account registration.

If you already use Home Assistant, the sister project—the ESPHome version of this project ([https://github.com/timj-code/bc7215_ac_esphome](https://github.com/timj-code/bc7215_ac_esphome))—may be more suitable for you. Matter support for air conditioners is still at an early stage and provides relatively limited functionality, so it is not as comprehensive as Home Assistant.

Based on my experience during development, neither Apple Home nor Google Home is especially smooth enough when controlling devices such as air conditioners that require real-time feedback. There can sometimes be noticeable delays before control results appear on the phone, and establishing a connection can also take a relatively long time. **Overall, however, it is still a very cool way to add smart control to an air conditioner that has not yet been integrated into your smart home—or to give one to a friend who has an iPhone—because it is not restricted to particular air conditioner brands or models, requires no additional app, and requires no extra controller device for iPhone users.**

## Limitations

Matter devices can be used without a dedicated app. This is an advantage, but it also has a downside: the user experience is largely outside the device manufacturer's control. For example, the interface and overall experience may differ significantly between Apple and Android platforms, especially for a complex device such as an air conditioner.

Matter is also still evolving, and its support for air conditioners remains limited. Air conditioner functions are mainly mapped to HVAC system modes. Many functions found on split-system air conditioners have no corresponding mapping in the protocol, or may be defined by the protocol but not yet supported by smartphone platforms.

The limitations I have found so far are listed below.

#### Protocol Limitations

| Item                   | Conventional Split-System Air Conditioner                                                                     | Matter Protocol                                                                                                                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Temperature control    | A single target temperature                                                                                   | Separate cooling and heating target temperatures. In Auto mode in particular, a temperature range is set instead of a single target temperature.                                                                |
| Temperature resolution | Usually 1°C. The air conditioner control library used by this device also supports integer temperatures only. | The device cannot specify the temperature adjustment step through the protocol. Apple and Google currently both use 0.5°C as the minimum adjustment step.                                                       |
| Fan control            | Usually four levels: Auto, High, Medium, and Low                                                              | The fan section has its own power switch. The protocol supports both discrete fan levels and percentage-based control, but smartphone vendors currently appear to support only percentage-based fan adjustment. |

Project implementation: only the most common Cooling and Heating modes are currently supported. Other modes are not yet supported. Fan settings from 1% to 33% are mapped to Low, 34% to 66% are mapped to Medium, and values above 66% are mapped to High. When the temperature is set to a value ending in 0.5°C, it is automatically rounded up to the next whole degree.

#### Limitations Introduced by Application Platforms

I have currently tested only the four platforms below. If you can help test other Matter-compatible IoT platforms, such as Tuya, Xiaomi, or Aqara, a