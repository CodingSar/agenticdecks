# Cryptography

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Information, Codes and Cryptography](README.md)
> **Builds on:** [Fermat, Euler and Primitive Roots](../../02-number-systems/02-elementary-number-theory/fermat-euler-and-primitive-roots.md), [Finite Fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md), [Elliptic Curves](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/elliptic-curves.md), [Lattices and Sphere Packing](../../08-geometry/03-convex-and-discrete-geometry/lattices-and-sphere-packing.md), [Information Theory](information-theory.md)
> **Enables:** [Mathematics and Society](../../15-mathematics-in-context/mathematics-and-society.md), [Public-Key Cryptography (CS)](../../../cs-first-principles/11-security-and-cryptography/02-cryptography/public-key-cryptography.md), [Foundations of Modern Cryptography (CS)](../../../cs-first-principles/11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md)

## Essence

Cryptography makes communication secure against an adversary. Its mathematical turn came in two steps. Claude Shannon (1949) defined perfect secrecy and showed it needs a key as long as the message. Then Whitfield Diffie and Martin Hellman (1976) showed that two strangers can agree on a secret over a public line, provided some functions are easy to compute but hard to invert. Public-key cryptography rests on a handful of number-theoretic problems: factoring integers, and discrete logarithms in multiplicative groups of finite fields and in elliptic curve groups. Peter Shor's quantum algorithm (1994) solves all of these, which is why new standards based on lattices and hash functions were published in 2024.

## Core tenets

1. **Perfect secrecy is possible but expensive.** A cipher is perfectly secret if the ciphertext gives no information about the message: their mutual information is zero. The one-time pad, adding a uniformly random key bit to each message bit modulo 2, achieves it, and Shannon proved that any perfectly secret scheme needs at least as many key bits, in entropy, as message bits. Practical cryptography therefore settles for computational security: no efficient adversary can break the scheme with more than negligible probability.

2. **Computational security rests on unproved hardness.** A one-way function is easy to compute and hard to invert on random inputs. Its existence is equivalent to that of pseudorandom generators and of secure digital signatures, and it would imply P ≠ NP (polynomial time differs from nondeterministic polynomial time). Whether one-way functions exist is open as of 2026, so every security proof is conditional: it reduces breaking the scheme to solving a problem believed hard.

3. **Diffie–Hellman key exchange uses discrete logarithms.** Fix a prime p and a primitive root g modulo p. Alice sends gᵃ, Bob sends gᵇ, and each computes gᵃᵇ, while an eavesdropper sees only gᵃ and gᵇ. Recovering a from gᵃ is the discrete logarithm problem. In a group of prime order q, generic algorithms such as Pollard's rho method take about √q operations, and Victor Shoup (1997) proved that no algorithm using only the group operations can do essentially better. The multiplicative group of a finite field is not generic: index calculus factors elements over small primes and solves discrete logarithms in subexponential time, forcing keys of thousands of bits. At the British Government Communications Headquarters, James Ellis, Clifford Cocks (1973) and Malcolm Williamson had found equivalent ideas earlier, declassified in 1997.

4. **RSA encryption rests on Euler's theorem and the difficulty of factoring.** In RSA, named from the initials of Ronald Rivest, Adi Shamir and Leonard Adleman (1977), one chooses primes p and q, publishes n = pq and an exponent e, and keeps d with ed ≡ 1 modulo (p − 1)(q − 1). Encryption is m ↦ mᵉ mod n; decryption is c ↦ cᵈ mod n, which returns m by Euler's theorem. Knowing p and q gives d, so factoring breaks RSA; whether breaking RSA requires factoring is open as of 2026. The number field sieve factors in time roughly exp(c (log n)^(1/3) (log log n)^(2/3)); the 829-bit challenge number RSA-250 was factored in 2020.

