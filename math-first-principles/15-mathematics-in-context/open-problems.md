# Open Problems

> **Layer:** [15 Mathematics in Context](README.md)
> **Builds on:** [The Riemann Zeta Function](../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md), [Sieves and Additive Problems](../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/sieves-and-additive-problems.md), [Elliptic Curves](../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/elliptic-curves.md), [Three-Manifolds and the Poincaré Conjecture](../07-topology/03-manifolds/three-manifolds-and-the-poincare-conjecture.md), [Undecidable Problems](../13-structure-and-metamathematics/02-computability-and-incompleteness/undecidable-problems.md)
> **Enables:** [Mathematics and Society](mathematics-and-society.md), [P, NP and NP-Completeness (CS)](../../cs-first-principles/02-theory-of-computation/04-complexity/p-np-and-np-completeness.md)

## Essence

Some questions resist every attack for decades or centuries, and naming them organises research: Hilbert's list of 1900 shaped twentieth-century mathematics, and the Clay Mathematics Institute (CMI) announced seven Millennium Prize Problems on 24 May 2000, each carrying a prize of one million US dollars. As of 2026 only one, the Poincaré conjecture, has been solved. Other famous problems are simple to state, such as the twin prime and Goldbach conjectures, and their difficulty lies in controlling how primes behave additively. What is known is as instructive as what is not: partial results, barriers explaining why methods fail, and one disputed claimed proof. Every status below is as of 2026.

## Core tenets

1. **The seven Millennium problems span the subject.**

   | Problem | Question | Status as of 2026 |
   |---|---|---|
   | Riemann hypothesis | Do all non-trivial zeros of the zeta function have real part ½? | Open |
   | P versus NP | Can every problem whose solutions are quickly checked also be quickly solved? | Open |
   | Navier–Stokes | Do smooth solutions of the three-dimensional fluid equations exist for all time? | Open |
   | Yang–Mills and mass gap | Does quantum Yang–Mills theory exist rigorously, with a positive mass gap? | Open |
   | Hodge conjecture | Are Hodge classes on projective varieties combinations of algebraic cycles? | Open |
   | Birch and Swinnerton-Dyer | Does the rank of an elliptic curve equal the order of vanishing of its L-function at 1? | Open |
   | Poincaré conjecture | Is every simply connected closed three-manifold a sphere? | Solved by Perelman |

2. **Each open Millennium problem has substantial partial results.** For the Riemann hypothesis, Brian Conrey (1989) showed more than 40% of the zeros lie on the critical line, and very many have been checked numerically. For P versus NP, three barriers (relativisation, natural proofs and algebrisation) show that broad classes of techniques cannot settle it. For Navier–Stokes, Jean Leray (1934) proved weak solutions exist for all time, and Luis Caffarelli, Robert Kohn and Louis Nirenberg (1982) showed any singular set is very small; the two-dimensional case is solved. For the Hodge conjecture, the Lefschetz theorem settles the case of (1,1) classes. For Birch and Swinnerton-Dyer, work of Benedict Gross, Don Zagier and Victor Kolyvagin proves it when the L-function vanishes to order at most 1, and Manjul Bhargava with coauthors showed that a positive proportion of elliptic curves satisfy it. Yang–Mills is furthest from resolution: no interacting quantum field theory in four dimensions has been rigorously constructed.

3. **The Poincaré conjecture fell to geometry.** Grigori Perelman posted three papers in 2002–2003 completing Richard Hamilton's programme of deforming a metric by the Ricci flow and cutting out singularities. The proof was checked by several teams over the following years. Perelman declined the Fields Medal in 2006 and the Clay prize in 2010.

4. **Twin primes: bounded gaps are proved, gap 2 is open.** The conjecture says infinitely many primes p have p + 2 prime. Chen Jingrun (1973) proved infinitely many primes p have p + 2 either prime or a product of two primes. Yitang Zhang (2013) proved that some gap below 70,000,000 occurs infinitely often; James Maynard's method and the Polymath project lowered this to 246. Sieve methods face a "parity barrier" that prevents them alone from reaching 2.

5. **Goldbach: the weak form is proved, the strong form is open.** The conjecture says every even number greater than 2 is a sum of two primes. It has been checked by computer up to 4 × 10¹⁸. Ivan Vinogradov (1937) proved every sufficiently large odd number is a sum of three primes, and Harald Helfgott's 2013 proof of this for every odd number above 5 is widely accepted. Chen also proved every large even number is a prime plus a number with at most two prime factors.

6. **Collatz: easy to state, possibly beyond current methods.** Iterate n ↦ n/2 if n is even, n ↦ 3n + 1 if odd; the conjecture says every starting value reaches 1. It has been checked for all starting values below about 2⁶⁸. Terence Tao (2019) proved that almost all orbits, in a logarithmic density sense, reach values almost bounded. John Conway (1972) showed that a natural generalisation of such iterations is undecidable, so no uniform method settles all problems of this shape.

7. **The abc conjecture has a disputed claimed proof.** Formulated by David Masser and Joseph Oesterlé in 1985, it says that for each ε > 0 only finitely many coprime triples a + b = c have c greater than rad(abc)^(1 + ε), where rad multiplies the distinct primes dividing abc. In 2012 Shinichi Mochizuki claimed a proof via his inter-universal Teichmüller theory, published in 2021 in a journal he edits. In 2018 Peter Scholze and Jakob Stix identified what they consider a fatal gap in a key corollary. As of 2026 the proof is not accepted by most experts, and the conjecture is generally regarded as open.

## Key concepts

| Term | Meaning |
|---|---|
| Millennium Prize Problems | Seven problems named by the Clay Mathematics Institute in 2000 |
| Critical line | The line of complex numbers with real part ½ |
| Barrier | A theorem showing a class of proof methods cannot resolve a problem |
| Mass gap | A positive lower bound on the energy of particle states above the vacuum |
| Weak solution | A solution satisfying an equation in an averaged, integrated sense |
| Parity barrier | The inability of sieves to distinguish numbers with odd and even counts of prime factors |
| Radical rad(n) | The product of the distinct primes dividing n |

## How it fits

- **Below:** the zeta function, sieves, elliptic curves and three-manifolds supply the problems; undecidability shows that some questions of this kind have no general solution.
- **Above:** nothing; this is the top layer.
- **Siblings:** [practice](mathematical-practice-and-discovery.md) describes how partial progress accumulates; [computers and proof](computers-and-proof.md) supplies verification and search; [history](history-of-mathematics.md) records problems such as Fermat's last theorem that did fall.

## Common misconceptions

- **"Checking a conjecture up to huge numbers makes it nearly certain."** Prime-counting inequalities have failed far beyond any computation; checks rule out small counterexamples only.
- **"Mochizuki proved abc."** His claim is published but not accepted by most experts as of 2026.
- **"Open means no progress."** Each problem has deep partial results and barriers that guide research.

## Go deeper

- J. Carlson, A. Jaffe and A. Wiles (eds), *The Millennium Prize Problems* (2006): the official problem descriptions by leading experts.
- R. K. Guy, *Unsolved Problems in Number Theory* (3rd ed., 2004): a compendium with references.
- J. C. Lagarias (ed.), *The Ultimate Challenge: The 3x+1 Problem* (2010): surveys of the Collatz problem.
