# String Algorithms

> **Layer:** [05 Algorithms and Data Structures](../README.md) › String Algorithms
> **Children:** [String Matching](string-matching.md) · [Tries and Suffix Structures](tries-and-suffix-structures.md)

## What this area is about

Strings (sequences over an alphabet) are how computers hold text, source code, genomes, network payloads and logs. This area answers two questions. *Where does a pattern occur in a text?* (string matching), and *how should I preprocess a text or a set of keys so that many later queries are fast?* (tries and suffix structures). The naive answers are quadratic or worse; the good ones are linear in the size of the input or the output.

The unifying idea is **never re-examine what you already know**. A naive matcher that fails after matching 10 characters slides the pattern one step and re-compares characters it has already seen. Knuth–Morris–Pratt (KMP) precomputes how the pattern overlaps itself so the text pointer never moves backwards. Suffix trees and suffix arrays push the same idea to the text side: preprocess the text once in linear time, then answer any substring query in time proportional to the pattern. The choice between the two children is whether to preprocess the pattern or the text.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [String Matching](string-matching.md) | Find occurrences of a pattern in a text: naive, Knuth–Morris–Pratt, Boyer–Moore, Rabin–Karp, Aho–Corasick, edit distance | [Finite automata](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md), [hashing](../02-fundamental-data-structures/hash-tables.md), [dynamic programming](../03-design-paradigms/dynamic-programming.md) |
| [Tries and Suffix Structures](tries-and-suffix-structures.md) | Index a key set or a whole text for fast repeated queries: tries, suffix trees, suffix arrays, the Burrows–Wheeler transform | [Search trees](../02-fundamental-data-structures/search-trees.md), [non-comparison sorting](../04-sorting-and-searching/non-comparison-sorting.md), string matching |

```
   preprocess the PATTERN (size m)          preprocess the TEXT (size n)
   ───────────────────────────────          ────────────────────────────
   KMP / automaton:  O(m) + O(n) per text   suffix tree / array: O(n) once
   Aho–Corasick: many patterns at once      then each query O(m + occurrences)
   good for: one search, streaming text     good for: many searches, fixed text
```

Read string matching first: its failure-function idea reappears in Aho–Corasick, which builds a trie of patterns, and that trie leads into the second file.

## Connections to sibling areas

- **[Foundations](../01-foundations/README.md):** Knuth–Morris–Pratt's linear time is an amortized argument; suffix-array construction proofs rest on invariants about sorted prefixes.
- **[Fundamental Data Structures](../02-fundamental-data-structures/README.md):** tries are search trees keyed by characters; Rabin–Karp is a rolling hash table lookup.
- **[Design Paradigms](../03-design-paradigms/README.md):** edit distance and sequence alignment are dynamic programming; Rabin–Karp is randomized; suffix-array construction by difference cover (DC3) is divide and conquer.
- **[Sorting and Searching](../04-sorting-and-searching/README.md):** a suffix array is the sorted list of suffixes, built with radix-sort ideas and searched with binary search.
- **[Graph Algorithms](../05-graph-algorithms/README.md):** automata and tries are graphs; de Bruijn graphs assemble genomes from overlapping reads.
- **[Advanced Topics](../07-advanced-topics/README.md):** compressed indexes (the Ferragina–Manzini, or FM, index) and streaming pattern matching push string algorithms into small space.

## Connections across layers

String matching is [finite-automata](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md) theory made efficient; the Burrows–Wheeler transform links indexing to [compression](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md); [character encoding](../../03-digital-logic/01-number-representation/character-encoding.md) decides what a "character" is (bytes vs Unicode code points). Above, these algorithms run in [lexers](../../06-programming-languages/03-compilers/lexing-and-parsing.md), `grep` and search engines, [intrusion detection](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md) (multi-pattern matching on packets), [Internet Protocol (IP) forwarding](../../08-networking/03-network-layer/ip-addressing-and-forwarding.md) (longest-prefix match in tries), [diff](../../12-software-engineering/02-process/version-control.md), and the tokenizers of [language models](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md).

## Cross-cutting threads

- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): pay to preprocess once, answer many queries fast.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): suffix arrays and the Burrows–Wheeler transform show that a clever representation of a text is both an index and a compressor.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): suffix trees are fast but take 10–20 bytes per character; suffix arrays and FM indexes trade speed for space.
- [Recursion and self-reference](../../CROSS-CUTTING.md#recursion-and-self-reference): the failure function describes how a pattern matches itself.
