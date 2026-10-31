# The Classification of Simple Lie Algebras

> **Layer:** [08 Geometry](../README.md) › [Lie Theory](README.md)
> **Builds on:** [Lie groups and Lie algebras](lie-groups-and-lie-algebras.md), [Eigenvalues and diagonalisation](../../04-linear-algebra/02-determinants-and-eigenvalues/eigenvalues-and-diagonalisation.md), [Quadratic forms and positive definiteness](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md), [Composition series and simple groups](../../05-abstract-algebra/01-groups/composition-series-and-simple-groups.md)
> **Enables:** [Representations of Lie groups](representations-of-lie-groups.md), [The Langlands programme](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/the-langlands-programme.md), [The mathematics of quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md)

## Essence

A simple Lie algebra has no ideals except zero and itself, and is not abelian; every semisimple Lie algebra is a direct sum of simple ones. Over the complex numbers the simple Lie algebras of finite dimension are completely known: four infinite families, Aₙ, Bₙ, Cₙ and Dₙ, which are the Lie algebras of the special linear, odd orthogonal, symplectic and even orthogonal groups, and exactly five exceptions, G₂, F₄, E₆, E₇ and E₈. Wilhelm Killing found the list in papers of 1888 to 1890, and Élie Cartan's thesis of 1894 made the proofs rigorous. The method converts an algebra into a finite configuration of vectors, a root system, and then into a small graph, the Dynkin diagram, whose possible shapes can be listed by hand.

## Core tenets

1. **Semisimplicity is detected by a bilinear form.** The Killing form is B(X, Y) = tr(ad X ad Y), a symmetric bilinear form invariant under the adjoint action. Cartan's criterion says a Lie algebra over ℂ is semisimple exactly when B is non-degenerate. Non-degeneracy gives orthogonal complements of ideals, so a semisimple algebra splits as a direct sum of simple ideals, as finite groups split into [simple composition factors](../../05-abstract-algebra/01-groups/composition-series-and-simple-groups.md), though here the splitting is a genuine direct sum.

2. **A Cartan subalgebra diagonalises the algebra.** In a semisimple algebra g, choose a maximal abelian subalgebra h of elements whose adjoint maps are [diagonalisable](../../04-linear-algebra/02-determinants-and-eigenvalues/eigenvalues-and-diagonalisation.md). Commuting diagonalisable maps diagonalise simultaneously, so g = h ⊕ ⊕ g_α, where on each root space g_α every H in h acts by the scalar α(H). The non-zero linear functionals α that occur are the roots. For sl(n), h is the diagonal matrices and the root spaces are spanned by the matrix units E_ij with i ≠ j, with roots εᵢ − εⱼ.

3. **Each root carries a copy of sl(2).** For every root α, the spaces g_α, g_(−α) and their bracket form a copy of sl(2) with basis E, F, H satisfying

```
[H, E] = 2E,   [H, F] = −2F,   [E, F] = H
```

   The finite-dimensional representations of sl(2) have integer weights, so the numbers 2⟨β, α⟩/⟨α, α⟩ are integers for all roots α and β, where ⟨·, ·⟩ is the inner product induced by the Killing form, positive definite on the real span of the roots.

4. **Integrality forces only four angles.** Multiplying the two integers 2⟨β, α⟩/⟨α, α⟩ and 2⟨α, β⟩/⟨β, β⟩ gives 4cos²θ, which must be an integer between 0 and 4; excluding the parallel case leaves 0, 1, 2 or 3. So two roots meet at 90°, 60° or 120°, 45° or 135°, or 30° or 150°, and their length ratio is 1, √2 or √3. The reflections in the hyperplanes orthogonal to the roots permute the roots and generate a finite group, the Weyl group.

5. **Simple roots and Dynkin diagrams encode everything.** Choosing a generic direction splits the roots into positive and negative, and the simple roots are the positive roots that are not sums of two others; they form a basis, and every root is an integer combination of them with coefficients all of one sign. The Dynkin diagram has a node per simple root and joins two nodes by 0, 1, 2 or 3 lines according to 4cos²θ, with an arrow pointing to the shorter root. Serre's relations rebuild the algebra from the diagram, so isomorphic diagrams give isomorphic algebras.

