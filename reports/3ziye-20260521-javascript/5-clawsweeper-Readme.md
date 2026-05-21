# 🦞🧹 ClawSweeper

ClawSweeper is the conservative maintenance bot for OpenClaw repositories. It
keeps the backlog reviewed, keeps maintainer-visible GitHub comments tidy, and
turns narrow trusted findings into guarded repair or automerge work.

The current production targets are `openclaw/openclaw`, `openclaw/clawhub`, and
self-review for `openclaw/clawsweeper`.

The OpenClaw-hosted ClawSweeper instance is not a public review service and does
not provide free reviews for third-party repositories. If you want ClawSweeper
for your own project, fork this repository, deploy it in your own organization,
and configure that self-hosted instance for your repositories.

At a high level ClawSweeper:

- reviews open issues and pull requests on a schedule and on exact GitHub events
- writes one durable markdown report per item in generated state
- syncs one marker-backed public review comment per issue or PR, edited in place
- closes only unchanged, high-confidence, policy-allowed proposals
- routes maintainer commands such as `@clawsweeper review`,
  `@clawsweeper fix`, `@clawsweeper autofix`, and `@clawsweeper automerge`
- can acknowledge maintainer comment commands through an optional GitHub App
  webhook before the GitHub Actions fallback starts
- repairs opted-in PRs through a bounded Codex review/fix loop before merge
- can open guarded implementation PRs for strict, reproducible bug issues
- reviews code-bearing commits that land on target `main` branches
- publishes dashboard, audit, repair, and activity state to
  `openclaw/clawsweeper-state`

ClawSweeper is not a generic auto-close bot. Review is proposal-only, apply is
guarded, Codex never gets write credentials during review, and every GitHub
mutation is rechecked against live target state immediately before it happens.

## Capabilities

### Issue and PR Reviews

Scheduled runs scan open issues and pull requests, while target repositories can
forward exact issue/PR events with `repository_dispatch` for low-latency
one-item reviews. Each review writes
`records/<repo-slug>/items/<number>.md` with the decision, evidence, proposed
maintainer-facing comment, runtime metadata, and GitHub snapshot hash.

ClawSweeper syncs one marker-backed public review comment per item and edits it
in place instead of posting repeated comments. If a review starts before a
completed comment exists, it first posts a short status placeholder, then
replaces that same comment with the final review. Pull request comments include
hidden verdict/action markers so trusted repair and automerge flows can continue
without scraping visible prose. See
[`docs/pr-review-comments.md`](docs/pr-review-comments.md).

For open issues with complete, current kept-open reviews, ClawSweeper also
projects selected structured review conclusions into advisory GitHub labels for
maintainer filtering and project views. These labels expose states such as
current-main reproduction, source reproduction, linked open PRs, queueable
fixes, missing info, and product/security review needs. They are advisory only
and do not trigger repair, merge, or close behavior. Label-only syncs record
`labels_synced_at` in the durable report so GitHub `updated_at` changes caused
by ClawSweeper-owned label writes do not look like fresh target-side activity to
the scheduler. See
[`docs/work-lane.md`](docs/work-lane.md).

### Apply and State

Apply mode re-fetches live GitHub state, checks labels, maintainer authorship,
paired issue/PR state, snapshot drift, and repository profile rules before
commenting or closing anything. Closed or already-closed reports move to
`records/<repo-slug>/closed/<number>.md`; reopened archived items move back to
`items/` as stale work.

Generated state lives on the `state` branch of `openclaw/clawsweeper-state`:
durable `records/`, `jobs/`, `results/`, audit output, workflow status JSON,
repair ledgers, and the rendered dashboard. The state repo `main` branch is the
dashboard renderer source, so a checkout on `main` intentionally does not show
`records/`. Hydrate this repo with `git -C ../clawsweeper-state switch state &&
node scripts/hydrate-state.ts --state-dir ../clawsweeper-state` when local
commands need generated records. This repository stays focused on source,
workflows, docs, and tests.

### Repair and Automerge

Maintainer commands can opt PRs into `autofix` or `automerge`, dispatch a fresh
exact-head review, and run a bounded Codex review/fix loop. Codex handles the
code repair and local validation loop; deterministic executor steps own every
GitHub mutation, branch push, label update, and final merge gate.

Automerge waits for exact-head review, required checks, mergeability, and policy
gates. If repair was needed, the mutable status comment records each review,
repair, re-review, and merge step with timing and links. The final merge result
summarizes both the original PR change and any ClawSweeper fixups.

For issues, strict bug reviews that are high-confidence reproducible, do not
already h