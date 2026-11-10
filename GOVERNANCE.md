# Governance

This document describes how the [`winsell-vn`](https://github.com/winsell-vn)
organization makes decisions. It applies to every repository in the
organization unless a repository ships its own `GOVERNANCE.md`.

## Roles

| Role | Who | What they can do |
| --- | --- | --- |
| Owner | WinSell leadership | Sets strategy, manages billing and members, controls org-level security settings |
| Maintainer | Members of the `winsell-vn/maintainers` team | Merges pull requests, manages issues, reviews changes, administers releases |
| Contributor | Anyone who opens a pull request | Proposes changes, reports issues, participates in discussions |

Membership of the `maintainers` team is granted by an owner. The current
roster is visible on the
[team page](https://github.com/orgs/winsell-vn/teams/maintainers).

## Decision making

Most decisions are made through pull request review by a maintainer. A change
is accepted when it has at least one approving maintainer review and a green
CI run.

- **Routine fixes** — a maintainer may merge directly after CI passes.
- **Features and schema changes** — need a maintainer review plus an issue or
  design note describing the problem being solved.
- **Breaking API changes** — need a written migration plan in the pull request
  and a minor version bump at minimum.
- **Releases and publishing** — a maintainer or an owner performs the publish
  step. No automated workflow may publish a release without one.

When maintainers cannot reach agreement, an owner breaks the tie.

## Code ownership

The default `CODEOWNERS` file assigns every path to
`@winsell-vn/maintainers`. A repository may narrow this further — for example,
requiring a second reviewer for `prisma/schema.prisma` or for anything under
`Backend/src/modules/auth/`.

## Changes to these defaults

Changes to this repository — the organization-wide defaults, starter workflows
and community health files — are made through pull requests here, with the same
review rules as any other repository. A change that affects every repository in
the organization should explain which repositories it changes behaviour for.

## Security

Vulnerabilities are handled privately. See [SECURITY.md](SECURITY.md) for the
reporting process and the response targets that apply organization-wide.

## Code of conduct

Participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
