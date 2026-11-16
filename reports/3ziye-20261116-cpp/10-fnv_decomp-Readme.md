# FNV decompilation

The decompilation of FNV, the Steam release for PC (version 1.4.0.525): C++ source code rebuilt function by function
from the game's executable. Built with the compilers the game was built with, every function listed in
`build/units.json` compiles to the same bytes as the original.

The project was spearheaded on [fnvdecomp.com](https://fnvdecomp.com), where a frozen version of the community
project stays online.

- **What it is for.** The modding community has kept working on FNV for more than a decade. This repository is meant
  for that community: for research, modding and game preservation, and only those purposes.
- **Source code only.** It contains no game files, no assets, no executables and nothing you can play, and nothing
  of the game is distributed here.
- **You need the game.** To use any of this you need to own the Steam version of FNV (1.4.0.525).
- **Trademarks** belong to their holders, listed under [Legal](#legal). This project is not affiliated with or
  endorsed by any of them.

## Contributing

Pull requests are welcome from anyone. Most of what is left is readability: many functions still have placeholder
names (`FUN_00xxxxxx`), vague names or no comment, and all of that can be improved without changing a single byte of
the output.

### The automatic check

Every pull request gets an automatic check, called `match`. It runs on GitHub's machines, involves no part of the
game, and has to pass before a pull request can be merged:

1. It finds the translation units your change can affect: the files you changed, every unit that includes them, and
   every unit whose entry in `build/units.json` changed.
2. It builds each of those units twice, from `main` and with your change, with the Microsoft compilers the game was
   built with.
3. Every function has to come out identical, at its original address: the same code bytes, and every call and data
   reference resolving to the same original address through `build/units.json`, exception-handling code included.
   A function that moved to another unit is compared with what it compiled to in its old unit. `main` matches the
   game byte for byte, so a change that passes still does.

What to expect:

- **Passes:** renaming functions, parameters, variables, types and fields; adding or improving comments;
  reformatting; restructuring headers and types; moving functions between units (see "Changing the build recipe"). A
  change only to comments, spacing or blank lines passes without a build.
- **Fails:** anything that changes what a function compiles to. The check lists the functions that differ by
  address; see what differs with your own copy of the game:
  `python3 tools/build_and_match.py --image <your FalloutNV.exe> --only <unit>`.
- **Needs a maintainer:** changes outside `src/`, `include/`, `build/units.json` and Markdown files (the tools, the
  workflow), and changes to `build/units.json` beyond what "Changing the build recipe" allows. The check fails on
  these and nobody can merge them, so open an issue instead. Changes to the tools and the workflow are made by the
  repository owner and verified against the game.

### Review and merging

A pull request is merged when the check passes and two reviewers have approved it:

- Nobody can skip the check, the repository owner included.
- Two approvals are needed. An approval is dropped when new commits arrive, and the last push has to be approved by
  someone other than the person who made it.
- The pull request has to be up to date with `main`. If `main` moves first, use "Update branch" and the check runs
  again on the combined code.

After every change to `main`, the whole of `main` is also built against the game's executable on the project's own
machine. That build proves `main` still matches the game byte for byte, not only that it compiles the same as
before.

### Renaming a function

`build/units.json` lists every function by its original address and its decorated (mangled) name. When you rename a
function, put its new decorated name at the same address, in every unit that lists it; otherwise the check reports
the old name as unbound. Adding a declaration or a string literal can renumber the compiler's string labels
(`$SG...`) that `build/units.json` names; the check says so when that is the cause.

A unit may also bind a name to an address it refers to, for example a global or a vtable that the code used to write
as a number: the check builds the unit again and the bytes at every function's address have to stay the same.
Exception-handling code resolves names through the whole of `build/units.json`, so when a pull request changes any
names there, the check also rebuilds every unit with exception-handling code. That adds a few minutes.

### Marking where a name comes from

A pull request that gives functions, globals, classes or fields new names from outside sources must say, at each
renamed definition, where the name came from. Then any group of names can be found an