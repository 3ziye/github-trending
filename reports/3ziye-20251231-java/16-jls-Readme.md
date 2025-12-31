# JLS (Java Language Server) using the [Java compiler API](https://docs.oracle.com/javase/10/docs/api/jdk.compiler-summary.html)

This server is based on the original implementation at `https://github.com/georgewfraser/java-language-server`,
with updated functionality and ongoing improvements.

A Java language server based on v3.0 of the protocol and implemented using the Java compiler API.

## Enhancements in this fork

This fork keeps the original behavior while adding practical improvements for day-to-day work:

- Lombok support (annotation processing + `-javaagent` wiring).
- Faster startup and navigation with workspace caches.
- Persistent workspace index cache to speed up restarts.
- Parallel indexing for large projects.
- Smarter compile scoping to reduce work on main vs. test sources.
- Completion prioritizes already-imported types.
- Optional timing/debug logs via `~/.config/jls/logging.properties`.
- Unused import warnings in diagnostics.


## IMPORTANT
I may often introduce **breaking changes** until i'm satisfied with a stable version so prepare your horses for a wild ride


## First-run checklist

- Install a compatible JDK and verify `java -version`.
- (Optional) create `~/.config/jls/runtimes.json` for per-project runtime selection.
- (Optional) add `~/.config/jls/logging.properties` for timing logs.
- Build or download release artifacts so `dist/` exists.

## Installation (other editors)

JLS does not bundle a runtime. Install a compatible JDK and either add it to PATH, set `JAVA_HOME`, or configure `~/.config/jls/runtimes.json`.

### Neovim (with nvim-lspconfig)

See `docs/lazyvim-java-lsp.md` for a complete LazyVim example. For a minimal `nvim-lspconfig` setup:
Ensure a compatible JDK is installed and available on PATH (or set `JAVA_HOME`).

```lua
local lspconfig = require("lspconfig")
local configs = require("lspconfig.configs")

if not configs.jls then
  configs.jls = {
    default_config = {
      cmd = {
        "/path/to/jls/dist/lang_server_{linux|mac|windows}.sh",
        "-Dorg.javacs.lombokPath=/path/to/lombok.jar",
      },
      filetypes = { "java" },
      root_dir = lspconfig.util.root_pattern("pom.xml", "build.gradle", "build.gradle.kts", ".java-version", ".git"),
      settings = {
        java = {
          classPath = {
            "lib/some-dependency.jar",
          },
          docPath = {
            "lib/some-dependency-sources.jar",
          },
          externalDependencies = {
            "junit:junit:jar:4.12:test",
            "junit:junit:4.12",
          },
          mavenSettings = "/Users/you/.m2/settings.xml",
        },
      },
    },
  }
end

lspconfig.jls.setup({})
```

### Linux (env-based Lombok)
For including lombok support execute
```sh
export LOMBOK_PATH=/path/to/lombok.jar
```
before using language server

## [Issues](https://github.com/idelice/jls/issues)

## Usage

The language server will provide autocomplete and other features using:
* .java files anywhere in your workspace
* Java platform classes
* External dependencies specified using `pom.xml` or [settings](#Settings)

## Settings

If the language server doesn't detect your external dependencies automatically, you can specify them in your LSP client settings (the JSON examples map directly to `settings.java.*` in most clients):

```json
{
    "java.externalDependencies": [
        "junit:junit:jar:4.12:test", // Maven format
        "junit:junit:4.12" // Gradle-style format is also allowed
    ]
}
```

If all else fails, you can specify the Java class path and the locations of
source jars manually:

```json
{
    "java.classPath": [
        "lib/some-dependency.jar"
    ],
    "java.docPath": [
        "lib/some-dependency-sources.jar"
    ]
}
```

If your project needs a private Maven repository, make sure the language server
uses the same `settings.xml` that contains your credentials:

```json
{
    "java.mavenSettings": "/Users/you/.m2/settings.xml"
}
```

That file is passed to `mvn -s …` when Maven runs dependency goals, so private
artifacts can be resolved just like they are in `jdtls`.

You can generate a list of external dependencies using your build tool:
* Maven: `mvn dependency:list`
* Gradle: `gradle dependencies`

The Java language server will look for the dependencies you specify in `java.externalDependencies` in your Maven and Gradle caches `~/.m2` and `~/.gradle`. You should use your build tool to download the library *and* source jars of all your dependencies so that the Java language server can find them:
* Maven
  * `mvn dependency:resolve` for compilation and autocomplete
  * `mvn dependency:resolve -Dclassifier=sources` for inline Javadoc help
* Gradle
  * `gradle dependencies` for compilation and autocomplete
  * Include `classifier: sources` in your build.gradle for inline Javadoc help, for example:
    ```
    dependencies {
        testCompile group: 'junit', name: 'junit', version: '4.+'
        testCompile group: 'junit', name: 'junit', version: '4.+', classifie