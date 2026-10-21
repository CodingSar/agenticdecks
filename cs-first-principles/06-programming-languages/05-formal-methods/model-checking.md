# Model Checking

> **Layer:** [06 Programming Languages](../README.md) › [Formal Methods](README.md)
> **Builds on:** [Finite automata and regular languages](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md), [Graph traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md), [Propositional logic](../../01-mathematical-foundations/01-logic/propositional-logic.md), [Finite-state machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md)
> **Enables:** [Consensus](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md), [Secure protocols](../../11-security-and-cryptography/02-cryptography/secure-protocols-and-tls.md), [Deadlock](../../07-operating-systems/03-concurrency/deadlock.md)

## Essence

Model checking (Clarke and Emerson, 1981; Queille and Sifakis, 1982) verifies a system automatically by exploring every state it can reach and checking that a property holds in all of them. The system is described as a finite state-transition model; the property is written in temporal logic, which can say things like "the two processes are never in the critical section together" or "every request is eventually answered". If the property fails, the checker returns a counterexample: a concrete execution trace that leads to the violation. That trace is often the most valuable output, because it shows a bug in a concurrent design that testing would almost never hit. The single idea is **exhaustive search of a finite state space, made feasible by clever representation and reduction**, with the state-explosion problem as the constant enemy.

## Core tenets

1. **Finite state spaces make verification decidable.** General program verification is undecidable, but whether a finite graph has a path to a bad state is just [graph search](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md). Model checking buys full automation by restricting to finite models, or finite abstractions of infinite systems. The price is that the model, not the code, is usually what gets verified.
2. **Temporal logic states properties over executions, not single states.** Linear Temporal Logic (LTL) (Pnueli, 1977) talks about each execution path: `G ¬(crit1 ∧ crit2)` ("globally, never both critical"), `G (req → F ack)` ("every request is eventually acknowledged"). Computation Tree Logic (CTL) quantifies over branching futures: `AG EF reset` ("from every reachable state, a reset is always possible").
3. **Safety and liveness are the two fundamental kinds of property.** A safety property says nothing bad ever happens; any violation has a finite counterexample (a trace to the bad state). A liveness property says something good eventually happens; a violation is an infinite trace in which it never does, shown as a lasso (a path into a cycle). Every property is the intersection of a safety and a liveness property (Alpern and Schneider, 1985).
4. **Concurrency causes state explosion.** A system of n components, each with k local states, can have up to kⁿ global states, and interleavings multiply paths further. Ten processes with ten states each give ten billion combinations. This exponential growth is the central problem of the field, and every major technique is a way to fight it.
5. **Symbolic model checking represents sets of states as formulas.** Instead of listing states, represent them as a Boolean function using Binary Decision Diagrams (BDDs) (Bryant, 1986). McMillan's symbolic model checking (1990s) computed reachable sets with BDD operations and verified hardware with more than 10²⁰ states. Bounded model checking instead unrolls the transition relation k steps into a Boolean Satisfiability (SAT) formula and asks a SAT solver for a counterexample of length at most k.
6. **Reductions shrink the space without losing answers.** Partial-order reduction explores only one ordering of independent actions (if two threads touch disjoint variables, both interleavings lead to the same state). Symmetry reduction treats identical processes as interchangeable. Abstraction replaces concrete data with a few abstract values, and Counterexample-Guided Abstraction Refinement (CEGAR) refines the abstraction whenever a counterexample turns out to be spurious.
7. **Automata connect temporal logic and the model.** An LTL property can be translated into a Büchi automaton, an automaton over infinite words. Checking the model against the property becomes checking that the product of the model and the automaton for the property's negation has no accepting cycle, a nested depth-first search. This is how the SPIN model checker works.
8. **Industry uses model checking where concurrency bugs are expensive.** Hardware companies adopted it after the 1994 Pentium floating-point division bug made the cost of escaped bugs visible. Amazon Web Services engineers used the Temporal Logic of Actions (TLA+) and its model checker to find subtle bugs in designs for DynamoDB and S3 (Newcombe et al., 2015). Microsoft's Static Driver Verifier model-checks Windows drivers against interface rules.

   ```tla
   \* TLA+ invariant for a mutual-exclusion protocol
   MutualExclusion == ~(pc[1] = "cs" /\ pc[2] = "cs")
   ```

## Key concepts

| Term | Meaning |
|---|---|
| Kripke structure | A state-transition graph labelled with the propositions true in each state |
| Linear Temporal Logic (LTL) | Logic over single execution paths with operators G (always), F (eventually), X (next), U (until) |
| Computation Tree Logic (CTL) | Logic that quantifies over all (A) or some (E) future paths |
| Safety property | "Nothing bad happens"; violated by a finite trace |
| Liveness property | "Something good eventually happens"; violated by an infinite trace |
| Counterexample | A concrete execution demonstrating a property violation |
| State explosion | Exponential growth of global states with the number of components |
| Binary Decision Diagram (BDD) | A compact canonical graph representation of a Boolean function |
| Bounded model checking | Searching for violations up to depth k using a satisfiability solver |
| Partial-order reduction | Exploring one representative ordering of independent concurrent actions |

## How it fits

- **Below:** Models are [finite-state machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md) and [automata](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md); exploration is [graph traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md); BDDs and SAT build on [propositional logic](../../01-mathematical-foundations/01-logic/propositional-logic.md) and [Boolean algebra](../../01-mathematical-foundations/04-algebra/boolean-algebra.md). SAT is [complete for NP (nondeterministic polynomial time)](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md), yet modern solvers handle millions of variables in practice.
- **Above:** Model checking verifies [consensus protocols](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md), [cache-coherence protocols](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md), [security protocols](../../11-security-and-cryptography/02-cryptography/secure-protocols-and-tls.md) and freedom from [deadlock](../../07-operating-systems/03-concurrency/deadlock.md) in concurrent code.
- **Siblings:** Fully automatic where [Hoare logic](hoare-logic-and-program-proofs.md) needs human invariants, but limited to finite models where [proof assistants](proof-assistants-and-dependent-types.md) handle unbounded systems.

## Common misconceptions

- **"Model checking proves the code correct."** Usually it checks a model of the design; bugs introduced when implementing the model are not caught unless the model is derived from the code.
- **"No counterexample means the system is correct."** It means the model satisfies the stated properties within any bounds used; missing properties and too-small bounds are common gaps.
- **"State explosion makes it useless for real systems."** Symbolic methods, reductions and abstraction routinely handle industrial hardware and protocol designs, and small-scope bugs are found quickly even when full verification is out of reach.

## Go deeper

- Edmund M. Clarke, Orna Grumberg and Doron A. Peled, *Model Checking* (1999): the standard textbook.
- Leslie Lamport, *Specifying Systems* (2002): TLA+ for engineers designing concurrent and distributed systems.
- Chris Newcombe et al., "How Amazon Web Services Uses Formal Methods" (2015): industrial experience.
