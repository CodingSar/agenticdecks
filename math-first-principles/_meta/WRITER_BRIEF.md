# Writer brief

You are writing part of a first-principles knowledge base of Mathematics. Read [`PLAN.md`](PLAN.md) (why the tree has this shape) and [`TAXONOMY.md`](TAXONOMY.md) (every path that exists) first. The sibling projects [`../../cs-first-principles/`](../../cs-first-principles/README.md) and [`../../medicine-first-principles/`](../../medicine-first-principles/README.md) are finished and use the same templates; open two of their leaves (for example `cs-first-principles/01-mathematical-foundations/04-algebra/abstract-algebra.md` and `cs-first-principles/07-operating-systems/03-concurrency/deadlock.md`) to see the target quality and density.

## The reader

A capable, scientifically literate adult (think: an engineer, scientist or programmer) who wants the *essence* of each topic: what is true, why it is true, and how it connects to everything else. They can follow a definition, a formula and a short argument, but they are not a mathematician and should never need a textbook open to follow a file. They are learning how mathematics *thinks*: why a definition is the right one, which idea makes a proof work, and what a theorem buys.

## Rules for every file

1. **Create exactly the paths in `TAXONOMY.md`.** Do not add, rename or skip files. If you think the taxonomy is wrong, write the file anyway and add your suggestion to your final report.
2. **Abbreviations:** spell out each abbreviation on its first use *in each file*, then use the short form: "Zermelo–Fraenkel set theory with the axiom of Choice (ZFC)", then "ZFC". Every file may be the first one a reader opens. This includes common ones (Ordinary Differential Equation (ODE), Singular Value Decomposition (SVD), Central Limit Theorem (CLT), greatest common divisor (gcd)) in the first file where they appear in body text. Do not expand abbreviations inside headings. Symbols and standard function names (ℝ, sin, log, det, dim, ker) are notation and need no expansion; abbreviations read as words (gcd, lcm, ODE, PDE, ZFC) do. Write "if and only if", never "iff"; avoid "i.e.", "e.g." and "QED".
3. **Links are relative** and point only to paths in `TAXONOMY.md` (or `README.md` of a directory listed there, or `../CROSS-CUTTING.md`-style paths to the root files). Count the `../` carefully: a leaf at `12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-prime-number-theorem.md` links to `../../09-advanced-analysis/02-complex-analysis/cauchys-theorem-and-its-consequences.md`. A link into a sibling tree (from a leaf, `../../../cs-first-principles/...`) is allowed in the body and in "Enables", never in "Builds on"; check that the target exists before you link it.
4. **Proof idea over statement.** Every tenet explains *why* it is true: the idea that makes the proof work, and what breaks without each hypothesis. "ℝ is complete" is a label; "Every bounded increasing sequence of reals converges, because its terms are all below the least upper bound s, and for each ε > 0 some term exceeds s − ε, after which all terms do; in ℚ the sequence 1, 1.4, 1.41, 1.414, … is bounded and increasing but has no limit, because its limit would be √2" is a tenet.
5. **Accuracy is non-negotiable.** State theorems with their exact hypotheses. Distinguish a theorem from a conjecture, a heuristic and a definition. Date the status of open problems and recent results ("open as of 2026"; "proved by Perelman in 2002–2003"). No invented citations: cite only real, canonical works you are sure of (author, title, year). Attribute a theorem to a person and a year only where you are sure of both. Where you are unsure, leave the detail out and list it in your report.
6. **Plain, direct English.** Short sentences. Active voice. No filler, no marketing tone. British spelling by default (generalise, colour, programme, analyse, centre) except inside established names and taxonomy file names. Use a small worked example when it makes a tenet concrete. Use Markdown tables to compare things.
7. **Notation: Unicode, never LaTeX.** Every file must read correctly as plain text. Use ℕ ℤ ℚ ℝ ℂ, ∀ ∃ ¬ ∧ ∨ ⇒ ⇔, ∈ ∉ ⊆ ∪ ∩ ∅ ×, → ↦ ∘, ≤ ≥ ≠ ≈ ≅ ≡, ∑ ∏ ∫ ∂ ∇ √ ∞, Greek letters (ε, δ, π, λ), and superscripts and subscripts (x², xⁿ, aₙ); write x^(n+1) or a_(n+1) where no Unicode character exists. Put a formula longer than a line, or a derivation, in a fenced code block. Define every symbol the first time you use it. Markdown pitfalls: inside a table write an absolute value as `\|x\|` or ∣x∣ (a bare `|` ends the cell); write an inner product as ⟨x, y⟩, never `<x, y>`; write multiplication as `·` or `×`, never `*`. The checker warns (`NOTATION`) about LaTeX.
8. **Length.** Leaves: 500–1,100 words. Parent READMEs: 400–900 words. Layer READMEs (top-level `NN-*/README.md`): 600–1,200 words. Be dense, not long. The checker warns (`LENGTH`) about a file outside its limits.
9. **No front matter, no emoji, no HTML.** ASCII diagrams in fenced code blocks are welcome when they show structure (a lattice of subgroups, a commutative diagram, a chain of theorems, a phase portrait).

