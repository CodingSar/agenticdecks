# 02 Theory of Computation

> **Layer:** 02 Theory of Computation
> **Children:** [Information Theory](01-information-theory/README.md) · [Automata and Formal Languages](02-automata-and-formal-languages/README.md) · [Computability](03-computability/README.md) · [Complexity](04-complexity/README.md) · [Quantum Computation](05-quantum-computation/README.md)

## What this area is about

Theory of computation asks what information is, what machines can do with it, and at what cost, *before any machine is built*. It answers with mathematical models and proved limits: how few bits can describe a source and how many can cross a noisy channel; which patterns a machine with a given kind of memory can recognise; which problems no program can ever solve; which solvable problems need astronomically more time than others; and how much of this changes if the machine obeys quantum mechanics.

The single idea that unifies the layer is that **computation and information can be studied as mathematical objects, independent of any hardware**. A Turing machine, a finite automaton or a probability distribution over messages is defined with nothing more than sets, functions, logic and probability. That is why the results are permanent. Faster chips do not make the halting problem decidable or compress random data.

## Why this layer sits here

This layer is the **purely formal pillar** of Computer Science (CS). It rests only on [01 Mathematical Foundations](../01-mathematical-foundations/README.md): [logic](../01-mathematical-foundations/01-logic/README.md) for proofs and Boolean formulas, [sets, relations and functions](../01-mathematical-foundations/02-sets-relations-functions/README.md) for languages, machines and cardinality arguments, [discrete mathematics](../01-mathematical-foundations/03-discrete-mathematics/README.md) for counting, graphs and recurrences, [algebra](../01-mathematical-foundations/04-algebra/README.md) for codes and quantum states, and [probability](../01-mathematical-foundations/06-probability-and-statistics/README.md) for entropy and randomised computation. It does not depend on [00 Engineering Foundations](../00-engineering-foundations/README.md) at all; it sits at 02 because everything above it needs its results.

Placing it below [03 Digital Logic](../03-digital-logic/README.md) and [04 Computer Architecture](../04-computer-architecture/README.md) says something deliberate: **what any machine can and cannot do is fixed before one is built**. The engineering layers construct a particular machine out of transistors, but the limits that machine will face (undecidability, intractability, the entropy and capacity bounds) were settled here, and they apply equally to every machine those layers could ever build.

The layer is also where the two pillars of the stack are joined. The [Church–Turing thesis](03-computability/church-turing-thesis.md) claims that the formal notion of "Turing-computable" captures everything a mechanical procedure, and by its physical extension any physical device, can compute. That claim is what licenses the physical pillar ([00](../00-engineering-foundations/README.md) → [03](../03-digital-logic/README.md) → [04](../04-computer-architecture/README.md)) to build *one* universal stored-program machine and trust it to run every algorithm the formal pillar can describe. The universal Turing machine is the blueprint; the instruction set architecture is its engineering realisation.

The abstraction this layer contributes to the stack is **the model of computation with its cost measures and its limits**: a precise notion of what an algorithm is, how to count its resources, and which problems are impossible or intractable for every algorithm.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Information Theory](01-information-theory/README.md) | Measures information; proves limits of compression and reliable transmission; defines the information in a single string | Probability, algebra (and Turing machines, for Kolmogorov complexity) |
| [Automata and Formal Languages](02-automata-and-formal-languages/README.md) | Machines with restricted memory; what each memory form can recognise | Sets, logic, induction |
| [Computability](03-computability/README.md) | The general model (Turing machines, lambda calculus); the thesis; undecidability | Automata, cardinality |
| [Complexity](04-complexity/README.md) | Cost of decidable problems; P (polynomial time) vs NP (nondeterministic polynomial time); the map of classes | Computability, asymptotics |
| [Quantum Computation](05-quantum-computation/README.md) | How quantum physics changes efficiency but not computability | Complexity, linear algebra |

```
   information theory          automata (finite memory, one stack)
   (what data is worth)                    |  add an unbounded tape
            \                              v
             \                   computability  (what can be computed)
              \                            |  add a budget
               \                           v
                +--------------->  complexity    (what it costs)
                                           |  change the physics
                                           v
                                 quantum computation
```

Information theory stands slightly apart: it studies data rather than machines, and its leaves can be read first or last, except [Kolmogorov complexity](01-information-theory/kolmogorov-complexity.md), which needs Turing machines and the halting problem. The other four form a chain. Automata show that memory structure determines power and introduce the proof style (pumping, closure, reductions). Computability removes the memory limit and finds the absolute boundary. Complexity puts a budget back and finds the practical boundary. Quantum computation changes the physical assumptions underneath and shows which boundaries move (some complexity ones) and which do not (computability ones). Information and computation meet in [Kolmogorov complexity](01-information-theory/kolmogorov-complexity.md) (the shortest program for a string, uncomputable by a reduction from halting) and in cryptography, where security is defined as "indistinguishable from high entropy to every efficient algorithm".

