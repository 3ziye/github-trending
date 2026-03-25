# Fetcharr

<img src=".doc-misc/fetcharr-temp-icon.png" width="60"/>

###### Icon is LLM-generated and temporary until one from an artist can be sourced.

<img src=".doc-misc/example-screenshot.png" width="1000"/>

## What is it?

Since Huntarr died, I still needed an application that scanned and upgraded my media.
I tried a few different projects but I didn't like any of them for various reasons.

Since vibe-coding is a big deal these days, I decided to brush off my Java rust and try my hand at
a containerized project that used configuration similar to Unpackerr and did one thing and did it well.
The few portions with LLM assistance have been noted (search `ChatGPT`) and generated code was read and verified before use.

No use of opencode, claude code, cursor, etc in this project. Any LLM assistance was done via web UI.
Largely to ask questions about design, errors, or specific details I've forgotten since touching Java.
Readme also written by hand.

I think I hit that nail on the head.

Currently supports the following:
- Radarr
- Sonarr
- Lidarr
- Whisparr

### Huntarr? What?

[The Huntarr saga](https://www.reddit.com/r/selfhosted/comments/1rckopd/huntarr_your_passwords_and_your_entire_arr_stacks/) is an interesting one
if you're curious, but if you're not familiar with the history then here's the short of what Fetcharr does:

The idea is that you’ll occasionally want to go through all your media and make sure it’s the best quality available and that nothing’s missing.
New releases get published, remuxes sometimes fix issues, etc. This little CLI container goes through and periodically searches every *arr app you connect
it to, so you don’t have to sacrifice hours of your weekend doing (as much) manual hunting.

Now, it's worth mentioning that Sonarr, Radarr, etc have had a built-in system that does this for a while now, but I've never gotten
them to work reliably. Maybe it's just bad luck or some strange misconfiguration, but I've always had a need for apps like
Scoutarr (Upgradinatorr), Huntarr, etc. Considering the popularity of these apps it feels like I am not the only one.

Update to this: I learned that at *arr stack uses RSS feeds to scan for and fetch updates, so if your indexer doesn't support those
feeds or the feeds or too old (or a myriad of other issues that can come from this kind of system) then you won't get replacement content
even if it exists. This is why these kinds of "hunting", "fetching", "upgrading", etc systems work so well. They simply force the *arr
apps to periodically update their content through their configured indexer, regardless of RSS feed availability.

If the concept sounds interesting to you, give Fetcharr a try. See if it finds anything. If my experience while developing this is anything
to go by, you'll get some results almost immediately. Likely within a few hours, and maybe even within a few seconds. See if it helps
and if you want to add it to your stack.

## How do I use it?

Docker, Kubernetes, whatever container system you currently use. Use the `latest` tag for the latest production build or
the `dev` tag for the latest development build.

Or by immutable tag: https://hub.docker.com/r/egg82/fetcharr/tags

Also available on GitHub: https://github.com/users/egg82/packages/container/package/fetcharr

<details open>
<summary>Docker</summary>

```bash
docker run \
  -e VERIFY_CERTS=true \
  -e SSL_PATH=/etc/ssl/certs/ca-bundle.crt \
  -e SEARCH_AMOUNT=5 \
  -e SEARCH_INTERVAL=1hour \
  -e RADARR_0_URL=https://radarr.home.lab \
  -e RADARR_0_API_KEY=e8ea891d72ff973fa6db0d34369a60a7 \
  -e SONARR_0_URL=https://sonarr.home.lab \
  -e SONARR_0_API_KEY=71730b5dfaa4293fe0c050844c10df66 \
  -e SONARR_1_URL=https://anime.home.lab \
  -e SONARR_1_API_KEY=bdb84dc8e4b787c76be8aae2dfe9bd19 \
  -v ./config:/app/config \
  -v ./cache:/app/cache \
  -v ./logs:/app/logs \
  egg82/fetcharr:latest
```
</details>

<details>
<summary>Docker Compose</summary>

```dockerfile
services:
  fetcharr:
    image: egg82/fetcharr:latest
    container_name: fetcharr
    hostname: fetcharr
    environment:
      - VERIFY_CERTS=true
      - SSL_PATH=/etc/ssl/certs/ca-bundle.crt
      - SEARCH_AMOUNT=5
      - SEARCH_INTERVAL=1hour
      - RADARR_0_URL=https://radarr.home.lab
      - RADARR_0_API_KEY=e8ea891d72ff973fa6db0d34369a60a7
      - SONARR_0_URL=https://sonarr.home.lab
      - SONARR_0_API_KEY=71730b5dfaa4293fe0c050844c10df66
      - SONARR_1_URL=https://anime.home.lab
      - SONARR_1_API_KEY=bdb84dc8e4b787c76be8aae2dfe9bd19
    volumes:
      - ./config:/app/config
      - ./cache:/app/cache
      - ./logs:/app/logs
    restart: unless-stopped
```
</details>

<details>
<summary>Kubernetes</summary>

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: fetcharr
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: config
  namespace: fetcharr
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 1Gi
---
apiVersion: v1
kind: PersistentVolumeClai