# Brief: abbreviation writer

The learner does not yet know the abbreviations. Anki shows each card alone, in random order, so every card must be
self-contained: write **"full name (ABBR)"** the first time an abbreviation appears on a card, then the bare ABBR afterwards
on that same card.

Input: `work/out/<Deck>.json` and a reader's report at the scratchpad path you were given
(`{"abbreviations": {"MMU": {"expansion": "memory management unit", ...}}}`). The report is a starting point, not
the truth: verify every expansion, add abbreviations the reader missed, and skip ones that are universally known
(see the whitelist in `work/ABBREV_READER_BRIEF.md`).

## Rules
1. Per note, expand the **first occurrence** in reading order: `front` (or `text` for cloze) → `back` → `extra`.
   Later occurrences on the same note stay abbreviated.
2. **Never leak the answer.** If the card's answer is the expansion itself, or the front would give away the back by
   naming the concept, expand in `back` instead of `front`. For cloze, never put the expansion inside `{{c1::...}}`
   when the deletion is the abbreviation; expand outside the braces, or in `extra` if it would spoil the deletion.
3. Form: `memory management unit (MMU)`; keep proper-noun capitalisation (`Portable Operating System Interface (POSIX)`).
   For plurals/possessives: `translation lookaside buffers (TLBs)`. Inside `<code>` tags, leave the token alone and expand
   it in prose nearby instead.
4. If a card already expands it in any phrasing ("the TLB, a cache of translations"), leave that card alone.
5. Keep backs within the length rule (≤ ~60 words). If an expansion pushes a back over, move a clause to `extra`.
6. Don't change anything else. Keep guids. Keep HTML and MathJax intact.
7. Implement as a Python script (regex over the four fields with word boundaries, skipping `<code>…</code>`,
   `{{c…}}` interiors, `<img …>` and attributes), driven by a hand-verified `{ABBR: expansion}` map plus a per-note
   exception list for rule 2. Dump with `indent=1, ensure_ascii=False`. Then re-read ~30 random changed notes to check
   they read naturally, fix the map/script, re-run.
8. Run `python3 tools/check.py work/out/<Deck>.json` → 0 errors. Append `## Abbreviations expanded` with the final
   `ABBR → expansion` list and the number of notes touched to `work/out/<Deck>.changelog.md`.
Don't run build.py, don't commit, don't touch other decks. Final reply: notes touched, abbreviations in the map, any
you deliberately left bare and why.
