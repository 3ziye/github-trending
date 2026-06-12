# XALEN Ephemeris

**A pure-Rust astronomical ephemeris for astrology — JPL-class planet accuracy, zero `unsafe` core, Apache-2.0.**

[![Crates.io](https://img.shields.io/crates/v/xalen-ephemeris.svg)](https://crates.io/crates/xalen-ephemeris)
[![docs.rs](https://img.shields.io/docsrs/xalen-ephemeris)](https://docs.rs/xalen-ephemeris)
[![CI](https://github.com/vedika-io/xalen-ephemeris/actions/workflows/ci.yml/badge.svg)](https://github.com/vedika-io/xalen-ephemeris/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

> **Publish status:** the Rust crates, the PyPI `xalen` wheel, and the npm `xalen` (native) / `xalen-ephemeris` (WASM) packages are **not published to their registries yet** — the Crates.io / docs.rs registry badges above are placeholders until first release. Build from source per the per-binding READMEs (`crates/xalen-python`, `crates/xalen-node`, `crates/xalen-wasm`).

> **Validated against the references that matter** — JPL Horizons **DE440** (NASA's
> definitive ephemeris), the real DE440 binary kernel, **Swiss Ephemeris**, and the
> public calculators (astro.com, AstroSage, Drik Panchang, Prokerala, Jagannatha
> Hora). **Sun + Mercury–Saturn sub-arcsecond** vs DE440 (Sun 0.21″, Mercury–Saturn
> ≤ 0.76″; Uranus/Neptune ~1.8–2.5″, Pluto arcminute-class in-window). Analytical
> **Moon RMS ~2.8″ / max ~12″** vs pyswisseph (AD 1600–2100); the DE440 kernel takes
> the Moon **sub-arcsecond**. Pure Rust, zero `unsafe` in the core, thread-safe,
> Apache-2.0. Full report → [docs/ACCURACY.md](docs/ACCURACY.md).

```rust
use xalen_ephem::{Almanac, Body};
use xalen_time::{calendar_to_jd, CalendarSystem, JulianDay};
use xalen_ayanamsa::Ayanamsa;
use xalen_vedic::nakshatra::Nakshatra;

let jd = calendar_to_jd(1990, 3, 15, 12.0 - 5.5, CalendarSystem::default());
let almanac = Almanac::default_vedic();
let pos = almanac.geocentric_ecliptic(Body::Moon, jd).unwrap();
let sid = (pos.longitude.to_degrees() - Ayanamsa::Lahiri.compute_deg(jd.as_f64())).rem_euclid(360.0);
println!("{}", Nakshatra::from_longitude_deg(sid)); // Swati
```

---

## What You Get

- **50 ayanamsa systems** -- Lahiri, KP Krishnamurti, Raman, Fagan-Bradley, True Chitrapaksha, True Revati, Surya Siddhanta, all Galactic Center variants, Babylonian (Kugler), all Swiss Ephemeris IDs (0-46), plus a fully custom variant with user-defined epoch, value, and precession rate

- **23 house systems** -- Placidus, Koch, Campanus, Regiomontanus, Whole Sign, Equal, Porphyry, Morinus, Alcabitius, Topocentric (Polich-Page), Meridian, Vehlow, Sripati, Krusinski-Pisa, Sunshine (Makransky & Treindl), Pullen Sinusoidal (Delta & Ratio), Carter Poli-Equatorial, APC, Zariel, Alcabitius Classic -- with automatic Porphyry fallback at polar latitudes. (Gauquelin sectors is an experimental placeholder that currently returns Placidus cusps, not a true Gauquelin division.)

- **12+ astrology traditions** -- Vedic/Jyotish (dasha, shadbala, KP, Jaimini, Tajaka, panchang with tithi/nakshatra/yoga/karana transition times, compatibility, 16 divisional charts, yoga, dosha), Western (aspects, dignities, 97 Arabic Lots, Hellenistic, Uranian, Cosmobiology, progressions, exact solar/lunar returns by iterative refinement, declination aspects + antiscia, harmonics, horary), Chinese (BaZi, Zi Wei Dou Shu, Feng Shui Flying Stars, Qi Men Dun Jia [experimental]), Lal Kitab, I Ching (64 hexagrams + all 384 line texts, verbatim public-domain Legge SBE XVI), Numerology, Korean Saju, Japanese Nine Star Ki, Burmese Mahabote (day-sign profile only), Mayan, Aztec, Tibetan, Persian/Zoroastrian, Egyptian, Celtic

- **506 built-in fixed stars** (in `xalen-western`) with proper motion and precession correction (all mag < 3.0, Behenian, Royal, Nakshatra yogatara, IAU-named to mag ~5). The `xalen-stars` crate adds **8,870 compiled-in Hipparcos stars** (every Hipparcos record at Vmag ≤ 6.5, propagated J1991.25 → J2000.0, zero data files) on top of a 108-star curated core catalog — and still supports loading the full 118,218-star Hipparcos catalog from CSV at runtime

- **Solar and lunar eclipse engine** -- rigorous Besselian elements (Explanatory Supplement §11; Meeus Ch. 54) for global type / γ / greatest-eclipse, plus a per-observer local-circumstances layer (magnitude, obscuration, C1–C4 contact times); lunar eclipse classification (total / partial / penumbral) via Meeus Ch. 55. Global type validated against NASA for 2017-08-21 and 2024-04-08

- **Black Moon Lilith** -- both **mean** lunar apogee and **True (osculating)** Lilith (Swiss `SE_OSCU_APOG`), Chiron, True Node, Mean Node

- **Velocity / daily motion** for every body, with `is_retrograde()`,
  **topocentric positions** (diurnal parallax) for an observer's exact location,
  and **equatorial RA/Dec, heliocentric, and rectangular XYZ** output alongside
  the geocentric ecliptic place

- **Time systems** -- UT1 / TT / TDB Julian Day types, UTC↔TAI with the full
  leap-second table, a