# Fermat's Last Theorem

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Elliptic Curves and Modular Forms](README.md)
> **Builds on:** [Elliptic Curves](elliptic-curves.md), [Modular Forms](modular-forms.md), [Ideals and the Class Group](../01-algebraic-number-theory/ideals-and-the-class-group.md), [p-adic Numbers and Local Fields](../01-algebraic-number-theory/p-adic-numbers-and-local-fields.md), [Schemes](../03-algebraic-geometry/schemes.md)
> **Enables:** [The Langlands Programme](the-langlands-programme.md), [History of Mathematics](../../15-mathematics-in-context/history-of-mathematics.md), [Mathematical Practice and Discovery](../../15-mathematics-in-context/mathematical-practice-and-discovery.md)

## Essence

Fermat's Last Theorem (FLT) states that xⁿ + yⁿ = zⁿ has no solutions in positive integers when n ≥ 3. Fermat wrote it in a margin around 1637, claiming a proof that the margin could not contain; it took until 1994. The proof does not attack the equation directly. Instead a hypothetical solution is turned into an elliptic curve so strange that it cannot be modular, and then all semistable elliptic curves over ℚ are shown to be modular. The theorem became a corollary of a much larger statement linking elliptic curves and modular forms, and the methods built for it now drive the Langlands programme.

## Core tenets

1. **It suffices to treat n = 4 and odd primes.** Any n ≥ 3 is divisible by 4 or by an odd prime p, and a solution for n gives one for each divisor. Fermat himself handled n = 4 by infinite descent: a solution produces a smaller one, which is impossible for positive integers. Euler treated n = 3 in 1770, and further exponents were settled one at a time in the nineteenth century.

2. **Kummer's ideals reached the regular primes.** Over ℤ[ζ_p] the equation factors as zᵖ = ∏ (x + ζʲy), and if that ring had unique factorisation each factor would be nearly a p-th power. Unique factorisation fails, but Kummer showed in the 1840s that ideal factorisation suffices when p does not divide the class number: the regular primes of [the class group](../01-algebraic-number-theory/ideals-and-the-class-group.md). The irregular primes, starting with 37, resisted, and no general argument emerged from this route.

3. **A solution would give the Frey curve.** Suppose aᵖ + bᵖ = cᵖ with p ≥ 5 prime and a, b, c coprime. Hellegouarch had studied the curve

   ```
   E: y² = x(x − aᵖ)(x + bᵖ)
   ```

   and Frey suggested in the mid-1980s that it could not be modular. Its discriminant is 16(abc)^(2p), almost a perfect p-th power, so it is semistable and its points of order p form a Galois representation ramified in a way so restricted that it ought to come from a modular form of level 2. Serre made this precise in his conjectures on modular Galois representations.

4. **Ribet showed modularity would forbid it (1986).** Ribet proved the needed level-lowering theorem: if the Frey curve were modular, its mod p representation would come from a weight-2 cusp form of level 2. The modular curve X₀(2) has genus 0, so there are no such forms. So FLT follows from the statement that semistable elliptic curves over ℚ are modular, part of the Taniyama–Shimura–Weil conjecture.

5. **Wiles proved modularity by proving R = T.** Start from the representation on the 3-torsion points E[3]. Its image lies in GL₂(𝔽₃), a solvable group, so the Langlands–Tunnell theorem shows that it comes from a modular form. The hard step lifts this to all of the 3-adic Tate module. Wiles compared a ring R parametrising all suitable [3-adic](../01-algebraic-number-theory/p-adic-numbers-and-local-fields.md) lifts of the representation with a Hecke ring T parametrising the modular ones, and showed R = T by a numerical criterion. When E[3] is not irreducible, a "3–5 switch" uses E[5] and an auxiliary curve.

6. **A gap, a repair, and publication.** Wiles announced the proof in June 1993 in lectures at the Isaac Newton Institute in Cambridge. A gap appeared later that year in the argument that bounded a Selmer group. In September 1994 Wiles, working with Taylor, found a way around it, the Taylor–Wiles patching method. The proof appeared in 1995 in the *Annals of Mathematics*, as Wiles's long paper and a joint paper of Taylor and Wiles.

7. **The full modularity theorem followed in 2001.** Breuil, Conrad, Diamond and Taylor extended the method to every elliptic curve over ℚ, semistable or not, completing the Taniyama–Shimura–Weil conjecture. Every elliptic curve over ℚ therefore has an L-function with analytic continuation and functional equation, the starting point for the known cases of the [Birch and Swinnerton-Dyer conjecture](elliptic-curves.md).

8. **The methods outlived the theorem.** Modularity lifting theorems of Taylor–Wiles type became a standard tool. Khare and Wintenberger used them to prove Serre's modularity conjecture for two-dimensional mod p representations, published in 2009. Variants prove modularity over other fields and potential modularity, which gave the Sato–Tate theorem. Each is a case of the reciprocity predicted by [the Langlands programme](the-langlands-programme.md).

## Key concepts

| Term | Meaning |
|---|---|
| Regular prime | A prime p not dividing the class number of ℚ(ζ_p) |
| Frey curve | y² = x(x − aᵖ)(x + bᵖ) built from a putative solution |
| Semistable curve | One whose reduction at each prime has at worst a node |
| Galois representation | The action of Gal(ℚ̄/ℚ) on torsion points, as matrices |
| Level lowering | Ribet's theorem removing primes from the level of a modular form |
| R = T | Deformation ring equals Hecke ring: every lift is modular |
| Modularity theorem | Every elliptic curve over ℚ is modular (2001) |

## How it fits

- **Below:** [Kummer's theory](../01-algebraic-number-theory/ideals-and-the-class-group.md) gave the first general results; [elliptic curves](elliptic-curves.md) and [modular forms](modular-forms.md) are the two sides of the proof; [schemes](../03-algebraic-geometry/schemes.md) give the language of reduction mod p.
- **Above:** a standard case study in [the history of mathematics](../../15-mathematics-in-context/history-of-mathematics.md) and in [how mathematics is done](../../15-mathematics-in-context/mathematical-practice-and-discovery.md), including how a published claim is checked and repaired.
- **Siblings:** modularity is the GL(2) case of [Langlands reciprocity](the-langlands-programme.md).

## Common misconceptions

- **"Wiles proved FLT directly"**: he proved modularity of semistable curves; FLT follows through Frey and Ribet.
- **"Fermat had a valid proof"**: no proof by him is known for general n, and most historians doubt he had one.
- **"The result matters for its own sake"**: the equation has no applications; the methods created for it are what changed number theory.

## Go deeper

- Gary Cornell, Joseph H. Silverman and Glenn Stevens (editors), *Modular Forms and Fermat's Last Theorem* (1997): the proof expounded by many hands.
- Henri Darmon, Fred Diamond and Richard Taylor, "Fermat's Last Theorem", in *Current Developments in Mathematics* (1995): the standard survey.
- Simon Singh, *Fermat's Last Theorem* (1997): the history for a general reader.
