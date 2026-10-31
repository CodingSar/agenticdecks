# The Langlands Programme

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Elliptic Curves and Modular Forms](README.md)
> **Builds on:** [Class Field Theory](../01-algebraic-number-theory/class-field-theory.md), [Modular Forms](modular-forms.md), [Fermat's Last Theorem](fermats-last-theorem.md), [Representations of Lie Groups](../../08-geometry/04-lie-theory/representations-of-lie-groups.md), [Fourier Analysis on Groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md)
> **Enables:** [Open Problems](../../15-mathematics-in-context/open-problems.md), [Higher Categories and Homotopy Type Theory](../../13-structure-and-metamathematics/01-category-theory/higher-categories-and-homotopy-type-theory.md)

## Essence

The Langlands programme is a web of conjectures, proposed by Robert Langlands from 1967, that predicts a dictionary between two worlds. On one side are Galois representations, which encode how primes split in number fields and how many points varieties have mod p. On the other are automorphic forms, highly symmetric functions on groups that generalise modular forms, studied with harmonic analysis. The dictionary should match them so that their L-functions agree prime by prime. Class field theory is its one-dimensional case, and the modularity theorem behind Fermat's Last Theorem is a two-dimensional case over ℚ. The general conjectures are open as of 2026, but their partial proofs are among the deepest results in mathematics.

## Core tenets

1. **It began with a letter to Weil.** In January 1967 Langlands wrote a long handwritten letter to André Weil setting out conjectures that tied automorphic forms on reductive groups to number theory, including the L-group and what became functoriality. Langlands treated them as speculation; they became a research programme.

2. **The Galois side is n-dimensional representations.** The absolute Galois group Gal(ℚ̄/ℚ) acts on the étale cohomology of varieties over ℚ. For an elliptic curve E it acts on the ℓ-adic Tate module, giving a two-dimensional representation ρ_E in which the trace of the Frobenius at p is a_p = p + 1 − #E(𝔽_p). In general a Galois representation records, through the traces of Frobenius elements, how arithmetic behaves at every prime.

3. **The automorphic side is harmonic analysis on adelic groups.** For a reductive group G, such as GL(n), automorphic forms are functions on G(ℚ)\G(𝔸), where 𝔸 is the ring of adeles, and automorphic representations are the irreducible pieces of the space they span, decomposed as [Fourier analysis on groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md) decomposes functions on a circle. Dirichlet characters are the automorphic forms of GL(1); [modular forms](modular-forms.md) are those of GL(2). Each automorphic representation has Hecke eigenvalues at almost all primes and an L-function.

4. **Reciprocity matches the two sides.** The reciprocity conjecture says that suitable n-dimensional Galois representations correspond to automorphic representations of GL(n), with the trace of Frobenius at p equal to the Hecke eigenvalue at p, so the L-functions coincide. One consequence would be that every such Galois L-function has analytic continuation and a functional equation, which is how Artin's conjecture on Artin L-functions would follow.

5. **Known cases include class field theory and modularity.** For GL(1) over any number field, reciprocity is [class field theory](../01-algebraic-number-theory/class-field-theory.md): Artin's map pairs abelian characters of the Galois group with Hecke characters. For GL(2) over ℚ, the modularity of elliptic curves, completed in 2001 after the work on [Fermat's Last Theorem](fermats-last-theorem.md), is reciprocity for the representations ρ_E. The Langlands–Tunnell theorem treats two-dimensional Artin representations with solvable image, such as the S₃ example of x³ − x − 1 and its weight-1 form of level 23. The local Langlands correspondence for GL(n) over p-adic fields was proved by Harris and Taylor and by Henniart around 2000.

6. **Functoriality transfers forms between groups.** Each reductive group G has a Langlands dual group Ĝ: GL(n) is its own dual, while SO(2n + 1) and Sp(2n) are dual to each other. Functoriality predicts that a homomorphism between dual groups transfers automorphic representations of one group to another, matching Hecke eigenvalues. Base change and the Jacquet–Langlands correspondence are proved instances. Transfer of symmetric powers from GL(2) to GL(n + 1), in potential form, is what proved the Sato–Tate distribution of the a_p.

7. **The fundamental lemma unlocked the trace formula.** The Arthur–Selberg trace formula compares automorphic representations of different groups by comparing sums over conjugacy classes, but this "stabilisation" needs a combinatorial identity between orbital integrals called the fundamental lemma. Despite its name it resisted decades of effort. Ngô Bảo Châu proved it in 2008, published in 2010, by a geometric study of the Hitchin fibration, and received a Fields Medal in 2010.

8. **Geometric Langlands reflects the arithmetic version.** Weil's analogy runs from number fields to function fields of curves over finite fields to Riemann surfaces. In the last setting the programme becomes the geometric Langlands conjecture, an equivalence between categories of sheaves attached to G-bundles on a curve and to local systems for the dual group. A proof of the main conjecture over ℂ, spread over several long papers, was announced in 2024 by Gaitsgory, Raskin and collaborators. The arithmetic conjectures over number fields, reciprocity and functoriality in general, remain open as of 2026.

## Key concepts

| Term | Meaning |
|---|---|
| Galois representation | A homomorphism from a Galois group to GL(n) |
| Automorphic representation | An irreducible piece of functions on G(ℚ)\G(𝔸) |
| Reciprocity | Galois representations match automorphic ones with equal L-functions |
| Dual group Ĝ | The group whose representations index transfers; GL(n) is self-dual |
| Functoriality | Transfer of automorphic representations along maps of dual groups |
| Trace formula | Spectral sum equals geometric sum over conjugacy classes |
| Fundamental lemma | Identity of orbital integrals needed to stabilise the trace formula |
| Geometric Langlands | The analogue for curves over ℂ, stated with categories of sheaves |

## How it fits

- **Below:** [class field theory](../01-algebraic-number-theory/class-field-theory.md) is the GL(1) case; [modular forms](modular-forms.md) and [modularity](fermats-last-theorem.md) the GL(2) case; [representations of Lie groups](../../08-geometry/04-lie-theory/representations-of-lie-groups.md) provide the local theory at the real place.
- **Above:** the general conjectures are central [open problems](../../15-mathematics-in-context/open-problems.md); the geometric version is written in the derived and [higher categories](../../13-structure-and-metamathematics/01-category-theory/higher-categories-and-homotopy-type-theory.md) of layer 13.
- **Siblings:** [Dirichlet L-functions](../02-analytic-number-theory/primes-in-arithmetic-progressions.md) are the simplest automorphic L-functions; [elliptic curves](elliptic-curves.md) are the test case for reciprocity.

## Common misconceptions

- **"It is one conjecture"**: it is a family of conjectures, reciprocity, functoriality and local and geometric versions, with many proved cases.
- **"The geometric proof settles the number-theoretic conjectures"**: it concerns curves over ℂ; the arithmetic conjectures are open as of 2026.
- **"Fermat's Last Theorem was the goal"**: it was one consequence of one case.

## Go deeper

- Stephen Gelbart, "An elementary introduction to the Langlands program", *Bulletin of the American Mathematical Society* (1984): the classic survey.
- Edward Frenkel, *Love and Math* (2013): the programme and its geometric side for a general reader.
- Daniel Bump, *Automorphic Forms and Representations* (1997): GL(2) in full, from modular forms to adelic representations.
