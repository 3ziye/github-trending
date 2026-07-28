# Shell Gym - an Interactive Linux Command-Line Trainer

Shell Gym is a background daemon with a built-in web UI that turns
any Linux box into an interactive command-line trainer.

"Learn the idea in a tutorial. Build the reflex in Shell Gym."

Tutorials explain concepts - Shell Gym drills them, helping you form the right muscle memory.
Open a **split-screen**: a completely ordinary terminal on the one side, and the Shell Gym UI
on the other. The UI shows small, fast-changing assignments - **reps** (in the traditional
gym sense). Each rep asks for one concrete action (enter a directory, create a file, kill a
process, free a port) and completes automatically the moment the system state changes.
There is no "check" button and no copy-paste: you will have to type real commands into a real shell,
and the gym trainer will observe your actions and guide you on the way.

> [!TIP]
> Try it online: [Shell Gym Playground](https://labs.iximiuz.com/playgrounds/shellgym) (requires a free sign-up with GitHub)

https://github.com/user-attachments/assets/820ed962-38bf-49c8-92ea-87d51f8e4da4

## Why it exists

Reading about navigating the file tree, stdio redirection, or signals is not the same as being
able to perform these actions without thinking. That fluency comes only from hands-on practice
and repetition - and this is what Shell Gym provides.

## How it works

The student's shell is not modified in any way: no prompt hooks, no wrappers, no special shell functions.
All observation happens from the outside, meaning you work in the regular Linux terminal.

The Linux "magic" Shell Gym uses to achieve "zere instrumentation" observation:

- **procfs** - discovering the interactive shells, reading their working directories, scanning processes, files, and ports.
- **the kernel proc connector** - a netlink firehose of every `exec()` on the box, used to notice which commands the user runs.
- **plain state checks** - files existing, processes running, ports listening.

Because nothing is injected into the shell, the skills practiced in the
gym transfer one-to-one to any real terminal. See [detection.md](docs/detection.md)
for how each mechanism works.

## Quick start

> [!TIP]
> **Shell Gym does not open a terminal for you** - the web UI is only the "trainer" half of the
> screen. You type commands into your own regular terminal, placed side by side with the UI:
>
> - Some terminals (e.g., `cmux`) can show a browser pane next to the shell, giving you the
>   split-screen out of the box.
> - With any other terminal, use your OS's window tiling to put a terminal window and a
>   browser window side by side.

Quickest way to try Shell Gym without any setup is the [Shell Gym online playground](https://labs.iximiuz.com/playgrounds/shellgym) -
a regular Ubuntu VM with Shell Gym (and Go) preinstalled and the split-screen view already arranged (requires a free sign-in with GitHub).

Shell Gym runs on a plain Linux host (a VM, a spare laptop, an EC2 instance, etc.) **as root**.
It should work on most (if not all) mainstream Linux distributions.

> [!CAUTION]
> Since reps will ask you to perform real actions on the live system, **use Shell Gym only with a disposable Linux host.** A few options:
> - Use a local VM (Lima, SlicerVM, VirtualBox, etc.)
> - Use an [iximiuz Labs Linux Playground](https://labs.iximiuz.com/playgrounds?category=linux&filter=official)
> - Use a DigitalOcean droplet, an EC2 instance, etc.

### Option 1: Download a release binary

Grab the latest release tarball (it bundles the `shellgym` binary and the
sample learning path) and unpack it:

```sh
arch=$(uname -m | sed 's/x86_64/amd64/; s/aarch64/arm64/')
curl -L "https://github.com/iximiuz/shellgym/releases/latest/download/shellgym_linux_${arch}.tar.gz" | tar xz
```

### Option 2: Build from source

Clone the repository and build the binary (requires Go):

```sh
make build
ln -s bin/shellgym shellgym
```

### Start the daemon

```sh
sudo ./shellgym serve --path "$PWD/paths/sample-linux-101" --user $USER
```

...or start the Shell Gym daemon in the background:

```sh
sudo systemd-run --unit=shellgym --collect \
    "$PWD/shellgym" serve --path "$PWD/paths/sample-linux-101" --user $USER
```

Once started, open the web UI in a browser and follow the learning path:

```sh
open http://127.0.0.1:63636
```

## Bring your own learning paths

Shell Gym defines a format, not a curriculum. The bundled [sample-linux-101](paths/sample-linux-101) path is the reference implementation.
A **learning path** is a directory tree that follows the following structure:

```
paths/<path>/              # path.yaml: id, title, user
    010.module-a/          # numeric prefix defines order
        module.md          # optional module intro (static)
        010.unit-x/
            unit.md        # a signle "rep" (tasks + checks)
    020.module-b/          # another module
        ...
```

- **Path** - the whole course (`path.yaml` + modules). One daemon serves one path.
- **Module** - a themed 