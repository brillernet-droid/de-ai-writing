# Security Policy

This public repository is a lightweight Codex skill. It should not contain API keys, model provider secrets, user data, production prompts, payment callbacks, database credentials, or private ToneKeep product logic.

## Reporting A Problem

Open a GitHub issue if you find:

- a leaked secret or credential;
- private user text committed by mistake;
- instructions that encourage falsifying citations, sources, or personal details;
- wording that presents style signals as proof of AI use;
- unsafe handling of medical, legal, financial, or policy text.

Do not paste live secrets into an issue. Describe the file and line, then rotate the secret immediately if it was ever public.

## Maintainer Checklist

- Keep production keys in server-side environment variables only.
- Keep user history, feedback, training samples, and billing data out of this public repo.
- Run `python3 scripts/validate_repository.py` before release.
- Review public examples for privacy and factual safety.

