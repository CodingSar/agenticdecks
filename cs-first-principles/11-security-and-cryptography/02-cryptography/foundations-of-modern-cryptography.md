# Foundations of Modern Cryptography

> **Layer:** [11 Security and Cryptography](../README.md) › [Cryptography](README.md)
> **Builds on:** [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Complexity classes](../../02-theory-of-computation/04-complexity/complexity-classes.md), [Entropy and information](../../02-theory-of-computation/01-information-theory/entropy-and-information.md), [Security design principles](../01-security-principles/security-design-principles.md)
> **Enables:** [Symmetric encryption](symmetric-encryption.md), [Hash functions and message authentication codes](hash-functions-and-macs.md), [Public-key cryptography](public-key-cryptography.md)

## Essence

Modern cryptography, as developed from the late 1970s onward, rests on three steps. First, a **precise definition** of what it means to break a scheme, written as a game between a challenger and an adversary with stated powers. Second, a **precise assumption**, such as "no efficient algorithm factors products of two large random primes". Third, a **proof by reduction**: any efficient adversary that wins the game with non-negligible advantage can be turned into an efficient algorithm that breaks the assumption. This gives *computational* security, which is weaker than Shannon's *perfect* secrecy but achievable with short keys. Its practical meaning is that security claims are conditional, specific and checkable, not a matter of confidence in clever design.

## Core tenets

1. **Perfect secrecy exists but is impractical.** Shannon (1949) defined perfect secrecy: the ciphertext reveals nothing about the plaintext, so the posterior distribution of the message equals the prior. The one-time pad (exclusive-or (XOR) the message with a uniformly random key of equal length, used once) achieves it, and Shannon proved any perfectly secret scheme needs at least as many key bits of entropy as message bits. Keys that long must be distributed and never reused (reuse leaks the XOR of two messages), so practical cryptography accepts computational security instead.

2. **Computational security bounds the adversary's resources and success.** A scheme is (t, ε)-secure if every adversary running in time at most t succeeds with advantage at most ε over guessing. Asymptotically: every probabilistic polynomial-time adversary has negligible advantage, meaning smaller than the inverse of any polynomial in the security parameter. Concretely, "128-bit security" means the best known attack needs on the order of 2¹²⁸ operations, far beyond any foreseeable computation (about 10³⁸).

3. **Indistinguishability is the right notion of secrecy.** IND-CPA (indistinguishability under chosen-plaintext attack): the adversary may encrypt messages of its choice, then submits two equal-length messages, receives the encryption of one chosen at random, and must guess which. If it cannot do better than a coin flip (beyond negligible advantage), the ciphertext leaks no partial information. A consequence: secure encryption must be **randomised** or stateful, since a deterministic scheme lets the adversary encrypt both candidates and compare. IND-CCA (adding a decryption oracle for other ciphertexts) also rules out tampering-based attacks and is the standard target for public-key encryption.

4. **Integrity has its own definitions, separate from secrecy.** Encryption alone does not prevent modification: flipping a bit of a stream-cipher ciphertext flips the same plaintext bit. Existential unforgeability under chosen-message attack (EUF-CMA) says an adversary who has seen tags or signatures on messages of its choice cannot produce a valid one on any new message. Authenticated encryption combines IND-CPA with ciphertext integrity, and implies IND-CCA.

5. **Pseudorandomness is the core building block.** A pseudorandom generator stretches a short random seed into a long output no efficient test can distinguish from uniform. A pseudorandom function (PRF) is a keyed function that looks like a random function to anyone without the key; a pseudorandom permutation (PRP) is the invertible version and is the idealisation of a block cipher. Most symmetric constructions are proved secure assuming their underlying primitive is a PRF or PRP.

6. **Everything rests on one-way functions, whose existence is unproved.** A one-way function is easy to compute and hard to invert on random inputs. Their existence would imply P ≠ NP (some problems whose answers are easy to check are hard to solve), which is itself unproved, so all computational cryptography is conditional. In practice, assumptions are ranked by how much study they have survived: factoring and discrete logarithms (decades), the Advanced Encryption Standard (AES) as a PRP (since 1998), lattice problems (the basis of post-quantum schemes). Reductions also give concrete parameters: a loose reduction may require larger keys.

7. **Randomness quality is a security assumption.** Keys, nonces and many algorithms need unpredictable bits. A weak random number generator breaks otherwise perfect cryptography: the Debian OpenSSL bug (2006–2008) left only 32,768 possible keys per architecture and key type. Systems use the operating system's cryptographically secure generator, seeded from hardware events and entropy sources, never a general-purpose generator like `rand()`.

8. **Idealised models are useful but are not proofs about real functions.** The random oracle model treats a hash function as a truly random function available to all parties, which makes many practical schemes provable. Canetti, Goldreich and Halevi (1998) showed contrived schemes secure in this model but insecure with any real hash. Random-oracle proofs are strong heuristic evidence, and widely used schemes rely on them, but they are a weaker guarantee than a standard-model proof.

## Key concepts

| Term | Meaning |
|---|---|
| Perfect secrecy | Ciphertext gives zero information about plaintext |
| Security parameter | Size parameter (key length) against which efficiency and advantage are measured |
| Negligible function | Smaller than 1/p(n) for every polynomial p, for large n |
| Advantage | Adversary's success probability minus that of guessing |
| Reduction | Algorithm converting a scheme-breaker into an assumption-breaker |
| IND-CPA / IND-CCA | Indistinguishability under chosen-plaintext / chosen-ciphertext attack |
| EUF-CMA | Existential unforgeability under chosen-message attack |
| PRF / PRP | Keyed function / permutation indistinguishable from a random one |
| One-way function | Easy to compute, hard to invert on average |
| Random oracle model | Analysis treating a hash as a public truly random function |

## How it fits

- **Below:** advantage and negligibility are [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md); efficiency comes from [complexity classes](../../02-theory-of-computation/04-complexity/complexity-classes.md) and the [P versus NP](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) question; perfect secrecy is [information theory](../../02-theory-of-computation/01-information-theory/entropy-and-information.md); proofs by reduction mirror [NP-completeness reductions](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md); Kerckhoffs's principle comes from [design principles](../01-security-principles/security-design-principles.md).
- **Above:** every [symmetric](symmetric-encryption.md), [hash and message authentication code](hash-functions-and-macs.md) and [public-key](public-key-cryptography.md) scheme is stated against these definitions; [protocols](secure-protocols-and-tls.md) are analysed by the same method; [randomized algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md) share the pseudorandomness ideas.
- **Siblings:** this file supplies the vocabulary for all others in [Cryptography](README.md).

## Common misconceptions

- **"Encryption guarantees integrity."** Unauthenticated encryption is malleable; integrity needs a message authentication code (MAC), a signature or authenticated encryption.
- **"A secret algorithm is more secure."** Unanalysed designs routinely fall to known techniques; security must rest on the key alone.
- **"Provably secure means unbreakable."** The proof is relative to a model and an assumption; implementations, side channels and misuse lie outside it.

## Go deeper

- Katz and Lindell, *Introduction to Modern Cryptography* (3rd ed., 2020): the standard rigorous textbook.
- Boneh and Shoup, *A Graduate Course in Applied Cryptography* (freely available draft): definitions with practical constructions.
- Goldwasser and Micali, "Probabilistic Encryption", *Journal of Computer and System Sciences* (1984): the origin of semantic security.
- Shannon, "Communication Theory of Secrecy Systems", *Bell System Technical Journal* (1949).
