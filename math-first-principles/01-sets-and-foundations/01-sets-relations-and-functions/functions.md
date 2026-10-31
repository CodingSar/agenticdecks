# Functions

> **Layer:** [01 Sets and Foundations](../README.md) › [Sets, Relations and Functions](README.md)
> **Builds on:** [Relations and orders](relations-and-orders.md), [Sets and set operations](sets-and-set-operations.md), [Predicate logic and quantifiers](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md)
> **Enables:** [Equivalence relations and quotients](equivalence-relations-and-quotients.md), [Countable sets](../02-infinity-and-cardinality/countable-sets.md), [The axiom of choice](../03-axiomatic-set-theory/the-axiom-of-choice.md), [Topological spaces and continuous maps](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md), [Categories and functors](../../13-structure-and-metamathematics/01-category-theory/categories-and-functors.md)

## Essence

A function f: A → B assigns to each element of A exactly one element of B, and set theory makes that literal: f is a relation, a set of pairs, containing exactly one pair (a, b) for each a ∈ A. The definition says nothing about formulas, so any assignment counts, including ones nobody can write down. Functions are how mathematics compares sets: an injection shows that one set fits inside another, a surjection that one covers another, a bijection that two have the same size. The recurring questions about a map are whether it is injective or surjective and how it acts on subsets; the answers explain why continuity is defined by preimages and why every function contains a quotient.

## Core tenets

1. **A function is its graph; surjectivity also needs a stated codomain.** f ⊆ A × B is a function from A to B when ∀a ∈ A ∃!b ∈ B ((a, b) ∈ f), where ∃! means "there exists exactly one"; then f(a) = b. Rules with the same pairs are one function: (x + 1)² − 2x − 1 and x² define the same map ℝ → ℝ. That map is not surjective, since −1 is missed, but x ↦ x² from ℝ onto [0, ∞) is.

2. **Injective, surjective, bijective, and how they compose.** f is injective if f(a) = f(a′) ⇒ a = a′, surjective if every b ∈ B equals some f(a), and bijective if both. Injectivity is proved by assuming f(a) = f(a′) and deducing a = a′; surjectivity by solving f(a) = b for an arbitrary b. Composites of injections are injective and of surjections surjective; conversely, if g ∘ f is injective then f is, and if g ∘ f is surjective then g is. f has a two-sided inverse g (g ∘ f = id_A and f ∘ g = id_B, where id_A is the identity map a ↦ a) exactly when f is bijective.

3. **One-sided inverses separate the two notions, and one of them needs choice.** An injection f: A → B with A non-empty has a left inverse g, with g ∘ f = id_A: send each f(a) back to a and every other point of B to a fixed a₀ ∈ A. Without "non-empty" this fails, since the empty map ∅ → B has no left inverse when B is non-empty. A surjection has a right inverse h, with f ∘ h = id_B, by picking a point of each preimage f⁻¹[{b}]; with infinitely many points and no rule for picking, that needs [the axiom of choice](../03-axiomatic-set-theory/the-axiom-of-choice.md), and "every surjection has a right inverse" is equivalent to it over the other axioms.

4. **Preimages respect all set operations; images respect only unions.** For S ⊆ A and T ⊆ B, the image is f[S] = {f(a) : a ∈ S} and the preimage is f⁻¹[T] = {a ∈ A : f(a) ∈ T}. Preimages commute with unions, intersections and complements, because "f(a) ∈ T ∩ T′" unfolds to "f(a) ∈ T ∧ f(a) ∈ T′". Images commute with unions but not intersections: for f(x) = x², f[{−1} ∩ {1}] = ∅ while f[{−1}] ∩ f[{1}] = {1}, and equality holds for all S and T exactly when f is injective. That is why [continuity](../../06-real-analysis/01-limits-and-convergence/continuity.md) and measurability are defined by pulling sets back, not pushing them forward.

5. **Every function factors as a surjection followed by an injection.** f: A → B factors as A → f[A] → B, first onto the image, then the inclusion. The relation a ~ a′ ⇔ f(a) = f(a′), the kernel of f, has one class for each point of the image, and [a] ↦ f(a) is a bijection from the classes to f[A]. This is the set-level first isomorphism theorem, which groups, rings and vector spaces repeat with structure added.

6. **Sequences, tuples and families are functions.** A sequence of reals is a function ℕ → ℝ, an n-tuple is a function on {1, …, n}, and a family (Aᵢ) indexed by I is a function on I. So the product ∏ Aᵢ is the set of functions f on I with f(i) ∈ Aᵢ for each i. For finitely many non-empty Aᵢ it is non-empty by induction; for infinitely many, its non-emptiness is exactly the axiom of choice.

7. **Function sets count like powers.** Bᴬ, the set of all functions A → B, has |B|^|A| elements for finite A and B, because each of the |A| inputs independently picks one of |B| outputs; 𝒫(A) matches {0, 1}ᴬ through indicator functions. The edge cases follow the definition: there is exactly one function ∅ → B (the empty set of pairs), so B^∅ has one element and 0⁰ = 1 in counting, while no function goes from a non-empty set to ∅. Currying, reading a function of two arguments as a function-valued function of one, matches C^(A×B) with (Cᴮ)ᴬ: the law c^(ab) = (cᵇ)ᵃ.

## Key concepts

| Term | Meaning |
|---|---|
| Function f: A → B | a set of pairs with exactly one pair (a, b) for each a ∈ A |
| Image f[S] | {f(a) : a ∈ S}; f[A] is the range |
| Preimage f⁻¹[T] | {a : f(a) ∈ T}; defined for every function |
| Injective | distinct inputs give distinct outputs |
| Surjective | every element of the codomain is an output |
| Bijective | injective and surjective |
| Composition g ∘ f | a ↦ g(f(a)): first f, then g |
| Left, right inverse | g with g ∘ f = id_A; h with f ∘ h = id_B |
| Bᴬ | the set of all functions A → B |

## How it fits

- **Below:** a function is a special [relation](relations-and-orders.md), a set of pairs built in [sets and set operations](sets-and-set-operations.md); "exactly one" is the quantifier ∃! of [predicate logic](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md).
- **Above:** bijections define size in [countable sets](../02-infinity-and-cardinality/countable-sets.md) and [cardinal numbers](../02-infinity-and-cardinality/cardinal-numbers.md); maps that preserve structure are [homomorphisms](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md), [linear maps](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md) and [continuous maps](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md); [category theory](../../13-structure-and-metamathematics/01-category-theory/categories-and-functors.md) takes maps and their composition as primitive.
- **Siblings:** every function defines an [equivalence relation](equivalence-relations-and-quotients.md), its kernel, and every equivalence relation arises this way from its quotient map.

## Common misconceptions

- **"A function is a formula"**: any assignment is a function; the indicator function of ℚ on ℝ (1 on rationals, 0 elsewhere) is one, and most functions ℕ → ℕ are computed by no program.
- **"f⁻¹[T] only makes sense when f is invertible"**: the preimage is defined for every function; only the inverse function f⁻¹ needs a bijection.
- **"g ∘ f = id implies f ∘ g = id"**: for the inclusion f: {0} → {0, 1} and the constant map g: {0, 1} → {0}, g ∘ f is the identity but f ∘ g sends 1 to 0.

## Go deeper

- Paul R. Halmos, *Naive Set Theory* (1960): functions, families and products in a few pages.
- F. William Lawvere and Stephen H. Schanuel, *Conceptual Mathematics: A First Introduction to Categories* (2nd edition, 2009): functions and composition as the starting point.
