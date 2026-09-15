# The Anti-Mage project

Tired of anti-detect browsers? So am I. That is why I am publishing some of the techniques that catch them.

A non-profit Go project that scores how coherent a browser environment is, together with the reference data the scoring reads. A client asks for a score and gets back one determination, one number, and one sentence saying what the two mean. There is no signature list, no known-tool database, and nothing to keep updated. The whole thing runs on making a browser disagree with itself.

I know this will get reverse engineered. That is fine, and it is a starting shot. Everything here is MIT and the source is the specification.

## What it catches

23 independent readings, each looking at one place where a browser's own surfaces have to agree with each other and with the platform the browser claims to be:

| | |
|---|---|
| Platform claim | Installed fonts against the claimed platform |
| Agreement across execution scopes | Native accessor integrity |
| Numeric built-in behaviour | Exception types against the specification |
| Screen geometry against CSS | Viewport against the screen it claims |
| Layout and text metric identities | Agreement between the CSS and script paths |
| Time zone against measured offsets | Audio buffer coherence |
| Automation residue | Permission state coherence |
| ICE gathering against its own reported state | Candidate gathering against the state machine that runs it |
| Two serialisations of one drawing surface | Reported media capabilities |
| Hardware decoders against the device named | Both graphics interfaces against one device |
| The device named against the generation reported for it | Capabilities against the version claimed |
| What this browser reported it could not do | |

The browser-side collector takes 34 measurements to feed those readings. Native accessor integrity alone is four separate readings of every accessor a spoofer has to touch: how the function serialises, whether three different enumerators of its own keys agree, whether the property still sits on the interface prototype object where the interface definition puts it, and whether calling it with the wrong receiver throws the TypeError the specification mandates.

None of that needs to know what tool produced the environment. It only needs two things the browser said to disagree.

<img width="1186" height="679" alt="image" src="https://github.com/user-attachments/assets/a7a5ebf2-3843-469d-b806-5b5ca0e26fd6" />

## How the score is built

Each reading returns one of five determinations. `consistent` and `contradiction` are what they sound like. `instrumented` means the surface reports its own modification. `inconclusive` means the reading ran and decided nothing. `unverified` means the reading declined to weigh in, and that last one matters most, because it is the difference between a detector and a random number generator.

A reading abstains when the probe was not collected, when the browser does not expose the feature, when the page was not delivered to a secure context and the feature is gated there, when nothing was named to compare against, or when the reference table it would have read has not been verified against a system I have actually observed. A browser is never scored for lacking a feature.

Findings that survive that are weighed by class rather than counted. A surface that reports its own modification weighs least. A plain disagreement weighs more. A disagreement that nothing but a deliberate change produces weighs most. Those combine so that each further body of evidence adds less than the one before it, and the result is rounded onto a step of ten, so no single reading can be isolated by watching the last digit. The constants are in `internal/scan/band.go` if you want them.

Two properties hold by construction and are covered by tests. Only evidence raises the score, so withdrawing a reading can never raise it. And a self-declared hook explains its own downstream damage: when an accessor reports that it has been modified and a later reading contradicts itself in a way that accessor accounts for, the finding is downgraded from a lie to a declared modification. Suppression cannot buy confidence, and a privacy tool that is honest about what it patches is not treated as a liar for it.

The score tops out at 90. Nothing here will ever tell you an environment is certainly modified.

## Results

100 samples per browser on Windows. Scores land on multiples of ten, so range and median sit on that step exactly. The mean is given to one decimal and the last column rounds it back onto the step. 0 means nothing disagreed.

| Browser | n | Range | Median | Mean | Rounded |
|---------|---|-------|--------|------|---------|
| Chrome, stock | 100 | 0 | 0 | 0.0 | **0** |
| Firefox, stock | 100 | 0 | 0 | 0.0 | **0** |
| Edge, stock | 100 | 0 | 0 | 0.0 | **0** |
| Brave | 100 | 10-30 | 10 | 13.4 | **10** |
| AdsPower | 100 | 50-70 | 60 | 60.0 | **60** |
| CloakBrowser | 100 | 40-8