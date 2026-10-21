# Attention and Transformers

> **Layer:** [13 Artificial Intelligence](../README.md) › [Deep learning](README.md)
> **Builds on:** [Neural networks and backpropagation](neural-networks-and-backpropagation.md), [Linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md)
> **Enables:** [Large language models](../04-advanced-paradigms/large-language-models.md), [Generative models](../04-advanced-paradigms/generative-models.md), [Computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md)

## Essence

Attention lets every element of a sequence look at every other element and pull in information from the ones that matter, with "what matters" computed from the content itself. It works like a soft dictionary lookup: each position issues a query, compares it with every position's key, and takes a weighted average of their values. The transformer (Vaswani et al., 2017) builds a whole network from attention plus small per-position feed-forward layers, with no recurrence. Because all positions are processed at once, training parallelises across the sequence on Graphics Processing Units (GPUs), which is why transformers scaled where Recurrent Neural Networks (RNNs) could not. The price is cost quadratic in sequence length.

## Core tenets

1. **Attention is a differentiable lookup.** With queries Q, keys K and values V (each a matrix of row vectors, keys of dimension d_k),

   Attention(Q, K, V) = softmax(QKᵀ / √d_k) V

   Each row of QKᵀ scores one query against all keys by dot product; softmax turns scores into weights that sum to 1; the output is the weighted average of values. Unlike a hash-table lookup, which returns one exact match, attention returns a blend, and because every step is differentiable, the network learns what to query for.

2. **Scaling by √d_k keeps softmax trainable.** If query and key components have unit variance, their dot product has variance d_k. Large scores push softmax into a near one-hot regime where gradients vanish. Dividing by √d_k keeps scores near unit variance.

3. **Q, K and V are learned projections of the same input (in self-attention).** For input X, Q = XW_Q, K = XW_K, V = XW_V. Multi-head attention runs h such attentions in parallel with smaller projections and concatenates them, letting different heads specialise (one tracks syntax, another the previous token). Interpretability research has found specific heads that implement copying and pattern completion ("induction heads").

4. **Attention has no notion of order without positional information.** Self-attention is permutation-equivariant: shuffle the inputs and the outputs shuffle identically. Order must be injected, by adding positional encodings to the inputs or, common as of the mid-2020s, by rotating queries and keys by position-dependent angles (Rotary Position Embedding, RoPE) so scores depend on relative distance.

5. **A transformer block is attention plus a feed-forward network, each wrapped in a residual connection and normalisation.** h ← h + Attention(Norm(h)); h ← h + MLP(Norm(h)), where MLP is a Multi-Layer Perceptron applied to each position independently. Attention moves information between positions; the MLP processes it within a position and holds much of the model's stored knowledge. The residual stream lets dozens to over a hundred blocks stack stably.

6. **Masking turns the same machinery into an autoregressive generator.** A decoder-only transformer applies a causal mask so position t attends only to positions ≤ t, then trains to predict token t+1 at every position simultaneously. One sequence of length n gives n training examples in a single parallel pass, a large efficiency gain over RNNs, which must process tokens one after another.

7. **Cost is quadratic in sequence length, and inference is memory-bound.** The n × n score matrix costs O(n² d) compute and naively O(n²) memory. FlashAttention (2022) avoids materialising it by tiling the computation to fit in on-chip memory, an application of cache blocking. At generation time, keys and values of previous tokens are cached (the key-value (KV) cache) so each new token costs O(n), but that cache grows with context and batch size and often dominates GPU memory. Many variants (sparse, linear, sliding-window attention; state-space models) trade some quality for sub-quadratic cost.

## Key concepts

| Term | Meaning |
|---|---|
| Query, key, value | Learned projections: what a position looks for, what it offers for matching, what it contributes |
| Softmax | softmax(z)_i = exp(z_i) / Σ_j exp(z_j); turns scores into a probability distribution |
| Self-attention | Q, K and V all derived from the same sequence |
| Cross-attention | Queries from one sequence, keys and values from another (for example, text attending to an image) |
| Multi-head attention | Several attentions in parallel on lower-dimensional projections |
| Causal mask | Blocks attention to future positions so the model can be autoregressive |
| Positional encoding | Information about position added to or rotated into representations |
| KV cache | Stored keys and values of past tokens, reused during generation |
| Context window | Maximum number of tokens the model attends over |

## How it fits

- **Below:** Everything is [matrix multiplication](../../01-mathematical-foundations/04-algebra/linear-algebra.md) and softmax over [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) distributions, trained by [backpropagation](neural-networks-and-backpropagation.md). Efficient kernels depend on the [memory hierarchy](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md) of [GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md); the lookup intuition comes from [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) and associative memory.
- **Above:** [Large language models](../04-advanced-paradigms/large-language-models.md) are decoder-only transformers at scale; diffusion [generative models](../04-advanced-paradigms/generative-models.md) use transformer denoisers; Vision Transformers serve [computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md); protein-structure and speech models use the same block.
- **Siblings:** [Convolution](convolutional-networks.md) hard-codes local connectivity; attention learns connectivity from content. Transformers' parallelism made them the natural target for [training at scale](training-at-scale.md).

## Common misconceptions

- **"Attention weights explain the model's decision."** They show where information moved in one layer, not why the output came out as it did; information is mixed across many heads and layers.
- **"Transformers understand order natively."** Without positional information, a transformer treats its input as a set.
- **"Long context is free."** Compute grows quadratically and the KV cache linearly with context; models also often use information in the middle of long contexts less reliably than information near the ends.

## Go deeper

- Ashish Vaswani et al., "Attention Is All You Need" (2017): the transformer paper.
- Dzmitry Bahdanau, Kyunghyun Cho and Yoshua Bengio, "Neural Machine Translation by Jointly Learning to Align and Translate" (2014): attention before transformers.
- Tri Dao et al., "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness" (2022): attention as a memory-hierarchy problem.
- Nelson Elhage et al., "A Mathematical Framework for Transformer Circuits" (2021): reading the residual stream and attention heads mechanistically.
