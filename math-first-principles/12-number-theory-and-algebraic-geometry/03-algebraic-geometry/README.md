# Algebraic Geometry

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › Algebraic Geometry
> **Children:** [Varieties and the Nullstellensatz](varieties-and-the-nullstellensatz.md) · [Projective varieties and Bézout's theorem](projective-varieties-and-bezouts-theorem.md) · [Algebraic curves and Riemann–Roch](algebraic-curves-and-riemann-roch.md) · [Schemes](schemes.md)

## What this area is about

Algebraic geometry studies the solution sets of polynomial equations as geometric objects. Its founding observation is a dictionary: a shape cut out by polynomials and the ring of polynomial functions on it determine each other, so geometry can be done with commutative algebra and algebra can be pictured. The dictionary needs care to be exact. Over an algebraically closed field it is Hilbert's Nullstellensatz; to make intersection counts exact, one adds points at infinity and works in projective space; to study curves, one counts functions with prescribed poles by the Riemann–Roch theorem. Finally Grothendieck's schemes extend the dictionary to every commutative ring, so that ℤ itself, and equations over ℤ, become geometric.

The unifying idea is that *a space is known by the functions on it*. Points become ideals, maps become ring homomorphisms in reverse, and invariants such as dimension and genus are read from the algebra.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Varieties and the Nullstellensatz](varieties-and-the-nullstellensatz.md) | affine varieties, the Zariski topology, the ideal–variety dictionary, coordinate rings, dimension | 05 rings and ideals |
| [Projective varieties and Bézout's theorem](projective-varieties-and-bezouts-theorem.md) | points at infinity, completeness, intersection multiplicity, Bézout | varieties, 08 projective geometry |
| [Algebraic curves and Riemann–Roch](algebraic-curves-and-riemann-roch.md) | genus, divisors, Riemann–Roch, the Weierstrass equation, the genus trichotomy | projective varieties |
| [Schemes](schemes.md) | Spec of any ring, nilpotents, arithmetic families over Spec ℤ, functor of points, cohomology | all three, number fields |

The order is the historical one and also the logical one. Affine varieties set up the dictionary; projective varieties complete them so that counts become exact; curves are the first case worked out in full; schemes generalise everything at once. Readers interested in number theory can go from curves straight to elliptic curves and return to schemes when reduction mod p needs a language.

```
 polynomials ⟷ zero sets (Nullstellensatz, k algebraically closed)
        │ add points at infinity
        ▼
 projective varieties ── exact intersection counts (Bézout)
        │ dimension 1
        ▼
 curves: genus, divisors, Riemann–Roch ──► elliptic curves
        │ any ring, any prime ideal
        ▼
 schemes: Spec ℤ, nilpotents, families over ℤ
```

## Connections to sibling areas

- **[Algebraic Number Theory](../01-algebraic-number-theory/README.md)** is geometry over Spec ℤ: rings of integers are one-dimensional like curves, class groups are Picard groups, and splitting of primes is branching of covers.
- **[Analytic Number Theory](../02-analytic-number-theory/README.md)** has its main conjecture proved in the geometric setting: curves and varieties over finite fields satisfy the Riemann Hypothesis, by Weil and Deligne.
- **[Elliptic Curves and Modular Forms](../04-elliptic-curves-and-modular-forms/README.md)** begins with genus 1 curves, uses Bézout for the group law and Riemann–Roch for the equation, and uses modular curves as moduli spaces.

## Connections across layers

- **Below:** [polynomial rings](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md) and [ideals](../../05-abstract-algebra/02-rings-and-fields/rings-and-ideals.md) supply the algebra; [projective geometry](../../08-geometry/01-classical-geometry/projective-geometry.md) the space; [Riemann surfaces](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md) and the [classification of surfaces](../../07-topology/03-manifolds/classification-of-surfaces.md) the complex and topological pictures.
- **Above:** schemes were a driving example for [category theory](../../13-structure-and-metamathematics/01-category-theory/categories-and-functors.md) and [homological algebra](../../13-structure-and-metamathematics/01-category-theory/homological-algebra.md); the Nullstellensatz underlies [quantifier elimination](../../13-structure-and-metamathematics/03-model-theory-and-independence/quantifier-elimination-and-decidable-theories.md) for algebraically closed fields; curves over finite fields give [error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md).

## Cross-cutting threads

- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): the ideal–variety correspondence.
- [Duality](../../CROSS-CUTTING.md#duality): spaces and rings with arrows reversed; Serre duality in Riemann–Roch.
- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): projective varieties are complete, so counts are exact.
- [Invariants](../../CROSS-CUTTING.md#invariants): dimension, degree and genus.
- [Abstraction and generalisation](../../CROSS-CUTTING.md#abstraction-and-generalisation): from varieties over ℂ to schemes over any ring.
- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): irreducible components, and curves sorted by genus.
