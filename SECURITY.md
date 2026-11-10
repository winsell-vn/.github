# Security Policy

WinSell takes security seriously. We run open-source products that handle
content pipelines, API keys and traffic, so we treat reports with care and
respond fast.

## Supported versions

Only the latest released version of each repository receives security fixes.
We do not backport patches to old release lines.

| Version | Supported |
| --- | --- |
| latest release | ✅ |
| older releases | ❌ |

## Reporting a vulnerability

**Please do not open a public issue, discussion or pull request for a
vulnerability.**

Report privately through GitHub Security Advisories:

- **social-hive** → [Report a vulnerability](https://github.com/winsell-vn/social-hive/security/advisories/new)
- **wisa-connect** → [Report a vulnerability](https://github.com/winsell-vn/wisa-connect/security/advisories/new)
- **Any other repository** → [Report a vulnerability](https://github.com/winsell-vn/.github/security/advisories/new)

If advisories are unavailable for a repository, email
**security@winsell.vn** with the details and encrypt the message if you prefer
(PGP key on request).

Include as much of the following as you can:

- type of issue (authentication bypass, injection, privilege escalation, etc.)
- affected repository, version or commit
- steps to reproduce, ideally a minimal proof of concept
- impact: what an attacker gains
- any known mitigations

## What to expect

| Stage | Target |
| --- | --- |
| Acknowledgement | within 3 business days |
| Triage and severity assessment | within 7 business days |
| Fix released | depends on severity; critical issues are expedited |
| Public advisory | after a fix is available, credit given to the reporter unless anonymity is requested |

We will keep you updated while the report is being worked on. If a report is
declined, we explain why.

## Scope

In scope:

- authentication, authorization and session handling
- injection (SQL, command, template, XSS)
- insecure deserialization, file upload and path traversal
- secret exposure
- SSRF and privilege escalation between tenants

Out of scope:

- findings that require an already-compromised host
- denial of service through volumetric abuse
- reports against third-party dependencies without a demonstrated impact on our code
- missing hardening headers with no exploitable consequence

## Hardening already in place

- Secret scanning and push protection enabled on public repositories
- Dependabot alerts and automated security updates
- `robots`-and-crawler-aware UGC link handling (`rel="ugc nofollow noopener noreferrer"`)
- File upload validated by magic bytes, not by MIME type
- JWT access tokens with short TTL plus rotating refresh tokens in HttpOnly cookies
- Optional TOTP 2FA and Cloudflare Turnstile on registration/login

## Security updates

Security fixes ship as a patch release with a CVE where applicable and are
announced in the repository's releases page.
