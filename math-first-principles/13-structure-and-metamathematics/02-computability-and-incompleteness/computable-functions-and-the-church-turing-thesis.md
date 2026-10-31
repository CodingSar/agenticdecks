# Computable Functions and the Church–Turing Thesis

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Computability and incompleteness](README.md)
> **Builds on:** [Mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md), [Functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md), [Countable sets](../../01-sets-and-foundations/02-infinity-and-cardinality/countable-sets.md), [Natural numbers and the Peano axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md)
> **Enables:** [Undecidable problems](undecidable-problems.md), [Gödel's incompleteness theorems](godels-incompleteness-theorems.md), [Turing machines](../../../cs-first-principles/02-theory-of-computation/03-computability/turing-machines.md), [The Church–Turing thesis (CS)](../../../cs-first-principles/02-theory-of-computation/03-computability/church-turing-thesis.md), [Lambda calculus](../../../cs-first-principles/02-theory-of-computation/03-computability/lambda-calculus.md)

## Essence

Before one can prove that no algorithm solves a problem, "algorithm" needs a mathematical definition. In 1936 Alonzo Church and Alan Turing gave two very different ones, λ-definability and the Turing machine, and these turned out to define the same class of functions on the natural numbers, as did Gödel and Herbrand's general recursive functions. The Church–Turing thesis says that this class is exactly the class of functions computable by any effective procedure. It cannot be proved, since "effective procedure" is informal, but the evidence for it is overwhelming, and every impossibility result in this area rests on it. This leaf treats computability from the side of functions on ℕ; the machine side is in the computer science tree.

## Core tenets

1. **Primitive recursion is natural but provably not enough.** The primitive recursive functions start from zero, successor and projections and are closed under composition and definition by recursion, f(n + 1) = g(n, f(n)); every such function is total and obviously computable. But their definitions can be listed effectively as f₀, f₁, …, so d(n) = fₙ(n) + 1 is computable and differs from every fₙ. Wilhelm Ackermann's function (1928) is an explicit total computable function that grows faster than every primitive recursive one.

2. **Unbounded search forces partial functions.** Adding the μ-operator, μy[g(x, y) = 0] = the least y with g(x, y) = 0, gives the partial recursive functions. The search may never stop, so the functions are partial, and this is unavoidable: any effective list of total functions can be diagonalised as above, whereas the diagonal of a list of partial functions may simply be undefined where it would contradict itself.

3. **The models are equivalent, and the proof is by simulation.** Stephen Kleene showed in 1936 that the λ-definable and general recursive functions coincide, and Turing showed in 1937 that both coincide with the Turing-computable functions. Each proof codes the configurations of one model as natural numbers and simulates its steps in the other. Register machines, cellular automata and modern programming languages give the same class.

4. **Every computable function has a normal form and a universal interpreter.** By Kleene's normal form theorem there are a primitive recursive predicate T and function U such that the e-th partial computable function satisfies the identity below. Here T(e, x, y) says that y codes a halting computation of program e on input x. The function (e, x) ↦ φ_e(x) is therefore itself computable: a universal machine exists.

   ```
   φ_e(x)  =  U( μy T(e, x, y) )
   ```

5. **Computably enumerable sets are the Σ₁ sets.** A set is computably enumerable (c.e.) if some program lists its members, equivalently if it is the domain of a partial computable function, equivalently if it has the form {x : ∃y R(x, y)} with R computable. A set is computable if and only if both it and its complement are c.e.: run the two listings side by side until x appears in one of them.

6. **The thesis is a thesis, not a theorem.** It identifies an informal notion with a formal one, so no proof is possible; one could only refute it by exhibiting an effective procedure outside the class. Turing's 1936 paper argued for it by analysing a human clerk following rules with finite memory and finitely many symbols, an argument Kurt Gödel accepted as conclusive. No accepted counterexample has appeared since.

7. **Almost every function is uncomputable.** Programs are finite strings, so there are countably many computable functions, while there are uncountably many functions ℕ → ℕ. The same holds for real numbers: Turing's computable reals, whose digits a program can print, are countable and form a real closed field, yet Ernst Specker (1949) gave a computable increasing bounded sequence of rationals whose limit is not computable, such as the sum of 2^(−k) over the members k of the halting set, listed in order of discovery.

## Key concepts

| Term | Meaning |
|---|---|
| Primitive recursive function | Built from zero, successor and projections by composition and recursion |
| μ-operator | Unbounded search for the least witness |
| Partial computable function | Computed by a program that may fail to halt |
| φ_e | The partial function computed by program number e |
| Universal function | (e, x) ↦ φ_e(x), itself computable |
| Computably enumerable (c.e.) | Listable by a program; Σ₁ |
| Church–Turing thesis | Effective computability is Turing computability |

## How it fits

- **Below:** Definition by [induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md) on the [natural numbers](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md) supplies primitive recursion, and [countability](../../01-sets-and-foundations/02-infinity-and-cardinality/countable-sets.md) shows most [functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md) escape it.
- **Above:** The machine side is in [Turing machines](../../../cs-first-principles/02-theory-of-computation/03-computability/turing-machines.md), the [λ-calculus](../../../cs-first-principles/02-theory-of-computation/03-computability/lambda-calculus.md) and the computer science account of the [thesis](../../../cs-first-principles/02-theory-of-computation/03-computability/church-turing-thesis.md).
- **Siblings:** [Undecidable problems](undecidable-problems.md) diagonalise against φ_e, and [Gödel's theorems](godels-incompleteness-theorems.md) use the fact that the theorems of an effective theory are c.e.

## Common misconceptions

- **"The thesis has been proved."**: Equivalences between particular models have been proved; the identification with the informal notion of an effective procedure cannot be.
- **"Computable means feasible."**: The Ackermann function is computable, yet its values at small inputs cannot be written down; feasibility is the subject of complexity theory.
- **"Physical computers might compute more."**: That is the separate physical Church–Turing thesis, about what nature allows; it is not part of the mathematical thesis.

## Go deeper

- Alan Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem" (1936): the original analysis, still readable.
- Nigel Cutland, *Computability: An Introduction to Recursive Function Theory* (1980): a clear first course.
- Robert Soare, *Turing Computability: Theory and Applications* (2016): the modern account by a leading researcher.
