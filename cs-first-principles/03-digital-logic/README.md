# 03 Digital Logic

> **Layer:** 03 Digital Logic (where the physical and formal pillars meet)
> **Children:** [Number Representation](01-number-representation/README.md) · [Combinational Logic](02-combinational-logic/README.md) · [Sequential Logic](03-sequential-logic/README.md) · [Hardware Design](04-hardware-design/README.md)

## What this area is about

Digital logic is where computer science's two roots join. From the formal side comes Boolean algebra, a mathematical system of values 0 and 1 with operations AND, OR and NOT. From the physical side comes the Complementary Metal-Oxide-Semiconductor (CMOS) transistor pair, a switch that restores clean voltage levels at every stage. Claude Shannon's observation, in his 1937 master's thesis (published 1938), that switching circuits obey Boolean algebra fused the two: any Boolean function can be built as a circuit, and circuits can be designed by algebra. This layer answers: *how do we represent information in bits, compute any function of those bits with gates, remember results over time, and engineer all of this into real chips?*

The answer comes in four parts. Number representation decides what bit patterns mean. Combinational logic computes functions of bits with networks of gates. Sequential logic adds memory and a clock, turning circuits into finite state machines that step through time. Hardware design is the engineering flow that turns descriptions of such machines into silicon that meets its speed and power budgets.

The one interface this layer contributes to the stack is the **synchronous digital system**: registers holding fixed-width binary values that update together on each clock edge, with combinational logic computing the next values. Every processor, memory controller and accelerator above is an instance of it, and computer architecture is the art of choosing which registers and logic to build.

## Why this layer sits here

Digital logic needs both roots, which is why it sits at 03, after each has had its own start.

- From [00 Engineering Foundations](../00-engineering-foundations/README.md) it takes the restoring switch: [CMOS](../00-engineering-foundations/03-semiconductor-devices/cmos.md) gates, the [digital abstraction](../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md) with its noise margins, gate and wire delays from [capacitance and timing](../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md), positive [feedback](../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md) for memory, and the energy cost of switching from [thermodynamics](../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md).
- From [01 Mathematical Foundations](../01-mathematical-foundations/README.md) it takes [Boolean algebra](../01-mathematical-foundations/04-algebra/boolean-algebra.md) and [propositional logic](../01-mathematical-foundations/01-logic/propositional-logic.md) for function design, and [number theory](../01-mathematical-foundations/03-discrete-mathematics/number-theory.md) for modular arithmetic on fixed-width words.
- From [02 Theory of Computation](../02-theory-of-computation/README.md) it takes the [finite automaton](../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md), which a synchronous circuit implements, and complexity results that explain why [logic minimisation](02-combinational-logic/logic-minimization.md) is hard.

```
   01 Math (Boolean algebra) ──► 02 Theory (automata)
              │                         │
              ▼                         ▼
   ┌──────────────────── 03 DIGITAL LOGIC ────────────────────┐
   │ number representation · combinational · sequential · HDL │
   └──────────────────────────────────────────────────────────┘
              ▲                         │
   00 Engineering (CMOS, delay, energy) ▼
                              04 Computer Architecture and above
```

What the layers above need from it: a menu of standard parts (adders, multiplexers, register files, and Static Random-Access Memory (SRAM), Dynamic Random-Access Memory (DRAM) and flash [memory cells](03-sequential-logic/memory-cells.md)), a timing model (critical path sets clock period), a power model (`αCV²f` plus leakage), number formats with known behaviour, and a design flow that can produce custom hardware. [04 Computer Architecture](../04-computer-architecture/README.md) assembles these into processors; it is the first layer that can assume both pillars entirely.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Number Representation](01-number-representation/README.md) | What bits mean: binary, two's complement, floating point, text encodings | Digital abstraction, number theory |
| [Combinational Logic](02-combinational-logic/README.md) | Computing functions of bits: gates, minimisation, adders, multiplexers, the Arithmetic Logic Unit (ALU) | Boolean algebra, CMOS, representation |
| [Sequential Logic](03-sequential-logic/README.md) | Remembering and stepping through time: flip-flops, clocking, finite state machines, memory cells | Combinational logic, feedback, transistors |
| [Hardware Design](04-hardware-design/README.md) | Building real chips: Hardware Description Languages (HDLs), Field-Programmable Gate Array (FPGA) and Application-Specific Integrated Circuit (ASIC) implementation, timing and power sign-off | All three above, fabrication |

