# Type Theory and Alternative Foundations

> **Layer:** [01 Sets and Foundations](../README.md) › [Axiomatic Set Theory](README.md)
> **Builds on:** [Paradoxes and naive set theory](paradoxes-and-naive-set-theory.md), [Zermelo–Fraenkel set theory](zermelo-fraenkel-set-theory.md), [The axiom of choice](the-axiom-of-choice.md), [Formal proof systems](../../00-logic-and-proof/01-formal-logic/formal-proof-systems.md), [Constructive and intuitionistic logic](../../00-logic-and-proof/03-the-axiomatic-method/constructive-and-intuitionistic-logic.md)
> **Enables:** [Categories and functors](../../13-structure-and-metamathematics/01-category-theory/categories-and-functors.md), [Higher categories and homotopy type theory](../../13-structure-and-metamathematics/01-category-theory/higher-categories-and-homotopy-type-theory.md), [Computers and proof](../../15-mathematics-in-context/computers-and-proof.md), [Philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md), [Proof assistants and dependent types (CS)](../../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md)

## Essence

Set theory is not the only possible foundation. A type theory gives every object a type when it is introduced, so a question such as "is x a member of itself?" cannot even be written down, and the paradoxes are blocked by grammar instead of by axioms. Russell's theory of types came first; Martin-Löf's dependent type theory made types into a constructive language in which proofs are programs; category-theoretic foundations take functions, not membership, as primitive. These are not rivals about what is true: ordinary mathematics can be expressed in each. They differ in what they make easy, and type theories won the proof assistants because a computer can check their proofs mechanically.

## Core tenets

1. **Types make "x ∈ x" unwritable.** In Russell's theory (1908), individuals have type 0, sets of individuals type 1, sets of those type 2, and x ∈ y is well formed only when y's type is one above x's. *Principia Mathematica* (Whitehead and Russell, 1910–1913) used a ramified version with an axiom of reducibility; Ramsey and Chwistek simplified it to simple type theory, and Church (1940) restated it with λ-notation, the basis of higher-order logic (HOL). The cost is duplication: each type has its own empty set and its own natural numbers.

2. **Typing is checked by an algorithm, not proved.** A type theory works with judgements such as "a has type A", derived by rules that are syntax-directed. In Martin-Löf type theory (MLTT) in its intensional form, whether a judgement holds is decidable, so a computer can check a proof term completely. Membership in set theory, by contrast, is a proposition that must be proved like any other.

3. **In MLTT, propositions are types and proofs are programs.** Types may depend on terms: Vec(n) is the type of lists of length n. Under the Curry–Howard correspondence, a proof of A ⇒ B is a function from proofs of A to proofs of B, a proof of ∀x B(x) is a dependent function, and a proof of ∃x B(x) is a pair of a witness and a proof. The base logic is [constructive](../../00-logic-and-proof/03-the-axiomatic-method/constructive-and-intuitionistic-logic.md): excluded middle is not built in.

4. **Choice behaves differently.** Read with Curry–Howard, "for every x there is a y with R(x, y)" already contains a function picking y, so this form of choice is a theorem of MLTT. The set-theoretic [axiom of choice](the-axiom-of-choice.md), applied to propositions whose proofs carry no data, is different: combined with function extensionality and quotients it implies excluded middle, by Diaconescu's argument. This is exactly how the Lean library derives `Classical.em` from `Classical.choice`.

