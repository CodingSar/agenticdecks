# Probability

> **Layer:** [01 Mathematical Foundations](../README.md) › [Probability and Statistics](README.md)
> **Builds on:** [Sets](../02-sets-relations-functions/sets.md), [Combinatorics](../03-discrete-mathematics/combinatorics.md)
> **Enables:** [Random Variables and Distributions](random-variables-and-distributions.md), [Randomized Algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md), [Entropy and Information](../../02-theory-of-computation/01-information-theory/entropy-and-information.md), [Probabilistic Reasoning](../../13-artificial-intelligence/01-classical-ai/probabilistic-reasoning.md), [Foundations of Modern Cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md)

## Essence

Probability is the mathematics of uncertainty: it assigns numbers between 0 and 1 to events in a way that is consistent, so that degrees of belief or long-run frequencies can be combined by rules. Formally, it is a measure on a set of outcomes (the sample space) that is non-negative, totals 1 and adds up over disjoint events. Computer scientists need it for three reasons. Systems face uncertain inputs (packet loss, disk failure, user arrivals). Algorithms use randomness on purpose, gaining speed or simplicity in exchange for a tiny, controllable chance of error. And learning systems reason from evidence to conclusions, which is exactly what conditional probability and Bayes' rule formalise.

## Core tenets

1. **Three axioms define probability, and everything else follows.** For events *A* (subsets of a sample space Ω): P(A) ≥ 0, P(Ω) = 1, and P(A ∪ B) = P(A) + P(B) when *A* and *B* are disjoint (extended to countable unions). From these come P(not A) = 1 − P(A) and inclusion–exclusion. Kolmogorov's 1933 axiomatisation made probability part of [set](../02-sets-relations-functions/sets.md) and measure theory, which is why events behave like sets.

2. **Conditioning restricts the world to what you know.** P(A | B) = P(A ∩ B) / P(B): among the outcomes where *B* happened, the fraction where *A* also happened. Every update of belief on evidence, every spam filter and every diagnostic test is conditioning. The multiplication rule P(A ∩ B) = P(A | B)·P(B) lets you compute joint probabilities step by step, as in a chain of independent packet transmissions.

3. **Bayes' rule inverts conditioning, and base rates dominate.** P(H | E) = P(E | H)·P(H) / P(E). With a disease prevalence of 1 in 1,000 and a test that is 99% sensitive and 99% specific, a positive result means only about a 9% chance of disease, because false positives from the 999 healthy people swamp the true positives. The same base-rate effect makes intrusion detection systems with low false-positive rates still drown analysts in false alarms when attacks are rare.

4. **Independence is a strong assumption that makes computation easy and is often false.** *A* and *B* are independent when P(A ∩ B) = P(A)·P(B). It lets probabilities multiply: if each of 1,000 servers fails independently with probability 0.001 per day, the chance none fails is about e^(−1) ≈ 0.37. But correlated failures (shared power, shared software bugs, shared network switches) break this, which is why [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md) worries about common-mode failure more than about individual component rates.

5. **The union bound needs no independence.** P(A₁ ∪ … ∪ Aₙ) ≤ Σ P(Aᵢ). It is often loose but always valid, so it is the default tool for showing that *nothing* goes wrong: if each of *n* bad events has probability at most 1/n², all of them together have probability at most 1/n. Analyses of hashing, randomized algorithms and cryptographic security reductions lean on it constantly.

6. **Randomness can defeat adversaries and simplify algorithms.** A deterministic algorithm has worst-case inputs an adversary can choose; a randomized one has only unlucky coin flips, which no input can force. Randomized quicksort is O(n log n) expected on every input; universal hashing bounds expected collisions for every key set; Miller–Rabin primality testing errs with probability at most 4^(−k) after *k* rounds. Repeating a randomized algorithm drives error probability down exponentially.

7. **Probability is how security is defined.** Modern cryptography says a scheme is secure if every efficient attacker succeeds with only *negligible* probability, smaller than any inverse polynomial in the key length. Brute-forcing a 128-bit key succeeds with probability 2^(−128) per guess. Good randomness is a security requirement: predictable random number generators have broken real systems, because a key that is not uniformly random has fewer effective bits than its length.

8. **Intuition about probability is unreliable, so compute.** The birthday paradox (23 people give a better-than-even chance of a shared birthday), the base-rate fallacy and the gambler's fallacy (independent trials do not "balance out") all fool experienced engineers. Writing down the sample space and the events, then applying the rules, prevents most errors.

## Key concepts

| Term | Meaning |
|---|---|
| Sample space (Ω) | The set of all possible outcomes |
| Event | A subset of the sample space |
| Probability measure | Function from events to [0, 1] satisfying the axioms |
| Conditional probability | P(A ∣ B) = P(A ∩ B) / P(B) |
| Independence | P(A ∩ B) = P(A)·P(B) |
| Bayes' rule | P(H ∣ E) = P(E ∣ H)·P(H) / P(E) |
| Prior / posterior | Belief before / after seeing evidence |
| Union bound | Probability of any of several events is at most the sum |
| Law of total probability | P(A) = Σ P(A ∣ Bᵢ)·P(Bᵢ) over a partition Bᵢ |
| Negligible | Smaller than 1/poly(n) for every polynomial; cryptographic "never" |

## How it fits

- **Below:** Events are [sets](../02-sets-relations-functions/sets.md); finite, equally likely cases reduce probability to [combinatorics](../03-discrete-mathematics/combinatorics.md).
- **Above:** [Information theory](../../02-theory-of-computation/01-information-theory/entropy-and-information.md) defines entropy from probabilities. [Randomized algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md), [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) and [streaming sketches](../../05-algorithms-and-data-structures/07-advanced-topics/streaming-and-online-algorithms.md) are analysed with it. [Cryptographic security](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md) is defined by it. [Probabilistic reasoning](../../13-artificial-intelligence/01-classical-ai/probabilistic-reasoning.md) and [machine learning](../../13-artificial-intelligence/02-machine-learning-foundations/supervised-learning.md) are built on Bayes' rule and likelihood. Randomised backoff in [Ethernet and wireless media access](../../08-networking/02-link-layer/media-access-and-ethernet.md) and leader election timeouts in [consensus](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md) use randomness to break symmetry.
- **Siblings:** [Random variables](random-variables-and-distributions.md) attach numbers to outcomes so you can compute averages and tails; [statistical inference](statistical-inference.md) runs probability backwards, from observed data to unknown parameters.

## Common misconceptions

- **"A 99%-accurate test means a positive is 99% likely to be right."** That depends on the base rate; for rare conditions most positives are false.
- **"Independent failures are the norm."** Real failures correlate through shared dependencies; multiplying small probabilities can underestimate risk by orders of magnitude.
- **"Randomized algorithms are unreliable."** Their error probability can be pushed below the probability of a hardware fault by a few repetitions.

## Go deeper

- Joseph Blitzstein and Jessica Hwang, *Introduction to Probability* (2nd ed., 2019): clear, intuition-first, free online.
- Michael Mitzenmacher and Eli Upfal, *Probability and Computing* (2nd ed., 2017): probability for randomized algorithms and data structures.
- William Feller, *An Introduction to Probability Theory and Its Applications, Vol. 1* (3rd ed., 1968): the classic.
