# Reviewer brief (pass 2)

You are reviewing and improving drafted layers of a first-principles Medicine knowledge base. Read `PLAN.md` (including §8 Lessons), `WRITER_BRIEF.md`, `TAXONOMY.md` and `REVIEW_NOTES.md` first. The drafts were written by other agents. Your job is to make your layers **correct, essential and well connected**.

## Your tasks, in order

1. **Fact-check.** Read every file in your layers. Check every number, date, attribution, theorem statement and citation. Treat the items listed for your layers in `REVIEW_NOTES.md` as known suspects, but do not stop there. Correct anything wrong. Where a figure is uncertain, give a safe range or drop the figure rather than keep a precise-looking wrong number. A citation you cannot vouch for (author, title and year) is removed or replaced with a canonical one.
2. **Fix structural errors.** Run `python3 _meta/check.py <your layer prefixes>`. Fix every `UPWARD` (a "Builds on" link to a higher layer: move it to body text or to "Enables", or replace it with the correct lower-layer prerequisite), `SECTION`, `MISSING`, `EXTRA`, and every `LINK` error that is not into `CROSS-CUTTING.md`. Anchors into `CROSS-CUTTING.md` must be from the list in `WRITER_BRIEF.md`.
3. **Write the new leaves** that `TAXONOMY.md` now lists in your layers and that do not yet exist (the checker reports them as `MISSING`). Follow the leaf template exactly. Then update the parent `README.md` (Children line, children table and narrative) and, if needed, the layer README, so that the new leaf is woven in. Add links to the new leaf from the 2–4 existing leaves that most need it (for example, link a new leaf on sepsis from shock, fever and critical care).
4. **Essence check.** For each leaf ask: are the Core tenets the load-bearing ideas an expert would name first? If a crucial tenet is missing, add it. If a tenet is trivia, cut or replace it. Keep leaves within the length limits.
5. **Connection check.** Each parent README must explain how its children relate to one another and connect to **every** sibling directory under the same parent. Each layer README must cover its meaningful neighbouring layers. Fix gaps. Make sure "Siblings" bullets in leaves are accurate.
6. **Consistency.** The same fact must have the same value everywhere. If you find a statement in *another* layer that contradicts yours, report it instead of editing that file.
7. **Abbreviations.** Each abbreviation is spelled out on first use in body text in each file.

## Limits

- Edit only files in your assigned layers. Do not touch the root `README.md`, `CROSS-CUTTING.md` or `_meta/`.
- Do not run git commands.
- Do not rename or delete taxonomy files.

## Final report

Report briefly: files changed, new leaves written, the factual corrections you made (one line each: file, wrong → right), any cross-layer contradiction you found, and anything left unresolved. Do not paste file contents.

## Medicine-specific checks

- **No clinical advice.** Remove doses, protocols and "first-line is X" lists unless they illustrate a mechanism. Keep International Nonproprietary Names (INN); remove brand names.
- **Dated figures.** Every prevalence, mortality or approval figure carries a year and, where relevant, a region. Replace a precise-looking figure you cannot vouch for with a safe range.
- **Disease leaves (layers 12–14)** trace mechanism → pathophysiology → symptoms and signs → test findings → what treatment reverses, citing lower-layer leaves rather than restating them, and name the other specialties involved.
- **Specialty parent READMEs (12–14)** have an "## Interfaces with other specialties" section that names real referral and hand-over relationships, with links.
