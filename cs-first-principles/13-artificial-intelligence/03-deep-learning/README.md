# Deep Learning

> **Layer:** [13 Artificial Intelligence](../README.md) › Deep learning
> **Children:** [Neural networks and backpropagation](neural-networks-and-backpropagation.md) · [Convolutional networks](convolutional-networks.md) · [Recurrent networks and sequence models](recurrent-networks-and-sequence-models.md) · [Attention and transformers](attention-and-transformers.md) · [Training at scale](training-at-scale.md)

## What this area is about

Deep learning is Machine Learning (ML) with deep neural networks: long compositions of simple differentiable layers trained end to end by gradient descent. The question it answers is how to learn directly from raw signals (pixels, waveforms, characters) without a human first designing the features. Its unifying idea is **learned representation**: each layer transforms the previous layer's output into a slightly more useful description, and backpropagation adjusts every layer at once so that the final description makes the task easy.

Three forces made it work after decades of false starts: large labelled and unlabelled datasets from the web, Graphics Processing Units (GPUs) that perform dense matrix arithmetic hundreds of times faster than general processors, and a handful of engineering fixes (Rectified Linear Unit (ReLU) activations, careful initialisation, normalisation, residual connections) that made deep stacks trainable. Since 2012 it has become the dominant approach in vision, speech and language.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Neural networks and backpropagation](neural-networks-and-backpropagation.md) | The universal mechanism: layers, composition, and the chain-rule algorithm that trains them | Calculus, optimisation |
| [Convolutional networks](convolutional-networks.md) | Architecture with a locality and translation prior for grid data | Neural networks |
| [Recurrent networks and sequence models](recurrent-networks-and-sequence-models.md) | Architecture that carries a state through time; gating, sequence-to-sequence, state-space models | Neural networks |
| [Attention and transformers](attention-and-transformers.md) | Architecture where connectivity is computed from content; the basis of modern language models | Neural networks |
| [Training at scale](training-at-scale.md) | Running the training loop on thousands of accelerators; scaling laws | All of the above; parallel hardware |

```
                 neural networks + backpropagation
                    (composition, chain rule)
                /              |                 \
   share across space   share across time    connect by content
     convolution          recurrence  ---------> attention
     (locality)        (fixed-size state)  bottleneck relieved,
                \              |          recurrence dropped
                 \             |                 /
                          training at scale
          (data, model and pipeline parallelism; scaling laws)
```

Read neural networks first: everything else is a specialisation of it. The three architecture leaves answer "which inductive bias should the architecture build in?". Convolution assumes nearby inputs interact and patterns repeat across positions; recurrence assumes the past can be summarised in a fixed-size state carried forward one step at a time; attention assumes nothing about distance and learns which positions interact. Read recurrent networks before attention: attention was invented to relieve the recurrent encoder-decoder's bottleneck, and the transformer then dropped recurrence because sequential steps cannot be parallelised. State-space models, covered in the same leaf, are recurrence redesigned to train in parallel. Transformers' weaker prior needs more data, which is why the last child, scale, mattered so much to their rise. Training at scale is where deep learning becomes a distributed-systems problem.

## Connections to sibling areas

- **[Classical AI](../01-classical-ai/README.md):** Deep networks replaced the hand-written perception and heuristics of classical Artificial Intelligence (AI), wherever explicit models had failed. In hybrids such as AlphaGo, learned networks supply the evaluation function that classical tree search uses.
- **[Machine learning foundations](../02-machine-learning-foundations/README.md):** Deep learning inherits the loss-optimise-evaluate loop unchanged. It also strains classical theory: over-parameterised networks generalise better than capacity bounds predict.
- **[Advanced paradigms](../04-advanced-paradigms/README.md):** Deep networks are the function approximators inside deep reinforcement learning, diffusion models and large language models. The paradigms change the objective and data; the machinery here stays the same.

## Connections across layers

Deep learning is matrix arithmetic from [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md) driven by gradients from [calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md). It owes its speed to [GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) and [accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md) and to reduced-precision [floating point](../../03-digital-logic/01-number-representation/floating-point.md); its largest runs are [distributed and parallel](../../10-distributed-and-parallel-computing/README.md) computations in [cloud](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) data centres; its data pipelines draw on [data management](../../09-data-management/README.md). Upward it supplies [computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md), learned [media compression](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md) and neural rendering in [graphics](../../14-human-and-visual-computing/02-computer-graphics/README.md). Demand for deep learning compute now shapes [hardware design](../../04-computer-architecture/README.md) itself.

## Cross-cutting threads

- [Composition](../../CROSS-CUTTING.md#composition): deep networks are compositions of simple layers whose gradients compose by the chain rule.
- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): data, tensor and pipeline parallelism; transformers process all positions at once, where recurrent networks must step through time.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): convolution exploits spatial locality; the key-value (KV) cache and tiled attention exploit the memory hierarchy.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): mini-batches amortise weight loads across many examples.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): the network's whole job is learning a representation; low-precision number formats trade accuracy for throughput.
