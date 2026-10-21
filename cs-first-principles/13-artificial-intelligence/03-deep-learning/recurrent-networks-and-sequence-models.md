# Recurrent Networks and Sequence Models

> **Layer:** [13 Artificial Intelligence](../README.md) › [Deep learning](README.md)
> **Builds on:** [Neural networks and backpropagation](neural-networks-and-backpropagation.md), [Finite state machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md), [Linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), [Probabilistic reasoning](../01-classical-ai/probabilistic-reasoning.md)
> **Enables:** [Attention and transformers](attention-and-transformers.md), [Large language models](../04-advanced-paradigms/large-language-models.md), [Generative models](../04-advanced-paradigms/generative-models.md)

## Essence

Text, speech, sensor streams and actions arrive as sequences of varying length, and the meaning of each element depends on what came before. A Recurrent Neural Network (RNN) handles this the way a state machine does: it keeps a fixed-size hidden state, and at each step it combines the state with the next input to produce a new state, reusing the same weights at every step. Training unrolls the loop into a very deep network and backpropagates through it, which exposes the central difficulty: gradients that must travel back through many steps shrink or blow up exponentially. Gated cells (Long Short-Term Memory (LSTM), Gated Recurrent Unit (GRU)) fixed this well enough to power translation and speech recognition in the 2010s. Attention then replaced recurrence because it trains in parallel and connects distant positions directly. Linear state-space models bring recurrence back in a form that also trains in parallel.

## Core tenets

1. **An RNN is a learned state machine with shared weights.** At each step t,

   h_t = tanh(W_h h_{t−1} + W_x x_t + b),  y_t = W_y h_t

   The same W_h, W_x and W_y apply at every position, so the network handles any length with a fixed number of parameters, just as a convolution reuses one filter at every pixel. The hidden state h_t is a lossy summary of the whole prefix x_1 … x_t; everything the model remembers must fit in it.

2. **Training is backpropagation through time.** Unrolling the loop over n steps gives an n-layer feed-forward network whose layers share weights. Backpropagation through time (BPTT) runs ordinary backpropagation on it and sums each shared weight's gradient over all steps. Memory grows with sequence length, so long streams use truncated BPTT: backpropagate only through the last k steps while carrying the state forward.

3. **Gradients vanish or explode through time.** The gradient of h_t with respect to h_k is a product of t − k Jacobians, each roughly diag(tanh′) · W_h. If the largest singular value of W_h, scaled by the activation slope, is below 1, the product shrinks exponentially; above 1 it grows (Bengio, Simard and Frasconi, 1994; Hochreiter, 1991). Plain RNNs therefore struggle to learn dependencies more than a few tens of steps apart. Exploding gradients are tamed cheaply by clipping the gradient norm; vanishing gradients need a change of architecture.

4. **Gates create an additive memory path.** An LSTM (Hochreiter and Schmidhuber, 1997; forget gate added by Gers et al., 2000) keeps a separate cell state updated as

   c_t = f_t ⊙ c_{t−1} + i_t ⊙ c̃_t,  h_t = o_t ⊙ tanh(c_t)

   where the forget, input and output gates f, i, o are sigmoids in (0, 1) computed from h_{t−1} and x_t, and ⊙ is element-wise multiplication. When f_t ≈ 1 the cell carries information and gradient forward almost unchanged, the same idea as a residual connection but applied across time. The GRU (Cho et al., 2014) merges cell and hidden state and uses two gates; it performs comparably with fewer parameters.

5. **Encoder-decoder models map sequences to sequences, through a bottleneck.** Sequence-to-sequence learning (Sutskever, Vinyals and Le, 2014) reads the source sentence with one RNN into a final state vector, then generates the target with a second RNN conditioned on that vector, one token at a time. It made end-to-end neural machine translation work, but quality fell on long sentences because the whole source had to squeeze through one fixed-size vector.

