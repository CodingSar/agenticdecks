# LLMs & Agentic Engineering — changelog

**Inputs:** `transformers_llm_working_understanding` (46) + `LLM_Agentic_Harness_Engineering_2026` (55) = 101 notes. Also 3 notes moved in from `statistics-bayes-ml-rl-geometric` (S141 attention scaling + attention_hull.svg, S149 scaling laws, S173 RLHF/DPO), so 104 inputs in total.
**Output:** 126 notes (113 basic, 13 cloze) in 9 subdecks: 01 Tokens & Embeddings, 02 Transformer Architecture, 03 Inference & Serving, 04 Training & Adaptation, 05 RAG & Context Engineering, 06 Agent Memory, 07 Agentic Patterns, 08 Harness Engineering, 09 Evaluation & Reliability.

## Summary
- Deleted: 5. Fully merged: 1. Partial merges (both guids kept on cards with different angles): 5.
- Splits: 23 source notes split, giving 27 extra cards. The mean answer is ~24 words; the longest is 45.
- New cards: 1 ("what MHA/MQA/GQA/MLA have in common": shrinking the KV cache).
- Analogies: 25 added (20%). Examples: KV cache as memoisation, quantization as JPEG, RAG as an open-book exam, MemGPT as RAM/disk paging, Mem0 vs ground-truth logs as event sourcing, harness as a Kubernetes API server with admission control, prompt injection as SQL injection, idempotency as an elevator button, pass@k vs pass^k as free throws.
- Formatting: `<div class="ex">` / `<div class="mk">` blocks became `extra` with `<b>Example:</b>` / `<b>Marketing check:</b>` labels. Expansions of acronyms were kept only where they help.

## Merges
- H32 (cardinal rule: never let the LLM call tools directly) → H31 (harness definition). A new split card covers what goes wrong without a harness.
- Partial: T11 / H1 KV cache (T11 = what and why, plus prefill/decode and prompt-caching splits; H1 = linear memory growth).
- Partial: T16 / H4 lost-in-the-middle (T16 = definition; H4 = why ordering, not rewording).
- Partial: T12 / H7 (the RoPE part of H7 merged into T12's positional-encoding card; H7 keeps FlashAttention).
- Partial: T31 / H45 prompt injection (T31 = what and why; H45 = harness treatment; the marketing check moved to H45).
- Partial: T45 vendor-phrase table became a 3-item cloze; "learns from every interaction" went to T15 (stateless chatbot).
- Moved in: S141 (with the convex-hull figure), S149 (+ Chinchilla split), S173 (split into reward model / KL-regularised objective / DPO).

## Deletions
- H5 dated vendor list of million-token models; the durable lesson is in the 1M-context marketing-check card (T18).
- H6 DeepSeek V4 news item; no durable lesson beyond the MoE/MLA/compression cards.
- H14 MIRIX "six memory types": framework trivia.
- H15 list of memory frameworks: product trivia that changes monthly.
- H19 vague "layered memory controls drift" restatement, covered by the H9/H10 memory cards.

## Other edits
- Enumerations became clozes: KV-cache optimisations, Anthropic workflow patterns, antipatterns, harness components, context-engineering techniques, memory types and paradigms, episodic-memory properties, LLM-judge biases, "99% accuracy" follow-ups, 1M-context checks, prompt/RAG/fine-tune decision rule.
- MQA/GQA/MLA comparison split into one card per variant.
- Contrast cards: pass@k vs pass^k, guardrails vs evaluations, agent vs workflow, pre-inference vs JIT retrieval.
- Dated statistics kept only as labelled data points in `extra` (Datadog 429s, SWE-bench scaffold spread), with the lasting principle in the answer.
