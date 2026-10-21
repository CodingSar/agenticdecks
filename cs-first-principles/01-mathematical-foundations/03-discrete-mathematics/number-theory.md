# Number Theory

> **Layer:** [01 Mathematical Foundations](../README.md) › [Discrete Mathematics](README.md)
> **Builds on:** [Proof Techniques](../01-logic/proof-techniques.md), [Relations and Orders](../02-sets-relations-functions/relations-and-orders.md)
> **Enables:** [Abstract Algebra](../04-algebra/abstract-algebra.md), [Public-Key Cryptography](../../11-security-and-cryptography/02-cryptography/public-key-cryptography.md), [Integers and Two's Complement](../../03-digital-logic/01-number-representation/integers-and-twos-complement.md), [Hash Tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md), [Quantum Algorithms](../../02-theory-of-computation/05-quantum-computation/quantum-algorithms.md)

## Essence

Number theory studies the integers: divisibility, primes, remainders and the arithmetic of "clock" systems where numbers wrap around. For a computer scientist it matters for three reasons. Machine integers *are* modular arithmetic: a 32-bit register computes modulo 2^32. Hashing, checksums and pseudo-random generators use remainders to spread values evenly. And public-key cryptography rests on a striking asymmetry: some number-theoretic operations (multiplying primes, raising to a power modulo *n*) are fast, while their inverses (factoring, discrete logarithm) appear to be infeasible for classical computers. The central tool is modular arithmetic, where congruence modulo *n* turns infinitely many integers into *n* residue classes that can be added and multiplied consistently.

## Core tenets

1. **Division with remainder is unique, and that defines `mod`.** For integers *a* and *n > 0* there are unique *q* and *r* with *a = qn + r* and *0 ≤ r < n*. Programming languages disagree on the sign of `%` for negative operands (C truncates toward zero, Python floors), a practical trap when computing hash buckets or array indices from signed values.

2. **Congruence mod *n* is an equivalence that respects + and ×.** *a ≡ b (mod n)* when *n* divides *a − b*. If *a ≡ a'* and *b ≡ b'*, then *a + b ≡ a' + b'* and *ab ≡ a'b'*. So you can reduce intermediate results at every step and still get the right final remainder. This is why a Central Processing Unit (CPU) can discard carries beyond bit 31 and still compute correct low bits, and why [two's complement](../../03-digital-logic/01-number-representation/integers-and-twos-complement.md) addition is the same circuit for signed and unsigned numbers.

3. **Euclid's algorithm computes the greatest common divisor in logarithmic steps.** gcd(a, b) = gcd(b, a mod b), and the remainders shrink at least by half every two steps, so the number of steps is O(log min(a, b)). The *extended* version also finds integers *x, y* with *ax + by = gcd(a, b)*. When gcd(a, n) = 1, this gives *x* with *ax ≡ 1 (mod n)*, the modular inverse that Rivest–Shamir–Adleman (RSA) key generation needs.

4. **Primes are the multiplicative atoms, and factorisation is unique.** Every integer above 1 is a product of primes in exactly one way (the fundamental theorem of arithmetic). Primes are plentiful: about n/ln n of them lie below *n*, so a random 1,024-bit odd number is prime with probability about 1/355. Primality is testable quickly (Miller–Rabin in randomized polynomial time; the Agrawal–Kayal–Saxena (AKS) test deterministically, 2002), but no known classical algorithm factors large products of two primes quickly. RSA's security rests on that gap.

5. **Arithmetic mod a prime is a field.** When *p* is prime, every non-zero residue has a multiplicative inverse, so you can divide. Fermat's little theorem says *a^(p−1) ≡ 1 (mod p)* for *a* not divisible by *p*; Euler's theorem generalises it to *a^φ(n) ≡ 1 (mod n)* when gcd(a, n) = 1. RSA works because encryption *m^e* and decryption *c^d* with *ed ≡ 1 (mod φ(n))* undo each other. Finite fields also underlie Reed–Solomon codes and elliptic-curve cryptography (see [abstract algebra](../04-algebra/abstract-algebra.md)).

6. **Modular exponentiation is fast; its inverse appears hard.** Computing *g^x mod p* takes O(log x) multiplications by repeated squaring, so a 2,048-bit exponent needs only a few thousand modular multiplications. Recovering *x* from *g^x mod p* (the discrete logarithm problem) has no known efficient classical algorithm for well-chosen groups. This one-way asymmetry powers Diffie–Hellman key exchange and digital signatures. Shor's algorithm (1994) solves both factoring and discrete logarithm in polynomial time on a large quantum computer, which is why [post-quantum cryptography](../../11-security-and-cryptography/02-cryptography/public-key-cryptography.md) exists.

7. **The Chinese Remainder Theorem splits one modulus into several.** If *n = n₁n₂* with gcd(n₁, n₂) = 1, then a residue mod *n* corresponds exactly to a pair of residues mod *n₁* and mod *n₂*. Computations can be done in the smaller moduli in parallel and recombined. RSA implementations use it to speed decryption roughly fourfold.

8. **Remainders spread values, if the modulus is chosen well.** Hashing by *k mod m* distributes keys evenly only if *m* shares no structure with the keys: a power-of-two *m* uses only the low bits, so keys that differ only in high bits all collide. Linear congruential generators *x' = (ax + c) mod m* are fast but predictable, so they are unacceptable for cryptography.

## Key concepts

| Term | Meaning |
|---|---|
| Divisibility (a ∣ b) | b = ka for some integer k |
| Congruence | a ≡ b (mod n) when n divides a − b |
| gcd | Greatest common divisor; computed by Euclid's algorithm |
| Modular inverse | x with ax ≡ 1 (mod n); exists iff gcd(a, n) = 1 |
| Prime | Integer above 1 with no divisors except 1 and itself |
| Euler's totient φ(n) | Count of 1 ≤ k ≤ n coprime to n; φ(pq) = (p−1)(q−1) |
| Fermat's little theorem | a^(p−1) ≡ 1 (mod p) for prime p not dividing a |
| Discrete logarithm | Find x given g^x mod p |
| Chinese Remainder Theorem (CRT) | Residues mod coprime factors determine the residue mod their product |

## How it fits

- **Below:** Congruence is an [equivalence relation](../02-sets-relations-functions/relations-and-orders.md); results are proved with [induction and contradiction](../01-logic/proof-techniques.md).
- **Above:** [Abstract algebra](../04-algebra/abstract-algebra.md) generalises residues into groups, rings and fields. [Public-key cryptography](../../11-security-and-cryptography/02-cryptography/public-key-cryptography.md) is applied number theory. Machine [integer arithmetic](../../03-digital-logic/01-number-representation/integers-and-twos-complement.md) is arithmetic mod 2^w. [Hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) and [randomized algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md) use modular hashing. Cyclic Redundancy Checks (CRCs) and [error-correcting codes](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md) use polynomial remainders.
- **Siblings:** [Combinatorics](combinatorics.md) counts residues and coprime numbers; [induction](induction-and-recurrences.md) proves correctness and running time of Euclid's algorithm.

## Common misconceptions

- **"Factoring is proven hard."** It is not known to be NP-hard (as hard as everything in Nondeterministic Polynomial time) or even outside P classically; RSA relies on decades of failed attempts, not on a proof.
- **"`a % n` is always non-negative."** In C, C++, Java and Go it takes the sign of the dividend.
- **"Big primes are rare, so finding them is slow."** Density about 1/ln n plus fast probabilistic tests makes generating a 2,048-bit prime take milliseconds.

## Go deeper

- Victor Shoup, *A Computational Introduction to Number Theory and Algebra* (2nd ed., 2009): number theory with algorithms in view, free online.
- G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers* (1938, 6th ed. 2008): the classic reference.
- Ronald Rivest, Adi Shamir and Leonard Adleman, "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems" (1978): number theory becoming security.
