# Cardinal Numbers

> **Layer:** [01 Sets and Foundations](../README.md) › [Infinity and Cardinality](README.md)
> **Builds on:** [Countable sets](countable-sets.md), [Cantor's diagonal argument](cantors-diagonal-argument.md), [Equivalence relations and quotients](../01-sets-relations-and-functions/equivalence-relations-and-quotients.md), [Functions](../01-sets-relations-and-functions/functions.md)
> **Enables:** [Ordinal numbers and transfinite induction](ordinal-numbers-and-transfinite-induction.md), [The axiom of choice](../03-axiomatic-set-theory/the-axiom-of-choice.md), [Linear independence, bases and dimension](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md), [Forcing and independence](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md), [Large cardinals](../../13-structure-and-metamathematics/03-model-theory-and-independence/large-cardinals.md)

## Essence

A cardinal number measures the size of a set, with no reference to order: two sets have the same cardinal when they are in bijection, and ∣A∣ ≤ ∣B∣ when A injects into B. Addition, multiplication and exponentiation extend from finite sets by disjoint unions, products and function sets. At infinite sizes addition and multiplication collapse (ℵ₀ + ℵ₀ = ℵ₀ · ℵ₀ = ℵ₀), while exponentiation always climbs, since 2^κ > κ. The simplest question that remains, whether anything lies between ℵ₀ and the size of ℝ, cannot be settled by the standard axioms.

## Core tenets

1. **Size is compared by maps, and "same size" is an equivalence.** Equinumerosity is reflexive, symmetric and transitive, because identities, inverses and composites of bijections are bijections. Its classes are proper classes, too big to be sets, so a cardinal cannot simply be "the class of A". In Zermelo–Fraenkel set theory with choice (ZFC), the standard axioms, ∣A∣ is defined instead as the least [ordinal](ordinal-numbers-and-transfinite-induction.md) equinumerous with A, a canonical representative of the class.

2. **Cantor–Schröder–Bernstein: injections both ways give a bijection.** Given injections f: A → B and g: B → A, trace each element backwards through g⁻¹ and f⁻¹ as far as possible. The chain either stops in A, stops in B, or runs for ever; use f on elements whose chain stops in A or never stops, and g⁻¹ on those whose chain stops in B. No choice is needed. So ≤ is antisymmetric on cardinals. Example: [0, 1] and (0, 1) have the same size, via the inclusion and x ↦ (x + 1)/3.

3. **Comparability needs the axiom of choice.** "For all A and B, ∣A∣ ≤ ∣B∣ or ∣B∣ ≤ ∣A∣" is equivalent to the axiom of choice over Zermelo–Fraenkel set theory without choice (ZF). One direction uses Hartogs' theorem (1915), provable in ZF: for every set A some ordinal does not inject into A, so if that ordinal and A are comparable, A injects into an ordinal and is well-orderable. Without choice, cardinals form a partial order, not a chain.

4. **Arithmetic is defined by sets, then shown well defined.** κ + λ is the size of a disjoint union, κ · λ of a product and κ^λ of the set of functions from a set of size λ to one of size κ. Each depends only on the sizes, since bijections of the inputs give bijections of the outputs. The finite laws survive: (κ^λ)^μ = κ^(λ·μ) is currying, and 2^κ = ∣𝒫(A)∣ through indicator functions, so Cantor's theorem reads κ < 2^κ.

5. **Infinite sums and products collapse.** ℵ₀ + ℵ₀ = ℵ₀ (evens and odds) and ℵ₀ · ℵ₀ = ℵ₀ (pairing). Interleaving two binary sequences into one gives 2^ℵ₀ · 2^ℵ₀ = 2^ℵ₀, so the plane has as many points as the line; Cantor wrote to Dedekind in 1877, "I see it, but I don't believe it". In ZFC every infinite κ has κ · κ = κ, so κ + λ = κ · λ = max(κ, λ) when one is infinite and neither is 0. Tarski showed that "κ · κ = κ for every infinite κ" is itself equivalent to choice.

6. **The continuum is 2^ℵ₀, and much of analysis has that size.** Dedekind cuts inject ℝ into 𝒫(ℚ), which has the size of 𝒫(ℕ), and the Cantor set, the reals in [0, 1] with ternary digits only 0 and 2, receives an injection from 𝒫(ℕ), so ∣ℝ∣ = 2^ℵ₀ by Cantor–Schröder–Bernstein. Also ℵ₀^ℵ₀ = 2^ℵ₀. A continuous f: ℝ → ℝ is fixed by its values on ℚ, so there are only (2^ℵ₀)^ℵ₀ = 2^ℵ₀ of them, against 2^(2^ℵ₀) functions ℝ → ℝ in all.

7. **The continuum hypothesis is independent.** The continuum hypothesis (CH) says 2^ℵ₀ = ℵ₁, the next cardinal after ℵ₀. Gödel showed that CH is consistent with ZFC by building the constructible universe L, in which it holds (1938; monograph 1940); Cohen showed that its negation is consistent too, inventing [forcing](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md) for the purpose (1963). ZFC does constrain the continuum: by König's theorem, 2^ℵ₀ cannot be ℵ_ω, a union of countably many smaller cardinals.

8. **No simple set refutes CH, and no known axiom settles it.** Every uncountable closed set of reals, and more generally every uncountable Borel set, contains a perfect set and so has size 2^ℵ₀; a counterexample to CH cannot be that simple. [Large cardinal](../../13-structure-and-metamathematics/03-model-theory-and-independence/large-cardinals.md) axioms do not decide CH, because small forcing preserves them (Lévy and Solovay, 1967), while forcing axioms such as the proper forcing axiom imply 2^ℵ₀ = ℵ₂. Whether some new axiom should be accepted to decide CH is debated and unresolved as of 2026.

## Key concepts

| Term | Meaning |
|---|---|
| ∣A∣ ≤ ∣B∣ | some injection A → B exists |
| ∣A∣ < ∣B∣ | ∣A∣ ≤ ∣B∣ and no bijection exists |
| ℵ₀, ℵ₁, ℵ₂, … | the infinite cardinals of well-orderable sets, in increasing order |
| 2^κ | the size of the power set of a set of size κ |
| Continuum | 2^ℵ₀, the size of ℝ |
| Cantor–Schröder–Bernstein | injections both ways give a bijection |
| CH | 2^ℵ₀ = ℵ₁ |
| Generalised continuum hypothesis (GCH) | 2^κ is the next cardinal after κ, for every infinite κ |
| Cantor set | reals in [0, 1] with ternary digits 0 and 2; size 2^ℵ₀, length zero |

## How it fits

- **Below:** cardinality starts from [countable sets](countable-sets.md), gets its strictness from [the diagonal argument](cantors-diagonal-argument.md), and is the quotient of all sets by equinumerosity in the sense of [equivalence relations](../01-sets-relations-and-functions/equivalence-relations-and-quotients.md).
- **Above:** dimension is the cardinality of a [basis](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md), and ℝ over ℚ has a basis of size 2^ℵ₀; [Hausdorff dimension](../../09-advanced-analysis/01-measure-and-integration/hausdorff-dimension-and-fractals.md) refines size among sets of the same cardinality; [forcing](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md) and [large cardinals](../../13-structure-and-metamathematics/03-model-theory-and-independence/large-cardinals.md) study what ZFC leaves open.
- **Siblings:** under choice, cardinals are the initial [ordinals](ordinal-numbers-and-transfinite-induction.md), those equinumerous with no smaller ordinal; [the axiom of choice](../03-axiomatic-set-theory/the-axiom-of-choice.md) is what makes all cardinals comparable.

## Common misconceptions

- **"Infinity plus one is bigger than infinity"**: ℵ₀ + 1 = ℵ₀, since n ↦ n + 1 frees a place. Only order can tell ω + 1 from ω, which is the job of ordinals.
- **"A set of length zero is small in size"**: the Cantor set has length zero and the size of ℝ. Measure, dimension and cardinality are different notions of [size](../../CROSS-CUTTING.md#infinity-and-size).
- **"CH is waiting for a cleverer proof"**: proofs from ZFC of CH or of its negation are both impossible, if ZFC is consistent.

## Go deeper

- Paul R. Halmos, *Naive Set Theory* (1960): cardinal arithmetic in a few pages.
- Karel Hrbacek and Thomas Jech, *Introduction to Set Theory* (3rd edition, 1999): cardinals with and without choice.
- Thomas Jech, *Set Theory* (3rd millennium edition, 2003): the standard reference.
