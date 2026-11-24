# UnfairPlay

UnfairPlay recovers a FairPlay model from an enrolled Mac and uses it to
decrypt personalized iOS IPAs. It is a standalone Go program.

It does not log in to Apple, buy apps, or download IPAs. You can use ipatool or
another downloader for that part.

## Legal and ethical use

Use UnfairPlay only with apps you lawfully acquired and accounts and devices
you control. It is intended for interoperability, preservation, and authorized
research. The authors do not condone piracy, credential theft, copyright
infringement, or unauthorized distribution of decrypted apps.

## Discord

Project discussion and support: [UnfairPlay Discord](https://discord.gg/hpwvuQHfaf).

## Build

```sh
go build -o unfairplay ./cmd/unfairplay
```

## Usage

First, sign in to the native Mac App Store. Install an iPhone or iPad app and
open it once. Set up reusable decryption from that installed app:

```sh
sudo ./unfairplay setup --app /Applications/App.app
```

No separate IPA download is needed when the installed bundle contains supported
encrypted images and their matching licenses. Setup and collect build a private
validation archive from the complete inner iOS bundle, preserving its bytes.
Unsupported, incomplete, symlinked, or already-decrypted bundles fail closed.

To validate against a downloaded IPA instead, pass `--ipa` explicitly:

```sh
sudo ./unfairplay setup --app /Applications/App.app --ipa App.ipa
```

The installed app and IPA must be the same app and belong to the same Store
enrollment. An explicit IPA takes precedence; failed validation never triggers
an automatic retry using the installed bundle.

Recovery still authenticates the selected SINF and requires complete archive
decryption before saving a model. Reports identify `validation_source` as
`installed-app` or `provided`. A reconstructed validation archive describes the
installed variant, not the original Store download or any omitted architectures.

Large enrollment databases print bounded recovery progress to standard error.
The final JSON result remains on standard output.

The setup result includes `plaintext_verified` for the validation archive.
A successful setup can report `false` when any decrypted image lacks
pre-encryption hashes; this is separate from whether the model was recovered
and saved successfully.

The saved model is private. It is tied to the Mac App Store enrollment, not to
one app, so it can decrypt other personalized IPAs from the same enrollment.
Back it up only in encrypted storage and never share it.

Decrypt another IPA:

```sh
./unfairplay decrypt --input AnotherApp.ipa
```

The default model directory is inside the user configuration directory. Set
`UNFAIRPLAY_MODEL_DIR` or pass `--model` to use another location.

### Export enrollment now, choose an IPA later

On an already enrolled Mac, export the enrollment without supplying an installed
app or IPA:

```sh
sudo ./unfairplay export-enrollment --output enrollment.snapshot
```

The output parent directory must already exist. The command never overwrites an
existing snapshot. It writes a mode-0600 file and restores its ownership to the
invoking user when run through sudo.

The snapshot contains the hardware identity and one distinct supported SIDB
container. Export authenticates and decodes the container, but does not select
an account/key route or produce a validated model. It neither enrolls the Mac
nor adds missing licenses. Treat it as broader private enrollment state: keep it
secret and transfer it only to machines you control, preserving mode 0600.

Later, on macOS or Linux, select a personalized IPA and run setup as your normal
user:

```sh
./unfairplay setup --enrollment enrollment.snapshot --ipa App.ipa
./unfairplay decrypt --input AnotherApp.ipa
```

This uses the IPA's own licenses; no installed-app path is required. Setup
authenticates the exact selected route and signed page-key envelopes, then
decrypts and validates the complete IPA before installing the usual reusable
model. Missing pre-encryption hashes remain `plaintext_verified=false`.
Snapshot setup currently requires every encrypted image in the IPA to share
one user/key selector; multiple-selector IPAs reject explicitly. A snapshot can
be reused with different IPAs or selectors already present in its captured
state. Missing records require an appropriate enrollment; recovery never tries
other routes. Re-export after enrollment changes when necessary.

`--app` and `--enrollment` are mutually exclusive. Existing app-based setup and
saved models continue to work. Synthetic tests cover this workflow; private
installed-app versus snapshot equivalence is an opt-in control in [QA.md](QA.md).

### Recoverable IPA decryption

```sh
./unfairplay decrypt-recoverable --input App.ipa --model source-model.bin
./unfairplay encrypt --input App.decrypted-recoverable.ipa --model destination-model.bin
```

The first command saves the application key and source rights in a private
`.sinf-recovery` file. The second restor