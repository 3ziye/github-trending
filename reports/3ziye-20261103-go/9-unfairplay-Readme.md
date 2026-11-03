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
open it once. Download a matching encrypted IPA with the same Apple Account.

Set up reusable decryption once:

```sh
sudo ./unfairplay setup \
  --app /Applications/App.app \
  --ipa App.ipa
```

Large enrollment databases print bounded recovery progress to standard error.
The final JSON result remains on standard output.

The setup result includes `plaintext_verified` for the matching IPA. A successful
setup can report `false` when any decrypted image lacks pre-encryption hashes;
this is separate from whether the model was recovered and saved successfully.

The saved model is private. It is tied to the Mac App Store enrollment, not to
one app, so it can decrypt other personalized IPAs from the same enrollment.
Back it up only in encrypted storage and never share it.

Decrypt another IPA:

```sh
./unfairplay decrypt --input AnotherApp.ipa
```

The default model directory is inside the user configuration directory. Set
`UNFAIRPLAY_MODEL_DIR` or pass `--model` to use another location.

IPAs with extensions and watch apps are decrypted in one pass.

The output keeps the input's `SC_Info` licenses and `iTunesMetadata.plist`,
which identify the Store account. To create a redacted copy for private
analysis or authorized collaboration, add `--strip-account-data`: it omits
every `SC_Info` member and removes the Apple ID and purchaser fields from
`iTunesMetadata.plist`. Redaction does not authorize redistributing the app;
the legal and ethical use terms above still apply. Test without
keeping plaintext with:

```sh
./unfairplay verify --input AnotherApp.ipa
```

The decryption path handles ARMv6/Thumb-1, ARMv7, ARM64, and
ARM64_32/watchOS slices.
Available pre-encryption page hashes must match; a mismatch fails closed.
Older executables without these tables can decrypt, but report
`plaintext_verified=false`.

### Convert an IPA for macOS

This requires an encrypted IPA personalized for the same Store enrollment as
your saved model. Convert it with:

```sh
./unfairplay convert-ipa-macos \
  --input App.ipa \
  --model /private/path/fairplay-enrollment.bin
```

Omit `--model` to use the saved model. The default output is `App.macos.ipa`.
Use `--output` to choose another path or `--force` to replace an existing
output.

The command uses a saved version-2 enrollment model. You can instead use a
matching private 16-byte credential:

```sh
chmod 600 credential.bin
./unfairplay convert-ipa-macos \
  --input App.ipa \
  --credential credential.bin
```

The conversion:

- decodes the current private record with the direct enrollment model;
- validates and rewrites the personalized SINF into the macOS layout;
- preserves its app key, signature, rights, and other private fields;
- adds every SINF copy declared by Apple for encrypted frameworks and
  extensions; and
- leaves all Mach-O executables byte-identical and encrypted.

Model-based conversion supports the observed 440- and 448-byte private SINF
records and the same bounded appended-rights geometry used by recovery.

The result is still an IPA, not a macOS installer. A macOS iOS-app wrapper or
compatible installer must preserve this basic layout:

```text
App iOS.app/
  WrappedBundle -> Wrapper/App.app
  Wrapper/App.app
  Wrapper/iTunesMetadata.plist
```

The converted IPA and wrapper contain a private account license. Keep them
private. This feature does not decrypt, modify, re-sign, or bypass checks inside
the app. Apps may still reject macOS, require unavailable hardware, or depend on
services that are not present on macOS.

## Advanced commands

`collect` and `recover` expose the two setup stages for diagnostics and
archived captures. `doctor` checks a capture, IPA, or model.

```sh
sudo ./unfairplay collect --app /Applications/App.app --ipa App.ipa --output App.capture
./unfairplay recover --capture App.capture --output App.recovery
```

## FAQ

### What is an enrollment?

An enrollment is the FairPlay state created when an Apple Account uses the Mac
App Store on a Mac. It links the account, Mac, and FairPlay selector. `setup`
turns that state into a reusable private model.

### What are SINF, SUPF, SIDB, and SC Info?

- **Personalized SINF:** an app 