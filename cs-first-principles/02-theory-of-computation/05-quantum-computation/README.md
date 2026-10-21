# Quantum Computation

> **Layer:** [02 Theory of Computation](../README.md) › Quantum Computation
> **Children:** [Qubits and Quantum Circuits](qubits-and-quantum-circuits.md) · [Quantum Algorithms](quantum-algorithms.md)

## What this area is about

Classical complexity theory assumes the machine obeys classical physics: bits are definite and probabilities add. Quantum computation asks **what changes if the machine instead obeys quantum mechanics**, where the state is a vector of complex amplitudes that can interfere. The answer has two parts, and both matter. What can be computed does not change: a classical machine can simulate any quantum circuit, so the Church–Turing thesis survives. What can be computed *efficiently* probably does change, for a narrow but important set of problems, most famously factoring.

The unifying idea is **interference**. An n-qubit register carries 2ⁿ amplitudes, but measurement yields only n bits. A quantum algorithm is useful only if it arranges for wrong answers' amplitudes to cancel and right answers' to add up before measuring. Problems with hidden algebraic structure (periodicity, symmetries) allow this to give exponential gains; problems without structure allow at most a quadratic gain.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Qubits and Quantum Circuits](qubits-and-quantum-circuits.md) | The machine model: states, unitary gates, entanglement, measurement, noise and error correction | Linear algebra, probability, quantum physics |
| [Quantum Algorithms](quantum-algorithms.md) | What the model buys: bounded-error quantum polynomial time (BQP), the Quantum Fourier Transform (QFT), Shor, Grover, simulation, and the limits of speedup | Circuits, complexity classes, number theory |

Read the circuit model first. It establishes the three facts that algorithms must work around: amplitudes can cancel, measurement is destructive and returns little, and states cannot be copied.

```
   prepare             evolve                         measure
  |0...0>  --H^n-->  superposition  --U_f, QFT or -->  n classical bits
                     (2^n amplitudes)  Grover steps    (one random outcome,
                                       = interference    probability |amp|^2)
```

## Connections to sibling areas

- **[Information Theory](../01-information-theory/README.md):** Quantum information theory generalises Shannon entropy to von Neumann entropy. Holevo's bound (n qubits carry at most n retrievable bits) is the information-theoretic reason quantum parallelism cannot be read out directly.
- **[Automata and Formal Languages](../02-automata-and-formal-languages/README.md):** Quantum finite automata exist, but bounded memory still bounds power; the interesting quantum effects need unbounded registers.
- **[Computability](../03-computability/README.md):** Quantum computers compute exactly the Turing-computable functions. They are the main test case for the *physical* and *extended* forms of the Church–Turing thesis.
- **[Complexity](../04-complexity/README.md):** BQP sits between BPP (bounded-error probabilistic polynomial time) and PSPACE (polynomial space). Its relationship to NP (nondeterministic polynomial time), believed to be incomparable, is the precise statement of "quantum computers are not magic".

## Connections across layers

Below, it rests directly on [quantum mechanics](../../00-engineering-foundations/01-physics-of-computation/quantum-mechanics-and-band-theory.md) and on [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), [number theory](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md) and [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md). Reversible gates connect it to [Landauer's principle](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md) and to classical [logic gates](../../03-digital-logic/02-combinational-logic/logic-gates.md).

Above, its main practical consequence today is in [security and cryptography](../../11-security-and-cryptography/README.md): Shor's algorithm forces the move to post-quantum [public-key cryptography](../../11-security-and-cryptography/02-cryptography/public-key-cryptography.md), and Grover's bound sets [symmetric key](../../11-security-and-cryptography/02-cryptography/symmetric-encryption.md) sizes. Physically, quantum processors are built as special-purpose [accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md) controlled by classical computers, and their engineering is dominated by noise, the same enemy as in [reliability and redundancy](../../00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md).

## Cross-cutting threads

- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): Holevo's bound, no-cloning and Grover's optimality limit what quantum hardware can deliver.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): amplitudes are a new representation of information in which cancellation is possible.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): quantum error correction spreads one logical qubit across many physical ones.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): exponential state space against destructive, low-bandwidth readout.
