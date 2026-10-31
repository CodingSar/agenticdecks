# Axioms, Definitions and Theorems

> **Layer:** [00 Logic and Proof](../README.md) › [The Axiomatic Method](README.md)
> **Builds on:** [What a Proof Is](../02-methods-of-proof/what-a-proof-is.md), [Predicate Logic and Quantifiers](../01-formal-logic/predicate-logic-and-quantifiers.md), [Soundness, Completeness and Compactness](../01-formal-logic/soundness-completeness-and-compactness.md)
> **Enables:** [Consistency and Independence](consistency-and-independence.md), [Zermelo–Fraenkel Set Theory](../../01-sets-and-foundations/03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md), [Natural Numbers and the Peano Axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md), [Euclidean Geometry](../../08-geometry/01-classical-geometry/euclidean-geometry.md), [Groups and Subgroups](../../05-abstract-algebra/01-groups/groups-and-subgroups.md)

## Essence

The axiomatic method organises a body of mathematics as a list of axioms, accepted without proof, from which every other statement is derived. Definitions add names for things built from the primitive notions, and theorems are what has been proved. Euclid's *Elements*, from around 300 BCE, is the ancient model; Hilbert's *Grundlagen der Geometrie* (1899) is the modern one, in which axioms are no longer self-evident truths about one subject but conditions that pick out a class of structures. Every theorem then holds in every structure satisfying the axioms.

## Core tenets

1. **Axioms constrain; they do not describe one thing.** In the modern view the primitive terms ("point", "line", "lies on") carry no meaning beyond what the axioms say about them. Hilbert is reported to have said that one must be able to say "tables, chairs and beer mugs" in place of "points, lines and planes". A theorem then means: in any structure where the axioms hold, so does this. By soundness, nothing else can be derived ([Soundness, Completeness and Compactness](../01-formal-logic/soundness-completeness-and-compactness.md)).

2. **Hidden assumptions surface when the axioms are taken literally.** Euclid's first proposition constructs an equilateral triangle on a segment AB by drawing the circles centred at A through B and at B through A, and taking a point where they meet. Nothing in his postulates guarantees that they meet. In the plane ℚ² of points with rational coordinates, the circles of radius 1 centred at (0, 0) and (1, 0) meet only at (1/2, ±√3/2), which are not in ℚ², so a continuity principle is genuinely needed. Pasch (1882) found further unstated order axioms, and Hilbert's list of 1899 supplied axioms of incidence, order, congruence, parallels and continuity ([Euclidean Geometry](../../08-geometry/01-classical-geometry/euclidean-geometry.md)).

3. **Some axiom systems aim at one structure, others at many.** The Peano axioms and the axioms of a complete ordered field are meant to describe ℕ and ℝ ([Natural Numbers and the Peano Axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md)). The group axioms are meant to have many models, and that is their power: Lagrange's theorem, that the order of a subgroup divides the order of a finite group, is proved once from the axioms and then holds for symmetries, permutations and residues alike ([Groups and Subgroups](../../05-abstract-algebra/01-groups/groups-and-subgroups.md), [abstraction and generalisation](../../CROSS-CUTTING.md#abstraction-and-generalisation)).

4. **A definition is an abbreviation and must be well defined.** "n is even" abbreviates "∃k (n = 2k)", and any definition can in principle be eliminated by substituting its meaning. A definition that names an object must name exactly one: "the least element of S" needs S to have one and only one least element. A function defined on representatives must not depend on the choice: f(a/b) = a + b is not a function on ℚ, since 1/2 = 2/4 but 1 + 2 = 3 while 2 + 4 = 6.

5. **Definitions are chosen, not discovered true or false.** A definition cannot be false, only unhelpful. 1 is excluded from the primes because otherwise factorisation would not be unique: 6 = 2 · 3 = 1 · 2 · 3. The ε–δ definition of a limit replaced talk of quantities "approaching" one another because it made the theorems provable and the counterexamples visible. Good definitions are tuned so that the theorems one wants become true and short.

6. **Status words record what has been proved.** A theorem is a proved statement; a lemma is a theorem used mainly to prove others; a corollary follows quickly from a theorem; a conjecture is believed but unproved. The Riemann hypothesis and Goldbach's conjecture are both open as of 2026, and many theorems are stated conditionally, "if the Riemann hypothesis holds, then …", which are genuine theorems about an implication. Status changes only by proof or counterexample.

7. **Four questions can be asked of any axiom system.** Is it consistent, free of contradiction? Is each axiom independent of the others? Is it complete, deciding every sentence in its language? Is it categorical, having only one model up to isomorphism? Consistency is essential; the others are properties that some systems have and others, such as the group axioms, deliberately lack ([Consistency and Independence](consistency-and-independence.md)).

## Key concepts

| Term | Meaning |
|---|---|
| Axiom | A statement accepted without proof as a starting point |
| Primitive notion | An undefined term whose meaning is fixed only by the axioms |
| Definition | A new name for something expressible in existing terms |
| Well-defined | Naming exactly one object, independent of any choices made |
| Theorem | A statement derived from the axioms |
| Lemma, corollary | A theorem used to prove others; a theorem that follows quickly |
| Conjecture | A statement believed true but not proved |
| Model | A structure in which all the axioms hold |
| Categorical | Having exactly one model up to isomorphism |

## How it fits

- **Below:** [What a Proof Is](../02-methods-of-proof/what-a-proof-is.md) gives the derivations; [Predicate Logic and Quantifiers](../01-formal-logic/predicate-logic-and-quantifiers.md) gives the language axioms are written in; [Soundness, Completeness and Compactness](../01-formal-logic/soundness-completeness-and-compactness.md) shows that theorems are exactly what holds in all models.
- **Above:** [Zermelo–Fraenkel Set Theory](../../01-sets-and-foundations/03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md) axiomatises almost all of mathematics at once; [Natural Numbers and the Peano Axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md), [Euclidean Geometry](../../08-geometry/01-classical-geometry/euclidean-geometry.md) and [Groups and Subgroups](../../05-abstract-algebra/01-groups/groups-and-subgroups.md) are the classic systems.
- **Siblings:** [Consistency and Independence](consistency-and-independence.md) asks the first two of the four questions; [Constructive and Intuitionistic Logic](constructive-and-intuitionistic-logic.md) varies the logic in which the axioms are used.

## Common misconceptions

- **"Axioms are self-evident truths"**: that was the older view; modern axioms are chosen to describe a class of structures, and some, such as the axiom of choice, were long disputed.
- **"A conjecture with overwhelming numerical support is effectively a theorem"**: π(x) < li(x) holds for every x ever computed, yet Littlewood proved in 1914 that the inequality reverses infinitely often.
- **"A definition can be wrong"**: it can be useless, or not well defined, but a well-defined definition is never false.

## Go deeper

- Euclid, *The Thirteen Books of the Elements*, translated by Thomas L. Heath (1908): the original axiomatic text, with commentary.
- David Hilbert, *Grundlagen der Geometrie* (1899): axioms as implicit definitions of a class of structures.
- Robin Hartshorne, *Geometry: Euclid and Beyond* (2000): Euclid read alongside Hilbert's axioms, with the gaps filled.
