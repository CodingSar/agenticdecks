# Boolean Algebra

> **Layer:** [01 Mathematical Foundations](../README.md) › [Algebra](README.md)
> **Builds on:** [Propositional Logic](../01-logic/propositional-logic.md), [Sets](../02-sets-relations-functions/sets.md), [Relations and Orders](../02-sets-relations-functions/relations-and-orders.md)
> **Enables:** [Logic Gates](../../03-digital-logic/02-combinational-logic/logic-gates.md), [Logic Minimization](../../03-digital-logic/02-combinational-logic/logic-minimization.md), [Arithmetic and Building Blocks](../../03-digital-logic/02-combinational-logic/arithmetic-and-building-blocks.md), [Query Optimization](../../09-data-management/03-query-processing/query-optimization.md)

## Essence

Boolean algebra is the algebra of two values, 0 and 1, under the operations AND (·), OR (+) and NOT (complement). It turns logical reasoning into symbol manipulation with equational laws, much as ordinary algebra does for numbers. George Boole introduced it in 1854 as an algebra of logic; Claude Shannon showed in his 1937 master's thesis that it exactly describes networks of relay switches, which made it the design language of every digital circuit since. The same laws govern propositional formulas, subsets of a set, and bitwise operations on machine words, so one body of theorems serves logic, set theory, hardware design and low-level programming at once.

## Core tenets

1. **One set of laws covers logic, sets and bits.** A Boolean algebra is a set with ∧, ∨, ¬, 0 and 1 obeying commutativity, associativity, distributivity (both ways), identity (`x ∨ 0 = x`, `x ∧ 1 = x`) and complement (`x ∨ ¬x = 1`, `x ∧ ¬x = 0`). Truth values, subsets of a set under ∪ ∩ and complement, and *n*-bit words under `| & ~` all satisfy these laws. So a fact proved once, such as De Morgan's law, holds for formulas, sets and bitmasks alike.

2. **Both operations distribute over each other, unlike ordinary arithmetic.** `x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z)` and also `x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z)`. The second law has no counterpart for + and × on numbers. It is why any expression can be pushed into either sum-of-products or product-of-sums form, which correspond to two-level AND–OR and OR–AND circuits.

3. **Duality halves the work.** Swapping ∧ with ∨ and 0 with 1 in any law gives another valid law. De Morgan's laws, `¬(x ∧ y) = ¬x ∨ ¬y` and `¬(x ∨ y) = ¬x ∧ ¬y`, are the bridge: they let a designer convert AND-OR logic into NAND-NAND logic, which matters because a Complementary Metal-Oxide-Semiconductor (CMOS) NAND gate is smaller and faster than an AND gate (an AND is a NAND plus an inverter).

4. **Every Boolean function has a canonical form, and therefore a circuit.** Any function of *n* inputs equals the OR of its *minterms*, one AND term per input combination that yields 1. This sum-of-products form exists for every function, which proves that AND, OR and NOT, and hence NAND alone, can build any combinational circuit. The canonical form is usually far from minimal, which is why [logic minimization](../../03-digital-logic/02-combinational-logic/logic-minimization.md) exists.

5. **Simplification laws reduce circuit size and delay.** Absorption (`x ∨ (x ∧ y) = x`), idempotence (`x ∨ x = x`) and consensus (`xy ∨ ¬xz ∨ yz = xy ∨ ¬xz`) remove redundant terms. Fewer literals means fewer transistors, less power and shorter critical paths. Karnaugh maps and the Quine–McCluskey method are systematic ways of applying these laws; finding a truly minimal circuit in general is computationally hard.

6. **Shannon expansion splits a function on one variable.** `f = x·f(x=1) + ¬x·f(x=0)`. Applied recursively it gives a decision tree, which is how a multiplexer implements any function and how Binary Decision Diagrams (BDDs) represent functions compactly. Reduced ordered BDDs are canonical for a fixed variable order, so two circuits are equivalent exactly when their BDDs are identical, a basis of hardware equivalence checking and early [model checking](../../06-programming-languages/05-formal-methods/model-checking.md).

7. **Exclusive OR adds a ring structure that arithmetic and codes need.** Exclusive OR (XOR) is addition modulo 2: `x ⊕ x = 0` and `x ⊕ 0 = x`. With AND as multiplication, {0, 1} becomes the field GF(2), the Galois field with two elements. A half adder's sum bit is XOR and its carry is AND; parity checks, Cyclic Redundancy Checks (CRCs), stream ciphers and Redundant Array of Independent Disks (RAID) level 5 parity are all XOR arithmetic. XOR is its own inverse, which is why `c = m ⊕ k` and `m = c ⊕ k` use the same operation.

8. **Bitwise operations are Boolean algebra in parallel.** A 64-bit `&` computes 64 independent ANDs in one instruction. Bitsets, Bloom filters, chess move generators and database bitmap indexes exploit this to evaluate set operations on 64 elements per cycle, or more with Single Instruction, Multiple Data (SIMD) registers.

## Key concepts

| Term | Meaning |
|---|---|
| Boolean algebra | A structure with ∧, ∨, ¬, 0, 1 satisfying the standard laws |
| De Morgan's laws | Complement swaps ∧ and ∨ |
| Duality | Exchange ∧/∨ and 0/1 to turn one law into another |
| Minterm / maxterm | AND of all variables (each possibly negated) / OR of all variables |
| Sum of products (SOP) | OR of AND terms; maps to two-level AND–OR logic |
| Absorption | `x ∨ xy = x`, `x(x ∨ y) = x` |
| Shannon expansion | `f = x·f₁ + ¬x·f₀`, splitting on variable `x` |
| BDD | Graph representation of a Boolean function from repeated Shannon expansion |
| XOR / GF(2) | Addition mod 2; the two-element field |

## How it fits

- **Below:** It is the algebraic form of [propositional logic](../01-logic/propositional-logic.md) and of [set operations](../02-sets-relations-functions/sets.md); order-theoretically, a Boolean algebra is a complemented distributive [lattice](../02-sets-relations-functions/relations-and-orders.md).
- **Above:** [Logic gates](../../03-digital-logic/02-combinational-logic/logic-gates.md) implement its operations in transistors, [adders](../../03-digital-logic/02-combinational-logic/arithmetic-and-building-blocks.md) are built from its formulas, and [hardware description languages](../../03-digital-logic/04-hardware-design/hardware-description-languages.md) compile to it. Query optimisers rewrite `WHERE` predicates with its laws. Compilers simplify conditions and bit manipulations with it.
- **Siblings:** [Abstract algebra](abstract-algebra.md) places Boolean algebra among rings and fields (GF(2) and Boolean rings). [Linear algebra](linear-algebra.md) over GF(2) is the mathematics of parity and linear error-correcting codes.

## Common misconceptions

- **"Boolean algebra is just logic with different symbols."** It is a general algebraic structure with many models (power sets, bit vectors), which is exactly why it applies to hardware and data structures.
- **"`+` in Boolean algebra behaves like ordinary addition."** `1 + 1 = 1` for OR; the operation that behaves like addition mod 2 is XOR.
- **"The canonical sum of products is a good circuit."** It can have 2^n terms; it proves existence, not efficiency.

## Go deeper

- Claude Shannon, "A Symbolic Analysis of Relay and Switching Circuits" (1938, from his 1937 thesis): the paper that connected Boole to hardware.
- M. Morris Mano and Michael Ciletti, *Digital Design* (6th ed., 2018): Boolean algebra applied to circuit design.
- Donald Knuth, *The Art of Computer Programming, Vol. 4A: Combinatorial Algorithms* (2011): bitwise tricks and BDDs in depth.
