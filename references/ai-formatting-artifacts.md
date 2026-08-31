# Formatting And Attribution Artifacts

Use this reference for Markdown, pasted chat output, headings, bullets, citations, quotations, and documentation prose. Keep formatting that serves the reader or is required by the target venue.

## Formatting Signals

| Pattern | Severity | Better move |
| --- | --- | --- |
| Excessive bold labels in bullets | high | Use plain bullets or integrate the points into prose. |
| Repeated `**Label:** explanation` bullets | high | Combine related points or use content-specific headings. |
| Too many headings in short text | medium | Remove headings or keep one meaningful heading. |
| Generic headings: `Overview`, `Key points`, `Conclusion`, `Takeaways` | medium | Use a specific heading or no heading. |
| Emoji in professional prose | medium | Remove unless the user's real style calls for it. |
| Horizontal rules between ordinary sections | medium | Use normal section flow. |
| Markdown tables for content that is not comparative | medium | Use prose or bullets. |
| Repeated em dashes for artificial polish | medium | Use a sentence, comma, colon, or parenthesis where clearer. |
| Title Case everywhere | low | Use sentence case unless the target style requires otherwise. |

## Chatbot Residue

Remove these from final prose unless they belong in a real email or dialogue:

- `Of course!`, `Certainly!`, `Great question`, `Here is an overview`, `I hope this helps`.
- `Would you like me to …`, `Let me know if …`, `As an AI language model`.
- `当然可以`, `以下是`, `下面是`, `希望这对你有帮助`, `如果你需要，我可以 …`.
- `as of my last update` or similar knowledge-cutoff language; replace only with verified, dated information.

## Source And Attribution Tells

- Vague authorities: `experts argue`, `observers have noted`, `industry reports suggest`.
- Lists of media outlets without a claim, quotation, or finding.
- Plausible but unsourced dates, studies, statistics, quotations, and names.
- `information is limited` followed by invented or speculative detail.

Better move: name a supplied source, narrow the statement, mark it for verification, or leave the uncertainty visible. Never fill the gap with plausible details.

## Code And Documentation

- In stable documentation, describe current behavior rather than narrating what a change did.
- Delete comments that only restate obvious code; keep comments explaining intent, constraints, or edge cases.
- Use domain-relevant examples rather than endless `foo/bar` placeholders when examples help.
- Do not add an exhaustive checklist to a tiny task; retain only the reader's real decisions.

## Cleanup Checklist

1. Remove assistant prefaces and sign-offs.
2. Collapse repeated label-style bullets and generic headings.
3. Verify or flag sources, dates, names, quotations, and claims.
4. Normalize punctuation only for the target publication or style.
5. Preserve quotations, citations, data, code, and required format unless the user asks to change them.
