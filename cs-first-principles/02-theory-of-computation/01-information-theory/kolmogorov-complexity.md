# Kolmogorov Complexity

> **Layer:** [02 Theory of Computation](../README.md) › [Information Theory](README.md)
> **Builds on:** [Entropy and Information](entropy-and-information.md), [Turing Machines](../03-computability/turing-machines.md), [Halting Problem and Undecidability](../03-computability/halting-problem-and-undecidability.md), [Functions and Cardinality](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md)
> **Enables:** [Source Coding and Compression](source-coding-and-compression.md), [Generalization and Bias-Variance](../../13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md), [Foundations of Modern Cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md)

## Essence

Kolmogorov complexity measures the information in a single object, with no probability model: K(x) is the length of the shortest program that prints the string x and halts. A string of a million zeros has tiny complexity (a short loop prints it); a string of a million fair coin flips almost certainly has complexity close to a million bits, because no description shorter than the string itself exists. The idea was found independently by Ray Solomonoff (1964), Andrey Kolmogorov (1965) and Gregory Chaitin (1966–69). It gives precise meaning to "random", "simple" and "compressible" for individual strings, agrees with Shannon entropy on average, and turns out to be uncomputable, which ties information theory to the limits of [computability](../03-computability/README.md).

## Core tenets

1. **Complexity is shortest description length.** Fix a universal machine U (a [universal Turing machine](../03-computability/turing-machines.md), or any general-purpose language). K_U(x) = min{|p| : U(p) = x}. Since a program can contain x literally, K(x) ≤ |x| + c for a constant c. A string is *compressible* when K(x) is much smaller than |x|, which happens exactly when it has a regularity that a program can exploit.

2. **The choice of language matters only up to a constant (invariance theorem).** For any two universal machines U and V there is a constant c, the length of an interpreter for V written for U, such that |K_U(x) − K_V(x)| ≤ c for every x. So K is an objective property of long strings, the way asymptotic cost is a property of an algorithm. For short strings the constant dominates and the number says little.

3. **Most strings are incompressible.** There are 2ⁿ strings of length n but fewer than 2ⁿ⁻ᵏ programs shorter than n − k bits, so fewer than a 2⁻ᵏ fraction of strings can be compressed by k or more bits. At least one string of every length has K(x) ≥ n. This is the pigeonhole argument behind "no compressor shrinks everything" ([source coding](source-coding-and-compression.md)), stated per string. Incompressible strings pass every computable statistical test for randomness (Martin-Löf), so "random" can be defined as "incompressible".

4. **K is uncomputable.** Suppose a program could compute K. Then a short program could search strings in order and print the first x with K(x) ≥ n. That program has length about log₂ n + c, which is less than n for large n, so it would describe x in fewer than n bits: a contradiction (a formal version of the Berry paradox, "the smallest number not definable in under twenty words"). Equivalently, computing K would solve the [halting problem](../03-computability/halting-problem-and-undecidability.md). K can be approximated from above, since every compressor gives an upper bound, but no procedure can certify that a string is incompressible.

5. **Formal systems cannot prove strings complex (Chaitin's incompleteness).** For any consistent, effectively axiomatised theory there is a constant L, roughly the length of the theory's own description, such that the theory cannot prove K(x) > L for any specific x, even though almost all strings satisfy it. This is a quantitative form of [Gödel's incompleteness](../../01-mathematical-foundations/01-logic/predicate-logic.md): a theory cannot certify more information than it contains.

6. **On average, Kolmogorov complexity equals Shannon entropy.** Using self-delimiting (prefix-free) programs, so that lengths obey the Kraft inequality, for any computable distribution P: H(P) ≤ Σ P(x)K(x) ≤ H(P) + K(P) + O(1), where K(P) is the length of a program describing P. For a long sequence from an independent identically distributed source, K(x₁…xₙ)/n approaches the [entropy](entropy-and-information.md) with probability 1. Entropy is the average-case theory over a known distribution; Kolmogorov complexity is the individual-case theory with no distribution assumed. Its chain rule, K(x, y) = K(x) + K(y | x) up to logarithmic terms, mirrors H(X, Y) = H(X) + H(Y | X).

7. **Learning is compression: Occam's razor made precise.** The Minimum Description Length (MDL) principle (Rissanen, 1978) chooses the model M minimising L(M) + L(data | M), the bits to describe the model plus the bits to describe the data given the model. An overfitted model has a short second term but pays heavily in the first, because it memorises noise, and noise is incompressible. Solomonoff's universal prior, which weights each hypothesis by 2^(−program length), is an optimal but uncomputable predictor, the idealised limit of [generalization](../../13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md) arguments. Practical echoes are regularisation and the fact that a language model's training loss is a code length.

8. **Real compressors make the idea usable.** Replacing K with the output length of gzip, bzip2 or a neural compressor gives computable upper bounds. The Normalized Compression Distance compares two files by how much better they compress together than apart, and clusters genomes, languages and malware families without domain features. Pseudorandom generators, by contrast, produce strings with *low* K (a short seed plus the program) that no efficient test can tell from random, which is why [cryptographic](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md) randomness is defined by computational indistinguishability rather than by incompressibility.

## Key concepts

| Term | Meaning |
|---|---|
| K(x) | Length of the shortest program that outputs x and halts |
| Conditional K(x \| y) | Shortest program that outputs x when given y as input |
| Invariance theorem | Different universal languages change K by at most an additive constant |
| Incompressible | K(x) ≥ \|x\|; the algorithmic definition of a random string |
| Prefix-free complexity | Variant using self-delimiting programs; makes code lengths obey Kraft |
| Berry paradox | Self-reference behind the uncomputability of K |
| MDL | Choose the model minimising model bits plus data-given-model bits |
| Solomonoff induction | Prediction with prior 2^(−K); optimal but uncomputable |

## How it fits

- **Below:** Programs and the universal machine come from [Turing machines](../03-computability/turing-machines.md); uncomputability comes from the [halting problem](../03-computability/halting-problem-and-undecidability.md); the incompressibility count is the [cardinality](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md) and pigeonhole argument.
- **Above:** MDL and Occam-style bounds inform [model selection and generalization](../../13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md); the "compression is prediction" view underlies [large language models](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md) as compressors; the contrast between incompressible and pseudorandom strings shapes [cryptographic](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md) definitions. The *incompressibility method* also proves average-case lower bounds for [algorithms](../../05-algorithms-and-data-structures/04-sorting-and-searching/comparison-sorting.md).
- **Siblings:** [Entropy](entropy-and-information.md) is the expected-value counterpart; [source coding](source-coding-and-compression.md) achieves entropy for known or learnable sources, while K is the ideal no compressor can reach in general; [channel capacity](channel-capacity-and-error-correction.md) concerns adding redundancy rather than removing it.

## Common misconceptions

- **"A compressor tells you a file's information content."** It gives an upper bound on K. A file that looks random to gzip may be the output of a ten-line program, such as the digits of π.
- **"K depends on the programming language, so it is arbitrary."** Only by an additive constant, which is negligible for long strings.
- **"High complexity means interesting structure."** Random noise has maximal K and no structure; measures such as logical depth and sophistication try to capture "meaningful" complexity instead.

## Go deeper

- Ming Li and Paul Vitányi, *An Introduction to Kolmogorov Complexity and Its Applications* (4th ed., 2019): the standard reference, including the incompressibility method.
- Thomas M. Cover and Joy A. Thomas, *Elements of Information Theory* (2nd ed., 2006), chapter 14: Kolmogorov complexity alongside entropy.
- Peter Grünwald, *The Minimum Description Length Principle* (2007): MDL as a practical theory of learning.
