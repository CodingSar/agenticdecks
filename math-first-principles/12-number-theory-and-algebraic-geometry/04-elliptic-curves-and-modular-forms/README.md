# Elliptic Curves and Modular Forms

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › Elliptic Curves and Modular Forms
> **Children:** [Elliptic curves](elliptic-curves.md) · [Modular forms](modular-forms.md) · [Fermat's Last Theorem](fermats-last-theorem.md) · [The Langlands programme](the-langlands-programme.md)

## What this area is about

This area is where the three earlier ones meet. An elliptic curve is a geometric object, a cubic curve of genus 1, whose rational points form a group studied with the tools of algebraic number theory. A modular form is an analytic object, a holomorphic function with a large group of symmetries, whose coefficients carry arithmetic and whose L-function behaves like ζ. The modularity theorem says that the two are the same data: every elliptic curve over ℚ has a modular form whose coefficients count its points mod p. That theorem proved Fermat's Last Theorem, and it is the two-dimensional case of the Langlands programme, which predicts the same kind of match for Galois representations of every dimension.

The unifying idea is that *counting points mod p is a spectral problem*: the numbers p + 1 − #E(𝔽_p), which look arithmetic, are eigenvalues of Hecke operators acting on spaces of modular forms.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Elliptic curves](elliptic-curves.md) | group law, Mordell's theorem, torsion, the Hasse bound, L-functions, the Birch and Swinnerton-Dyer conjecture, cryptography | 03 curves, 01 p-adic fields |
| [Modular forms](modular-forms.md) | SL₂(ℤ) acting on ℍ, Eisenstein series, Δ, Hecke operators, levels, modular curves, modularity | elliptic curves, 02 zeta |
| [Fermat's Last Theorem](fermats-last-theorem.md) | Kummer, the Frey curve, Ribet, Wiles and Taylor–Wiles, the full modularity theorem | elliptic curves, modular forms |
| [The Langlands programme](the-langlands-programme.md) | reciprocity, functoriality, the fundamental lemma, geometric Langlands | all three, 01 class field theory |

Elliptic curves come first and modular forms second; the last tenets of each meet in the modularity theorem. Fermat's Last Theorem shows that theorem at work, and the Langlands programme places it in a much larger pattern that begins with class field theory.

```
 elliptic curve E/ℚ ──► a_p = p + 1 − #E(𝔽_p) ──┐
                                                ├─ equal (modularity, 1995–2001)
 modular form f = ∑ aₙqⁿ ──► Hecke eigenvalues ─┘
        │                                       │
        ▼                                       ▼
 Frey curve + Ribet ──► Fermat's Last Theorem   GL(2) case of reciprocity
                                                │  (GL(1) = class field theory)
                                                ▼
                                   the Langlands programme
```

## Connections to sibling areas

- **[Algebraic Number Theory](../01-algebraic-number-theory/README.md)** provides class groups and units for Mordell's theorem, p-adic methods for the local study of E, Kummer's theory for the history of Fermat's Last Theorem, and class field theory as the GL(1) model for Langlands.
- **[Analytic Number Theory](../02-analytic-number-theory/README.md)** provides the template of Euler products and functional equations; L-functions of elliptic curves and modular forms are degree-2 analogues of ζ and L(s, χ).
- **[Algebraic Geometry](../03-algebraic-geometry/README.md)** provides Riemann–Roch for the Weierstrass equation, Bézout for the group law, schemes for reduction mod p, and étale cohomology for Galois representations.

## Connections across layers

- **Below:** [finite fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md) carry the reductions mod p; [holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md) and [hyperbolic geometry](../../08-geometry/01-classical-geometry/non-euclidean-geometry.md) the modular forms; [representations of Lie groups](../../08-geometry/04-lie-theory/representations-of-lie-groups.md) the automorphic side of Langlands.
- **Above:** elliptic curves secure key exchange and signatures in [cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md) and, in the computer science tree, [public-key cryptography](../../../cs-first-principles/11-security-and-cryptography/02-cryptography/public-key-cryptography.md); the Birch and Swinnerton-Dyer conjecture and the Langlands conjectures are among the [open problems](../../15-mathematics-in-context/open-problems.md); the proof of Fermat's Last Theorem is a case study in the [history of mathematics](../../15-mathematics-in-context/history-of-mathematics.md).

## Cross-cutting threads

- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): modularity matches geometry with analysis.
- [Symmetry](../../CROSS-CUTTING.md#symmetry): modular forms are defined by their symmetry under SL₂(ℤ).
- [Structure and morphism](../../CROSS-CUTTING.md#structure-and-morphism): the chord-and-tangent group law and Hecke operators.
- [Local to global](../../CROSS-CUTTING.md#local-to-global): the a_p at each prime assemble into one L-function, and Ш measures what the local data miss.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): the Frey curve cannot exist.