## Leaf template

```markdown
# <Title>

> **Layer:** [NN Layer name](<relative path to layer README>) › [Parent name](README.md)
> **Builds on:** [Topic](<rel path>), [Topic](<rel path>)
> **Enables:** [Topic](<rel path>), [Topic](<rel path>)

## Essence

One paragraph (3–6 sentences): what this is, the problem it solves or the question it answers, and the single idea that makes it work. A reader who reads only this paragraph should come away with the right mental model.

## Core tenets

1. **<Tenet stated as a claim.>** Two to four sentences of proof idea or mechanism: why it is true, what breaks without each hypothesis, what follows from it.
2. ...
(5–9 tenets. These are the heart of the file: the load-bearing ideas without which the topic is misunderstood.)

## Key concepts

| Term | Meaning |
|---|---|
| ... | ... |

(5–12 terms that the tenets rely on. Precise one-line definitions.)

## How it fits

- **Below:** what this topic takes from the layers beneath, and which assumption it relies on.
- **Above:** what higher layers build with it.
- **Siblings:** how it contrasts with or complements the other leaves in the same parent.

## Common misconceptions

- **"<Misconception>"**: why it is wrong, in one or two sentences.
(2–4 items.)

## Go deeper

- Author, *Title* (year): one phrase on why it is the right next read.
(2–4 canonical sources.)
```

Layer 15 has no parent directories, so its leaves have the Layer line `> **Layer:** [15 Mathematics in Context](README.md)`.

## "Builds on" and "Enables"

- **Downward only.** "Builds on" may only link to the same layer or lower layers. A related idea in a higher layer is mentioned in the body text with a link, or listed in "Enables", never listed as a prerequisite. The checker reports violations as `UPWARD`.
- **Counts.** "Builds on" and "Enables" each list 1–5 links to other leaves or READMEs, *anywhere* in the tree (cross-layer links are the point). At least one of them should cross a layer boundary.
- **The one upward exception: 00 may build on 01**, because the semantics of logic is written in sets. To keep the two roots free of cycles, it is used narrowly:
  - In 00, only `01-formal-logic/soundness-completeness-and-compactness.md` builds on 01, and only on `sets-and-set-operations.md`, `relations-and-orders.md` or `functions.md` (all three in `01-sets-and-foundations/01-sets-relations-and-functions/`). Of the other 00 files, only those in `03-the-axiomatic-method/` may build on that soundness leaf.
  - In 01, those three leaves build only on 00's `propositional-logic.md`, `predicate-logic-and-quantifiers.md` and the `02-methods-of-proof/` leaves, and on each other in taxonomy order.
- **No cycles.** Within a layer, prefer to build on files that come earlier in taxonomy order. Build on a later file only if it does not itself, directly or through others, build on yours; when in doubt, put it in "Enables". Countable sets and cardinal numbers each look like the other's prerequisite: countable sets comes first, so cardinal numbers builds on it, not the reverse. A valid forward edge: the inverse function theorem (06/03) builds on the contraction mapping principle (06/04), which builds on nothing in 06/03. The checker reports cycles as `CYCLE`.
- **Never list a leaf of a sibling tree in "Builds on".** The sibling trees have their own checkers and their own order.

## Theorems, conjectures and programmes

- **A leaf named after a theorem, or built around one**, states the theorem precisely once (every hypothesis, the conclusion), gives the proof idea in a tenet, shows what breaks without each hypothesis (with a counterexample), and says what the theorem is used for, with links.
- **An open problem or a research programme** (the Riemann hypothesis, the twin prime conjecture, the Langlands programme) says exactly what is known and since when, what would follow from a solution, and why it is hard. Never state a conjecture as a theorem, and date every status claim.
- **History in passing.** One clause on who found an idea and what problem forced it is welcome when it explains the idea. History for its own sake belongs in `15-mathematics-in-context/history-of-mathematics.md`.
- **Go deeper** lists canonical books and papers you are sure of, for example Walter Rudin, *Principles of Mathematical Analysis* (3rd edition, 1976). Prefer one classic and one modern or gentler text. Give a year only where you are sure of it.

## Parent README template (directories below the top level)

