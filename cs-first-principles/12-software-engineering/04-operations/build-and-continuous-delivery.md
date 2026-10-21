# Build and Continuous Delivery

> **Layer:** [12 Software Engineering](../README.md) › [Operations](README.md)
> **Builds on:** [Version control](../02-process/version-control.md), [Testing](../03-quality/testing.md), [Linking and loading](../../06-programming-languages/04-runtime-systems/linking-and-loading.md), [Graph traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md)
> **Enables:** [Reliability engineering](reliability-engineering.md), [Development lifecycles](../02-process/development-lifecycles.md)

## Essence

A build turns source code into runnable artifacts; a delivery pipeline takes each change from commit to production. Continuous integration (CI) means every change is merged into the main line and automatically built and tested, many times a day. Continuous delivery (CD) extends this so that every change that passes the pipeline is releasable at the push of a button, and continuous deployment releases it automatically. The core insight, made central by Humble and Farley (*Continuous Delivery*, 2010), is that releasing is risky in proportion to how much changes at once and how manual the process is. So make releases small, frequent, automated and reversible, and they become routine instead of dangerous.

## Core tenets

1. **A build is a function from inputs to outputs, and should behave like one.** If the same source, dependencies and tools always produce the same artifact, the build is *reproducible* and *hermetic*. Then outputs can be cached by a hash of their inputs, builds can be distributed across machines, and an artifact can be traced to the exact source that made it. Bazel (from Google's internal Blaze) and Nix are built on this idea; reproducible builds also let anyone verify that a binary matches its source, which defends against tampered build systems.
2. **Build systems are dependency-graph engines.** Make (Feldman, 1979) introduced the model: targets, their dependencies and the command to rebuild them. The build tool walks the directed acyclic graph in [topological order](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md), rebuilding only what is out of date and running independent steps in parallel. Correct incremental builds require that every dependency is declared; an undeclared one gives stale or non-deterministic results.
3. **Integrate continuously to keep merges small.** The longer changes stay apart, the more they conflict, and the harder the integration ("merge hell"). CI makes integration a daily non-event: every commit to the main line is built and tested, and a broken main line is fixed or reverted at once, because everyone builds on it.
4. **Build once, promote the same artifact.** The binary or container image tested in staging must be the one deployed to production, with environment differences supplied as configuration. Rebuilding per environment risks shipping something different from what was tested.
5. **Separate deploying from releasing.** Deploying puts new code on servers; releasing exposes it to users. Feature flags let unfinished or risky code ship dark and be turned on gradually or off instantly without a new deploy. This decouples engineering cadence from product decisions and makes rollback of behaviour a configuration change.
6. **Roll out progressively and watch.** A canary release sends a small fraction of traffic (say 1%) to the new version, compares its error rate and latency with the old version, and proceeds or rolls back automatically. Blue-green deployment keeps the old environment ready for instant switch-back. These limit the blast radius of a bad change to a few users for a few minutes.
7. **Delivery performance is measurable, and speed and stability go together.** *Accelerate* (Forsgren, Humble and Kim, 2018) identified four key metrics: deployment frequency, lead time for changes, change failure rate, and time to restore service. High performers led on all four at once; the practices that make deployment fast (automation, small batches, trunk-based development) also make it safe.
8. **The pipeline is part of the attack surface.** Build systems and dependencies run with access to production artifacts. Compromising them, as in the 2020 SolarWinds attack, poisons every downstream user. Pinned and verified dependencies, signed artifacts and provenance records (for example the Supply-chain Levels for Software Artifacts (SLSA) framework) defend the supply chain.

## Key concepts

| Term | Meaning |
|---|---|
| Continuous integration (CI) | Merging all changes to a shared main line frequently, each verified by an automated build and tests |
| Continuous delivery (CD) | Keeping every passing change in a releasable state |
| Continuous deployment | Automatically releasing every change that passes the pipeline |
| Hermetic build | A build that depends only on declared inputs, not on the host machine's state |
| Reproducible build | A build that produces bit-identical outputs from the same inputs |
| Artifact | A versioned build output: binary, package or container image |
| Feature flag | A run-time switch that turns code paths on or off without redeploying |
| Canary release | Rolling a change out to a small subset of traffic first and comparing health metrics |
| Lead time for changes | Time from commit to running in production |

## How it fits

- **Below:** builds orchestrate compilers and [linkers](../../06-programming-languages/04-runtime-systems/linking-and-loading.md); deployment targets [containers](../../07-operating-systems/07-virtualization/containers.md) and [cloud](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) infrastructure. Caching artifacts by input hash relies on [hash functions](../../11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md), and the build graph is scheduled like any [task-parallel](../../10-distributed-and-parallel-computing/01-parallel-computing/data-and-task-parallelism.md) computation.
- **Above:** progressive rollout is a main tool of [reliability engineering](reliability-engineering.md); canary analysis relies on [observability](observability.md).
- **Siblings:** reliability engineering decides how fast the pipeline may ship (error budgets); observability decides whether a rollout proceeds. The pipeline executes the [tests](../03-quality/testing.md) and [static checks](../03-quality/static-analysis-and-code-review.md) from the quality area.

## Common misconceptions

- **"CI means having a CI server."** CI is a practice: integrating to the main line at least daily and keeping it green. A server running tests on long-lived branches is not CI.
- **"Deploying often is reckless."** Each small deploy carries little change, so it is easier to test, observe and reverse. Rare, large releases are the risky ones.
- **"Rollback is always possible."** Code can be rolled back; data changes and external side effects often cannot. Schema migrations must be designed to be backward compatible (expand, migrate, then contract).

## Go deeper

- Jez Humble and David Farley, *Continuous Delivery* (2010): the deployment pipeline in full.
- Nicole Forsgren, Jez Humble and Gene Kim, *Accelerate* (2018): the four key metrics and the evidence behind them.
- Titus Winters, Tom Manshreck and Hyrum Wright, *Software Engineering at Google* (2020): chapters on build systems, continuous integration and continuous delivery.
