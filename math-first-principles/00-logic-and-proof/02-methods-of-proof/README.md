# Methods of Proof

> **Layer:** [00 Logic and Proof](../README.md) › Methods of Proof
> **Children:** [What a Proof Is](what-a-proof-is.md) · [Direct Proof, Contraposition and Contradiction](direct-proof-contraposition-and-contradiction.md) · [Cases, Constructions and Counterexamples](cases-constructions-and-counterexamples.md) · [Mathematical Induction](mathematical-induction.md)

## What this area is about

This area is about how proofs are actually written: the small number of argument shapes that, combined, make up almost every proof in mathematics. A written proof is a compressed formal derivation, and its shape is dictated by the logical form of the statement. To prove an implication, assume the hypothesis; to prove "for all", take an arbitrary object; to prove "there exists", produce one or show that its absence is impossible; to prove something for every natural number, give a base case and a step.

The unifying idea is that each method is a valid inference pattern, justified by a tautology or a rule of logic, and that choosing among them is a matter of which formulation of the problem gives the most to work with. Knowing the methods also means knowing their failure modes: missed cases, circular steps, an inductive step that breaks at one value, a contradiction produced by a slip.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [What a Proof Is](what-a-proof-is.md) | What counts as a proof, how logical form gives its skeleton, why evidence is not proof | Formal Logic |
| [Direct Proof, Contraposition and Contradiction](direct-proof-contraposition-and-contradiction.md) | The three ways to prove an implication or a single statement | What a Proof Is |
| [Cases, Constructions and Counterexamples](cases-constructions-and-counterexamples.md) | Disjunctions, existence and refutation | What a Proof Is, Direct Proof |
| [Mathematical Induction](mathematical-induction.md) | Statements about every natural number, and everything built by rules | What a Proof Is, Direct Proof |

Start with what a proof is, then the methods for implications. Cases and induction are siblings that both build on direct proof: one handles finitely many possibilities, the other infinitely many arranged in a well-founded order.

```
              What a Proof Is
                     │
     Direct, Contraposition, Contradiction
              ┌──────┴───────┐
   Cases, Constructions    Mathematical
   and Counterexamples      Induction
```

## Connections to sibling areas

- [Formal Logic](../01-formal-logic/README.md) supplies the rules that these methods use informally: natural deduction is the formal version of "assume P and derive Q", and the tautology (¬Q ⇒ ¬P) ⇔ (P ⇒ Q) justifies contraposition. In return, induction from this area proves the soundness and completeness theorems there.
- [The Axiomatic Method](../03-the-axiomatic-method/README.md) fixes the starting points that proofs start from and asks which of these methods are constructive: proof by contradiction of a positive statement and non-constructive existence proofs are exactly what intuitionistic logic gives up.

## Connections across layers

Upward, these methods are used everywhere, but some layers rest on particular ones. Induction becomes an axiom in [Number Systems](../../02-number-systems/README.md) and is extended to the transfinite in [Sets and Foundations](../../01-sets-and-foundations/README.md). Pigeonhole, counting and the probabilistic method in [Combinatorics and Graph Theory](../../03-combinatorics-and-graph-theory/README.md) are engines of non-constructive existence. Diagonal arguments by contradiction lead to the impossibility theorems of [Structure and Metamathematics](../../13-structure-and-metamathematics/README.md). [Mathematics in Context](../../15-mathematics-in-context/README.md) asks how proofs are discovered and how computers now check them.

## Cross-cutting threads

- [Induction and recursion](../../CROSS-CUTTING.md#induction-and-recursion): induction proves what recursion defines.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): constructive and non-constructive existence proofs.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): only proof, never search, establishes that something cannot exist.
- [Invariants](../../CROSS-CUTTING.md#invariants): a strengthened inductive hypothesis is an invariant preserved by each step.
- [Extremal principles and optimisation](../../CROSS-CUTTING.md#extremal-principles-and-optimisation): the least counterexample and infinite descent pick an extreme case and show it cannot exist.
