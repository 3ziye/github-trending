# Hytale Server Plugin API Documentation

This project is auto-generated from the decompiled source code and shared as a reference only, to allow reading of public methods. It is not intended for build purposes. 
<br>

For more details you can visit our discord channel:  https://www.akatron.net/hytale-discord


## AI Integration

If you intend to use this project as a reference for writing code with artificial intelligence, you can download it and specify the file location com/hypixel/hytale in your prompts so that the agent can receive information about the project.


## Languages
[Türkçe (Turkish)](README_TR.md)

## Core API Documentation
- [English](HYTALE_CORE_API.md)
- [Türkçe](HYTALE_CORE_API_TR.md)


## AssetEditor
- **Version**: 1.0.0
- **Main Class**: `com.hypixel.hytale.builtin.asseteditor.AssetEditorPlugin`

_No public methods found or file parse error._

---

## BlockSpawner
- **Version**: 1.0.0
- **Main Class**: `com.hypixel.hytale.builtin.blockspawner.BlockSpawnerPlugin`

### Public Methods
```java
public static BlockSpawnerPlugin get();
public Query<ChunkStore> getQuery();
public void onEntityAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer);
public void onEntityRemove(@Nonnull Ref<ChunkStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer);
public void onEntityAdd(@Nonnull Holder<ChunkStore> holder, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store);
public void onEntityRemoved(@Nonnull Holder<ChunkStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store);
public Query<ChunkStore> getQuery();
```

---

## BlockTick
- **Version**: 1.0.0
- **Main Class**: `com.hypixel.hytale.builtin.blocktick.BlockTickPlugin`

### Public Methods
```java
public static BlockTickPlugin get();
public TickProcedure getTickProcedure(int blockId);
public int discoverTickingBlocks(@Nonnull Holder<ChunkStore> holder, @Nonnull WorldChunk chunk);
```

---

## BlockPhysics
- **Version**: 1.0.0
- **Main Class**: `com.hypixel.hytale.builtin.blockphysics.BlockPhysicsPlugin`

### Public Methods
```java
public static void validatePrefabs(@Nonnull LoadAssetEvent event);
```

---

## BuilderTools
- **Version**: 1.0.0
- **Main Class**: `com.hypixel.hytale.builtin.buildertools.BuilderToolsPlugin`

_No public methods found or file parse error._

---

## Crafting
- **Version**: 1.0.0
- **Main Class**: `com.hypixel.hytale.builtin.crafting.CraftingPlugin`

### Description
Manages the crafting system, including recipes, crafting benches (stations), and player unlocked recipes.
It handles checking if a player has the required materials and if a specific recipe is valid for a given bench.

### Public Methods
```java
// Returns the singleton instance
public static CraftingPlugin get();

// Gets all available recipe IDs for a specific bench ID and category.
public static Set<String> getAvailableRecipesForCategory(String benchId, String benchCategoryId);

// Checks if an item stack can be used as a material in the current state of a bench.
public static boolean isValidCraftingMaterialForBench(BenchState benchState, ItemStack itemStack);

// Checks if an item is valid for upgrading a bench.
public static boolean isValidUpgradeMaterialForBench(BenchState benchState, ItemStack itemStack);

// Gets a list of all recipes available for a given Bench block.
public static List<CraftingRecipe> getBenchRecipes(@Nonnull Bench bench);

// Gets recipes for a bench type (e.g. Crafting, Diagram, Structural) and name.
public static List<CraftingRecipe> getBenchRecipes(BenchType benchType, String name);

// Unlocks a recipe for a player ("learns" it). Returns true if it was newly learned.
// Requires the specific player Entity Reference.
public static boolean learnRecipe(@Nonnull Ref<EntityStore> ref, @Nonnull String recipeId, @Nonnull ComponentAccessor<EntityStore> componentAccessor);

// Locks a recipe for a player ("forgets" it).
public static boolean forgetRecipe(@Nonnull Ref<EntityStore> ref, @Nonnull String itemId, @Nonnull ComponentAccessor<EntityStore> componentAccessor);

// Sends a packet to the client syncing their list of known recipes.
public static void sendKnownRecipes(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor);
```

---

## CommandMacro
- **Version**: 1.0.0
- **Main Class**: `com.hypixel.hytale.builtin.commandmacro.MacroCommandPlugin`

### Public Methods
```java
public static MacroCommandPlugin get();
public void loadCommandMacroAsset(@Nonnull LoadedAssetsEvent<String, MacroCommandBuilder, DefaultAssetMap<String, MacroCommandBuilder>> event);
```

---

## Instances
- **Version**: 1.0.0
- **Main Class**: `com.hypixel.hytale.builtin.instances.InstancesPlugin`

_No public methods found or file parse error._

---

## LANDiscovery
- **Version**: 1.0.0
- **Main Class**: `com.hypixel.hytale.builtin.landisco