# Qubits and Quantum Circuits

> **Layer:** [02 Theory of Computation](../README.md) › [Quantum Computation](README.md)
> **Builds on:** [Linear Algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Quantum Mechanics and Band Theory](../../00-engineering-foundations/01-physics-of-computation/quantum-mechanics-and-band-theory.md), [Church–Turing Thesis](../03-computability/church-turing-thesis.md)
> **Enables:** [Quantum Algorithms](quantum-algorithms.md), [Logic Gates](../../03-digital-logic/02-combinational-logic/logic-gates.md), [Domain-Specific Accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md)

## Essence

A quantum computer stores information in qubits, whose state is a unit vector in a complex vector space rather than a definite 0 or 1. A register of n qubits has a state described by 2ⁿ complex amplitudes, and quantum gates act on all of them at once by unitary (length-preserving, reversible) matrices. Reading the register (measurement) returns just n classical bits, chosen at random with probabilities given by the squared magnitudes of the amplitudes, and destroys the rest. The power of quantum computation therefore does not come from "trying all answers in parallel". It comes from **interference**: arranging computation so that amplitudes for wrong answers cancel and amplitudes for right answers reinforce before you measure.

## Core tenets

1. **A qubit is a unit vector in ℂ².** Its state is |ψ⟩ = α|0⟩ + β|1⟩ with complex α, β and |α|² + |β|² = 1. Measuring in the standard basis gives 0 with probability |α|² and 1 with probability |β|², and leaves the qubit in the state observed. Amplitudes, unlike probabilities, can be negative or complex, and that is what allows them to cancel.

2. **n qubits live in a 2ⁿ-dimensional space, and most states are entangled.** The joint state space is the tensor product (ℂ²)^⊗n, so a general state needs 2ⁿ amplitudes: about 10¹⁵ complex numbers for n = 50, beyond the memory of a typical cluster. Entangled states, such as the Bell state (|00⟩ + |11⟩)/√2, cannot be written as a product of single-qubit states; measuring one qubit fixes the other's outcome. Entanglement produces correlations no classical shared randomness can reproduce (Bell's theorem), but it cannot send information faster than light.

3. **Gates are unitary matrices, so computation is reversible.** A gate U satisfies U†U = I: it preserves lengths and can be undone. Key gates: the Hadamard H maps |0⟩ to (|0⟩ + |1⟩)/√2 and creates superposition; the Pauli X is NOT; phase gates (S, T) rotate the |1⟩ amplitude; Controlled-NOT (CNOT) flips a target qubit when a control qubit is 1 and creates entanglement. Classical irreversible gates such as AND can be embedded reversibly (the Toffoli gate), so quantum circuits can do anything classical circuits can, with modest overhead.

4. **A small gate set is universal.** CNOT plus all single-qubit gates generates every unitary exactly; H, T and CNOT approximate any unitary to any precision, and the Solovay–Kitaev theorem says the overhead is only polylogarithmic in 1/ε. But almost all n-qubit unitaries need exponentially many gates, so "universal" does not mean "efficient". Algorithms matter.

5. **Measurement extracts only n bits, and that is the crux.** Holevo's bound says n qubits can convey at most n classical bits of retrievable information, despite their 2ⁿ amplitudes. A circuit that puts 2ⁿ candidate answers in superposition and then measures returns one random candidate, no better than guessing. Useful algorithms must use interference to concentrate amplitude on the answer, which works only for problems with exploitable structure (periodicity, symmetry, a known checking procedure).

6. **Quantum states cannot be copied.** The no-cloning theorem says no unitary maps |ψ⟩|0⟩ to |ψ⟩|ψ⟩ for all |ψ⟩, because cloning is not linear. This forbids naive backup and error correction by repetition, enables quantum key distribution (an eavesdropper cannot copy without disturbing), and forces quantum error correction to spread one logical qubit's information across many physical qubits without measuring it directly.

7. **Noise is the engineering problem; error correction is the theoretical answer.** Physical qubits (superconducting circuits, trapped ions, neutral atoms, photons) lose coherence in microseconds to seconds, and two-qubit gate error rates are around 10⁻³ in good 2020s hardware. The threshold theorem says that if physical error rates are below a constant threshold (about 1% for the surface code), arbitrarily long computations can be made reliable with polylogarithmic overhead. In practice estimates run to hundreds or thousands of physical qubits per logical qubit, so a cryptographically relevant machine needs on the order of a million physical qubits.

8. **Quantum computation does not escape the Church–Turing thesis.** A classical computer can simulate any quantum circuit by tracking all 2ⁿ amplitudes, in exponential time, or in polynomial space by summing over paths. So quantum computers compute the same functions as Turing machines; what they may change is efficiency, which is the *extended* [Church–Turing thesis](../03-computability/church-turing-thesis.md).

## Key concepts

| Term | Meaning |
|---|---|
| Qubit | Two-level quantum system; state α\|0⟩ + β\|1⟩ with \|α\|² + \|β\|² = 1 |
| Amplitude | Complex coefficient whose squared magnitude is an outcome probability |
| Superposition | A state that is a linear combination of basis states |
| Entanglement | Joint state not expressible as a product of individual states |
| Unitary gate | Reversible, length-preserving linear map |
| Measurement | Probabilistic readout that collapses the state to the observed outcome |
| Interference | Amplitudes adding or cancelling along different computational paths |
| Decoherence | Loss of quantum behaviour through unwanted coupling to the environment |
| Logical vs physical qubit | Error-corrected encoded qubit vs individual hardware qubit |

## How it fits

- **Below:** States and gates are vectors and matrices from [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md) over complex numbers; measurement uses [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md). The physics is the same [quantum mechanics](../../00-engineering-foundations/01-physics-of-computation/quantum-mechanics-and-band-theory.md) that explains semiconductors, here used directly rather than averaged away. Reversibility connects to Landauer's principle in [thermodynamics](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md).
- **Above:** The circuit model parallels classical [logic gates](../../03-digital-logic/02-combinational-logic/logic-gates.md); the reversible Toffoli gate is the bridge. Quantum processors are attached to classical hosts as special-purpose [accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md). No-cloning underpins quantum key distribution, a niche part of [secure protocols](../../11-security-and-cryptography/02-cryptography/secure-protocols-and-tls.md).
- **Siblings:** This leaf defines the machine; [quantum algorithms](quantum-algorithms.md) shows what interference can achieve with it and where the gains stop.

## Common misconceptions

- **"A quantum computer tries every answer in parallel and picks the right one."** Measurement returns one random outcome. Speedups need interference engineered for the problem's structure.
- **"Entanglement allows faster-than-light communication."** Measurement outcomes on each side are individually random; correlations appear only when results are compared over a classical channel.
- **"Qubits are just probabilistic bits."** Probabilities are non-negative and cannot cancel; amplitudes can. That cancellation is the whole source of quantum advantage.

## Go deeper

- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., 2010): the standard reference.
- N. David Mermin, *Quantum Computer Science: An Introduction* (2007): written for computer scientists, minimal physics.
- John Preskill, "Quantum Computing in the NISQ Era and Beyond" (2018): realistic view of noisy near-term hardware.
