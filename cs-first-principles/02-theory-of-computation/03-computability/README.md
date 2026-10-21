# Computability

> **Layer:** [02 Theory of Computation](../README.md) › Computability
> **Children:** [Turing Machines](turing-machines.md) · [Lambda Calculus](lambda-calculus.md) · [Church–Turing Thesis](church-turing-thesis.md) · [Halting Problem and Undecidability](halting-problem-and-undecidability.md)

## What this area is about

Computability asks the most basic question in Computer Science (CS): **what can be computed at all**, given unlimited time and memory? Its answer has two halves. First, there is a precise, robust definition of "computable": whatever a Turing machine (or, equivalently, the lambda calculus) can do. Second, that class has hard edges: some perfectly well-defined problems, starting with whether a program halts, lie outside it, and no future hardware or cleverness will bring them in.

The unifying idea is that **programs are data**. Because a machine can be written down as a string, one machine can read, simulate and reason about another. That single fact gives both the power of computing (a universal machine that runs any program) and its limits (a program that asks a hypothetical decider about itself and does the opposite). Universality and undecidability are two consequences of the same self-reference.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Turing Machines](turing-machines.md) | The state-and-tape model; universality; decidable vs recognisable | Automata, cardinality |
| [Lambda Calculus](lambda-calculus.md) | The substitution model; functions as the only primitive; root of programming languages | Functions, logic |
| [Church–Turing Thesis](church-turing-thesis.md) | Why the two models (and all others) define the same class, and why that class is "the computable" | Both models |
| [Halting Problem and Undecidability](halting-problem-and-undecidability.md) | What lies outside: diagonalisation, reductions, Rice's theorem | Turing machines, the thesis |

Read the two models first, in either order: Turing machines model the *machine*, the lambda calculus models the *language*. The thesis then argues they capture the same notion, and that this notion is the right one. The halting problem uses the universal machine and program-as-data encoding to draw the boundary.

```
        Turing machines           lambda calculus        (+ recursive functions,
        (state + tape)            (substitution)            Post systems, RAMs...)
               \                        /
                \---- proved equal ----/
                           |
                  Church-Turing thesis:  this class = "effectively computable"
                           |
              +------------+-------------+
              |                          |
       universal machine            diagonalisation
     (one machine runs all)      (halting undecidable,
                                  Rice's theorem, ...)
```

## Connections to sibling areas

- **[Information Theory](../01-information-theory/README.md):** [Kolmogorov complexity](../01-information-theory/kolmogorov-complexity.md) defines the information in a single string as its shortest program, linking entropy to computability. It is uncomputable, by a reduction from the halting problem.
- **[Automata and Formal Languages](../02-automata-and-formal-languages/README.md):** Turing machines are the top of the Chomsky hierarchy. Undecidability explains why grammar equivalence and similar questions fail for context-free languages.
- **[Complexity](../04-complexity/README.md):** Complexity theory restricts attention to decidable problems and asks what they cost. It reuses this area's tools: Turing machines as the cost model, diagonalisation for the hierarchy theorems, and reductions for completeness.
- **[Quantum Computation](../05-quantum-computation/README.md):** Quantum computers compute exactly the Turing-computable functions; they challenge only the *extended* thesis about efficiency, not computability.

## Connections across layers

From [mathematical foundations](../../01-mathematical-foundations/README.md), the area uses [logic](../../01-mathematical-foundations/01-logic/predicate-logic.md), [proof by contradiction](../../01-mathematical-foundations/01-logic/proof-techniques.md), [cardinality](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md) and [induction](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md). Through the Church–Turing thesis it meets the physical pillar: [digital logic](../../03-digital-logic/README.md) and [computer architecture](../../04-computer-architecture/README.md) build a universal machine out of [transistors](../../00-engineering-foundations/03-semiconductor-devices/cmos.md).

Upward, the universal machine becomes the stored-program computer and the [interpreter](../../06-programming-languages/04-runtime-systems/interpreters-and-virtual-machines.md). The lambda calculus becomes [functional programming](../../06-programming-languages/01-paradigms/functional.md) and [type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md). Undecidability bounds [static analysis](../../12-software-engineering/03-quality/static-analysis-and-code-review.md), [compiler optimisation](../../06-programming-languages/03-compilers/optimization.md), [formal verification](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md) and malware detection in [security](../../11-security-and-cryptography/README.md).

## Cross-cutting threads

- [Recursion and self-reference](../../CROSS-CUTTING.md#recursion-and-self-reference): universal machines, the Y combinator and the halting proof all rely on programs that take programs as input.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): the halting problem and Rice's theorem are absolute limits.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): the thesis lets every higher layer treat "a computer" as one abstract machine.
- [Virtualization](../../CROSS-CUTTING.md#virtualization): the universal Turing machine is the first virtual machine, one machine pretending to be any other.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): undecidability is why verification needs restricted languages, annotations or approximation.
