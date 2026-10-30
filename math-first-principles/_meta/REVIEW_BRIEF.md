# Reviewer brief (pass 2)

You are reviewing and improving drafted layers of a first-principles Mathematics knowledge base. Read `PLAN.md` (including §8 Lessons), `WRITER_BRIEF.md`, `TAXONOMY.md` and `REVIEW_NOTES.md` first. The drafts were written by other agents. Your job is to make your layers **correct, essential and well connected**.

## Your tasks, in order

1. **Fact-check.** Read every file in your layers. Check every theorem statement and its hypotheses, every date, attribution and citation, and every number. Treat the items listed for your layers in `REVIEW_NOTES.md` as known suspects, but do not stop there. Correct anything wrong. Where a date or attribution is uncertain, drop it rather than keep a precise-looking wrong one. A citation you cannot vouch for (author, title and year) is removed or replaced with a canonical one.
2. **Fix structural errors.** Run `python3 -B _meta/check.py <your layer prefixes>`. Fix every `UPWARD` (a "Builds on" link to a higher layer: move it to body text or to "Enables", or replace it with the correct lower-layer prerequisite), `CYCLE` (remove the "Builds on" link that runs against taxonomy order), `SECTION`, `MISSING`, `EXTRA`, and every `LINK` or `ANCHOR` error. Anchors into `CROSS-CUTTING.md` must be from the list in `WRITER_BRIEF.md`.
3. **Write the new leaves** that `TAXONOMY.md` now lists in your layers and that do not yet exist (the checker reports them as `MISSING`). Follow the leaf template exactly. Then update the parent `README.md` (Children line, children table and narrative) and, if needed, the layer README, so that the new leaf is woven in. Add links to the new leaf from the 2–4 existing leaves that most need it.
4. **Essence check.** For each leaf ask: are the Core tenets the load-bearing ideas an expert would name first? If a crucial tenet is missing, add it. If a tenet is trivia, cut or replace it. Keep leaves within the length limits.
5. **Connection check.** Each parent README must explain how its children relate to one another and connect to **every** sibling directory under the same parent. Each layer README must cover its meaningful neighbouring layers. Fix gaps. Make sure "Siblings" bullets in leaves are accurate.
6. **Consistency.** The same fact must have the same value everywhere, and the same object the same name and notation. If you find a statement in *another* layer that contradicts yours, report it instead of editing that file.
7. **Abbreviations.** Each abbreviation is spelled out on first use in body text in each file.

## Limits

- Edit only files in your assigned layers. Do not touch the root `README.md`, `CROSS-CUTTING.md` or `_meta/`.
- Do not run git commands.
- Do not rename or delete taxonomy files.

## Final report

Report briefly: files changed, new leaves written, the factual corrections you made (one line each: file, wrong → right), any cross-layer contradiction you found, and anything left unresolved. Do not paste file contents.

## Mathematics-specific checks

- **Exact statements.** Every theorem is stated with all its hypotheses. Where a hypothesis is dropped "for simplicity", the file says so. A "for all" that is really "for almost all", or an "if" that is really "if and only if", is fixed.
- **Proof ideas.** Every Core tenet says why its claim is true, or what breaks without it. A tenet that only states a fact gets its reason, or is replaced.
- **Status and dates.** Open problems carry "open as of 2026"; recent results carry the year of proof and, where it differs, of publication. A conjecture is never stated as a theorem, and a result proved only under a hypothesis (the Generalised Riemann Hypothesis, the axiom of choice, large cardinals) says so.
- **Notation.** Unicode only: clear every `NOTATION` warning. Symbols are defined on first use, and the same symbol means the same thing within a file.
- **Length and order.** Clear every `LENGTH` warning and every `CYCLE` error in your layers.
