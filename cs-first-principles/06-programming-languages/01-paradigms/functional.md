# Functional Programming

> **Layer:** [06 Programming Languages](../README.md) › [Paradigms](README.md)
> **Builds on:** [Lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md), [Functions and cardinality](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md), [Induction and recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md)
> **Enables:** [Polymorphism and type inference](../02-semantics-and-types/polymorphism-and-type-inference.md), [Proof assistants and dependent types](../05-formal-methods/proof-assistants-and-dependent-types.md), [Batch and stream processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md)

## Essence

Functional programming treats a program as an expression to be evaluated rather than a list of commands to execute. Functions are values: they can be passed as arguments, returned as results and stored in data structures. In the pure form, functions have no side effects, so calling a function with the same arguments always gives the same result, and any expression can be replaced by its value without changing the program's meaning. The paradigm descends directly from Church's [lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md) (1930s), through Lisp (1958), ML (1970s) and Haskell (1990). The single idea is **referential transparency**: when nothing changes behind your back, programs can be reasoned about with ordinary algebra.

## Core tenets

1. **Referential transparency makes equational reasoning valid.** If `f(x)` has no side effects, `f(x) + f(x)` equals `2 * f(x)`, and a compiler or a human may rewrite one into the other. In imperative code this rewrite is wrong whenever `f` prints, mutates or reads changing state. Purity is what lets functional programs be proved, refactored and optimised by substitution.
2. **Higher-order functions replace control structures.** Loops become `map`, `filter` and `fold`; callbacks, strategies and iterators become function arguments. A single `fold` captures every "walk a list and accumulate" loop, so the pattern is written and verified once.

   ```haskell
   sum     = foldr (+) 0
   product = foldr (*) 1
   length  = foldr (\_ n -> n + 1) 0
   ```

3. **Immutable data is shared, not copied.** Updating a persistent data structure creates a new version that reuses most of the old one; a balanced tree update copies only the O(log n) nodes on the path to the change. Old versions remain valid, which gives cheap undo, snapshots and safe sharing between threads.
4. **Recursion replaces iteration, and tail calls make it cheap.** A function that calls itself as its very last action (a tail call) needs no new stack frame, so a tail-recursive function runs in constant stack space like a loop. Scheme requires this optimisation; many languages, including Java and Python, do not perform it.
5. **Algebraic data types and pattern matching make data shape explicit.** A type is defined as a sum of alternatives, each a product of fields (`data Shape = Circle Double | Rect Double Double`). Pattern matching takes values apart by case, and the compiler can check that every case is handled. This is why "null pointer" errors are rare in ML-family languages: absence is a case (`Option`/`Maybe`) that must be matched.
6. **Effects are made explicit rather than banned.** Real programs must do input and output. Pure languages represent effects as values: Haskell's `IO` type describes an action that the runtime will perform, and monads sequence such actions. Impure functional languages (OCaml, Clojure, Scala) allow effects but make immutability the default.
7. **Evaluation strategy is a real design choice.** Strict (eager) evaluation computes arguments before the call, which is predictable in time and space. Lazy evaluation computes a value only when needed, enabling infinite structures and reuse of results, but making memory use hard to predict. By the Church–Rosser property, if both strategies reach a normal form they reach the same one; laziness terminates in some cases where strictness does not.
8. **Purity makes parallelism safe.** Expressions with no shared mutable state cannot race. That is why `map` over a large dataset parallelises trivially, and why the MapReduce model (Dean and Ghemawat, 2004) is named after two functional primitives.

## Key concepts

| Term | Meaning |
|---|---|
| Pure function | A function whose result depends only on its arguments and that has no side effects |
| Referential transparency | Any expression can be replaced by its value without changing program behaviour |
| First-class function | A function that can be passed, returned and stored like any other value |
| Higher-order function | A function that takes or returns functions (`map`, `fold`, `compose`) |
| Closure | A function value together with the variables it captured from its defining scope |
| Algebraic data type | A type built from sums (alternatives) and products (tuples/records) |
| Persistent data structure | A structure whose updates produce new versions while keeping old ones valid |
| Tail call | A call in final position, which can reuse the caller's stack frame |
| Monad | A structure for sequencing computations that carry an effect (state, failure, input/output) |

## How it fits

- **Below:** The [lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md) gives the core model (abstraction, application, substitution). Mathematical [functions](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md) give the intuition, and [structural induction](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) is how recursive functions are proved correct.
- **Above:** Functional ideas power data pipelines in [batch and stream processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md), conflict-free data types in [eventual consistency](../../10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md), and the dependently typed languages of [proof assistants](../05-formal-methods/proof-assistants-and-dependent-types.md).
- **Siblings:** Compared with [imperative](imperative-and-procedural.md) programming, it removes assignment; compared with [object-oriented](object-oriented.md) programming, it organises code around operations over data types rather than around stateful objects. [Logic programming](logic-and-declarative.md) goes one step further, from functions to relations.

## Common misconceptions

- **"Functional programs are slow because they copy everything."** Persistent structures share almost everything, and optimising compilers (the Glasgow Haskell Compiler, OCaml) turn many recursive functions into tight loops. Allocation is heavy, but generational garbage collectors make short-lived allocation cheap.
- **"Functional means no state."** State exists; it is passed explicitly (as arguments and results) or isolated in a typed effect, rather than hidden in shared variables.
- **"You need category theory to use monads."** A monad is just a pattern for chaining steps that each may carry an effect; the theory is optional.

## Go deeper

- Harold Abelson and Gerald Jay Sussman, *Structure and Interpretation of Computer Programs* (2nd ed., 1996): functional thinking from first principles in Scheme.
- John Backus, "Can Programming Be Liberated from the von Neumann Style?" (1978 Turing Award lecture): the classic case for function-level programming.
- John Hughes, "Why Functional Programming Matters" (1989): higher-order functions and laziness as tools for modularity.
- Chris Okasaki, *Purely Functional Data Structures* (1998): how immutable structures achieve good asymptotic bounds.
