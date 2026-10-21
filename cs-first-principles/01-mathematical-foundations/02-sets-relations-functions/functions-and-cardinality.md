# Functions and Cardinality

> **Layer:** [01 Mathematical Foundations](../README.md) › [Sets, Relations and Functions](README.md)
> **Builds on:** [Sets](sets.md), [Relations and Orders](relations-and-orders.md)
> **Enables:** [Halting Problem and Undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), [Hash Functions and MACs](../../11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md), [Functional Programming](../../06-programming-languages/01-paradigms/functional.md), [Source Coding and Compression](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md)

## Essence

A function `f: A → B` is a relation that pairs every element of its domain `A` with exactly one element of its codomain `B`. Functions are the mathematical model of a deterministic computation: same input, same output. Three properties, injective (one-to-one), surjective (onto) and bijective (both), tell you whether information is lost, whether every output is reachable, and whether a computation can be undone. Comparing sets by functions between them gives *cardinality*, the notion of size. For infinite sets this produces the surprising fact that some infinities are larger than others, and that the set of programs is strictly smaller than the set of problems, so most problems have no program.

## Core tenets

1. **A function is a relation with exactly one output per input.** `f ⊆ A × B` such that for each `a` there is a unique `b` with `(a, b) ∈ f`. A *partial* function may be undefined on some inputs, which is what a program that can loop forever or throw really computes. Pure functions in [functional programming](../../06-programming-languages/01-paradigms/functional.md) are mathematical functions; procedures with side effects are not, which is the whole reason referential transparency is a property worth naming.

2. **Injective means no information is lost.** If `f(a₁) = f(a₂)` implies `a₁ = a₂`, then the input can be recovered from the output. Lossless compression and encryption must be injective, or decoding is ambiguous. A function from a larger finite set into a smaller one cannot be injective (pigeonhole), so every [hash function](../../11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md) has collisions and the design goal is to make them hard to *find*, not to avoid them.

3. **Surjective means every output is hit; bijective means perfectly invertible.** A bijection has an inverse `f⁻¹` with `f⁻¹(f(a)) = a`. Bijections are the formal meaning of "same information, different encoding": two's complement is a bijection between bit patterns and an integer range, a permutation is a bijection from a set to itself, and a block cipher under a fixed key is a bijection on blocks.

4. **Composition is associative, and that makes pipelines work.** `(g ∘ f)(x) = g(f(x))`, and `h ∘ (g ∘ f) = (h ∘ g) ∘ f`. Associativity means a chain of transformations can be grouped any way, which is what lets Unix pipes, compiler passes and neural-network layers be built and reasoned about in pieces. Composing injections gives an injection, and likewise for surjections and bijections.

5. **Cardinality compares sizes by bijection.** Two sets have the same cardinality when a bijection exists between them. For finite sets this is counting. For infinite sets it gives strange but true results: the even numbers, the integers and the rationals all have the same size as ℕ. Such sets are *countable*: their elements can be listed in a sequence, which is the same as saying a program could enumerate them.

6. **Some infinite sets are uncountable (Cantor).** The real numbers, and the set of all infinite bit strings, cannot be listed: any list misses the diagonal string that differs from the *i*-th entry at position *i*. More generally, `|P(A)| > |A|` for every set `A`. There are always more subsets than elements.

7. **There are countably many programs but uncountably many problems.** Every program is a finite string over a finite alphabet, so programs are countable. A decision problem is a subset of ℕ (the inputs whose answer is yes), and there are uncountably many subsets. So almost every problem is undecidable. The [halting problem](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) is a concrete, natural example of what this counting argument guarantees exists.

8. **Functions are values (higher-order functions and currying).** The set of all functions from `A` to `B` is written `B^A`, and it has |B|^|A| elements when finite, which is why there are 2^(2^n) Boolean functions of *n* inputs. A function of two arguments `A × B → C` corresponds exactly to a function `A → (B → C)` (currying). Treating functions as data is the mathematical basis of [lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md), closures and callbacks.

## Key concepts

| Term | Meaning |
|---|---|
| Domain / codomain | The set of inputs / the set outputs are drawn from |
| Image (range) | The set of outputs actually produced |
| Partial function | Defined on only part of its domain |
| Injective | Distinct inputs give distinct outputs |
| Surjective | Every element of the codomain is some output |
| Bijective | Injective and surjective; has an inverse |
| Composition | `g ∘ f`, apply `f` then `g` |
| Countable | Finite, or in bijection with ℕ |
| Uncountable | Infinite but not countable, such as ℝ |
| Currying | Turning `A × B → C` into `A → (B → C)` |

## How it fits

- **Below:** Functions are special [relations](relations-and-orders.md), built from [sets](sets.md).
- **Above:** Computability theory ([02](../../02-theory-of-computation/README.md)) rests on the countability argument. [Compression](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md) and [encryption](../../11-security-and-cryptography/02-cryptography/symmetric-encryption.md) need injectivity. Asymptotic notation compares functions on ℕ ([asymptotic analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md)). [Functional languages](../../06-programming-languages/01-paradigms/functional.md) and [type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md) treat functions as first-class values with function types.
- **Siblings:** [Sets](sets.md) supplies the objects; [relations](relations-and-orders.md) supplies the general case of which functions are the deterministic special case.

## Common misconceptions

- **"A good hash function has no collisions."** Pigeonhole forbids that whenever the input space is larger than the output space; collisions must merely be rare and hard to find.
- **"All infinities are the same size."** The reals are strictly larger than the integers, and this gap is why most problems are uncomputable.
- **"A program is a function."** A program with side effects or nontermination is at best a partial function on a state space, not a function on its visible arguments.

## Go deeper

- Paul Halmos, *Naive Set Theory* (1960): functions and cardinal numbers, briefly and precisely.
- Michael Sipser, *Introduction to the Theory of Computation* (3rd ed., 2012): uses diagonalisation to prove undecidability.
- Eric Lehman, F. Thomson Leighton and Albert Meyer, *Mathematics for Computer Science* (2017 revision, free online): functions, bijections and infinite sets.
