![Cover-21](https://github.com/user-attachments/assets/770e4972-84f7-433e-87db-6391601256ba)
Born React Native Godot
-----------------------

React Native Godot allows embedding the Godot Engine into React Native applications.

Born React Native Godot was created by [Born](https://born.com) and developed by [Migeran](https://migeran.com), in close collaboration between the two teams.

# Main Features

* Supports Android and iOS, built on [LibGodot](https://github.com/migeran/libgodot).
* Stable implementation serving millions of users in [Born](https://born.com)'s applications.
* Supports starting, stopping and restarting the Godot Engine. [(docs)](#initialize-the-godot-instance)
* When restarting, the engine can be reconfigured, so a different Godot app may be loaded each time. [(docs)](#stop-the-godot-instance)
* It is also possible to pause and resume the running Godot instance. [(docs)](#pause-the-godot-instance)
* Godot is running on a separate thread, so it does not affect the main thread of the application nor the React Native JavaScript thread. [(docs)](#threading-and-javascript-in-react-native)
* The Godot main window and any subwindows created by the Godot app may be embedded into the React Native application either on the same screen, or on separate screens (see [example app](example/)).
* The whole Godot API is accessible from TypeScript / JavaScript. It is possible to instantiate objects, call methods, get and set properties, attach JS functions to signals, provide JS functions as callables to Godot methods ... etc. [(docs)](#godot-api-usage)

<p align="center">
  <video src="https://github.com/user-attachments/assets/33266f05-d733-4c1d-ab49-edaaf426e3e1" width="600" controls></video>
</p>

# Getting Started with the Example App

The [example app](example/) shows the main features of React Native Godot in action.

## Install Prerequisites

During development we use [ASDF](https://asdf-vm.com/) to manage most external dependencies required for React Native development, like Node, Java, Gradle or Ruby. If you also use ASDF, just run:

```sh
asdf install
```
    
This will make sure that all the dependencies are the same like in our environment. Otherwise you may also install React Native prerequisites using any other method.

## Export the Godot app

Run the following scripts for either platform you plan to test (or both):

```sh
cd example
./export_godot_GodotTest.sh android
./export_godot_GodotTest.sh ios
./export_godot_GodotTest2.sh android
./export_godot_GodotTest2.sh ios
```

The script is configured to look for Godot in the standard system wide installation folder on macOS. If your Godot is installed elsewhere, or you are on Linux, just point the `GODOT_EDITOR`
environment variable to your Godot editor prior to running the above scripts:

```sh
export GODOT_EDITOR=/path/to/godot_editor
```

## Configure and download LibGodot

```sh
cd example
yarn
yarn download-prebuilt
```

These commands will resolve all the React Native and other dependencies from npm. The second one will download the prebuilt LibGodot release from GitHub.

## Run on the iOS Simulator

```sh
cd example/ios
bundle install
bundle exec pod install
cd ..
yarn ios
```

## Run on the Android Emulator

```sh
cd example
yarn android
```

## Use your native IDEs

You may use Xcode and Android Studio the same way as with any other project. Just open:

* ``ios/GodotTest.xcworkspace`` from Xcode
* ``android`` from Android Studio

> [!note]
> If you are using ASDF to manage your Java and Node dependencies, you should start Android Studio from under the `react-native-godot` (or `example`) folder, so it can find these tools. For example on macOS:

```sh
cd example
open -a "Android Studio"
```

## Convenience script for dependency management

There is an `update_deps.sh` script included in the example app's folder. It will execute all the setup commands for both iOS and Android in one step, so you may start your work immediately.

```sh
cd example
./update_deps.sh
yarn ios # or yarn android
```

# Your first React Native Godot App

Born React Native Godot is distributed on npm.

Just follow these steps to add it to your React Native application:

## Update `package.json`

```sh
yarn add @borndotcom/react-native-godot
```

## Download the prebuilt LibGodot packages

The LibGodot packages used by React Native Godot are not distributed on npm. Instead, they are downloaded separately by issuing the following command:

```sh
yarn download-prebuilt
```

This way React Native Godot can be updated independently from LibGodot, and also local, customized builds of LibGodot are supported.

## Import React Native Godot in your App code

```typescript
import { RTNGodot, RTNGodotView, runOnGodotThread } from "@borndotcom/react-native-godot";
```

## Add the Godot View to your view, e.g.

```tsx
const App = () => {
  return (
    <View>
      <RTNGodotView style={...}/>
    </View>
  );
};
```

If no `windowName` property is specified, that view is fo