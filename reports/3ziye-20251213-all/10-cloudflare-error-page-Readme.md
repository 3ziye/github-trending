# Cloudflare Error Page Generator

📢 **Update (2025/12/09)**: All icons used in the error page have been fully redrawn as vector assets. These icons along with the stylesheet are also inlined into a single file of the error page, eliminating any need of hosting additional resources, and ensuring better experience for you and your end users.

## What does this project do?

This project creates customized error pages that mimics the well-known Cloudflare error page. You can also embed it into your website.

## Online Editor

Here's an online editor to create customized error pages. Try it out [here](https://virt.moe/cferr/editor/).

![Editor](https://github.com/donlon/cloudflare-error-page/blob/images/editor.png?raw=true)

## Quickstart for Programmers

### Python

Install `cloudflare-error-page` with pip.

``` Bash
pip install git+https://github.com/donlon/cloudflare-error-page.git
```

Then you can generate an error page using the `render` function. ([example.py](examples/example.py))

``` Python
import webbrowser
from cloudflare_error_page import render as render_cf_error_page

# This function renders an error page based on the input parameters
error_page = render_cf_error_page({
    # Browser status is ok
    'browser_status': {
        "status": 'ok',
    },
    # Cloudflare status is error
    'cloudflare_status': {
        "status": 'error',
        "status_text": 'Error',
    },
    # Host status is also ok
    'host_status': {
        "status": 'ok',
        "location": 'example.com',
    },
    # can be 'browser', 'cloudflare', or 'host'
    'error_source': 'cloudflare',

    # Texts shown in the bottom of the page
    'what_happened': '<p>There is an internal server error on Cloudflare\'s network.</p>',
    'what_can_i_do': '<p>Please try again in a few minutes.</p>',
})

with open('error.html', 'w') as f:
    f.write(error_page)

webbrowser.open('error.html')
```

You can also see live demo [here](https://virt.moe/cferr/examples/default).

A demo server using Flask is also available in [flask_demo.py](examples/flask_demo.py).

### Node.js/NPM

A Node.js package is available in [nodejs](nodejs) folder. However currently it supports only Node.js but not web browsers,
and we plan to refactor it into a shared package, so it can work in both environments.

(Thanks [@junduck](https://github.com/junduck) for creating this.)

### PHP

``` PHP
/* Coming soon! */
```

## More Examples

### Catastrophic infrastructure failure

``` Python
params = {
    "title": "Catastrophic infrastructure failure",
    "more_information": {
        "for": "no information",
    },
    "browser_status": {
        "status": "error",
        "status_text": "Out of Memory",
    },
    "cloudflare_status": {
        "status": "error",
        "location": "Everywhere",
        "status_text": "Error",
    },
    "host_status": {
        "status": "error",
        "location": "example.com",
        "status_text": "On Fire",
    },
    "error_source": "cloudflare",
    "what_happened": "<p>There is a catastrophic failure.</p>",
    "what_can_i_do": "<p>Please try again in a few years.</p>",
}
```

![Catastrophic infrastructure failure](https://github.com/donlon/cloudflare-error-page/blob/images/example.png?raw=true)

[Demo](https://virt.moe/cferr/examples/catastrophic)

### Web server is working

``` Python
params = {
    "title": "Web server is working",
    "error_code": "200",
    "more_information": {
        "hidden": True,
    },
    "browser_status": {
        "status": "ok",
        "status_text": "Seems Working",
    },
    "cloudflare_status": {
        "status": "ok",
        "status_text": "Often Working",
    },
    "host_status": {
        "status": "ok",
        "location": "example.com",
        "status_text": "Almost Working",
    },
    "error_source": "host",
    "what_happened": "<p>This site is still working. And it looks great.</p>",
    "what_can_i_do": "<p>Visit the site before it crashes someday.</p>",
}
```

![Web server is working](https://github.com/donlon/cloudflare-error-page/blob/images/example2.png?raw=true)

[Demo](https://virt.moe/cferr/examples/working)

## FAQ

### How to show real user IP / Cloudflare Ray ID / data center location in the error page so that it looks more realistic?

Ray ID and user IP field in the error page can be set by `ray_id` and `client_ip` properties in the `params` argument passed to the render function. The real Cloudflare Ray ID and the data center location of current request can be extracted from the `Cf-Ray` request header (e.g. `Cf-Ray: 230b030023ae2822-SJC`). Detailed description of this header can be found at [Cloudflare documentation](https://developers.cloudflare.com/fundamentals/reference/http-headers/#cf-ray).

To lookup the city name of the data center corresponding to the three letter code in the header, you can use a location list from [here](https://github.com/Netrvin/cloudflare-colo-list/blob/main/DC-Colos.json)

The demo server runs in our website did handl