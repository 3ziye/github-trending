Fix for this issue appeared as CVE-2024-49746: [bulletin](https://source.android.com/docs/security/bulletin/2025-02-01#framework), [patch](https://android.googlesource.com/platform/frameworks/native/+/b3cdb06ab9137a67e4ee212ae6655de383fdaaaa%5E%21/)

# "This seems wrong"

Above title is the comment from [`Parcel::continueWrite` method](https://cs.android.com/android/platform/superproject/main/+/main:frameworks/native/libs/binder/Parcel.cpp;l=3029-3132;drc=f4c9b48c19f1b040efb35932b322f47e7779cafe), which is actually responsible for resizing `Parcel` objects, either when explicitly request by user (for example through [`setDataSize()`](https://developer.android.com/reference/android/os/Parcel#setDataSize(int))) or when calling one of `write` methods when current data capacity is too small

```cpp
status_t Parcel::continueWrite(size_t desired)
{
    // SNIP: Validate desired size
    // SNIP: Assign kernelFields & rpcFields from variant member of this class
    // SNIP: Count number of objects (Binder handles and File Descriptors)
    //       that will be present after resize and assign to objectsSize

    if (mOwner) {
        // If the size is going to zero, just release the owner's data.
        if (desired == 0) {
            freeData();
            return NO_ERROR;
        }

        // If there is a different owner, we need to take
        // posession.
        uint8_t* data = (uint8_t*)malloc(desired);
        // SNIP: Check if malloc succeeded
        binder_size_t* objects = nullptr;

        if (kernelFields && objectsSize) {
            objects = (binder_size_t*)calloc(objectsSize, sizeof(binder_size_t));
            // SNIP: Check if calloc succeeded

            // Little hack to only acquire references on objects
            // we will be keeping.
            size_t oldObjectsSize = kernelFields->mObjectsSize;
            kernelFields->mObjectsSize = objectsSize;
            acquireObjects();
            kernelFields->mObjectsSize = oldObjectsSize;
        }
        // SNIP: rpcFields handling for non-/dev/binder Parcels

        if (mData) {
            memcpy(data, mData, mDataSize < desired ? mDataSize : desired);
        }
        if (objects && kernelFields && kernelFields->mObjects) {
            memcpy(objects, kernelFields->mObjects, objectsSize * sizeof(binder_size_t));
        }
        // ALOGI("Freeing data ref of %p (pid=%d)", this, getpid());
        if (kernelFields) {
            // TODO(b/239222407): This seems wrong. We should only free FDs when
            // they are in a truncated section of the parcel.
            closeFileDescriptors();
        }
        mOwner(mData, mDataSize, kernelFields ? kernelFields->mObjects : nullptr,
               kernelFields ? kernelFields->mObjectsSize : 0);
        mOwner = nullptr;

        // SNIP: Allocation count tracking
        // SNIP: Assign data and objects to this object
    } else if (mData) {
        // SNIP: Resize data owned by this instance of Parcel
    } else {
        // SNIP: Allocate initial data for currently empty Parcel
    }

    return NO_ERROR;
}
```

[When that comment was introduced](https://android.googlesource.com/platform/frameworks/native/+/53b6ffe5af3951e8784c451ef8c4ff19f3d6b196%5E!/), `closeFileDescriptors()` call was moved from `IPCThreadState::freeBuffer()` (which is called in above code through `mOwner()` function pointer) to `continueWrite()` method, however logic was same as before. After all, `Parcel` is core part of Android IPC and if core IPC was closing File Descriptors it shouldn't it'd be obvious problem

Which brings us to important part: when above code is being used? It is used when Parcel class moves ownership of data received from Binder driver (which at that point reside in [`/dev/binder` `mmap`](https://cs.android.com/android/platform/superproject/main/+/main:frameworks/native/libs/binder/ProcessState.cpp;l=587-592;drc=187efe18e3de6258af0230198c881915cc695567) and cannot be written to (any attempts to write that memory would lead to `SIGSEGV`)), that is `Parcel` being either incoming transaction data (`data` argument passed to [`onTransact()`](https://developer.android.com/reference/android/os/Binder#onTransact(int,%20android.os.Parcel,%20android.os.Parcel,%20int))) or incoming reply (that is, `Parcel` object that was passed to [`transact()`](https://developer.android.com/reference/android/os/IBinder#transact(int,%20android.os.Parcel,%20android.os.Parcel,%20int)) call as `reply` argument, `transact()` sets reference within that `Parcel` object)

In practice, only case we'd enter `if (mOwner)` block is when system [calls `setDataSize(0)` to release transaction data](https://cs.android.com/android/platform/superproject/main/+/main:frameworks/native/libs/binder/IPCThreadState.cpp;l=1483-1488;drc=187efe18e3de6258af0230198c881915cc695567), but in that case we'd also enter `if (desired == 0)` which does early return. During legitimate system usage there's no case where we'd enter "If there is a 