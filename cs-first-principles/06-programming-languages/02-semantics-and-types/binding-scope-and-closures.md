# Binding, Scope and Closures

> **Layer:** [06 Programming Languages](../README.md) › [Semantics and Types](README.md)
> **Builds on:** [Syntax and semantics](syntax-and-semantics.md), [Lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md), [Stacks and queues](../../05-algorithms-and-data-structures/02-fundamental-data-structures/stacks-and-queues.md)
> **Enables:** [Functional programming](../01-paradigms/functional.md), [Semantic analysis](../03-compilers/semantic-analysis.md), [Memory management and garbage collection](../04-runtime-systems/memory-management-and-garbage-collection.md)

## Essence

A binding connects a name to the thing it denotes: a value, a memory location, a function or a type. Scope is the region of program text where a binding is visible; lifetime (extent) is the period of execution during which the bound entity exists. Most languages use lexical (static) scope: a name refers to the nearest enclosing definition in the source text, so you can resolve every name by reading the code. A closure is what makes lexical scope work when functions are values: a function bundled with the environment of bindings it was defined in, so it still sees those bindings after the defining function has returned. The single idea is that **names are resolved by where code is written, not by where it runs**, and a closure carries the "where it was written" along with it.

## Core tenets

1. **Binding time is a spectrum, and later binding buys flexibility at a cost.** Some bindings are fixed at language design time (`+` means addition), some at compile time (a local's stack offset), some at link time (a library function's address), some at run time (a virtual method's target). Each later binding adds flexibility and removes an optimisation the earlier binding would have allowed.
2. **Lexical scope makes name resolution a static, local question.** Under lexical scope, the binding of a free variable is found by walking outward through the enclosing blocks in the source. A compiler can resolve every reference before running, and a reader can understand a function without knowing its callers. Almost every modern language uses it.
3. **Dynamic scope resolves names by the call stack, and it breaks modularity.** Under dynamic scope (early Lisp, Emacs Lisp by default, shell variables) a free variable refers to the most recent binding still active at run time. A function's behaviour then depends on who called it, so renaming a local variable in a caller can change a distant callee.

   ```python
   x = "global"
   def show(): return x
   def caller():
       x = "local"
       return show()
   caller()   # lexical scope: "global";  dynamic scope would give "local"
   ```

4. **Shadowing and alpha-equivalence: names of bound variables do not matter.** An inner binding of `x` hides an outer one. Renaming a bound variable consistently (`λx.x` to `λy.y`) never changes meaning; this is alpha-equivalence from the [lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md). Substitution must avoid capturing a free variable by accident, which is why compilers often rename every variable to a unique name early.
5. **A closure pairs code with its defining environment.** When a function refers to variables from an enclosing scope and the function escapes (is returned or stored), the closure keeps those variables alive. In this example each counter has its own private `n`, which outlives the call to `make_counter`.

   ```javascript
   function makeCounter() { let n = 0; return () => ++n; }
   const c = makeCounter(); c(); c();   // 1, then 2
   ```

6. **Escaping closures break stack discipline, forcing heap allocation.** A stack frame dies when its function returns, but a captured variable may be needed later. The implementation must move captured variables to the heap (closure conversion), and something must eventually free them. This is one main reason why languages with first-class functions use [garbage collection](../04-runtime-systems/memory-management-and-garbage-collection.md), and why Rust's borrow checker must reason about closure lifetimes.
7. **Capture by reference versus by value changes behaviour.** JavaScript and Python closures capture variables, not snapshots of values, so all closures created in a loop over one shared variable see its final value. C++ lambdas make the choice explicit (`[=]` copies, `[&]` references), and capturing a reference to a local that then dies is a dangling-pointer bug.
8. **Environments are the run-time form of scope.** An interpreter keeps a chain of environment frames mapping names to locations; a compiler replaces names with fixed offsets (stack slot, closure field, global address), turning a lookup into a single memory access. Static links or display arrays let nested functions find outer frames.

## Key concepts

| Term | Meaning |
|---|---|
| Binding | An association between a name and an entity (value, location, function, type) |
| Scope | The program region in which a binding is visible |
| Lifetime (extent) | The period at run time during which an entity exists |
| Lexical (static) scope | Names resolve to the nearest enclosing definition in the source text |
| Dynamic scope | Names resolve to the most recent active binding on the call stack |
| Free variable | A variable used in an expression but not bound within it |
| Closure | A function value plus the environment that binds its free variables |
| Environment | A mapping from names to locations or values at a point in execution |
| Shadowing | An inner binding hiding an outer binding of the same name |

## How it fits

- **Below:** Free and bound variables and substitution come from the [lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md). Stack allocation of frames relies on the last-in first-out discipline of [stacks](../../05-algorithms-and-data-structures/02-fundamental-data-structures/stacks-and-queues.md) and the hardware's call conventions in the [Instruction Set Architecture (ISA)](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md).
- **Above:** [Semantic analysis](../03-compilers/semantic-analysis.md) builds symbol tables to implement scope; [linkers](../04-runtime-systems/linking-and-loading.md) resolve the bindings left open across separately compiled files; closures underlie callbacks in event-driven [input/output models](../../07-operating-systems/06-io-and-devices/io-models.md) and module privacy in [information hiding](../../12-software-engineering/01-design/modularity-and-information-hiding.md).
- **Siblings:** [Syntax and semantics](syntax-and-semantics.md) gives the framework; [type systems](type-systems.md) use the same environments, mapping names to types instead of values.

## Common misconceptions

- **"A closure copies the values it uses."** In most languages it captures the variables themselves, so later mutation is visible inside the closure.
- **"Scope and lifetime are the same thing."** A static local in C has function scope but program-long lifetime; a captured variable is out of scope for the caller but still alive.
- **"Global variables are just variables with big scope."** Every function can read and write them, so every function's behaviour may depend on every other's: they turn local reasoning into global reasoning.

## Go deeper

- Harold Abelson and Gerald Jay Sussman, *Structure and Interpretation of Computer Programs* (2nd ed., 1996), section 3.2: the environment model of evaluation.
- Shriram Krishnamurthi, *Programming Languages: Application and Interpretation* (2nd ed., 2017): builds interpreters that make scope and closures concrete.
- Peter J. Landin, "The Mechanical Evaluation of Expressions" (1964): introduced closures and the environment-based abstract machine.
