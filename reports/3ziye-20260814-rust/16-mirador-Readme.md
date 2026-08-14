# mirador

[![CI](https://github.com/jchultarsky/mirador/actions/workflows/ci.yml/badge.svg)](https://github.com/jchultarsky/mirador/actions/workflows/ci.yml)
[![crates.io](https://img.shields.io/crates/v/mirador.svg)](https://crates.io/crates/mirador)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Rust 1.95+](https://img.shields.io/badge/rust-1.95%2B-dea584.svg)](https://www.rust-lang.org)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)](#install)

An opinionated personal dashboard for your terminal: world clocks, a calendar,
weather, a real task list, notes, a market watchlist, and live CPU and network
charts, laid out how you want them.

It is built for one job — to sit in a terminal tab you leave open all day and
glance at. That single constraint drives every decision below: nothing blinks,
nothing shimmers, and nothing is designed to pull you back to it.

A *mirador* is a lookout — the tower you climb to see everything at once.

![All thirteen mirador panels on a wide terminal, in use: a block-numeral clock, two months of calendar, weather with an hourly forecast, the task list, an agenda of upcoming events, notes, a news panel of headlines, a watch log, a calculator, a pomodoro timer, and a market watchlist beside live CPU and network graphs. Focus moves between panels, a task is typed in and added to the list, the panel picker switches a panel off and the grid reflows around it, arrange mode moves the task panel along its row and up into the row above until it takes a row of its own, the help overlay opens and scrolls, three sums are typed into the calculator and feed up its tape, and the pomodoro timer starts counting down](https://raw.githubusercontent.com/jchultarsky/mirador/main/docs/demo.gif)

*All thirteen panels on a first run, at 200x50 — wide enough that nothing has to fall
back. The lit frame is the focused panel, with its own keys in its bottom
border; every other panel is dimmed, so exactly one thing is at full brightness.*

*A minute of it in use. Focus moves with `Tab`; a task is typed in and
lands in the list, which goes from four open to five. `w` opens the panel picker,
switches one off, and the grid closes over the gap. `m` starts arranging: the
task panel moves along its row, then up into the row above, then past the top
edge into a row of its own — the real panels move as the keys are pressed, and
`Esc` puts it all back. `?` lists every binding for the focused panel and
scrolls when there are more than fit. Then three sums go into the calculator:
each answer appears in the right-hand column as it is typed, and Enter feeds it
up the tape, where the results line up on their decimal points.*

*The tasks and the note are the examples mirador seeds on a first run, and the
weather, the prices and the graphs are whatever was true while it recorded —
`docs/record-demo.sh` drives a real build under tmux. The one staged thing is
the calendar, because mirador deliberately never invents one: without a sample
the agenda panel would spend the recording explaining how to point it at a file.*

## Why

Most terminal dashboards are built to be *watched* — a system monitor you open
when something is wrong, dense and busy and refreshing as fast as it can.
mirador is built to be **glanced at**: one tab, all day, in the corner of your
eye. Everything follows from that. Nothing blinks or shimmers. The unfocused
panels dim so exactly one thing is at full brightness. A notice retires on your
first keypress, because a dashboard that nags is a dashboard you close.

**Your data stays in files you own.** Tasks, notes and the watchlist are plain
TOML you can hand-edit, keep in git, or delete. No database, no sync service,
no account, no API key, no telemetry, and nothing phones home unless you ask it
to — including the updater, which runs only when you run it, and an update check
that is off until you turn it on.

**It is a real task list, not a checklist.** Due dates, priorities, notes, tags,
filtering and full editing without leaving the dashboard. That is the panel most
dashboards treat as a checkbox, and it is the one you will use most.

The three network panels use free key-less endpoints:
[Open-Meteo](https://open-meteo.com) for weather, Yahoo's public chart endpoint
for prices — see [Market data](#market-data) for what that one means for you —
and, for news, whichever RSS feeds you configure. The shipped feeds are NASA,
Phys.org and Ars Technica; change or empty them in `[news.feeds]`.

Those three fetch the data their panels exist to show, which is not the same as
phoning home: nothing is sent about you, and switching a panel off with `w`
stops its requests entirely.

## How this was built

**mirador is written with heavy AI assistance.** The implementation, the tests
and most of this documentation were written by Claude (Anthropic), working from
my direction and review. The product decisions — what to build, what t