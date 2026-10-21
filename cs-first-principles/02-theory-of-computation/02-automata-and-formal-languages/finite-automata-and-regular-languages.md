# Finite Automata and Regular Languages

> **Layer:** [02 Theory of Computation](../README.md) › [Automata and Formal Languages](README.md)
> **Builds on:** [Sets](../../01-mathematical-foundations/02-sets-relations-functions/sets.md), [Functions and Cardinality](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md), [Proof Techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md)
> **Enables:** [Finite State Machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md), [Lexing and Parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md), [String Matching](../../05-algorithms-and-data-structures/06-string-algorithms/string-matching.md), [Model Checking](../../06-programming-languages/05-formal-methods/model-checking.md)

## Essence

A finite automaton is the simplest model of a computer: a machine with a fixed, finite amount of memory that reads its input once, left to right, and then says yes or no. The set of strings it accepts is a *language*, and the languages that some finite automaton accepts are called *regular*. Three very different descriptions (deterministic automata, nondeterministic automata and regular expressions) turn out to define exactly the same class, which is a sign that the class is natural. The defining limitation is equally clean: a finite machine cannot count without bound, so languages such as "n a's followed by n b's" are out of reach. Everything with bounded memory, from a vending machine controller to a network protocol state machine, lives here.

## Core tenets

1. **A Deterministic Finite Automaton (DFA) is a finite set of states plus a transition function.** Formally M = (Q, Σ, δ, q₀, F): states Q, input alphabet Σ, transition δ: Q × Σ → Q, start state q₀ and accepting states F. It reads one symbol per step and moves to δ(state, symbol). Its only memory is which state it is in, so a machine with k states can remember at most log₂ k bits about the input so far.

2. **Nondeterminism adds convenience, not power.** A Nondeterministic Finite Automaton (NFA) may have several possible next states (or ε-moves that consume no input) and accepts if *any* path accepts. The subset construction simulates it with a DFA whose states are *sets* of NFA states, so every NFA has an equivalent DFA. The price is size: an n-state NFA can require 2ⁿ DFA states (for example, "the n-th symbol from the end is 1").

3. **Regular expressions, NFAs and DFAs are equivalent (Kleene's theorem).** Regular expressions build languages from single symbols using union (|), concatenation and Kleene star (*). Thompson's construction turns any regular expression into an NFA of linear size, and state elimination turns any automaton back into a regular expression. This is why `grep` and lexer generators can compile patterns into fast automata.

4. **Regular languages are closed under the Boolean operations and more.** Union, intersection, complement, concatenation, star and reversal of regular languages are regular. Complement is easy for a DFA (swap accepting and non-accepting states); intersection uses the product construction, running two DFAs in lock-step on pairs of states. Closure lets you prove a language regular by building it from known regular pieces, and is the basis of automata-based verification.

5. **Every regular language has a unique minimal DFA (Myhill–Nerode).** Two strings x and y are equivalent for language L if, for every suffix z, xz ∈ L exactly when yz ∈ L. L is regular if and only if this relation has finitely many classes, and the classes *are* the states of the smallest DFA. Hopcroft's algorithm finds it in O(n log n) time for n states, so two DFAs can be tested for equivalence by minimising both.

6. **The pumping lemma exposes the limit of finite memory.** If L is regular, there is a p (the number of DFA states works) such that every w ∈ L with |w| ≥ p can be split w = xyz with |xy| ≤ p, |y| ≥ 1, and xyⁱz ∈ L for all i ≥ 0. Why: reading p symbols visits p + 1 states, so some state repeats (pigeonhole), and the loop between the repeats can be traversed any number of times. To show {aⁿbⁿ} is not regular, pump inside the a's: the count of a's changes and the count of b's does not.

7. **Membership is fast and decision problems are decidable.** A DFA decides membership in O(n) time with O(1) memory. Emptiness, finiteness, equivalence and inclusion of regular languages are all decidable. This tractability is exactly what disappears as you climb the [Chomsky hierarchy](chomsky-hierarchy.md).

8. **"Regex" in programming languages is often not regular.** Backreferences such as `(a*)b\1` match {aⁿbaⁿ}, which is not regular, and backtracking engines that support them can take exponential time on crafted input (Regular expression Denial of Service, ReDoS). Automaton-based engines (RE2, Rust's `regex`) give linear-time matching by refusing such features.

## Key concepts

| Term | Meaning |
|---|---|
| Alphabet Σ | Finite set of symbols |
| Language | Any set of finite strings over Σ |
| DFA | Exactly one next state per (state, symbol) |
| NFA | Zero or more next states, plus ε-moves; accepts if any path accepts |
| Subset construction | Builds a DFA whose states are sets of NFA states |
| Regular expression | Pattern built from symbols with union, concatenation and star |
| Myhill–Nerode relation | Strings equivalent if no suffix distinguishes them |
| Pumping length p | Threshold beyond which accepted strings contain a repeatable loop |

## How it fits

- **Below:** It needs only [sets](../../01-mathematical-foundations/02-sets-relations-functions/sets.md), [functions](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md), [equivalence relations](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md) and the pigeonhole principle from [combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md). A DFA is a labelled directed [graph](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md).
- **Above:** A synchronous circuit with k flip-flops is a DFA with at most 2ᵏ states ([finite state machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md)). Lexers are DFAs generated from regular expressions ([lexing and parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md)). Knuth–Morris–Pratt and Aho–Corasick are pattern DFAs ([string matching](../../05-algorithms-and-data-structures/06-string-algorithms/string-matching.md)). Protocol specifications such as the Transmission Control Protocol (TCP) connection states are finite automata ([UDP and TCP](../../08-networking/04-transport-layer/udp-and-tcp.md)), and [model checkers](../../06-programming-languages/05-formal-methods/model-checking.md) verify systems by building product automata.
- **Siblings:** Adding a stack gives [pushdown automata](context-free-grammars-and-pushdown-automata.md) and nested structure; the [Chomsky hierarchy](chomsky-hierarchy.md) places regular languages at its bottom level.

## Common misconceptions

- **"NFAs are more powerful than DFAs."** They accept exactly the same languages. They can be exponentially more succinct, which matters for size but not for what is computable.
- **"Every real computer is just a finite automaton, so this is all that matters."** Technically true, but the state count (2 to the number of memory bits) is so vast that finite-automaton reasoning is useless. Models with unbounded memory describe real programs far better.
- **"The pumping lemma proves a language is regular."** It is a necessary condition only. Some non-regular languages satisfy it; use Myhill–Nerode for a complete characterisation.

## Go deeper

- Michael Sipser, *Introduction to the Theory of Computation* (3rd ed., 2012), chapter 1: the clearest modern treatment.
- John E. Hopcroft, Rajeev Motwani and Jeffrey D. Ullman, *Introduction to Automata Theory, Languages, and Computation* (3rd ed., 2006): more constructions and applications.
- Ken Thompson, "Regular Expression Search Algorithm" (1968): regex-to-NFA compilation in four pages.
- Russ Cox, "Regular Expression Matching Can Be Simple And Fast" (2007, web article): why automaton matching beats backtracking.
