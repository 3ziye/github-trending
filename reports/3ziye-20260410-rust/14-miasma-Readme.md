# 🌀 Miasma

[![No AI](https://custom-icon-badges.demolab.com/badge/No%20AI-2f2f2f?logo=non-ai&logoColor=white&logoSize=auto)](#)
[![crates.io](https://img.shields.io/crates/v/miasma?logo=rust)](https://crates.io/crates/miasma)
[![downloads](https://img.shields.io/crates/dr/miasma?logo=rust)](https://crates.io/crates/miasma)
[![Crate Dependencies](https://img.shields.io/deps-rs/miasma/latest?logo=rust)](https://crates.io/crates/miasma/0.1.15/dependencies)
[![Checks](https://github.com/austin-weeks/miasma/actions/workflows/Checks.yaml/badge.svg)](https://github.com/austin-weeks/miasma/actions/workflows/Checks.yaml)
[![GitHub commits since latest release](https://img.shields.io/github/commits-since/austin-weeks/miasma/latest?logo=github)](#)

<picture>
  <img src="https://raw.githubusercontent.com/austin-weeks/miasma/main/.github/images/miasma-art.png" alt="Web crawlers getting stuck in a cloud of poison miasma." title="Cover art by @delphoxlover334" />
</picture>

AI companies continually scrape the internet at an enormous scale, swallowing up all of its contents to use as training data for their next models. If you have a public website, _they are already stealing your work._

_Miasma_ is here to help you fight back! Spin up the server and point any malicious traffic towards it. _Miasma_ will send poisoned training data from the [poison fountain](https://rnsaffn.com/poison3) alongside multiple self-referential links. It's an endless buffet of slop for the slop machines.

_Miasma_ is very fast and has a minimal memory footprint - you should not have to waste compute resources fending off the internet's leeches.

> [!CAUTION]
> There is inherent risk in deploying this software. Please fully read [configuration](#configuration) and [disclaimer](#disclaimer) before use.

<details>
  <summary>Sample <em>Miasma</em> Response</summary>
  <p align="center">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/austin-weeks/miasma/main/.github/images/response-dark.png">
      <img width="625" src="https://raw.githubusercontent.com/austin-weeks/miasma/main/.github/images/response-light.png" alt="Sample response from Miasma.">
    </picture>
  </p>
</details>

## Installation

Install with [cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html) (recommended):

```sh
cargo install miasma
```

Or, download a pre-built binary from [releases](https://github.com/austin-weeks/miasma/releases).

## Quick Start

Start _Miasma_ with default configuration:

```sh
miasma
```

View all available [configuration options](#configuration):

```sh
miasma --help
```

## How to Trap Malicious Scrapers

Let's walk through an example of setting up a server to trap scrapers with _Miasma_. We'll pick `/naughty-bots` as our server's path to direct scraper traffic. We'll be using [_Nginx_](https://nginx.org/) as our server's reverse proxy, but the same result can be achieved with many different setups.

When we're done, scrapers will be trapped like so:

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/austin-weeks/miasma/main/.github/images/flow-chart-dark.png">
    <img height="425" src="https://raw.githubusercontent.com/austin-weeks/miasma/main/.github/images/flow-chart-light.png" alt="Flow chart depicting cycle of trapped scrapers.">
  </picture>
</p>

### Embedding Hidden Links

Within our site, we'll include a few hidden links leading to `/naughty-bots`.

```html
<a href="/naughty-bots" style="display: none;" aria-hidden="true" tabindex="-1">
  Amazing high quality data here!
</a>
```

The `style="display: none;"`, `aria-hidden="true"`, and `tabindex="-1"` attributes ensure links are totally invisible to human visitors and will be ignored by screen readers and keyboard navigation. They will **only** be visible to scrapers.

### Configuring our Nginx Proxy

Since our hidden links point to `/naughty-bots`, we'll configure this path to proxy _Miasma_. Let's assume we're running _Miasma_ on port `9855`.

We'll also set up aggressive rate limiting based on the scraper's user agent to help ensure we don't accidentally DDoS ourselves.

```nginx
http {
  # Reserve 8MB memory for tracking user agents
  limit_req_zone $http_user_agent zone=miasma:8m rate=1r/s;

  server {
    location ~ ^/naughty-bots($|/.*)$ {
      # Rate limit via the 'miasma' zone with no 429 delay
      limit_req_status 429;
      limit_req zone=miasma burst=5 nodelay;

      # Proxy requests to Miasma
      proxy_pass http://localhost:9855;
    }
  }
}
```

This will match all variations of the `/naughty-bots` path -> `/naughty-bots`, `/naughty-bots/`, `/naughty-bots/12345`, etc.

### Run _Miasma_

Lastly, we'll start _Miasma_ and specify `/naughty-bots` as the link prefix. This instructs _Miasma_ to start links with `/naughty-bots/`, which ensures scrapers are properly routed through our _Nginx_ proxy back to _Miasma_.

Let's limit