```markdown
# <Name>

> **Layer:** [NN Layer name](<rel path>) › <this node>
> **Children:** [Child](child.md) · [Child](child.md) · ...

## What this area is about

The question this area answers and the one idea that unifies its children (1–2 paragraphs).

## How the children fit together

Explain the internal logic: the order to read them, which child depends on which, and how together they make up the parent. A table (Child | Its role in the whole | Depends on) followed by a short narrative works well. An ASCII diagram is welcome if it shows real structure.

## Connections to sibling areas

For each sibling directory under the same layer: one short paragraph or bullet on how this area and that sibling connect (shared ideas, results one uses from the other, tension between their points of view). Link to the sibling's README.

## Connections across layers

What this area takes from lower layers and gives to higher ones, with links.

## Cross-cutting threads

Bullets linking to `CROSS-CUTTING.md` anchors (see list below) for the principles visible here, each with one phrase on how it shows up.
```

## Layer README template (`NN-*/README.md`)

Same as the parent template, plus, before "How the children fit together":

```markdown
## Why this layer sits here

What it needs from the layers below (with links) and what the layers above need from it. State the one abstraction or idea this layer contributes to the stack.
```

and the "Connections to sibling areas" section becomes **"Connections to neighbouring layers"**: how this layer connects to each other top-level layer it touches meaningfully (not all 15; the 4–8 that matter), with links to their READMEs. The layer README of 15 lists its seven leaves on the Children line.

## Cross-cutting principle anchors

`CROSS-CUTTING.md` will be written last, with these anchors. Link to them as `<rel path>/CROSS-CUTTING.md#<anchor>`:

| Anchor | Principle |
|---|---|
| `abstraction-and-generalisation` | Keep only the hypotheses a proof uses; the general statement is often easier to prove and applies everywhere |
| `structure-and-morphism` | An object is known by the maps that preserve its structure: homomorphisms, continuous maps, isometries, functors |
| `equivalence-and-quotients` | Declare equal what differs only in what you ignore: ℤ/n, quotient groups and spaces, homotopy, isomorphism |
| `invariants` | A quantity unchanged by the allowed moves proves impossibility and tells objects apart: parity, degree, determinant, Euler characteristic, homology |
| `symmetry` | The transformations that preserve an object form a group, and the group explains the object: Galois, Klein, Noether |
| `duality` | Theories that mirror each other: dual spaces, projective duality, linear programming duality, Fourier and Pontryagin duality, Poincaré duality |
| `linearisation` | Replace the curved by its best linear approximation, then control the error: derivative, tangent space, Lie algebra, linear stability, Newton's method |
| `approximation-and-limits` | Define the exact as the limit of the approximate and estimate the gap: ε–δ, series, numerical error, asymptotics |
| `completeness-and-compactness` | No holes and no escape to infinity: the two properties that make existence proofs work, in ℝ, in function spaces and in logic |
| `local-to-global` | Build global facts from local ones and measure what blocks the gluing: manifolds, analytic continuation, sheaves, the Hasse principle, cohomology |
| `decomposition-and-classification` | Break objects into simple pieces and list the pieces: primes, simple groups, Jordan form, irreducible representations, surfaces |
| `induction-and-recursion` | Prove or define for all cases by reducing each to smaller ones: induction, infinite descent, transfinite induction, recursion |
| `existence-and-construction` | Knowing that something exists versus building it: the axiom of choice, compactness arguments, the probabilistic method, constructive proof |
| `infinity-and-size` | Different ways to measure how big a set is (cardinality, measure, dimension, category, growth rate) and what each one sees |
| `randomness-and-averaging` | Averages of many independent pieces are nearly certain: the law of large numbers, concentration, ergodic theorems, Monte Carlo |
| `extremal-principles-and-optimisation` | The largest, smallest or best object is often special, and its existence proves the theorem: least action, extremal combinatorics, variational methods |
| `dictionaries-between-fields` | Translate a problem into a field where it is easier: algebraic geometry, Fourier analysis, Galois theory, Langlands, Curry–Howard |
| `impossibility-and-obstruction` | Proofs that something cannot be done, and the invariant that blocks it: √2, the quintic, trisecting an angle, the halting problem, incompleteness, Arrow's theorem |

## Check your work

From `math-first-principles/`, run `python3 -B _meta/check.py <your prefix>` (for example `python3 -B _meta/check.py 07`). Fix every `SECTION`, `EXTRA`, `UPWARD`, `CYCLE`, `LINK` and `ANCHOR` error and every `LENGTH` and `NOTATION` warning in your files. `MISSING` lines for files that other writers own are expected while they work; links to those files are not errors.

## Your final report (to the coordinator)

When done, report: files written (count), any taxonomy suggestions, any link you were unsure about, and any statement, attribution or date you were not fully sure of so the reviewer can check it. Do not paste the files.
