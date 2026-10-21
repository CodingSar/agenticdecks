# Polymorphism and Type Inference

> **Layer:** [06 Programming Languages](../README.md) › [Semantics and Types](README.md)
> **Builds on:** [Type systems](type-systems.md), [Logic and declarative programming](../01-paradigms/logic-and-declarative.md), [Graph traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md)
> **Enables:** [Functional programming](../01-paradigms/functional.md), [Abstraction and interfaces](../../12-software-engineering/01-design/abstraction-and-interfaces.md), [Proof assistants and dependent types](../05-formal-methods/proof-assistants-and-dependent-types.md)

## Essence

Polymorphism lets one piece of code work for values of many types. Without it, a static type system would force you to write `reverseIntList`, `reverseStringList` and so on, separately, for every element type. There are three kinds (Strachey, 1967; Cardelli and Wegner, 1985): parametric polymorphism (one definition that works uniformly for all types, as in generics), ad hoc polymorphism (one name with different implementations per type, as in overloading and type classes), and subtype polymorphism (a value of a more specific type used where a general one is expected). Type inference is the complementary idea: the compiler works out the types itself, so the programmer gets static checking without writing annotations everywhere. The Hindley–Milner (HM) algorithm does this completely for ML-style languages by turning typing into equation solving.

## Core tenets

1. **Parametric polymorphism works because the code never inspects the type.** A function `reverse : ∀a. List a → List a` handles any element type because it only moves elements, never looks inside them. This uniformity yields "theorems for free" (Wadler, 1989): from the type alone you know `reverse` cannot invent new elements, only rearrange, drop or duplicate existing ones.
2. **Ad hoc polymorphism dispatches on the type.** Overloading resolves `+` to integer or floating-point addition at compile time. Haskell's type classes and Rust's traits generalise this: a function `sort : Ord a => List a → List a` works for any type that supplies a comparison, and the compiler passes the right comparison implicitly.
3. **Subtyping is a relation that must be checked carefully with variance.** If `Cat <: Animal`, a function returning `Cat` can stand in for one returning `Animal` (covariant results), but a function accepting `Cat` cannot stand in for one accepting `Animal` (parameters are contravariant). Mutable containers must be invariant: Java's covariant arrays are unsound, which is why storing a `Dog` into an `Animal[]` that is really a `Cat[]` throws `ArrayStoreException` at run time.
4. **Polymorphism is implemented by either sharing one copy or making many.** *Uniform representation* (Java generics with erasure, OCaml) compiles one version that treats every value as a pointer-sized box. *Monomorphisation* (C++ templates, Rust generics) generates a specialised copy per type, giving full speed at the cost of code size and compile time. Dictionary passing implements type classes by adding a hidden argument holding the method table.
5. **Hindley–Milner inference is constraint generation plus unification.** Give every unknown a fresh type variable, walk the program generating equations (`if f is applied to x then type(f) = type(x) → β`), and solve them with Robinson's unification (the same algorithm as [Prolog's](../01-paradigms/logic-and-declarative.md)). Any variable left unconstrained is generalised to `∀`. The result is the *principal type*, the most general type, from which every other valid type is an instance.

   ```ocaml
   let compose f g x = f (g x)
   (* inferred: ('b -> 'c) -> ('a -> 'b) -> 'a -> 'c *)
   ```

6. **Let-polymorphism is the restriction that keeps inference decidable.** HM generalises types only at `let` bindings, not for function parameters, so an argument cannot itself be used at two types inside the function. Full System F (Girard 1972, Reynolds 1974), where any term can be polymorphic, has undecidable type inference (Wells, 1999). Practical languages sit near HM and ask for annotations where they go beyond it.
7. **Inference is near-linear in practice but exponential in the worst case.** HM inference is complete for deterministic exponential time (DEXPTIME) in theory (Mairson, 1990; Kfoury, Tiuryn and Urzyczyn), because nested `let`s can create types of exponential size, but real programs never trigger this. Local type inference (Scala, Kotlin, C#, Rust within functions) infers less but scales well and gives better error messages.
8. **Subtyping and full inference do not mix easily.** Adding subtyping turns equations into inequalities, which makes principal types and complete inference much harder. That is why object-oriented languages generally infer only local variable types (`var`, `auto`) and require signatures on methods.

## Key concepts

| Term | Meaning |
|---|---|
| Parametric polymorphism | One definition that behaves uniformly for all types (`∀a.`) |
| Ad hoc polymorphism | One name with type-specific implementations (overloading, type classes) |
| Subtype polymorphism | Values of a subtype are accepted where a supertype is expected |
| Variance | How subtyping of components affects subtyping of a composite (co-, contra-, in-variant) |
| Type variable | A placeholder for an unknown type, solved or generalised by inference |
| Unification | Finding the most general substitution that makes two type terms equal |
| Principal type | The most general type of an expression; all others are its instances |
| Monomorphisation | Compiling a generic definition into one specialised copy per type used |
| Type erasure | Compiling generics to a single version, discarding type arguments at run time |

## How it fits

- **Below:** Unification is a [logic-programming](../01-paradigms/logic-and-declarative.md) primitive with roots in [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md); constraint solving is a [graph](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md) problem over type terms, often implemented with [union-find](../../05-algorithms-and-data-structures/02-fundamental-data-structures/union-find.md). Subtyping is a [partial order](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md).
- **Above:** Generic libraries (collections, algorithms) depend on parametric polymorphism; [design patterns](../../12-software-engineering/01-design/design-patterns.md) depend on subtyping; [just-in-time compilers](../04-runtime-systems/jit-compilation.md) specialise polymorphic code at run time much as monomorphisation does ahead of time.
- **Siblings:** Extends [type systems](type-systems.md) with generality; uses the environments of [binding and scope](binding-scope-and-closures.md); inference is part of [semantic analysis](../03-compilers/semantic-analysis.md) in compilers.

## Common misconceptions

- **"Type inference means dynamic typing."** Inferred types are fully static; the compiler simply writes them for you.
- **"Generics are just templates."** C++ templates are checked only after expansion (until concepts in C++20); ML and Rust generics are checked once, against their declared constraints, before any instantiation.
- **"Inheritance is the only way to get polymorphism."** Parametric and ad hoc polymorphism give reuse without any subtyping relation at all.

## Go deeper

- Luis Damas and Robin Milner, "Principal Type-Schemes for Functional Programs" (1982): the definitive HM algorithm (Algorithm W).
- Philip Wadler, "Theorems for Free!" (1989): what parametricity guarantees.
- Benjamin C. Pierce, *Types and Programming Languages* (2002), chapters 15, 22 and 23: subtyping, reconstruction and System F.
