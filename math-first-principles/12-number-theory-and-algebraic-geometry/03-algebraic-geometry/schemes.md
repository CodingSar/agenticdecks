# Schemes

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Algebraic Geometry](README.md)
> **Builds on:** [Varieties and the Nullstellensatz](varieties-and-the-nullstellensatz.md), [Algebraic Curves and Riemann–Roch](algebraic-curves-and-riemann-roch.md), [Number Fields and Algebraic Integers](../01-algebraic-number-theory/number-fields-and-algebraic-integers.md), [Rings and Ideals](../../05-abstract-algebra/02-rings-and-fields/rings-and-ideals.md)
> **Enables:** [Fermat's Last Theorem](../04-elliptic-curves-and-modular-forms/fermats-last-theorem.md), [The Langlands Programme](../04-elliptic-curves-and-modular-forms/the-langlands-programme.md), [Categories and Functors](../../13-structure-and-metamathematics/01-category-theory/categories-and-functors.md), [Homological Algebra](../../13-structure-and-metamathematics/01-category-theory/homological-algebra.md)

## Essence

The Nullstellensatz matches varieties with certain rings: finitely generated, over an algebraically closed field, with no nilpotents. Grothendieck, around 1960, removed every one of those conditions. To any commutative ring A he attached a geometric space, its spectrum Spec A, whose points are the prime ideals of A, and he glued such spaces into schemes. The ring ℤ becomes a curve whose points are the primes; a polynomial with integer coefficients becomes a family of varieties, one over each prime; and nilpotent elements become infinitesimal thickenings that remember tangency. The price is abstraction; the reward is that number theory and geometry become one subject, strong enough to prove the Weil conjectures and Fermat's Last Theorem.

## Core tenets

1. **Spec A is the set of prime ideals, with the Zariski topology.** For a commutative ring A, the closed sets of Spec A are V(I) = {primes containing I}. Prime ideals are used rather than maximal ones because a ring homomorphism φ: A → B pulls primes back to primes, giving a continuous map Spec B → Spec A, while maximal ideals need not pull back to maximal ones: the maximal ideal (0) of ℚ pulls back to (0) in ℤ. So Spec is a functor, and non-maximal primes appear as generic points: (0) in Spec k[x] lies in every non-empty open set, and its closure is the whole line.

2. **Ring elements are functions with values in varying fields.** The value of f ∈ A at a point 𝔭 is its image in the residue field κ(𝔭), the fraction field of A/𝔭. In Spec ℤ the closed points are the primes (p), with residue fields 𝔽_p, and the generic point (0) has residue field ℚ. The integer 12 is a function that vanishes at (2) and (3), to order 2 at (2), just as x²(x − 1) vanishes on the line. Spec ℤ[i] → Spec ℤ is then a double cover of a curve, branched only over (2), where the prime ramifies.

3. **The structure sheaf makes Spec a space with functions.** On the basic open set D(f), where f does not vanish, the functions are the localisation A_f, with f inverted. These glue into a sheaf of rings 𝒪, and the pair (Spec A, 𝒪) is an affine scheme. The global functions are A again, and morphisms of affine schemes correspond exactly to ring homomorphisms in the opposite direction: affine schemes are commutative rings, read geometrically.

4. **Schemes are glued from affine pieces.** A scheme is a space with a sheaf of rings that is locally isomorphic to affine schemes, as a manifold is locally Euclidean. Projective space over any ring, including ℙⁿ over ℤ, is glued from n + 1 affine charts. Grothendieck wrote the foundations with Dieudonné in the *Éléments de géométrie algébrique* (EGA), 1960–1967, and developed the cohomology in his seminars.

5. **Nilpotents record infinitesimal information.** Spec k[ε]/(ε²) has a single point, but a morphism from it to X is a point of X with a tangent vector. Intersecting the parabola y = x² with its tangent y = 0 gives Spec k[x, y]/(y, y − x²) = Spec k[x]/(x²): a point with multiplicity 2, as [Bézout](projective-varieties-and-bezouts-theorem.md) requires, recorded in the ring instead of counted by hand.

6. **Arithmetic bases put all primes in one picture.** The equation y² = x³ − 2 defines a scheme over Spec ℤ, a surface fibred over the "curve" Spec ℤ. Its fibre over (p) is the curve reduced mod p, over 𝔽_p; its generic fibre is the curve over ℚ. The fibres are smooth except over primes dividing the discriminant, here 2 and 3, the primes of bad reduction. Rational points become sections of the family. This is the setting of [elliptic curves](../04-elliptic-curves-and-modular-forms/elliptic-curves.md) over ℤ, of modular curves, and of the proof of [Fermat's Last Theorem](../04-elliptic-curves-and-modular-forms/fermats-last-theorem.md).

7. **A scheme is its functor of points.** For a ring R, X(R) is the set of morphisms Spec R → X: solutions of the equations of X with coordinates in R. By the Yoneda lemma, X is determined by this functor on rings. Moduli spaces are defined this way, as schemes whose R-points classify families of objects over R, such as the modular curves, whose points classify elliptic curves with extra structure.

8. **Cohomology turns geometry into linear algebra.** Serre's paper FAC (*Faisceaux algébriques cohérents*, 1955) introduced sheaf cohomology into algebraic geometry, and GAGA (*Géométrie algébrique et géométrie analytique*, 1956) showed that for complex projective varieties algebraic and analytic coherent cohomology agree. Grothendieck's étale cohomology, built with Artin and Verdier, works over any base. Deligne used it to complete the proof of the Weil conjectures in 1974, including the analogue of the Riemann Hypothesis for varieties over finite fields.

## Key concepts

| Term | Meaning |
|---|---|
| Spec A | The prime ideals of a commutative ring, with the Zariski topology |
| Generic point | A non-closed point whose closure is a whole component |
| Residue field κ(𝔭) | Fraction field of A/𝔭, where functions take values at 𝔭 |
| Structure sheaf | Functions on open sets; A_f on D(f) |
| Affine scheme | (Spec A, 𝒪); equivalent to the ring A |
| Nilpotent | A non-zero element with a zero power; geometrically a thickening |
| Fibre over (p) | The reduction mod p of a scheme over ℤ |
| Functor of points | R ↦ X(R), which determines X |

## How it fits

- **Below:** [the Nullstellensatz](varieties-and-the-nullstellensatz.md) is the special case of maximal ideals over an algebraically closed field; [rings of integers](../01-algebraic-number-theory/number-fields-and-algebraic-integers.md) give one-dimensional schemes like curves; [curves](algebraic-curves-and-riemann-roch.md) get their cohomological Riemann–Roch here.
- **Above:** schemes were a driving example for [categories and functors](../../13-structure-and-metamathematics/01-category-theory/categories-and-functors.md) and for [homological algebra](../../13-structure-and-metamathematics/01-category-theory/homological-algebra.md); [the Langlands programme](../04-elliptic-curves-and-modular-forms/the-langlands-programme.md) gets its Galois representations from étale cohomology.
- **Siblings:** [projective varieties](projective-varieties-and-bezouts-theorem.md) become Proj of graded rings; the [class group](../01-algebraic-number-theory/ideals-and-the-class-group.md) is the Picard group of Spec 𝒪_K.

## Common misconceptions

- **"Schemes are abstraction for its own sake"**: they were built to prove the Weil conjectures, and they did.
- **"Every point is closed"**: generic points are not, and they carry the information of a whole component.
- **"A scheme is determined by its underlying space"**: Spec k and Spec k[ε]/(ε²) are both one point, but their rings differ.

## Go deeper

- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry* (freely available notes): a modern, example-driven course.
- David Eisenbud and Joe Harris, *The Geometry of Schemes* (2000): pictures of Spec ℤ, nilpotents and families.
- Robin Hartshorne, *Algebraic Geometry* (1977), chapters II and III: the standard graduate treatment.
