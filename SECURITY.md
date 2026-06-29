# Security Policy

## Reporting a vulnerability

If you discover a security vulnerability in `mypackage`, **please do not open
a public GitHub issue**. Public issues are visible to everyone and may give
attackers a head start.

Instead, use GitHub's **Private Vulnerability Reporting** feature:

- [Report a vulnerability](https://github.com/BenFlint123/validation_automation/security/advisories/new)

This creates a private draft advisory visible only to maintainers until a fix is coordinated.

## What to include in a report

To help us triage quickly, please include where possible:

- A description of the vulnerability and its potential impact.
- The affected version(s) or commit SHA.
- Steps to reproduce, or a minimal proof-of-concept.
- Any suggested mitigation.

## Response expectations

- **Acknowledgement:** within 5 business days of receiving the report.
- **Initial assessment:** within 10 business days.
- **Fix and disclosure:** timing depends on severity and complexity. We will
  coordinate disclosure with you and credit you in the release notes if you
  wish.

## Supported versions

`mypackage` is in early development (`0.x`). Only the latest released
version receives security fixes. Once a `1.x` line is published, this section
will be updated with a formal support window.

## Scope

This policy covers vulnerabilities in:

- The `mypackage` Python package source (`src/mypackage/`).
- The build, packaging, and CI/CD configuration in this repository.

Issues in third-party dependencies should be reported upstream to the relevant
project; please still let us know so we can apply mitigations or pin a fixed
version.
