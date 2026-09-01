# ToneKeep De-AI Writing Skill

`de-ai-writing` is a bilingual Codex skill for revising Chinese and English prose that reads too machine-like, over-defensive, or unsupported. It helps an AI assistant diagnose style signals and rewrite the text while preserving the author's facts, citations, terminology, register, and intended stance.

This repository is the public skill edition of ToneKeep. It is intended to share the method and let others use a lightweight writing workflow. It does not contain ToneKeep's private web product backend, scoring logic, payment logic, training data, RAG database, model prompts, or user data system.

Try the ToneKeep web beta: https://briller-web-293031-7-1435053784.sh.run.tcloudbase.com/

## What It Does

- Flags AI-like wording, formulaic structure, chatbot residue, and over-polished rhythm.
- Reduces unnecessary defensive writing without deleting real uncertainty.
- Keeps academic, technical, medical, legal, financial, and policy text source-safe.
- Supports voice matching from a user-supplied sample.
- Handles Chinese, English, and Chinese-English translation cleanup.

## What It Is Not

- Not a formal AI detector.
- Not a plagiarism checker.
- Not a guarantee that writing will pass any detector.
- Not a tool for fabricating citations, anecdotes, personal details, errors, or "human quirks".
- Not the full ToneKeep SaaS product.

## ToneKeep Web Beta

The public web beta lets non-technical users paste text, run AI-style diagnosis, and test natural rewriting without installing this skill. The web product is separate from this repository and keeps production logic on the server side.

Use the web beta for product feedback. Use this repository to inspect or install the lightweight skill workflow.

## Repository Structure

```text
de-ai-writing/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── ai-lexicon.md
│   ├── ai-structure-patterns.md
│   └── ai-formatting-artifacts.md
├── examples/
├── docs/
└── scripts/
```

## Installation

Clone this repository into your Codex skills directory:

```bash
git clone https://github.com/brillernet-droid/de-ai-writing.git ~/.codex/skills/de-ai-writing
```

Restart Codex or refresh your skill list. Then invoke it with:

```text
Use $de-ai-writing to rewrite this paragraph so it sounds less like AI while preserving the factual claims.
```

If you do not use Codex skills directly, you can still read `SKILL.md` as a structured editing guide.

## Usage Examples

Audit only:

```text
Use $de-ai-writing in audit mode. Tell me which phrases, structure choices, or formatting artifacts make this sound AI-written.
```

Academic-safe rewrite:

```text
Use $de-ai-writing academic-safe mode. Keep the statistical claims, citations, and formal register, but reduce AI-like structure and vague importance claims.
```

Voice match:

```text
Use $de-ai-writing voice-match mode. First infer my writing habits from Sample A, then revise Draft B without making it generic.
```

Translation cleanup:

```text
Use $de-ai-writing translation-naturalise mode. Rewrite this Chinese-to-English translation so it follows natural English argument logic.
```

See `examples/` for before-and-after cases.

## Design Principles

The skill uses four practical passes:

1. Precision pass: remove defensive padding and calibrate claims.
2. De-AI pass: remove stock phrasing, template structure, and chatbot residue.
3. Authorship pass: restore the author's own logic, rhythm, and evidence.
4. Source pass: flag unsupported claims instead of inventing replacements.

The key rule is simple: make the writing more authored, not artificially messy.

## Public And Private Boundary

This public repository intentionally includes only the lightweight skill instructions and reference guides. The following should remain private in any commercial ToneKeep product:

- detailed scoring weights and ranking logic;
- production prompts and model-routing strategy;
- user profile, history, billing, and quota logic;
- private training samples and feedback data;
- payment callbacks, keys, and cloud deployment configuration.

## For Maintainers

Run the repository validation check before publishing changes:

```bash
python3 scripts/validate_repository.py
```

This checks required files, basic Markdown links, and common secret patterns.

## Roadmap

- More examples for academic abstracts, grant text, emails, personal statements, and Chinese business copy.
- More conservative source-safe patterns for research and medical writing.
- Optional scanners for local phrase and structure checks.
- Public documentation for using the skill in writing education and product demos.

## License

MIT License. See `LICENSE`.
