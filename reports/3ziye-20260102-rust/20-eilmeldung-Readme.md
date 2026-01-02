

![Logo of eilmeldung](docs/images/logo.png) 
  

![Screenshot of eilmeldung](docs/images/hero-shot.jpg) 

*eilmeldung* is a *TUI RSS reader* based on the awesome [news-flash](https://gitlab.com/news-flash/news_flash) library.  
- *fast* in every aspect: non-blocking terminal user interface, (neo)vim-inspired keybindings, instant start-up and no clutter
- *stands* on the shoulder of *giants*: based on the news-flash library, *eilmeldung* supports many RSS providers, is efficient and reliable
- *powerful* and yet *easy to use out-of-the-box*: sane defaults which work for most, and yet configurable to meet anyones requirements, from keybindings to colors, from displayed content to RSS provider
- read news like a pro: filter and search news with a easy-to-learn powerful *query language*, activate *zen mode* to focus on the article content and nothing else

*eilmeldung* is German for *breaking news*

# Showreel

https://github.com/user-attachments/assets/a8a1dc60-0705-4521-a88d-3520923d2891

This video demonstrates
- basic (vim-like) navigation and reading
- *zen* mode: just show content
- creating new tags and tagging a article
- *filtering* and *searching* article list by using a article queries
- *tagging* multiple articles by using an article query

# Installation 

Follow any of the installation methods below, then run *eilmeldung*. It will guide you through the setup process.

## Important: Nerd Fonts

You need a [Nerd Font](https://github.com/ryanoasis/nerd-fonts) compatible font/terminal for icons to display correctly!

## Via Homebrew

To install via [homebrew](https://brew.sh), tap this repository and install *eilmeldung*:

```bash
brew tap christo-auer/eilmeldung https://github.com/christo-auer/eilmeldung
brew install eilmeldung
```

## Via AUR (Arch)

There are two AUR packages: `eilmeldung` compiles the latest release and `eilmeldung-git` the `HEAD` of `main`. Use `paru` or `yay` to install.

## Via Cargo

In order to compile `eilmeldung` from source, you need `cargo` with a `rust` compiler with at least edition 2024 (e.g., use `rustup` and `rustup default stable`) and some build deps:

| Distribution | Dependencies (Build and Runtime)                                                           |
| ---          | ---                                                                                        |
| Ubuntu       | `# apt install rustup build-essential cargo perl libssl-dev pkg-config libxml2-dev clang libsqlite3-dev`<br>install stable rust toolchain as your user: `rustup default stable` |
| Fedora       | `# dnf install cargo rust perl libxml2-devel openssl-devel clang sqlite-devel`                           |
| Arch         | `# pacman -S cargo base-devel clang perl libxml2 openssl libsixel sqlite3`                             |

To compile the latest unreleased version (`HEAD` in `main`):
```bash
cargo install --locked --git https://github.com/christo-auer/eilmeldung
```
and for the latest tag:
```bash
cargo install --locked --git https://github.com/christo-auer/eilmeldung/tree/0.5.2
```


## Nix Flake and Home Manager

<details>
<summary> Expand for installation on Nix and Home Manager</summary>

  Add *eilmeldung* to your inputs, apply `eilmeldung.overlays.default` overlay to `pkgs`. If you want Home Manager integration, add Home Manager module `eilmeldung.homeManager.default`. Here is an example:

  ```nix
  {
    inputs = {
      // ...
      eilmeldung.url = "github:christo-auer/eilmeldung";
    };

    outputs = { nixpkgs, home-manager, eilmeldung, ... }: {
      homeConfigurations."..." = home-manager.lib.homeManagerConfiguration {
        pkgs = import nixpkgs {
          system = "x86_64-linux";
          overlays = [ eilmeldung.overlays.default ];
        };
        
        modules = [
          // ...
          eilmeldung.homeManagerModules.default
        ];
      };
    };
  }
  ```

Home Manager configuration works by defining the settings from the configuration file:

```nix
programs.eilmeldung = {
  enable = true;

  settings = {
    refresh_fps = 60;
    article_scope = "unread";


    theme = {
      color_palette = {
        background = "#1e1e2e";
        // ...
      };
    };

    input_config.mappings = {
        "q" = ["quit"];
        "j" = ["down"];
        "k" = ["up"];
        "g g" = ["gotofirst"];
        "G" = ["gotolast"];
        "o" = ["open" "read" "nextunread"];
    };

    feed_list = [
      "query: \"Today Unread\" today unread"
      "query: \"Today Marked\" today marked"
      "feeds"
      "* categories"
      "tags"
    ];
  };
};


```

</details>


# Getting Started

Once installed, run `eilmeldung` to begin. On first launch, you'll be guided through:

## Initial Setup

**Note**: inoreader is currently **NOT** directly supported. Create an issue if you need support for inoreader!

1. Choose Your Provider: Select from local or cloud-based RSS providers ([see news_flash_gtk for all supported providers](https://gitlab.com/news-flash/news_flash_gtk)