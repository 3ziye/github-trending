# Furgit

[![builds.sr.ht status](https://builds.sr.ht/~runxiyu/furgit.svg)](https://builds.sr.ht/~runxiyu/furgit?)
[![Go Reference](https://pkg.go.dev/badge/git.sr.ht/~runxiyu/furgit.svg)](https://pkg.go.dev/git.sr.ht/~runxiyu/furgit)

Furgit is a fast Git library in pure Go.

## Project status

Furgit is in initial development, does not have tagged releases yet, and we can
guarantee that the API will break every now and then. Do not use in
production. When we do have tagged releases, we will likely follow
[Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## History

Furgit's lineage is from [Villosa](https://codeberg.org/lindenii/villosa), a
new, work-in-progress software development forge. It started as an internal
package inside Villosa, and was later extracted into a standalone module.

## Goals and current features

We do not focus on command-line utilities; in particular, Furgit does not
intend to replace [upstream git](https://git-scm.com). It is intended to be
used as a library.

We intend for repository objects to be freely usable across goroutines, which
may enable long-running applications such as forges to keep a pool of recently
used repos (including their `.idx` and `.pack` cache) for rapid access.

There is no specific plan for features yet, but we'll initially focus on
developing what forges like [Villosa](https://codeberg.org/lindenii/villosa) and
[tangled](https://tangled.org/@tangled.org/core) (and other forges if
interested) requires. Afterwards, we'll take a look at what other usages (such
as writing Git clients, IDE integration, etc) would need.

Furgit has no dependencies outside the standard library. In the future,
packages from `golang.org/x` may be included. It is unlikely that other
dependencies will be introduced.

Currently, furgit is very basic; it supports reading and writing loose objects
and reading from packfiles. There is some infrastructure for writing packfiles
in the tests but they need to be refactored.

## Environment requirements

We currently do not intend to support flexible storage backends such as
[storers in go-git](https://pkg.go.dev/github.com/go-git/go-git/v5/plumbing/storer);
a standard UNIX-like filesystem with
[syscall.Mmap](https://pkg.go.dev/syscall#Mmap) is expected.

## Performance

Furgit is being aggressively optimized for performance.

It is difficult to optimize Go code to be as performant as libgit2 (or
for that matter, upstream git). However, we are making tiny steps
towards it.

The first step that has been arguably a success is the packfile parser.
By using memory-mapped I/O, relatively optimized delta resolution, and
zero-copy techniques, Furgit is able to perform the equivalent to
`git ls-tree --long HEAD` on the Linux repository in about 2ms on
a ThinkPad T14, which is comparable to Git, faster than libgit2,
and significantly faster than go-git.

However this is a microbenchmark and does not reflect all real-world
performance. For example, when recursively listing tree entires and
commits, Furgit's performance is slightly slower than libgit2, both
lack behind Git by multiple orders of magnitude.

Things we might consider in the future include:

* [commit-graph](https://git-scm.com/docs/commit-graph)
* Using a custom zlib implementation to amortize decompression overhead
* More optimizations to delta resolution

## Hash algorithm

Furgit supports both SHA-256 and SHA-1.

The default tests run with SHA-256. To run tests with SHA-1, use the `sha1`
build tag.

## Go versions

We currently support Go 1.18 or later, in order to support
ougccgo](https://gcc.gnu.org/onlinedocs/gccgo/).

gccgo support may be dropped in the future if there is a strong reason to use
newer language features.

## Active services using Furgit

There's an experimental instance of [Villosa](https://codeberg.org/lindenii/villosa)
hosting [a copy of Linux](https://villosa.lindenii.org/test//repos/linux/)
([tree](https://villosa.lindenii.org/test//repos/linux/HEAD/tree/)) using
Furgit as the Git backend.

## Repos and community resources

The [main repository](https://forge.lindenii.org/furgit/-/repos/furgit/) is
hosted on [Lindenii Forge](https://forge.lindenii.org/forge/-/repos/server/)
(the previous iteration of [Villosa](https://codeberg.org/lindenii/villosa)).

To contribute, clone the repository from the SSH remote
`ssh://forge.lindenii.org/forge/-/repos/server`, create a unique branch that
begins with `contrib/`, and push. Your branch will be associated with your SSH
key and a merge request will be created, and the maintainers will be notified
on IRC.

Anonymous SSH cloning is supported with or without a key. Pushing requires an
SSH key: no key pre-registration is required, but you have to ensure that your
key is consistent throughout pushes if you push multiple times.

```
git clone ssh://forge.lindenii.org/furgit/-/repos/furgit
cd furgit
git checkout -b contrib/name_of_your_contribution
# edit and commit stuff
git push -u origin HEAD
```

There are a