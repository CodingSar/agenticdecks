# Equivalence Relations and Quotients

> **Layer:** [01 Sets and Foundations](../README.md) › [Sets, Relations and Functions](README.md)
> **Builds on:** [Relations and orders](relations-and-orders.md), [Functions](functions.md), [Cases, constructions and counterexamples](../../00-logic-and-proof/02-methods-of-proof/cases-constructions-and-counterexamples.md)
> **Enables:** [Integers and rational numbers](../../02-number-systems/01-constructing-the-numbers/integers-and-rational-numbers.md), [Modular arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md), [Homomorphisms and quotient groups](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md), [Subspaces, products and quotients](../../07-topology/01-point-set-topology/subspaces-products-and-quotients.md), [Cardinal numbers](../02-infinity-and-cardinality/cardinal-numbers.md)

## Essence

An equivalence relation declares things the same for a purpose: it is reflexive, symmetric and transitive, like equality but coarser. Each one cuts its set into disjoint classes, and the quotient set X/~ has those classes as its elements, so "the same for this purpose" becomes literal equality in a new set. Integers modulo n, fractions, real numbers, quotient groups, the circle as a glued interval and homotopy classes are all quotients. The price is one obligation: anything defined on a class through a representative must give the same answer for every representative, or it is not defined at all.

## Core tenets

1. **Equivalence relations and partitions are the same thing.** If ~ is an equivalence on X, the classes [x] = {y ∈ X : y ~ x} cover X, since reflexivity puts x in [x], and two classes are equal or disjoint: if z lies in both [x] and [y], symmetry and transitivity give x ~ y, and then every element of [x] is in [y] and back. Conversely, "lies in the same block" of a partition is an equivalence. Transitivity is essential: "differs by at most 1" on ℤ is reflexive and symmetric, but 0 ~ 1 ~ 2 while 0 ≁ 2, and its would-be classes overlap.

2. **The quotient map turns equivalence into equality.** X/~ is the set of classes, and q: X → X/~, q(x) = [x], is surjective with q(x) = q(y) ⇔ x ~ y. Every surjection f: X → Y has this form up to renaming: for the relation x ~ x′ ⇔ f(x) = f(x′), the map [x] ↦ f(x) is a bijection from X/~ to Y.

3. **A function on classes is well defined exactly when it ignores the choice of representative.** To define F on X/~ by F([x]) = f(x), the function f must be constant on each class; then F is the unique map with F ∘ q = f, which is the universal property of the quotient:

```
    X ───── f ─────► Y
    │                ▲
  q │                │ F    F exists exactly when f is constant
    ▼                │      on classes; it is unique because
   X/~ ──────────────┘      q is surjective
```

   Failures are easy to write down. "The numerator of a/b" is not a function on fractions, because 1/2 = 2/4 have numerators 1 and 2. The parity of a representative is well defined on ℤ/4, because 4 is even, but not on ℤ/5, where 0 and 5 name the same class.

4. **Operations descend when the relation is a congruence.** On ℤ, a ≡ b (mod n) means n ∣ a − b. Multiplication of classes is well defined because if x ≡ x′ and y ≡ y′, then xy − x′y′ = x(y − y′) + (x − x′)y′ is a multiple of n; sums are similar. A relation that respects the operations this way is a congruence, and the quotient inherits laws such as associativity and distributivity because q is surjective and preserves the operations. This is how ℤ/n, quotient groups and quotient rings are built.

5. **Fractions show why every hypothesis is needed.** On pairs of integers (a, b) with b ≠ 0, set (a, b) ~ (c, d) ⇔ ad = bc; the classes are the rationals. For transitivity, ad = bc and cf = de give adf = bcf = bde, so d(af − be) = 0, and cancelling d needs both d ≠ 0 and the absence of zero divisors in ℤ. If b = 0 were allowed, (0, 0) would be equivalent to every pair while (1, 0) ≁ (1, 1), so transitivity would fail.

6. **Any relation generates an equivalence, and gluing is this construction.** The smallest equivalence containing a relation R puts x ~ y when a finite zigzag x = x₀, x₁, …, xₙ = y joins them, each step an R-pair in one direction or the other. [0, 1] with 0 ~ 1 is a circle, and a square with opposite edges identified is a torus. Groups given by generators and relations are such quotients, and for some finitely presented groups no algorithm decides whether two words are equal (Novikov and Boone, 1950s); see [free groups and presentations](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md).

7. **Invariants are functions on the quotient, and classifying means finding complete ones.** A quantity that agrees on equivalent objects (remainder mod n, dimension, number of holes of a surface) is exactly a function on the quotient. It is complete when different classes get different values, as dimension is for finite-dimensional vector spaces over a fixed field. Picking one representative per class is easy when a canonical one exists, such as the remainder in {0, …, n − 1}, but needs the axiom of choice in general: a set containing one element of each class of ℝ under x − y ∈ ℚ cannot be measurable (Vitali, 1905), see [the axiom of choice](../03-axiomatic-set-theory/the-axiom-of-choice.md).

## Key concepts

| Term | Meaning |
|---|---|
| Equivalence relation | a reflexive, symmetric and transitive relation |
| Class [x] | the set of all elements equivalent to x |
| Partition | non-empty, pairwise disjoint subsets whose union is the whole set |
| Quotient set X/~ | the set of classes |
| Quotient map q | x ↦ [x]; surjective, with q(x) = q(y) exactly when x ~ y |
| Well defined | giving the same value for every representative of a class |
| Congruence | an equivalence relation that respects the operations |
| Kernel of f | the equivalence x ~ x′ ⇔ f(x) = f(x′) |
| Complete invariant | a function on the quotient that separates all classes |

## How it fits

- **Below:** an equivalence is a [relation](relations-and-orders.md) with three properties; the quotient map and the factorisation of a function through its image come from [functions](functions.md).
- **Above:** ℤ, ℚ and ℝ (as classes of Cauchy sequences) are quotients in [02 Number Systems](../../02-number-systems/README.md); [quotient groups](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md) and rings, quotient vector spaces, [quotient spaces](../../07-topology/01-point-set-topology/subspaces-products-and-quotients.md) and [homotopy classes](../../07-topology/02-algebraic-topology/homotopy-and-the-fundamental-group.md) follow the same pattern. This is the thread [equivalence and quotients](../../CROSS-CUTTING.md#equivalence-and-quotients).
- **Siblings:** an equivalence is the symmetric counterpart of a [partial order](relations-and-orders.md), and a preorder (reflexive and transitive) becomes a partial order on the quotient by "a ≤ b and b ≤ a"; every [function](functions.md) defines an equivalence, its kernel.

## Common misconceptions

- **"An equivalence class is an element"**: it is a set of elements; [x] = [y] says x ~ y, not x = y. In ℤ/5, [2] = [7] although 2 ≠ 7.
- **"Reflexivity follows from symmetry and transitivity"**: the argument "x ~ y and y ~ x give x ~ x" needs some y with x ~ y; the empty relation on a non-empty set is symmetric and transitive but not reflexive.

## Go deeper

- Paul R. Halmos, *Naive Set Theory* (1960): equivalence relations and partitions in a few pages.
- Michael Artin, *Algebra* (2nd edition, 2011): quotients of groups, rings and modules, with the universal property used throughout.
