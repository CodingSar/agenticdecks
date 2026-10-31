# Cases, Constructions and Counterexamples

> **Layer:** [00 Logic and Proof](../README.md) › [Methods of Proof](README.md)
> **Builds on:** [What a Proof Is](what-a-proof-is.md), [Direct Proof, Contraposition and Contradiction](direct-proof-contraposition-and-contradiction.md), [Predicate Logic and Quantifiers](../01-formal-logic/predicate-logic-and-quantifiers.md)
> **Enables:** [Constructive and Intuitionistic Logic](../03-the-axiomatic-method/constructive-and-intuitionistic-logic.md), [Inclusion–Exclusion and the Pigeonhole Principle](../../03-combinatorics-and-graph-theory/01-enumeration/inclusion-exclusion-and-the-pigeonhole-principle.md), [The Probabilistic Method](../../03-combinatorics-and-graph-theory/03-discrete-probability/the-probabilistic-method.md), [Colouring and Planarity](../../03-combinatorics-and-graph-theory/02-graph-theory/colouring-and-planarity.md), [Computers and Proof](../../15-mathematics-in-context/computers-and-proof.md)

## Essence

Three methods handle what direct proof leaves aside: disjunctions, existence, and universal claims that may be false. Proof by cases splits a problem into finitely many exhaustive possibilities and proves the claim in each. Existence is shown constructively, by exhibiting an object, or non-constructively, by showing that non-existence is impossible. A universal claim is refuted by a single counterexample, and looking for one is the natural first step before trying to prove anything.

## Core tenets

1. **Cases must be exhaustive, and each must be proved.** Every integer is even or odd, and (2k)² = 4k² while (2k + 1)² = 4(k² + k) + 1, so every square leaves remainder 0 or 1 on division by 4. A sum of two squares therefore leaves 0, 1 or 2, and no number of the form 4m + 3 is a sum of two squares. Forgetting a case is the typical error: dividing x² = x by x to get x = 1 loses the solution x = 0.

2. **"Without loss of generality" is an appeal to symmetry.** To show max(x, y) ≥ (x + y)/2, one may assume x ≥ y, because the statement is unchanged when x and y are swapped; then max(x, y) = x = (x + x)/2 ≥ (x + y)/2. The phrase is legitimate only when the omitted cases are images of the treated one under a symmetry of the problem.

3. **Case analyses can be enormous, and computers can carry them.** Appel and Haken's proof of the four colour theorem (1976) reduced the problem to well over a thousand configurations, each checked by computer. Heule, Kullmann and Marek (2016) showed that the integers from 1 to 7824 can be split into two classes with no class containing a, b, c with a² + b² = c², but those from 1 to 7825 cannot; their proof, found by a satisfiability (SAT) solver, is about 200 terabytes long.

4. **A constructive existence proof exhibits the object.** To prove that some number is a sum of two positive cubes in two different ways, write 1729 = 1³ + 12³ = 9³ + 10³. A construction proves more than existence: it gives a witness that can be checked, computed with and often generalised.

5. **A non-constructive proof shows existence without exhibiting an object.** Among any 13 people, two share a birth month, by the pigeonhole principle, though the argument does not say which two. The intermediate value theorem gives a root of x⁵ − x − 1 between 1 and 2, since the value is −1 at 1 and 29 at 2, without naming it. Erdős (1947) showed that for k ≥ 3 the Ramsey number R(k, k) exceeds 2^(k/2): on that many vertices, the two-colourings of the edges containing a set of k vertices with all edges of one colour are fewer than all two-colourings, so some colouring has no such set, and the count names none ([Ramsey Theory](../../03-combinatorics-and-graph-theory/04-extremal-combinatorics/ramsey-theory.md)). This tension runs through mathematics ([existence and construction](../../CROSS-CUTTING.md#existence-and-construction)).

6. **One counterexample refutes a universal claim, however much evidence supports it.** Euler conjectured that no k-th power is a sum of n positive k-th powers with 2 ≤ n < k. Lander and Parkin (1966) found by computer search that 27⁵ + 84⁵ + 110⁵ + 133⁵ = 144⁵, and Elkies (1988) found 2682440⁴ + 15365639⁴ + 18796760⁴ = 20615673⁴. Centuries of failed searches had counted for nothing.

7. **Each hypothesis of a theorem has a counterexample that shows it is needed.** A continuous function on a closed bounded interval attains a maximum. Drop "closed": x on (0, 1) has none. Drop "bounded": x on [0, ∞) has none. Drop "continuous": the function equal to x on [0, 1) and to 0 at 1 has none on [0, 1]. Weierstrass's continuous nowhere-differentiable function, presented in 1872, refuted the belief that continuous functions are differentiable at most points. A failed search for a counterexample often reveals why a statement is true, so searching for counterexamples is half of searching for proofs.

## Key concepts

| Term | Meaning |
|---|---|
| Proof by cases | Splitting into exhaustive possibilities and proving each |
| Without loss of generality | Treating one case and transferring it to the others by a symmetry |
| Constructive existence proof | A proof that exhibits the object |
| Non-constructive existence proof | A proof that an object exists without exhibiting it |
| Witness | An object satisfying an existential statement |
| Pigeonhole principle | If n + 1 objects lie in n boxes, some box holds two |
| Counterexample | An instance satisfying the hypotheses but not the conclusion |
| Sharp hypothesis | A hypothesis shown to be needed by a counterexample without it |

## How it fits

- **Below:** [Predicate Logic and Quantifiers](../01-formal-logic/predicate-logic-and-quantifiers.md) gives the rules for ∨ and ∃ that these methods apply; [What a Proof Is](what-a-proof-is.md) and [Direct Proof, Contraposition and Contradiction](direct-proof-contraposition-and-contradiction.md) supply the surrounding argument.
- **Above:** [Inclusion–Exclusion and the Pigeonhole Principle](../../03-combinatorics-and-graph-theory/01-enumeration/inclusion-exclusion-and-the-pigeonhole-principle.md) and [The Probabilistic Method](../../03-combinatorics-and-graph-theory/03-discrete-probability/the-probabilistic-method.md) are engines of non-constructive existence; [Colouring and Planarity](../../03-combinatorics-and-graph-theory/02-graph-theory/colouring-and-planarity.md) and [Computers and Proof](../../15-mathematics-in-context/computers-and-proof.md) show machine case analysis; [Constructive and Intuitionistic Logic](../03-the-axiomatic-method/constructive-and-intuitionistic-logic.md) asks which proofs construct.
- **Siblings:** [Direct Proof, Contraposition and Contradiction](direct-proof-contraposition-and-contradiction.md) treats implications; [Mathematical Induction](mathematical-induction.md) replaces infinitely many cases by a base and a step.

## Common misconceptions

- **"Checking many cases proves the statement"**: only checking all of them does; the circle-region pattern 1, 2, 4, 8, 16 breaks at the next step.
- **"A non-constructive proof is not a real proof"**: it is valid in classical logic; what it lacks is a witness, which constructive mathematics demands.
- **"An example where the conclusion fails refutes the theorem"**: only if it satisfies every hypothesis; otherwise it shows that a hypothesis is needed.

## Go deeper

- Bernard R. Gelbaum and John M. H. Olmsted, *Counterexamples in Analysis* (1964): why each hypothesis of the standard theorems is there.
- Lynn Arthur Steen and J. Arthur Seebach Jr., *Counterexamples in Topology* (1970): the same for topological spaces.
- Noga Alon and Joel H. Spencer, *The Probabilistic Method* (4th edition, 2016): non-constructive existence through probability.
