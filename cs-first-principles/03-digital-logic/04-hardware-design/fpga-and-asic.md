# FPGA and ASIC

> **Layer:** [03 Digital Logic](../README.md) › [Hardware Design](README.md)
> **Builds on:** [Hardware Description Languages](hardware-description-languages.md), [Fabrication and Scaling](../../00-engineering-foundations/03-semiconductor-devices/fabrication-and-scaling.md), [Arithmetic and Building Blocks](../02-combinational-logic/arithmetic-and-building-blocks.md)
> **Enables:** [Domain-Specific Accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md), [Cloud Computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md), [Timing and Power](timing-and-power.md)

## Essence

A digital design described in a Hardware Description Language (HDL) can become physical hardware in two main ways. An Application-Specific Integrated Circuit (ASIC) is a custom chip: the design is turned into transistors and wires and fabricated, giving the best speed, power and unit cost but requiring millions of dollars and months before the first chip exists, with no way to change it afterwards. A Field-Programmable Gate Array (FPGA) is a mass-produced chip full of configurable logic blocks and programmable wiring; loading a configuration bitstream makes it behave like the design, within minutes and as often as you like. The price of that flexibility is that the configuration machinery itself costs area, delay and power, typically an order of magnitude or more. Choosing between them is an economic decision driven by volume, performance need and how often the design changes.

## Core tenets

1. **An FPGA implements logic with lookup tables, not gates.** A `k`-input Lookup Table (LUT) is a tiny memory of `2ᵏ` bits addressed by its inputs, so it can implement *any* `k`-input function by storing the truth table (typically `k` = 4 to 6). Each logic block pairs LUTs with flip-flops. Synthesis for an FPGA maps logic onto LUTs rather than minimising gate count.

2. **Programmable routing dominates an FPGA.** Logic blocks are connected through a mesh of wire segments joined by configuration-controlled switches. These switches add resistance and capacitance, so most of an FPGA's area and most of a signal's delay are in the routing, not the logic. Place-and-route quality therefore largely determines FPGA performance.

3. **Hard blocks recover efficiency for common functions.** Modern FPGAs embed fixed-function blocks: Digital Signal Processing (DSP) slices with multipliers and accumulators, block memories, high-speed serial transceivers, memory controllers and sometimes whole processor cores. Designs that map their arithmetic and storage onto these blocks close much of the gap to ASICs for those parts.

4. **The FPGA-ASIC gap is large and measurable.** Kuon and Rose (2007) measured FPGAs needing about 35 times the area of a standard-cell ASIC for the same logic (about 18 times when hard multipliers and memories are used), with critical paths roughly 3.4 to 4.6 times slower and around 14 times the dynamic power (about 7 times with hard blocks). Configurability is paid for in every transistor of the programmable fabric.

5. **ASICs trade huge fixed cost for low unit cost.** An ASIC requires a full physical design flow (synthesis to standard cells, floorplanning, placement, clock-tree synthesis, routing, timing closure, verification) and a set of photomasks that at leading-edge nodes costs millions of dollars. These Non-Recurring Engineering (NRE) costs are paid once; each additional chip is cheap. FPGAs have almost no NRE but a high unit price.

6. **Volume decides the economics.** Total cost is roughly `NRE + units × unit_cost`. Below some crossover volume FPGAs are cheaper; above it ASICs win. FPGAs also win when the design must change in the field (evolving standards, prototyping, network functions) or when time to market matters more than efficiency. ASICs win for high-volume or efficiency-critical products: phone processors, network switches, machine-learning accelerators.

7. **Both share the front end, and the boundary is blurring.** The same HDL and much of the same verification serve both, which is why ASIC teams prototype on FPGAs. Structured ASICs, eFPGA (embedded FPGA blocks inside ASICs) and FPGA-equipped cloud instances occupy the middle ground. The FPGA was introduced by Xilinx in 1985 (the XC2064) and has grown from glue logic to data-centre accelerators.

## Key concepts

| Term | Meaning |
|---|---|
| Application-Specific Integrated Circuit (ASIC) | A chip fabricated for one design. |
| Field-Programmable Gate Array (FPGA) | A chip whose logic and wiring are configured after manufacture. |
| Lookup Table (LUT) | Small memory implementing any function of its `k` inputs. |
| Bitstream | The configuration data loaded into an FPGA. |
| Standard cell | Pre-designed, pre-characterised gate or flip-flop used in ASIC layout. |
| Place and route | Choosing locations for cells and paths for wires. |
| Timing closure | Iterating a design until all timing constraints are met. |
| Non-Recurring Engineering (NRE) | One-time design and mask costs. |
| Tape-out | Sending the final design to fabrication. |

## How it fits

- **Below:** Both consume netlists from [hardware description languages](hardware-description-languages.md). ASIC economics follow from mask costs and yield in [fabrication and scaling](../../00-engineering-foundations/03-semiconductor-devices/fabrication-and-scaling.md). LUTs are multiplexers over truth tables ([arithmetic and building blocks](../02-combinational-logic/arithmetic-and-building-blocks.md)).
- **Above:** Specialised hardware in [domain-specific accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md) is built as ASICs or prototyped on FPGAs. Cloud providers offer FPGA instances and deploy custom ASICs for networking and machine learning ([cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md), [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md)). FPGA bitstreams and shared FPGAs raise their own [side-channel](../../11-security-and-cryptography/03-system-security/side-channels.md) concerns.
- **Siblings:** [Hardware description languages](hardware-description-languages.md) are the shared input; [timing and power](timing-and-power.md) analysis decides whether either implementation meets its targets.

## Common misconceptions

- **"FPGAs are slow processors."** They are not processors at all; they become the circuit you describe, and can beat processors by running many operations in parallel each cycle.
- **"An ASIC is always better."** Per chip it is faster and more efficient, but at low volume or with changing requirements its fixed costs and inflexibility usually lose.
- **"FPGA design is software programming."** The input is a hardware description; timing, parallelism and resource limits still govern the result.

## Go deeper

- Ian Kuon and Jonathan Rose, "Measuring the Gap Between FPGAs and ASICs" (2007): quantitative comparison of area, speed and power.
- Vaughn Betz, Jonathan Rose and Alexander Marquardt, *Architecture and CAD for Deep-Submicron FPGAs* (1999): how FPGA fabrics and their tools are designed.
- Neil Weste and David Harris, *CMOS VLSI Design* (4th ed., 2010): the ASIC design flow from cells to chip.
