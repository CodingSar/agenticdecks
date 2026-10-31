# Information Theory

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Information, Codes and Cryptography](README.md)
> **Builds on:** [Counting Principles and Binomial Coefficients](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md), [The Probabilistic Method](../../03-combinatorics-and-graph-theory/03-discrete-probability/the-probabilistic-method.md), [Estimates and Inequalities](../../06-real-analysis/01-limits-and-convergence/estimates-and-inequalities.md), [The Law of Large Numbers](../../11-probability-and-statistics/02-limit-theorems/the-law-of-large-numbers.md)
> **Enables:** [Error-Correcting Codes](error-correcting-codes.md), [Cryptography](cryptography.md), [Statistical Learning Theory](../06-data-and-learning/statistical-learning-theory.md), [Entropy and Information (CS)](../../../cs-first-principles/02-theory-of-computation/01-information-theory/entropy-and-information.md)

## Essence

Claude Shannon's paper "A Mathematical Theory of Communication" (1948) created a subject complete with its main theorems. It measures information by entropy, the average number of bits needed to describe the outcome of a random source, and proves two limits. The source coding theorem says a source can be compressed to its entropy and no further. The noisy-channel coding theorem says every channel has a capacity C: below C, messages can be sent with error probability as small as desired; above it, they cannot. Both proofs are probabilistic and both rest on one observation, that long random sequences are almost all typical.

## Core tenets

1. **Entropy measures uncertainty in bits.** For a random variable X taking values with probabilities p₁, …, pₙ,

   ```
   H(X) = − p₁ log₂ p₁ − ⋯ − pₙ log₂ pₙ
   ```

   It is 0 for a certain outcome, log₂ n for a uniform one, and in between otherwise: a coin landing heads with probability 0.11 has entropy about 0.5 bits. Shannon showed that this formula is, up to the choice of base, the only measure that is continuous, increasing in n for uniform distributions, and additive when a choice is split into stages. Concavity of the logarithm, through Jensen's inequality, gives the basic facts: H(X) ≤ log₂ n, and conditioning cannot increase entropy.

2. **Almost all long sequences are typical.** If X₁, …, Xₙ are independent copies of X, the law of large numbers applied to −log₂ p(Xᵢ) shows that with probability tending to 1 the sequence has probability close to 2^(−nH). There are therefore about 2^(nH) typical sequences, which together carry nearly all the probability, out of 2^(n log₂ ∣A∣) possible sequences over the alphabet A. This asymptotic equipartition property is the counting fact behind both coding theorems, and for a biased coin it is the estimate of the binomial coefficient C(n, pn) ≈ 2^(nH(p)).

3. **A source can be compressed to its entropy and no further.** Indexing the typical sequences takes about nH bits, and fewer bits cannot distinguish enough sequences to succeed with high probability. For symbol-by-symbol codes, lengths ℓᵢ of a prefix code satisfy the Kraft inequality ∑ 2^(−ℓᵢ) ≤ 1, from which the average length L of the best one satisfies H ≤ L < H + 1. David Huffman (1952) found the optimal code by repeatedly merging the two least likely symbols, and Abraham Lempel and Jacob Ziv (1977, 1978) gave universal methods that approach the entropy rate without knowing the source statistics.

4. **Mutual information measures what one variable reveals about another.** I(X; Y) = H(X) − H(X ∣ Y) is symmetric and nonnegative. It is a special case of the Kullback–Leibler divergence D(p ∥ q) = ∑ p log₂(p/q) (Solomon Kullback and Richard Leibler, 1951), which is nonnegative by Jensen's inequality and zero only when p = q. The data processing inequality says that if Z is computed from Y alone, then I(X; Z) ≤ I(X; Y): no manipulation of data creates information about its source.

