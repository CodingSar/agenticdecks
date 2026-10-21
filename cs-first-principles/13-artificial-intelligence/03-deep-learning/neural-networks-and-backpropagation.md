# Neural Networks and Backpropagation

> **Layer:** [13 Artificial Intelligence](../README.md) › [Deep learning](README.md)
> **Builds on:** [Learning as optimization](../02-machine-learning-foundations/learning-as-optimization.md), [Calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md), [Linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), [Dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md)
> **Enables:** [Convolutional networks](convolutional-networks.md), [Attention and transformers](attention-and-transformers.md), [Training at scale](training-at-scale.md), [SIMD and GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md)

## Essence

A neural network is a function built by composing many simple layers, each a linear map followed by a fixed non-linearity: h = σ(Wx + b). Stacking layers lets the network build features of features, so it can learn its own representation of raw input instead of relying on hand-designed features. Training adjusts all the weights by gradient descent, and the gradient is computed by **backpropagation**: the chain rule applied backwards through the composition, reusing intermediate results so that the gradient for every parameter costs about as much as one extra forward pass. Composition gives expressiveness; backpropagation makes that expressiveness trainable; dense matrix multiplication makes it fast on parallel hardware.

## Core tenets

1. **A layer is a linear map plus a non-linearity, and the non-linearity is essential.** A Multi-Layer Perceptron (MLP) computes h₁ = σ(W₁x + b₁), h₂ = σ(W₂h₁ + b₂), and so on. Without σ, any stack of linear layers collapses into a single linear map, no more expressive than one layer. The Rectified Linear Unit (ReLU), σ(z) = max(0, z), is the common default because it is cheap and does not saturate for positive inputs.

2. **Wide enough networks can approximate anything; deep ones do it efficiently.** The universal approximation theorem says a single hidden layer with enough units can approximate any continuous function on a bounded domain arbitrarily well. It says nothing about how many units or whether training finds them. Depth matters because many natural functions are compositional (edges → textures → parts → objects), and deep networks can represent such functions with exponentially fewer units than shallow ones.

3. **Backpropagation is the chain rule organised as dynamic programming.** The network is a computational graph. A forward pass computes and stores every intermediate value. A backward pass then computes ∂L/∂h for each node from the gradients of its consumers, multiplying by local derivatives: for h = σ(Wx), ∂L/∂W = (∂L/∂h ⊙ σ'(Wx)) xᵀ. Each node's gradient is computed once and reused, so the full gradient costs a small constant times the forward pass, regardless of how many parameters there are. Naively differentiating each parameter separately would cost one forward pass per parameter.

4. **Memory, not arithmetic, often limits training.** The backward pass needs the activations stored during the forward pass, so training memory grows with depth × batch size × layer width. Activation checkpointing trades this back by recomputing some activations, a classic time-space trade-off.

5. **Gradients vanish or explode through many layers.** The gradient at an early layer is a product of many Jacobians. If their typical magnitude is below 1 the product shrinks exponentially (vanishing); above 1 it grows (exploding). This blocked deep networks before about 2010. The fixes are careful initialisation (scaling weights by 1/√fan-in), non-saturating activations, normalisation layers, and residual connections.

6. **Residual connections make depth trainable.** A residual block computes h_{l+1} = h_l + F(h_l). The identity path carries both signal and gradient unchanged through the network, so gradients reach early layers even through hundreds of blocks. Residual Networks (ResNets, 2015) made 100+ layer networks routine, and every transformer uses the same structure.

7. **Most of the work is matrix multiplication, which is why GPUs matter.** A layer applied to a batch is one General Matrix Multiply (GEMM): thousands of independent multiply-adds with high arithmetic intensity. Graphics Processing Units (GPUs) and tensor accelerators execute these at hundreds of teraflops in low precision (circa 2024 hardware). The 2012 AlexNet result, trained on two consumer GPUs, showed that this hardware fit turned neural networks from a curiosity into the dominant method.

## Key concepts

| Term | Meaning |
|---|---|
| Neuron / unit | One output of a layer: a weighted sum of inputs passed through a non-linearity |
| Activation function | The element-wise non-linearity σ (ReLU, Gaussian Error Linear Unit (GELU), sigmoid, tanh) |
| Computational graph | Directed acyclic graph of operations whose composition defines the network |
| Forward pass | Evaluating the network and storing intermediates |
| Backward pass | Propagating ∂L/∂(node) from output to inputs via the chain rule |
| Automatic differentiation | Mechanically computing exact derivatives of programs; backpropagation is its reverse mode |
| Initialisation | Choice of starting weights; sets whether signals shrink or grow through depth |
| Residual connection | Skip path adding a block's input to its output |
| Normalisation layer | Rescaling activations to zero mean and unit variance (batch, layer or root-mean-square norm) |

## How it fits

- **Below:** Backpropagation is the multivariate chain rule from [calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md), organised like [dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md). Layers are [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md); throughput comes from [GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) and [accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md); low-precision arithmetic comes from [floating point](../../03-digital-logic/01-number-representation/floating-point.md).
- **Above:** [Convolutional networks](convolutional-networks.md) and [transformers](attention-and-transformers.md) are neural networks with specific weight-sharing structure; every model in [advanced paradigms](../04-advanced-paradigms/README.md) is trained by backpropagation.
- **Siblings:** This file is the base the other three refine: architecture (convolution, attention) chooses the structure, and [training at scale](training-at-scale.md) runs the same loop on thousands of devices.

## Common misconceptions

- **"Neural networks work like brains."** The 1943 McCulloch–Pitts neuron was brain-inspired, but modern networks are differentiable function compositions trained by a method brains are not known to use.
- **"The universal approximation theorem explains deep learning."** It guarantees existence, not learnability or generalisation, and is about shallow networks.
- **"Backpropagation is a learning algorithm."** It only computes gradients. The learning algorithm is the optimiser (stochastic gradient descent, Adam) that uses them.

## Go deeper

- David Rumelhart, Geoffrey Hinton and Ronald Williams, "Learning Representations by Back-Propagating Errors" (1986): the paper that popularised backpropagation.
- Ian Goodfellow, Yoshua Bengio and Aaron Courville, *Deep Learning* (2016): chapters 6–8 cover networks, backpropagation and optimisation.
- Kaiming He et al., "Deep Residual Learning for Image Recognition" (2015): residual connections and why depth became trainable.
