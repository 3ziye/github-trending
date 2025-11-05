![Screenshot of Android application with title AbxDroppedApk and lots of text describing that it is running within system_server](Screenshot_20231024-164541.png)

Fixes for issue described here appeared under CVE-2024-34740 / A-307288067:

* [Bulletin](https://source.android.com/docs/security/bulletin/2024-08-01#Framework)
* [Patch linked from bulletin](https://android.googlesource.com/platform/frameworks/libs/modules-utils/+/700c28908051ceb55e1456d2d21229bc17c6895a)
* Two other patches: [1](https://android.googlesource.com/platform/frameworks/base/+/8b1e072210796e9772d3d07bdbae424b38447db6%5E!/) [2](https://android.googlesource.com/platform/frameworks/base/+/7250d76a8a2d501af62081d88545c301d43106a4%5E!/)

# Android Binary XML

Inside Android `system_server`, many services store their state across reboots in XML files

```
$ adb shell su 0 find /data/system -name '*.xml' | sort
/data/system/appops_accesses.xml
/data/system/cachequota.xml
/data/system/device_policies.xml
/data/system/device_policy_state.xml
/data/system/display-manager-state.xml
/data/system/input-manager-state.xml
/data/system/inputmethod/subtypes.xml
/data/system/install_sessions.xml
/data/system/job/jobs_1000.xml
/data/system/job/jobs_10131.xml
/data/system/log-files.xml
/data/system/netpolicy.xml
/data/system/notification_policy.xml
/data/system/overlays.xml
/data/system/packages.xml
/data/system/package-watchdog.xml
/data/system/sensor_privacy_impl.xml
/data/system/sensor_privacy.xml
/data/system/shortcut_service.xml
/data/system/users/0/app_idle_stats.xml
/data/system/users/0/appwidgets.xml
/data/system/users/0/package-restrictions.xml
/data/system/users/0/settings_global.xml
/data/system/users/0/settings_secure.xml
/data/system/users/0/settings_system.xml
/data/system/users/0/wallpaper_info.xml
/data/system/users/0.xml
/data/system/users/userlist.xml
/data/system/watchlist_settings.xml
```

Historically these have been plain text XML files with indentation, which allowed developers easy reading of them, however [in Android 12 new binary version of that format was introduced, citing 1.5% of all time spent by `system_server` being spent on these XML operations](https://android.googlesource.com/platform/frameworks/base/+/4ccea8796991d678ead4399130ec31edf63ff4fa%5E%21/)

It should be noted that this format is only used internally by system and has files with magic value `"ABX\x00"`. It is different from [format used inside APKs](https://cs.android.com/android/platform/superproject/main/+/main:frameworks/base/libs/androidfw/ResourceTypes.cpp;l=1770;drc=d4e49e63519397789d284a03aea5fafc119cb1b0) for `AndroidManifest.xml`, `res/xml/*.xml`, `res/layout/*.xml`, etc. which has no explicit "magic value", however usually starts `0300 0800` (which is [header](https://cs.android.com/android/platform/superproject/main/+/main:frameworks/base/libs/androidfw/include/androidfw/ResourceTypes.h;l=608;drc=d4e49e63519397789d284a03aea5fafc119cb1b0) with `type=RES_XML_TYPE` and `headerSize=8`)

Whenever system reads one of these internal state XML files, it [uses `"ABX\0"` magic value in file to choose either parser for Binary XML file or regular XML parser](https://cs.android.com/android/platform/superproject/main/+/main:frameworks/base/core/java/android/util/Xml.java;l=188-192;drc=97a370a95275e79c69e79d7ead11aa38934a5575). Whenever these files are saved as Binary XML is [controlled by system property](https://cs.android.com/android/platform/superproject/main/+/main:frameworks/base/core/java/android/util/Xml.java;drc=97a370a95275e79c69e79d7ead11aa38934a5575;l=74?q=Xml.java) and is enabled by default

When Binary XML files are in use, you can read their contents for example through `adb shell su 0 abx2xml /data/system/packages.xml -`

One of things this binary format does is offering typed accessors, so serializer offers `attributeInt(String namespace, String name, int value)` method, which writes value as binary integer, avoiding round-trip through String which would be new allocation and subsequent object for Garbage Collection

Another type that can be directly serialized is byte array

```java
@Override
public XmlSerializer attributeBytesBase64(String namespace, String name, byte[] value)
        throws IOException {
    if (namespace != null && !namespace.isEmpty()) throw illegalNamespace();
    mOut.writeByte(ATTRIBUTE | TYPE_BYTES_BASE64);
    mOut.writeInternedUTF(name);
    mOut.writeShort(value.length);
    mOut.write(value);
    return this;
}
```

There's also similar method `attributeBytesHex` which only differs by `TYPE_*` tag written. That tag is used by `abx2xml` tool to convert byte array to appropriate String representation

`mOut` is instance of `FastDataOutput`, which provides functions of Java's [`DataOutputStream`](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutputStream.html). `writeByte`/`writeShort`/`writeInt`/`writeUTF`/`write` use same format as standard `DataOutputStream`

Similarly to [`Parcel`](https://github.com/michalb