Representation comes first because it defines what the circuits operate on; the adder is designed around two's complement, not the other way round. Combinational logic then provides stateless computation. Sequential logic adds state, and with it the ability to implement any finite state machine, and, given enough memory, a programmable computer. Hardware design is the practical capstone: it shows how the previous three are written down, implemented on FPGAs or as ASICs, and checked against physical limits.

## Connections to neighbouring layers

- **[00 Engineering Foundations](../00-engineering-foundations/README.md):** The physical root. Every gate is a CMOS circuit; every delay is a resistance-capacitance (RC) product; every bit of static storage is positive feedback; every power budget is `CV²`. The end of Dennard scaling, explained in [fabrication and scaling](../00-engineering-foundations/03-semiconductor-devices/fabrication-and-scaling.md), is why power dominates hardware design today.
- **[01 Mathematical Foundations](../01-mathematical-foundations/README.md):** The formal root. Boolean algebra is the design language for logic, modular arithmetic underlies integer formats, and real analysis is what floating point approximates.
- **[02 Theory of Computation](../02-theory-of-computation/README.md):** Finite state machines are finite automata in hardware; a finite controller plus extensible memory approximates a [Turing machine](../02-theory-of-computation/03-computability/turing-machines.md); circuit size and depth are complexity measures; [information theory](../02-theory-of-computation/01-information-theory/entropy-and-information.md) bounds how few bits an encoding can use.
- **[04 Computer Architecture](../04-computer-architecture/README.md):** The direct consumer. ALUs, register files, pipeline registers and SRAM caches are assembled into processors; clock period becomes a factor in [the performance equation](../04-computer-architecture/06-performance/the-performance-equation.md).
- **[06 Programming Languages](../06-programming-languages/README.md):** Number formats become primitive types; compilers must respect integer overflow rules and floating-point non-associativity; HDLs are languages with their own semantics.
- **[11 Security and Cryptography](../11-security-and-cryptography/README.md):** Integer overflow causes [memory safety vulnerabilities](../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md), and data-dependent timing and power leak secrets through [side channels](../11-security-and-cryptography/03-system-security/side-channels.md).
- **[13 Artificial Intelligence](../13-artificial-intelligence/README.md):** Low-precision floating-point formats and multiply-accumulate arrays are what make [training at scale](../13-artificial-intelligence/03-deep-learning/training-at-scale.md) affordable.

## Connections across layers

The synchronous model here is the hardware ancestor of many higher ideas. Pipelining registers become [processor pipelines](../04-computer-architecture/02-processor-microarchitecture/pipelining.md); finite state machines reappear as protocol state in [the User Datagram Protocol (UDP) and Transmission Control Protocol (TCP)](../08-networking/04-transport-layer/udp-and-tcp.md) and as the objects of [model checking](../06-programming-languages/05-formal-methods/model-checking.md); the global clock that makes hardware simple is exactly what [distributed systems](../10-distributed-and-parallel-computing/02-distributed-foundations/time-clocks-and-ordering.md) lack; and metastability in hardware is a physical cousin of [race conditions](../07-operating-systems/03-concurrency/race-conditions-and-critical-sections.md) in software.

## Cross-cutting threads

- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): voltages become bits, transistors become gates, gates become blocks, settling becomes clock cycles.
- [Encoding and representation](../CROSS-CUTTING.md#encoding-and-representation): two's complement, Institute of Electrical and Electronics Engineers (IEEE) 754 floating point and Unicode Transformation Format 8-bit (UTF-8) each make some operations cheap.
- [Composition](../CROSS-CUTTING.md#composition): functionally complete gates compose into any function; flip-flops plus logic compose into any finite machine.
- [State and time](../CROSS-CUTTING.md#state-and-time): the clock discretises time; metastability is the irreducible cost.
- [Pipelining and parallelism](../CROSS-CUTTING.md#pipelining-and-parallelism): parallel-prefix adders and register insertion.
- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): area, delay and power; FPGA flexibility against ASIC efficiency.
- [Invariants and correctness](../CROSS-CUTTING.md#invariants-and-correctness): the static discipline and setup and hold constraints are invariants every path must keep.
