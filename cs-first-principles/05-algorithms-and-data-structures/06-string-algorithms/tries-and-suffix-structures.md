# Tries and Suffix Structures

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [String Algorithms](README.md)
> **Builds on:** [Search Trees](../02-fundamental-data-structures/search-trees.md), [Non-Comparison Sorting](../04-sorting-and-searching/non-comparison-sorting.md), [String Matching](string-matching.md), [Source Coding and Compression](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md)
> **Enables:** [IP Addressing and Forwarding](../../08-networking/03-network-layer/ip-addressing-and-forwarding.md), [Large Language Models](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md), [Storage Layouts](../../09-data-management/02-storage-and-indexing/storage-layouts.md)

## Essence

A trie (prefix tree) stores a set of strings by sharing common prefixes: each edge is labelled by a character, and each key is a root-to-node path. Looking up a key of length m takes O(m) steps regardless of how many keys are stored, and all keys with a given prefix sit in one subtree. A *suffix tree* is a compressed trie of all suffixes of a text, and it turns every substring question ("does P occur? how often? what is the longest repeated substring?") into a walk from the root, after O(n) preprocessing. A *suffix array* is the sorted list of suffix start positions, a smaller and more cache-friendly alternative. The Burrows–Wheeler Transform (BWT) rearranges a text using the same sorted order, and it is both the core of bzip2 compression and of compressed full-text indexes used in genome sequencing.

## Core tenets

1. **A trie branches on characters, not comparisons.** At each node you follow the child for the next character of the key, so lookup costs O(m) for a key of length m, independent of the number of keys n. A balanced search tree of strings needs O(log n) string comparisons, each up to O(m). Tries therefore win for many keys with shared prefixes, and they support prefix queries (autocomplete, all keys starting with "inter") naturally.

2. **Plain tries waste space; compression fixes it.** A node with an array of child pointers for a 256-symbol alphabet is mostly empty. Remedies: *compressed (radix, Patricia) tries* merge chains of single-child nodes into one edge labelled by a string, so the node count is O(n) for n keys; child sets are stored as sorted arrays, hash maps or bitmaps; *ternary search trees* use a small binary tree at each node. Adaptive radix trees choose a node layout by fan-out and are used as in-memory database indexes.

3. **Longest-prefix match is the trie's killer application in networking.** An Internet Protocol (IP) router must find the most specific routing-table entry (the longest prefix) matching each destination address, millions of times per second. A binary trie on address bits answers this by walking the address and remembering the last node that held a route. Multi-bit tries, compressed tries and hardware Ternary Content-Addressable Memory (TCAM) make it fast enough for line rate.

4. **A suffix tree indexes every substring of a text in linear space.** Every substring of T is a prefix of some suffix, so a compressed trie of all n suffixes contains every substring as a path. It has at most 2n nodes, with edge labels stored as (start, end) pointers into T. Weiner (1973), McCreight (1976) and Ukkonen (1995) showed it can be built in O(n) time for a constant alphabet. Then pattern search costs O(m + occurrences), and longest repeated substring, longest common substring of two strings and many other problems become linear.

5. **Suffix arrays trade a log factor for a large constant-factor saving in space.** A suffix array is just the n suffix start positions sorted lexicographically: 4 or 8 bytes per character versus 10–20 or more for a suffix tree. Searching for P is binary search over suffixes: O(m log n), or O(m + log n) with an auxiliary Longest Common Prefix (LCP) array. Construction is O(n) with skew/DC3 (Kärkkäinen and Sanders, 2003) or SA-IS (Nong, Zhang and Chan, 2009), using radix-sort ideas. Suffix array plus LCP array can simulate most suffix-tree algorithms.

6. **The Burrows–Wheeler Transform makes a text both compressible and searchable.** Sort all rotations of T and output the last column. Characters that precede similar contexts end up adjacent, producing long runs that compress well (bzip2 uses this). The transform is reversible from the last column alone via the LF-mapping. Adding small rank tables gives the FM-index (named for Ferragina and Manzini, 2000), which counts pattern occurrences in O(m) time using space close to the compressed size of the text. Genome read aligners such as the Burrows–Wheeler Aligner (BWA) and Bowtie are built on it.

7. **Tries organise vocabularies for tokenizers and autocomplete.** Language-model tokenizers find the longest vocabulary match at each position, a trie walk. Search engines' term dictionaries and spelling correctors often use tries or their minimised form (finite-state transducers), sharing both prefixes and suffixes.

8. **Theory and practice diverge on memory.** Suffix trees have optimal O(n) time but pointer-heavy nodes that thrash caches and can exhaust Random-Access Memory (RAM) for gigabyte texts. Suffix arrays, compressed tries and FM-indexes are usually preferred in practice, not for better asymptotics but because they fit in memory and scan sequentially.

## Key concepts

| Term | Meaning |
|---|---|
| Trie | Tree whose root-to-node paths spell keys, one character per edge |
| Compressed (radix / Patricia) trie | Trie with single-child chains merged into string-labelled edges |
| Longest-prefix match | Find the stored key that is the longest prefix of a query |
| Suffix tree | Compressed trie of all suffixes of a text; O(n) nodes |
| Suffix array | Suffix start positions sorted lexicographically |
| LCP array | Length of the longest common prefix of adjacent suffixes in the suffix array |
| BWT | Last column of the sorted rotations of a text; reversible and compressible |
| FM-index | Compressed text index based on the BWT supporting fast pattern counting |

## How it fits

- **Below:** tries are [search trees](../02-fundamental-data-structures/search-trees.md) branching on digits, the same idea as most-significant-digit [radix sort](../04-sorting-and-searching/non-comparison-sorting.md); the BWT connects to [source coding](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md).
- **Above:** [IP forwarding](../../08-networking/03-network-layer/ip-addressing-and-forwarding.md); [tokenizers](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md); in-memory [database indexes](../../09-data-management/02-storage-and-indexing/storage-layouts.md); full-text search; [Domain Name System (DNS)](../../08-networking/05-application-layer/naming-and-dns.md) name lookup structures; genome assembly and alignment.
- **Siblings:** [string matching](string-matching.md) preprocesses the pattern; this file preprocesses the text or key set. Aho–Corasick sits between them: it is a trie of patterns with Knuth–Morris–Pratt style failure links.

## Common misconceptions

- **"Tries are always faster than hash tables."** Hash lookup is also O(m) to hash the key, usually with better cache behaviour; tries win when you need prefix queries or ordered traversal.
- **"Suffix trees are the practical choice for big texts."** Their memory footprint makes suffix arrays or FM-indexes the usual choice.
- **"The BWT is a compression algorithm."** It is a reversible permutation that makes text easier to compress; the compression comes from later stages (move-to-front, run-length and entropy coding).

## Go deeper

- Dan Gusfield, *Algorithms on Strings, Trees, and Sequences* (1997): suffix trees and their applications.
- Udi Manber and Gene Myers, "Suffix Arrays: A New Method for On-Line String Searches" (1993).
- Michael Burrows and David Wheeler, "A Block-sorting Lossless Data Compression Algorithm" (1994).
- Paolo Ferragina and Giovanni Manzini, "Opportunistic Data Structures with Applications" (2000): the FM-index.
