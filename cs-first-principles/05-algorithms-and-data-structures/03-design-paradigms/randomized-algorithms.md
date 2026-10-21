# Randomized Algorithms

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Design Paradigms](README.md)
> **Builds on:** [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Random Variables and Distributions](../../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md), [Complexity Classes](../../02-theory-of-computation/04-complexity/complexity-classes.md)
> **Enables:** [Hash Tables](../02-fundamental-data-structures/hash-tables.md), [Searching and Selection](../04-sorting-and-searching/searching-and-selection.md), [Streaming and Online Algorithms](../07-advanced-topics/streaming-and-online-algorithms.md), [Public-Key Cryptography](../../11-security-and-cryptography/02-cryptography/public-key-cryptography.md), [Consensus](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md)

## Essence

A randomized algorithm flips coins as it runs. Its behaviour on a fixed input becomes a random variable, and we analyse expected running time or the probability of error over the algorithm's own random choices, not over a distribution of inputs. This shifts the burden from "hope the inputs are nice" to "no input is bad for most coin flips," which defeats adversaries who know the algorithm but not the coins. Randomization often gives algorithms that are simpler or faster than any known deterministic one: random-pivot quicksort, universal hashing, primality testing, minimum cut, and sketches that summarise huge data in tiny space.

## Core tenets

1. **Randomness moves the average from the input to the algorithm.** Average-case analysis assumes inputs follow some distribution, and fails when they do not (sorted data, adversarial requests). A randomized algorithm guarantees its expected bound for *every* input, because the randomness is under its control. Quicksort with a uniformly random pivot makes about 2n ln n ≈ 1.39 n log₂ n comparisons in expectation on any input.

2. **Las Vegas algorithms are always correct; Monte Carlo algorithms are always fast.** Las Vegas algorithms (randomized quicksort, randomized quickselect) always return the right answer, and only the running time is random. Monte Carlo algorithms (Miller–Rabin primality testing, Karger's min-cut, Bloom filters) run in bounded time but may err with small probability. A Las Vegas algorithm can be turned into Monte Carlo by stopping early; Monte Carlo becomes Las Vegas only if answers can be checked.

3. **Error probability can be driven down exponentially by repetition.** If a one-sided Monte Carlo test errs with probability at most 1/2, running it k times independently errs with probability at most 2⁻ᵏ. Miller–Rabin errs with probability at most 1/4 per round on a composite, so 40 rounds give error below 2⁻⁸⁰, far below the probability of hardware faults. This amplification is why "probably correct" is acceptable in practice.

4. **Concentration bounds turn expectations into guarantees.** Expected time alone allows rare disasters. Markov's inequality, Chebyshev's inequality and especially Chernoff bounds show that sums of independent random variables are tightly concentrated around their mean: the probability of deviating by a constant factor falls exponentially. These bounds prove that randomized quicksort is O(n log n) *with high probability* (probability at least 1 − 1/n^c), not just on average.

5. **Random sampling estimates large quantities cheaply.** To estimate a fraction to within ±ε with confidence 1 − δ needs O(log(1/δ)/ε²) samples, independent of the population size. This underlies sketching, approximate query processing, A/B testing and Monte Carlo integration. Reservoir sampling keeps a uniform sample of k items from a stream of unknown length in O(k) memory.

6. **Randomization breaks symmetry where determinism cannot.** When identical processes must choose a leader or avoid colliding, deterministic rules give identical choices. Random choices break the tie: Ethernet's binary exponential backoff picks a random delay after a collision; randomized consensus protocols sidestep the Fischer–Lynch–Paterson (FLP) impossibility of deterministic consensus in asynchronous systems with one crash failure. Random choice of two servers and picking the less loaded one ("power of two choices") reduces maximum load from Θ(log n / log log n) to Θ(log log n).

7. **Pseudorandomness is what we actually use.** Real programs use Pseudorandom Number Generators (PRNGs): deterministic functions of a seed whose outputs pass statistical tests. That suffices for algorithms such as quicksort. Security needs Cryptographically Secure PRNGs (CSPRNGs) seeded from hardware entropy, because a predictable generator lets an attacker choose bad inputs or guess keys. Whether randomness genuinely adds power (does Bounded-error Probabilistic Polynomial time, BPP, equal P?) is open, but strong evidence suggests derandomization is possible in principle: primality, once known only to be in randomized polynomial time, was shown to be in P by the Agrawal–Kayal–Saxena (AKS) test in 2002.

## Key concepts

| Term | Meaning |
|---|---|
| Las Vegas algorithm | Always correct; running time is a random variable |
| Monte Carlo algorithm | Bounded running time; answer correct with high probability |
| Expected running time | Mean time over the algorithm's coin flips, for the worst input |
| With high probability | Probability at least 1 − 1/n^c for some constant c |
| Chernoff bound | Exponentially small tail bound for sums of independent random variables |
| Amplification | Repeating a randomized test to reduce error probability exponentially |
| BPP | Problems solvable in polynomial time with two-sided error at most 1/3 |
| PRNG / CSPRNG | Deterministic generator of random-looking bits / one unpredictable to adversaries |

## How it fits

- **Below:** analysis rests on [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [random variables](../../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md) and linearity of expectation; the class BPP lives among the [complexity classes](../../02-theory-of-computation/04-complexity/complexity-classes.md); physical entropy sources come from [noise](../../00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md).
- **Above:** [key generation](../../11-security-and-cryptography/02-cryptography/public-key-cryptography.md) uses Miller–Rabin; [Ethernet](../../08-networking/02-link-layer/media-access-and-ethernet.md) uses random backoff; [randomized consensus and leader election](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md) use random timeouts (as Raft does); [stochastic gradient descent](../../13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md) samples mini-batches; [load balancers](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md) use power of two choices.
- **Siblings:** randomization strengthens [divide and conquer](divide-and-conquer.md) (random pivots) and [hash tables](../02-fundamental-data-structures/hash-tables.md) (universal hashing), and powers [streaming sketches](../07-advanced-topics/streaming-and-online-algorithms.md).

## Common misconceptions

- **"Randomized means unreliable."** Las Vegas algorithms are always correct, and Monte Carlo error can be made smaller than the chance of a cosmic-ray bit flip.
- **"Expected time is the same as average-case time."** Expected time holds for every input; average case holds only for an assumed input distribution.
- **"`rand()` is fine for anything."** Ordinary PRNGs are predictable from a few outputs; anything security-relevant needs a CSPRNG.

## Go deeper

- Rajeev Motwani and Prabhakar Raghavan, *Randomized Algorithms* (1995): the standard text.
- Michael Mitzenmacher and Eli Upfal, *Probability and Computing* (2nd ed., 2017): concentration bounds and their algorithmic uses.
- Manindra Agrawal, Neeraj Kayal, Nitin Saxena, "PRIMES is in P" (2004): deterministic primality, a landmark derandomization.