6. **Positivity cuts the diagrams down to a finite list.** The [quadratic form](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md) given by the Gram matrix of the simple roots must be positive definite. Testing small subdiagrams shows a connected diagram has no cycles, at most one branch point and at most one multiple edge. A branch with arms of p, q and r nodes, counting the centre in each, is allowed only when 1/p + 1/q + 1/r > 1, the inequality that also classifies the Platonic solids. The solutions give Dₙ, E₆, E₇ and E₈; double edges give Bₙ, Cₙ and F₄; the triple edge gives G₂.

7. **The result is a complete list with known dimensions.** No two items in the list are isomorphic once low-rank coincidences are excluded, such as A₁ = B₁ = C₁ and D₃ = A₃.

```
Aₙ  sl(n+1)    n(n+2)        n ≥ 1
Bₙ  so(2n+1)   n(2n+1)       n ≥ 2
Cₙ  sp(2n)     n(2n+1)       n ≥ 3
Dₙ  so(2n)     n(2n−1)       n ≥ 4
G₂ 14   F₄ 52   E₆ 78   E₇ 133   E₈ 248
```

   E₈ has 240 roots, which together with its 8-dimensional Cartan subalgebra give 248; those roots are the minimal vectors of the [E₈ lattice](../03-convex-and-discrete-geometry/lattices-and-sphere-packing.md).

8. **Each hypothesis matters.** Over ℝ each complex simple algebra has several real forms, such as su(2) and sl(2, ℝ), classified later by Cartan. In characteristic p there are further simple algebras, such as Witt algebras. In infinite dimensions Kac–Moody algebras come from diagrams whose quadratic form is only semidefinite or indefinite. Solvable algebras have no comparable classification; the Levi decomposition writes any finite-dimensional algebra as a solvable ideal plus a semisimple part, so the list covers only the semisimple half.

## Key concepts

| Term | Meaning |
|---|---|
| Simple Lie algebra | Non-abelian, with no ideals but zero and itself |
| Killing form | B(X, Y) = tr(ad X ad Y); non-degenerate exactly for semisimple algebras |
| Cartan subalgebra | A maximal abelian subalgebra acting diagonalisably |
| Root | A non-zero eigenvalue functional of the Cartan subalgebra |
| Root system | A finite set of vectors closed under its reflections, with integrality |
| Weyl group | The finite group generated by reflections in the roots |
| Simple roots | A basis of positive roots from which all roots are integer combinations |
| Dynkin diagram | A graph on the simple roots recording angles and relative lengths |
| Exceptional algebra | One of G₂, F₄, E₆, E₇, E₈ |

## How it fits

- **Below:** [Lie algebras](lie-groups-and-lie-algebras.md) supply the objects, diagonalisation supplies root spaces, and positive-definite forms bound the diagrams.
- **Above:** The Langlands programme is organised by reductive groups and their dual groups, read off by reversing Dynkin arrows; particle physics uses SU(3) and SU(2).
- **Siblings:** [Representations of Lie groups](representations-of-lie-groups.md) are labelled by weights in the same root geometry; the [regular polytopes](../03-convex-and-discrete-geometry/polytopes.md) share symmetry groups with root systems, the 24-cell with F₄.

## Common misconceptions

- **"The exceptional algebras are curiosities"**: E₈ governs the densest packing in dimension 8, and the exceptional algebras recur in physics and geometry.
- **"The classification holds over any field"**: It is for ℂ, or algebraically closed fields of characteristic 0; real forms and characteristic p differ.
- **"Every Lie algebra is a sum of simple ones"**: Only semisimple ones; solvable algebras such as the upper triangular matrices are not.

## Go deeper

- Humphreys, *Introduction to Lie Algebras and Representation Theory* (1972): the standard route to the classification.
- Fulton and Harris, *Representation Theory: A First Course* (1991): many examples before the general theory.
- Hawkins, *Emergence of the Theory of Lie Groups* (2000): the history from Lie to Killing, Cartan and Weyl.
