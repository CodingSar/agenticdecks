# Semantic Analysis

> **Layer:** [06 Programming Languages](../README.md) › [Compilers](README.md)
> **Builds on:** [Lexing and parsing](lexing-and-parsing.md), [Binding, scope and closures](../02-semantics-and-types/binding-scope-and-closures.md), [Type systems](../02-semantics-and-types/type-systems.md), [Hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md)
> **Enables:** [Intermediate representations](intermediate-representations.md), [Static analysis and code review](../../12-software-engineering/03-quality/static-analysis-and-code-review.md), [Memory-safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md)

## Essence

Semantic analysis is the compiler phase that checks the rules a grammar cannot express and records what every name and expression means. The parser only knows that `x = f(y, 2)` is well-formed; semantic analysis finds out which `x`, `f` and `y` are meant, whether `f` takes two arguments, and whether the result can be assigned to `x`. It does this by building symbol tables that implement the language's scope rules, then walking the Abstract Syntax Tree (AST) and applying the type system's rules to each node. Its output is an annotated AST in which every name points to its declaration and every expression carries its type. The single idea is **context-sensitive checking by attribute computation over the tree**: information flows down (what is in scope here?) and up (what type does this subexpression have?) until every node is decorated and every rule is checked.

## Core tenets

1. **Semantic analysis handles exactly what context-free grammars cannot.** "Declared before use", "no duplicate declarations in one scope", "number of arguments matches the definition" and type rules all depend on information elsewhere in the program. Rather than use a more powerful (and slower) grammar formalism, compilers parse with a context-free grammar and enforce these rules in a separate pass with ordinary data structures.
2. **Symbol tables implement scope.** A symbol table maps names to declarations (kind, type, location). For lexical scope it is a stack of [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md): entering a block pushes a new table, lookups search from the innermost outwards, leaving the block pops it. Lookup is effectively constant time per level, so name resolution is linear in program size.
3. **Attribute grammars formalise the flow of information.** Knuth (1968) attached attributes to grammar symbols. *Synthesised* attributes flow up the tree (the type of `a + b` is computed from the types of `a` and `b`); *inherited* attributes flow down (the scope a statement is in). Real compilers rarely use the formalism directly, but every type checker is an attribute evaluator in practice.
4. **Type checking applies typing rules node by node; inference solves for unknowns.** For a language with explicit annotations, each node's type is computed from its children and compared with what the context expects. For a language with [type inference](../02-semantics-and-types/polymorphism-and-type-inference.md), the pass generates constraints and solves them by unification. Either way, the result is that every expression has a known type before code generation.
5. **Checking inserts implicit operations into the tree.** When the language allows `int + double`, the checker inserts an explicit conversion node. It also resolves overloaded operators (`+` on strings means concatenation), chooses which overloaded function is meant, and marks which calls need dynamic dispatch. The back end never has to guess.

   ```
   source:   d = i + 2.5          (i : int, d : double)
   AST after: Assign(d, AddF64(IntToF64(Var i), Const 2.5))
   ```

6. **Some checks are flow-sensitive and need more than a tree walk.** "Every path returns a value", "variable definitely assigned before use" (Java) and Rust's borrow checking depend on control flow, not just nesting. Compilers run these on a control-flow graph, with the same dataflow techniques used for [optimisation](optimization.md).
7. **Good error messages are a semantic-analysis product.** Because the checker knows the declared and expected types and the source positions, it can say "expected `String`, found `int` at line 12, column 8". Error recovery here means assigning an "error type" that is compatible with everything, so one mistake does not cascade into dozens of reports.
8. **The phase decides what can go wrong at run time.** Whatever semantic analysis does not check statically must be either checked at run time (array bounds in Java, casts) or left undefined (array bounds in C). That choice, made in the language design and implemented here, determines whether out-of-bounds writes become exceptions or [exploitable vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md).

## Key concepts

| Term | Meaning |
|---|---|
| Symbol table | A mapping from names to their declarations, organised by scope |
| Name resolution | Linking each use of an identifier to the declaration it refers to |
| Attribute grammar | A grammar whose symbols carry values computed by rules attached to productions |
| Synthesised attribute | A value computed from a node's children (flows up) |
| Inherited attribute | A value passed from a node's parent or siblings (flows down) |
| Type checking | Verifying that each expression's type matches what its context requires |
| Coercion | An implicit type conversion inserted by the compiler |
| Overload resolution | Choosing which of several same-named functions a call refers to |
| Definite assignment | A flow-sensitive check that every variable is written before it is read |

## How it fits

- **Below:** It implements the abstract rules of [binding and scope](../02-semantics-and-types/binding-scope-and-closures.md) and [type systems](../02-semantics-and-types/type-systems.md) using [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) and [tree traversals](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md). It is limited by [undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md): flow-sensitive checks must be conservative.
- **Above:** Static analysers, linters and editor tooling ([static analysis](../../12-software-engineering/03-quality/static-analysis-and-code-review.md)) reuse this phase; the annotated tree is lowered into an [intermediate representation](intermediate-representations.md).
- **Siblings:** It consumes the AST from [lexing and parsing](lexing-and-parsing.md) and is the last phase that knows about source-language concepts; after lowering to an [intermediate representation](intermediate-representations.md), names and high-level types are mostly gone.

## Common misconceptions

- **"If it compiles, it type-checks everything."** Only what the type system expresses. Casts, unchecked generics and `unsafe` blocks are explicit escapes from checking.
- **"Semantic analysis is one pass."** Many languages need several: one to collect all declarations (so functions can be called before their definition), another to check bodies, and more for flow-sensitive properties.
- **"Dynamically typed languages skip this phase."** They still resolve scopes (Python decides at compile time which names are local) and often run linters and optional type checkers built on the same ideas.

## Go deeper

- Andrew W. Appel, *Modern Compiler Implementation in ML* (1998), chapter 5: symbol tables and type checking, implemented.
- Donald E. Knuth, "Semantics of Context-Free Languages" (1968): the original attribute grammars.
- Alfred V. Aho, Monica S. Lam, Ravi Sethi and Jeffrey D. Ullman, *Compilers: Principles, Techniques, and Tools* (2nd ed., 2006), chapters 5 and 6: syntax-directed translation and type checking.