## Connections to neighbouring layers

- **[01 Mathematical Foundations](../01-mathematical-foundations/README.md):** The only layer this one needs. Diagonalisation from [cardinality](../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md) becomes the halting proof and the hierarchy theorems; [propositional logic](../01-mathematical-foundations/01-logic/propositional-logic.md) becomes Boolean satisfiability (SAT); [probability](../01-mathematical-foundations/06-probability-and-statistics/probability.md) becomes entropy.
- **[00 Engineering Foundations](../00-engineering-foundations/README.md):** No dependency, but contact at the bottom: [Landauer's principle](../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md) prices erasing a bit in heat, physical [noise](../00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md) is what channel coding defeats, and [quantum mechanics](../00-engineering-foundations/01-physics-of-computation/quantum-mechanics-and-band-theory.md) is the physics of quantum computation.
- **[03 Digital Logic](../03-digital-logic/README.md):** Where the pillars meet. Sequential circuits are [finite state machines](../03-digital-logic/03-sequential-logic/finite-state-machines.md), the hardware form of finite automata; [logic minimisation](../03-digital-logic/02-combinational-logic/logic-minimization.md) is NP-hard in general.
- **[04 Computer Architecture](../04-computer-architecture/README.md):** The stored-program computer realises the universal Turing machine; [the instruction set architecture (ISA) contract](../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) is its transition table made concrete.
- **[05 Algorithms and Data Structures](../05-algorithms-and-data-structures/README.md):** The direct consumer. Asymptotic analysis and complexity classes become the [models of computation](../05-algorithms-and-data-structures/01-foundations/models-of-computation.md) and design paradigms there; NP-hardness motivates [approximation](../05-algorithms-and-data-structures/07-advanced-topics/approximation-algorithms.md).
- **[06 Programming Languages](../06-programming-languages/README.md):** Lambda calculus is the core of [functional languages](../06-programming-languages/01-paradigms/functional.md) and [type systems](../06-programming-languages/02-semantics-and-types/type-systems.md); grammars and automata drive [lexing and parsing](../06-programming-languages/03-compilers/lexing-and-parsing.md); undecidability bounds [formal methods](../06-programming-languages/05-formal-methods/README.md).
- **[11 Security and Cryptography](../11-security-and-cryptography/README.md):** Modern cryptography is built on computational hardness assumptions and entropy; Shor's algorithm is why [public-key cryptography](../11-security-and-cryptography/02-cryptography/public-key-cryptography.md) is being replaced.
- **[13 Artificial Intelligence](../13-artificial-intelligence/README.md):** Cross-entropy and mutual information are the objectives of [learning](../13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md); PSPACE-hardness (hardness for all polynomial-space problems) of planning explains why [search and planning](../13-artificial-intelligence/01-classical-ai/search-and-planning.md) relies on heuristics.

## Connections across layers

Beyond the neighbours above, channel capacity and error-correcting codes set the limits of the [link layer](../08-networking/02-link-layer/encoding-and-framing.md) and [storage devices](../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md); impossibility results in [distributed systems](../10-distributed-and-parallel-computing/02-distributed-foundations/impossibility-results.md) echo the style of undecidability proofs; and Rice's theorem explains why [static analysis](../12-software-engineering/03-quality/static-analysis-and-code-review.md) must approximate.

## Cross-cutting threads

- [Limits and impossibility](../CROSS-CUTTING.md#limits-and-impossibility): the home of the deepest limits in CS: entropy, capacity, undecidability, hardness, Holevo's bound.
- [Recursion and self-reference](../CROSS-CUTTING.md#recursion-and-self-reference): universal machines and diagonal arguments are programs reasoning about programs.
- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): the Church–Turing thesis lets every upper layer treat any computer as the same abstract machine.
- [Encoding and representation](../CROSS-CUTTING.md#encoding-and-representation): problems become languages, machines become strings, messages become codes.
- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): expressiveness against decidability, time against space, rate against reliability.
- [Redundancy and fault tolerance](../CROSS-CUTTING.md#redundancy-and-fault-tolerance): error-correcting codes, classical and quantum.
- [Trust and verification](../CROSS-CUTTING.md#trust-and-verification): NP certificates and the limits on verifying programs automatically.
