Fix for this issue has appeared as CVE-2025-22441: [bulletin](https://source.android.com/docs/security/bulletin/2025-08-01#framework) [patch](https://android.googlesource.com/platform/frameworks/base/+/60335b2eae7311fe6e10e140b64489008a38a5a8%5E%21/) [follow up](https://android.googlesource.com/platform/frameworks/base/+/37bf5823504f2a256f128123393cd149721b87fc%5E%21/#F0)

# Passing `ApplicationInfo` around

[`ApplicationInfo`](https://developer.android.com/reference/android/content/pm/ApplicationInfo) is structure defining various information about installed app, most notably path to apk file from which resources and code are loaded

Usually it is passed from system to applications, however sometimes there are cases where non-system caller could provide own one. For example in the past that was [vulnerability in `bindBackupAgent()` method, where attacker could pass in parameter own `ApplicationInfo` object with `uid` and `sourceDir` values and they weren't checked against what apps are really installed in system](https://seclists.org/fulldisclosure/2015/Apr/52), because that method was meant to be called internally by `system_server`, but was exposed to `adb shell`

This time though, I've looked closely at [`ApplicationInfo` field within `RemoteViews`](https://cs.android.com/android/platform/superproject/main/+/main:frameworks/base/core/java/android/widget/RemoteViews.java;l=356;drc=978f80da915fe0a64d0b6425ce30d5359563b5e9)

`RemoteViews` is object describing view that can come from another process. This most notably is [used for home screen widgets](https://developer.android.com/guide/topics/appwidgets#handle-events), where app providing widget builds `RemoteViews` and then it is ["applied"](https://developer.android.com/reference/android/widget/RemoteViews#apply(android.content.Context,%20android.view.ViewGroup)) within home screen process

Other places where `RemoteViews` are used are [notifications](https://developer.android.com/reference/android/app/Notification.Builder#setCustomBigContentView(android.widget.RemoteViews)) (applied by SystemUI process) and [autofill dialogs](https://developer.android.com/reference/android/service/autofill/Presentations.Builder#setDialogPresentation(android.widget.RemoteViews)) (provided by autofill service, applied by `system_server`)

`RemoteViews.mApplication` field is serialized through `Parcel` and therefore may come from remote processes and whenever `RemoteViews` are applied it is used by following method [(snippet source)](https://cs.android.com/android/platform/superproject/main/+/main:frameworks/base/core/java/android/widget/RemoteViews.java;l=6545-6561;drc=978f80da915fe0a64d0b6425ce30d5359563b5e9):

```java
private Context getContextForResourcesEnsuringCorrectCachedApkPaths(Context context) {
    if (mApplication != null) {
        if (context.getUserId() == UserHandle.getUserId(mApplication.uid)
                && context.getPackageName().equals(mApplication.packageName)) {
            return context;
        }
        try {
            LoadedApk.checkAndUpdateApkPaths(mApplication);
            return context.createApplicationContext(mApplication,
                    Context.CONTEXT_RESTRICTED);
        } catch (NameNotFoundException e) {
            Log.e(LOG_TAG, "Package name " + mApplication.packageName + " not found");
        }
    }

    return context;
}
```

Most interesting here is `LoadedApk.checkAndUpdateApkPaths()` call, as this is static method and will modify some global state [(snippet source)](https://cs.android.com/android/platform/superproject/main/+/main:frameworks/base/core/java/android/app/LoadedApk.java;l=2275-2302;drc=5916ee589c4880e2d8a1a9ad6dc852108e4c44c1)

```java
public static void checkAndUpdateApkPaths(ApplicationInfo expectedAppInfo) {
    // Get the LoadedApk from the cache
    ActivityThread activityThread = ActivityThread.currentActivityThread();
    if (activityThread == null) {
        Log.e(TAG, "Cannot find activity thread");
        return;
    }
    checkAndUpdateApkPaths(activityThread, expectedAppInfo, /* cacheWithCode */ true);
    checkAndUpdateApkPaths(activityThread, expectedAppInfo, /* cacheWithCode */ false);
}

private static void checkAndUpdateApkPaths(ActivityThread activityThread,
        ApplicationInfo expectedAppInfo, boolean cacheWithCode) {
    String expectedCodePath = expectedAppInfo.getCodePath();
    LoadedApk loadedApk = activityThread.peekPackageInfo(
            expectedAppInfo.packageName, /* includeCode= */ cacheWithCode);
    // If there is load apk cached, or if the cache is valid, don't do anything.
    if (loadedApk == null || loadedApk.getApplicationInfo() == null
            || loadedApk.getApplicationInfo().getCodePath().equals(expectedCodePath)) {
        return;
    }
    // Duplicate framework logic
    List<String> oldPaths = new ArrayList<>();
    LoadedApk.makePaths(activityThread, expectedAppInfo, oldPaths);

    // Force update the LoadedApk instance, which should update the r