# Integers and Two's Complement

> **Layer:** [03 Digital Logic](../README.md) › [Number Representation](README.md)
> **Builds on:** [Binary and Positional Notation](binary-and-positional-notation.md), [Abstract Algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md), [Number Theory](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md)
> **Enables:** [Arithmetic and Building Blocks](../02-combinational-logic/arithmetic-and-building-blocks.md), [The ISA Contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md), [Memory Safety Vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md)

## Essence

Hardware integers are not mathematical integers. They are fixed-width bit patterns, and arithmetic on them wraps around modulo `2ⁿ`. Two's complement is the encoding of signed integers that turns this wrap-around into an advantage: it gives the most significant bit a *negative* weight, so that the very same adder circuit that adds unsigned numbers also adds signed ones correctly. That is why every modern processor uses it. The price is a set of edge cases that programmers must know: overflow, an asymmetric range with one more negative value than positive, and different behaviour for signed and unsigned comparison, division and right shift.

## Core tenets

1. **Unsigned `n`-bit arithmetic is arithmetic modulo `2ⁿ`.** An `n`-bit register holds values `0` to `2ⁿ - 1`. Addition, subtraction and multiplication keep only the low `n` bits of the true result, which is exactly reduction modulo `2ⁿ`. These operations form a ring, so familiar algebraic laws (associativity, commutativity, distributivity) still hold; only order comparisons are disturbed by wrap-around.

2. **Two's complement gives the top bit weight `-2^{n-1}`.** An `n`-bit pattern `b_{n-1} ... b_0` means `-b_{n-1} · 2^{n-1} + Σ_{i<n-1} b_i · 2ⁱ`. In 8 bits, `11111111` is `-128 + 127 = -1` and `10000000` is `-128`. Equivalently, a negative value `-x` is stored as the unsigned pattern for `2ⁿ - x`, its representative modulo `2ⁿ`.

3. **One adder serves signed and unsigned numbers alike.** Because a two's complement pattern and its unsigned reading are congruent modulo `2ⁿ`, adding the bit patterns gives the correct low `n` bits for both interpretations. Subtraction is addition of the negation, and negation is `-x = ~x + 1` (invert all bits, add one). So `a - b` is computed as `a + ~b + 1`, using the adder's carry-in for the `+1`. Alternatives such as sign-magnitude and ones' complement need extra correction logic and have two zeros; two's complement has one.

4. **The range is asymmetric.** `n` bits cover `-2^{n-1}` to `2^{n-1} - 1`: for 32 bits, about ±2.1 × 10⁹. The most negative value has no positive counterpart, so `-INT_MIN` and `abs(INT_MIN)` overflow back to `INT_MIN`. This single fact has caused many real bugs.

5. **Overflow is detected differently for signed and unsigned.** An unsigned add overflows when there is a carry out of the top bit. A signed add overflows when both operands have the same sign and the result has the other sign; in hardware, when the carry into the top bit differs from the carry out. Processors compute both conditions on every add and expose them as separate flags (carry and overflow), leaving it to software to check the one that matches its interpretation.

6. **Widening a signed value copies its sign bit.** To extend an `n`-bit two's complement value to more bits without changing its value, replicate the top bit (sign extension): `1111 1111` (-1 in 8 bits) becomes `1111 1111 1111 1111` (-1 in 16 bits). Unsigned values are zero-extended. Instruction sets therefore provide both kinds of load and shift: arithmetic right shift copies the sign bit (dividing by 2 and rounding toward negative infinity), while logical right shift fills with zeros.

7. **Languages layer different promises on the same hardware.** Most hardware wraps silently. Java defines signed overflow to wrap. C and C++ make signed overflow undefined behaviour, which lets compilers assume it never happens (for example, that `x + 1 > x` always), while unsigned arithmetic wraps by definition. Rust panics on overflow in debug builds and wraps in release builds unless asked otherwise. Mixing signed and unsigned values in comparisons can silently convert `-1` into the largest unsigned value.

8. **Integer errors become security errors.** An overflow in a size calculation such as `count * sizeof(item)` can yield a small number, causing a too-small buffer to be allocated and then overrun. Many memory-corruption vulnerabilities start with an integer that wrapped where the programmer assumed mathematical arithmetic.

## Key concepts

| Term | Meaning |
|---|---|
| Unsigned integer | Bit pattern read with all weights positive; range `0` to `2ⁿ - 1`. |
| Two's complement | Signed encoding with top-bit weight `-2^{n-1}`. |
| Ones' complement / sign-magnitude | Older signed encodings with two zeros and costlier arithmetic. |
| Overflow | A true result that does not fit the representable range. |
| Carry flag | Indicates unsigned overflow on add (or borrow on subtract). |
| Overflow flag | Indicates signed overflow. |
| Sign extension | Widening by replicating the sign bit. |
| Arithmetic / logical shift | Right shift that copies the sign bit / fills with zeros. |

## How it fits

- **Below:** Two's complement is arithmetic in the ring ℤ/2ⁿℤ from [abstract algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md) and modular arithmetic from [number theory](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md), applied to the bit patterns of [binary notation](binary-and-positional-notation.md).
- **Above:** The shared adder is built in [arithmetic and building blocks](../02-combinational-logic/arithmetic-and-building-blocks.md). Condition flags and signed/unsigned instruction variants are part of [the Instruction Set Architecture (ISA) contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md). Language rules for overflow belong to [type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md), and overflow-driven bugs appear in [memory safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md).
- **Siblings:** [Floating point](floating-point.md) gives up exactness for range; integers give up range for exactness. [Character encoding](character-encoding.md) uses unsigned integers as code points.

## Common misconceptions

- **"Overflow is an error the hardware reports."** Hardware sets flags but carries on; whether overflow is an error, wraps, or is undefined is a language decision.
- **"Negating a number always works."** Negating the most negative value overflows back to itself.
- **"Signed and unsigned need different adders."** In two's complement the same adder serves both; only overflow detection, comparison, division and right shift differ.

## Go deeper

- Randal Bryant and David O'Hallaron, *Computer Systems: A Programmer's Perspective* (2003), chapter 2: integer representation and its pitfalls.
- Henry Warren, *Hacker's Delight* (2002): bit-level tricks built on two's complement.
- Donald Knuth, *The Art of Computer Programming, Vol. 2: Seminumerical Algorithms* (1969): the arithmetic underpinnings.
