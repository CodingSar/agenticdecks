# Observability

> **Layer:** [12 Software Engineering](../README.md) › [Operations](README.md)
> **Builds on:** [Feedback and control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md), [Time, clocks and ordering](../../10-distributed-and-parallel-computing/02-distributed-foundations/time-clocks-and-ordering.md), [Streaming and online algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/streaming-and-online-algorithms.md), [Debugging](../03-quality/debugging.md)
> **Enables:** [Reliability engineering](reliability-engineering.md), [Build and continuous delivery](build-and-continuous-delivery.md)

## Essence

Observability is the ability to understand what a running system is doing, and why, from the data it emits. The term comes from control theory (Kalman, 1960), where a system is observable if its internal state can be inferred from its outputs. For software, the outputs are telemetry: **metrics** (numbers aggregated over time), **logs** (records of discrete events) and **traces** (the path of one request through many services). Monitoring answers questions you predicted ("is the error rate above 1%?"); observability aims to answer questions you did not predict during an incident ("why are only Android users in one region slow since 14:02?"). Because you cannot add instrumentation to the past, what you can learn about a failure depends on what you chose to record before it.

## Core tenets

1. **Metrics, logs and traces trade detail for cost.** Metrics are cheap and fast to query because they aggregate: a counter costs the same at 10 or 10 million requests per second, but loses individual events. Logs keep each event's detail but cost storage proportional to traffic. Traces keep causal structure across services but are usually sampled. Real systems use all three and link them, for example by putting a trace identifier in every log line.
2. **Measure what users experience, starting with a few signals.** Google's Site Reliability Engineering (SRE) book proposes four golden signals: latency, traffic, errors and saturation. Brendan Gregg's utilisation, saturation and errors (USE) method applies to each resource; the rate, errors and duration (RED) method to each service. These turn an overwhelming space of possible metrics into a short list that catches most problems.
3. **Averages hide the tail; use percentiles.** If 1% of requests take 2 seconds, the mean may look fine while one user in a hundred waits. Latency is reported as percentiles (p50, p99, p99.9). Dean and Barroso ("The Tail at Scale", 2013) showed why the tail dominates at scale: if a page fans out to 100 servers, each slow 1% of the time, about 63% of page loads hit at least one slow server.
4. **Percentiles cannot be averaged; aggregate distributions instead.** The mean of per-server p99s is not the fleet p99. Correct aggregation keeps histograms or mergeable sketches (such as t-digest or High Dynamic Range (HDR) histograms) and computes percentiles from the merged result. This is a [streaming-algorithm](../../05-algorithms-and-data-structures/07-advanced-topics/streaming-and-online-algorithms.md) problem: bounded memory, approximate answers with known error.
5. **Distributed tracing reconstructs causality across services.** Each request gets a trace identifier; each unit of work (span) records its parent, start and duration. Assembling spans shows where time went in a request that touched dozens of services. Google's Dapper (Sigelman et al., 2010) established the design, with low-rate sampling to keep overhead small; OpenTelemetry is the current open standard.
6. **Cardinality is the cost driver.** A metric labelled by status code has a handful of time series; labelled by user identifier it may have millions. Storage and query cost grow with the number of distinct label combinations. High-cardinality detail belongs in logs or wide structured events, where it can be queried, not in metric labels.
7. **Alert on symptoms that need a human, not on every cause.** An alert should mean "users are affected or soon will be, and someone must act". Alerting on service level objective (SLO) burn rate (how fast the error budget is being consumed) catches real problems while ignoring harmless blips. Noisy alerts cause fatigue, and fatigued responders miss the real page.
8. **Timestamps from different machines do not agree exactly.** Clocks drift and are synchronised only to within milliseconds or worse, so ordering events across hosts by wall-clock time can mislead. Traces avoid this by recording parent-child causality explicitly, the same idea as [logical clocks](../../10-distributed-and-parallel-computing/02-distributed-foundations/time-clocks-and-ordering.md).

## Key concepts

| Term | Meaning |
|---|---|
| Telemetry | Data a system emits about its own behaviour |
| Metric | A numeric measurement aggregated over time (counter, gauge, histogram) |
| Structured log | An event record with named fields rather than free text |
| Trace / span | The tree of work done for one request / one timed operation within it |
| Percentile (p99) | The value below which the given fraction of observations fall |
| Tail latency | The latency of the slowest requests (high percentiles) |
| Cardinality | The number of distinct label-value combinations, hence of time series |
| Burn rate | How fast the error budget is being consumed relative to the SLO window |
| Sampling | Recording only a fraction of events or traces to bound cost |

## How it fits

- **Below:** the concept is from [control theory](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md); metric collection is [sampling](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md) of a continuous process, with the same aliasing risks if the interval is too coarse. Aggregation relies on [streaming algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/streaming-and-online-algorithms.md); ordering relies on [clocks and causality](../../10-distributed-and-parallel-computing/02-distributed-foundations/time-clocks-and-ordering.md); storing telemetry at scale is a [log-structured](../../09-data-management/02-storage-and-indexing/lsm-trees.md) and [time-series](../../09-data-management/01-data-models/non-relational-models.md) data problem.
- **Above:** telemetry about user behaviour is personal data, so retention and access are governed by [privacy law](../../15-computing-in-context/law-privacy-and-policy.md).
- **Siblings:** [reliability engineering](reliability-engineering.md) defines the service level indicators (SLIs) that observability measures; [continuous delivery](build-and-continuous-delivery.md) uses it to judge canaries. It is the production form of [debugging](../03-quality/debugging.md).

## Common misconceptions

- **"More data means more observability."** Unstructured, unlinked, unqueried logs at great cost answer nothing. What matters is whether you can ask new questions and get answers quickly.
- **"Average latency is a good health measure."** Averages are dominated by the common case and hide the slow tail that users notice and that fan-out amplifies.
- **"Dashboards are observability."** Dashboards answer predefined questions. Novel failures need the ability to slice raw, high-dimensional data in ways no dashboard anticipated.

## Go deeper

- Betsy Beyer et al. (eds.), *Site Reliability Engineering* (2016): the chapter "Monitoring Distributed Systems" and the four golden signals.
- Benjamin H. Sigelman et al., "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure", Google Technical Report (2010): the design of modern tracing.
- Jeffrey Dean and Luiz André Barroso, "The Tail at Scale", *Communications of the ACM* (2013): why tail latency dominates in fan-out systems.
- Charity Majors, Liz Fong-Jones and George Miranda, *Observability Engineering* (2022): observability as querying wide events.
