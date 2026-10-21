# Streaming and Online Algorithms

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Advanced Topics](README.md)
> **Builds on:** [Randomized Algorithms](../03-design-paradigms/randomized-algorithms.md), [Hash Tables](../02-fundamental-data-structures/hash-tables.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Entropy and Information](../../02-theory-of-computation/01-information-theory/entropy-and-information.md)
> **Enables:** [Page Replacement](../../07-operating-systems/04-memory-management/page-replacement.md), [Batch and Stream Processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md), [Content Delivery and Caching](../../08-networking/05-application-layer/content-delivery-and-caching.md), [Observability](../../12-software-engineering/04-operations/observability.md)

## Essence

Classical algorithms see their whole input before deciding anything. Two important settings forbid this. In the **online** setting, requests arrive one at a time and each must be answered irrevocably before the next is seen: which page to evict from a cache, which server to assign a job to. Online algorithms are judged by their *competitive ratio*, the worst-case ratio of their cost to that of an optimal algorithm that knows the future. In the **streaming** setting, data passes by once and is too large to store; the algorithm keeps a small *sketch* (often polylogarithmic in size) and answers approximate queries (how many distinct items, which items are frequent, what is the median) with error ε and failure probability δ. Both trade perfect information for guarantees that hold under ignorance.

## Core tenets

1. **Competitive analysis compares against a clairvoyant optimum.** An online algorithm is c-competitive if, for every request sequence σ, ALG(σ) ≤ c · OPT(σ) + b for a constant b, where OPT knows σ in advance. This is a worst-case game against an adversary who chooses σ knowing the algorithm. It answers "how much does not knowing the future cost?" with a number.

2. **Ski rental is the archetype: hedge between renting and buying.** Renting costs 1 per day, buying costs B. Not knowing how many days you will ski, rent for B − 1 days then buy. If you stop before buying you paid the optimum; otherwise you paid at most 2B − 1 versus the optimum B: a ratio below 2, which is the best any deterministic strategy can do. The same reasoning decides when to spin versus block on a lock, and when to power down an idle disk.

3. **Paging: LRU is k-competitive, and nothing deterministic does better.** With a cache of k pages, Least Recently Used (LRU) and First-In First-Out (FIFO) incur at most k times the misses of Belady's optimal offline policy (evict the page used farthest in the future), and Sleator and Tarjan (1985) showed no deterministic algorithm beats k. Randomized marking algorithms achieve O(log k) against an oblivious adversary. In practice LRU does much better than k times optimal because real access streams have locality, which competitive analysis ignores; this gap motivated analysis with resource augmentation and locality models.

4. **Streaming lower bounds come from information.** Answering some queries exactly requires remembering nearly the whole stream. Counting distinct elements exactly needs Ω(n) bits in the worst case, as does exact frequency of every item. The way out is approximation plus randomness: estimate within a factor 1 ± ε with probability 1 − δ, which needs only O((1/ε²) log(1/δ)) counters for many problems.

5. **Hashing gives tiny summaries of huge sets.** To count distinct elements, hash each item to a uniform value and track the maximum number of leading zeros seen: with d distinct items you expect to see about log₂ d leading zeros. HyperLogLog (Flajolet et al., 2007) averages many such registers and estimates cardinalities in the billions with about 2% error using roughly 1.5 KB. A Bloom filter answers "have I seen x?" with no false negatives and a tunable false-positive rate (about 1% at 9.6 bits per element with 7 hash functions).

6. **Frequency sketches find heavy hitters in small space.** The Count-Min sketch (Cormode and Muthukrishnan, 2005) keeps d rows of w counters; each item increments one counter per row via independent hashes, and its estimate is the minimum. With w = ⌈e/ε⌉ and d = ⌈ln(1/δ)⌉ the estimate overcounts by at most εN with probability 1 − δ, where N is the stream length. The deterministic Misra–Gries algorithm finds all items with frequency above N/k using k − 1 counters.

7. **Sampling and quantile sketches summarise distributions.** Reservoir sampling keeps a uniform random sample of k items from a stream of unknown length in O(k) memory: keep item i with probability k/i, replacing a random current member. Quantile sketches (Greenwald–Khanna, t-digest, KLL) answer "what is the 99th percentile latency?" within rank error ε using space roughly O((1/ε) log(εN)) or better, which is why monitoring systems can report tail latency across billions of requests.

8. **Sketches are mergeable, which makes them distributed.** Many sketches (HyperLogLog, Count-Min, KLL) can be combined: merge sketches from 1,000 servers and you get the sketch of the union. This lets distributed systems compute approximate global statistics in one round of communication, a key property for stream processors and observability pipelines.

## Key concepts

| Term | Meaning |
|---|---|
| Online algorithm | Makes irrevocable decisions on each request without knowledge of future requests |
| Competitive ratio | Worst-case ratio of online cost to optimal offline cost |
| Belady's algorithm (OPT) | Offline paging that evicts the page used farthest in the future |
| Streaming algorithm | One pass over data with memory much smaller than the input |
| Sketch | Compact randomized summary supporting approximate queries |
| (ε, δ)-approximation | Error at most ε with probability at least 1 − δ |
| HyperLogLog | Distinct-count sketch based on leading zeros of hashes |
| Count-Min sketch | Frequency sketch using a grid of hashed counters, taking the minimum |
| Reservoir sampling | Uniform sample of fixed size from a stream of unknown length |

## How it fits

- **Below:** analysis rests on [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) and [universal hashing](../02-fundamental-data-structures/hash-tables.md); space lower bounds come from [information theory](../../02-theory-of-computation/01-information-theory/entropy-and-information.md); paging models the [cache hierarchy](../../04-computer-architecture/03-memory-hierarchy/cache-design.md).
- **Above:** [page replacement](../../07-operating-systems/04-memory-management/page-replacement.md) in operating systems, [CDN and web caching](../../08-networking/05-application-layer/content-delivery-and-caching.md), [stream processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md), approximate distinct counts in [databases](../../09-data-management/03-query-processing/query-optimization.md), latency percentiles in [observability](../../12-software-engineering/04-operations/observability.md), Bloom filters in [LSM-trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md), and [network traffic monitoring](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md) for heavy hitters and attacks.
- **Siblings:** competitive ratios parallel [approximation ratios](approximation-algorithms.md) (one measures ignorance of the future, the other intractability); paging connects to [external-memory algorithms](external-memory-and-cache-oblivious.md), which assume an ideal cache close to LRU.

## Common misconceptions

- **"A sketch is just a sample."** Sketches like HyperLogLog and Count-Min are hash-based summaries that see every item; they beat sampling for counts and frequencies.
- **"LRU being k-competitive means it is bad."** The bound is against an adversary; on real workloads with locality, LRU is near-optimal. The point is that no deterministic algorithm can do better in the worst case.
- **"Bloom filters can say an item is absent when it is present."** They never give false negatives (absent deletions); they give occasional false positives.

## Go deeper

- Allan Borodin and Ran El-Yaniv, *Online Computation and Competitive Analysis* (1998): the standard text.
- Daniel D. Sleator and Robert E. Tarjan, "Amortized Efficiency of List Update and Paging Rules" (1985): founded competitive analysis.
- Philippe Flajolet, Éric Fusy, Olivier Gandouet, Frédéric Meunier, "HyperLogLog: the analysis of a near-optimal cardinality estimation algorithm" (2007).
- Graham Cormode and S. Muthukrishnan, "An Improved Data Stream Summary: The Count-Min Sketch and its Applications" (2005).
