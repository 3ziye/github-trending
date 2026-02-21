<h1 align="center">Vouch</h1>

<p align="center">
  A community trust management system.
</p>

<p align="center">
  <a href="FAQ.md">FAQ</a> · <a href="COOKBOOK.md">Cookbook</a> · <a href="CONTRIBUTING.md">Contributing</a>
</p>

---

People must be **vouched for** before
interacting with certain parts of a project (the exact parts are
configurable to the project to enforce). People can also be explicitly
**denounced** to block them from interacting with the project.

The implementation is generic and can be used by any project on any code forge,
but we provide **GitHub integration** out of the box via GitHub actions
and the CLI.

The vouch list is maintained in a single flat file using a minimal format
that can be trivially parsed using standard POSIX tools and any programming
language without external libraries.

**Vouch lists can also form a web of trust.** You can configure Vouch to
read other project's lists of vouched or denounced users. This way,
projects with shared values can share their trust decisions with each other
and create a larger, more comprehensive web of trust across the ecosystem.
Users already proven to be trustworthy in one project can automatically
be assumed trustworthy in another project, and so on.

> [!WARNING]
>
> This is an experimental system in use by [Ghostty](https://github.com/ghostty-org/ghostty).
> We'll continue to improve the system based on experience and feedback.

## Why?

Open source has always worked on a system of _trust and verify_.

Historically, the effort required to understand a codebase, implement
a change, and submit that change for review was high enough that it
naturally filtered out many low quality contributions from unqualified people.
For over 20 years of my life, this was enough for my projects as well
as enough for most others.

Unfortunately, the landscape has changed particularly with the advent
of AI tools that allow people to trivially create plausible-looking but
extremely low-quality contributions with little to no true understanding.
Contributors can no longer be trusted based on the minimal barrier to entry
to simply submit a change.

But, open source still works on trust! And every project has a definite
group of trusted individuals (maintainers) and a larger group of probably
trusted individuals (active members of the community in any form). So,
let's move to an explicit trust model where trusted individuals can vouch
for others, and those vouched individuals can then contribute.

## Who is Vouched?

**Who** and **how** someone is vouched or denounced is left entirely up to the
project integrating the system. Additionally, **what** consequences
a vouched or denounced person has is also fully up to the project.
Implement a policy that works for your project and community.

## Usage

### GitHub

Integrating vouch into a GitHub project is easy with the
[provided GitHub Actions](https://github.com/mitchellh/vouch/tree/main/action).
By choosing which actions to use, you can fully control how
users are vouched and what they can or can't do.

For an example, look at this repository! It fully integrates vouch.

Below is a list of the actions and a brief description of their function.
See the linked README in the action directory for full usage details.

| Action                                                        | Trigger               | Description                                                                                                                                                                                |
| ------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [check-issue](action/check-issue/README.md)                   | `issues`              | Check if an issue author is vouched on open or reopen. Bots and collaborators with write access are automatically allowed. Optionally auto-close issues from unvouched or denounced users. |
| [check-pr](action/check-pr/README.md)                         | `pull_request_target` | Check if a PR author is vouched on open or reopen. Bots and collaborators with write access are automatically allowed. Optionally auto-close PRs from unvouched or denounced users.        |
| [check-user](action/check-user/README.md)                     | Any                   | Check if a GitHub user is vouched. Outputs the user's status and fails the step by default if the user is not vouched. Set `allow-fail` to only report via output.                         |
| [manage-by-discussion](action/manage-by-discussion/README.md) | `discussion_comment`  | Let collaborators vouch, denounce, or unvouch users via discussion comments. Updates the vouched file and commits the change.                                                              |
| [manage-by-issue](action/manage-by-issue/README.md)