# Engineering Method

> **Layer:** [00 Engineering Foundations](../README.md) › Engineering Method
> **Children:** [Tradeoffs and Constraints](tradeoffs-and-constraints.md) · [Reliability and Redundancy](reliability-and-redundancy.md) · [Measurement and Modeling](measurement-and-modeling.md)

## What this area is about

The other four areas of this layer describe *what* physical computing is made of. This one describes *how engineers think* when they build with it. It answers: *how do you design something that works, reliably and at acceptable cost, when every choice has a price and every model is approximate?* The answers are not specific to electronics; they are the habits that every higher layer of computer science inherits, from processor design to distributed systems to machine-learning practice.

The unifying idea is **deciding under constraints with imperfect knowledge**. Tradeoffs and constraints define the space of acceptable designs and the frontier of best ones. Reliability and redundancy deal with the certainty that parts fail, by spending resources to keep the whole working. Measurement and modelling are how you know where you stand: models predict, measurements check, and the gap between them is where engineering learning happens.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Tradeoffs and Constraints](tradeoffs-and-constraints.md) | The decision framework: binding constraints, Pareto frontiers, figures of merit, common case, diminishing returns | Optimisation |
| [Reliability and Redundancy](reliability-and-redundancy.md) | Designing for failure: series and parallel reliability, independence, voting, codes, availability | Probability, tradeoffs |
| [Measurement and Modeling](measurement-and-modeling.md) | Knowing what is true: models and their validity, estimation, statistics of measurement, benchmarks | Statistics |

The three form a loop rather than a chain. You model a design to predict its cost and performance, locate it against the tradeoff frontier, add redundancy where failure would be unacceptable (itself a tradeoff of cost for dependability), measure the result, and revise the model. Read tradeoffs first because it frames the other two, then reliability as the most important specific tradeoff, then measurement as the discipline that keeps both honest.

```
        model ──predict──► design point on the tradeoff frontier
          ▲                         │
          │                   add redundancy where failure is unacceptable
       refine                       │
          └──── measure ◄───────────┘
```

## Connections to sibling areas

- **[Physics of Computation](../01-physics-of-computation/README.md):** Physics provides the hardest constraints (heat removal, the speed of light) and the irreducible fault sources (thermal noise, particle strikes).
- **[Electrical Circuits](../02-electrical-circuits/README.md):** The lumped model is the archetypal model with a validity domain; noise margins are a form of redundancy.
- **[Semiconductor Devices](../03-semiconductor-devices/README.md):** Yield is reliability statistics applied to manufacturing; scaling history is a sequence of tradeoffs as constraints shifted.
- **[Signals and Systems](../04-signals-and-systems/README.md):** Analog versus digital is a precision-cost tradeoff; feedback loops are a modelling and measurement problem in which stability must be verified.

## Connections across layers

These ideas reappear at every level. Tradeoffs: [the performance equation](../../04-computer-architecture/06-performance/the-performance-equation.md), [Amdahl's law](../../04-computer-architecture/06-performance/amdahls-law.md), [impossibility results](../../10-distributed-and-parallel-computing/02-distributed-foundations/impossibility-results.md) and [software architecture](../../12-software-engineering/01-design/software-architecture.md). Reliability: [channel capacity and error correction](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md), [crash consistency](../../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md), [replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md) and [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md). Measurement: [latency, bandwidth and queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md), [observability](../../12-software-engineering/04-operations/observability.md) and [evaluation and experimentation](../../13-artificial-intelligence/02-machine-learning-foundations/evaluation-and-experimentation.md). The mathematics comes from [optimization](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md), [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) and [statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md).

## Cross-cutting threads

- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): introduced here as a method, then met in every layer.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): extra copies, bits and time to survive failure.
- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): the measure-model-adjust loop of engineering itself.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): measure what you can rather than trusting models or intuition.
