# Varieties and the Nullstellensatz

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Algebraic Geometry](README.md)
> **Builds on:** [Polynomial Rings](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md), [Rings and Ideals](../../05-abstract-algebra/02-rings-and-fields/rings-and-ideals.md), [Field Extensions](../../05-abstract-algebra/02-rings-and-fields/field-extensions.md), [Topological Spaces and Continuous Maps](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md)
> **Enables:** [Projective Varieties and Bézout's Theorem](projective-varieties-and-bezouts-theorem.md), [Algebraic Curves and Riemann–Roch](algebraic-curves-and-riemann-roch.md), [Schemes](schemes.md), [Quantifier Elimination and Decidable Theories](../../13-structure-and-metamathematics/03-model-theory-and-independence/quantifier-elimination-and-decidable-theories.md)

## Essence

Algebraic geometry studies the shapes cut out by polynomial equations: circles, parabolas, surfaces, and their analogues in any number of variables and over any field. Its first discovery is that such a shape and the algebra of polynomials that vanish on it determine each other. Hilbert's Nullstellensatz ("theorem of the zeros", 1893) makes this exact over an algebraically closed field such as ℂ: points correspond to maximal ideals, shapes to radical ideals, and maps between shapes to ring homomorphisms in the opposite direction. From then on, geometric questions can be answered by commutative algebra, and algebraic questions can be pictured.

## Core tenets

1. **Algebraic sets are zero sets, and finitely many equations always suffice.** Fix a field k and write k[x₁, …, xₙ] for the polynomial ring. For a set S of polynomials, V(S) is the set of points of kⁿ where all of them vanish. V(S) depends only on the ideal that S generates, and Hilbert's basis theorem (1890) says every ideal of k[x₁, …, xₙ] is finitely generated. The proof is by induction on n: the leading coefficients of the polynomials of degree d in an ideal of A[x] form an ideal of A, and an ascending chain of these must stop.

2. **Zero sets form a topology.** Finite unions and arbitrary intersections of algebraic sets are algebraic, because V(I)∪V(J) = V(IJ) and ⋂V(Iₐ) = V(∑Iₐ). Taking them as closed sets gives the Zariski topology. It is very coarse: on the line the proper closed sets are the finite sets, so any two non-empty open sets meet and the space is not Hausdorff. Its virtue is that it is defined over any field, with no notion of distance.

3. **The weak Nullstellensatz: proper ideals have zeros.** If k is algebraically closed, every maximal ideal of k[x₁, …, xₙ] has the form (x₁ − a₁, …, xₙ − aₙ), so a set of polynomials with no common zero generates the whole ring: 1 = ∑ gᵢfᵢ for some gᵢ. The key step is Zariski's lemma: a field that is finitely generated as a k-algebra is a finite extension of k, hence equal to k when k is algebraically closed. Over ℝ the statement fails, since x² + 1 has no real zero yet generates a proper ideal.

4. **The strong Nullstellensatz: vanishing means radical membership.** Let I(X) be the ideal of polynomials vanishing on X. For an ideal J over an algebraically closed field, I(V(J)) = √J, the set of f with some power fᵐ ∈ J. Rabinowitsch's trick derives this from the weak form: if f vanishes on V(J), then J together with 1 − y·f has no common zero in kⁿ⁺¹, so 1 = ∑ gᵢfᵢ + h·(1 − y·f); substituting y = 1/f and clearing denominators puts a power of f in J.

5. **The result is a dictionary that reverses inclusion.** Over an algebraically closed field:

   ```
   points of kⁿ              ⟷  maximal ideals of k[x₁, …, xₙ]
   algebraic sets            ⟷  radical ideals
   irreducible sets          ⟷  prime ideals
   larger set                ⟷  smaller ideal
   ```

   An algebraic set is irreducible if it is not a union of two smaller ones. Because chains of ideals stabilise, every algebraic set is a finite union of irreducible components: V(xz, yz) in k³ is the plane z = 0 together with the z-axis. An irreducible algebraic set is an affine variety.

6. **Varieties are their coordinate rings.** The coordinate ring k[V] = k[x₁, …, xₙ]/I(V) is the ring of polynomial functions on V. A polynomial map V → W corresponds to a k-algebra homomorphism k[W] → k[V], by pulling functions back. This gives an equivalence, reversing arrows, between affine varieties and finitely generated k-algebras that are integral domains. So the parabola y = x² is isomorphic to the line, since k[x, y]/(y − x²) ≅ k[x], while the hyperbola xy = 1 is not: its ring k[x, 1/x] has units other than constants.

7. **Dimension has algebraic and geometric faces that agree.** The dimension of a variety V is the length of the longest chain of irreducible subvarieties, which equals the longest chain of prime ideals in k[V] (the Krull dimension) and also the transcendence degree of the field of rational functions on V. Curves have dimension 1, surfaces 2. A single non-constant equation in kⁿ cuts out a set all of whose components have dimension n − 1.

8. **The theory is effective.** Gröbner bases, introduced by Buchberger in 1965, are generating sets for which division by the ideal behaves like division by one polynomial. They decide ideal membership, compute V(I) and its components, and eliminate variables, so the dictionary can be run by a computer algebra system.

## Key concepts

| Term | Meaning |
|---|---|
| Algebraic set V(I) | Common zeros of the polynomials in an ideal I |
| Zariski topology | The topology whose closed sets are the algebraic sets |
| Radical √J | The polynomials some power of which lies in J |
| Nullstellensatz | I(V(J)) = √J over an algebraically closed field |
| Affine variety | An irreducible algebraic set |
| Coordinate ring k[V] | Polynomial functions on V, the quotient k[x₁, …, xₙ]/I(V) |
| Dimension | Longest chain of irreducible subvarieties; Krull dimension of k[V] |

## How it fits

- **Below:** [polynomial rings](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md) and [ideals](../../05-abstract-algebra/02-rings-and-fields/rings-and-ideals.md) are the algebra; algebraically closed fields come from [field extensions](../../05-abstract-algebra/02-rings-and-fields/field-extensions.md); the Zariski topology is a [topological space](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md) of an unusual kind.
- **Above:** the Nullstellensatz is the algebraic core of [quantifier elimination](../../13-structure-and-metamathematics/03-model-theory-and-independence/quantifier-elimination-and-decidable-theories.md) for algebraically closed fields.
- **Siblings:** [projective varieties](projective-varieties-and-bezouts-theorem.md) add points at infinity; [curves](algebraic-curves-and-riemann-roch.md) are the one-dimensional case; [schemes](schemes.md) extend the dictionary to every commutative ring and to all prime ideals. Rings of integers in [number fields](../01-algebraic-number-theory/number-fields-and-algebraic-integers.md) play the role of coordinate rings of curves.

## Common misconceptions

- **"The Nullstellensatz holds over any field"**: over ℝ, x² + 1 generates a proper ideal with no zeros; algebraic closure is essential.
- **"An algebraic set determines its equations"**: it determines only the radical; x and x² cut out the same point. Schemes keep the difference.
- **"Zariski-closed means closed in the usual sense, and conversely"**: Zariski-closed sets are closed over ℂ, but most closed sets, such as a disc, are not Zariski-closed.

## Go deeper

- David Cox, John Little and Donal O'Shea, *Ideals, Varieties, and Algorithms* (4th edition, 2015): the dictionary with Gröbner bases, at undergraduate level.
- Miles Reid, *Undergraduate Algebraic Geometry* (1988): a short, lively first course.
- M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra* (1969): the algebra behind the Nullstellensatz and dimension.
