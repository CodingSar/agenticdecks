# Public-Key Cryptography

> **Layer:** [11 Security and Cryptography](../README.md) › [Cryptography](README.md)
> **Builds on:** [Number theory](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md), [Abstract algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md), [Foundations of modern cryptography](foundations-of-modern-cryptography.md), [Quantum algorithms](../../02-theory-of-computation/05-quantum-computation/quantum-algorithms.md)
> **Enables:** [Secure protocols and Transport Layer Security](secure-protocols-and-tls.md), [Authentication](../04-network-and-application-security/authentication.md), [Byzantine fault tolerance](../../10-distributed-and-parallel-computing/03-consensus-and-replication/byzantine-fault-tolerance.md)

## Essence

Symmetric cryptography needs a shared secret, but two strangers on the internet have none. Public-key (asymmetric) cryptography solves this by giving each party a key pair: a **public key** anyone may know and a **private key** only its owner holds. Three capabilities follow. **Key exchange** (Diffie–Hellman, 1976) lets two parties agree on a shared secret over a public channel. **Public-key encryption** lets anyone encrypt to the owner. **Digital signatures** let the owner sign data so that anyone can verify, and no one else can forge, the signature. All rest on **trapdoor or one-way structure** in mathematics: operations easy in one direction and infeasible to reverse without a secret, such as exponentiation in a group versus discrete logarithm, or multiplying primes versus factoring. Public-key operations are thousands of times slower than symmetric ones, so they are used to establish and authenticate keys, not to encrypt bulk data.

## Core tenets

1. **Diffie–Hellman turns a hard problem into a shared secret.** Fix a group with generator g. Alice picks secret a and sends gᵃ; Bob picks secret b and sends gᵇ; both compute gᵃᵇ. An eavesdropper sees g, gᵃ and gᵇ, and recovering gᵃᵇ is believed hard (the computational Diffie–Hellman problem, which is no harder than discrete logarithm). Plain Diffie–Hellman is unauthenticated: a man-in-the-middle can run separate exchanges with each side, so the exchanged values must be signed or otherwise authenticated.

2. **RSA uses the difficulty of factoring.** Rivest, Shamir and Adleman (1977): choose primes p and q, publish n = pq and an exponent e, and keep d with ed ≡ 1 mod (p−1)(q−1). Then (mᵉ)ᵈ ≡ m mod n by Euler's theorem, and computing d from (n, e) is as hard as factoring n. "Textbook" RSA is deterministic and malleable, so it is insecure on its own; real use needs randomised padding: OAEP (Optimal Asymmetric Encryption Padding) for encryption and PSS (Probabilistic Signature Scheme) for signatures. The older PKCS #1 v1.5 encryption padding enabled Bleichenbacher's padding-oracle attack (1998) and its descendants.

3. **Elliptic curves give the same security with much smaller keys.** Discrete logarithm on a well-chosen elliptic curve group has no known sub-exponential classical algorithm, unlike factoring and discrete logarithm modulo a prime. So a 256-bit elliptic-curve key gives about 128-bit security, comparable to RSA with 3,072-bit moduli. Elliptic-Curve Diffie–Hellman (ECDH, for example X25519) and signatures (ECDSA, and the deterministic EdDSA scheme Ed25519) dominate new deployments.

4. **Signatures provide integrity, origin and non-repudiation to everyone.** A signature on a message (in practice, on its hash) can be checked by anyone with the public key, unlike a MAC (message authentication code), whose verifiers could also forge. The security goal is existential unforgeability under chosen-message attack. Implementation details are security-critical: ECDSA needs a fresh secret random nonce per signature; reusing or biasing it reveals the private key, which is how the Sony PlayStation 3 signing key was recovered in 2010. Deterministic nonce derivation (as in EdDSA, or RFC 6979 for ECDSA) removes that risk.

5. **Hybrid encryption combines speed and convenience.** To encrypt a large message to a public key, generate a random symmetric key, encrypt the message with authenticated symmetric encryption, and encrypt (or agree on) only the symmetric key with public-key methods. Key encapsulation mechanisms (KEMs) formalise the second step. Every practical system, from Transport Layer Security (TLS) to encrypted email, works this way.