5. **Elliptic curves give the same security with smaller keys.** Neal Koblitz and Victor Miller independently proposed (1985) doing Diffie–Hellman in the group of points of an elliptic curve over a finite field. By Hasse's theorem the group has about p points, within 2√p, and for well-chosen curves no algorithm better than the generic √q one is known, so a 256-bit curve offers security comparable to a 3,072-bit RSA modulus.

6. **Quantum computers would break all of these.** Shor (1994) gave polynomial-time quantum algorithms for factoring and discrete logarithms in any finite abelian group, including elliptic curve groups, by finding the period of a function with the quantum Fourier transform. Lov Grover's search algorithm (1996) gives only a square-root speedup against symmetric ciphers, so doubling key lengths suffices there. As of 2026 no quantum computer has run Shor's algorithm on numbers of cryptographic size.

7. **Post-quantum cryptography uses lattices and hash functions.** In learning with errors (Oded Regev, 2005), one must find a secret vector s from A and As + e modulo q, where e is small noise; Regev showed that solving random instances would solve worst-case lattice problems, such as approximating short vectors, for which no efficient quantum algorithm is known. In August 2024 the United States National Institute of Standards and Technology published three standards: the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM), the Module-Lattice-Based Digital Signature Algorithm (ML-DSA), and the Stateless Hash-Based Digital Signature Algorithm (SLH-DSA), whose security rests only on hash functions. Caution is warranted: a candidate based on isogenies of elliptic curves, the Supersingular Isogeny Key Encapsulation, was broken classically in 2022.

## Key concepts

| Term | Meaning |
|---|---|
| Perfect secrecy | Ciphertext independent of plaintext; needs key entropy at least message entropy |
| One-way function | Easy to compute, hard to invert on random inputs |
| Discrete logarithm | Recovering a from gᵃ in a cyclic group |
| Generic group | A model in which algorithms use only the group operations, forcing about √q steps |
| Learning with errors | Recovering s from noisy linear equations As + e modulo q |

## How it fits

- **Below:** RSA and Diffie–Hellman use [Fermat's and Euler's theorems and primitive roots](../../02-number-systems/02-elementary-number-theory/fermat-euler-and-primitive-roots.md) and [finite fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md); elliptic curve cryptography uses the group law on [elliptic curves](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/elliptic-curves.md); post-quantum schemes rest on hard problems about [lattices](../../08-geometry/03-convex-and-discrete-geometry/lattices-and-sphere-packing.md); perfect secrecy is a statement of [information theory](information-theory.md).
- **Above:** cryptography's public role, from secure commerce to state surveillance, is discussed in [mathematics and society](../../15-mathematics-in-context/mathematics-and-society.md); protocols and implementations are in [public-key cryptography](../../../cs-first-principles/11-security-and-cryptography/02-cryptography/public-key-cryptography.md) and [foundations of modern cryptography](../../../cs-first-principles/11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md); Shor's algorithm is treated in [quantum algorithms](../../../cs-first-principles/02-theory-of-computation/05-quantum-computation/quantum-algorithms.md).
- **Siblings:** Robert McEliece's cryptosystem (1978) hides a decodable [error-correcting code](error-correcting-codes.md) as a random-looking one, and remains unbroken by quantum algorithms.

## Common misconceptions

- **"Cryptography is proved secure"**: security proofs are reductions to problems believed hard; none of the underlying assumptions has been proved, and some, such as those behind the isogeny scheme above, have failed.
- **"Quantum computers break all cryptography"**: Shor's algorithm breaks factoring and discrete logarithms; symmetric ciphers and hash functions lose only a square root, and lattice-based schemes have no known quantum attack.

## Go deeper

- Jonathan Katz and Yehuda Lindell, *Introduction to Modern Cryptography* (3rd edition, 2020): definitions and proofs.
- Jeffrey Hoffstein, Jill Pipher and Joseph H. Silverman, *An Introduction to Mathematical Cryptography* (2nd edition, 2014): number theory, elliptic curves and lattices.
- Neal Koblitz, *A Course in Number Theory and Cryptography* (2nd edition, 1994): a concise mathematical introduction.
