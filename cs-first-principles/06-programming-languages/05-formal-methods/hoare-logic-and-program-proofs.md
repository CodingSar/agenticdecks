# Hoare Logic and Program Proofs

> **Layer:** [06 Programming Languages](../README.md) › [Formal Methods](README.md)
> **Builds on:** [Predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md), [Induction and recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md), [Syntax and semantics](../02-semantics-and-types/syntax-and-semantics.md), [Correctness and invariants](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md)
> **Enables:** [Proof assistants and dependent types](proof-assistants-and-dependent-types.md), [Static analysis and code review](../../12-software-engineering/03-quality/static-analysis-and-code-review.md), [Lock-free synchronization](../../07-operating-systems/03-concurrency/lock-free-synchronization.md)

## Essence

Hoare logic (Hoare, 1969, building on Floyd, 1967) is a formal system for proving that imperative programs meet their specifications. Its central object is the Hoare triple `{P} C {Q}`: if precondition `P` holds before command `C` runs, and `C` terminates, then postcondition `Q` holds afterwards. Each language construct has an inference rule, so a proof about a whole program is assembled from proofs about its parts, following the syntax. The hard creative step is finding loop invariants; once they are supplied, the rest can be reduced mechanically to logical formulas, called verification conditions, that automatic solvers can often discharge. The single idea is **reasoning about state changes by tracking what is true, not what the values are**.

## Core tenets

1. **A specification is a pair of predicates over program state.** The precondition states what the caller must guarantee; the postcondition states what the code promises in return. This is the formal version of a contract: `{x ≥ 0} y := sqrt(x) {y*y = x}`. Writing the specification is often where the real bugs are found, because it forces a precise statement of intent.
2. **Each construct has one rule, so proofs compose.** The assignment axiom works backwards: `{Q[e/x]} x := e {Q}`, meaning that to have `Q` after the assignment, `Q` with `e` substituted for `x` must hold before. Sequencing chains triples through an intermediate assertion. The conditional rule proves each branch under its guard. The rule of consequence lets you strengthen preconditions and weaken postconditions using ordinary logic.
3. **Loops are handled by invariants, and finding them is the hard part.** The while rule says: if `I` holds before the loop, and each iteration preserves `I` while the guard `B` is true, then after the loop `I ∧ ¬B` holds. Choosing `I` is an act of insight equivalent to understanding why the loop works; it is the same induction argument used in [algorithm correctness proofs](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md).

   ```
   {n ≥ 0}
   i := 0; s := 0;
   while i < n do        invariant I:  s = 0 + 1 + ... + (i-1)  ∧  i ≤ n
     s := s + i; i := i + 1
   {s = n(n-1)/2}        follows from I ∧ ¬(i < n), i.e. I ∧ i = n
   ```

4. **Partial correctness ignores termination; total correctness adds a variant.** `{P} C {Q}` as above says nothing if `C` loops forever. Total correctness additionally requires a variant: an integer expression that is bounded below and strictly decreases on every iteration, so the loop must stop. Termination is undecidable in general, which is why it is proved separately and needs human-supplied measures.
5. **Weakest preconditions make proofs computable.** Dijkstra (1975) defined `wp(C, Q)`, the weakest precondition guaranteeing that `C` terminates in a state satisfying `Q`. For loop-free code `wp` is computed mechanically by working backwards. Given annotated loop invariants, a verifier computes verification conditions and hands them to a Satisfiability Modulo Theories (SMT) solver such as Z3. Tools such as Dafny, Why3, Frama-C and SPARK work this way.
6. **Aliasing breaks the simple rules; separation logic restores modularity.** The assignment axiom assumes that changing `x` changes nothing else. With pointers, a write through `p` may change what `*q` means. Separation logic (Reynolds, O'Hearn and others, around 2000–2002) adds a separating conjunction `P * Q` meaning "P and Q hold for disjoint parts of the heap", and a frame rule that lets a proof about one part of the heap ignore the rest. Facebook's Infer analyser and many verified systems are built on it.
7. **Concurrency needs reasoning about interference.** When threads share state, an assertion one thread relies on may be invalidated by another. Owicki–Gries (1976) checks that each thread's assertions are stable under the other threads' actions; rely–guarantee and concurrent separation logic make this modular. This is how lock-free algorithms and kernels are proved.
8. **Design by contract is Hoare logic used at run time.** Eiffel, and assertion libraries in many languages, state preconditions, postconditions and class invariants in code and check them during execution. This gives no proof, but it makes specifications executable, documents intent and catches violations near their cause.

## Key concepts

| Term | Meaning |
|---|---|
| Hoare triple `{P} C {Q}` | If `P` holds before `C` and `C` terminates, `Q` holds after |
| Precondition / postcondition | What must be true before a command / what is guaranteed after |
| Loop invariant | An assertion true before and after every iteration of a loop |
| Variant (ranking function) | A bounded quantity that decreases each iteration, proving termination |
| Partial / total correctness | Correct if it terminates / correct and guaranteed to terminate |
| Weakest precondition `wp(C, Q)` | The least restrictive condition under which `C` establishes `Q` |
| Verification condition | A logical formula whose validity implies the program meets its specification |
| Separation logic | An extension of Hoare logic for reasoning about disjoint heap regions |
| Frame rule | Proofs about part of the heap remain valid when unrelated heap is added |

## How it fits

- **Below:** Assertions are formulas of [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md); the while rule is [induction](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) on iterations; Hoare logic is the axiomatic style of [semantics](../02-semantics-and-types/syntax-and-semantics.md). [Undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) is why invariants and variants must be supplied.
- **Above:** Separation logic underpins industrial [static analysis](../../12-software-engineering/03-quality/static-analysis-and-code-review.md); concurrent program logics verify [lock-free algorithms](../../07-operating-systems/03-concurrency/lock-free-synchronization.md); contract-style specifications improve [testing](../../12-software-engineering/03-quality/testing.md) through assertions and property checks.
- **Siblings:** [Model checking](model-checking.md) avoids invariants by exhaustive search but only on finite models; [proof assistants](proof-assistants-and-dependent-types.md) embed Hoare logic as a library and check its proofs with a trusted kernel.

## Common misconceptions

- **"A verified program cannot fail."** It meets its specification under the assumptions of the proof (compiler, hardware, environment). If the specification is wrong or incomplete, the program can be "correct" and still useless.
- **"Hoare logic proves termination."** The standard triple is partial correctness; termination needs a separate variant argument.
- **"Program proofs are only academic."** Amazon, Microsoft, Meta and the aerospace and railway industries use Hoare- and separation-logic-based tools in production.

## Go deeper

- C. A. R. Hoare, "An Axiomatic Basis for Computer Programming" (1969): the original eight-page paper.
- Edsger W. Dijkstra, *A Discipline of Programming* (1976): weakest preconditions and deriving programs from specifications.
- David Gries, *The Science of Programming* (1981): the classic practical guide to invariants and proof.
- John C. Reynolds, "Separation Logic: A Logic for Shared Mutable Data Structures" (2002): the extension that made heap reasoning modular.
