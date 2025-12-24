= Chronicle Queue
Peter Lawrey, Rob Austin
:css-signature: demo
:toc: macro
:toclevels: 2
:icons: font
:source-highlighter: rouge

Chronicle Queue is a broker-less, off-heap Java library for ultra-low-latency, persisted messaging at millions of events/sec.

image:https://maven-badges.herokuapp.com/maven-central/net.openhft/chronicle-queue/badge.svg[caption="",link=https://maven-badges.herokuapp.com/maven-central/net.openhft/chronicle-queue]
image:https://javadoc.io/badge2/net.openhft/chronicle-queue/javadoc.svg[link="https://www.javadoc.io/doc/net.openhft/chronicle-queue/latest/index.html"]
image:https://img.shields.io/github/license/OpenHFT/Chronicle-Queue[GitHub]
image:https://img.shields.io/gitter/room/OpenHFT/Lobby.svg?style=popout[link="https://gitter.im/OpenHFT/Lobby"]
image:https://img.shields.io/badge/release%20notes-subscribe-brightgreen[link="https://chronicle.software/release-notes/"]
image:https://sonarcloud.io/api/project_badges/measure?project=OpenHFT_Chronicle-Queue&metric=alert_status[link="https://sonarcloud.io/dashboard?id=OpenHFT_Chronicle-Queue"]

image::docs/images/Queue_line.png[width=20%]

toc::[]

== Overview

Chronicle Queue is a persisted low-latency messaging framework for high performance applications.
It supports multiple writers to a queue via locking, and multiple lock-less concurrent readers of the queue.

This project covers the Java version of Chronicle Queue.
A {cpp} version of this project is also available and supports Java/{cpp} interoperability plus additional language bindings e.g. Python.
If you are interested in evaluating the {cpp} version please contact mailto:sales@chronicle.software[sales@chronicle.software].

At first glance Chronicle Queue can be seen as simply *another queue implementation*.
However, it has major design choices that should be emphasised.
Using _off-heap storage_, Chronicle Queue provides an environment where applications do not suffer from Garbage Collection (GC).
When implementing high-performance and memory-intensive applications (you heard the fancy term "bigdata"?) in Java, one of the biggest problems is garbage collection.

Chronicle Queue allows messages to be added to the end of a queue ("appended"), read from the queue ("tailed"),
and also supports random-access seek.

link:https://player.vimeo.com/video/201989439[Why Use Chronicle Queue Between Microservices?]

A number of relevant system properties are listed in link:docs/systemProperties.adoc[systemProperties.adoc].

== What Is Chronicle Queue?

You could consider a Chronicle Queue to be similar to a low latency broker-less durable/persisted topic that can contain messages of different types and sizes.
Chronicle Queue is a distributed unbounded persisted queue that:

* supports asynchronous RMI and Publish/Subscribe interfaces with microsecond latencies.
* passes messages between JVMs in under a microsecond
* passes messages between JVMs on different machines via replication in under 10 microseconds
(<<Chronicle Queue Enterprise Edition,Enterprise feature>>)
* provides stable, soft real-time latencies into the millions of messages per second for a single thread to one queue; with total ordering of every event.

When publishing 40-byte messages, a high percentage of the time we achieve latencies under 1 microsecond.
The 99th percentile latency is the worst 1 in 100, and the 99.9th percentile is the worst 1 in 1000 latency.

.Latency to send/receive on the same machine.
[width="60%",options="header"]
|=======
| Batch Size | 10 million events per minute | 60 million events per minute | 100 million events per minute
| 99%ile | 0.78 &micro;s | 0.78 &micro;s | 1.2 &micro;s
| 99.9%ile | 1.2 &micro;s | 1.3 &micro;s | 1.5 &micro;s
|=======

.Latency to send/receive on a second machine.
[width="60%",options="header"]
|=======
| Batch Size | 10 million events per minute | 60 million events per minute | 100 million events per minute
| 99%ile | 20 &micro;s | 28 &micro;s | 176 &micro;s
| 99.9%ile | 901 &micro;s | 705 &micro;s | 5,370 &micro;s
|=======

NOTE: 100 million events per minute is sending an event every 660 nanoseconds; replicated and persisted.

IMPORTANT: This performance is not achieved using a _large cluster of machines_.
This is using one thread to publish, and one thread to consume.

=== Design Motivation and Features

Chronicle Queue is designed to:

* be a "record everything store" which can read with microsecond real-time latency.
This supports even the most demanding High Frequency Trading systems.
However, it can be used in any application where the recording of information is a concern.

* support reliable replication with notification to either the appender (writer of message) or a tailer (reader of message), when a message has been successfully replicated.

==== Persistence

Chronicle Queue assumes disk space is cheap compared with memory.
Chronicle Queue makes full use of the disk space you have, and so you are not limited by the main memory of your machine.
If you use s