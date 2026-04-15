# react-native-notify-kit

Maintained Notifee-compatible fork — a feature-rich React Native notification library (Android & iOS).

<!-- markdownlint-disable MD033 -->
<p align="center">
  <a href="https://www.npmjs.com/package/react-native-notify-kit"><img src="https://img.shields.io/npm/v/react-native-notify-kit.svg" alt="npm version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue.svg" alt="License"></a>
  <img src="https://img.shields.io/badge/platform-Android%20%7C%20iOS-green.svg" alt="Platform">
  <img src="https://img.shields.io/badge/React%20Native-%3E%3D0.73-blue.svg" alt="React Native">
</p>

<hr/>

An actively maintained fork of Notifee for React Native notifications, continued and improved by Marco Crupi.

This repository preserves the original Notifee APIs and native core while continuing development for modern React Native releases.

## Why this fork

The original [Notifee](https://github.com/invertase/notifee) repository was **officially archived** by Invertase on April 7, 2026 (last release: v9.1.8, December 2024). The archived README recommends this fork (`react-native-notify-kit`) as a community-maintained drop-in replacement, alongside `expo-notifications`. Previously, in [issue #1254](https://github.com/invertase/notifee/issues/1254), the Invertase maintainer had already suggested migrating to `expo-notifications`.

However, `expo-notifications` does not cover several advanced capabilities that many production apps rely on:

- **Android foreground services** (ongoing notifications for background tasks)
- **Rich notification styles** (BigPicture, Messaging, Inbox)
- **Progress bar notifications**
- **Full-screen intent notifications** (alarm/call screens)
- **Ongoing / persistent notifications**

This fork fills the gap: it preserves all of Notifee's advanced features, migrates the bridge to React Native's **New Architecture** (TurboModules), and actively fixes the critical bugs left unresolved upstream — see the [bug fix table](#bugs-fixed-from-upstream-notifee) below.

## Project Status

<a href="https://github.com/marcocrupi/react-native-notify-kit/commits"><img src="https://img.shields.io/github/last-commit/marcocrupi/react-native-notify-kit.svg" alt="Last commit"></a>

- Officially recommended by Invertase as the community-maintained fork (April 2026)
- Maintained fork of Notifee — actively developed and published as `react-native-notify-kit`
- New Architecture only (TurboModules)
- Minimum supported React Native: `0.73`
- Development target: React Native `0.84`
- License: `Apache-2.0`
- Full changelog: [CHANGELOG.md](CHANGELOG.md)

The native core (NotifeeCore) is compiled from source as part of the bridge module (since 9.2.0) and the public API is **100% compatible** with the original `@notifee/react-native` — migration is a safe, drop-in replacement.

## Installation

```bash
yarn add react-native-notify-kit
# or
npm install react-native-notify-kit
```

For iOS, run `cd ios && pod install` after installing.

## Migration from @notifee/react-native

If you're coming from the original Notifee package, migrating takes just a few steps:

1. **Swap the package:**

   ```bash
   yarn remove @notifee/react-native
   yarn add react-native-notify-kit
   ```

2. **Update imports** — find and replace across your codebase:

   ```diff
   - import notifee from '@notifee/react-native';
   + import notifee from 'react-native-notify-kit';
   ```

   The default export is still called `notifee`, so your application code stays the same — only the import path changes.

3. **Reinstall pods** (iOS):

   ```bash
   cd ios && pod install
   ```

No native code changes are required. The public API is fully compatible with `@notifee/react-native`.

## Quick Start

```ts
import notifee, { AndroidImportance } from 'react-native-notify-kit';

// 1. Request permission (required on Android 13+ and iOS)
await notifee.requestPermission();

// 2. Create a channel (Android only, required for Android 8+)
await notifee.createChannel({
  id: 'default',
  name: 'Default Channel',
  importance: AndroidImportance.HIGH,
});

// 3. Display a notification
await notifee.displayNotification({
  title: 'Hello',
  body: 'This is a local notification',
  android: { channelId: 'default' },
});
```

> **Note:** The default export name `notifee` is kept intentionally for backward compatibility. If you're migrating from `@notifee/react-native`, a simple find-and-replace of the import path is all you need.

### 4. Handle events

In your `index.js` (before `AppRegistry.registerComponent`):

```ts
import notifee from 'react-native-notify-kit';

// Background/killed state events
notifee.onBackgroundEvent(async ({ type, detail }) => {
  console.log('Background event:', type, detail.notification?.id);
});
```

In your React component:

```ts
import { useEffect } from 'react';
import notifee, { EventType } from 'react-native-notify-kit';

useEffect(() => {
  return notifee.onForegroundEvent(({ type