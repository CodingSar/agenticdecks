# The Church–Turing Thesis

> **Layer:** [02 Theory of Computation](../README.md) › [Computability](README.md)
> **Builds on:** [Turing Machines](turing-machines.md), [Lambda Calculus](lambda-calculus.md), [Thermodynamics and Energy](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md)
> **Enables:** [Halting Problem and Undecidability](halting-problem-and-undecidability.md), [Complexity Classes](../04-complexity/complexity-classes.md), [Qubits and Quantum Circuits](../05-quantum-computation/qubits-and-quantum-circuits.md), [Digital Logic](../../03-digital-logic/README.md), [History of Computing](../../15-computing-in-context/history-of-computing.md)

## Essence

The Church–Turing thesis says that every function that can be computed by an effective procedure (a finite, mechanical, step-by-step method that a careful clerk could follow without insight) can be computed by a Turing machine. It is not a theorem, because "effective procedure" is an informal notion; it is a claim that a mathematical definition captures an intuitive one. The evidence is overwhelming: every model ever proposed (Turing machines, lambda calculus, recursive functions, Post systems, register machines, modern programming languages) computes exactly the same class of functions. The thesis is where the formal pillar of Computer Science (CS) meets the physical one: it licenses us to treat "what a computer can do" and "what a Turing machine can do" as the same question.

## Core tenets

1. **It equates an informal notion with a formal one.** The informal side is "effectively calculable". The formal side is "Turing-computable" (equivalently, lambda-definable or general recursive). Because one side is informal, the thesis cannot be proved, only supported or refuted by a counterexample: a procedure everyone agrees is mechanical that no Turing machine can carry out. None has been found since 1936.

2. **The main evidence is convergence.** Around 1936, Church (lambda calculus), Gödel and Kleene (general recursive functions), Turing (machines) and Post (production systems) proposed independent definitions; all were proved equivalent. Every later model (random-access machines, cellular automata, every general-purpose programming language) also lands in the same class. Independent definitions that keep agreeing suggest they have found something real.

3. **Turing's own argument is conceptual, not just empirical.** He analysed a human computer: finitely many distinguishable symbols in view, finitely many states of mind, local changes, attention moving a bounded distance per step. Each restriction is forced by human finitude, and together they yield exactly a Turing machine. This is why Gödel, unconvinced by earlier definitions, accepted Turing's as the right one.

4. **The thesis makes impossibility results meaningful.** Without it, "no Turing machine decides halting" would be a fact about one formalism. With it, the [halting problem](halting-problem-and-undecidability.md) becomes unsolvable by *any* algorithm in any language on any computer. Every undecidability result in programming, verification and mathematics inherits its force from the thesis.

5. **The physical Church–Turing thesis is a separate, stronger claim.** It says any function computable by a physical system is Turing-computable. This is a claim about physics, not mathematics. Proposed "hypercomputers" rely on infinite precision, infinite steps in finite time or exotic spacetimes, and none is believed physically realisable. Finite energy and finite information density ([thermodynamics](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md)) are the usual reasons. Quantum computers do *not* violate it: a classical machine can simulate them, slowly.

6. **The extended (complexity-theoretic) thesis is about efficiency, and is probably false.** The extended thesis says any reasonable physical model can be simulated by a probabilistic Turing machine with only polynomial overhead. If so, the class of efficiently solvable problems would be the same on every machine. [Quantum computation](../05-quantum-computation/quantum-algorithms.md) is the main challenge: Shor's algorithm factors integers in polynomial time, a task with no known efficient classical algorithm. If large quantum computers work as theory predicts, the extended thesis fails while the original thesis stands.

7. **It is the bridge that lets hardware stand in for mathematics.** Because a stored-program computer with enough memory can simulate a universal Turing machine, and vice versa, theorems about Turing machines are theorems about real computers (up to memory limits). This is the link between this layer and [digital logic](../../03-digital-logic/README.md) and [architecture](../../04-computer-architecture/README.md): physics builds the machine, and the thesis says it is the right machine.

## Key concepts

| Term | Meaning |
|---|---|
| Effective procedure | Finite, mechanical, insight-free method that always follows explicit rules |
| Turing-computable | Computable by some Turing machine that halts on the input |
| General recursive function | Function built from basics by composition, primitive recursion and unbounded search |
| Physical Church–Turing thesis | Any physically realisable computation is Turing-computable |
| Extended Church–Turing thesis | Any reasonable model is simulable with polynomial overhead |
| Hypercomputation | Hypothetical computation beyond Turing machines |

## How it fits

- **Below:** It rests on the formal definitions of [Turing machines](turing-machines.md) and [lambda calculus](lambda-calculus.md) and on [proof techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md) for their equivalence. Its physical form draws on [physics of computation](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md) and [quantum mechanics](../../00-engineering-foundations/01-physics-of-computation/quantum-mechanics-and-band-theory.md).
- **Above:** It justifies the claim that one general-purpose computer ([the instruction set architecture contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md)) can run any algorithm, that every general-purpose [programming language](../../06-programming-languages/README.md) is equally expressive, and that undecidability limits [static analysis](../../12-software-engineering/03-quality/static-analysis-and-code-review.md) and [formal methods](../../06-programming-languages/05-formal-methods/model-checking.md). Its history is part of the [history of computing](../../15-computing-in-context/history-of-computing.md).
- **Siblings:** It explains why the [Turing machine](turing-machines.md) and [lambda calculus](lambda-calculus.md) leaves describe the same thing, and why the [halting problem](halting-problem-and-undecidability.md) is a universal limit. Its extended form links to [complexity](../04-complexity/complexity-classes.md) and [quantum computation](../05-quantum-computation/README.md).

## Common misconceptions

- **"The thesis is a proven theorem."** It cannot be proved because one side is informal. What is proved is the equivalence of the formal models.
- **"It says the human mind (or the universe) is a Turing machine."** The original thesis concerns what a human following rules can compute, not everything humans or nature do. Stronger physical and cognitive versions are separate, debated claims.
- **"Quantum computers refute Church–Turing."** They compute the same functions as classical machines. At most they refute the *extended* thesis about efficiency.

## Go deeper

- Alan M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem" (1936): section 9 gives the analysis of a human computer.
- Robin Gandy, "Church's Thesis and Principles for Mechanisms" (1980): an analysis of the physical, machine version.
- B. Jack Copeland, "The Church-Turing Thesis", *Stanford Encyclopedia of Philosophy* (first published 1997, revised since): a careful survey of the versions and their status.
- Scott Aaronson, *Quantum Computing Since Democritus* (2013): the extended thesis and its quantum challenge.
