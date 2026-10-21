# Syntax and Semantics

> **Layer:** [06 Programming Languages](../README.md) › [Semantics and Types](README.md)
> **Builds on:** [Context-free grammars and pushdown automata](../../02-theory-of-computation/02-automata-and-formal-languages/context-free-grammars-and-pushdown-automata.md), [Lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md), [Relations and orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md)
> **Enables:** [Lexing and parsing](../03-compilers/lexing-and-parsing.md), [Type systems](type-systems.md), [Hoare logic and program proofs](../05-formal-methods/hoare-logic-and-program-proofs.md)

## Essence

Syntax is the form of a program: which strings of characters are legal and how they group into a tree. Semantics is the meaning: what a legal program computes. They are deliberately separate. The same meaning can have many syntaxes (`x+1` and `(+ x 1)`), and a syntactically valid program can be meaningless (`"a" / 3` in a typed language). Syntax is fixed precisely by a grammar; semantics is fixed precisely by one of three mathematical styles (operational, denotational or axiomatic), or, in most real languages, by a long prose standard. The single idea is **compositionality**: the meaning of a phrase is determined by the meanings of its parts and how they are combined, so meaning can be defined by recursion over the syntax tree.

## Core tenets

1. **Concrete syntax is for humans; abstract syntax is for meaning.** The concrete syntax includes parentheses, keywords and precedence rules. A parser turns it into an Abstract Syntax Tree (AST) that keeps only structure: `(1 + 2) * 3` becomes `Mul(Add(1,2),3)`. Every later stage (semantics, typing, compilation) is defined on the AST, so syntax design can change without touching meaning.
2. **Grammars define syntax, but ambiguity must be removed.** Most languages' syntax is described by a [context-free grammar](../../02-theory-of-computation/02-automata-and-formal-languages/context-free-grammars-and-pushdown-automata.md). A grammar is ambiguous if one string has two parse trees: `if a then if b then s else t` (the "dangling else") or `1 - 2 - 3` without associativity rules. Ambiguity means two meanings, so languages resolve it by precedence, associativity and disambiguation rules.
3. **Some "syntax" rules are not context-free.** "Declare a variable before use" and "call a function with the right number of arguments" need information from elsewhere in the program. Compilers therefore split checking: the grammar handles nesting, and [semantic analysis](../03-compilers/semantic-analysis.md) handles context-sensitive rules using symbol tables.
4. **Operational semantics defines meaning by execution steps.** Small-step (structural) operational semantics (Plotkin, 1981) gives rules for one step of computation, such as `if true then e1 else e2 → e1`. Big-step semantics relates an expression directly to its final value. Operational semantics is closest to an interpreter, and it is the standard tool for proving type soundness.
5. **Denotational semantics maps each phrase to a mathematical object.** Scott and Strachey (1970s) defined the meaning of a program as a function, for example from input states to output states, built compositionally from its parts. Loops and recursion are given meaning as the least fixed point of an equation, which needs domain theory to handle non-termination. Two programs are equivalent exactly when they denote the same object.
6. **Axiomatic semantics defines meaning by what can be proved.** Hoare logic (1969) gives each construct a rule relating preconditions and postconditions, such as `{P[e/x]} x := e {P}`. The meaning of a program is the set of facts about it that are provable. This is the basis of [program verification](../05-formal-methods/hoare-logic-and-program-proofs.md).
7. **Unspecified and undefined behaviour are semantic choices.** A language standard may leave things open: evaluation order in C is unspecified (any order is allowed), and signed overflow is undefined (no requirement at all). These gaps give compilers freedom to optimise but make the same source mean different things on different compilers.

   ```
   int i = 0;  a[i] = i++;   // C: undefined behaviour (unsequenced read and write of i)
   ```

8. **Syntactic sugar adds convenience without new meaning.** A construct is sugar if it can be translated into existing constructs locally: `for` loops into `while`, `x += 1` into `x = x + 1` (when `x` has no side effects). Defining a language as a small core plus sugar keeps the semantics small and the proofs tractable.

## Key concepts

| Term | Meaning |
|---|---|
| Concrete syntax | The exact textual form of programs, including punctuation and keywords |
| Abstract Syntax Tree (AST) | A tree that records only the structural content of a program |
| Ambiguous grammar | A grammar under which some string has more than one parse tree |
| Operational semantics | Meaning given by rules describing how a program executes, step by step |
| Denotational semantics | Meaning given by mapping each phrase to a mathematical object |
| Axiomatic semantics | Meaning given by logical rules for what can be proved about programs |
| Compositionality | The meaning of a whole is a function of the meanings of its parts |
| Fixed point | A value `x` with `f(x) = x`; used to give meaning to recursion and loops |
| Syntactic sugar | Surface syntax definable by local translation into a core language |

## How it fits

- **Below:** Grammars come from [formal language theory](../../02-theory-of-computation/02-automata-and-formal-languages/README.md); the lambda calculus provides the minimal core used to study semantics; [relations](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md) and partial orders underpin step relations and fixed points.
- **Above:** [Parsers](../03-compilers/lexing-and-parsing.md) implement the syntax; [interpreters](../04-runtime-systems/interpreters-and-virtual-machines.md) are executable operational semantics; [compiler correctness](../03-compilers/optimization.md) means preserving semantics; [formal methods](../05-formal-methods/README.md) reason with axiomatic semantics.
- **Siblings:** [Binding and scope](binding-scope-and-closures.md) is the first piece of semantics any language must define. [Type systems](type-systems.md) are a static approximation of the semantics defined here.

## Common misconceptions

- **"The compiler defines the language."** When a compiler is the only specification, its bugs become features and other implementations cannot be checked against anything. Standards (the C standard, the ECMAScript specification) and formal definitions (Standard ML, WebAssembly) exist to separate the meaning from any one implementation.
- **"Syntax is superficial."** Syntax decides what is easy to read and what errors are easy to make; Lisp's uniform syntax enables macros, and C's declarator syntax causes real bugs.
- **"The three semantic styles compete."** They answer different questions (how it runs, what it is, what can be proved) and are routinely proved consistent with each other for the same language.

## Go deeper

- Glynn Winskel, *The Formal Semantics of Programming Languages* (1993): all three styles for one small language, with proofs that they agree.
- Benjamin C. Pierce, *Types and Programming Languages* (2002), chapters 3 and 5: operational semantics as the working tool.
- Robin Milner, Mads Tofte, Robert Harper and David MacQueen, *The Definition of Standard ML* (revised, 1997): a full language defined formally.
