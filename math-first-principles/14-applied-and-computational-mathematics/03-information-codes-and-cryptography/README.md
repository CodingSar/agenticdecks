# Information, Codes and Cryptography

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › Information, Codes and Cryptography
> **Children:** [Information Theory](information-theory.md) · [Error-Correcting Codes](error-correcting-codes.md) · [Cryptography](cryptography.md)

## What this area is about

This area is the mathematics of sending messages. Three adversaries stand between sender and receiver: redundancy, which wastes bandwidth; noise, which corrupts symbols; and eavesdroppers, who read or alter what is sent. Information theory measures what is fundamentally possible against the first two, error-correcting codes achieve it constructively, and cryptography defends against the third. One figure began all three: Claude Shannon's papers of 1948 and 1949 founded information theory, set the goal that coding theory has pursued since, and gave the first mathematical definition of secrecy.

The unifying idea is that a message is an element of a large finite set, and that its fate depends on the geometry and arithmetic of that set. Compression counts typical sequences; error correction packs well-separated codewords into a vector space over a finite field; public-key cryptography hides structure inside groups where some computations are easy and their inverses are believed hard. Finite fields, polynomials and probability are the shared tools.

## How the children fit together

```
                 information theory
        (entropy, capacity: what is possible)
              /                      \
   error-correcting codes          cryptography
  (algebraic constructions     (hardness: what is
   that reach the limits)       infeasible to undo)
              \______________________/
           finite fields, polynomials, lattices
```

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Information theory](information-theory.md) | The limits: entropy, the source coding theorem, channel capacity and the noisy-channel coding theorem | Probability, counting |
| [Error-correcting codes](error-correcting-codes.md) | The constructions: linear codes, distance bounds, Hamming and Reed–Solomon codes, and capacity-approaching codes | Information theory, finite fields |
| [Cryptography](cryptography.md) | Security: perfect secrecy, one-way functions, Diffie–Hellman, Rivest–Shamir–Adleman (RSA), elliptic curves, quantum attacks and post-quantum standards | Number theory, finite fields, information theory |

Read information theory first: its theorems are existence statements, proved by random choice, which say what any scheme can achieve. Error-correcting codes then try to reach those limits with explicit structure, since a random code cannot be decoded efficiently. Cryptography uses information theory to define perfect secrecy, finds it too costly, and moves to computational security, where the question is no longer what is possible but what is feasible.

The two later children mirror each other. A code is designed so that the receiver can undo noise easily; a cipher is designed so that only the key holder can undo the encryption. The two meet in Robert McEliece's cryptosystem, whose public key is a code disguised so that decoding it looks like the hard problem of decoding a random linear code. Both sides also depend on the same algebra: Reed–Solomon codes and elliptic curve cryptography both compute in finite fields, and lattices serve both as dense sphere packings and as the source of post-quantum hardness.

## Connections to sibling areas

- [Numerical analysis](../01-numerical-analysis/README.md): Reed–Solomon decoding is interpolation over a finite field, and the fast Fourier transform appears in both fast encoding and fast multiplication of large integers for cryptography.
- [Optimisation](../02-optimisation/README.md): channel capacity is a concave maximisation, and linear programming gives both decoders and upper bounds on the size of codes.
- [Mathematical modelling](../04-mathematical-modelling/README.md): quantum mechanics underlies both Shor's algorithm, which threatens current public-key schemes, and quantum key distribution.
- [Games, decisions and finance](../05-games-decisions-and-finance/README.md): the Kelly criterion for betting is a capacity formula, and cryptographic protocols are analysed as games between honest parties and adversaries.
- [Data and learning](../06-data-and-learning/README.md): compressed sensing is decoding over the real numbers, and entropy and Kullback–Leibler divergence are the losses and bounds of learning theory.

## Connections across layers

The area draws on [finite fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md) and [polynomial rings](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md) for codes, on [elementary number theory](../../02-number-systems/README.md) and [elliptic curves](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/elliptic-curves.md) for public-key cryptography, on [lattices and sphere packing](../../08-geometry/03-convex-and-discrete-geometry/lattices-and-sphere-packing.md) for both, and on the [law of large numbers](../../11-probability-and-statistics/02-limit-theorems/the-law-of-large-numbers.md) for information theory. It gives back problems: the existence of one-way functions is tied to the P versus NP question (polynomial versus nondeterministic polynomial time), listed among [open problems](../../15-mathematics-in-context/open-problems.md), and the public stakes of encryption are part of [mathematics and society](../../15-mathematics-in-context/mathematics-and-society.md).

## Cross-cutting threads

- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): no compression below entropy, no reliable rate above capacity, no code beyond the Singleton bound.
- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): random codes prove the coding theorems, and random keys give secrecy.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): Shannon proved good codes exist; practical codes near capacity came only in the 1990s, and polar codes (2009) were proved to reach it with low-complexity decoding.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): codes become lattices, and number theory becomes security.
