# Retrieval and Embeddings

> **Layer:** [13 Artificial Intelligence](../README.md) › [Advanced paradigms](README.md)
> **Builds on:** [Unsupervised learning](../02-machine-learning-foundations/unsupervised-learning.md), [Attention and transformers](../03-deep-learning/attention-and-transformers.md), [Computational geometry](../../05-algorithms-and-data-structures/07-advanced-topics/computational-geometry.md), [Linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), [Evaluation and experimentation](../02-machine-learning-foundations/evaluation-and-experimentation.md)
> **Enables:** [Large language models](large-language-models.md), [Computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md), [Non-relational models](../../09-data-management/01-data-models/non-relational-models.md)

## Essence

An embedding is a learned map from an object (a word, a passage, an image, a user) to a vector, trained so that geometric closeness means similarity for some task. Once meaning is geometry, "find things related to this" becomes "find the nearest vectors", a query that works across paraphrases, languages and even modalities where keyword matching fails. Exact nearest-neighbour search over billions of high-dimensional vectors is too slow, so practical systems use **approximate** indexes (graph-based, cluster-based and compressed) that trade a little recall for orders of magnitude in speed and memory. Retrieval-Augmented Generation (RAG) puts this machinery in front of a Large Language Model (LLM): fetch the most relevant documents, place them in the prompt, and let the model answer from them. The whole pipeline is only as good as its weakest stage, so each stage must be measured separately.

## Core tenets

1. **An embedding is a representation shaped by its training objective.** Word2vec (Mikolov et al., 2013) learned word vectors by predicting a word's neighbours, exploiting the distributional hypothesis that words in similar contexts have similar meanings; vector offsets then captured relations such as king − man + woman ≈ queen. Modern text and image encoders are transformers trained contrastively: pull matching pairs (question and answer, image and caption) together and push the other items in the batch apart. "Similar" therefore means whatever the training pairs meant. An encoder trained on topical similarity may rank a passage that contradicts the query as highly as one that answers it.

2. **Similarity is a dot product, and normalisation makes the metrics agree.** Cosine similarity is the dot product of unit vectors, and for unit vectors squared Euclidean distance equals 2 − 2 · cosine, so all three give the same ranking. A dual (bi-)encoder embeds queries and documents independently, so the corpus is embedded once offline and each query costs one encoder pass plus a search. Vectors from different models live in unrelated spaces: changing the embedding model means re-embedding the whole corpus.

3. **Exact search is linear, and high dimensions defeat tree indexes.** Brute force compares the query with all n vectors of dimension d, O(nd) per query: one billion 768-dimensional float32 vectors occupy about 3 terabytes, and a single machine needs seconds or more just to stream them past one query. Space-partitioning trees such as k-d trees help in two or three dimensions but degrade towards a linear scan beyond roughly 10–20, because in high dimensions distances concentrate and almost every partition must be checked. Hence approximate nearest-neighbour (ANN) search, judged by recall@k (the fraction of true nearest neighbours returned) against latency and memory.

4. **Graph indexes walk greedily towards the query.** Hierarchical Navigable Small World (HNSW) graphs (Malkov and Yashunin, 2016) link each vector to a few dozen near neighbours and add sparse upper layers with long-range links, like a skip list. A query enters at the top, greedily moves to the neighbour closest to the query, and descends layer by layer, visiting a tiny fraction of the data. HNSW gives high recall at low latency but stores full vectors plus links in memory and handles deletions awkwardly.

5. **Cluster indexes search only the promising regions.** An inverted-file (IVF) index runs k-means on the corpus, assigns each vector to its nearest centroid's list, and at query time scans only the lists of the few centroids nearest the query (the "nprobe" parameter). Raising nprobe raises recall and cost together. A true neighbour that fell just across a cluster boundary is missed unless its list is probed.

6. **Product quantisation compresses vectors so they fit in memory.** Product quantisation (PQ; Jégou, Douze and Schmid, 2011) splits each vector into m sub-vectors and replaces each with the index of the nearest of 256 learned centroids, so a vector becomes m bytes. A 768-dimensional float32 vector (3,072 bytes) coded with m = 96 shrinks 32-fold. Distances are approximated by summing precomputed query-to-centroid table entries, which is fast. Combined as IVF-PQ, this is how billion-scale search fits on one machine; the lost precision is usually recovered by re-ranking a short list with full vectors.

