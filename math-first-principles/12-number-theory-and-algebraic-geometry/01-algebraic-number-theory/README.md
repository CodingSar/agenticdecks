# Algebraic Number Theory

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › Algebraic Number Theory
> **Children:** [Number fields and algebraic integers](number-fields-and-algebraic-integers.md) · [Ideals and the class group](ideals-and-the-class-group.md) · [p-adic numbers and local fields](p-adic-numbers-and-local-fields.md) · [Class field theory](class-field-theory.md)

## What this area is about

Many questions about ordinary integers become easier in a larger ring. Which primes are sums of two squares? Work in ℤ[i], where p = x² + y² means p = (x + iy)(x − iy). Does xᵖ + yᵖ = zᵖ have solutions? Factor the left side over ℤ[ζ_p]. Algebraic number theory studies these larger rings, the rings of integers of number fields, and the price of entering them: unique factorisation of elements can fail. The repair is to factor ideals instead, and the class group measures exactly how far elements fall short. A second tool looks at one prime at a time by completing ℚ to the p-adic field ℚ_p, where Hensel's lemma makes equations easy. Class field theory then assembles the local and global pictures into a complete description of the abelian extensions of a number field.

The unifying idea is that *arithmetic is controlled by how primes behave in extensions*: whether a prime splits, stays prime or ramifies decides which equations are solvable mod p, and that behaviour is governed by ideals, by completions and finally by the Galois group.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Number fields and algebraic integers](number-fields-and-algebraic-integers.md) | rings of integers 𝒪_K, norm, discriminant, Minkowski's lattice, units, splitting of primes | 05 field extensions, rings and ideals |
| [Ideals and the class group](ideals-and-the-class-group.md) | Dedekind domains, unique factorisation of ideals, finiteness of the class group, Kummer | number fields |
| [p-adic numbers and local fields](p-adic-numbers-and-local-fields.md) | completions, Hensel's lemma, the local-to-global principle and its failures | number fields, 06 completeness |
| [Class field theory](class-field-theory.md) | Frobenius elements, Artin reciprocity, the Hilbert class field, Kronecker–Weber | all three |

Read the first two in order: the ring 𝒪_K is defined first, and its ideals are then shown to factor uniquely. The third can be read in parallel, since it needs only ℚ and a prime p. The fourth uses all three: ray class groups come from the class group, and the local theory comes from the p-adic fields.

```
 number fields K, rings 𝒪_K
        │
        ├──► ideals factor; Cl(K) finite ──┐
        │                                  │
        └──► completions K_𝔭, Hensel ──────┤
                                           ▼
                         class field theory: abelian L/K ⟷ ray class groups
                                           │
                                           ▼
                            (non-abelian: the Langlands programme)
```

## Connections to sibling areas

- **[Analytic Number Theory](../02-analytic-number-theory/README.md)** supplies the counting side: the Dedekind zeta function of K has a residue involving the class number, and Dirichlet's class number formula for L(1, χ) is a case. Chebotarev's density theorem generalises Dirichlet's theorem on primes in progressions.
- **[Algebraic Geometry](../03-algebraic-geometry/README.md)** treats 𝒪_K as the coordinate ring of an arithmetic curve: Dedekind domains are the smooth affine curves of algebra, and the class group is a Picard group. Schemes make this analogy literal.
- **[Elliptic Curves and Modular Forms](../04-elliptic-curves-and-modular-forms/README.md)** uses class groups and units in the proof of Mordell's theorem, Kummer's methods in the history of Fermat's Last Theorem, and class field theory as the one-dimensional case of the Langlands programme.

## Connections across layers

- **Below:** [field extensions](../../05-abstract-algebra/02-rings-and-fields/field-extensions.md) and [the Galois correspondence](../../05-abstract-algebra/03-galois-theory/the-galois-correspondence.md) supply the algebra; [quadratic reciprocity](../../02-number-systems/02-elementary-number-theory/quadratic-reciprocity.md) is the first reciprocity law; [completeness](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md) builds ℚ_p as ℝ is built.
- **Above:** class groups and number fields underlie lattice-based and older number-theoretic [cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md); the cohomological proofs of class field theory were early uses of [homological algebra](../../13-structure-and-metamathematics/01-category-theory/homological-algebra.md).

## Cross-cutting threads

- [Local to global](../../CROSS-CUTTING.md#local-to-global): Hasse–Minkowski, and its failure measured by Ш.
- [Equivalence and quotients](../../CROSS-CUTTING.md#equivalence-and-quotients): the class group is ideals modulo principal ideals.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): the class group obstructs unique factorisation.
- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): ℚ_p is a completion, ℤ_p is compact.
- [Duality](../../CROSS-CUTTING.md#duality): Artin reciprocity matches extensions with subgroups of idele classes.
- [Symmetry](../../CROSS-CUTTING.md#symmetry): Frobenius elements turn splitting of primes into Galois symmetries.
