# Reliability and Redundancy

> **Layer:** [00 Engineering Foundations](../README.md) › [Engineering Method](README.md)
> **Builds on:** [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Noise and Signal Integrity](../02-electrical-circuits/noise-and-signal-integrity.md)
> **Enables:** [Channel Capacity and Error Correction](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md), [Replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md), [Reliability Engineering](../../12-software-engineering/04-operations/reliability-engineering.md), [Crash Consistency and Journaling](../../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md)

## Essence

Every component eventually fails, and a system built from many components fails more often than any one of them. Reliability engineering quantifies this with probability and fights it with redundancy: extra copies, extra bits or extra time arranged so that the system keeps working when parts do not. The key insight, due to John von Neumann, is that reliable systems can be built from unreliable parts, provided failures are detected or outvoted and, crucially, are independent. Most real reliability problems come from failures that are not independent: shared power, shared software bugs, shared assumptions. The same reasoning reappears at every layer, from error-correcting memory to replicated databases.

## Core tenets

1. **Fault, error and failure are distinct.** A fault is a defect or event (a broken transistor, a cosmic-ray strike, a bug). An error is the resulting incorrect internal state (a flipped bit). A failure is when the delivered service deviates from its specification. Redundancy works by stopping faults from becoming errors, or errors from becoming failures. Avizienis and colleagues (2004) give the standard taxonomy.

2. **Series systems are weaker than their weakest part.** If a system needs all `n` independent components to work, its reliability is the product `R = R1 · R2 · ... · Rn`. A thousand components each 99.99% reliable give a system that is only about 90% reliable. This is why large systems such as data centres with 10⁵ disks see failures every day: at scale, failure is a normal operating condition, not an exception.

3. **Parallel redundancy multiplies unreliabilities.** If a system works when *any* of `n` independent copies works, its failure probability is the product of the copies' failure probabilities: `1 - R = (1 - R1)(1 - R2)...`. Two copies each failing with probability 1% fail together with probability 0.01%. Redundancy therefore buys reliability exponentially in the number of copies, as long as failures are independent.

4. **Independence is the assumption that breaks.** Common-mode failures, such as a shared power supply, a firmware bug present in every replica, a flood in the one building, or a load spike that hits all servers, defeat redundancy because the copies fail together. Designing for reliability is largely the work of finding and removing hidden correlations: diverse hardware, separate failure domains, staggered updates.

5. **Masking requires a majority; detection requires only a difference.** Two copies that disagree reveal an error but cannot say which is right. Three copies with a majority vote, Triple Modular Redundancy (TMR), can mask one failure. In general, masking `f` arbitrary failures needs `2f + 1` copies, and tolerating `f` malicious (Byzantine) ones needs `3f + 1`. Detection plus a retry or a fallback is often cheaper than masking.

6. **Information redundancy is the most efficient kind.** Rather than copying data whole, add a few check bits computed from it. A parity bit detects any single-bit error; a Hamming code (1950) corrects single-bit errors with only `log2 n` extra bits for `n` data bits. Error-Correcting Code (ECC) memory, Redundant Array of Independent Disks (RAID) parity and network checksums all trade a little storage for a large gain in reliability.

7. **Availability depends on repair as much as on failure.** Availability is Mean Time To Failure (MTTF) divided by the sum of MTTF and Mean Time To Repair (MTTR): `MTTF / (MTTF + MTTR)`. Halving repair time improves availability as much as doubling component life. Hence the emphasis on fast detection, automatic failover and quick restart in every layer above.

8. **Failure rates change over a component's life.** Hardware often follows a "bathtub curve": high early failure (manufacturing defects, weeded out by burn-in), a long period of low constant rate, then rising wear-out. A constant rate implies an exponential lifetime distribution, the usual simplifying assumption in reliability models; it is wrong at the start and end of life.

## Key concepts

| Term | Meaning |
|---|---|
| Reliability `R(t)` | Probability a component works without failure up to time `t`. |
| Availability | Fraction of time a system delivers correct service. |
| Mean Time To Failure (MTTF) | Expected time until a component fails. |
| Mean Time To Repair (MTTR) | Expected time to restore service after failure. |
| Fault / error / failure | Cause / incorrect state / visible deviation from specification. |
| Common-mode failure | A single cause that fails several redundant copies together. |
| Triple Modular Redundancy (TMR) | Three copies with majority voting to mask one failure. |
| Error-correcting code | Added check bits that let errors be detected and corrected. |
| Failure domain | A set of components that can fail together from one cause. |

## How it fits

- **Below:** Reliability models are applied [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md). Physical fault sources, such as soft errors and noise, come from [noise and signal integrity](../02-electrical-circuits/noise-and-signal-integrity.md) and wear-out from [thermodynamics](../01-physics-of-computation/thermodynamics-and-energy.md).
- **Above:** Information redundancy is formalised in [channel capacity and error correction](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md) and used in [Dynamic Random-Access Memory (DRAM) and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md). Time redundancy (retry) and logging appear in [reliable delivery](../../08-networking/04-transport-layer/reliable-delivery.md) and [crash consistency](../../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md). Replication and voting lead to [replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md), [consensus](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md) and [Byzantine fault tolerance](../../10-distributed-and-parallel-computing/03-consensus-and-replication/byzantine-fault-tolerance.md). Operating practice is in [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md). See also [redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance).
- **Siblings:** Redundancy is a [tradeoff](tradeoffs-and-constraints.md) of cost for dependability, and estimating failure rates depends on [measurement and modeling](measurement-and-modeling.md).

## Common misconceptions

- **"Two copies double the reliability."** With independent failures they do much better than double; with correlated failures they may do almost nothing.
- **"Redundancy always helps."** Every extra component adds failure modes, and the switching and voting logic can itself become the single point of failure.
- **"High reliability means rare failures."** At scale, high availability comes from tolerating frequent component failures and repairing quickly.

## Go deeper

- John von Neumann, "Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components" (1956): the founding argument for redundancy.
- Algirdas Avizienis, Jean-Claude Laprie, Brian Randell and Carl Landwehr, "Basic Concepts and Taxonomy of Dependable and Secure Computing" (2004): the standard vocabulary.
- Richard Hamming, "Error Detecting and Error Correcting Codes" (1950): the first practical error-correcting codes.
