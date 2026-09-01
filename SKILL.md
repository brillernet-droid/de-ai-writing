---
name: de-ai-writing
description: Revise Chinese or English prose to remove AI-like wording, formulaic structure, chatbot residue, and unnecessary defensive writing while preserving the author's voice, facts, citations, terminology, and evidence-based uncertainty. Use when the user asks to 降 AI, 去 AI 味, humanize writing, make text sound less like ChatGPT, remove generic AI phrasing, edit overly polished prose, reduce caveats, or rewrite academic, business, product, email, or translated copy more naturally.
---

# De-AI Writing Editor

## Objective

Make the writing sound authored: specific, purposeful, rhythmically natural, and appropriate to its genre. Edit for three independent failures:

1. **Defensive writing** — apology-like caveats, self-undermining claims, negative framing, and explanation added only to pre-empt imagined criticism.
2. **AI-like writing** — stock vocabulary, generic structure, empty emphasis, over-balanced sentences, chatbot formatting, and uniformly polished rhythm.
3. **Ungrounded writing** — vague authorities, unsupported specificity, literal translation, and generic claims that conceal the writer's actual evidence or point of view.

Do not optimise for detector scores. Do not fabricate anecdotes, citations, sources, personal details, quirks, or errors. Preserve all facts, numbers, technical terms, intended stance, and material uncertainty.

This is the public skill edition of ToneKeep. It documents a lightweight writing workflow and must not include private production prompts, scoring weights, model-routing logic, user data, payment logic, or training samples.

## Modes

- `rewrite` — default. Return a ready-to-use revision.
- `audit` / `detect` — flag the signals without rewriting.
- `edit` — edit a supplied file in place only when the user explicitly asks for a file edit.
- `voice-match` — use a supplied writing sample to preserve the author's vocabulary, rhythm, paragraph openings, punctuation, and degree of warmth.
- `academic-safe` — use for papers, abstracts, grants, peer-review responses, and medical or technical text. Preserve the field's formal register and calibrate every claim to its evidence.
- `translation-naturalise` — rewrite Chinese–English or English–Chinese translation so it follows the target language's normal argument and sentence logic rather than mirroring the source line by line.
- `source-safe` — flag claims, attributions, dates, quotations, or citations that cannot be supported from the supplied material; do not invent replacements.

## Editing Intensity

- `light` — make local wording, rhythm, and formatting edits; preserve the original structure.
- `standard` — default. Remove repeated AI-like and defensive patterns, then improve local structure where needed.
- `structural` — rebuild paragraph order or argument shape when the existing structure is generic, repetitive, or misaligned with the genre.

If the draft is already natural and fit for purpose, make only light edits. Do not manufacture variation merely to make the text look less polished.

## Protected Material

Do not alter quoted language, citations, reference details, numerical results, statistical notation, code, table cells, legal labels, medical instructions, or required reporting language unless the user explicitly asks. If a quotation needs to be rewritten, offer a clearly labelled paraphrase rather than silently changing the quoted text.

## Workflow

1. Identify the genre, audience, target language, and requested mode. If a voice sample is supplied, infer its real habits before revising.
2. Map each paragraph's job: claim, evidence, explanation, limitation, implication, request, or transition.
3. Run the **precision pass**:
   - Delete defensive disclaimers that add no evidence, scope, logic, or reader guidance.
   - State scope positively: what the text examines, covers, compares, or decides.
   - Keep every limit that affects validity, interpretation, safety, legality, ethics, or correct use.
   - Replace stacked modal hedges with the actual source of uncertainty: population, time frame, design, missing estimate, or evidence quality.
4. Run the **de-AI pass**:
   - Replace or cut generic phrases only when they are vague, repeated, unsupported, or unnatural for the genre.
   - Remove throat-clearing, self-praise, abstract importance claims, template openings, and generic future promises.
   - Prefer actors, mechanisms, objects, dates, evidence, and specific consequences.
   - Break formulaic symmetry and vary sentence and paragraph length according to the work each part does.
   - Remove chatbot prefaces, sign-offs, and over-organised formatting.
5. Run the **authorship pass**:
   - If a writing sample is supplied, retain its observable habits: sentence length, plain-word preference, transitions, punctuation, degree of warmth, and treatment of uncertainty.
   - Replace generic abstractions with supplied actors, evidence, scenes, decisions, mechanisms, or consequences.
   - If the draft lacks a needed personal or concrete detail, flag the gap or use a clearly marked placeholder. Never invent it.
6. Run the **source pass**:
   - Replace vague attributions such as `experts argue` or `studies show` only when a supplied source supports the replacement.
   - Flag unsourced dates, quotations, studies, names, and statistics for verification. Do not make factual claims sound firmer merely because the prose is cleaner.
7. Rebuild the argument around an appropriate structure: claim-first, evidence-first, problem–constraint–choice, finding–limitation–meaning, objection–answer, or chronology.
8. Run the **calibration pass** and return the requested output.

