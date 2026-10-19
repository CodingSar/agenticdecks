# Brief for new-deck writer agents

You are writing a brand-new Anki deck in /home/user/agenticdecks for one learner: a curious cloud/enterprise architect
who wants a solid, lasting general education in the subject. Match the existing decks in style and depth.

Read first: `work/GUIDELINES.md` (card rules + field schema). Then skim two existing decks for tone and layout, e.g.
`work/out/Adaptive_Systems.json` and `work/out/Physics_for_Datacenters.json` (short backs, analogy box, `extra` with
`<b>Label:</b>` prefixes, cloze for lists, contrast cards, `source` as a short context label).

## What a good card is here
- **Understanding over trivia.** Ask *why* a movement/idea/law arose, *how to recognise* it, *what it reacted against*,
  *what followed from it*, and *how to tell look-alikes apart*. Pure dates, birthplaces and patrons are out unless the
  date/name is the vocabulary people actually use (e.g. "1789", "Bauhaus", "Newton's 2nd law").
- **Anchors, not catalogues.** Name 1–3 canonical works/people per movement as recognisable anchors; don't list ten.
- **Atomic.** One idea per card; backs ≤ ~25 words (hard max 60). Lists become one cloze deletion per item.
- **Analogies** in the `analogy` field for 20–30% of cards, where an abstract idea needs a concrete hook. Accurate only.
- **Contrast cards** ("Baroque vs Rococo: how to tell?") for every pair that's commonly confused.
- **Abbreviations:** write `full name (ABBR)` on first use on every card (cards are seen alone); see GUIDELINES rule 11.
- **Formulas** in MathJax `\( \)`, physics only where the formula *is* the idea.
- **Images:** no downloaded or copyrighted images. You may draw simple, clean SVG diagrams yourself (≤ 20 KB each,
  legible on a white background, 600×400-ish, dark strokes, a little colour) and save them to `media/<prefix>_<name>.svg`,
  referenced as `<img src="...">` in `image`. Use them where a picture carries the idea (an arch type, a column order, a
  vault, a wave diagram, a circuit, a chord progression on a staff is fine as text instead). 0–15 per deck is right.
- **Size:** 150–220 notes, in 8–12 subdecks (`Deck::01 Topic`), ordered chronologically or from fundamentals upward.
- `source`: a short period/era/topic label (e.g. "Baroque · 1600–1750", "Mechanics"). `tags`: hierarchical, no spaces.
- `guid`: `null` for all notes (new deck).

## Output (only write these files)
- `work/out/<OutputName>.json` = `{"deck_name": ..., "file": "<OutputName>.apkg", "description": "<1–2 sentence HTML description>", "notes": [...]}`
  Every note carries all schema keys (`guid,type,deck,tags,front,back,text,image,analogy,extra,source,reverse`).
- `work/out/<OutputName>.changelog.md` = 10–20 lines: scope, subdeck outline, what you deliberately left out, and any
  overlap with existing decks you avoided.
Generate the JSON from a Python script in your scratchpad folder (hand-written dicts). Then run
`python3 tools/check.py work/out/<OutputName>.json` until **0 errors** and no long-answer warnings.
Don't run build.py, don't touch other files, don't commit. Final reply: 5 lines — notes, subdecks, analogies, images, overlaps avoided.
