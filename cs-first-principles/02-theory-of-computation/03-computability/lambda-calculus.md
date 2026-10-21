# Lambda Calculus

> **Layer:** [02 Theory of Computation](../README.md) › [Computability](README.md)
> **Builds on:** [Functions and Cardinality](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md), [Predicate Logic](../../01-mathematical-foundations/01-logic/predicate-logic.md), [Induction and Recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md)
> **Enables:** [Functional Programming](../../06-programming-languages/01-paradigms/functional.md), [Binding, Scope and Closures](../../06-programming-languages/02-semantics-and-types/binding-scope-and-closures.md), [Type Systems](../../06-programming-languages/02-semantics-and-types/type-systems.md), [Proof Assistants and Dependent Types](../../06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md)

## Essence

The lambda calculus, introduced by Alonzo Church in the early 1930s, is a model of computation with only three constructs: variables, function definition and function application. Computation is substitution: applying `(λx. body)` to an argument replaces x in the body with that argument. There are no numbers, Booleans, loops or memory cells, yet all of them can be encoded as functions, and the calculus computes exactly the same functions as [Turing machines](turing-machines.md). Where a Turing machine is the blueprint of hardware, the lambda calculus is the blueprint of programming languages: its ideas of binding, scope, higher-order functions and types underlie every modern language.

## Core tenets

1. **Three forms of term are enough.** A term is a variable `x`, an abstraction `λx. M` (a function with parameter x and body M), or an application `M N`. That is the entire syntax. Functions are anonymous and take one argument; several arguments are handled by currying, `λx. λy. M`, a function that returns a function.

2. **Computation is beta-reduction.** The single rule `(λx. M) N → M[x := N]` replaces every free x in M with N. A term with no reducible part is in *normal form*, and that normal form is the result. Alpha-conversion (renaming bound variables, `λx. x` = `λy. y`) is needed so substitution never captures a free variable by accident, which is the formal root of lexical scoping.

3. **Data is encoded as behaviour.** Church numerals represent n as "apply f n times": `0 = λf. λx. x`, `2 = λf. λx. f (f x)`. Booleans are selectors: `true = λa. λb. a`, `false = λa. λb. b`, so `if c then t else e` is just `c t e`. Pairs, lists and arithmetic follow. The lesson is that functions alone can represent any finite structure.

4. **Recursion comes from self-application.** There is no way to name a function inside its own body, but the fixed-point combinator `Y = λf. (λx. f (x x)) (λx. f (x x))` satisfies `Y g = g (Y g)`. So `Y` turns a non-recursive "one step" function into a recursive one. Self-application `(x x)` is also what allows non-termination: `Ω = (λx. x x)(λx. x x)` reduces to itself forever.

5. **The result does not depend on evaluation order (Church–Rosser).** If a term reduces to two different terms, both can be reduced further to a common term. Consequently a term has at most one normal form. Order still matters for *whether* you find it: normal-order (leftmost-outermost first, like lazy evaluation) finds a normal form whenever one exists, while applicative order (arguments first, like strict evaluation) can loop on `(λx. y) Ω`.

6. **It is exactly as powerful as Turing machines.** Turing proved in 1937 that lambda-definable functions and Turing-computable functions coincide. Church and Turing independently used their models to show the Entscheidungsproblem (deciding the truth of first-order logic statements) unsolvable; Church used the undecidability of whether a lambda term has a normal form. That two unrelated definitions agree is a pillar of the [Church–Turing thesis](church-turing-thesis.md).

7. **Adding types trades power for guarantees.** In the simply typed lambda calculus every term terminates (strong normalisation), so it is *not* Turing complete; general recursion must be added explicitly. Richer type systems (System F, dependent types) keep termination while expressing more. Under the Curry–Howard correspondence, types are logical propositions and well-typed terms are proofs, which is how proof assistants such as Coq (now Rocq) and Lean work.

## Key concepts

| Term | Meaning |
|---|---|
| Abstraction λx. M | Anonymous function with parameter x and body M |
| Application M N | Calling function M on argument N |
| Free / bound variable | Bound if introduced by an enclosing λ; free otherwise |
| Beta-reduction | (λx. M) N → M with N substituted for x |
| Alpha-equivalence | Terms equal up to renaming bound variables |
| Normal form | A term with no remaining beta-redex |
| Currying | Representing a multi-argument function as nested one-argument functions |
| Y combinator | Term giving fixed points, hence recursion without names |
| Curry–Howard | Types correspond to propositions, programs to proofs |

## How it fits

- **Below:** It is a formal system of [functions](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md) with variable binding as in [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md); properties are proved by structural [induction](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) on terms.
- **Above:** Lisp (1958), ML, Haskell and every language with closures descend from it ([functional programming](../../06-programming-languages/01-paradigms/functional.md)). Its substitution rules define [binding, scope and closures](../../06-programming-languages/02-semantics-and-types/binding-scope-and-closures.md). Typed lambda calculi are the core of [type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md), [type inference](../../06-programming-languages/02-semantics-and-types/polymorphism-and-type-inference.md) and [proof assistants](../../06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md). Compilers for functional languages use lambda-based [intermediate representations](../../06-programming-languages/03-compilers/intermediate-representations.md).
- **Siblings:** [Turing machines](turing-machines.md) model computation as state change on a tape; the lambda calculus models it as expression rewriting. The [Church–Turing thesis](church-turing-thesis.md) rests on their equivalence, and the [halting problem](halting-problem-and-undecidability.md) has a lambda version (no term decides whether a term has a normal form).

## Common misconceptions

- **"Lambda calculus is about Greek-letter syntax in programming languages."** Lambda expressions in Python or Java borrow the name; the calculus is a complete model of computation, and their closures are its semantics.
- **"Pure functional means it cannot loop."** The untyped calculus is Turing complete and can diverge (Ω). Only typed variants without general recursion guarantee termination.
- **"Evaluation order changes the answer."** Church–Rosser guarantees the normal form is unique; order only affects whether evaluation terminates and how much work it does.

## Go deeper

- Alonzo Church, "An Unsolvable Problem of Elementary Number Theory" (1936): the first undecidability result, via lambda-definability.
- Henk Barendregt, *The Lambda Calculus: Its Syntax and Semantics* (1984): the definitive reference.
- Benjamin C. Pierce, *Types and Programming Languages* (2002), chapters 5–12: untyped and simply typed lambda calculus for programmers.
- Philip Wadler, "Propositions as Types" (2015): readable history of Curry–Howard.
