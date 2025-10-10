# Wyrm - v0.3 Hatchling

&#128679; Pre-release version &#128679;. If you want to support this project, please give it a star! I will be releasing updates and
devlogs on my [blog](https://fluxsec.red/) and [YouTube](https://www.youtube.com/@FluxSec) to document progress, so please give me a follow there.

Wyrm (pronounced 'worm', an old English word for 'serpent' or 'dragon') is a post exploitation, open source, Red Team security testing framework framework, written in Rust designed to be used by Red Teams, Purple Teams, 
Penetration Testers, and general infosec hobbyists. This project is fully built in Rust, with extra effort going into obfuscating artifacts which
could be present in memory. Project created and maintained by [flux](https://github.com/0xflux/), for **legal authorised security testing only**.

![Wyrm Malware Post Exploitation Implant Red Team](resources/wyrm_landscape.png)

Wyrm currently supports only HTTP(S) agents using a custom encryption scheme for encrypting traffic below TLS, with a unique packet design so that
the packets cannot be realistically decrypted even under firewall level TLS inspection.

This project is a work in progress, currently released at v0.2 (Hatchling). Updates are planned through versions 1,0, 2.0, 3.0, and 4.0. You can view
the planned roadmap in this project (see [Milestones.md](https://github.com/0xflux/Wyrm/blob/master/Milestones.md)). In time, this is designed to be an open source competitor to **Cobalt Strike**, **Mythic**, **Sliver**, etc.

For any bugs, or feature requests, please use the Issues tab, and for anything else - please use GitHub Discussions. I am active on this project,
so I will be attentive to anything raised.

### Features

- Implant uses a configurable profile to customise features and configurations
- IOCs encrypted in the payload to assist in anti-analysis and anti-yara hardening
- Implant transmits data encrypted below TLS, defeating perimeter inspection security tools out the box
- Dynamic payload generation
- Easy mechanism to stage files (such as built implants, PDF, zip, etc) on the C2 for download to support phishing campaigns and initial attack vectors
- Supports native Windows API commands, more planned in future updates
- Easy to use terminal client for the operator to task & inspect agents, and to manage staged resources
- Implant uses the most common User-Agent for comms to help it blend in covertly with traffic by default, this is also configurable to suit your engagement
- Easy, automated C2 infrastructure deployment with `install_server.sh`
- Anti-sandbox techniques which are highly configurable by the operator through profiles
- Backed by a database, fully timestamped to make reporting easier

This project is not currently accepting contributions, please **raise issues** or use **GitHub Discussions** and I will look into them, and help
answer any questions.

**Before deploying the C2**, you should read the C2 readme file, found in the `/c2` directory. Proper docs are coming soon
in time for v1.0 release, at https://wyrm-c2.com.

A mental model for the C2 is as follows:

![Wyrm C2](resources/c2_model.png)

The below image demonstrates the **Below TLS Encryption** feature and how it is implemented:

![Wyrm Below TLS Encryption](resources/wyrm_post_diag.png)

### Updates

**WARNING:** Before pulling an update; please check the [release notes](https://github.com/0xflux/Wyrm/blob/master/RELEASE_NOTES.md) to see whether there are any breaking changes - for example if the
**configurable C2 profile** changes in a breaking way from a previous profile you have, you will want to make sure you backup and migrate
your profile. I will be excluding `/c2/profiles/*` from git once the project is published in pre-release to prevent accidentally overwriting
your previous profile when running `git pull` to update your software.

As per the roadmap, this project will see significant development over the next 12 months. To pull updates, whether they are new features
or bug fixes, you simply just do a git pull, re-build the c2 in release mode via:

- `sudo systemctl stop wyrm`
- `cd c2`, 
- `cargo build --release`
- `sudo systemctl start wyrm`

### Setup

The project contains an install shell script, and is designed to be run on `Debian` based Linux flavours.
The install script will install all required dependencies to the project, as well as making a new user, `wyrm_user`
that will run the C2 service.

The user account is created as `sudo useradd --system --no-create-home --shell /usr/sbin/nologin wyrm_user`.

**Server Setup**

1) Install your favourite reverse proxy (NGINX / Apache etc). The web app will default to serve on `0.0.0.0` at `:8080`. You can edit this in `/c2/.env` (at step 2), so configure your reverse proxy to use whatever you define in the `.env`.
2) Clone the repo to your server & mark the install script executable.
3) **SECURITY**: 
   1) In `c2/.env` edit:
      1) `POSTGRES_PASSWORD`
      2) `ADMIN_TOKEN` - **DO NOT USE THE 