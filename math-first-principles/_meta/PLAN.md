# Plan: a first-principles taxonomy of Mathematics

## 1. Goal

Build a knowledge base that explains Mathematics from the ground up: logic and sets at the bottom, the number systems built from them, the great branches in the order in which they depend on one another (combinatorics, linear and abstract algebra, analysis, topology, geometry, advanced analysis, differential equations, probability), the syntheses where branches fuse, the study of mathematics by mathematics, the applications, and finally mathematics as a human activity. Every **leaf** holds the few tenets you must understand to grasp the essence of that topic. Every **parent** explains how its children fit together and how it connects to its siblings. The tree should be deep enough to be a map of the whole field, but each file short enough to read in one sitting.

This is a sibling of [`../../cs-first-principles/`](../../cs-first-principles/README.md) and [`../../medicine-first-principles/`](../../medicine-first-principles/README.md) and follows the same method: a fixed taxonomy, parallel writer agents, a mechanical checker, a review pass, and a cross-cutting index. The Computer Science (CS) tree has a short mathematics layer (its layer 01), a toolkit for computing. This tree is the subject itself.

## 2. What "first principles" means here

1. **Dependency order.** A topic appears above everything it needs. Read bottom-up, nothing relies on an idea you have not yet met. Galois theory (05) is written for a reader who already knows groups, polynomial rings and field extensions (05) and the complex numbers (02). The prime number theorem (12) is written for one who already knows contour integration and analytic continuation (09).
2. **Essence over coverage.** Mathematics is vast; a leaf says what is *true and load-bearing*, not everything known. The test: if you forgot this, would you misunderstand the topic? A leaf on compactness explains why "every open cover has a finite subcover" is the abstraction of "closed and bounded" that makes existence proofs work in any space. It does not catalogue the dozen variants of compactness.
3. **Proof idea over statement.** Every tenet says *why* a thing is true: the idea that makes the proof work, and what breaks without each hypothesis. "A continuous function on a closed bounded interval attains its maximum" is a label. This is a tenet: "Every sequence in [a, b] has a convergent subsequence, because repeated bisection keeps a half that contains infinitely many terms, and the completeness of ℝ supplies the limit. Apply this to a sequence on which f approaches its supremum, and continuity makes the limit point a maximum. Drop completeness and the theorem fails: on [1, 2] ∩ ℚ the function x ↦ −(x² − 2)² never reaches its supremum 0. Drop finite dimension and it fails again: in an infinite-dimensional Hilbert space the unit vectors e₁, e₂, … stay √2 apart, so the closed unit ball is bounded but not compact."
4. **Explicit edges.** A tree shows one parent per node, but mathematics is a dense graph. Groups appear in algebra, in topology (the fundamental group), in geometry (symmetry), in number theory (the class group) and in physics (Noether's theorem). Every file states what it **builds on** and what it **enables**, and [`../CROSS-CUTTING.md`](../CROSS-CUTTING.md) follows ideas such as invariants, duality, linearisation and local-to-global through every layer in which they appear.
5. **Understanding, not the examination.** Facts that matter only for an examination (a dozen integration tricks, memorised formulas, competition shortcuts) are left out. Ideas that change how one thinks about a problem stay in.

## 3. Top-level structures considered

Choosing the top level decides which relationships the tree shows for free and which it must spell out. Six candidates were compared.

### A. The foundational ladder (logic → sets → numbers → structures; Whitehead and Russell, *Principia Mathematica*, 1910–1913; Bourbaki, *Éléments de mathématique*, from 1939)

- **Strengths:** It is the logical order of the subject: every object is built from sets, and every proof is a derivation in logic. It matches the request (foundations at the bottom).
- **Weaknesses:** Followed strictly, it is a single chain that says nothing about how the branches above the numbers depend on one another. Bourbaki's six core books (sets, algebra, general topology, functions of a real variable, topological vector spaces, integration) leave out combinatorics, probability, most of geometry and all of applied mathematics. The ladder also shows the finished building, not why it was built.

### B. The Mathematics Subject Classification (MSC2020)

- **Strengths:** It is the field's own map, maintained by Mathematical Reviews and zbMATH Open to file every paper, with 63 two-digit classes from 00 (general and overarching topics) to 97 (mathematics education). Nothing is missing.
- **Weaknesses:** It is flat and numbered by tradition, not by dependency. Ten of its classes (70–86) are mechanics and physics. It separates what is one idea (26 Real functions and 40 Sequences, series, summability) and gives a niche the same rank as a continent. It is used here as the coverage check (§6).

### C. Bourbaki's mother structures (algebraic, order and topological structures; "The Architecture of Mathematics", 1948)

- **Strengths:** It explains why algebra and topology are different branches, and how the rich objects of mathematics arise by combining structures: an ordered field, a topological group, a Lie group, a Banach space.
- **Weaknesses:** Three kinds of structure cannot order a whole subject. Number theory, combinatorics and probability are not "a structure", and the scheme says nothing about applications. It is used to sort the middle of the stack: algebraic structure (04, 05), then order and topology (06, 07), then their combinations (08, 09).

### D. The degree and qualifying-examination branches (algebra, analysis, geometry and topology, probability, applied; *The Princeton Companion to Mathematics*, 2008)

- **Strengths:** A mathematics graduate recognises every area, and it reflects how mathematicians describe their own work.
- **Weaknesses:** It is a list of departments. It says nothing about which branch rests on which, and it splits ideas that belong together (Fourier analysis is analysis, algebra and number theory at once). It is used as the sanity check.

### E. A unifying language (Klein's Erlangen programme, 1872; categories, Eilenberg and Mac Lane, 1945)

- **Strengths:** It shows that branches share patterns. A geometry is a group acting on a space. A theory is a category of objects and structure-preserving maps. Homology turns a topological question into an algebraic one.
- **Weaknesses:** The language is abstract and presupposes the examples it unifies: nobody learns categories before groups and spaces. It is used for layer 13 and for the cross-cutting index.

### F. Historical (counting and measurement → Greek proof → algebra → calculus → rigour → abstraction → computation)

- **Strengths:** It shows why ideas arose and which problems forced them.
- **Weaknesses:** History is not dependency. Calculus (Newton and Leibniz, 1660s–1680s) came two centuries before the real numbers it rests on were constructed (Dedekind and Cantor, 1872), and set theory, on which everything is now built, was axiomatised only in 1908 (Zermelo).

## 4. Decision: a foundational ladder at the bottom, the branches in dependency order in the middle, syntheses and metamathematics near the top, with two roots and a cross-cutting index

The chosen structure is **A's foundational ladder for layers 00–02, the branches in dependency order for layers 03–11 sorted by C's mother structures, the syntheses at 12, E's unifying languages at 13 and in the cross-cutting index, and application and context at 14 and 15**, numbered as one topological order, with **B** as the coverage check, **D** as the sanity check (a mathematics graduate should recognise every area) and **F** confined to a leaf on history.

- **Top level = numbered layers 00–15.** The numbers are a topological order of the dependency graph: every layer depends only on lower numbers.
- **Two roots at the bottom.** `00` Logic and Proof is the deductive root: what follows from what, and what counts as a proof. `01` Sets and Foundations is the ontological root: what mathematical objects are, and how large a collection can be. Each leans on the other. Zermelo–Fraenkel set theory (ZF) is a theory written in first-order logic, so 01 builds on 00. The semantics of logic (a model is a set with relations on it) is written in sets, so 00 may cite 01; the checker allows that one upward exception.
- **The roots meet in the numbers.** `02` Number Systems builds ℕ from the Peano axioms, ℤ and ℚ as quotients of pairs, ℝ by completing ℚ, and ℂ as pairs of reals. This is where induction (from logic) and constructions by equivalence class (from sets) first produce the objects everyone uses. Elementary number theory sits here because it needs nothing beyond ℤ and induction.
- **Structure before limits.** Layers `03`–`05` are finite or algebraic. Combinatorics counts and finds forced structure; linear algebra studies the one structure that is understood completely; abstract algebra studies structure in general. None of them needs a limit.
- **The limit enters at 06.** Real analysis is where the completeness of ℝ does its work: convergence, the derivative, the integral, and metric spaces as the general setting for limits. `07` Topology abstracts nearness from distance. `08` Geometry puts measurement back (curvature, symmetry groups, Lie groups) and so uses 04–07. `09` Advanced analysis brings measure, holomorphy and infinite-dimensional linear algebra. `10` Differential equations and dynamics and `11` Probability and statistics apply analysis to change and to chance.
- **Syntheses at 12.** Algebraic and analytic number theory, algebraic geometry, and elliptic curves and modular forms are where the branches fuse. The proof of Fermat's Last Theorem uses algebra, complex analysis, geometry and representation theory at once.
- **Mathematics about mathematics at 13.** Category theory, computability and incompleteness, and model theory study the structure and the limits of mathematics itself. Their subject sits at the bottom of the stack, but their content is a reflection on examples from every layer, so they sit high.
- **Application and context at the top.** `14` uses the whole stack to compute, decide and model: numerical analysis, optimisation, information and codes, physical and biological models, games and finance, data and learning. `15` treats mathematics as a human activity: its history, its philosophy, how it is discovered and checked, computers and proof, open problems, teaching, and its place in society.
- **Cross-cutting principles** (invariants, symmetry, duality, linearisation, approximation and limits, local-to-global, decomposition and classification, impossibility and obstruction, and others) get their own index, `CROSS-CUTTING.md`, linking each to every leaf where it appears. This repairs the main weakness of any tree.

### Why this order and not another (key placement decisions)

| Decision | Alternative rejected | Reason |
|---|---|---|
| Logic (00) and sets (01) as twin roots | One foundations layer, or sets first | Logic says how to reason and sets say what is reasoned about; neither reduces to the other without circularity. ZF is written in first-order logic, and first-order semantics is written in sets. Two layers with one permitted upward link (00 → 01) make the circle explicit instead of hiding it. |
| The number systems constructed (02), not assumed | Take ℝ as given at the bottom | Building ℕ → ℤ → ℚ → ℝ → ℂ shows what each extension buys (subtraction, division, limits, a root for every polynomial) and what it costs (ℂ cannot be ordered). It is also the first real use of quotients and of completion, two ideas that recur in every layer. |
| Elementary number theory in 02; algebraic and analytic number theory in 12 | All of number theory in one place | Divisibility, primes, congruences and quadratic reciprocity need only ℤ and induction. Ideals, class groups and the zeta function need rings and Galois theory (05) and complex analysis (09). Splitting by method keeps both in dependency order. |
| Combinatorics and graph theory low (03) | Combinatorics as a late or "applied" branch | Counting needs only ℕ, induction and functions, and it supplies arguments (double counting, the pigeonhole principle, generating functions) used throughout algebra, probability and computing. Discrete probability sits here because a finite sample space needs only counting. |
| Linear algebra (04) below abstract algebra (05) | Linear algebra as a special case of modules | Vector spaces are the one structure classified completely (by dimension), so they are the right first abstraction. Groups, rings and modules then generalise what the reader has already seen in matrices. |
| Algebra (04, 05) below analysis (06) | Calculus first, as in most curricula | Analysis needs ℝ (02) and linear maps (the derivative is one, 04), but algebra needs no limits. Placing algebra first lets 06 treat the derivative of a function of several variables as a linear map from the start. |
| Metric spaces in 06 | Metric spaces in topology (07) | Distance is what makes ε–δ arguments work, and completeness and the contraction mapping principle are tools of analysis. Topology then abstracts what remains when distance is forgotten. |
| Topology (07) below geometry (08) | Geometry first, as in history | Manifolds, differential forms and the Gauss–Bonnet theorem need open sets, compactness and the Euler characteristic. Euclidean geometry needs less, but it sits in 08 so that one layer tells the story from Euclid to curvature. |
| Lie theory in 08 | Lie theory in algebra (05) | A Lie group is a group that is also a smooth manifold, and its Lie algebra is its tangent space at the identity. It needs groups (05), the derivative (06) and manifolds (07), so it belongs where they meet. |
| Measure, complex, functional and harmonic analysis together (09), above topology | Complex analysis beside real analysis | Measure theory needs the topology of ℝ; complex analysis uses winding numbers and homotopy (07); functional analysis is linear algebra (04) in infinite dimensions with a topology (07); harmonic analysis needs all three. One layer above its tools keeps that visible. |
| Ordinary and partial differential equations (10) above 09 | Differential equations right after calculus | Existence theorems use completeness and the contraction mapping principle (06); Partial Differential Equation (PDE) theory needs Lebesgue spaces, Fourier analysis and distributions (09); dynamical systems need manifolds (07). Recipes for solving textbook equations are left to textbooks. |
| Probability (11) above measure theory (09); discrete probability in 03 | All of probability in one place | Finite probability needs only counting. The law of large numbers, the Central Limit Theorem (CLT) and Brownian motion need measure, integration and the Fourier transform. Stating both keeps the elementary version readable without hiding what rigour requires. |
| Number theory and algebraic geometry together (12), above the branches | Inside algebra (05) | Modern number theory and algebraic geometry use everything below: rings and Galois theory (05), complex analysis (09), topology and cohomology (07, 08), and representation theory. They are where the branches fuse, so they sit above all of them. |
| Category theory, computability and model theory (13), not at the bottom | Category theory as a foundation in 01 | Their subject is foundational, but their content is a reflection on examples from every layer: the Yoneda lemma means little without groups and spaces, and forcing means little without ZF and Gödel. Alternative foundations (type theory) are introduced in 01 and developed in 13. |
| Applied and computational mathematics (14) near the top | Numerical analysis beside analysis | Numerical analysis, optimisation, coding theory and learning theory each use several branches at once: linear algebra and analysis for numerics, convexity and duality for optimisation, finite fields for codes, probability and high-dimensional geometry for learning. |
| History, philosophy and practice at the top (15) | History as an introduction | What mathematics is, how it is discovered and checked, and what remains open can only be discussed once the reader has seen the mathematics. |

## 5. File conventions

- **Directories** are parent nodes; each has a `README.md` (the parent explanation).
- **Leaves** are `.md` files inside a parent directory, one topic each. Layer 15 is small enough to hold its leaves directly.
- **Numeric prefixes** (`00-`, `01-`…) give reading order at every level.
- **Links** are relative so the tree works on GitHub and in any Markdown viewer.
- **Abbreviations:** each file spells an abbreviation out on first use, for example "Zermelo–Fraenkel set theory with the axiom of Choice (ZFC)", then uses the short form. Every file may be the first one a reader opens.
- **Notation:** Unicode symbols (ℝ, ∀, ∈, ≤, ∫, x²), never LaTeX, so that every file reads correctly as plain text. Longer formulas go in fenced code blocks.
- **Spelling and names:** British spelling as default (generalise, colouring, programme) except in established names. A theorem carries a person's name and a year only where both are certain.
- Templates and style rules: [`WRITER_BRIEF.md`](WRITER_BRIEF.md). The full path list is in [`TAXONOMY.md`](TAXONOMY.md).

## 6. Coverage check against the Mathematics Subject Classification (MSC2020)

| MSC2020 class | Where it lives |
|---|---|
| 00 General and overarching topics; 01 History and biography | 15 |
| 03 Mathematical logic and foundations | 00, 01, 13 |
| 05 Combinatorics | 03 |
| 06 Order, lattices, ordered algebraic structures | 01, 03 |
| 08 General algebraic systems | 05, 13 |
| 11 Number theory | 02, 12 |
| 12 Field theory and polynomials | 05 |
| 13 Commutative algebra | 05, 12 |
| 14 Algebraic geometry | 12 |
| 15 Linear and multilinear algebra; matrix theory | 04 |
| 16 Associative rings and algebras; 17 Nonassociative rings and algebras | 05; Lie algebras in 08 |
| 18 Category theory; homological algebra | 13 |
| 20 Group theory and generalizations | 05 |
| 22 Topological groups, Lie groups | 08, 09 |
| 26 Real functions; 40 Sequences, series, summability | 06 |
| 28 Measure and integration | 09 |
| 30 Functions of a complex variable | 09 |
| 31 Potential theory | 10 |
| 33 Special functions | 06, 09, 12 |
| 34 Ordinary differential equations; 35 Partial differential equations | 10 |
| 37 Dynamical systems and ergodic theory | 10 |
| 39 Difference and functional equations | 03, 10 |
| 41 Approximations and expansions | 06, 14 |
| 42 Harmonic analysis on Euclidean spaces; 43 Abstract harmonic analysis | 09 |
| 44 Integral transforms; 46 Functional analysis; 47 Operator theory | 09 |
| 49 Calculus of variations and optimal control; optimization | 10, 14 |
| 51 Geometry; 52 Convex and discrete geometry; 53 Differential geometry | 08 |
| 54 General topology; 55 Algebraic topology; 57 Manifolds and cell complexes | 07 |
| 58 Global analysis, analysis on manifolds | 08, 10 |
| 60 Probability theory and stochastic processes | 03, 11 |
| 62 Statistics | 11, 14 |
| 65 Numerical analysis | 14 |
| 68 Computer science | 13, 14, and the CS tree |
| 70–86 Mechanics and physics | 14, with 08 and 10 |
| 90 Operations research, mathematical programming | 03, 14 |
| 91 Game theory, economics, finance, and other social and behavioral sciences | 14 |
| 92 Biology and other natural sciences | 14, and the Medicine tree |
| 93 Systems theory; control | 10, 14 |
| 94 Information and communication theory, circuits | 14 |
| 97 Mathematics education | 15 |

Covered only in passing: 19 K-theory, 32 Several complex variables and analytic spaces, 45 Integral equations, and most of 70–86 beyond the leaves on quantum mechanics, general relativity and Hamiltonian systems.

## 7. Process

1. **Plan** (this file) and fix the full path list (`TAXONOMY.md`) so that cross-links can be written before the target files exist.
2. **Draft in parallel.** One writer agent per layer, with layer 14 split in two (16 writers), all working to `WRITER_BRIEF.md`.
3. **Verify mechanically.** `_meta/check.py` finds missing files, files outside the taxonomy, missing sections, broken relative links and anchors, and "Builds on" links that point upward or form a cycle. It warns about files outside their length limits and about LaTeX notation.
4. **Review.** A separate pass per pair of layers reads for factual errors, missing load-bearing tenets and weak connections, and fixes them (`REVIEW_BRIEF.md`).
5. **Cross-cutting index.** Build `CROSS-CUTTING.md` from the finished leaves.
6. **Iterate** until the checker is clean and the review finds nothing load-bearing.

## 8. Lessons carried over from the CS and Medicine trees

- **"Builds on" must point down; everything else goes in the body.** A related idea in a higher layer (the completeness of metric spaces, 06, for a leaf on the real numbers, 02) goes in "Enables" or in the text with a link, never in "Builds on". The checker reports violations as `UPWARD`.
- **00 and 01 are twin roots.** Logic's semantics is written in sets, so 00 may build on 01; nothing else may point upward. Only the leaf on soundness, completeness and compactness uses that exception, which keeps the two roots free of cycles.
- **No cycles.** Two leaves in one layer can each look like the other's prerequisite (countable sets and cardinal numbers). The checker reports "Builds on" cycles as `CYCLE`.
- **Lengths overran in both earlier trees.** The checker now warns (`LENGTH`) when a file is outside its limits, and it counts only tokens that contain a letter or digit, so table pipes and arrows do not inflate the count.
- **Links to files not yet written are not errors.** While writers work in parallel, a link to a planned path is skipped (the missing file is reported once, as `MISSING`), and links into `CROSS-CUTTING.md` are checked against the fixed list of anchors.
- **Gaps found by writers become new leaves in the review pass**, not ad hoc files. Writers report them; the taxonomy is amended first.
- **Status is dated.** Open problems and recent results carry a year ("open as of 2026"; "proved in 2002–2003").
- **Anchor headings use plain hyphens.** The anchor generator drops en dashes, so headings in `CROSS-CUTTING.md` are written with ASCII hyphens ("Local-to-global").

## 9. What was done

(Filled in as passes complete.)

| Pass | Work | Result |
|---|---|---|
| 1. Draft | 16 writer agents to `WRITER_BRIEF.md` | 314 files (242 leaves, 72 READMEs), about 304,000 words; 0 checker problems. Writers' taxonomy suggestions, doubtful claims and cross-layer links logged in `REVIEW_NOTES.md`. Taxonomy amended after the draft: areas 06/03 and 06/04 swapped so metric spaces precede several-variable calculus, and 15 leaves added for gaps the writers found |
| 2. Review | 8 reviewer agents, two layers each (14 alone), to `REVIEW_BRIEF.md`: fact-check every number, date, attribution and citation; tighten hypotheses; write the 15 new leaves; strengthen sibling connections | About 50 factual corrections, among them Cantor's 1891 diagonal argument, R(5,5) ≤ 46 (Angeltveit–McKay 2024), elliptic-curve rank 29 (Elkies–Klagsbrun 2024), the 2025 International Mathematical Olympiad (IMO) results, the convexity hypothesis of the Karush–Kuhn–Tucker (KKT) conditions, and the uses of the axiom of choice; 15 new leaves; 329 files: 257 leaves, 72 READMEs, about 322,000 words |
| 3. Index | `CROSS-CUTTING.md`: 18 principles traced bottom-up through 206 links, each with a "When it misleads" note, and a closing table of tensions | Every anchor resolves |
| 4. Coherence | Audit of the 16 layer READMEs as one bottom-up story | Neighbouring layers agree on what each gives and takes; every parent README links all its children, including the 15 new leaves; layer 06 prose follows the new order |

`python3 _meta/check.py` reports 0 problems: every taxonomy path exists, every link and anchor resolves, every leaf has the required sections and length, and no "Builds on" link points upward.

## 10. Known limits and next iterations

- Leaves are capped at about 1,100 words, so each one gives the idea of a proof, not the proof. The "Go deeper" sources are the next step.
- There are no exercises, and mathematics is learnt by doing it. Each "Go deeper" list points to a book that has them.
- Candidate leaves not yet added: K-theory and the Atiyah–Singer index theorem, the Jordan curve theorem, several complex variables, operator algebras, geometric group theory, symplectic topology, the representation theory of the symmetric groups, tropical geometry, arithmetic dynamics, combinatorial optimisation, matroids and designs, statistical mechanics, quantum information, time series, inverse problems, decision theory and mechanism design.
- Claims that move fast are dated in the text and should be rechecked on each revision: the refereeing of the proof of the geometric Langlands conjecture, bounds on diagonal Ramsey numbers (the post-2023 exponential improvements are mentioned only in outline), record elliptic-curve ranks, and the capabilities of AI systems in competition mathematics and formal proof.
