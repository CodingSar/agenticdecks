# 13 Artificial Intelligence

> **Layer:** 13 Artificial Intelligence
> **Children:** [Classical AI](01-classical-ai/README.md) · [Machine learning foundations](02-machine-learning-foundations/README.md) · [Deep learning](03-deep-learning/README.md) · [Advanced paradigms](04-advanced-paradigms/README.md)

## What this area is about

Artificial Intelligence (AI) asks how to build programs that act sensibly in situations their programmers did not spell out case by case: recognise a face, plan a route, play a game, answer a question, write code. Every other layer of this tree assumes a human writes down the algorithm. AI is the layer where the program must work out *what to do* from a model of the world or from examples of it.

The field has made one large shift over its history, and that shift organises this layer. **Classical AI** (roughly 1956 to the 1990s) has humans write the knowledge: states and actions, constraints, logical rules, probabilistic dependencies. General algorithms then search and reason over that knowledge. **Machine Learning (ML)**, and above all deep learning since 2012, has humans write only a family of functions, an objective and a dataset; the knowledge itself is *learned* by optimisation. Classical AI scales with the ingenuity of the knowledge engineer; ML scales with data and compute, which have grown by many orders of magnitude. That is why, as of the mid-2020s, learned systems dominate perception, language and games, while explicit reasoning survives in solvers, planners and verifiers, increasingly combined with learned components.

## Why this layer sits here

AI needs almost everything beneath it, which is why it sits near the top of the stack.

- **Classical AI** is built on [logic](../01-mathematical-foundations/01-logic/README.md) (knowledge representation, inference), on [graph search](../05-algorithms-and-data-structures/05-graph-algorithms/README.md) and [design paradigms](../05-algorithms-and-data-structures/03-design-paradigms/README.md) such as backtracking and dynamic programming, and on [complexity](../02-theory-of-computation/04-complexity/README.md) and [computability](../02-theory-of-computation/03-computability/README.md) results that tell it which problems are hard or undecidable.
- **Learned functions** are built on [linear algebra](../01-mathematical-foundations/04-algebra/linear-algebra.md) (every layer of a network is a matrix multiply), [calculus and optimisation](../01-mathematical-foundations/05-continuous-mathematics/README.md) (gradients drive learning), and [probability and statistics](../01-mathematical-foundations/06-probability-and-statistics/README.md) (models are distributions; evaluation is inference). They became practical only with [Graphics Processing Units (GPUs) and accelerators](../04-computer-architecture/04-parallel-architecture/README.md) from Layer 04 that perform dense arithmetic in low-precision [floating point](../03-digital-logic/01-number-representation/floating-point.md), the [data systems](../09-data-management/README.md) of Layer 09 that store and prepare training corpora, and the [distributed and parallel computing](../10-distributed-and-parallel-computing/README.md) of Layer 10 that spreads one training run over thousands of chips.
- It also relies on [software engineering](../12-software-engineering/README.md) practice to build, test and operate models, and on [security](../11-security-and-cryptography/README.md) thinking once models face adversaries.

The abstraction this layer contributes to the stack is the **learned function**: a component whose behaviour is specified by an objective and data rather than by code, and that maps messy inputs (pixels, speech, text) to useful outputs. Layers above treat it as a building block: [Layer 14](../14-human-and-visual-computing/README.md) uses it for vision, interfaces and media, and [Layer 15](../15-computing-in-context/README.md) asks what society should do about it.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Classical AI](01-classical-ai/README.md) | Hand-written models plus general algorithms: search, constraints, logic, probabilistic inference | Logic, algorithms, probability |
| [Machine learning foundations](02-machine-learning-foundations/README.md) | Learning functions from data: loss, optimisation, generalisation, evaluation | Calculus, linear algebra, statistics |
| [Deep learning](03-deep-learning/README.md) | Deep neural networks that learn their own representations; convolutional, recurrent and attention architectures; scale | ML foundations, parallel hardware |
| [Advanced paradigms](04-advanced-paradigms/README.md) | Reinforcement Learning (RL), generative models, Large Language Models (LLMs), retrieval and embeddings, alignment | All of the above |

