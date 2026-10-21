# Context-Free Grammars and Pushdown Automata

> **Layer:** [02 Theory of Computation](../README.md) › [Automata and Formal Languages](README.md)
> **Builds on:** [Finite Automata and Regular Languages](finite-automata-and-regular-languages.md), [Induction and Recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md), [Stacks and Queues](../../05-algorithms-and-data-structures/02-fundamental-data-structures/stacks-and-queues.md)
> **Enables:** [Lexing and Parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md), [Syntax and Semantics](../../06-programming-languages/02-semantics-and-types/syntax-and-semantics.md), [Dynamic Programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md)

## Essence

Context-free grammars describe nested structure: balanced parentheses, expressions, blocks inside blocks. A grammar is a set of rewrite rules such as `E → E + T | T`, each replacing a single symbol regardless of its surroundings (hence "context-free"). The machines that recognise these languages are pushdown automata: finite automata equipped with an unbounded stack, which is exactly the memory needed to match each opener with its closer. This class is where the syntax of nearly every programming language lives, and parsing theory is the engineering of fast, unambiguous recognisers for useful subsets of it.

## Core tenets

1. **A Context-Free Grammar (CFG) generates strings by recursive substitution.** G = (V, Σ, R, S): variables V, terminals Σ, rules R of the form A → α (one variable on the left, any string of variables and terminals on the right) and a start variable S. A derivation rewrites variables until only terminals remain. A single-variable left side means each variable expands independently, so every derivation is a tree.

2. **The parse tree, not the string, carries meaning.** A parse tree shows which rule produced which substring, and compilers attach semantics to tree nodes. A grammar is *ambiguous* if some string has two parse trees: `E → E + E | E * E | n` gives `1 + 2 * 3` two readings. Ambiguity is fixed by stratifying the grammar (expression, term, factor) to encode precedence and associativity. Ambiguity of an arbitrary CFG is undecidable, and some languages are *inherently* ambiguous.

3. **Pushdown Automata (PDA) recognise exactly the context-free languages.** A PDA is a nondeterministic finite automaton that can push and pop symbols on a stack on each move. To simulate a grammar, keep the yet-to-be-matched part of a derivation on the stack; to build a grammar from a PDA, introduce a variable for each "go from state p to state q with net-zero stack change". The stack is the right memory because nested structure is last-opened, first-closed.

4. **Determinism matters here, unlike for finite automata.** Deterministic PDAs recognise a strict subset of context-free languages (CFLs), the deterministic CFLs. Palindromes {wwᴿ} need nondeterminism, because the machine must guess where the middle is. Practical parsers, LL(k) and LR(k) (reading Left to right, building a Leftmost or Rightmost derivation, with k tokens of lookahead), are deterministic and run in linear time, which is why language designers keep grammars within these classes.

5. **Every CFG can be parsed in polynomial time.** Put the grammar in Chomsky Normal Form (rules A → BC or A → a) and the Cocke–Younger–Kasami (CYK) algorithm fills a table of "which variables derive substring i..j" by [dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md) in O(n³) time. Earley's algorithm handles any CFG in O(n³) and is faster on unambiguous grammars (O(n²)) and on most deterministic ones (O(n)). The best known general bound ties to matrix multiplication (Valiant, 1975).

6. **The pumping lemma for CFLs exposes the limit of one stack.** If L is context-free, there is p such that every w ∈ L with |w| ≥ p splits as w = uvxyz with |vxy| ≤ p, |vy| ≥ 1, and uvⁱxyⁱz ∈ L for all i ≥ 0. Why: a long string has a tall parse tree, so some root-to-leaf path repeats a variable, and the subtree between the repeats can be copied or removed. Consequence: {aⁿbⁿcⁿ} is not context-free, because one stack can match two counts but not three.

7. **Closure is weaker than for regular languages.** CFLs are closed under union, concatenation, star and intersection with a regular language, but *not* under intersection or complement: {aⁿbⁿcᵐ} ∩ {aᵐbⁿcⁿ} = {aⁿbⁿcⁿ}. Many questions also become undecidable: whether two CFGs generate the same language, or whether a CFG generates every string, has no algorithm.

8. **Real language syntax is context-free plus checks.** "Every variable is declared before use" and "the call has as many arguments as the function has parameters" are not context-free. Compilers parse with a CFG and enforce such rules later in [semantic analysis](../../06-programming-languages/03-compilers/semantic-analysis.md), using symbol tables.

## Key concepts

| Term | Meaning |
|---|---|
| Production rule | A → α: replace variable A with string α |
| Derivation | Sequence of rule applications from start symbol to terminals |
| Parse tree | Tree recording which rule produced each part of the string |
| Ambiguous grammar | Some string has two distinct parse trees |
| PDA | Finite automaton plus an unbounded stack |
| Deterministic CFL | Language accepted by a deterministic PDA; parseable in linear time |
| Chomsky Normal Form | Every rule is A → BC or A → a |
| LL / LR parsing | Deterministic top-down / bottom-up parsing with k tokens of lookahead |

## How it fits

- **Below:** It extends [finite automata](finite-automata-and-regular-languages.md) with a stack, and its proofs are [structural induction](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) on derivations and trees ([graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md)).
- **Above:** Grammar notation (Backus–Naur Form, BNF) defines programming language syntax ([syntax and semantics](../../06-programming-languages/02-semantics-and-types/syntax-and-semantics.md)), and parser generators build LR or LL parsers from it ([lexing and parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md)). The call stack of a running program is the same structure a PDA uses ([stacks and queues](../../05-algorithms-and-data-structures/02-fundamental-data-structures/stacks-and-queues.md)). Data formats such as JavaScript Object Notation (JSON) and Extensible Markup Language (XML) are context-free, and parsing them with regular expressions is a classic source of [web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md) bugs.
- **Siblings:** [Regular languages](finite-automata-and-regular-languages.md) are the CFLs that need no stack; the [Chomsky hierarchy](chomsky-hierarchy.md) shows what a second stack (or a tape) adds.

## Common misconceptions

- **"Programming languages are context-free."** Their *grammars* are, but the full set of legal programs is not; declaration, typing and scoping rules are checked outside the grammar. C even needs symbol-table feedback while parsing.
- **"A regular expression can parse HyperText Markup Language (HTML) or balanced parentheses."** Pure regular expressions cannot match unbounded nesting; that needs a stack.
- **"Two stacks are just a bigger stack."** Two stacks can simulate a Turing machine's tape (one holds the left half, one the right), so a two-stack PDA is as powerful as any computer.

## Go deeper

- Michael Sipser, *Introduction to the Theory of Computation* (3rd ed., 2012), chapter 2: CFGs, PDAs and the pumping lemma.
- Alfred V. Aho, Monica S. Lam, Ravi Sethi and Jeffrey D. Ullman, *Compilers: Principles, Techniques, and Tools* (2nd ed., 2006), chapter 4: LL and LR parsing in practice.
