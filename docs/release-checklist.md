# Release Checklist

Before making a public release:

- `README.md` explains what the project is and what it is not.
- `LICENSE` is present.
- `SKILL.md` stays concise and agent-facing.
- Examples are synthetic, permission-safe, and do not expose user drafts.
- No API key, token, model prompt, cloud credential, payment key, database export, or user data is committed.
- Public language avoids detector-evasion claims.
- `python3 scripts/validate_repository.py` passes.
- GitHub repository description and topics match the public positioning.

Recommended topics:

```text
ai-writing
writing-assistant
codex-skill
prompt-engineering
academic-writing
chinese-english
tonekeep
```

