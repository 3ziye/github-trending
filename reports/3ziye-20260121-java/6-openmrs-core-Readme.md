<img src="https://talk.openmrs.org/uploads/default/original/2X/f/f1ec579b0398cb04c80a54c56da219b2440fe249.jpg" alt="OpenMRS"/>

[![Build Status](https://travis-ci.org/openmrs/openmrs-core.svg?branch=master)](https://travis-ci.org/openmrs/openmrs-core) [![Coverage Status](https://coveralls.io/repos/github/openmrs/openmrs-core/badge.svg?branch=master)](https://coveralls.io/github/openmrs/openmrs-core?branch=master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/a51303ee46c34775a7c31c8d6016da6b)](https://www.codacy.com/app/openmrs/openmrs-core?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=openmrs/openmrs-core&amp;utm_campaign=Badge_Grade)

api: [![API](https://snyk.io/test/github/openmrs/openmrs-core/badge.svg?targetFile=api%2Fpom.xml)](https://snyk.io/test/github/openmrs/openmrs-core?targetFile=api%2Fpom.xml)
test: [![test](https://snyk.io/test/github/openmrs/openmrs-core/badge.svg?targetFile=test%2Fpom.xml)](https://snyk.io/test/github/openmrs/openmrs-core?targetFile=test%2Fpom.xml)
tools: [![tools](https://snyk.io/test/github/openmrs/openmrs-core/badge.svg?targetFile=tools%2Fpom.xml)](https://snyk.io/test/github/openmrs/openmrs-core?targetFile=tools%2Fpom.xml)
web: [![web](https://snyk.io/test/github/openmrs/openmrs-core/badge.svg?targetFile=web%2Fpom.xml)](https://snyk.io/test/github/openmrs/openmrs-core?targetFile=web%2Fpom.xml)
webapp: [![webapp](https://snyk.io/test/github/openmrs/openmrs-core/badge.svg?targetFile=webapp%2Fpom.xml)](https://snyk.io/test/github/openmrs/openmrs-core?targetFile=webapp%2Fpom.xml)
DPGA: [![DPG Badge](https://img.shields.io/badge/Verified-DPG-3333AB?logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iMzEiIGhlaWdodD0iMzMiIHZpZXdCb3g9IjAgMCAzMSAzMyIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjIwMDggMjEuMzY3OEwxMC4xNzM2IDE4LjAxMjRMMTEuNTIxOSAxNi40MDAzTDEzLjk5MjggMTguNDU5TDE5LjYyNjkgMTIuMjExMUwyMS4xOTA5IDEzLjYxNkwxNC4yMDA4IDIxLjM2NzhaTTI0LjYyNDEgOS4zNTEyN0wyNC44MDcxIDMuMDcyOTdMMTguODgxIDUuMTg2NjJMMTUuMzMxNCAtMi4zMzA4MmUtMDVMMTEuNzgyMSA1LjE4NjYyTDUuODU2MDEgMy4wNzI5N0w2LjAzOTA2IDkuMzUxMjdMMCAxMS4xMTc3TDMuODQ1MjEgMTYuMDg5NUwwIDIxLjA2MTJMNi4wMzkwNiAyMi44Mjc3TDUuODU2MDEgMjkuMTA2TDExLjc4MjEgMjYuOTkyM0wxNS4zMzE0IDMyLjE3OUwxOC44ODEgMjYuOTkyM0wyNC44MDcxIDI5LjEwNkwyNC42MjQxIDIyLjgyNzdMMzAuNjYzMSAyMS4wNjEyTDI2LjgxNzYgMTYuMDg5NUwzMC42NjMxIDExLjExNzdMMjQuNjI0MSA5LjM1MTI3WiIgZmlsbD0id2hpdGUiLz4KPC9zdmc+Cg==)](https://digitalpublicgoods.net/r/openmrs)

OpenMRS is a patient-based medical record system focusing on giving providers a free customizable electronic medical record system (EMR).

The mission of OpenMRS is to improve health care delivery in resource-constrained environments by coordinating a global community that creates a robust, scalable, user-driven, open source medical record system platform.

#### Table of Contents

1. [Build](#build)
   1. [Prerequisites](#prerequisites)
   2. [Build Command](#build-command)
   3. [Deploy](#deploy)
2. [Docker build](#docker-build)
3. [Navigating the repository](#navigating-the-repository)
4. [Software Development Kit](#software-development-kit)
5. [Extending OpenMRS with Modules](#extending-openmrs-with-modules)
6. [Documentation](#documentation)
   1. [Developer guides](#developer-guides)
   2. [Wiki](#wiki)
   3. [Website](#website)
7. [Contributing](#contributing)
   1. [Code](#code)
   2. [Code Reviews](#code-reviews)
   3. [Translation](#translation)
8. [Issues](#issues)
9. [Community](#community)
10. [Support](#support)
11. [License](#license)

## Build

### Prerequisites

#### Java

OpenMRS is a Java application which is why you need to install a Java JDK.

If you want to build the master branch you will need a Java JDK of minimum version 8.

#### Maven

Install the build tool [Maven](https://maven.apache.org/).

You need to ensure that Maven uses the Java JDK needed for the branch you want to build.

To do so execute

```bash
mvn -version
```

which will tell you what version Maven is using. Refer to the [Maven docs](https://maven.apache.org/configure.html) if you need to configure Maven.

#### Git

Install the version control tool [git](https://git-scm.com/) and clone this repository with

```bash
git clone https://github.com/openmrs/openmrs-core.git
```

### Build Command

After you have taken care of the [Prerequisites](#prerequisites)

Execute the following

```bash
cd openmrs-core
mvn clean package
```

This will generate the OpenMRS application in `webapp/target/openmrs.war` which you will have to deploy into an application server like for example [tomcat](https://tomcat.apache.org/) or [jetty](http://www.eclipse.org/jetty/).

### Deploy

For development purposes you can simply deploy the `openmrs.war` into the application server jetty via

```bash
cd openmrs-core/webapp
mvn jetty:run
```

To run Jetty on a custom port, use the `jetty.http.port` property:

```bash
mvn -Djetty.http.port=8081 jetty:run
```

To run on Cargo, use the `cargo:run` command:

```bash
mvn cargo:r