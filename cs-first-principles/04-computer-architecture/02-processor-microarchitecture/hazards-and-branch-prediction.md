# Hazards and Branch Prediction

> **Layer:** [04 Computer Architecture](../README.md) › [Processor Microarchitecture](README.md)
> **Builds on:** [Pipelining](pipelining.md), [Finite-state machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md)
> **Enables:** [Superscalar and out-of-order](superscalar-and-out-of-order.md), [Side channels](../../11-security-and-cryptography/03-system-security/side-channels.md), [Compiler optimization](../../06-programming-languages/03-compilers/optimization.md)

## Essence

A hazard is any situation in which the next instruction in a pipeline cannot proceed in the next cycle without risking a wrong result. There are three kinds: **structural** (two instructions need the same hardware), **data** (an instruction needs a value an earlier one has not produced yet) and **control** (the pipeline does not yet know which instruction comes next because a branch is unresolved). Data hazards are mostly removed by forwarding results directly between stages. Control hazards are removed by *predicting* the branch outcome, fetching down the guessed path, and throwing that work away if the guess was wrong. Modern predictors are right more than 95% of the time on typical code, and that accuracy is what makes deep, wide pipelines worth building.

## Core tenets

1. **Structural hazards are solved by duplicating or separating resources.** If instruction fetch and data access share one memory port, a load and a fetch collide in the same cycle. Separate instruction and data caches (a split L1, used by essentially every modern core) remove this hazard. Register files are built with enough ports for every stage that needs them.

2. **Most data hazards disappear with forwarding.** In `add x1,x2,x3` followed by `sub x4,x1,x5`, the sum exists at the end of the execute stage, one cycle before it would be written to the register file. Forwarding (bypass) multiplexers route it directly from the pipeline register back to the ALU input, so `sub` does not wait. Only true dependences on long-latency operations still stall.

3. **Load-use hazards remain and must be scheduled around.** A load's value arrives after the memory stage, too late to forward into an immediately following instruction's execute stage; the pipeline must stall at least one cycle (four to five cycles of L1 latency on 2020s cores). Compilers reorder independent instructions into that gap, and out-of-order hardware does the same dynamically.

4. **Branches are frequent, so control hazards dominate.** Roughly one instruction in five to seven is a branch in typical integer code. If the pipeline waited for each branch to resolve, a deep pipeline would lose 10–20 cycles per branch. The penalty grows with depth and width: on a core that can issue six instructions per cycle and resolves branches 15 cycles in, one misprediction wastes up to 90 instruction slots.

5. **Prediction works because branches are predictable.** Loop branches are taken almost every time; many `if` statements go the same way most of the time; and many branches correlate with recent branches. A two-bit saturating counter per branch, indexed by its address, captures bias and tolerates a single anomaly. Correlating predictors (gshare, 1993) combine global history of recent outcomes with the address. Modern designs such as TAGE (Seznec, 2006) and perceptron predictors use several tables indexed by histories of different lengths and achieve misprediction rates of a few per thousand instructions on many workloads.

6. **Targets must be predicted too, not only directions.** The fetch stage needs the next address before the branch is even decoded. A Branch Target Buffer (BTB) caches the target address of recently taken branches, indexed by the branch's PC. A Return Address Stack predicts `return` targets by mirroring calls. Indirect branches (virtual calls, `switch` jump tables, interpreter dispatch) need dedicated indirect-target predictors.

7. **Speculation is correct only if mispredicted work leaves no architectural trace.** Instructions fetched down a wrong path must never update registers, memory, or raise exceptions; they are squashed when the branch resolves. But they *do* change microarchitectural state such as caches and predictor tables. Spectre (2018) showed that an attacker can steer speculation to read secrets and leak them through that residue, which turned a performance mechanism into a security boundary.

8. **Sometimes avoiding the branch beats predicting it.** Conditional moves and predicated instructions (`cmov` on x86, `csel` on ARM) turn a short unpredictable `if` into straight-line data flow. Compilers use them when a branch is likely to be mispredicted, such as data-dependent comparisons in sorting or searching.

## Key concepts

| Term | Meaning |
|---|---|
| Structural hazard | Two instructions need the same hardware resource in the same cycle |
| Data hazard | An instruction depends on a result not yet available (read-after-write) |
| Control hazard | Next instruction address unknown because a branch is unresolved |
| Forwarding (bypassing) | Routing a result from a later stage directly to an earlier stage's input |
| Stall | Holding an instruction back and inserting a bubble |
| Branch predictor | Hardware that guesses whether a conditional branch is taken |
| BTB | Branch Target Buffer: cache of predicted target addresses keyed by branch address |
| Misprediction penalty | Cycles lost flushing wrong-path instructions, roughly the depth to branch resolution |
| Speculative execution | Executing instructions before it is known that they should run |

## How it fits

- **Below:** predictors are small tables of [finite-state machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md) (saturating counters); their design is a problem of predicting from history, related to [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) and online learning.
- **Above:** [compiler optimizations](../../06-programming-languages/03-compilers/optimization.md) schedule loads early, unroll loops and use conditional moves; interpreters and [JIT compilers](../../06-programming-languages/04-runtime-systems/jit-compilation.md) are shaped by indirect-branch cost; [side-channel attacks](../../11-security-and-cryptography/03-system-security/side-channels.md) exploit speculation.
- **Siblings:** hazards are created by [pipelining](pipelining.md); [out-of-order execution](superscalar-and-out-of-order.md) generalises forwarding and speculation to hundreds of instructions.

## Common misconceptions

- **"Branch prediction is a minor optimisation."** On a deep, wide core, a mispredicted branch costs on the order of 15–20 cycles; code with random branches can run several times slower than the same code with predictable ones.
- **"Speculation is invisible because it is rolled back."** Architectural state is rolled back; microarchitectural state (caches, TLBs, predictors) is not, which is exactly what Spectre exploits.
- **"Data hazards always stall."** With forwarding, back-to-back dependent ALU instructions run without a stall; only loads and multi-cycle operations stall dependents.

## Go deeper

- Hennessy and Patterson, *Computer Architecture: A Quantitative Approach* (6th ed., 2017), Appendix C and Chapter 3: hazards, forwarding and dynamic prediction.
- Smith, *A Study of Branch Prediction Strategies* (ISCA 1981): the origin of counter-based prediction.
- Seznec and Michaud, *A Case for (Partially) TAgged GEometric History Length Branch Prediction* (JILP 2006): the TAGE predictor behind most modern designs.
- Kocher et al., *Spectre Attacks: Exploiting Speculative Execution* (IEEE S&P 2019): how speculation became a security problem.
