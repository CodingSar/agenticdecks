# Proof Assistants and Dependent Types

> **Layer:** [06 Programming Languages](../README.md) › [Formal Methods](README.md)
> **Builds on:** [Type systems](../02-semantics-and-types/type-systems.md), [Proof techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md), [Lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md), [Functional programming](../01-paradigms/functional.md)
> **Enables:** [Kernel architectures](../../07-operating-systems/01-kernel-and-abstractions/kernel-architectures.md), [Foundations of modern cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md), [Static analysis and code review](../../12-software-engineering/03-quality/static-analysis-and-code-review.md)

## Essence

A proof assistant (interactive theorem prover) is a program in which a human writes definitions, specifications and proofs, and the machine checks every step. The user states a goal and applies tactics that break it into subgoals; the system refuses any unjustified step. Most modern assistants (Coq, now renamed Rocq; Lean; Agda) are based on dependent type theory, where types can depend on values, so a type can express a complete specification ("a sorted list that is a permutation of the input") and a program of that type is a proof that the specification holds. Isabelle/HOL and HOL4, both named after higher-order logic (HOL), follow a different tradition with a small trusted kernel but share the same goal. The single idea is **reduce trust in a huge proof to trust in a tiny checker**: however long or automated the proof search, a small kernel independently verifies the final result.

## Core tenets

1. **The de Bruijn criterion: trust only a small kernel.** Proofs may be produced by complex tactics, automation and external solvers, but every proof is ultimately reduced to a term that a small, simple kernel checks. Tactic bugs cannot make a false theorem accepted. The Logic for Computable Functions (LCF) approach (Milner, 1970s) achieves this by making "theorem" an abstract type that only the kernel's inference rules can construct.
2. **Propositions are types, proofs are programs.** By the Curry–Howard correspondence, the proposition `A → B` is the type of functions from proofs of `A` to proofs of `B`; proving it means writing such a function. Type checking a proof term is therefore proof checking, and a type checker is a proof checker.
3. **Dependent types let types mention values.** A type such as `Vec A n` (vectors of exactly `n` elements) depends on the number `n`. Function types generalise to Π-types: `append : (n m : Nat) → Vec A n → Vec A m → Vec A (n + m)` states and enforces the length of the result. Σ-types pair a value with a proof about it, such as "a natural number together with a proof that it is prime".

   ```lean
   def head {α : Type} : (xs : List α) → xs ≠ [] → α
     | x :: _, _ => x          -- the empty case is impossible, and the checker knows it
   ```

4. **Termination is required for logical consistency.** If any function could loop forever, a non-terminating term could inhabit every type, including `False`, and every proposition would be "provable". Proof assistants therefore only accept functions they can show terminate, typically by structural recursion or a supplied well-founded measure. This makes their programming languages deliberately not Turing complete in their core.
5. **Type checking requires deciding equality of terms.** To check that a `Vec A (2 + 3)` is a `Vec A 5`, the checker must compute. Definitional equality (equality by evaluation) is checked automatically; propositional equality (equality that needs a proof) must be proved by the user.
6. **Induction is the workhorse, and tactics automate the routine.** Most proofs about programs go by [structural induction](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) over data types or derivations. Tactics (`induction`, `simp`, `omega`, `auto`) handle bookkeeping, arithmetic and rewriting, and "hammers" call external automated provers and reconstruct their answers as kernel-checkable proofs.
7. **Verified software is real, and it costs a lot of proof.** CompCert (Leroy, 2009) is a C compiler proved in Coq to preserve semantics; Csmith random testing found many wrong-code bugs in the GNU Compiler Collection and LLVM but none in CompCert's verified middle end (Yang et al., 2011). seL4 (Klein et al., 2009) is an operating-system microkernel with a machine-checked proof of functional correctness in Isabelle/HOL; its roughly 8,700 lines of C (plus about 600 of assembly) needed about 200,000 lines of proof and roughly 20 person-years. Proof-to-code ratios of 10:1 or more are typical.
8. **Proof assistants now check mathematics as well as software.** The Four Colour Theorem (Gonthier, 2005) and the Kepler conjecture (Flyspeck project, completed 2014) were formally verified, and Lean's mathlib library holds a large, growing body of formalised mathematics.

## Key concepts

| Term | Meaning |
|---|---|
| Proof assistant | An interactive system for writing and mechanically checking proofs |
| Trusted kernel | The small core whose correctness the whole system's soundness relies on |
| Tactic | A command that transforms a proof goal into simpler subgoals |
| Dependent type | A type that depends on a value, such as `Vec A n` |
| Π-type (dependent function) | A function type whose result type depends on the argument value |
| Σ-type (dependent pair) | A pair whose second component's type depends on the first |
| Curry–Howard correspondence | Propositions correspond to types and proofs to programs |
| Definitional equality | Equality the checker establishes by computation alone |
| Calculus of Inductive Constructions | The dependent type theory underlying Coq/Rocq and, in a variant, Lean |
| Program extraction | Producing executable code from a constructive proof |

## How it fits

- **Below:** It extends [type systems](../02-semantics-and-types/type-systems.md) and the typed [lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md) until they become a logic; it mechanises the [proof techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md) of mathematics; its programs are [functional](../01-paradigms/functional.md) and total. [Gödel's incompleteness](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) and undecidability mean not every true statement can be proved or found automatically.
- **Above:** Verified [microkernels](../../07-operating-systems/01-kernel-and-abstractions/kernel-architectures.md) (seL4), verified compilers, and verified cryptographic code (such as the HACL* library used in Firefox) rest on proof assistants; security proofs in [modern cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md) are increasingly machine-checked. They define the top of the assurance ladder in [software quality](../../12-software-engineering/03-quality/README.md), above testing and [static analysis](../../12-software-engineering/03-quality/static-analysis-and-code-review.md).
- **Siblings:** [Hoare logic](hoare-logic-and-program-proofs.md) is commonly embedded inside a proof assistant as a library; [model checking](model-checking.md) is automatic but finite, whereas proof assistants handle unbounded systems at the cost of human effort.

## Common misconceptions

- **"A machine-checked proof guarantees the system is correct."** It guarantees the stated theorem follows from the stated assumptions. The specification, the model of the hardware and compiler, and the kernel itself remain trusted.
- **"Dependent types are only for proofs."** Languages such as Idris and Agda, and refinement-typed languages, use them for everyday programming, for example to rule out out-of-bounds indexing at compile time.
- **"Proof assistants find proofs automatically."** They check proofs and automate routine steps; the overall proof structure and key insights still come from people.

## Go deeper

- Benjamin C. Pierce et al., *Software Foundations* (online, ongoing since 2007): learning Coq by proving properties of programs.
- Xavier Leroy, "Formal Verification of a Realistic Compiler" (2009): the CompCert project.
- Gerwin Klein et al., "seL4: Formal Verification of an OS Kernel" (2009): full functional verification of a microkernel.
