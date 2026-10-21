# Number Representation

> **Layer:** [03 Digital Logic](../README.md) › Number Representation
> **Children:** [Binary and Positional Notation](binary-and-positional-notation.md) · [Integers and Two's Complement](integers-and-twos-complement.md) · [Floating Point](floating-point.md) · [Character Encoding](character-encoding.md)

## What this area is about

Hardware stores and moves only fixed-width strings of bits. Programs need integers, real numbers and text. This area answers: *how do we encode mathematical and human objects as finite bit patterns, and what do those encodings make cheap, expensive or impossible?* It sits in Digital Logic rather than Mathematical Foundations because these are engineering encodings: their quirks, such as overflow, rounding, an asymmetric integer range or a string whose length depends on how you count, come from the finiteness of hardware, not from the mathematics they approximate.

The unifying idea is that **a bit pattern has no meaning until an encoding gives it one, and the encoding decides which operations are cheap**. Positional binary makes counting and shifting cheap. Two's complement makes signed and unsigned addition the same circuit. Floating point makes huge ranges cheap at the cost of exactness. UTF-8 (Unicode Transformation Format, 8-bit) makes byte-oriented text processing that is compatible with the American Standard Code for Information Interchange (ASCII) cheap text processing cheap at the cost of random access by character.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Binary and Positional Notation](binary-and-positional-notation.md) | The base: weights, `2ⁿ` patterns, hex, shifts, fixed width, byte order | Digital abstraction, number theory |
| [Integers and Two's Complement](integers-and-twos-complement.md) | Exact integers as arithmetic modulo `2ⁿ`; one adder for signed and unsigned; overflow | Binary |
| [Floating Point](floating-point.md) | Approximate reals with constant relative precision; Institute of Electrical and Electronics Engineers (IEEE) 754 correct rounding and special values | Binary, integers |
| [Character Encoding](character-encoding.md) | Text as code points and variable-length byte sequences; ASCII, Unicode, UTF-8 | Binary |

Read binary first: it establishes that `n` bits name `2ⁿ` things and that fixed width means modular arithmetic. Integers then turn modularity into a representation of negative numbers. Floating point builds on integers (its exponent and significand are integer fields) to trade exactness for range. Character encoding is the non-numeric case, showing the same principles applied to human symbols, with variable length as the new complication.

```
                       binary & positional notation
                (n bits = 2^n patterns, fixed width = mod 2^n)
                 ┌────────────────┼──────────────────┐
                 ▼                ▼                  ▼
          integers (exact,   floating point     character encoding
          small range)       (approx., huge     (symbols, variable
                 └──────────► range; uses        length)
                              integer fields)
```

## Connections to sibling areas

- **[Combinational Logic](../02-combinational-logic/README.md):** Encodings are chosen so that circuits are simple. Two's complement exists so that one adder serves signed and unsigned values; the adders, shifters and comparators there operate directly on these representations.
- **[Sequential Logic](../03-sequential-logic/README.md):** Registers hold fixed-width words, which is why width is fixed. State encodings for finite state machines (binary, one-hot, Gray) are another representation choice with cost consequences.
- **[Hardware Design](../04-hardware-design/README.md):** Wider formats cost area, delay and energy; the move to 16-bit and 8-bit floating point in accelerators is a timing-and-power decision.

## Connections across layers

The two-level choice comes from [analog vs digital](../../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md); the arithmetic is [number theory](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md) and [abstract algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md) on finite sets. Upward, these encodings fix the operand types of [the Instruction Set Architecture (ISA) contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) and the layout of [instruction encoding](../../04-computer-architecture/01-instruction-set-architecture/instruction-encoding-and-addressing.md). They become the primitive types of [type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md), the source of overflow-based [memory safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md), the numerical substrate of [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md), and the text of [the Hypertext Transfer Protocol (HTTP) and the web](../../08-networking/05-application-layer/http-and-the-web.md). The question of how *few* bits suffice is answered by [entropy and information](../../02-theory-of-computation/01-information-theory/entropy-and-information.md).

## Cross-cutting threads

- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): the central theme; each encoding makes some operations cheap and others costly.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): exactness against range, compactness against random access, precision against energy.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): `n` bits name only `2ⁿ` values, so overflow and rounding are unavoidable.
- [Interface vs implementation](../../CROSS-CUTTING.md#interface-vs-implementation): Unicode code points (what) are separate from UTF-8 bytes (how).
