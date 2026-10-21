# Turing Machines

> **Layer:** [02 Theory of Computation](../README.md) › [Computability](README.md)
> **Builds on:** [The Chomsky Hierarchy](../02-automata-and-formal-languages/chomsky-hierarchy.md), [Finite Automata and Regular Languages](../02-automata-and-formal-languages/finite-automata-and-regular-languages.md), [Functions and Cardinality](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md)
> **Enables:** [Church–Turing Thesis](church-turing-thesis.md), [Halting Problem and Undecidability](halting-problem-and-undecidability.md), [Complexity Classes](../04-complexity/complexity-classes.md), [Models of Computation](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md), [The Instruction Set Architecture Contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md)

## Essence

A Turing Machine (TM) is a finite automaton given an unbounded tape it can read, write and move along in both directions. Alan Turing designed it in 1936 by analysing what a human clerk does when computing with pencil and paper: look at a few symbols, consult a finite set of instructions, change a symbol, shift attention, repeat. The model is deliberately primitive, yet it can simulate every other reasonable model of computation, and one fixed machine (the universal TM) can simulate *any* TM given its description as input. That universal machine is the mathematical blueprint of the stored-program computer: a program is just data that a general machine interprets.

## Core tenets

1. **The definition is tiny.** A TM is (Q, Σ, Γ, δ, q₀, q_accept, q_reject): finite states Q, input alphabet Σ, tape alphabet Γ ⊇ Σ ∪ {blank}, and a transition function δ: Q × Γ → Q × Γ × {L, R}. Each step reads the symbol under the head, writes a symbol, moves one cell, and changes state. A *configuration* (state, tape contents, head position) captures everything about the computation at one instant, so a run is a sequence of configurations.

2. **There are three outcomes, not two.** On a given input a TM may accept, reject, or run forever. A language is *decidable* (recursive) if some TM halts on every input with the right answer. It is *recognisable* (recursively enumerable) if some TM accepts exactly its members but may loop on non-members. The gap between those two notions is where [undecidability](halting-problem-and-undecidability.md) lives.

3. **The model is robust: variants add speed, not power.** Multiple tapes, two-way infinite tapes, extra symbols, random-access memory and nondeterminism all compute exactly the same functions. A k-tape TM running in time t can be simulated by a one-tape TM in O(t²) time. A nondeterministic TM can be simulated deterministically by breadth-first search of its computation tree, with exponential slowdown. This robustness is the evidence behind the [Church–Turing thesis](church-turing-thesis.md), and the size of the slowdowns is the subject of [complexity theory](../04-complexity/complexity-classes.md).

4. **Machines are strings, so machines can process machines.** Any TM can be encoded as a finite string ⟨M⟩ over a fixed alphabet, which means TMs can be enumerated: M₁, M₂, M₃, and so on. There are therefore only countably many TMs but uncountably many languages ([Cantor](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md)), so almost every language is undecidable. Encoding programs as data is the root of both universality and self-reference.

5. **A universal TM exists.** There is a single machine U such that U(⟨M⟩, w) behaves exactly like M on w: it accepts, rejects or loops when M does. U keeps M's description on one part of its tape and M's simulated tape on another, and repeatedly looks up the transition to apply. The overhead is small (a logarithmic factor in time for a multitape U, with constants depending on M), so one general machine plus software replaces all special-purpose machines.

6. **Turing completeness is easy to reach.** Any system that can simulate a universal TM, given unbounded memory, is Turing complete. Very small systems qualify: two-counter machines, the lambda calculus, Conway's Game of Life, Rule 110 cellular automata, and accidentally even C++ templates and some configuration languages. The ingredients are conditional branching plus unbounded, rewritable storage.

7. **Real computers are TMs with finite tapes, and that is the right idealisation.** A physical machine has finitely many states, so strictly it is a finite automaton. But the number of states (2 to the number of memory bits) is so large that the TM model, which ignores the bound, predicts real behaviour far better. Theory proves lower bounds on the TM; engineering runs programs on approximations of it.

8. **TMs define cost as well as possibility.** Steps of a TM give time; cells visited give space. Because reasonable models simulate each other with only polynomial overhead, classes like P are the same whether defined on TMs or Random Access Machines (RAMs). For analysing actual algorithms the RAM, which can fetch any memory word in one step, is the more faithful model ([models of computation](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md)).

## Key concepts

| Term | Meaning |
|---|---|
| Tape | Unbounded sequence of cells, each holding one symbol |
| Transition function δ | (state, symbol read) → (new state, symbol to write, move L/R) |
| Configuration | Complete snapshot: state, tape contents, head position |
| Decidable | Some TM halts on all inputs and answers correctly |
| Recognisable | Some TM accepts exactly the members; may loop otherwise |
| Universal TM | One machine that simulates any machine from its description |
| Turing complete | Able to simulate a universal TM, given unbounded memory |
| Encoding ⟨M⟩ | A finite string describing machine M |

## How it fits

- **Below:** A TM is a [finite automaton](../02-automata-and-formal-languages/finite-automata-and-regular-languages.md) plus a tape, the top of the [Chomsky hierarchy](../02-automata-and-formal-languages/chomsky-hierarchy.md). Its counting arguments use [cardinality](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md).
- **Above:** The universal TM became the stored-program (von Neumann) computer, whose [instruction set](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) is a concrete transition table and whose memory is the tape. [Interpreters and virtual machines](../../06-programming-languages/04-runtime-systems/interpreters-and-virtual-machines.md) are universal machines in software. The RAM model used in [algorithm analysis](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md) is a TM variant chosen to match hardware costs.
- **Siblings:** [Lambda calculus](lambda-calculus.md) defines computation by substitution instead of state change; the [Church–Turing thesis](church-turing-thesis.md) explains why both define the same class; the [halting problem](halting-problem-and-undecidability.md) uses universality and encoding to show what no TM can do.

## Common misconceptions

- **"A Turing machine is a practical design."** It is a mathematical definition chosen for easy proofs. Nobody builds one; its value is that anything built can be reduced to it.
- **"Nondeterministic TMs can compute more."** They compute exactly the same functions. Whether they compute them *faster* by more than a polynomial is the P versus NP (polynomial versus nondeterministic polynomial time) question.
- **"Turing complete means powerful or useful."** It only means general. Many Turing-complete systems are hopeless to program, and many useful languages (Structured Query Language (SQL) without recursion, regular expressions) are deliberately not Turing complete so they always terminate.

## Go deeper

- Alan M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem" (1936): the original paper; section 9 is the clerk argument.
- Michael Sipser, *Introduction to the Theory of Computation* (3rd ed., 2012), chapter 3: the definitions and robustness results.
- Marvin L. Minsky, *Computation: Finite and Infinite Machines* (1967): small universal machines and counter machines.