5. **Every channel has a capacity, and it is achievable.** A memoryless channel is a conditional distribution p(y ∣ x), and its capacity is C = max I(X; Y) over input distributions. For the binary symmetric channel, which flips each bit with probability p, C = 1 − H(p), so at p = 0.11 half of each transmitted bit survives; for the erasure channel, which loses each bit with probability ε, C = 1 − ε; for the additive white Gaussian noise channel, C = ½ log₂(1 + P/N) bits per use, where P/N is the ratio of signal power to noise power. The noisy-channel coding theorem says that for every rate R < C and every δ > 0, long enough codes with rate R have error probability below δ, and for R > C the error probability is bounded away from 0.

6. **The proof chooses the code at random.** Shannon picked 2^(nR) codewords independently at random and decoded by looking for the unique codeword jointly typical with the received word. Averaged over all codebooks the error probability tends to 0 when R < C, so some codebook is good: the probabilistic method, decades before it had that name. The converse uses Fano's inequality, which bounds the error probability below in terms of the information lost. It proves good codes exist without exhibiting one; practical codes near capacity arrived in the 1990s.

7. **The theory extends to distortion and networks, not all of it solved.** Rate–distortion theory (Shannon, 1959) gives the fewest bits per symbol needed to reproduce a source within a given average distortion, the limit for lossy compression of audio and images. For networks of many senders and receivers, single-letter formulas are known only in special cases; the capacity of the general relay channel and of the general two-receiver broadcast channel is open as of 2026.

## Key concepts

| Term | Meaning |
|---|---|
| Entropy | The average information of a source, −∑ p log₂ p bits |
| Typical set | About 2^(nH) sequences carrying almost all the probability |
| Prefix code | A code in which no codeword begins another, so decoding is instantaneous |
| Mutual information | I(X; Y) = H(X) − H(X ∣ Y), the information Y gives about X |
| Kullback–Leibler divergence | D(p ∥ q), the expected log-likelihood ratio; nonnegative |
| Channel capacity | The largest rate of reliable communication, max I(X; Y) |

## How it fits

- **Below:** typical sequences come from the [law of large numbers](../../11-probability-and-statistics/02-limit-theorems/the-law-of-large-numbers.md); entropy estimates [binomial coefficients](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md); random coding is [the probabilistic method](../../03-combinatorics-and-graph-theory/03-discrete-probability/the-probabilistic-method.md); nonnegativity results are Jensen's inequality from [estimates and inequalities](../../06-real-analysis/01-limits-and-convergence/estimates-and-inequalities.md).
- **Above:** [statistical learning theory](../06-data-and-learning/statistical-learning-theory.md) uses Kullback–Leibler divergence and mutual information to bound what can be learned; cross-entropy is the standard loss in [deep learning](../06-data-and-learning/the-mathematics-of-deep-learning.md); entropy is also an invariant in [ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md); the computer-science treatment is in [entropy and information](../../../cs-first-principles/02-theory-of-computation/01-information-theory/entropy-and-information.md) and [source coding](../../../cs-first-principles/02-theory-of-computation/01-information-theory/source-coding-and-compression.md).
- **Siblings:** [error-correcting codes](error-correcting-codes.md) construct the codes whose existence the channel coding theorem promises; [cryptography](cryptography.md) began with Shannon's information-theoretic definition of perfect secrecy.

## Common misconceptions

- **"Information means meaning"**: entropy measures unpredictability; a random string has maximal entropy and no meaning, and Shannon set semantics aside explicitly.
- **"Noise limits accuracy, so reliable communication needs a clean channel"**: below capacity, coding makes the error probability as small as desired at a fixed positive rate; noise limits the rate, not the reliability.

## Go deeper

- Claude E. Shannon, "A Mathematical Theory of Communication", *Bell System Technical Journal* (1948): still readable, the source of almost everything here.
- Thomas M. Cover and Joy A. Thomas, *Elements of Information Theory* (2nd edition, 2006): the standard text.
- David J. C. MacKay, *Information Theory, Inference, and Learning Algorithms* (2003): information theory joined to inference and modern codes, free online.
