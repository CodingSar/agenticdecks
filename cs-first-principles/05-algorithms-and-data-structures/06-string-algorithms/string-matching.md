# String Matching

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [String Algorithms](README.md)
> **Builds on:** [Finite Automata and Regular Languages](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md), [Hash Tables](../02-fundamental-data-structures/hash-tables.md), [Dynamic Programming](../03-design-paradigms/dynamic-programming.md), [Amortized Analysis](../01-foundations/amortized-analysis.md)
> **Enables:** [Lexing and Parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md), [Network Attacks and Defenses](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md), [Version Control](../../12-software-engineering/02-process/version-control.md), [Tries and Suffix Structures](tries-and-suffix-structures.md)

## Essence

String matching finds every position where a pattern P of length m occurs in a text T of length n. The naive method tries each alignment and compares character by character, costing O(nm) in the worst case. The better algorithms avoid re-reading text characters whose relationship to the pattern is already known. Knuth–Morris–Pratt (KMP) precomputes how the pattern overlaps itself and runs in Θ(n + m) worst case. Boyer–Moore compares from the pattern's right end and skips ahead, often reading only a fraction of the text. Rabin–Karp compares hashes instead of strings, and extends naturally to many patterns. Aho–Corasick matches a whole dictionary of patterns in one pass. Approximate matching, where errors are allowed, uses dynamic programming (edit distance).

## Core tenets

1. **Naive matching wastes information.** On text `aaaaaaaa…b` and pattern `aaaab`, the naive algorithm matches four characters, fails, shifts by one, and re-compares three characters it already knows match. That redundancy is what gives O(nm). Every faster algorithm is a way of recording what a mismatch teaches you about the next possible alignment.

2. **KMP's failure function encodes how the pattern overlaps itself.** For each prefix P[0..j), compute π[j], the length of the longest proper prefix of P that is also a suffix of that prefix. On a mismatch after matching j characters, the pattern can shift so that the first π[j] characters are already aligned, and the text pointer never moves backwards. Each text character causes at most one forward step and the pattern pointer can only fall back as far as it has advanced, so the total is at most 2n comparisons: Θ(n) matching after Θ(m) preprocessing.

3. **KMP is a deterministic finite automaton for "text ends with P".** The states are 0..m (how much of P is currently matched), and the failure function defines transitions. Matching is then a single left-to-right walk with no backtracking, which suits streams. This is why string matching, regular-expression engines and [lexers](../../06-programming-languages/03-compilers/lexing-and-parsing.md) are all [finite automata](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md) underneath.

4. **Boyer–Moore is sublinear in practice by skipping.** It aligns the pattern and compares right to left. On a mismatch at text character c, the *bad-character rule* shifts the pattern to align c with its last occurrence in P (or past it entirely if c is absent); the *good-suffix rule* uses the matched suffix like KMP in reverse. With a large alphabet and a long pattern, most alignments fail on the first comparison and shift by nearly m, so it reads about n/m characters. That is why `grep` and similar tools use Boyer–Moore variants (often the simplified Horspool version).

5. **Rabin–Karp turns string comparison into number comparison.** Treat each length-m window as a number in base b modulo a prime p. A *rolling hash* updates the window's hash in O(1) when it slides by one: subtract the outgoing character's contribution, multiply by b, add the incoming one. Compare hashes; only on a hash match compare characters. Expected time is O(n + m) with a random prime or base, worst case O(nm) under many false matches. Its strength is that it extends easily to many patterns of equal length (put their hashes in a set) and to two-dimensional matching and plagiarism detection.

6. **Aho–Corasick matches many patterns in one pass.** Build a trie of all patterns, then add failure links (the multi-pattern generalisation of KMP's π) so every node points to the longest proper suffix that is also a trie path. Scanning the text once costs O(n + total pattern length + number of matches). Intrusion detection systems and antivirus scanners use it to search for thousands of signatures simultaneously.

7. **Approximate matching is dynamic programming.** The edit (Levenshtein) distance between two strings is the minimum number of insertions, deletions and substitutions to turn one into the other. Let D[i][j] be the distance between the first i characters of A and the first j of B; D[i][j] = min(D[i−1][j] + 1, D[i][j−1] + 1, D[i−1][j−1] + [A_i ≠ B_j]). That is Θ(nm) time. Under the Strong Exponential Time Hypothesis, no algorithm achieves O((nm)^(1−ε)) (Backurs and Indyk, 2015), so faster tools rely on bounded distance, bit-parallelism or heuristics, as in sequence aligners and `diff`.

8. **Regular expressions are a different, harder problem.** A true regular expression compiles to a finite automaton and can be matched in O(nm) time by simulating the nondeterministic automaton (Thompson, 1968). Many popular engines instead use backtracking to support features like backreferences, which are not regular; their worst case is exponential, enabling Regular-expression Denial of Service (ReDoS) attacks with patterns like `(a+)+b`.

## Key concepts

| Term | Meaning |
|---|---|
| Alignment (shift) | Position in the text where the pattern is currently placed |
| Failure (prefix) function π | Longest proper prefix of P[0..j) that is also its suffix |
| Bad-character rule | Boyer–Moore shift based on the mismatched text character |
| Rolling hash | Hash of a sliding window updated in O(1) per step |
| Aho–Corasick automaton | Trie of patterns plus failure links for multi-pattern matching |
| Edit (Levenshtein) distance | Minimum insertions, deletions and substitutions between two strings |
| Thompson construction | Translation of a regular expression into a nondeterministic automaton |
| Catastrophic backtracking | Exponential blow-up of backtracking regex engines on certain patterns |

## How it fits

- **Below:** theory of [finite automata](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md); hashing and [modular arithmetic](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md); [character encoding](../../03-digital-logic/01-number-representation/character-encoding.md) (matching Unicode Transformation Format 8-bit (UTF-8) bytes vs code points).
- **Above:** [lexers](../../06-programming-languages/03-compilers/lexing-and-parsing.md), search tools, [intrusion detection](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md), input validation in [web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md), [diff and merge](../../12-software-engineering/02-process/version-control.md), deduplication in [storage](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md) (content-defined chunking uses rolling hashes).
- **Siblings:** [tries and suffix structures](tries-and-suffix-structures.md) preprocess the text instead of the pattern, which wins when one text is searched many times.

## Common misconceptions

- **"Boyer–Moore is always faster than KMP."** It shines with long patterns and large alphabets; for short patterns or small alphabets (such as DNA's four letters), its skips are small.
- **"Regular expression matching is linear."** It is linear for automaton-based engines (RE2, Rust's regex); backtracking engines can be exponential.
- **"Hash equality means string equality."** Rabin–Karp must verify candidate matches, or accept a small probability of false positives.

## Go deeper

- Donald Knuth, James Morris, Vaughan Pratt, "Fast Pattern Matching in Strings" (1977).
- Robert S. Boyer and J Strother Moore, "A Fast String Searching Algorithm" (1977).
- Dan Gusfield, *Algorithms on Strings, Trees, and Sequences* (1997): the standard reference, with biological applications.
- Russ Cox, "Regular Expression Matching Can Be Simple And Fast" (2007): automata versus backtracking in practice.
