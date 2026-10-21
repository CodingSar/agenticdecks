# Source Coding and Compression

> **Layer:** [02 Theory of Computation](../README.md) › [Information Theory](README.md)
> **Builds on:** [Entropy and Information](entropy-and-information.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md)
> **Enables:** [Digital Media and Compression](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md), [Character Encoding](../../03-digital-logic/01-number-representation/character-encoding.md), [Storage Layouts](../../09-data-management/02-storage-and-indexing/storage-layouts.md)

## Essence

Source coding is the problem of representing the output of a source in as few bits as possible. Shannon's source coding theorem answers it exactly: a source with entropy H bits per symbol can be losslessly compressed to any rate above H bits per symbol and to no rate below it. Compression works by giving short codewords to likely symbols and long ones to unlikely symbols, so that the *average* length falls toward the entropy. Every practical compressor (Huffman, arithmetic coding, Lempel–Ziv, modern context-mixing and neural compressors) is a way of building a good probability model and turning it into a code. When some loss is acceptable, rate–distortion theory gives the matching limit.

## Core tenets

1. **Shannon's source coding theorem (lossless).** For a source emitting independent, identically distributed (i.i.d.) symbols with entropy H, and any ε > 0, blocks of n symbols can be encoded with an average of at most H + ε bits per symbol and decoded with error probability tending to 0 as n → ∞. Conversely, any scheme using fewer than H − ε bits per symbol fails with probability tending to 1. The same holds for stationary ergodic sources with the entropy rate in place of H.

2. **Why: the typical set.** By the law of large numbers, a long sequence almost surely has −(1/n) log₂ p(x₁…xₙ) ≈ H. So almost all probability lies on about 2^(nH) "typical" sequences, each of probability about 2^(−nH). Indexing just those takes nH bits. Everything else is so improbable it can be given a long escape code at negligible average cost. Below nH bits there are too few labels to cover the typical set.

3. **Variable-length codes must be uniquely decodable, and prefix codes lose nothing.** The Kraft–McMillan inequality Σ 2^(−ℓᵢ) ≤ 1 constrains codeword lengths ℓᵢ for any uniquely decodable code, and any lengths satisfying it can be realised by a prefix code (no codeword is a prefix of another), which decodes instantly. Choosing ℓᵢ = ⌈−log₂ pᵢ⌉ satisfies Kraft and gives average length below H + 1.

4. **Huffman coding is optimal symbol by symbol; arithmetic coding removes the rounding loss.** Huffman's greedy merge of the two least likely symbols gives the minimum average length among prefix codes for a known distribution, but it spends at least 1 bit per symbol, which wastes a lot when one symbol has probability 0.99. Arithmetic coding (and its fast cousin, asymmetric numeral systems) encodes a whole message as one subinterval of [0, 1) of width equal to its probability, getting within about 2 bits of −log₂ p(message) in total.

5. **Compression is prediction.** A coder spends −log₂ q(x) bits where q is its model's probability, so its average rate is the cross-entropy H(p, q) = H(p) + D(p ‖ q). Better models directly mean smaller files. This is why general-purpose compressors use context (previous bytes) to sharpen predictions, and why a good language model is also a good text compressor.

6. **Universal compressors learn the model as they go.** Lempel–Ziv (LZ77, LZ78) replaces repeated substrings with pointers to earlier occurrences. Without knowing the source statistics, its rate converges to the entropy rate of any stationary ergodic source. That universality is why LZ variants (DEFLATE in gzip and PNG, LZ4, Zstandard) dominate practical lossless compression.

7. **No lossless compressor shrinks every input.** There are 2ⁿ strings of length n but only 2ⁿ − 1 strings shorter than n, so by the pigeonhole principle some input must stay the same length or grow. Compressors win only on inputs that their model makes likely. Random or already-compressed data does not compress.

8. **Lossy compression trades bits for distortion, with its own limit.** Rate–distortion theory defines R(D), the minimum bits per symbol to reproduce a source within average distortion D, as the minimum mutual information I(X; X̂) over reproductions meeting the distortion budget. Practical codecs (JPEG, MP3, video codecs) approach it by transforming the signal (cosine or wavelet transforms concentrate energy in few coefficients), quantising coarsely where human perception is insensitive, then entropy-coding the result.

## Key concepts

| Term | Meaning |
|---|---|
| Rate | Average bits per source symbol produced by a code |
| Typical set | The ~2^(nH) sequences carrying almost all probability for long blocks |
| Prefix code | No codeword is a prefix of another, so decoding needs no lookahead |
| Kraft inequality | Σ 2^(−ℓᵢ) ≤ 1: the budget that codeword lengths must respect |
| Huffman code | Optimal prefix code for a known symbol distribution |
| Arithmetic coding | Encodes a message as an interval; near-optimal for any model |
| Lempel–Ziv | Dictionary method using back-references; universal |
| Rate–distortion function R(D) | Least rate achieving expected distortion at most D |

## How it fits

- **Below:** It takes entropy and the law of large numbers from [entropy](entropy-and-information.md) and [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), and the pigeonhole argument from [combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md). The physical signal is first turned into symbols by [sampling and quantisation](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md).
- **Above:** Variable-length encodings such as UTF-8 are frequency-aware codes ([character encoding](../../03-digital-logic/01-number-representation/character-encoding.md)). Columnar databases compress with dictionary and run-length coding ([storage layouts](../../09-data-management/02-storage-and-indexing/storage-layouts.md)). Web traffic is compressed in transit ([HTTP](../../08-networking/05-application-layer/http-and-the-web.md)), and media codecs are applied rate–distortion theory ([digital media](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md)). [Large language models](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md) are trained by minimising cross-entropy, which is code length.
- **Siblings:** Source coding *removes* redundancy to save bits; [channel coding](channel-capacity-and-error-correction.md) *adds* structured redundancy to survive noise. Shannon's separation theorem says that, for point-to-point links, doing the two separately loses nothing in the limit.

## Common misconceptions

- **"A clever enough algorithm can compress anything."** Counting forbids it: no lossless map can shrink all inputs, and the average over a source cannot beat its entropy.
- **"Compressing twice compresses more."** Good compressor output is close to random under the compressor's own model; a second pass finds no further structure and usually adds overhead.
- **"Huffman is optimal, full stop."** It is optimal among codes assigning a whole number of bits to each symbol. Arithmetic coding and block coding beat it when probabilities are skewed.

## Go deeper

- Thomas M. Cover and Joy A. Thomas, *Elements of Information Theory* (2nd ed., 2006), chapters 3, 5, 10 and 13: typical sets, codes, rate–distortion and universal coding.
- David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes" (1952): the original two-page construction.
- Jacob Ziv and Abraham Lempel, "A Universal Algorithm for Sequential Data Compression" (1977): the LZ77 paper.
- Khalid Sayood, *Introduction to Data Compression* (5th ed., 2017): practical lossless and lossy techniques.
