# Arithmetic and Building Blocks

> **Layer:** [03 Digital Logic](../README.md) › [Combinational Logic](README.md)
> **Builds on:** [Logic Gates](logic-gates.md), [Integers and Two's Complement](../01-number-representation/integers-and-twos-complement.md), [Divide and Conquer](../../05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md)
> **Enables:** [Datapath and Control](../../04-computer-architecture/02-processor-microarchitecture/datapath-and-control.md), [FPGA and ASIC](../04-hardware-design/fpga-and-asic.md), [Work, Span and Parallel Models](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md)

## Essence

Processors are not designed gate by gate. They are assembled from a small set of standard combinational blocks: multiplexers that select, decoders that route, adders that compute, comparators and shifters, and the Arithmetic Logic Unit (ALU) that combines them. Each block has a known structure and a known cost in area and delay. The central lesson is that the naive designs are serial and slow, and the fast designs are parallel algorithms in hardware. A ripple-carry adder takes time linear in the word width; a carry-lookahead or parallel-prefix adder takes logarithmic time by computing carries with a tree, exactly the divide-and-conquer idea from algorithms.

## Core tenets

1. **The multiplexer is the universal selector.** A 2-to-1 multiplexer (mux) outputs `s ? b : a`. A `2ᵏ`-to-1 mux, steered by `k` select bits, can implement *any* `k`-input Boolean function by feeding the truth table into its data inputs; this is exactly how Field-Programmable Gate Array (FPGA) lookup tables work. In a datapath, muxes choose which operand or result goes where, so control signals become mux selects.

2. **Decoders turn binary codes into one-hot selections.** An `n`-to-`2ⁿ` decoder asserts exactly one output line for each input code. Decoders select a memory row from an address, a register from a register number, and an operation from an opcode. Their size grows exponentially with `n`, which is why large memories decode addresses hierarchically.

3. **Binary addition is built from the full adder.** A full adder adds bits `a`, `b` and carry-in `c`: `sum = a ⊕ b ⊕ c`, `carry = ab + c(a ⊕ b)`. Chaining `n` of them, each passing its carry to the next, gives a ripple-carry adder: simple and small, but its worst-case delay grows linearly with `n` because a carry may propagate through every bit (as in `0111...1 + 1`).

4. **Carry-lookahead turns a sequential chain into a parallel prefix computation.** For each bit, define generate `g = ab` (this bit creates a carry) and propagate `p = a ⊕ b` (this bit passes a carry along). Then `c_{i+1} = g_i + p_i c_i`. Combining `(g, p)` pairs is associative, so all carries can be computed by a parallel-prefix tree in `O(log n)` levels. Kogge-Stone (1973) and Brent-Kung (1982) adders are such trees, trading wiring and area for depth. A 64-bit adder needs about six prefix levels instead of 64 ripple steps.

5. **Subtraction, comparison and negation reuse the adder.** In two's complement, `a - b = a + ~b + 1`: invert `b` and set carry-in to 1. Comparison is subtraction followed by inspecting the sign, zero and overflow results. One adder with a few muxes and inverters thus provides add, subtract, increment, compare and negate.

6. **Multiplication is many additions, made fast by deferring carries.** Multiplying two `n`-bit numbers produces `n` shifted partial products to sum. Carry-save adders add three numbers into two (a sum vector and a carry vector) with no carry propagation, so a tree of them (a Wallace tree, 1964, or Dadda tree) reduces all partial products to two in `O(log n)` levels, and one fast adder finishes. Booth encoding halves the number of partial products. Multipliers are large, which is why they are pipelined and why multiply-accumulate units dominate machine-learning accelerators.

7. **Shifters are log-depth mux networks.** A barrel shifter shifts by any amount in one pass using `log₂ n` stages of muxes, each stage shifting by `2ᵏ` or not according to one bit of the shift amount. The same structure, with the vacated bits filled with zeros, sign bits or wrapped bits, gives logical shifts, arithmetic shifts and rotations.

8. **The ALU is a menu of function units behind a multiplexer.** An ALU computes several operations (add, subtract, AND, OR, XOR, shift, compare) in parallel and uses a mux, driven by an operation code, to choose the result. It also outputs status flags (zero, negative, carry, overflow). This is the core computational element of the processor datapath.

## Key concepts

| Term | Meaning |
|---|---|
| Multiplexer (mux) | Selects one of several inputs according to select bits. |
| Decoder | Converts an `n`-bit code into one of `2ⁿ` active lines. |
| Full adder | Adds three bits, producing sum and carry. |
| Ripple-carry adder | Chain of full adders; delay linear in width. |
| Generate / propagate | Per-bit signals indicating carry creation / carry passing. |
| Parallel-prefix adder | Adder computing all carries with an associative tree in logarithmic depth. |
| Carry-save adder | Adds three numbers to two without propagating carries. |
| Barrel shifter | Logarithmic-depth network shifting by any amount. |
| Arithmetic Logic Unit (ALU) | Block computing a selectable arithmetic or logical operation with status flags. |

## How it fits

- **Below:** Built from [logic gates](logic-gates.md); the adder's dual signed/unsigned role relies on [two's complement](../01-number-representation/integers-and-twos-complement.md). Fast adders are [divide and conquer](../../05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md) and prefix computation in hardware.
- **Above:** ALUs, register-file decoders and operand muxes form the [datapath and control](../../04-computer-architecture/02-processor-microarchitecture/datapath-and-control.md) of a processor. Floating-point units extend these blocks to [floating point](../01-number-representation/floating-point.md). Multiply-accumulate arrays are the heart of [domain-specific accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md). The work and depth of a prefix tree are exactly the work and span of [work, span and parallel models](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md).
- **Siblings:** [Logic minimization](logic-minimization.md) optimises irregular logic; these blocks are regular structures whose best designs come from algorithmic insight rather than minimisation.

## Common misconceptions

- **"Addition is a single fast step."** It is the result of a carefully designed log-depth carry network; the carry chain is a classic critical path.
- **"Faster adders are just bigger ripple adders."** They use a different algorithm (parallel prefix), not more of the same.
- **"Multiplication is inherently much slower than addition."** With carry-save trees and pipelining, multiplication has high throughput; it costs area and latency, not proportionally more time per result.

## Go deeper

- David Harris and Sarah Harris, *Digital Design and Computer Architecture* (2007): building blocks and the ALU in a modern design flow.
- Behrooz Parhami, *Computer Arithmetic: Algorithms and Hardware Designs* (2000): adders, multipliers and dividers in depth.
- Peter Kogge and Harold Stone, "A Parallel Algorithm for the Efficient Solution of a General Class of Recurrence Equations" (1973): the prefix computation behind fast adders.