6. **Public keys need authentication, which is a trust problem, not a math problem.** Encrypting to the wrong public key, one supplied by an attacker, gives the attacker everything. A public-key infrastructure (PKI) binds names to keys with certificates signed by certificate authorities (CAs) that clients trust in advance; alternatives are trust-on-first-use (as in Secure Shell (SSH)), webs of trust, and key transparency logs. The weakest trusted authority bounds the whole system's security.

7. **Forward secrecy limits the damage of key theft.** If long-term keys only *sign* ephemeral Diffie–Hellman exchanges, and the ephemeral secrets are deleted after each session, then a later theft of the long-term key cannot decrypt recorded past sessions. Encrypting session keys directly under a long-term RSA key lacks this property, which is why TLS 1.3 removed RSA key transport.

8. **Large quantum computers would break RSA and elliptic curves; post-quantum schemes replace them.** Shor's algorithm (1994) factors and computes discrete logarithms in polynomial time on a fault-tolerant quantum computer, which would break every widely deployed public-key scheme; no such machine exists yet, but recorded traffic could be decrypted later ("harvest now, decrypt later"). The US National Institute of Standards and Technology (NIST) standardised lattice-based ML-KEM (FIPS 203) for key encapsulation and ML-DSA (FIPS 204) and the hash-based SLH-DSA (FIPS 205) for signatures in 2024. Deployments currently combine them with classical elliptic-curve schemes in hybrid mode, so security holds if either remains unbroken.

## Key concepts

| Term | Meaning |
|---|---|
| Key pair | Public key shared openly; private key kept secret |
| Discrete logarithm | Finding x from gˣ in a group; believed hard in suitable groups |
| Diffie–Hellman | Key agreement from exchanged group elements gᵃ, gᵇ |
| RSA | Encryption and signatures based on the hardness of factoring |
| Elliptic-curve cryptography | Discrete-log cryptography in elliptic-curve groups; small keys |
| Digital signature | Publicly verifiable, unforgeable tag from a private key |
| KEM | Key encapsulation mechanism: public-key method to establish a symmetric key |
| Certificate / CA | Signed binding of a name to a public key / the signer trusted to issue it |
| Forward secrecy | Past sessions stay secure after long-term key compromise |
| Post-quantum cryptography | Schemes believed secure against quantum attackers (lattices, hashes, codes) |

## How it fits

- **Below:** modular exponentiation, Euler's theorem and primality testing come from [number theory](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md); groups and finite fields from [abstract algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md); fast primality testing is a [randomized algorithm](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md); the quantum threat comes from [quantum algorithms](../../02-theory-of-computation/05-quantum-computation/quantum-algorithms.md).
- **Above:** [TLS](secure-protocols-and-tls.md) uses ephemeral Diffie–Hellman plus certificates; [authentication](../04-network-and-application-security/authentication.md) with passkeys is signature-based; code signing protects [software delivery](../../12-software-engineering/04-operations/build-and-continuous-delivery.md); [Byzantine protocols](../../10-distributed-and-parallel-computing/03-consensus-and-replication/byzantine-fault-tolerance.md) rely on signatures.
- **Siblings:** [symmetric encryption](symmetric-encryption.md) does the bulk work under keys agreed here; [hash functions](hash-functions-and-macs.md) compress messages before signing; [foundations](foundations-of-modern-cryptography.md) define IND-CCA and unforgeability.

## Common misconceptions

- **"Signing is encrypting with the private key."** That analogy holds only loosely for textbook RSA and is wrong in general; signatures and encryption are different primitives with different definitions.
- **"Bigger RSA keys are the long-term answer."** Shor's algorithm breaks RSA at any size in polynomial time; the answer is post-quantum schemes.
- **"Public-key crypto removes the need to trust anyone."** It moves the trust to whoever vouches for public keys.

## Go deeper

- Diffie and Hellman, "New Directions in Cryptography", *IEEE Transactions on Information Theory* (1976).
- Rivest, Shamir and Adleman, "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems", *Communications of the ACM* (1978).
- Boneh, "Twenty Years of Attacks on the RSA Cryptosystem", *Notices of the AMS* (1999).
- Bernstein and Lange, "Post-Quantum Cryptography", *Nature* (2017).
