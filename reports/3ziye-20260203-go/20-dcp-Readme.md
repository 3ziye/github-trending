# Developer Control Plane

This repository contains the Developer Control Plane tool (or DCP for short). DCP is implemented as a single binary (`dcp`) that can run in one of several modes depending on how it is invoked. The main modes of operation are:
- `dcp start-apiserver` - runs the DCP API server that holds the workload model and exposes a Kubernetes-compatible API for managing workloads using the [Tilt API server library](https://github.com/tilt-dev/tilt-apiserver). The API server is Kubernetes-compatible but using custom resource definitions. This is the main entry point for DCP; users or other tools such as Aspire invoke DCP in this mode to launch the API server and controllers.
- `dcp run-controllers` - runs the core DCP controllers that implement the standard behavior for DCP workload models. This mode is typically invoked as a child process of the API server.
- `dcp monitor-process` - monitors a given process and ensures that it's cleaned up properly when a DCP session ends. This mode is typically invoked as a child process of the controllers.
- `dcp monitor-container` - monitors a given container and ensures that it's cleaned up properly when a DCP session ends. This mode is typically invoked as a child process of the controllers.
- `dcp stop-process-tree` - stops a given process and all its child processes. Attempts to gracefully terminate the process tree first via signals and then forcibly terminates it if the graceful termination does not complete within a timeout.
- `dcp version` - displays version information about the DCP installation.
- `dcp info` - displays information about the current DCP installation and identified container runtime.

### Environment variables affecting DCP behavior

DCP has knowledge of a number of environment variables that can change its behavior; they are used mostly for testing.

| Variable | Description |
| --- | --------- |
| `DCP_BIN_PATH` and `DCP_EXTENSIONS_PATH` | These variables point to, respectively, the DCP root binary/configuration directory, and the DCP extensions directory. DCP root directory contains the main DCP CLI/API server binary and the default access configuration (kubeconfig) file. The extensions directory contains the DCP controller process binary and other extensions, if present. <br/> By default, DCP assumes the root directory to be `${HOME}/.dcp`. .NET Aspire tooling is using these environment variables to instruct DCP to use locations and binaries inside Aspire.Hosting.Orchestration workload instead. |
| `DEBUG_SESSION_PORT`, `DEBUG_SESSION_TOKEN`, and `DEBUG_SESSION_SERVER_CERTIFICATE` | These are variables that configure the endpoint for running Executables via a developer IDE/under debugger. For more information see [IDE execution specification](https://github.com/dotnet/aspire/blob/main/docs/specs/IDE-execution.md). |
| `DCP_SESSION_FOLDER` | This variable is used for isolating multiple DCP instances running concurrently on the same machine. If set (to a valid filesystem folder), DCP process(es) will create files related to their execution in this folder: the access configuration file (kubeconfig), captured Executable/Container logs, etc. |
| `DCP_LOG_SOCKET` | If set to a Unix domain socket, DCP will write its execution logs to that socket instead of writing them to standard error stream (`stderr`). This allows programs that launch DCP to capture its output even if DCP is running in `--detach` mode. <br/> The `--detach` mode causes DCP to fork itself and break the parent-child relationship (and lifetime dependency) from the process that launched it, but the side effect of doing so is that the parent process loses ability to monitor DCP standard output and standard error streamd. |
| `DCP_LOG_SESSION_ID` | If set, DCP will prepend this value to all diagnostics log names. If unset, a session ID will be calculated. The value is propagated to all child DCP processes. |
| `DCP_DIAGNOSTICS_LOG_LEVEL` | If set, enabled DCP diagnostic logging. <br/> Can be set to `error`, `info`, or `debug`; for troubleshooting `debug` is recommended, although it results in the most verbose output. |
| `DCP_DIAGNOSTICS_LOG_FOLDER` | If set to a valid filesystem folder, DCP will place the diagnostic logging files there. Otherwise (if enabled) they are written to the default temporary files folder. |
| `DCP_LOG_FILE_NAME_SUFFIX` | Suffix to append to the log file name (defaults to process ID if not set). |
| `DCP_LOGGING_CONTEXT` | If set, the value of this variable will be written to the log file as one of the first log messages (as verbose, "info" type of message). |
| `DCP_PRESERVE_EXECUTABLE_LOGS` | If set (to "true", "yes", or "1"), the logs from Executables will not be deleted when DCP shuts down. This can be useful to capture results of test runs that use DCP as the workload orchestrator. |
| `DCP_RESOURCE_WATCH_TIMEOUT_SECONDS` | A timeout for resource watch requests, in seconds. Watch requests will time out shortly after the specified value, to avo