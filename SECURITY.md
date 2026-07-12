# Security Policy

## No secrets in this repository

Every workflow in this repository has been sanitized before publication. The following are **stripped or blanked** from all `.json` files:

| Removed | Why |
|---|---|
| Credential IDs and values | Prevent leaking any linked credential |
| `meta.instanceId` | Not tied to any real n8n instance |
| `pinData` | May contain real records from test runs |
| Webhook path UUIDs | Replaced with `your-webhook-path` |
| `staticData`, `versionId`, `active` | Runtime/instance state |
| API keys, tokens, emails in parameters | Replaced with placeholders |

Credential slots are preserved **by type only** and labeled `Add your <service> credential`, so you know what to connect — but no secret material is present.

## Verification

You can confirm no secrets are present yourself:

```bash
# scan for common secret patterns — should return nothing
grep -rEn 'sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|ghp_[0-9A-Za-z]{36}|xox[baprs]-' workflows/
```

A CI check (`.github/workflows/validate.yml`) runs on every push and pull request to:
1. Validate every workflow is parseable JSON with a valid node graph
2. Fail the build if any credential-looking secret is detected

## Reporting a concern

If you believe a file contains sensitive data that slipped through sanitization, please **open a private security advisory** via the repository's **Security → Report a vulnerability** tab, or email the maintainer. Do not open a public issue for suspected secret exposure.

We aim to respond within 48 hours and remove any confirmed exposure immediately.

## Using these workflows safely

- Add your own credentials through n8n's credential manager — never hardcode keys into node parameters.
- Review any `Code` node before running it in production.
- Workflows with webhooks are inactive by default; set your own authentication before activating.
