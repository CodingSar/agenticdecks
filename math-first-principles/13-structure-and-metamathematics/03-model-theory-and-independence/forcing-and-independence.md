# Forcing and Independence

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Model theory and independence](README.md)
> **Builds on:** [Zermelo–Fraenkel set theory](../../01-sets-and-foundations/03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md), [The axiom of choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md), [Cardinal numbers](../../01-sets-and-foundations/02-infinity-and-cardinality/cardinal-numbers.md), [Models and the Löwenheim–Skolem theorems](models-and-the-lowenheim-skolem-theorems.md), [Gödel's incompleteness theorems](../02-computability-and-incompleteness/godels-incompleteness-theorems.md)
> **Enables:** [Large cardinals](large-cardinals.md), [Philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md), [Open problems](../../15-mathematics-in-context/open-problems.md)

## Essence

Cantor's continuum hypothesis (CH), that every infinite set of reals is either countable or the size of ℝ, was the first of Hilbert's 1900 problems. It is neither provable nor refutable in Zermelo–Fraenkel set theory with the axiom of choice (ZFC), if ZFC is consistent. Gödel showed in 1938 that CH holds in the constructible universe L, a minimal model built from definable sets; Paul Cohen showed in 1963 that it fails in models obtained by forcing, a method for adjoining a new "generic" set to a model while keeping control of what becomes true. Forcing has since shown that much of infinite combinatorics is independent of ZFC.

## Core tenets

1. **Independence results are relative consistency proofs.** By Gödel's second theorem ZFC cannot prove its own consistency, so the theorems take the form: if ZFC is consistent, so are ZFC + CH and ZFC + ¬CH. Each is proved by turning a model of ZFC into a model of the extended theory, or, syntactically, by turning a hypothetical proof of a contradiction from the extension into one from ZFC.

2. **Gödel's L: build the universe from definable sets only.** Let L₀ = ∅, let L_{α+1} be the set of subsets of L_α definable over L_α with parameters, and take unions at limits; L is the union over all ordinals. L satisfies ZF, the axiom of choice, since a definable well-ordering exists, and the generalised continuum hypothesis (GCH), 2^κ = κ⁺ for every infinite κ. The key is condensation: a countable elementary substructure of some L_α collapses, by Mostowski's collapse, onto some L_β with β countable, so every constructible subset of ω appears before stage ω₁ and there are only ℵ₁ of them. Gödel announced this in 1938 and published the monograph in 1940.

3. **Refuting CH needs a bigger model.** If V = L holds, L is the only inner model containing all the ordinals, and it satisfies CH, so ¬CH cannot be reached by shrinking. Cohen's idea was to enlarge a countable transitive model M of ZFC by a new set G that M cannot describe but whose effect M can still compute.

4. **Forcing adjoins a generic object.** For ¬CH take the partial order P of finite partial functions from ω₂ × ω to {0, 1}, with ω₂ computed in M, ordered by extension; each condition is a finite piece of information about ℵ₂ new subsets of ω. A filter G on P is generic if it meets every dense subset of P lying in M; since M is countable, such G exists by the Rasiowa–Sikorski lemma, a form of the Baire category theorem. M[G] consists of the values of names, objects of M describing elements of M[G] in terms of G. The forcing theorem says that every statement true in M[G] is forced by some condition in G, and that forcing is definable in M.

5. **The countable chain condition keeps cardinals from collapsing.** Every set of pairwise incompatible conditions in P is countable, by the Δ-system lemma, and this implies that M and M[G] have the same cardinals. The union of G gives ℵ₂ distinct subsets of ω, so 2^(ℵ₀) ≥ ℵ₂ in M[G] and CH fails. The only restriction ZFC places on 2^(ℵ₀) is König's theorem: its cofinality is uncountable, so it can be ℵ₁, ℵ₂ or ℵ_(ω+1) but not ℵ_ω. William Easton (1970) showed that for regular cardinals κ the function κ ↦ 2^κ is almost arbitrary.

6. **Forcing settles the independence of many classical questions.** Cohen also showed that the axiom of choice is independent of ZF. Suslin's hypothesis, that a complete dense linear order without endpoints in which every family of disjoint open intervals is countable must be isomorphic to ℝ, is independent (Thomas Jech, 1967, and Stanley Tennenbaum, 1968, for failure; Robert Solovay and Tennenbaum, 1971, for consistency). Saharon Shelah (1974) showed that Whitehead's problem in abelian group theory is independent.

7. **New axioms have not settled CH as of 2026.** Azriel Lévy and Solovay (1967) showed that large cardinals are preserved by small forcing, so they cannot decide CH. Forcing axioms such as Martin's Maximum (Matthew Foreman, Menachem Magidor and Shelah, 1988) imply 2^(ℵ₀) = ℵ₂, while W. Hugh Woodin, who earlier argued against CH, has more recently proposed an axiom "V = Ultimate L" under which CH holds. There is no consensus as of 2026.

## Key concepts

| Term | Meaning |
|---|---|
| Continuum hypothesis (CH) | 2^(ℵ₀) = ℵ₁ |
| Constructible universe L | The sets built in stages from definable subsets |
| Inner model | A transitive class model of ZF containing all ordinals |
| Forcing poset | A partial order of conditions, pieces of information about a new set |
| Generic filter | A filter meeting every dense set of the ground model |
| Name | An object of M that denotes an element of M[G] |
| Countable chain condition | Every antichain is countable, so cardinals are preserved |

## How it fits

- **Below:** It builds models of [ZFC](../../01-sets-and-foundations/03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md) with prescribed [cardinal arithmetic](../../01-sets-and-foundations/02-infinity-and-cardinality/cardinal-numbers.md) and [choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md), and is the strongest instance of proving independence by [models](models-and-the-lowenheim-skolem-theorems.md), made necessary by [Gödel](../02-computability-and-incompleteness/godels-incompleteness-theorems.md).
- **Above:** The [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) asks whether CH has a determinate truth value, and the status of CH is among the [open problems](../../15-mathematics-in-context/open-problems.md) of a foundational kind.
- **Siblings:** [Large cardinals](large-cardinals.md) are the other main source of new axioms; topos theory recasts forcing as sheaves on the forcing poset.

## Common misconceptions

- **"Forcing might show the Riemann hypothesis independent of ZFC."**: The Riemann hypothesis is equivalent to a Π⁰₁ statement about integers, and arithmetic statements are absolute: M and M[G] have the same natural numbers, so forcing cannot change them. Shoenfield's absoluteness theorem extends this to Σ¹₂ statements.
- **"Independent means meaningless."**: Independence is a fact about ZFC; many set theorists hold that CH is true or false and that new axioms should decide it.

## Go deeper

- Paul Cohen, *Set Theory and the Continuum Hypothesis* (1966): the inventor's own account.
- Kenneth Kunen, *Set Theory: An Introduction to Independence Proofs* (1980): the standard textbook.
- Thomas Jech, *Set Theory* (3rd millennium edition, 2003): the comprehensive reference.
- Timothy Chow, "A Beginner's Guide to Forcing" (2009): the motivation without the technicalities.
