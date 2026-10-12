# Card-writing guidelines (applied to every deck)

Sources: Wozniak, *Twenty Rules of Formulating Knowledge* (supermemo.com); SuperMemo wiki,
*Minimum information principle*; Matuschak, *How to write good prompts* (andymatuschak.org/prompts).

## Rules (most important first)

1. **Atomic: one fact or idea per card.** If the answer has several independent parts
   (a list, "X, Y and Z", "define A and explain B"), split it into separate cards. One
   question → one retrievable answer, so each review "lights the same bulbs".
2. **Short answers.** Aim for at most ~25 words / 1–3 short lines in `back`. Hard limit: about 60
   words of plain text. Anything longer gets split or trimmed, or the nice-to-know part moves to `extra`.
3. **Precise, unambiguous prompts.** The question should have exactly one acceptable answer.
   Give context in the prompt ("In Kubernetes, …", "In TOGAF ADM, …") when the topic alone would leave it open.
4. **No sets or long enumerations.** Don't ask "List the 7 X". Instead use (a) a cloze per
   item with the rest of the list visible as context, (b) "Which X does Y?" cards per item, or (c) when
   the set itself matters, a short mnemonic plus one cloze per element. Up to 3–4 items is acceptable
   when the items only make sense together (e.g. the three CAP properties).
5. **Understand before memorizing: ask why and how, not just what.** Prefer "Why does X happen?",
   "When would you choose X over Y?" and "What breaks if…?" over pure definitions. Keep definitions
   only for core vocabulary.
6. **Cloze for definitions and facts inside context.** Use one `{{c1::…}}` deletion per idea. Several
   deletions (c1, c2) in one note are fine when each makes its own good card.
7. **Analogies and imagery.** Add a short, vivid analogy (in the `analogy` field, 1–2 sentences)
   where it really helps understanding or memory. Analogies must be *accurate*. Don't force one onto
   every card: aim for the cards where an abstract idea needs a concrete hook.
8. **Interference: tell look-alikes apart.** When two concepts get confused (e.g. liveness vs readiness
   probe), add a contrast card ("X vs Y: key difference?").
9. **Redundancy is OK, duplication is not.** Two cards on the same fact from different angles
   (cause → effect and effect → cause) are fine. Two cards asking the same question are not: merge them.
10. **High signal only.** Delete cards that don't help on the job or in the exam the deck is for:
    book/author/publication trivia ("written in 1999 by…", "which edition…", "who wrote…"),
    "what does chapter N cover", deck-meta cards, history trivia with no lesson in it, and marketing
    fluff. Keep history only when it explains *why* something is the way it is.
11. **Visual formatting.** Use short HTML: `<b>` for the key term, `<br>` for line breaks,
    `<ul><li>` for at most 3–4 bullets, `<code>` for commands, flags and identifiers. No walls of
    text. Leave MathJax `\( \)` as it is.

## Field semantics (unified note types)

| field     | purpose |
|-----------|---------|
| `front`   | the question (basic) |
| `back`    | the minimal answer |
| `text`    | cloze text with `{{c1::...}}` (cloze type only) |
| `extra`   | optional context: an example, "in practice", a pitfall. Keep short (≤ ~50 words); use `<b>Label:</b>` prefixes |
| `analogy` | optional 1–2 sentence analogy / mental image |
| `image`   | optional `<img src="file.svg">`; only reference files that exist in `media/` |
| `source`  | short context label (chapter / exam / module), e.g. `CKA · Networking` |
| `tags`    | list of hierarchical tags, `::` separated, no spaces |
| `deck`    | full deck path, e.g. `Kubernetes::03 Networking` |
| `reverse` | `true` → also generate an image/back→front card (for visual notation only) |
| `guid`    | keep the original guid when a note is kept or edited; when a note is split, the first part keeps it and the others get `null` |
