# Entropy and Information

> **Layer:** [02 Theory of Computation](../README.md) › [Information Theory](README.md)
> **Builds on:** [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Random Variables and Distributions](../../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md)
> **Enables:** [Source Coding and Compression](source-coding-and-compression.md), [Channel Capacity and Error Correction](channel-capacity-and-error-correction.md), [Unsupervised Learning](../../13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md)

## Essence

Information theory measures *how much uncertainty a message removes*, independent of what the message means. Claude Shannon's 1948 insight was that a source of messages is best modelled as a random variable, and that the right measure of its information content is its entropy, H(X) = −Σ p(x) log₂ p(x) bits. Entropy is the average number of yes/no questions an optimal questioner needs to identify an outcome. It is not a convention but a theorem: it is the unique measure (up to the choice of logarithm base) that is continuous, grows with the number of equally likely outcomes, and adds up correctly when a choice is split into stages. Every later result about compression, transmission and learning is stated in terms of entropy and its relatives.

## Core tenets

1. **Information is surprise, measured on a log scale.** An outcome of probability p carries −log₂ p bits of "self-information". The log makes information from independent events add: two independent fair coin flips have probability 1/4 and carry 2 bits, exactly 1 + 1. Rare events are informative; a certain event (p = 1) tells you nothing.

2. **Entropy is the average surprise of a source.** H(X) = E[−log₂ p(X)]. A fair coin has H = 1 bit; a coin that lands heads 99% of the time has H ≈ 0.08 bits. Entropy is maximised by the uniform distribution (H = log₂ n for n outcomes) and is zero only when one outcome is certain.

3. **Entropy is the floor for lossless description.** No uniquely decodable code can have an average length below H(X) bits per symbol, and codes exist within 1 bit of it. That is why entropy is the currency of [compression](source-coding-and-compression.md): it is the irreducible part of the data once all predictable structure is removed.

4. **Conditioning never increases entropy on average.** H(X | Y) ≤ H(X), with equality exactly when X and Y are independent. Knowing something related can only help (on average; a particular observation can increase uncertainty). The chain rule H(X, Y) = H(X) + H(Y | X) says the cost of describing a pair is the cost of the first plus the remaining surprise of the second.

5. **Mutual information measures shared uncertainty.** I(X; Y) = H(X) − H(X | Y) = H(Y) − H(Y | X) is symmetric and non-negative. It is how many bits Y tells you about X. [Channel capacity](channel-capacity-and-error-correction.md) is the maximum mutual information between a channel's input and output; feature selection and clustering in machine learning often maximise it.

6. **Relative entropy measures the cost of a wrong model.** The Kullback–Leibler (KL) divergence D(p ‖ q) = Σ p(x) log₂ (p(x)/q(x)) is the expected number of extra bits you pay if you code data from p with a code optimised for q. It is ≥ 0 (Gibbs' inequality) and zero only when p = q, but it is not symmetric, so it is not a distance. Cross-entropy H(p, q) = H(p) + D(p ‖ q) is the standard loss function for classifiers and language models: minimising it fits q to p.

7. **Processing cannot create information.** The data-processing inequality says that if X → Y → Z form a Markov chain (Z depends on X only through Y), then I(X; Z) ≤ I(X; Y). No computation on Y, however clever, recovers information about X that Y did not already carry. This bounds what any decoder, estimator or neural network can extract.

8. **Shannon entropy is not the whole story for individual strings.** Kolmogorov complexity K(s), the length of the shortest program that prints s, measures the information in one particular string. For strings drawn from a computable source, the expected K is within a constant of the source entropy, which ties information theory to [computability](../03-computability/README.md). But K itself is uncomputable, a consequence of the [halting problem](../03-computability/halting-problem-and-undecidability.md).

## Key concepts

| Term | Meaning |
|---|---|
| Self-information | −log₂ p(x): the surprise of a single outcome, in bits |
| Entropy H(X) | Expected self-information; average bits needed to describe X |
| Joint entropy H(X, Y) | Entropy of the pair, treated as one random variable |
| Conditional entropy H(X \| Y) | Remaining uncertainty in X after learning Y |
| Mutual information I(X; Y) | Reduction in uncertainty of X from knowing Y |
| KL divergence D(p ‖ q) | Extra bits paid for coding p-data with a q-code; asymmetric, ≥ 0 |
| Cross-entropy H(p, q) | Average code length for p-data under a q-code: H(p) + D(p ‖ q) |
| Entropy rate | Limit of H(X₁…Xₙ)/n for a source with memory, such as English text |
| Kolmogorov complexity | Length of the shortest program that outputs a given string |

## How it fits

- **Below:** It rests entirely on [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md): random variables, expectations, independence and conditional distributions. Its inequalities come from convexity (Jensen's inequality), a piece of [continuous mathematics](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md).
- **Above:** Entropy sets the limits for [compression of media](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md), the capacity of [links](../../08-networking/02-link-layer/encoding-and-framing.md), the key lengths and randomness requirements of [cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md), and the loss functions of [machine learning](../../13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md). Physically, Landauer's principle links erasing one bit to a minimum heat cost of kT ln 2 ([thermodynamics](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md)).
- **Siblings:** This leaf defines the measures. [Source coding](source-coding-and-compression.md) shows entropy is achievable as a compression rate; [channel coding](channel-capacity-and-error-correction.md) shows mutual information is achievable as a transmission rate.

## Common misconceptions

- **"Entropy measures meaning or importance."** It measures unpredictability under a probability model. A random password has high entropy and no meaning; a crucial "yes" from a near-certain source carries almost no information.
- **"A file has an entropy."** Entropy belongs to a probability distribution, not a single string. A file's compressibility depends on the model you assume for its source; the model-free notion is Kolmogorov complexity, which cannot be computed.
- **"KL divergence is a distance."** It is asymmetric and fails the triangle inequality. D(p ‖ q) and D(q ‖ p) can differ wildly, which is why choosing which direction to minimise matters in variational inference.

## Go deeper

- Claude E. Shannon, "A Mathematical Theory of Communication" (1948): the founding paper, still readable.
- Thomas M. Cover and Joy A. Thomas, *Elements of Information Theory* (2nd ed., 2006): the standard rigorous text.
