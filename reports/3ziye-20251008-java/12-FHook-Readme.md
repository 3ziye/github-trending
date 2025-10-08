<p align="right">Language: <b>English</b> · <a href="README.cn.md">Chinese</a></p>

# FHook

**Full-function HOOK framework for the Android Java layer**

* **debug mode** — initialize and use directly inside the app
* **Android 9+ (API 28+)**, including the latest versions
* Intercept and modify **arguments/return values** of any **Java method**
* **Class/instance-wide batch hooks**, covering common **system hotspots** (class loading, device fingerprint, SharedPreferences writes, etc.)
* Three integration options: Gradle dependency (`implementation`), source integration (module/source copy), and (under compliance) app injection (repack or dynamic loading)

> For **lawful** security research, testing, and debugging only. Ensure you have proper authorization for any target.

---

## 1. What problem does it solve?

* **Rapid observation**: print call stacks/args/returns at runtime without touching target code
* **Temporary patching**: tweak args/returns or feed “mock data” to verify branches
* **Batch coverage**: one-click hook for all methods on a class/instance to accelerate debugging and regression
* **System hotspot auditing**: `Class.forName` / `ClassLoader.loadClass` / `Settings.Secure.getString` /
  `System.loadLibrary`, etc. can be intercepted and logged

---

## 2. Scenarios & Environment

* **Environment**: Android 9+ (API 28+); works with Kotlin/Java projects
* **Scenarios**: feature co-debugging, gray-box testing, automated acceptance, critical-path tracing & audit, crash triage
* **No dependency on** Xposed / Magisk / Root

---

## 3. Quick Start

### 3.1 Add JitPack repository

Add to **`settings.gradle`** or the root **`build.gradle`**:

```groovy
dependencyResolutionManagement {
  repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
  repositories {
    mavenCentral()
    maven { url 'https://jitpack.io' }
  }
}
```

> Kotlin DSL: `maven(url = "https://jitpack.io")`

### 3.2 Add dependency

In your **app module**:

```groovy
dependencies {
  implementation "com.github.Rift0911:fhook:+"
}
```

### 3.3 Initialize (auto / manual)

**Option A: Auto init in `attachBaseContext`**

```java
@Override
protected void attachBaseContext(Context base) {
    Log.d(TAG, "attachBaseContext");
    if (FCFG.IS_APP_INIT_AUTO) {
        Log.i(TAG, "attachBaseContext FHook.init= " + FHook.init(base));
    }
    super.attachBaseContext(base);
}
```

**Option B: Manual init anywhere (e.g., button click)**

```java
bt_main_02.setOnClickListener(v -> {
    if (FHook.isInited()) {
        FHook.unInit();
    } else {
        if (!FHook.init(this)) {
            Toast.makeText(this, "Init failed", Toast.LENGTH_LONG).show();
            Log.e(TAG, "Init failed");
        } else {
            Toast.makeText(this, "Init success", Toast.LENGTH_LONG).show();
            Log.i(TAG, "Init success");
        }
    }
});
```

> Handy calls: `FHook.unHookAll()` to remove all hooks; `FHook.showHookInfo()` to view current hook status.

### 3.4 Minimal runnable samples

#### A) Hook a regular app method

Take `THook.fun_I_III(int a, int b, int c): int` as an example — **modify args and return**:

```java
import java.lang.reflect.Method;
import android.util.Log;

Method m = THook.class.getMethod("fun_I_III", int.class, int.class, int.class);

FHook.hook(m)
    .setOrigFunRun(true) // run the original method first
    .setHookEnter((thiz, args, types, hh) -> {
        // change the first argument
        args.set(0, 6666);
        Log.d("FHook", "fun_I_III enter: " + args);
    })
    .setHookExit((ret, type, hh) -> {
        // force the return value
        Log.d("FHook", "fun_I_III exit, origRet=" + ret);
        return 8888;
    })
    .commit();
```

#### B) Hook a system method (device fingerprint sample)

Take `Settings.Secure.getString(ContentResolver, String)` — **forge ANDROID\_ID** selectively:

```java
import android.provider.Settings;
import android.content.ContentResolver;
import java.lang.reflect.Method;
import android.util.Log;

Method sysGet = Settings.Secure.class.getMethod(
        "getString", ContentResolver.class, String.class);

FHook.hook(sysGet)
    .setOrigFunRun(true)
    .setHookEnter((thiz, args, types, hh) -> {
        String key = (String) args.get(1);
        hh.extras.put("key", key);
        Log.d("FHook", "Settings.Secure.getString key=" + key);
    })
    .setHookExit((ret, type, hh) -> {
        String key = (String) hh.extras.get("key");
        if ("android_id".equalsIgnoreCase(key)) {
            return "a1b2c3d4e5f6a7b8"; // affect ANDROID_ID only
        }
        return ret; // keep others intact
    })
    .commit();
```

> Tip: for interface/bridge methods (e.g., `SharedPreferences.Editor.commit`), use
> `FHookTool.findMethod4Impl(editor, ifaceMethod)` to locate the **actual implementation method** before hooking for a higher success rate.

---

### 3.5 Constructor Hook Samples (System & Custom)

> Notes: By definition, a **constructor always runs**; `setOrigFunRun(true/false)` **has