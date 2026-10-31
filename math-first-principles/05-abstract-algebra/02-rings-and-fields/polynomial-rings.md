# Polynomial Rings

> **Layer:** [05 Abstract Algebra](../README.md) › [Rings and Fields](README.md)
> **Builds on:** [Rings and Ideals](rings-and-ideals.md), [Factorisation in Integral Domains](factorisation-in-integral-domains.md), [The Complex Numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md)
> **Enables:** [Field Extensions](field-extensions.md), [Finite Fields](finite-fields.md), [Solvability by Radicals](../03-galois-theory/solvability-by-radicals.md), [Commutative Rings and Localisation](commutative-rings-and-localisation.md), [Varieties and the Nullstellensatz](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/varieties-and-the-nullstellensatz.md), [Error-Correcting Codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md)

## Essence

A polynomial over a ring R is a formal expression a₀ + a₁x + ⋯ + aₙxⁿ, a finite list of coefficients, not a function. Over a field F the ring F[x] behaves like ℤ: it has division with remainder, greatest common divisors and unique factorisation into irreducible polynomials. Irreducible polynomials play the role of primes, and dividing by one gives a field, which is how new roots are manufactured: ℂ = ℝ[x]/(x² + 1). Gauss's lemma and Eisenstein's criterion decide irreducibility over ℚ in many cases, and Hilbert's basis theorem shows that every system of polynomial equations in finitely many variables reduces to finitely many. This leaf is the toolkit on which field theory and Galois theory run.

## Core tenets

1. **Polynomials are formal sequences of coefficients, not functions.** Over the field 𝔽ₚ = ℤ/p, the polynomial xᵖ − x is not zero, yet it vanishes at every element by Fermat's little theorem. Two polynomials are equal when their coefficients are; distinct polynomials can define the same function over a finite ring. Over an infinite field the distinction disappears, because a non-zero polynomial has only finitely many roots.

2. **Degrees add over a domain.** If R is an integral domain, the leading coefficient of fg is the product of the leading ones, so deg(fg) = deg f + deg g, R[x] is a domain and its units are the units of R. With zero divisors this fails: in ℤ/4, (2x + 1)² = 4x² + 4x + 1 = 1, so a degree-1 polynomial is a unit.

3. **F[x] over a field is a Euclidean domain, hence a principal ideal domain (PID) and a unique factorisation domain (UFD).** Long division gives f = qg + r with deg r < deg g, because leading coefficients can be inverted. Hence every ideal is (g) for a single g, greatest common divisors come from the Euclidean algorithm, and factorisation into irreducibles is unique up to constant factors. The remainder on division by x − a is f(a), so a is a root if and only if x − a divides f (the factor theorem).

4. **A non-zero polynomial of degree n over a domain has at most n roots.** Each root splits off a factor x − a, and in a domain a product vanishes only if a factor does. Without the domain hypothesis it fails: x² − 1 has four roots, 1, 3, 5 and 7, in ℤ/8. Commutativity matters too: x² + 1 has infinitely many roots among the quaternions, such as every unit pure quaternion.

5. **F[x]/(f) is a field if and only if f is irreducible.** Irreducible f generates a maximal ideal in a PID, so the quotient is a field, of dimension deg f over F, in which the class of x is a root of f (Kronecker's construction). If f = gh is a proper factorisation, then g and h become zero divisors. Examples: ℝ[x]/(x² + 1) ≅ ℂ, and 𝔽₂[x]/(x² + x + 1) is the field 𝔽₄ with four elements.

6. **Gauss's lemma: if R is a UFD, so is R[x], and a polynomial over ℤ that factors over ℚ already factors over ℤ.** Call a polynomial primitive if its coefficients have no common prime factor. If a prime p divided every coefficient of fg, reducing mod p would give f̄ḡ = 0 in the domain (R/p)[x], so p divides all coefficients of f or of g. Hence products of primitive polynomials are primitive, and denominators can be cleared from any rational factorisation. By induction ℤ[x₁, …, xₙ] and F[x₁, …, xₙ] are UFDs.

7. **Eisenstein's criterion: if a prime p divides every coefficient of f except the leading one, and p² does not divide the constant term, then f is irreducible over ℚ.** Reduced mod p, f becomes c·xⁿ. A factorisation f = gh would reduce to a product of monomials, so p would divide the constant terms of both g and h, and p² would divide f's constant term. Examples: xⁿ − 2 for every n, x⁵ − 6x + 3 with p = 3, and the cyclotomic polynomial Φₚ(x) = xᵖ⁻¹ + ⋯ + x + 1 after substituting x + 1 for x.

8. **Hilbert's basis theorem: if R is Noetherian, so is R[x].** A ring is Noetherian when every ideal is finitely generated. The proof takes, degree by degree, the ideals of leading coefficients and generates them finitely. So every ideal of F[x₁, …, xₙ] is finitely generated, and any system of polynomial equations is equivalent to a finite one. Hilbert's 1890 proof was famously non-constructive; Gröbner bases later made it computable.

## Key concepts

| Term | Meaning |
|---|---|
| R[x] | Formal polynomials with coefficients in R |
| Degree | The highest power with non-zero coefficient |
| Monic | Leading coefficient 1 |
| Irreducible polynomial | Non-constant, with no factorisation into two of lower degree |
| Primitive polynomial | Coefficients with no common prime factor |
| Eisenstein's criterion | A prime-divisibility test for irreducibility over ℚ |
| Noetherian ring | One in which every ideal is finitely generated |
| Formal derivative | f′ = ∑ k·aₖxᵏ⁻¹; a repeated root of f is a root of f′ |

## How it fits

- **Below:** [the complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md) reappear as ℝ[x]/(x² + 1), and polynomial division mirrors division with remainder in ℤ.
- **Above:** polynomial ideals describe [varieties](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/varieties-and-the-nullstellensatz.md); cyclic codes such as Reed–Solomon codes are ideals in 𝔽_q[x]/(xⁿ − 1), the core of [error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md).
- **Siblings:** [field extensions](field-extensions.md) are built as F[x]/(f); [finite fields](finite-fields.md) come from irreducible polynomials over 𝔽ₚ; [solvability by radicals](../03-galois-theory/solvability-by-radicals.md) needs Eisenstein for x⁵ − 6x + 3; [commutative rings and localisation](commutative-rings-and-localisation.md) build on Hilbert's basis theorem to study Noetherian rings and their dimension.

## Common misconceptions

- **"A polynomial is a function."** Over 𝔽ₚ, xᵖ − x and 0 agree as functions but are different polynomials.
- **"A polynomial of degree n has at most n roots in any ring."** It needs a commutative domain: ℤ/8 and the quaternions both break it.
- **"Irreducible means no roots."** That test works only for degree 2 and 3. (x² + 1)² has no real roots but is reducible over ℝ.

## Go deeper

- David Dummit and Richard Foote, *Abstract Algebra* (3rd edition, 2004): polynomial rings, Gauss's lemma and irreducibility criteria.
- David Cox, John Little and Donal O'Shea, *Ideals, Varieties, and Algorithms* (4th edition, 2015): polynomial ideals made computable through Gröbner bases.
