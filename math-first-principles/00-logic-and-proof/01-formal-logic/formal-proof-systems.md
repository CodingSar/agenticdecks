# Formal Proof Systems

> **Layer:** [00 Logic and Proof](../README.md) › [Formal Logic](README.md)
> **Builds on:** [Propositional Logic](propositional-logic.md), [Predicate Logic and Quantifiers](predicate-logic-and-quantifiers.md)
> **Enables:** [Soundness, Completeness and Compactness](soundness-completeness-and-compactness.md), [What a Proof Is](../02-methods-of-proof/what-a-proof-is.md), [Proof Theory and Reverse Mathematics](../../13-structure-and-metamathematics/02-computability-and-incompleteness/proof-theory-and-reverse-mathematics.md), [Computers and Proof](../../15-mathematics-in-context/computers-and-proof.md), [Proof Assistants and Dependent Types](../../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md)

## Essence

A formal proof system consists of axioms and rules of inference; a derivation is a finite list of formulas, each an axiom, a premise, or the result of a rule applied to earlier lines. Γ ⊢ φ means that a derivation of φ from premises in Γ exists, a purely syntactic fact. Hilbert systems, natural deduction, the sequent calculus and resolution derive exactly the same first-order consequences; they differ in how natural proofs look, how easily they are found and how long they must be. Separating ⊢ from ⊨ lets one ask whether the rules prove only truths, and all of them.

## Core tenets

1. **Checking a proof is mechanical; finding one is not.** Rules look only at the shapes of formulas, so a short program blind to their meaning decides whether a list is a derivation: a formal proof is a certificate that needs no trust. Finding one is different: for first-order logic no algorithm decides whether one exists, and for propositional logic no efficient method is known.

2. **A Hilbert system uses many axioms and one rule.** For ¬ and ⇒ (the others being abbreviations), three axiom schemes and modus ponens suffice; every instance of a scheme is an axiom. Even φ ⇒ φ takes five lines:

```
A1  φ ⇒ (ψ ⇒ φ)
A2  (φ ⇒ (ψ ⇒ χ)) ⇒ ((φ ⇒ ψ) ⇒ (φ ⇒ χ))
A3  (¬ψ ⇒ ¬φ) ⇒ (φ ⇒ ψ)
MP  from φ and φ ⇒ ψ, infer ψ        (modus ponens)

1  (φ ⇒ ((φ ⇒ φ) ⇒ φ)) ⇒ ((φ ⇒ (φ ⇒ φ)) ⇒ (φ ⇒ φ))   A2 with ψ := φ ⇒ φ, χ := φ
2  φ ⇒ ((φ ⇒ φ) ⇒ φ)                                   A1 with ψ := φ ⇒ φ
3  (φ ⇒ (φ ⇒ φ)) ⇒ (φ ⇒ φ)                             MP from 2 and 1
4  φ ⇒ (φ ⇒ φ)                                         A1 with ψ := φ
5  φ ⇒ φ                                               MP from 4 and 3
```

3. **The deduction theorem turns hypotheses into implications.** If Γ ∪ {φ} ⊢ ψ then Γ ⊢ φ ⇒ ψ, which licenses the everyday "assume φ and derive ψ". By induction on the derivation: an axiom or premise χ becomes φ ⇒ χ through A1, the line φ itself becomes φ ⇒ φ as above, and each use of modus ponens is rebuilt with A2. First-order logic needs a proviso: generalisation gives ∀x P(x) from P(x), yet P(x) ⇒ ∀x P(x) is not valid, so the derivation must not generalise on a variable free in φ.

4. **Natural deduction mirrors how mathematicians argue.** Gentzen (1934–35) and, independently, Jaśkowski (1934) replaced axioms by an introduction rule (how to prove) and an elimination rule (how to use) for each connective and quantifier. To prove ∀x φ(x), prove φ(x) for an x occurring in no open assumption, the formal "let x be arbitrary"; to use ∃x φ(x), assume φ(c) for a new name c and reach a conclusion that does not mention c. These rules give intuitionistic logic; classical logic needs one more, such as double-negation elimination.

