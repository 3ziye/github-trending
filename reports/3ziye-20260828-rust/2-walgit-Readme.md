# walgit — a git server that is one binary in front of an object store

walgit hosts git repositories with **no database, no leader and no local state that matters**. You run a
single binary, point it at an S3 or GCS bucket, and you have: smart HTTP (v0/v2) fetch and push, `bundle-uri`
clones served as static files, Git LFS, a browsing web UI, a JSON API with an SDK, per-repository push policy,
webhooks — and a server that scales to repositories **larger than the machine it runs on**. Every machine that
runs walgit is a disposable cache; the bucket is the repository.

```sh
# 1. a bucket (any S3-compatible store or GCS) and a config
cat > walgit.toml <<'EOF'
[server]
listen = "0.0.0.0:8080"
public_url = "https://git.example.com"
auto_create_on_push = true
[server.auth]
mode = "token"
anonymous_read = false
tokens = [{ principal = "me", token_env = "WALGIT_TOKEN_ME", write = true }]
[store]
backend = "s3"
bucket = "my-walgit"
[store.s3]
endpoint = "https://s3.us-east-1.amazonaws.com"
region = "us-east-1"
EOF

# 2. run it
WALGIT_TOKEN_ME=$(openssl rand -hex 24) walgit serve --config walgit.toml

# 3. use it — a push to a new name creates the repository
git -c http.extraHeader="Authorization: Bearer $WALGIT_TOKEN_ME" push https://git.example.com/acme/app.git main
```

That is the whole deployment. Add more machines pointed at the same bucket and they serve the same repositories,
consistently, with nothing to coordinate. Kill them all and you lose warmth, nothing else.

It is a Rust implementation of the architecture Cursor described in
[*Git at any scale*](https://cursor.com/blog/git-at-any-scale) (the system they call Continuity), with the changes
needed to run it on machines that are smaller than the repository. The post is worth reading first; it is kept
verbatim in `docs/reference/cursor-git-at-any-scale.md`.

---

## Why this shape

Git is distributed, and that makes hosting it miserable for one reason: **packfiles**. Everything in a repository
is compressed into large binary packs laid out to be small, not to be read in order; every git operation is a
random walk over gigabytes. That is fine on a laptop with the file in page cache and catastrophic over a network
filesystem, which is why "just put the repositories on NFS" failed at every large host that tried it. The design
that survived (GitHub's Spokes) keeps real repositories on local NVMe so upstream `git` does the work, and
replicates at the packfile level with strict consistency — paid for with three-phase commit across a fixed replica
set, a database that maps every repository to its machines, and a fleet of pets.

Continuity's insight changes the economics: **make a write-ahead log in object storage the source of truth, and
make every on-disk repository a cache.** A push is stored as an immutable object in the bucket and becomes visible
only when a tiny manifest is rewritten with a compare-and-swap. That CAS *is* the consensus — no election, no
quorum, no primary. Any instance may accept a push; two racing instances cannot both win. A replica that has never
seen a repository reads the log and has it. Reads are consistent without coordination because every read first
asks the store whether anything changed (a conditional GET, usually a 304). Compaction is done once by whoever holds
a lease and published *into the log*, so replicas download compacted packs instead of repacking. And because the
WAL is the truth, there is complete provenance: every push and every repack, replayable to any point.

walgit takes that as-is, and adds what a *monorepo on small machines* needs: serving refs and web pages for a
repository whose packs will never fit on the instance (a **remote reader** over HTTP range requests), keeping
commits and trees local while blobs stay in the bucket (the **history pack**), and moving clone bytes out of the
server entirely (**bundle-uri**: fresh clones and catch-ups are static files the bucket or a CDN hands out).

## What it does

| | |
|---|---|
| **git** | smart HTTP v0/v2: `ls-refs` with prefixes, fetch with filter/shallow/deepen/sideband-all, receive-pack (atomic, deletes, tags, push options, report-status-v2), `<owner>/<repo>` namespaces, sha1 and sha256 repositories. Upstream `git` does upload-pack/repack/bundle; walgit does receive-pack, the WAL and the plumbing. |
| **bundle-uri** | Bundles cut on calendar slots (weekly full, chained dailies, hourlies) as a pure function of the WAL: a fresh clone downloads the newest full plus the chain above it from the bucket and asks the server only for the remainder; a catch-up downloads exactly the slots it missed. Two lists per repo: `bundles/list` for clones, `bundles/catchup` for fetches. Blobless families for `--filter=blob:none`. |
| **LFS** | Batch API + basic transfer, objects in the bucket, optional read-through from an upstream LFS server for imported repositories. |
| **web UI + API** | A React UI (tree, blob, commits, diffs, the WAL's own health page) on a read-mostly JSON API 