# Automata and Formal Languages

> **Layer:** [02 Theory of Computation](../README.md) › Automata and Formal Languages
> **Children:** [Finite Automata and Regular Languages](finite-automata-and-regular-languages.md) · [Context-Free Grammars and Pushdown Automata](context-free-grammars-and-pushdown-automata.md) · [The Chomsky Hierarchy](chomsky-hierarchy.md)

## What this area is about

This area asks: **what can a machine with a given kind of memory recognise?** It turns every computational problem into a question about a *language*, a set of strings (the inputs whose answer is "yes"), and then studies which machines can decide membership. The unifying idea is that the *form of memory* determines the *form of structure* a machine can handle. Finite memory handles patterns that repeat but do not nest. A stack handles nesting. An unbounded read-write tape handles everything computable.

Each machine model also has a matching *generative* description: regular expressions for finite automata, context-free grammars for pushdown automata, unrestricted grammars for Turing machines. Having two views of the same class (one that recognises, one that generates) is what makes this theory practical. Engineers write the generative form (a regular expression, a grammar) and a tool compiles it into the recognising machine (a lexer, a parser).

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Finite Automata and Regular Languages](finite-automata-and-regular-languages.md) | Bounded memory: deterministic and nondeterministic finite automata (DFAs, NFAs), regular expressions, pumping lemma | Sets, functions, pigeonhole |
| [Context-Free Grammars and Pushdown Automata](context-free-grammars-and-pushdown-automata.md) | One stack: nested structure, parsing, the context-free pumping lemma | Finite automata, induction |
| [The Chomsky Hierarchy](chomsky-hierarchy.md) | The ladder that relates all levels, up to Turing machines | Both of the above |

Read in order. Each step adds memory and shows, with a pumping argument, what the previous level could not do.

```
  memory:     finite        + one stack        + linear tape        + unbounded tape
  machine:    DFA / NFA  ->  pushdown       ->  linear-bounded   ->  Turing machine
  grammar:    regular    ->  context-free   ->  context-sensitive ->  unrestricted
  example:    (ab)*         a^n b^n            a^n b^n c^n          halting language
  membership: O(n)          O(n^3)             PSPACE-complete      undecidable
  (PSPACE = problems solvable with polynomial memory)
```

The pattern to carry away: each extra unit of memory power makes more languages expressible and fewer questions answerable. Equivalence of two DFAs is decidable in near-linear time; equivalence of two context-free grammars is undecidable; and for Turing machines even "does it accept this input?" has no algorithm.

## Connections to sibling areas

- **[Information Theory](../01-information-theory/README.md):** Finite-state sources (Markov chains) are automata with probabilities, and their entropy rate is computable from the transition matrix. Prefix codes are decoded by walking a code tree, which is a finite automaton.
- **[Computability](../03-computability/README.md):** The top of the hierarchy *is* computability. Turing machines generalise pushdown automata by replacing the stack with a tape, and the undecidability results there explain why decision problems fail for grammars here.
- **[Complexity](../04-complexity/README.md):** Grammar classes line up with complexity classes: regular languages need constant space, context-sensitive languages are exactly nondeterministic linear space, and parsing algorithms are studied for their time bounds.
- **[Quantum Computation](../05-quantum-computation/README.md):** Quantum finite automata exist and can be exponentially more succinct for some languages, but one-way quantum automata with bounded error recognise only regular languages: finite quantum memory does not escape the finite-memory limit.

## Connections across layers

From [mathematical foundations](../../01-mathematical-foundations/README.md) it takes [sets](../../01-mathematical-foundations/02-sets-relations-functions/sets.md), [equivalence relations](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md), [graphs](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md) and [induction](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md).

It gives a lot upward. Finite automata become hardware [finite state machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md) and controllers. Regular expressions and grammars drive [lexing and parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md). Automata-based algorithms do [string matching](../../05-algorithms-and-data-structures/06-string-algorithms/string-matching.md). Product automata underlie [model checking](../../06-programming-languages/05-formal-methods/model-checking.md). Protocol state machines appear throughout [networking](../../08-networking/04-transport-layer/udp-and-tcp.md). Parsing untrusted input with the weakest sufficient language class is a defence in [web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md).

## Cross-cutting threads

- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): pumping lemmas prove what bounded memory cannot do.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): turning problems into languages over an alphabet is the representation step all of theory relies on.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): expressive power against decidability and parsing speed.
- [Recursion and self-reference](../../CROSS-CUTTING.md#recursion-and-self-reference): context-free rules are recursive definitions, and stacks are how recursion is executed.
- [Composition](../../CROSS-CUTTING.md#composition): product and subset constructions combine automata with predictable results.
