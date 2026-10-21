# Large Language Models

> **Layer:** [13 Artificial Intelligence](../README.md) › [Advanced paradigms](README.md)
> **Builds on:** [Attention and transformers](../03-deep-learning/attention-and-transformers.md), [Training at scale](../03-deep-learning/training-at-scale.md), [Unsupervised learning](../02-machine-learning-foundations/unsupervised-learning.md), [Character encoding](../../03-digital-logic/01-number-representation/character-encoding.md), [Source coding and compression](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md)
> **Enables:** [Alignment and safety](alignment-and-safety.md), [Interaction design principles](../../14-human-and-visual-computing/01-human-computer-interaction/interaction-design-principles.md), [Ethics and professional responsibility](../../15-computing-in-context/ethics-and-professional-responsibility.md)

## Essence

A Large Language Model (LLM) is a transformer, typically with billions to trillions of parameters, trained to predict the next token of text over a corpus of trillions of tokens. That single self-supervised objective turns out to require learning grammar, facts, translation, arithmetic, coding patterns and multi-step reasoning, because all of them help predict what comes next. Pre-training produces a model of text; further training with demonstrations, human preferences and reinforcement learning turns it into an assistant that follows instructions. At use time the model generates by repeatedly sampling a token and appending it to its input. As of the mid-2020s, LLMs are the most general-purpose Artificial Intelligence (AI) systems in wide use, and also systems whose failure modes (confident errors, sensitivity to phrasing, vulnerability to manipulation) are still being mapped.

## Core tenets

1. **The model defines a probability distribution over the next token.** Text is split into tokens by a subword scheme such as Byte-Pair Encoding (BPE), typically with vocabularies of 30,000 to 250,000 entries. The model outputs logits z over the vocabulary and p(token_i | context) = exp(z_i) / Σ_j exp(z_j). Training minimises cross-entropy, −Σ_t log p(x_t | x_<t), over the corpus. Lower loss means the model compresses text better: an LLM paired with arithmetic coding is a strong text compressor.

2. **Pre-training absorbs the corpus; post-training shapes behaviour.** A pre-trained base model continues any text plausibly, including unhelpful or harmful continuations. Supervised Fine-Tuning (SFT) on example dialogues teaches the assistant format. Reinforcement Learning from Human Feedback (RLHF) trains a reward model on human comparisons of responses and optimises the LLM against it; Direct Preference Optimization (DPO) and AI-feedback variants reach similar ends more cheaply. Post-training uses a tiny fraction of pre-training compute but changes behaviour dramatically.

3. **Capabilities improve predictably with scale, but not uniformly.** Loss follows [scaling laws](../03-deep-learning/training-at-scale.md) in parameters, data and compute. Specific skills can look as if they appear suddenly, partly because all-or-nothing accuracy metrics hide smoothly improving loss.

4. **In-context learning: the prompt is a program.** Given a few examples in its input, an LLM performs the new task without any weight update (Brown et al., 2020). The context window, ranging from a few thousand to over a million tokens in mid-2020s models, is the model's working memory; everything the model "knows" about the current task beyond its weights must be in it.

5. **Thinking out loud buys computation.** Each generated token costs a fixed amount of computation, so a model that writes intermediate reasoning ("chain of thought") before answering spends more computation on harder problems. Models trained with reinforcement learning on verifiable tasks (maths, code with tests) to produce long reasoning traces improved sharply on such tasks in 2024–2025. This "test-time compute" is now a scaling axis alongside model size.

6. **Retrieval and tools ground the model in external facts and actions.** Weights hold knowledge frozen at training time and imprecisely. Retrieval-Augmented Generation (RAG) fetches relevant documents into the context using [embeddings and approximate nearest-neighbour search](retrieval-and-embeddings.md); tool use lets the model emit structured calls to search engines, code interpreters or Application Programming Interfaces (APIs) and read the results. A loop of plan, act and observe gives "agents", which reintroduce classical [planning](../01-classical-ai/search-and-planning.md) problems: error accumulation, verification and safe action.

7. **Fluency is not reliability.** Because training rewards plausible continuations, models can produce fluent, confident statements that are false ("hallucinations"), particularly about rare facts. They can be steered by text in their input that the user did not write (prompt injection), which is a security problem when they read untrusted web pages or emails. These properties make evaluation and [alignment](alignment-and-safety.md) central engineering concerns rather than afterthoughts.

8. **Inference cost is dominated by memory bandwidth.** Generating one token requires reading every active weight from memory, so single-stream decoding speed is limited by memory bandwidth, not arithmetic. Serving systems batch many users together, cache keys and values, quantise weights to 8 or 4 bits, and use speculative decoding (a small model drafts, the large one verifies). Mixture-of-Experts (MoE) models activate only a fraction of their parameters per token, decoupling total knowledge capacity from per-token cost.

## Key concepts

| Term | Meaning |
|---|---|
| Token | Unit of text the model reads and writes, typically a word piece |
| Logits | Unnormalised scores over the vocabulary, turned into probabilities by softmax |
| Base model | Model after pre-training only; a text continuer |
| Instruction tuning / SFT | Fine-tuning on examples of desired responses |
| RLHF | Optimising the model against a reward model learned from human preference comparisons |
| In-context learning | Performing a task from examples in the prompt without weight updates |
| Chain of thought | Generating intermediate reasoning steps before the answer |
| RAG | Retrieving documents into the context to ground generation |
| Hallucination | Fluent output not supported by facts or the provided context |

## How it fits

- **Below:** The architecture is the decoder-only [transformer](../03-deep-learning/attention-and-transformers.md); training is [self-supervised learning](../02-machine-learning-foundations/unsupervised-learning.md) run with the systems of [training at scale](../03-deep-learning/training-at-scale.md); tokenisation sits on [character encoding](../../03-digital-logic/01-number-representation/character-encoding.md); the loss is a [code length](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md); post-training uses [reinforcement learning](reinforcement-learning.md).
- **Above:** LLMs become conversational and agentic interfaces in [interaction design](../../14-human-and-visual-computing/01-human-computer-interaction/interaction-design-principles.md), coding assistants in [software engineering](../../12-software-engineering/README.md), and new attack surfaces in [web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md). Their social effects belong to [ethics](../../15-computing-in-context/ethics-and-professional-responsibility.md) and [law and policy](../../15-computing-in-context/law-privacy-and-policy.md).
- **Siblings:** LLMs are autoregressive [generative models](generative-models.md) of text, shaped by [reinforcement learning](reinforcement-learning.md), grounded by [retrieval](retrieval-and-embeddings.md) and constrained by [alignment](alignment-and-safety.md) techniques. Their autoregressive generation loop comes from [recurrent language models](../03-deep-learning/recurrent-networks-and-sequence-models.md).

## Common misconceptions

- **"It is just autocomplete, so it cannot reason."** The training objective is next-token prediction, but predicting text well requires internal computation that, measurably, solves novel problems. Its reasoning is real but unreliable in ways human reasoning is not.
- **"It looks facts up in a database."** Unless retrieval is used, knowledge is stored diffusely in weights, which is why recall of rare facts is lossy and can be confidently wrong.
- **"The model learns from each conversation."** Weights are fixed at deployment; within a conversation it adapts only through its context.

## Go deeper

- Tom Brown et al., "Language Models are Few-Shot Learners" (2020): GPT-3 and in-context learning.
- Long Ouyang et al., "Training Language Models to Follow Instructions with Human Feedback" (2022): the SFT-plus-RLHF recipe.
- Jason Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (2022): intermediate steps as extra computation.
- Patrick Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (2020): grounding generation in retrieved text for Natural Language Processing (NLP) tasks.
