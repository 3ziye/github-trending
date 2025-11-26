# Pollianna
Pollianna is a Java library and Java command line agent
that accumulates JVM metrics over user-determined polling intervals and exposes them via JMX,
so that they can be consumed by both Java and non-Java telemetry data sinks.

Pollianna also has an API which exposes the same JVM metrics through method calls.
Additionally, it allows specifying an OpenTelemetry compatible endpoint to publish metrics to.

The offered metrics are intended to facilitate Java service deployment configuration and operation
and to support best-practice continuous monitoring.

* [List of Metrics](docs/metrics-list.md)
* [Specific Garbage Collector Considerations](docs/gc-specifics.md)

## Metrics Delivery

There are three distinct but not mutually exclusive ways to use Pollianna.
1. Register JMX beans that serve JVM metrics data via bean attributes.
   You can then apply a JMX scraper such as Prometheus to transport metrics from these JXM Beans.
2. Configure an OpenTelemetry endpoint.
   Pollianna will then directly send your selected metrics there.
3. Retrieve JVM metric data by local API calls. 
   No JMX involved. 
   How you further disseminate the metric data is then up to you.

### 1. Starting JMX Beans

All Pollianna JMX beans must be instated in one of these three ways:
- by a call to a Java method, typically very early in the `main()` program,
- by adding Pollianna as a Java command line agent to a JVM command line,
- by attaching Pollianna as a Java agent to a running JVM.

#### Starting JMX Beans by a Static Method Call
Pollianna can be started by:
```java
Pollianna.start();
```
Without any arguments, this call installs and starts the "Jvm" bean,
so is equivalent:
```java
Pollianna.start("Jvm");
```

If arguments are given, they configure, install, and start
one or several of Pollianna's JVM observation beans.
All arguments must be of type `String` and they are evaluated left-to-right.

If an argument begins with the keyword `file` followed by a colon (':'),
then it specifies a file path and all arguments in that file,
separated by semicolons (';'), are evaluated.
Examples:
```java
Pollianna.start("file:relative-path/pollianna-arguments.txt");
```
```java
Pollianna.start("file:/absolute-path/pollianna-arguments.txt");
```

If an argument begins with the keyword `interval` followed by a colon (':'),
then the rest of the argument specifies the interval time in seconds
to be used for periodic sampling (of RT and NMT metrics). The default is 10.
Example:
```java
Pollianna.start("interval:5");
```

Otherwise, an argument specifies a bean name.
If that name is followed by a pipe character ('|'),
then only the bean attributes listed after the colon will be exposed to JMX.
If an attribute has a non-primitive return type then its name has
the base name of a getter method in that type as a suffix.
Example: if the bean named before the colon has an attribute "Pause"
stemming from its getter method `getPause()`,
and the return type of `getPause()` has a getter method 'getMax()',
then the complete attribute name is "PauseMax".
Example bean argument with select attributes:
```java
"GcAggregate|PauseMax,CycleAvg,AllocationRateMax"
```
If the same bean name is specified multiple times, only the right-most argument applies.

The available beans are: `Jvm`, `RtAggregate`, `RtSample`, `GcAggregate`, `GcSample`, `CompilerAggregate`, and `CompilerSample`.
If the JDK in use supports NMT data discovery by a dedicated JMX bean (see below),
then these additional beans are available: `NmtAggregate` and `NmtSample`.

Example with multiple arguments:
```java
Pollianna.start("interval:20", "RtSample", "GcAggregate|PauseMax,CycleAvg,AllocationRateMax", "file:morePolliannaArguments.txt");
```

#### Pollianna as Java Command Line Agent
Adding this to your JVM command line invokes Pollianna without touching your application's source code.
```bash
-javaagent:pollianna-1.16.1.jar
```
You can provide the same arguments as for a Pollianna invokation by method call,
except that they have to be combined into one single string in which they are separated by semicolons.
Full example:
```shell
java -Xms4G -Xmx4G \
     -javaagent:pollianna-1.16.1.jar="interval:20;NmtSample;GcAggregate|PauseMax,CycleAvg,AllocationRateMax;file:morePolliannaArguments.txt" \
     MyApplication
```
This sets the sampling interval for NMT data to every 20 seconds, 
starts the `NmtSample` bean, starts the `GcAggregate` bean with a few select attributes,
and then reads and applies additional arguments from local file `"morePolliannaArguments.txt"`.

#### Attaching the Pollianna Agent to a Running JVM

Instead of specifying the agent on the command line,
operators can also dynamically attach it to a running Java program.
This leaves the original deployment code intact,
but requires additional code for the agent's deployment,
its activation, and local service PID discovery.

#### Enabling NMT Data
Pollianna beans for Native Memory Tracking (NMT) data will only function if:
1. 