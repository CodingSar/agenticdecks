# Cryptography

> **Layer:** [11 Security and Cryptography](../README.md) › Cryptography
> **Children:** [Foundations of modern cryptography](foundations-of-modern-cryptography.md) · [Symmetric encryption](symmetric-encryption.md) · [Hash functions and message authentication codes](hash-functions-and-macs.md) · [Public-key cryptography](public-key-cryptography.md) · [Secure protocols and Transport Layer Security](secure-protocols-and-tls.md)

## What this area is about

Cryptography is the science of protecting information from an adversary who can see, alter or inject data you do not physically control: data on a network, on a stolen laptop, in someone else's data centre. It provides a small set of primitives, encryption for confidentiality, message authentication and signatures for integrity and origin, and key exchange for establishing shared secrets between strangers, and it combines them into protocols.

The unifying idea of *modern* cryptography is **provable security relative to precise definitions and hardness assumptions**. A scheme is not "secure" because no one has broken it yet; it is secure if any efficient adversary that breaks it, in the sense of a precisely stated game, could be converted into an efficient algorithm for a problem believed to be hard (factoring large integers, computing discrete logarithms, distinguishing a well-studied block cipher from a random permutation). This turns cryptography from an art of clever codes into a discipline where claims can be checked, and it explains its main practical rule: use standard, vetted primitives and protocols, and never invent your own.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Foundations of modern cryptography](foundations-of-modern-cryptography.md) | Definitions (indistinguishability, unforgeability), hardness assumptions, reductions, randomness | Probability, complexity, information theory |
| [Symmetric encryption](symmetric-encryption.md) | Confidentiality with a shared key: block and stream ciphers, modes, authenticated encryption | Foundations |
| [Hash functions and message authentication codes](hash-functions-and-macs.md) | Integrity: fingerprints of data, keyed tags that detect tampering, password hashing | Foundations |
| [Public-key cryptography](public-key-cryptography.md) | Key exchange, public-key encryption and digital signatures between parties without a shared secret | Foundations, number theory |
| [Secure protocols and Transport Layer Security](secure-protocols-and-tls.md) | Combining the primitives into an authenticated, confidential channel; where real failures occur | All four above |

```
            foundations: definitions, assumptions, reductions
             /                     |                     \
   symmetric encryption     hashes and MACs       public-key crypto
   (fast bulk secrecy)      (integrity)           (key exchange, signatures)
             \                     |                     /
              +-------- authenticated encryption -------+
                                   |
                     protocols: TLS, SSH, Signal, ...
```

(MAC is a message authentication code; TLS is Transport Layer Security; SSH is the Secure Shell protocol.)

Read the foundations first: without the definitions, statements like "Advanced Encryption Standard (AES) in counter mode is secure" have no content, and the classic mistakes (deterministic encryption, unauthenticated ciphertexts, reused nonces) are not visible. Symmetric primitives come next because they do almost all the work in practice. Public-key cryptography solves the problem symmetric cryptography cannot: how two parties who have never met agree on a key. Protocols come last, and most real-world breaks happen there, in how correct primitives are combined, negotiated and implemented.

## Connections to sibling areas

- **[Security principles](../01-security-principles/README.md):** a cryptographic security definition is a threat model made exact; Kerckhoffs's principle (only the key is secret) is the founding design rule of the field.
- **[System security](../03-system-security/README.md):** cryptography protects data only while keys stay secret, so key storage depends on isolation and access control; [side channels](../03-system-security/side-channels.md) attack implementations, not mathematics.
- **[Network and application security](../04-network-and-application-security/README.md):** [authentication](../04-network-and-application-security/authentication.md) uses signatures, password hashing and challenge-response; the web's security rests on TLS and certificates.

## Connections across layers

Cryptography is the most mathematical part of the tree. It takes [modular arithmetic and primes](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md), [groups and finite fields](../../01-mathematical-foundations/04-algebra/abstract-algebra.md), [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [entropy](../../02-theory-of-computation/01-information-theory/entropy-and-information.md), and [complexity theory](../../02-theory-of-computation/04-complexity/complexity-classes.md). [Quantum algorithms](../../02-theory-of-computation/05-quantum-computation/quantum-algorithms.md) threaten its public-key half. Implementations rely on [constant-time code](../03-system-security/side-channels.md) and sometimes [formal verification](../../06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md). It enables [secure transport](../../08-networking/04-transport-layer/udp-and-tcp.md) and [the web](../../08-networking/05-application-layer/http-and-the-web.md), [version control](../../12-software-engineering/02-process/version-control.md) integrity, and [Byzantine fault tolerance](../../10-distributed-and-parallel-computing/03-consensus-and-replication/byzantine-fault-tolerance.md).

## Cross-cutting threads

- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): security rests on assumed computational hardness; perfect secrecy needs keys as long as messages.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): signatures and certificates move trust from channels to keys.
- [Composition](../../CROSS-CUTTING.md#composition): secure primitives can compose insecurely; composition theorems say when they do not.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): ambiguous encodings of signed data are a classic source of breaks.
- [The end-to-end argument](../../CROSS-CUTTING.md#the-end-to-end-argument): encryption belongs at the endpoints that hold the keys.
