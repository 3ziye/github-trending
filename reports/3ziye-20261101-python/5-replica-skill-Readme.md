# The Replica skill

Eleven Claude skills that clone any app. Free, MIT, no signup, no API key,
nothing to connect.

One reverse-engineers the app you want to clone. One rebuilds it. One tests it
for bugs. And one is the Entrepreneur: it reads what the app's users hate and
fixes it in yours, so you have an app you can sell.

In between, the others plan the stack and the database, rebuild the design
system, wire up auth and payments, score your clone against the original, give
it a name and a brand of its own, write the landing page and the store
listing, and put it live on your domain.

**It rebuilds what an app does, never what it owns.** Features and flows,
clean-room style. Not its code, its logo, its copy or its content. The
fine print is at the bottom, and the skills enforce it.

## Install

Paste this into Claude:

```
https://github.com/Jakeschincariol/replica-skill

install skill
```

Or as a plugin, in Claude Code:

```
/plugin marketplace add Jakeschincariol/replica-skill
/plugin install replica-skill@replica-skill
```

Claude Code namespaces plugin skills, so installed as a plugin they show up as
`/replica-skill:replica-recon` and so on. Copy the folders instead if you want
plain `/replica-recon`:

```bash
git clone https://github.com/Jakeschincariol/replica-skill.git
cp -r replica-skill/replica-* ~/.claude/skills/
```

Project-local instead of global: copy the same folders into your repo's
`.claude/skills/`. No Claude Code at all? Paste any single `SKILL.md` at the
top of a chat and it runs as a mode. You lose the Python tools, but the
method works.

The tools need Python 3.8 or newer. Nothing to pip install.

## The eleven

| command | what it does |
| --- | --- |
| `/replica-recon` | Reverse-engineers any app: screens, flows, components, data model. From public pages, screenshots, store listings and your own account. |
| `/replica-architect` | Plans the stack, database schema and API for your clone. |
| `/replica-design` | Rebuilds the design system: colours, type, spacing, components. As tokens, with your own assets. |
| `/replica-build` | Rebuilds the app screen by screen from the recon map. |
| `/replica-backend` | Auth, database, payments and integrations. |
| `/replica-test` | Clicks through every flow and tests it for bugs. |
| `/replica-diff` | Compares your clone against the original. A parity score and what is missing. |
| `/replica-entrepreneur` | Reads what the app's users hate in real reviews and turns it into fixes and a positioning angle. |
| `/replica-brand` | Names and rebrands your version so it is yours. |
| `/replica-launch` | Landing page, pricing and App Store listing. |
| `/replica-deploy` | Ships it live on your own domain. |

## How to use it

Run them in order. Each one reads what the last one wrote, in a `replica/`
folder in your project.

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

An example: cloning a scheduling app, the kind where you share a link and
people book a time with you.

1. **`/replica-recon`** with the app's URL. It reads the help center, the
   pricing page, the store listing and public walkthroughs, and you click
   through your own account with it. Out comes `replica/recon.md`: 18
   screens, 7 flows (guest books a meeting, host sets availability, guest
   reschedules...), the components, an inferred data model (users, event
   types, availability, bookings) and `features.csv`. The partner
   marketplace is marked out of scope: that is their network, not a feature.
2. **`/replica-architect`** picks Next.js, Postgres, Stripe and Resend, writes
   the schema (with a constraint so two guests can never book the same slot)
   and orders the build: the booking flow end to end first.
3. **`/replica-design`** measures the screenshots into tokens: colour roles,
   type scale, 8px spacing, the date picker and slot button specs. Open
   icons, an open font, your own words.
4. **`/replica-build`** builds the shell, then the booking flow, then every
   screen with all its states, ticking off `features.csv` as it goes.
5. **`/replica-backend`** adds sign up, Google Calendar through Google's own
   API with your keys, Stripe for paid bookings, reminder emails.
6. **`/replica-test`** writes a test plan from the 7 flows, Playwright specs
   for the happy paths and edge cases (time zones, a slot taken mid-booking,
   double submit), and logs bugs by severity until no S1 or S2 is open.
7. **`/replica-diff`** scores it. Features 86, all must-haves done, booking
   page layout 91. Missing: round-robin for teams, the website embed.
8. **`/replica-entrepreneur`** reads 140 real reviews across the App Store,
   G2, Capterra and Reddit. Top complaints: per-seat price jumps, no text
   reminders, guests confused by time zones. Each with counts and linked
   quotes. Fix plan: flat pricing, SMS reminders, a time zone confirm step.
   Angle: booking links for small teams that hate per-seat pricing.
9. **`