7. **RAG separates what the model knows from what it can look up.** Documents are split into chunks, embedded and indexed. At query time the system retrieves the top-k chunks, often re-ranks them with a cross-encoder that reads query and chunk together (slower, more accurate), and inserts them into the prompt with instructions to answer from them and cite them. Knowledge can then be updated, access-controlled and audited without retraining. Lexical search with an inverted index and the Best Matching 25 (BM25) ranking function still wins on rare names, codes and exact phrases, so production systems commonly combine dense and lexical results (hybrid search).

8. **Evaluate each stage, then the whole.** Retrieval is measured against labelled relevant documents with recall@k, Mean Reciprocal Rank (MRR) or normalised Discounted Cumulative Gain (nDCG); the ANN index is measured by its recall relative to exact search; generation is measured for faithfulness (is every claim supported by the retrieved text?) and answer correctness. If the right passage was never retrieved, no generator can fix it; if it was retrieved and the answer is still wrong, the fault is in reading. Retrieved text is also untrusted input: a document can carry instructions that hijack the model (indirect prompt injection).

## Key concepts

| Term | Meaning |
|---|---|
| Embedding | Learned vector whose geometry reflects task-defined similarity |
| Contrastive training | Pulling related pairs together and unrelated items apart in embedding space |
| Dual encoder / cross-encoder | Embeds query and document separately / reads them jointly to score relevance |
| ANN search | Nearest-neighbour search that may miss some true neighbours in exchange for speed |
| Recall@k | Fraction of the relevant (or true nearest) items found in the top k results |
| HNSW | Layered proximity graph searched greedily from coarse to fine |
| IVF | Index that clusters vectors and searches only the nearest clusters |
| Product quantisation | Compressing a vector as codebook indices for its sub-vectors |
| RAG | Generating an answer conditioned on retrieved documents |
| Hybrid search | Combining dense vector retrieval with lexical keyword retrieval |

## How it fits

- **Below:** Embeddings come from [self-supervised and contrastive learning](../02-machine-learning-foundations/unsupervised-learning.md) with [transformer](../03-deep-learning/attention-and-transformers.md) encoders; IVF is k-means; similarity is [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md); nearest-neighbour structures and the curse of dimensionality are [computational geometry](../../05-algorithms-and-data-structures/07-advanced-topics/computational-geometry.md); HNSW is greedy [graph traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md); locality-sensitive hashing generalises [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) so that near keys collide. Ranking metrics come from [evaluation](../02-machine-learning-foundations/evaluation-and-experimentation.md).
- **Above:** RAG and tool use ground [large language models](large-language-models.md); image-text embeddings power search and zero-shot recognition in [computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md); vector indexes are a data model in their own right in [non-relational stores](../../09-data-management/01-data-models/non-relational-models.md), and recommendation systems retrieve candidates the same way.
- **Siblings:** Retrieval is the main defence against the confident errors that [large language models](large-language-models.md) make from weights alone, and a new attack surface for [alignment and safety](alignment-and-safety.md). [Generative models](generative-models.md) produce content; retrieval decides which existing content conditions them.

## Common misconceptions

- **"Embedding similarity means semantic equivalence."** It means similarity under the training objective; negation, numbers and entity names are often weakly represented.
- **"A vector database makes RAG accurate."** The index only finds what the embedding ranks highly; chunking, the encoder and re-ranking usually matter more than the index.
- **"Approximate search loses too much."** Well-tuned indexes reach 90–99% recall@10 at a small fraction of exact cost, and re-ranking recovers most of the rest.

## Go deeper

- Christopher Manning, Prabhakar Raghavan and Hinrich Schütze, *Introduction to Information Retrieval* (2008): inverted indexes, ranking and retrieval evaluation.
- Hervé Jégou, Matthijs Douze and Cordelia Schmid, "Product Quantization for Nearest Neighbor Search" (2011): PQ and the inverted-file index.
- Yury Malkov and Dmitry Yashunin, "Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs" (2016 preprint; 2020 journal version): HNSW.
- Patrick Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (2020): RAG as a trained system, for Natural Language Processing (NLP) tasks.
