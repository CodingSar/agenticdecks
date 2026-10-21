# Information Theory

> **Layer:** [02 Theory of Computation](../README.md) › Information Theory
> **Children:** [Entropy and Information](entropy-and-information.md) · [Source Coding and Compression](source-coding-and-compression.md) · [Channel Capacity and Error Correction](channel-capacity-and-error-correction.md) · [Kolmogorov Complexity](kolmogorov-complexity.md)

## What this area is about

Information theory asks how much there is to say and how reliably it can be said. It treats a source of data as a random variable and a medium as a noisy conditional distribution, then proves exact limits: how few bits can represent a source, and how many bits per second can cross a noisy channel without error. The unifying idea is **entropy**, the average surprise of a random variable, together with its two-variable relative, **mutual information**. Every limit in this area is one of these quantities, and every achievability proof uses the same trick: in long blocks, randomness becomes predictable in aggregate (the law of large numbers), so almost all sequences behave "typically".

The area sits in the theory layer, not in networking, because its limits bind every layer that stores, moves or learns from data. A disk, a cache line protected by an Error-Correcting Code (ECC), a video codec, a Transmission Control Protocol (TCP) checksum and a language model's loss function all obey the same two theorems Claude Shannon proved in 1948.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Entropy and Information](entropy-and-information.md) | Defines the measures: entropy, conditional entropy, mutual information, relative entropy | Probability |
| [Source Coding and Compression](source-coding-and-compression.md) | Proves entropy is the exact limit of lossless compression; covers practical codes and lossy rate–distortion | Entropy |
| [Channel Capacity and Error Correction](channel-capacity-and-error-correction.md) | Proves mutual information (maximised) is the exact limit of reliable transmission; covers practical codes | Entropy, mutual information, algebra |
| [Kolmogorov Complexity](kolmogorov-complexity.md) | Information in a single string as its shortest program; incompressibility, uncomputability, MDL (Minimum Description Length) | Entropy, Turing machines, the halting problem |

Read the first three in order. The first leaf is the vocabulary; the next two are the two coding theorems that give that vocabulary operational meaning. Kolmogorov complexity comes last because it also needs [Turing machines](../03-computability/turing-machines.md): it drops the probability model and asks how much information one particular string contains. On average it agrees with entropy, which shows that Shannon's measure is not an artefact of probabilistic modelling, but it is uncomputable, so practical compression always works with an explicit or learned model.

```
          source                                         destination
            |                                                 ^
   [source encoder]  -- remove redundancy (rate -> H)         |
            |                                         [source decoder]
   [channel encoder] -- add structured redundancy (R < C)     |
            |                                         [channel decoder]
            +------------> noisy channel p(y|x) --------------+
```

The diagram is Shannon's model. Its punchline is the **separation theorem**: for a single sender and receiver, you can design the compressor and the error-correcting code independently and lose nothing in the limit of long blocks. Communication is possible whenever the source entropy rate is below the channel capacity. This modularity is why real systems layer compression (in the application) over error correction (in the physical and link layers).

## Connections to sibling areas

- **[Automata and Formal Languages](../02-automata-and-formal-languages/README.md):** Decoders and parsers are both machines that read symbol streams. Prefix codes are recognised by finite automata, and sources with memory are often modelled as finite-state [Markov chains](../../01-mathematical-foundations/06-probability-and-statistics/markov-chains.md) whose entropy rate can be computed.
- **[Computability](../03-computability/README.md):** [Kolmogorov complexity](kolmogorov-complexity.md), the length of the shortest program that prints a string, is the per-object version of entropy. It is uncomputable because computing it would solve the halting problem, which shows the two theories meeting at their limits.
- **[Complexity](../04-complexity/README.md):** Shannon's coding theorems say good codes exist but not that they are efficient; making decoding tractable is a complexity question (NP, nondeterministic polynomial time: maximum-likelihood decoding of general linear codes is NP-hard). Pseudorandomness, central to complexity-based cryptography, is defined as being computationally indistinguishable from high-entropy randomness.
- **[Quantum Computation](../05-quantum-computation/README.md):** Quantum information theory generalises entropy to von Neumann entropy. Holevo's bound says n qubits can carry at most n classical bits of retrievable information, despite their exponentially large state description.

## Connections across layers

From below, the area takes [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) and [finite-field algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md), and it explains why the [digital abstraction](../../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md) works at all: snapping a noisy voltage to 0 or 1 is a crude error-correcting code. Physically, [Landauer's principle](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md) ties erasing information to heat.

Upward, it sets limits and supplies tools for [character and number encodings](../../03-digital-logic/01-number-representation/character-encoding.md), [ECC memory and storage](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md), the [physical and link layers](../../08-networking/02-link-layer/encoding-and-framing.md), [cryptographic key strength](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md), [media codecs](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md) (built on [Fourier-type transforms](../../01-mathematical-foundations/05-continuous-mathematics/fourier-analysis.md)), and the cross-entropy objectives of [machine learning](../../13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md).

## Cross-cutting threads

- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): entropy bounds compression; capacity bounds reliable rate.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): the choice of code decides which messages are cheap.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): error-correcting codes are redundancy designed with mathematics.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): rate against distortion, rate against reliability, block length against latency.
- [Composition](../../CROSS-CUTTING.md#composition): the separation theorem lets source and channel codes be designed independently and stacked.
