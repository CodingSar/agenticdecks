# Binary and Positional Notation

> **Layer:** [03 Digital Logic](../README.md) › [Number Representation](README.md)
> **Builds on:** [Analog vs Digital](../../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md), [Number Theory](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md), [Combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md)
> **Enables:** [Integers and Two's Complement](integers-and-twos-complement.md), [Floating Point](floating-point.md), [Character Encoding](character-encoding.md), [Instruction Encoding and Addressing](../../04-computer-architecture/01-instruction-set-architecture/instruction-encoding-and-addressing.md)

## Essence

Digital hardware can reliably distinguish only two voltage levels, so everything a computer stores is a string of binary digits (bits). Positional notation is the idea that makes short strings stand for large numbers: each digit's weight is a power of the base, so `n` bits can name `2ⁿ` distinct values and a number `N` needs only about `log₂ N` bits. But a bit pattern has no meaning on its own. The same 32 bits can be an unsigned integer, a signed integer, a floating-point number, four characters or a machine instruction; meaning comes entirely from the interpretation the program or hardware applies. Choosing that interpretation, an encoding, decides which operations are cheap.

## Core tenets

1. **Positional notation gives each digit a weight that is a power of the base.** A string `d_{n-1} ... d_1 d_0` in base `b` means `Σ d_i · bⁱ`. In base 2, `1101` is `8 + 4 + 0 + 1 = 13`. Because weights grow geometrically, the number of digits needed grows only logarithmically with the value, which is why a 64-bit word can count to about 1.8 × 10¹⁹.

2. **Base 2 is chosen for physics, not mathematics.** Any base works mathematically. Two levels give the largest noise margin for a given voltage swing and map directly onto a transistor that is on or off. Multi-level encodings are used where density matters more than margin: flash cells store 3 or 4 bits by distinguishing 8 or 16 charge levels, and fast links send 2 bits per symbol with four-level Pulse-Amplitude Modulation (PAM4).

3. **`n` bits name exactly `2ⁿ` things, and that is all they can name.** This is pure counting. A 32-bit address can reach 2³² bytes (4 gibibytes, GiB); an 8-bit colour channel has 256 shades. To represent `k` distinct values you need at least `⌈log₂ k⌉` bits. Every encoding is a choice of which `2ⁿ` things the patterns stand for.

4. **Bits have no intrinsic meaning; interpretation is everything.** The byte `0x41` is the integer 65, the character "A" in the American Standard Code for Information Interchange (ASCII), or part of an instruction. Hardware applies an interpretation by which circuit receives the bits: the integer adder, the floating-point unit, the instruction decoder. Many bugs and security holes are type confusions: bits written under one interpretation and read under another.

5. **Fixed width makes arithmetic modular.** Hardware registers have a fixed number of bits, so results that need more bits lose their top bits. An `n`-bit unsigned adder therefore computes sums modulo `2ⁿ`: `255 + 1 = 0` in 8 bits. This is not a defect but a well-defined algebra (arithmetic in the ring of integers mod `2ⁿ`), and two's complement exploits it to represent negative numbers.

6. **Hexadecimal and octal are just grouped binary.** Since `16 = 2⁴`, each hexadecimal digit stands for exactly four bits, so `0xDEADBEEF` is a readable spelling of 32 specific bits. Converting is digit-by-digit, unlike converting to decimal. Hex exists for humans; hardware never uses it.

7. **Multiplying or dividing by the base is a shift.** Shifting a binary number left by `k` places multiplies it by `2ᵏ`; shifting right divides and truncates. Masking with `AND` extracts bit fields; `x & (x - 1)` clears the lowest set bit. Because the base is 2, these operations cost almost nothing in hardware, which is why powers of two pervade memory sizes, page sizes and hash-table capacities.

8. **Multi-byte values need a byte order.** Memory is addressed by bytes (8 bits), so a 32-bit value occupies four addresses. Little-endian machines (x86, most Arm configurations) store the least significant byte first; big-endian stores the most significant first and is the traditional "network byte order". The value is the same; only the mapping to addresses differs, and it matters whenever bytes cross between machines or files.

## Key concepts

| Term | Meaning |
|---|---|
| Bit | A binary digit, 0 or 1. |
| Byte | Eight bits; the smallest addressable unit in most machines. |
| Word | The natural operand width of a processor, often 32 or 64 bits. |
| Radix (base) | The number of distinct digit values and the ratio between digit weights. |
| Most / least significant bit | The bit with the largest / smallest weight. |
| Hexadecimal | Base 16; one digit per four bits. |
| Endianness | The order in which a multi-byte value's bytes are stored in memory. |
| Kibibyte (KiB) | 2¹⁰ = 1,024 bytes, distinct from the decimal kilobyte (1,000 bytes). |

## How it fits

- **Below:** The two-level choice comes from [analog vs digital](../../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md). Positional notation and modular arithmetic are [number theory](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md); counting patterns is [combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md).
- **Above:** Every other encoding builds on this: [integers](integers-and-twos-complement.md), [floating point](floating-point.md), [text](character-encoding.md) and [instructions](../../04-computer-architecture/01-instruction-set-architecture/instruction-encoding-and-addressing.md). Address width bounds memory in [virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md). Byte order is handled in protocol headers in [Internet Protocol (IP) addressing and forwarding](../../08-networking/03-network-layer/ip-addressing-and-forwarding.md). How many bits a message *needs* is the subject of [entropy and information](../../02-theory-of-computation/01-information-theory/entropy-and-information.md).
- **Siblings:** This leaf is the foundation for the other three, each of which is a specific interpretation of bit patterns with its own tradeoffs.

## Common misconceptions

- **"Computers store numbers."** They store bit patterns; numbers, text and code are interpretations applied by circuits and programs.
- **"Binary is used because it is mathematically special."** It is used because two levels are the most robust physical encoding; other bases are mathematically equivalent.
- **"A kilobyte is 1,024 bytes."** By standard (International Electrotechnical Commission) units, a kilobyte is 1,000 bytes and a kibibyte is 1,024; usage is inconsistent, so check which is meant.

## Go deeper

- Donald Knuth, *The Art of Computer Programming, Vol. 2: Seminumerical Algorithms* (1969), §4.1: positional number systems in depth.
- Charles Petzold, *Code: The Hidden Language of Computer Hardware and Software* (1999): a gentle path from switches to binary numbers.
- Randal Bryant and David O'Hallaron, *Computer Systems: A Programmer's Perspective* (2003): bit-level representation as programmers meet it.