5. **Cut elimination: every proof can be made direct.** The sequent calculus derives sequents Γ ⊢ Δ, read "if all of Γ hold, some formula of Δ holds". Its cut rule is the formal use of a lemma: from Γ ⊢ Δ, A and A, Γ ⊢ Δ infer Γ ⊢ Δ, and it is the only rule whose premises contain a formula absent from its conclusion. Gentzen's Hauptsatz says cuts can be removed, so a provable sequent has a proof built from its own subformulas; consistency follows, since no cut-free proof ends in the empty sequent. The price is length, which can grow by a tower of exponentials.

6. **Resolution is a single rule built for machines.** Premises and the negated goal become clauses, disjunctions of literals; from A ∨ p and B ∨ ¬p resolution infers A ∨ B, and a clause set is unsatisfiable if and only if repeated resolution reaches the empty clause. Lifted to first-order logic by J. A. Robinson (1965), it underlies Prolog and satisfiability (SAT) solvers. Haken (1985) showed that resolution needs exponentially long refutations of the pigeonhole principle (n + 1 pigeons do not fit in n holes). Cook and Reckhow (1979) showed that some proof system has polynomial-size proofs of all tautologies if and only if NP = coNP, where NP is the class of problems whose "yes" answers have certificates checkable in polynomial time and coNP the class whose "no" answers do: open as of 2026.

7. **Soundness and completeness are theorems about a system, not definitions.** A system is sound if Γ ⊢ φ implies Γ ⊨ φ and complete if the converse holds; neither is automatic. Without A3 the system stays sound but cannot derive ¬¬p ⇒ p, since reading ¬ as constantly true keeps every derivable formula a tautology. Second-order logic with full semantics has no sound, complete, effective system, since its validities cannot be listed.

## Key concepts

| Term | Meaning |
|---|---|
| Axiom scheme | A pattern every instance of which is an axiom |
| Derivation | A finite list of formulas, each an axiom, a premise or the result of a rule |
| Γ ⊢ φ | Some derivation of φ from premises in Γ exists |
| Deduction theorem | Γ ∪ {φ} ⊢ ψ implies Γ ⊢ φ ⇒ ψ |
| Natural deduction | Introduction and elimination rules for each connective and quantifier |
| Sequent | Γ ⊢ Δ: if all of Γ hold, some formula of Δ holds |
| Cut elimination | Every sequent-calculus proof can be rewritten without the cut rule |
| Resolution | From A ∨ p and B ∨ ¬p infer A ∨ B |

## How it fits

- **Below:** [Propositional Logic](propositional-logic.md) and [Predicate Logic and Quantifiers](predicate-logic-and-quantifiers.md) supply the formulas and the truth that the rules must respect.
- **Above:** proof assistants such as Coq, Isabelle and Lean check formal derivations ([Computers and Proof](../../15-mathematics-in-context/computers-and-proof.md), [Proof Assistants and Dependent Types](../../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md)); [Proof Theory and Reverse Mathematics](../../13-structure-and-metamathematics/02-computability-and-incompleteness/proof-theory-and-reverse-mathematics.md) studies derivations as mathematical objects.
- **Siblings:** [Soundness, Completeness and Compactness](soundness-completeness-and-compactness.md) proves that these rules capture ⊨ exactly; [What a Proof Is](../02-methods-of-proof/what-a-proof-is.md), in Methods of Proof, relates derivations to written proofs.

## Common misconceptions

- **"Mathematicians write formal proofs"**: published proofs are informal arguments that could be expanded into derivations, which is rarely done outside proof assistants.
- **"The proof system defines what is true"**: truth is defined by structures; a proof system is judged against it and can prove too little or, if unsound, falsehoods.
- **"Removing cuts makes proofs simpler"**: cut-free proofs are more direct but can be enormously longer; lemmas keep real proofs short.

## Go deeper

- M. E. Szabo (editor), *The Collected Papers of Gerhard Gentzen* (1969): includes "Investigations into Logical Deduction" (1934–35), the origin of natural deduction and the sequent calculus.
- Sara Negri and Jan von Plato, *Structural Proof Theory* (2001): cut elimination and natural deduction in modern form.
