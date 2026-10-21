# Formal Methods

> **Layer:** [06 Programming Languages](../README.md) › Formal Methods
> **Children:** [Hoare Logic and Program Proofs](hoare-logic-and-program-proofs.md) · [Model Checking](model-checking.md) · [Proof Assistants and Dependent Types](proof-assistants-and-dependent-types.md)

## What this area is about

Testing shows that a program works on the inputs you tried; formal methods show that it works on all of them. A formal method writes down a specification in logic, then establishes by mathematical proof or exhaustive search that the program, or a model of it, meets that specification. The goal is the strongest kind of assurance software can have, for the systems where failure is unacceptable: processors, compilers, operating-system kernels, cryptographic code, flight control and distributed protocols.

The unifying idea is **turning "is this program correct?" into a question of logic that a machine can check**. The field faces a hard wall: by [Rice's theorem](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), no algorithm can decide non-trivial properties of all programs. Each child is a different way around that wall. Hoare logic asks a human for the hard parts (loop invariants) and checks the rest. Model checking restricts to finite-state systems, where exhaustive search is possible. Proof assistants ask a human to build the whole proof interactively, but check every step against a small trusted kernel.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Hoare Logic and Program Proofs](hoare-logic-and-program-proofs.md) | Deductive reasoning about imperative programs with pre/postconditions and invariants | Predicate logic, axiomatic semantics |
| [Model Checking](model-checking.md) | Automatic, exhaustive exploration of a finite state space against temporal-logic properties | Automata, graph search |
| [Proof Assistants and Dependent Types](proof-assistants-and-dependent-types.md) | Interactive, machine-checked proofs; types expressive enough to state full specifications | Type systems, Curry–Howard |

```
                    automation
          high  <-------------------->  low
   Model checking     Hoare-style verifiers     Proof assistants
   (finite models,    (human gives invariants,  (human guides every proof,
    push-button,       a solver proves the       any property expressible,
    counterexamples)   verification conditions)  tiny trusted kernel)
          low   <-------------------->  high
                    expressiveness
```

Read Hoare logic first: it introduces specifications, invariants and the idea of verification conditions that everything else uses. Model checking is the push-button alternative for concurrent and protocol designs. Proof assistants are the most general and most labour-intensive, and through dependent types they also show that types and proofs are the same thing. In practice the three are combined: verifiers such as Dafny generate Hoare-style conditions and discharge them with automatic Satisfiability Modulo Theories (SMT) solvers, and proof assistants embed model checkers and solvers as tactics.

## Connections to sibling areas

- **[Paradigms](../01-paradigms/README.md).** Pure functional code is easiest to prove because it supports equational reasoning; imperative code needs Hoare logic to track state; logic programming and constraint solvers provide the automation inside verifiers.
- **[Semantics and Types](../02-semantics-and-types/README.md).** Hoare logic is an axiomatic semantics; proofs of soundness for type systems are formal methods applied to languages; dependent types are the far end of the type-system spectrum.
- **[Compilers](../03-compilers/README.md).** Verified compilers such as CompCert prove that compilation preserves meaning; translation validation checks each individual compilation instead.
- **[Runtime Systems](../04-runtime-systems/README.md).** Garbage collectors, memory models and Just-In-Time (JIT) compilers are subtle concurrent systems and are classic targets for model checking and proof.

## Connections across layers

Formal methods rest on [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md), [proof techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md) and [induction](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) from 01, and on [automata](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md), [computability](../../02-theory-of-computation/03-computability/README.md) and [complexity](../../02-theory-of-computation/04-complexity/README.md) from 02. Hardware verification ([hardware description languages](../../03-digital-logic/04-hardware-design/hardware-description-languages.md)) was model checking's first major industrial success. Upward, formal methods verify [kernels](../../07-operating-systems/01-kernel-and-abstractions/kernel-architectures.md) (seL4), [consensus protocols](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md) (the Temporal Logic of Actions, TLA+, at Amazon), [cryptographic protocols](../../11-security-and-cryptography/02-cryptography/secure-protocols-and-tls.md), and they sit at the top of the assurance ladder in [software quality](../../12-software-engineering/03-quality/README.md), beyond [testing](../../12-software-engineering/03-quality/testing.md) and [static analysis](../../12-software-engineering/03-quality/static-analysis-and-code-review.md).

## Cross-cutting threads

- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): the whole area is about stating and proving invariants.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): small trusted proof checkers make large proofs believable.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): undecidability and state-space explosion shape every technique.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): proofs proceed by refinement from abstract specification to concrete code.
- [Composition](../../CROSS-CUTTING.md#composition): modular proofs (frame rules, assume-guarantee) let verification scale.
