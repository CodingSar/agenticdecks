# Quantum Algorithms

> **Layer:** [02 Theory of Computation](../README.md) › [Quantum Computation](README.md)
> **Builds on:** [Qubits and Quantum Circuits](qubits-and-quantum-circuits.md), [Complexity Classes](../04-complexity/complexity-classes.md), [Number Theory](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md), [Abstract Algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md)
> **Enables:** [Public-Key Cryptography](../../11-security-and-cryptography/02-cryptography/public-key-cryptography.md), [Foundations of Modern Cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md), [Symmetric Encryption](../../11-security-and-cryptography/02-cryptography/symmetric-encryption.md)

## Essence

A handful of quantum algorithms show both how much faster quantum computers can be and how narrow that advantage is. Shor's algorithm factors integers and computes discrete logarithms in polynomial time, which would break the public-key cryptography (Rivest–Shamir–Adleman (RSA), Diffie–Hellman, elliptic curves) that secures the Internet. Grover's algorithm searches an unstructured space of N items in about √N steps instead of N, a quadratic speedup that is provably the best possible. Both work by the same mechanism: prepare a superposition, let a structured operation imprint the answer as a pattern of phases, and use interference to turn that pattern into a high-probability measurement.

## Core tenets

1. **BQP is the class of problems quantum computers solve efficiently.** BQP (Bounded-error Quantum Polynomial time) contains problems solvable by polynomial-size quantum circuits that answer correctly with probability at least 2/3. Known relations: P ⊆ BPP ⊆ BQP ⊆ PSPACE, where P is deterministic polynomial time, BPP its randomised analogue and PSPACE polynomial space. Factoring is in BQP but not known to be in BPP. NP-complete problems (NP: nondeterministic polynomial time) are not believed to be in BQP. No separation is proved: showing BQP ≠ BPP would itself prove P ≠ PSPACE.

2. **The Quantum Fourier Transform (QFT) finds periods.** The QFT on n qubits performs a [discrete Fourier transform](../../01-mathematical-foundations/05-continuous-mathematics/fourier-analysis.md) over 2ⁿ amplitudes using only O(n²) gates, exponentially fewer than the O(n·2ⁿ) operations of a classical Fast Fourier Transform (FFT) on the same vector. Measurement returns only one sample of the spectrum, but if the amplitudes are periodic that sample is close to a multiple of 2ⁿ/period, and a few samples reveal the period.

3. **Shor's algorithm reduces factoring to period finding.** To factor N, pick random a coprime to N; the function f(x) = aˣ mod N is periodic with period r, the order of a modulo N. Compute f on a superposition of all x, apply the QFT, measure, and recover r by continued fractions. If r is even and a^(r/2) ≢ −1 (mod N), then gcd(a^(r/2) ± 1, N) gives a non-trivial factor; this happens with probability at least 1/2. The total cost is polynomial in log N (roughly cubic with schoolbook arithmetic), compared with the best known classical algorithm, the general number field sieve, at exp(O((log N)^(1/3) (log log N)^(2/3))).

4. **The same idea breaks every widely deployed public-key scheme.** Discrete logarithms, in multiplicative groups and on elliptic curves, are also hidden-period (abelian hidden subgroup) problems, so RSA, Diffie–Hellman and elliptic-curve schemes all fall to a large fault-tolerant quantum computer. Hence the migration to lattice- and hash-based post-quantum schemes, standardised by the US National Institute of Standards and Technology (NIST) in 2024 (ML-KEM, ML-DSA, SLH-DSA). It is urgent because recorded traffic can be decrypted later ("harvest now, decrypt later").

5. **Grover's algorithm gives a quadratic speedup for unstructured search.** Given a black-box f: {0,1}ⁿ → {0,1} with a marked input, start in the uniform superposition over N = 2ⁿ inputs. Each Grover iteration flips the sign of the marked amplitude (oracle call) and then reflects all amplitudes about their mean, which rotates the state a fixed angle of about 2/√N toward the marked item. After about (π/4)√N iterations, measurement yields the marked item with high probability. Iterating further rotates *past* it.

6. **Grover's speedup is optimal, which caps quantum brute force.** Bennett, Bernstein, Brassard and Vazirani (1997) proved any quantum algorithm needs Ω(√N) oracle queries for unstructured search. So quantum computers cannot solve NP-complete problems by brute force faster than about 2^(n/2). A k-bit symmetric key offers roughly k/2 bits of security against a quantum attacker, hence 256-bit Advanced Encryption Standard (AES) keys for the long term. In practice the gain is weaker still, because Grover iterations are sequential and each costs many error-corrected gates.

7. **Simulating quantum systems is the most natural application.** Feynman (1982) observed that simulating quantum physics classically seems to need exponential resources, while a quantum computer can mirror the system directly. Hamiltonian simulation is BQP-complete and promises exponential speedups in chemistry and materials science, wherever clever classical approximations do not already suffice.

8. **Many claimed speedups shrink under scrutiny.** Quantum linear-system and machine-learning algorithms are exponentially faster only under strong assumptions (fast loading of data into amplitudes, wanting only a summary of the answer), and "dequantised" classical algorithms (Tang, 2018) matched several of them under the same assumptions. Variational and annealing methods on noisy hardware have no proven general advantage, and the "supremacy" experiments since 2019 solve tasks with no known practical use.

## Key concepts

| Term | Meaning |
|---|---|
| BQP | Problems solvable by polynomial-size quantum circuits with error ≤ 1/3 |
| Oracle (black box) | A function the algorithm may query, cost counted per query |
| Quantum Fourier Transform | Discrete Fourier transform on amplitudes in O(n²) gates |
| Period finding | Recovering r from a function with f(x + r) = f(x) |
| Hidden subgroup problem | General form of period finding; abelian case solved efficiently |
| Amplitude amplification | Grover's rotation, generalised to boost any success probability |
| Post-quantum cryptography | Classical schemes believed secure against quantum attack |

## How it fits

- **Below:** It uses the circuit model from [qubits and quantum circuits](qubits-and-quantum-circuits.md), modular arithmetic and Euler's theorem from [number theory](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md), group structure from [abstract algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md), and the class map from [complexity classes](../04-complexity/complexity-classes.md).
- **Above:** Shor's algorithm threatens [public-key cryptography](../../11-security-and-cryptography/02-cryptography/public-key-cryptography.md) and thus [Transport Layer Security (TLS)](../../11-security-and-cryptography/02-cryptography/secure-protocols-and-tls.md); Grover's bound sets key lengths in [symmetric encryption](../../11-security-and-cryptography/02-cryptography/symmetric-encryption.md) and output sizes of [hash functions](../../11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md).
- **Siblings:** [Qubits and quantum circuits](qubits-and-quantum-circuits.md) explains why interference is the resource; this leaf shows which problems can exploit it.

## Common misconceptions

- **"Quantum computers will make all computation exponentially faster."** Exponential speedups are known only for structured problems such as period finding and quantum simulation. Most workloads gain nothing.
- **"Quantum computers will break all encryption."** They break today's public-key schemes. Symmetric ciphers and hashes lose about half their security bits, fixed by doubling sizes, and post-quantum replacements exist.

## Go deeper

- Peter W. Shor, "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer" (1997, SIAM Journal on Computing; conference version 1994).
- Lov K. Grover, "A Fast Quantum Mechanical Algorithm for Database Search" (1996).
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (2010), chapters 5–6: QFT, Shor and Grover in detail.
