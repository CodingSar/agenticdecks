# Type Systems

> **Layer:** [06 Programming Languages](../README.md) › [Semantics and Types](README.md)
> **Builds on:** [Syntax and semantics](syntax-and-semantics.md), [Propositional logic](../../01-mathematical-foundations/01-logic/propositional-logic.md), [Halting problem and undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md)
> **Enables:** [Polymorphism and type inference](polymorphism-and-type-inference.md), [Memory-safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md), [Proof assistants and dependent types](../05-formal-methods/proof-assistants-and-dependent-types.md)

## Essence

A type system is a set of rules that assigns a type to each expression in a program and rejects programs whose parts do not fit together. Pierce's definition is the right mental model: "a tractable syntactic method for proving the absence of certain program behaviors by classifying phrases according to the kinds of values they compute." It is a lightweight, automatic proof system that runs on every program, every time it is compiled. The central property is **soundness**: if the checker accepts a program, the program cannot go wrong in the ways the type system rules out, such as adding a string to a function or reading a field that does not exist. Because exact checking is undecidable, every useful type system must be conservative and reject some programs that would actually have run fine.

## Core tenets

1. **A type system is a static approximation of run-time behaviour.** By [Rice's theorem](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), no algorithm decides any non-trivial property of every program. A type checker therefore reasons about *kinds* of values, not exact values, and is always decidable by design. The price is that `if (false) { "a" * 2 }` is rejected even though the bad branch never runs.
2. **Typing rules are inference rules over syntax.** Each construct has a rule saying how the type of the whole follows from the types of the parts. For example:

   ```
   Γ ⊢ e1 : bool    Γ ⊢ e2 : T    Γ ⊢ e3 : T
   ------------------------------------------
        Γ ⊢ if e1 then e2 else e3 : T
   ```

   Here Γ (the typing context) maps variables to types. Because the rules follow the grammar, checking is a single recursive walk over the syntax tree.
3. **Soundness means "well-typed programs do not go wrong" (Milner, 1978), and it is proved by progress and preservation.** *Progress:* a well-typed program is either a value or can take another step. *Preservation:* taking a step keeps the type. Together they show a well-typed program never reaches a stuck state such as applying a number as a function (Wright and Felleisen, 1994). An unsound type system (C's, with casts and unchecked arrays; TypeScript's, by design) still catches many bugs but promises nothing.
4. **Static and dynamic checking differ in *when*, not whether, errors are caught.** Statically typed languages (Java, Rust, Haskell) check before running. Dynamically typed languages (Python, JavaScript) attach a type tag to each value and check at each operation. Both are "type safe" if every operation is checked somewhere; the static approach finds errors earlier and removes run-time checks, while the dynamic approach accepts more programs.
5. **Strong versus weak is about loopholes, not about static versus dynamic.** C is statically typed but weakly typed: casts and pointer arithmetic let you treat any bytes as any type, which is how buffer overflows become exploits. Python is dynamically typed but strongly typed: `"1" + 1` raises an error. A memory-safe language is one whose type system (static plus run-time checks) has no such loopholes in safe code.
6. **Types are propositions, and programs are proofs.** The Curry–Howard correspondence matches type constructors to logical connectives: a function type `A → B` corresponds to implication, a pair `A × B` to conjunction, a sum `A + B` to disjunction. A term of type `A → B` is a constructive proof that A implies B. This is the bridge from type systems to [proof assistants](../05-formal-methods/proof-assistants-and-dependent-types.md).
7. **More precise types state more, and cost more.** Plain types say "this is an integer". Refinement and dependent types can say "this is an integer between 0 and the array's length". Linear and affine types say "this value is used exactly once", which is how Rust's ownership rules guarantee memory and thread safety without a garbage collector. Each step adds guarantees and makes checking or annotation harder.
8. **Gradual and optional typing mix the two disciplines.** TypeScript and Python's type hints let typed and untyped code coexist, so large codebases can gain types incrementally.

## Key concepts

| Term | Meaning |
|---|---|
| Type | A classification of values that determines which operations are meaningful |
| Typing judgement `Γ ⊢ e : T` | In context Γ, expression `e` has type `T` |
| Soundness | Accepted programs never exhibit the errors the type system is designed to exclude |
| Completeness | Every program that cannot go wrong is accepted; impossible for decidable systems over Turing-complete languages |
| Progress / preservation | The two lemmas that together prove soundness |
| Static typing | Type checking done before execution, on the program text |
| Dynamic typing | Type checking done during execution, using run-time tags on values |
| Type safety | The language enforces its type abstractions; no operation applies to the wrong kind of value |
| Curry–Howard correspondence | The identification of types with propositions and programs with proofs |
| Linear / affine type | A type whose values must be used exactly / at most once |

## How it fits

- **Below:** Typing rules are a deductive system in the sense of [propositional logic](../../01-mathematical-foundations/01-logic/propositional-logic.md) and [proof techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md); the simply typed [lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md) is the standard core. Machine-level types ([two's complement integers](../../03-digital-logic/01-number-representation/integers-and-twos-complement.md), [floating point](../../03-digital-logic/01-number-representation/floating-point.md)) inherit hardware behaviour such as overflow.
- **Above:** Type checking is a phase of [semantic analysis](../03-compilers/semantic-analysis.md). Memory-safe types eliminate the bug classes catalogued in [memory-safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md). Types are machine-checked [interfaces](../../12-software-engineering/01-design/abstraction-and-interfaces.md) and the cheapest form of [static analysis](../../12-software-engineering/03-quality/static-analysis-and-code-review.md).
- **Siblings:** [Polymorphism and type inference](polymorphism-and-type-inference.md) make the system expressive and low-burden. [Binding and scope](binding-scope-and-closures.md) define the context Γ. [Syntax and semantics](syntax-and-semantics.md) define the "going wrong" that soundness excludes.

## Common misconceptions

- **"Static types eliminate bugs."** They eliminate the bugs the type system can express: shape errors, missing cases, null misuse in some languages. Logic errors that respect the types remain.
- **"Dynamically typed languages are untyped."** They are checked at run time; truly untyped languages (assembly, the untyped lambda calculus) check nothing.
- **"A sound type system means the program cannot crash."** Soundness excludes stuck states, but division by zero, array bounds errors and non-termination are usually handled as defined run-time errors outside the type system's guarantee.

## Go deeper

- Benjamin C. Pierce, *Types and Programming Languages* (2002): the standard text, from untyped lambda calculus to subtyping and recursive types.
- Robin Milner, "A Theory of Type Polymorphism in Programming" (1978): the source of "well-typed programs cannot go wrong".
- Philip Wadler, "Propositions as Types" (2015): an accessible account of Curry–Howard.
