# Advanced Paradigms

> **Layer:** [13 Artificial Intelligence](../README.md) › Advanced paradigms
> **Children:** [Reinforcement learning](reinforcement-learning.md) · [Generative models](generative-models.md) · [Large language models](large-language-models.md) · [Retrieval and embeddings](retrieval-and-embeddings.md) · [Alignment and safety](alignment-and-safety.md)

## What this area is about

The foundations of Machine Learning (ML) assume a fixed dataset of inputs and labels and a model that predicts. This area covers what happens when those assumptions are dropped. **Reinforcement learning** (RL) drops the labels: an agent learns from rewards earned by acting. **Generative models** drop the single right answer: the model learns a whole distribution and samples new data from it. **Large language models** (LLMs) combine both at unprecedented scale: a generative model of text, refined by reinforcement learning, used as a general-purpose reasoning and interface engine. **Retrieval and embeddings** gives models a memory they can look up: learned vectors in which nearness means relatedness, searched approximately at scale and fed to language models as context. **Alignment and safety** asks the question that arises once systems are this capable and this indirectly specified: are they doing what we actually want?

The unifying idea is **optimisation of an objective that is only a proxy for the goal**. Reward is a proxy for desired behaviour; likelihood is a proxy for realism; next-token loss is a proxy for usefulness; embedding similarity is a proxy for relevance; human ratings are a proxy for human values. Each child exploits the power of optimising a proxy, and the last child deals with what happens when the proxy and the goal come apart.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Reinforcement learning](reinforcement-learning.md) | Learning behaviour from reward through interaction; the Bellman equation | Dynamic programming, deep networks |
| [Generative models](generative-models.md) | Learning and sampling high-dimensional distributions: autoregressive, Variational Autoencoder (VAE), Generative Adversarial Network (GAN), diffusion | Unsupervised learning, deep networks |
| [Large language models](large-language-models.md) | Autoregressive generation of text at scale, post-trained with RL, including Reinforcement Learning from Human Feedback (RLHF) | Transformers, generative models, reinforcement learning |
| [Retrieval and embeddings](retrieval-and-embeddings.md) | Learned vector representations, approximate nearest-neighbour search, Retrieval-Augmented Generation (RAG) | Unsupervised learning, transformers, nearest-neighbour structures |
| [Alignment and safety](alignment-and-safety.md) | Making capable optimised systems pursue intended goals and resist misuse | All of the above |

```
   reinforcement learning ----(RLHF, RL on verifiable rewards)---------+
                                                                       v
   generative models -----(autoregressive text model at scale)--> large language models
                                                                       ^
   retrieval and embeddings ----(RAG: documents into the context)------+

                 all four, once deployed and optimised against proxies
                                      |
                                      v
                           alignment and safety
     (reward hacking, misuse, prompt injection, robustness, oversight)
```

Read reinforcement learning and generative models in either order; they are independent foundations. Large language models then combine them: pre-training is generative modelling, post-training is reinforcement learning. Retrieval and embeddings comes next because its main modern use is to ground language models in documents they were not trained on, although embeddings predate LLMs and also drive search and recommendation. Alignment comes last because its problems are visible in all of these and most pressing in deployed language-model systems, where retrieved text is also a channel for prompt injection.

## Connections to sibling areas

- **[Classical AI](../01-classical-ai/README.md):** Classical Artificial Intelligence (AI) supplies the foundations here. Reinforcement learning formalises sequential decisions as Markov Decision Processes, an extension of probabilistic reasoning; game-playing systems combine it with classical tree search. LLM agents rediscover planning and frequently call classical solvers as tools.
- **[Machine learning foundations](../02-machine-learning-foundations/README.md):** Generative models are unsupervised density estimation; embeddings are learned representations from self-supervised and contrastive training, and approximate search revives nearest-neighbour methods; self-supervised pre-training is the reason LLMs exist; evaluation and generalisation problems reappear here in their hardest forms (open-ended outputs, distribution shift, contaminated benchmarks).
- **[Deep learning](../03-deep-learning/README.md):** Every paradigm here uses deep networks as its function approximator: convolutional networks and transformers as diffusion denoisers, transformers as LLMs, value and policy networks in deep RL. Training at scale is what makes frontier models possible.

## Connections across layers

From below, these paradigms need [probability](../../01-mathematical-foundations/06-probability-and-statistics/README.md), [dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md), [information theory](../../02-theory-of-computation/01-information-theory/README.md) and enormous parallel compute from [accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md) and [cloud systems](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md). Alignment borrows its adversarial mindset from [security](../../11-security-and-cryptography/README.md) and its operational practice from [software engineering](../../12-software-engineering/README.md). Upward, LLMs and generative models are reshaping [human-computer interaction](../../14-human-and-visual-computing/01-human-computer-interaction/README.md) and [media](../../14-human-and-visual-computing/03-media-and-vision/README.md), and raise the questions of [computing in context](../../15-computing-in-context/README.md).

## Cross-cutting threads

- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): reinforcement learning is learned closed-loop control; RLHF closes a loop through human judgement.
- [Recursion and self-reference](../../CROSS-CUTTING.md#recursion-and-self-reference): the Bellman equation defines value in terms of itself; models critique and train models.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): evaluating and controlling systems whose internal goals cannot be read directly.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): exploration versus exploitation; diversity versus fidelity; helpfulness versus harmlessness.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): testing can show a capability is present, never that it is absent.
