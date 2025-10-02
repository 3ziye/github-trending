# thermoptic

<!-- ![Rare image of the Major smiling]() -->

<a href="https://www.youtube.com/watch?v=qkXReli7eC0" target="_blank"><img src="_readme/gits.gif" width="100%"></a>

> *"I don't believe it, thermoptic camouflage!"*

## What is it?

This is an HTTP proxy designed to bypass services that use fingerprinting such as [JA4+](https://blog.foxio.io/ja4%2B-network-fingerprinting) to block certain HTTP clients. Using this proxy, you can use your preferred HTTP clients like `curl` and still have [magically](#how-does-that-work-exactly) indistinguishable fingerprints from a real (Chrome/Chromium) web browser. `thermoptic` also comes with some [fun features](#handling-browser-javascript-fingerprinting-with-thermoptic-hooks) to mitigate JavaScript-based fingerprinting. It also makes it easy to do hybrid scraping using both a web browser and low-level HTTP clients together.

Even if you’re unfamiliar with JA4+ fingerprinting, if you’ve done any scraping you’ve probably been blocked by it before. Popular services such as Cloudflare use such techniques (and other tricks) to detect use of "non-human" HTTP clients to block requests. These services can also use this fingerprinting to detect if you start a session with a real browser and then switch to a low-level client like `curl` later. `thermoptic` solves all of these problems by presenting a unified "real" browser fingerprint for all scraping requests.

## Example

Here's an example JA4H (HTTP) fingerprint of `curl` without the proxy:

```
$ curl https://ja4db.com/id/ja4h/
ge11nn090000_b6a016211e8a_000000000000_e3b0c44298fc
```

This is quite different from the fingerprint that Chrome produces when you visit the URL directly:

```
ge11cn19enus_f2808f0d04cf_9a10d4221160_7068f58def6e
```

However, when we use the proxy to make the request, our JA4H fingerprint is magically identical:

```
$ curl --proxy http://username:password@thermoptic:1234 https://ja4db.com/id/ja4h/
ge11cn19enus_f2808f0d04cf_9a10d4221160_7068f58def6e
```

(The same goes for our JA4 TLS fingerprint as well, etc).

## Setup

To start a `thermoptic` proxy which cloaks your traffic through a containerized Chrome instance on Ubuntu 22.04:

```
docker compose up --build
```

That's all, now you can proxy traffic through it:

```
curl --proxy http://changeme:changeme@127.0.0.1:1234 --insecure https://ja4db.com/id/ja4h/
```

Important notes:
* Default proxy username and password are `changeme` please make sure you change them before exposing externally.
* If you don't want to use `---insecure` you need to use the generated CA file located in `./ssl/rootCA.crt`. This is generated the first time you run `thermoptic`.
* You can connect `thermoptic` to any Chrome/Chromium instance launched with the `--remote-debugging-port` flag. This is essential as you'll want to set up and proxy through more commonly used environments to keep your fingerprint as low profile as possible (e.g. Chrome on Windows).

## How does this cloaking work exactly?

![Visual diagram example](_readme/diagram.png)

* An HTTP request is made using an HTTP client such as `curl` with `thermoptic` set as a proxy.
* `thermoptic` analyzes the request to best determine what type of browser request it's *supposed* to be (e.g. manual URL visit? Form submission? A `fetch()` request?).
* `thermoptic` uses the [Chrome Debugging Protocol (CDP)](https://chromedevtools.github.io/devtools-protocol/) to puppet the browser and set up a page that mocks the request exactly as it normally would occur in a real web browser.
* `thermoptic` triggers the request via the mocked context and captures the HTTP response.
* `thermoptic` sends the HTTP response back to the client.

Due to the fact that the browser is actually making the request using its full stack, the resulting JA4 fingerprints are identitical.

NOTE: Due to many WAFs employing JavaScript-level fingerprinting of web browsers, `thermoptic` also exposes hooks to utilize the browser for key steps of the scraping process. See [this section](#handling-browser-javascript-fingerprinting-with-thermoptic-hooks) for more information on this.

## Why *this* approach vs other solutions?

To put it bluntly: other approaches have fundamental flaws which prevent them from being a practical long term solution to the browser fingerprinting problem.

Many other attempts to "beat" browser JA4+ fingerprinting do so by reimplementing the various layers of the browser stack. This approach has a number of serious drawbacks, such as:

* Requiring great care to match the behavior of the "real" browser implementation perfectly. As a result, *any* quirks or discrepancies can be used to differentiate these clients from the "real" browser implementation.
* Attempting to only solve the problem at one layer of the stack. Chrome utilizes multiple protocols to provide a web browsing experience. As a result, even if you've made a perfectly-matching TLS layer your HTTP layer may give you away if it's not byte-perfect.
* As the "re