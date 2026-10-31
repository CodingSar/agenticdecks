# Philosophy of Mathematics

> **Layer:** [15 Mathematics in Context](README.md)
> **Builds on:** [Constructive and Intuitionistic Logic](../00-logic-and-proof/03-the-axiomatic-method/constructive-and-intuitionistic-logic.md), [Zermelo–Fraenkel Set Theory](../01-sets-and-foundations/03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md), [Gödel's Incompleteness Theorems](../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md), [Forcing and Independence](../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md), [History of Mathematics](history-of-mathematics.md)
> **Enables:** [Mathematical Practice and Discovery](mathematical-practice-and-discovery.md), [Computers and Proof](computers-and-proof.md), [The Scientific Method and Models (Medicine)](../../medicine-first-principles/01-quantitative-and-scientific-foundations/03-systems-and-models/the-scientific-method-and-models.md)

## Essence

Philosophy of mathematics asks what mathematical statements are about, how we know them, and why they apply to the physical world. Mathematical objects are not seen or touched, yet theorems about them seem more certain than any empirical law. Around 1900, the crisis in foundations turned these questions into rival programmes: logicism (mathematics is logic), formalism (mathematics is rule-governed symbol manipulation, secured by consistency proofs) and intuitionism (mathematics is mental construction). Gödel's incompleteness theorems of 1931 showed that none could deliver everything hoped for. Today Platonism, structuralism and nominalism are debated through Benacerraf's dilemma about knowledge and the Quine–Putnam indispensability argument.

## Core tenets

1. **Platonism explains objectivity but struggles to explain knowledge.** The Platonist holds that numbers and sets exist independently of minds and language, and theorems are true descriptions of them. This fits how mathematicians speak ("we discovered"). But Paul Benacerraf (1973) posed the difficulty: our knowledge of ordinary objects depends on causal contact with them, and abstract objects have no causal powers.

2. **Logicism derived arithmetic from logic, until a paradox broke it.** Gottlob Frege defined numbers as classes of equinumerous concepts and derived arithmetic in his *Grundgesetze*. His Basic Law V, which gives every concept an extension, implies Russell's paradox (1901), so the system was inconsistent. Russell and Whitehead's type theory avoided the paradox but needed an axiom of infinity that is hard to call logic. Neo-logicists observe that Hume's principle, "the number of Fs equals the number of Gs if and only if the Fs and Gs can be paired off exactly", suffices in second-order logic to derive the Peano axioms; whether that principle is analytic is disputed.

3. **Hilbert's formalist programme was limited by incompleteness.** David Hilbert proposed treating infinitary mathematics as a formal system and proving its consistency by finitary, evidently safe reasoning about strings of symbols. Gödel's second incompleteness theorem shows that a consistent, effectively axiomatised theory containing enough arithmetic cannot prove its own consistency, so no finitary proof formalisable in such a theory can secure it. Gerhard Gentzen (1936) proved the consistency of Peano arithmetic, but by induction along the ordinal ε₀, beyond what the theory itself proves. Relativised versions survive in proof theory and reverse mathematics.

4. **Intuitionism makes truth depend on construction.** L. E. J. Brouwer held that mathematics is a mental activity, so a statement is true only when a construction proving it has been found. On infinite domains this rejects the law of excluded middle. Arend Heyting formalised the logic, and the Brouwer–Heyting–Kolmogorov interpretation explains the connectives: a proof of "A or B" is a proof of one of them with a label saying which, and a proof of "there exists x with P" supplies a witness. The classical proof that some irrational a, b have a^b rational, by cases on whether √2^√2 is rational, gives no such witness. Errett Bishop's *Foundations of Constructive Analysis* (1967) showed that much analysis survives constructively, and via the Curry–Howard correspondence constructive proofs are programs, the basis of several proof assistants.

5. **Structuralism says mathematics studies positions in structures, not objects.** Benacerraf (1965) noted that 2 can be modelled as the set {{∅}} or as {∅, {∅}}, and nothing in arithmetic decides which is "really" 2. Structuralists conclude that numbers are places in the structure shared by all models of the Peano axioms, and only relations between places matter. This matches modern axiomatic practice, though it must still say what a structure is.

6. **Independence results sharpen the debate over truth.** Gödel (1940) and Paul Cohen (1963) showed the continuum hypothesis neither provable nor refutable from the Zermelo–Fraenkel axioms with choice. A Platonist holds that it is nonetheless true or false and new axioms may decide it; a pluralist holds that there are many equally legitimate universes of sets.

7. **Wigner's puzzle: mathematics is unreasonably effective in physics.** Eugene Wigner's 1960 essay pointed out that structures developed for internal reasons, such as complex Hilbert spaces and Riemannian geometry, later turned out to describe quantum mechanics and gravitation with extraordinary precision. Proposed answers include selection (physicists use the mathematics that fits and discard the rest, a point Richard Hamming made in 1980), the origin of mathematical concepts in experience, and the structuralist view that physics instantiates some of the structures mathematics catalogues.

8. **The indispensability argument turns effectiveness into existence.** W. V. Quine and Hilary Putnam argued that we should believe in the entities indispensable to our best scientific theories; real numbers and functions are indispensable to physics; so we should believe in them. Hartry Field's *Science Without Numbers* (1980) replied by reformulating Newtonian gravitation without quantifying over numbers, to show that mathematics is a conservative, dispensable tool. Whether this extends to modern physics is unresolved.

## Key concepts

| Term | Meaning |
|---|---|
| Platonism | Mathematical objects exist independently of minds |
| Logicism | Mathematics reduces to logic plus definitions |
| Formalism | Mathematics is the manipulation of symbols by rules; Hilbert's variant seeks consistency proofs |
| Intuitionism | Mathematical truth consists in mental construction; excluded middle fails on infinite domains |
| Structuralism | Mathematics studies structures; objects are positions in them |
| Nominalism | There are no abstract objects; mathematics is a useful fiction or tool |
| Hume's principle | Two collections have the same number if and only if they can be paired off exactly |
| Indispensability argument | Belief in science commits us to the mathematics it uses |

## How it fits

- **Below:** constructive logic, the Zermelo–Fraenkel axioms, incompleteness and forcing are the technical results each position must accommodate; [history](history-of-mathematics.md) explains the crisis that set the agenda.
- **Above:** nothing; this is the top layer.
- **Siblings:** [practice](mathematical-practice-and-discovery.md) asks what mathematicians actually do rather than what justifies it; [computers and proof](computers-and-proof.md) makes formalism concrete; [learning and teaching](learning-and-teaching-mathematics.md) meets the question of what understanding is.

## Common misconceptions

- **"Gödel proved that mathematical truth is relative."** He showed that formal provability falls short of truth in arithmetic; he himself was a Platonist.
- **"Intuitionists reject proof by contradiction."** They accept proving "not A" by deriving a contradiction from A; they reject concluding A from the absurdity of "not A".
- **"Philosophy has no effect on mathematics."** Constructivism shaped proof assistants, and debates on the continuum hypothesis guide research in set theory.

## Go deeper

- S. Shapiro, *Thinking about Mathematics* (2000): a clear survey of all the main positions.
- P. Benacerraf and H. Putnam (eds), *Philosophy of Mathematics: Selected Readings* (2nd ed., 1983): the classic papers, including Benacerraf's two.
- Ø. Linnebo, *Philosophy of Mathematics* (2017): a concise modern introduction.