5. **Universes stop types from containing themselves.** A type of all types, Type : Type, is inconsistent (Girard's paradox), the type-theoretic Russell paradox. So there is a hierarchy Type₀ : Type₁ : Type₂ : …, playing the role of Grothendieck universes. Lean and Coq (now called Rocq) also have a separate universe Prop of propositions that is impredicative: a proposition may quantify over all propositions.

6. **Category-theoretic foundations take functions as primitive.** Lawvere's elementary theory of the category of sets (ETCS, 1964) axiomatises sets and functions; an element of X is a map 1 → X from a one-point set. A question such as "is 2 ∈ 3?" cannot be asked, so junk theorems disappear. Without a replacement axiom, ETCS is weaker than Zermelo–Fraenkel set theory with choice (ZFC). Lawvere and Tierney's elementary toposes generalise it; their internal logic is intuitionistic in general and classical exactly when the topos is Boolean. Homotopy type theory adds the univalence axiom, under which equivalent structures are equal; see [higher categories and homotopy type theory](../../13-structure-and-metamathematics/01-category-theory/higher-categories-and-homotopy-type-theory.md).

7. **Proof assistants use type theories because their kernels can be small.** De Bruijn's criterion asks that every proof be checkable by a small, trusted kernel; his Automath project, begun in 1967, was the first such system. Isabelle/HOL uses higher-order logic; Coq (now called Rocq) uses the calculus of inductive constructions (CIC), and Lean a close relative of it. Set-theoretic systems exist too: Mizar is based on Tarski–Grothendieck set theory and Metamath's main library on ZFC. Landmark checks include the four colour theorem (Gonthier, 2005) and the Feit–Thompson odd order theorem (2012), both in Coq; see [computers and proof](../../15-mathematics-in-context/computers-and-proof.md).

## Key concepts

| Term | Meaning |
|---|---|
| Simple type theory | Russell's types as simplified by Ramsey and Chwistek and formalised by Church |
| HOL | higher-order logic, simple type theory with λ-terms |
| Judgement | a statement such as "a has type A", checked by rules |
| Dependent type | a type that depends on a term, such as Vec(n) |
| Curry–Howard correspondence | propositions as types, proofs as programs |
| MLTT | Martin-Löf's constructive dependent type theory |
| Universe | a type whose elements are types: Type₀ : Type₁ : … |
| ETCS | Lawvere's axioms for the category of sets |
| Topos | a category that behaves like the category of sets |
| Kernel | the small trusted program that checks every proof |

## How it fits

- **Below:** type theories answer [the paradoxes](paradoxes-and-naive-set-theory.md) differently from [Zermelo–Fraenkel set theory](zermelo-fraenkel-set-theory.md); they are [formal proof systems](../../00-logic-and-proof/01-formal-logic/formal-proof-systems.md) whose native logic is [constructive](../../00-logic-and-proof/03-the-axiomatic-method/constructive-and-intuitionistic-logic.md).
- **Above:** [categories](../../13-structure-and-metamathematics/01-category-theory/categories-and-functors.md) and [homotopy type theory](../../13-structure-and-metamathematics/01-category-theory/higher-categories-and-homotopy-type-theory.md); [computers and proof](../../15-mathematics-in-context/computers-and-proof.md) and the [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md); the computer science view is in [proof assistants and dependent types](../../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md) and [lambda calculus](../../../cs-first-principles/02-theory-of-computation/03-computability/lambda-calculus.md).
- **Siblings:** [the axiom of choice](the-axiom-of-choice.md) is where set theory and type theory most visibly part ways.

## Common misconceptions

- **"Type theory and set theory make rival claims about what mathematics is"**: each can interpret the other's ordinary mathematics; they are different languages for the same content.
- **"Proof assistants can only do constructive mathematics"**: Lean, Isabelle/HOL and Coq all support classical reasoning, and most formalised mathematics uses it.
- **"A machine-checked proof cannot be wrong"**: the kernel could have a bug, and the formal statement may not say what the author meant; checking reduces trust to a small kernel and a readable statement.

## Go deeper

- Per Martin-Löf, *Intuitionistic Type Theory* (1984): the original lectures, short and readable.
- The Univalent Foundations Program, *Homotopy Type Theory: Univalent Foundations of Mathematics* (2013): dependent types, univalence and mathematics done informally in type theory.
- F. William Lawvere and Robert Rosebrugh, *Sets for Mathematics* (2003): set theory built on functions instead of membership.