## Precision And Claim Calibration

| Situation | Write | Do not write |
| --- | --- | --- |
| Scope | `The analysis focuses on …` / `分析聚焦于……` | `This paper does not claim to cover …` |
| Observational result | `was associated with`, `indicates`, `与……相关` | `causes`, `proves`, `决定了` |
| Trial result | `improved the outcome in this sample`, `在本样本中改善了……` | `guarantees`, `proves for all settings` |
| Limited evidence | `suggests`, `is consistent with`, `supports further testing` | `may possibly perhaps suggest` |
| Missing evidence | state what is unknown and why | use confident language to hide the gap |

Place necessary limitations once, where readers need them. Do not scatter the same caveat through the title, abstract, introduction, results, and conclusion.

## Genre Rules

### Academic, technical, medical, legal, financial, or policy text

Keep the accepted register and required terminology. Preserve methodological qualifications, eligibility criteria, warnings, contraindications, reporting limits, and uncertainty that could alter a reader's decision. Do not turn association into causation or make a conclusion broader than the supplied evidence.

### Business, product, and policy copy

Replace empty praise such as `robust`, `seamless`, `transformative`, `赋能`, or `高质量` with the feature, process change, metric, or user outcome that justifies it.

### Chinese–English translation

Preserve the author's logic and degree of directness, then rebuild sentences for the target language rather than translating word by word. In English, restore a clear subject and main verb, reduce stacked noun phrases, and replace generic importance claims with the actual finding or action. In Chinese, avoid rigid translation of English subject chains, excessive passive constructions, and corporate-deck wording. Preserve named entities, terminology, citations, numbers, and deliberately distinctive phrasing.

### Emails and professional messages

State the decision, request, or boundary in the first two sentences. Keep only the context the recipient needs to act.

## Pattern Reference

Read [AI-ish lexicon](references/ai-lexicon.md) for phrase-level diagnosis, a long text, or a request to add an AI-like word or phrase to the rule set.

Read [AI-ish structure patterns](references/ai-structure-patterns.md) when paragraphs feel too smooth, generic, repetitive, or template-driven.

Read [Formatting and attribution artifacts](references/ai-formatting-artifacts.md) when the text includes Markdown, headings, bullets, citations, quotations, documentation prose, or pasted chat output.

Treat individual flags as editing signals, not automatic bans. A cluster of signals is stronger evidence than one word, transition, heading, or em dash. Use the severity labels as follows: `high` usually merits revision unless terminology requires it; `medium` merits revision when repeated, vague, or unsupported; `low` is context-dependent.

When the user asks to record a new phrase, structural pattern, or formatting tell, make the smallest useful update to the relevant reference file. Include why it can sound AI-like and when it may still be appropriate.

## Voice Calibration

When the user supplies a writing sample, derive a compact in-session profile before rewriting:

- preferred sentence length and paragraph shape;
- plain or technical vocabulary level;
- recurring sentence openings and transition habits;
- punctuation, formatting, and use of first person;
- how the writer expresses certainty, uncertainty, warmth, and disagreement.

Use the profile as positive guidance, not a disguise. Do not imitate a living writer's distinctive voice beyond the user's supplied samples, and do not store private samples in the public repository.

When no sample is supplied, default to clear, specific prose with a natural cadence. Do not add humor, slang, contractions, personal stories, or deliberate imperfections unless the genre supports them.

## Source-Safe Editing

Treat prose cleanup and factual verification as separate jobs. When sources are supplied, check whether the draft's claim matches them. When they are not supplied, flag rather than guess:

- vague collective authorities (`experts`, `observers`, `research`);
- exact dates, figures, studies, quotations, and names without a source;
- generic significance claims that do not identify a consequence;
- speculative detail following an acknowledged information gap.

## Output

For `rewrite`, return clean revised text. Add a short note only when an edit changed claim scope or a material limitation was retained.

For `audit`, group no more than eight findings under: **phrasing**, **structure**, **formatting**, and **precision**. Label them as signals, not proof of AI use.

For `voice-match`, return the revision followed by up to three brief observations about the retained voice. Do not imitate a supplied sample beyond its observable style.

For `source-safe`, return a concise issue list with: **claim or phrase**, **why it needs support**, and **safe edit or verification step**. Do not substitute an invented source or fact.

For `edit`, update only the requested file and report the edited path. Preserve unrelated content and formatting.

## Final Check

Before delivering, verify that the revision:

- starts with substance rather than generic context, apology, or chatbot framing;
- states what is true or in scope before what is not;
- keeps material uncertainty and removes only defensive padding;
- uses concrete actors, mechanisms, evidence, and consequences where available;
- does not repeat a template structure, transition ladder, or symmetrical sentence shape;
- leaves quotations, facts, citations, and technical content intact unless a change was explicitly requested;
- preserves the intended register and reads like a person wrote it for this situation.