```
   01 logic, 05 search ----------> [01 classical AI]  hand-written knowledge
                                         |   probabilistic reasoning bridges
   01 linear algebra, calculus,          v
      probability ---------------> [02 ML foundations] learned functions
   04 GPUs, 10 parallelism ------> [03 deep learning]   learned representations
   09 data, 10 training at scale        |
                                         v
                               [04 advanced paradigms]
   RL (reward) · generative models (distributions) · LLMs · retrieval · alignment
```

Read the children in order. Classical AI introduces the agent, the model and the combinatorial explosion that every method must fight. ML foundations replaces hand-written models with learned ones and introduces the central tension between fitting data and generalising beyond it. Deep learning supplies the function family and the engineering that made learning work on raw signals. Advanced paradigms changes the objective (reward, likelihood, human preference) and confronts what happens when highly capable systems optimise a proxy for what we want. Probabilistic reasoning is the hinge: it is classical AI's language for uncertainty and ML's language for models.

## Connections to neighbouring layers

- **[01 Mathematical foundations](../01-mathematical-foundations/README.md):** Logic for classical AI; linear algebra, calculus, optimisation and probability for everything learned. AI is applied mathematics more directly than any other layer above 05.
- **[02 Theory of computation](../02-theory-of-computation/README.md):** Hardness for nondeterministic polynomial time (NP-hardness) explains why search needs heuristics; undecidability bounds logical reasoners; information theory explains why prediction is compression and why language-model loss is a code length.
- **[04 Computer architecture](../04-computer-architecture/README.md):** Deep learning is co-designed with hardware. GPUs made it practical, and demand for it now drives tensor cores, high-bandwidth memory and dedicated accelerators.
- **[05 Algorithms and data structures](../05-algorithms-and-data-structures/README.md):** Classical AI is algorithm design under exponential state spaces; backpropagation and the Bellman equation are dynamic programming.
- **[09 Data management](../09-data-management/README.md) and [10 Distributed and parallel computing](../10-distributed-and-parallel-computing/README.md):** Training data pipelines and feature stores come from 09, and [vector search](04-advanced-paradigms/retrieval-and-embeddings.md) extends its indexing ideas to learned embeddings; data, tensor and pipeline parallelism and fault-tolerant clusters come from 10.
- **[11 Security and cryptography](../11-security-and-cryptography/README.md):** Models are attack surfaces (adversarial examples, prompt injection, data poisoning) and tools for attack and defence; alignment borrows threat modelling.
- **[14 Human and visual computing](../14-human-and-visual-computing/README.md):** Computer vision is now mostly deep learning; LLMs are becoming a primary user interface; generative models create images and media.
- **[15 Computing in context](../15-computing-in-context/README.md):** Bias, privacy, accountability, labour and regulation of AI are central topics of ethics and law.

## Cross-cutting threads

- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): the learned function as a component specified by objective and data rather than code.
- [Encoding and representation](../CROSS-CUTTING.md#encoding-and-representation): classical AI chooses representations by hand; deep learning learns them.
- [Feedback and control](../CROSS-CUTTING.md#feedback-and-control): training loops and reinforcement learning measure error and adjust.
- [Limits and impossibility](../CROSS-CUTTING.md#limits-and-impossibility): NP-hardness, semi-decidability, No Free Lunch.
- [Pipelining and parallelism](../CROSS-CUTTING.md#pipelining-and-parallelism): training at scale splits work across thousands of devices.
- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): expressiveness versus tractability; bias versus variance; capability versus cost.
- [Trust and verification](../CROSS-CUTTING.md#trust-and-verification): evaluating and aligning systems whose behaviour is not written down.