6. **Attention removed the bottleneck, then removed the recurrence.** Bahdanau, Cho and Bengio (2014) let the decoder take a learned weighted average of *all* encoder states at each step. The transformer (2017) kept attention and dropped recurrence entirely, for two reasons. Training: an RNN's step t cannot start until step t − 1 finishes, so n positions need n sequential steps, while attention processes all positions at once on parallel hardware. Path length: information between positions i and j passes through |i − j| state updates in an RNN but one attention hop in a transformer. The price is attention's cost quadratic in length and a key-value cache that grows with context, whereas an RNN carries a constant-size state.

7. **State-space models are the modern return of recurrence.** A linear state-space model (SSM) layer uses h_t = A h_{t−1} + B x_t, y_t = C h_t with no non-linearity inside the loop. Linearity lets the whole output be computed as a long convolution or an associative parallel scan during training, so it parallelises like attention, while generation still steps a fixed-size state at constant cost per token. S4 (Gu, Goel and Ré, 2021) showed such layers capture very long dependencies with carefully structured A; Mamba (Gu and Dao, 2023) makes A, B and C depend on the input, so the model can choose what to keep. A fixed-size state cannot store every earlier token exactly, so pure SSMs lag attention at verbatim recall and copying; as of the mid-2020s, hybrids that interleave SSM and attention layers are a common compromise.

## Key concepts

| Term | Meaning |
|---|---|
| Hidden state | Fixed-size vector summarising the sequence seen so far |
| Unrolling | Writing the recurrence out as one layer per time step |
| BPTT | Backpropagation through the unrolled network, summing gradients of shared weights |
| Truncated BPTT | Backpropagating only through a recent window of steps |
| Gradient clipping | Rescaling a gradient whose norm exceeds a threshold |
| Gate | Sigmoid-valued vector that scales what is kept, written or read |
| Cell state | LSTM's additively updated memory, separate from its output |
| Encoder-decoder | One network reads the input, another generates the output from its summary |
| Parallel scan | Computing all prefixes of an associative operation in logarithmic depth |

## How it fits

- **Below:** An RNN is the continuous, learned cousin of the [finite state machine](../../03-digital-logic/03-sequential-logic/finite-state-machines.md); training is [backpropagation](neural-networks-and-backpropagation.md) on the unrolled graph; whether gradients vanish is a question about the singular values of a matrix product from [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md). Hidden Markov Models and Kalman filters in [probabilistic reasoning](../01-classical-ai/probabilistic-reasoning.md) are the hand-specified predecessors with the same state-update shape; a Kalman filter is a linear state-space model.
- **Above:** [Large language models](../04-advanced-paradigms/large-language-models.md) inherit the autoregressive generate-one-token-and-feed-it-back loop from RNN language models; autoregressive [generative models](../04-advanced-paradigms/generative-models.md) of audio first used it too. Policies in [reinforcement learning](../04-advanced-paradigms/reinforcement-learning.md) use recurrent state when the environment is only partly observed.
- **Siblings:** [Convolutional networks](convolutional-networks.md) share weights across space, RNNs across time. [Attention and transformers](attention-and-transformers.md) replaced RNNs for most sequence tasks; [training at scale](training-at-scale.md) explains why parallel-friendly architectures won.

## Common misconceptions

- **"LSTMs solve long-term memory."** Gates make dependencies of hundreds of steps learnable, but the state is still fixed-size and sequential; very long contexts remain hard.
- **"Transformers won because attention is more expressive."** The decisive advantage was training parallelism on Graphics Processing Units (GPUs); quality per unit of compute followed from being able to scale.
- **"Recurrence is obsolete."** State-space and linear-recurrent layers are an active line of work precisely because constant-cost generation matters at long context.

## Go deeper

- Jeffrey Elman, "Finding Structure in Time" (1990): the simple recurrent network and what its hidden state learns.
- Sepp Hochreiter and Jürgen Schmidhuber, "Long Short-Term Memory" (1997): the gated cell and the constant error flow argument.
- Ilya Sutskever, Oriol Vinyals and Quoc Le, "Sequence to Sequence Learning with Neural Networks" (2014): encoder-decoder translation.
- Albert Gu and Tri Dao, "Mamba: Linear-Time Sequence Modeling with Selective State Spaces" (2023): input-dependent state-space models.
