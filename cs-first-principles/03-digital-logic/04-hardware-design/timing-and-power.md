# Timing and Power

> **Layer:** [03 Digital Logic](../README.md) › [Hardware Design](README.md)
> **Builds on:** [Clocking and Synchronous Design](../03-sequential-logic/clocking-and-synchronous-design.md), [Capacitance and Timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md), [Thermodynamics and Energy](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md)
> **Enables:** [Power and the End of Scaling](../../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md), [Pipelining](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md), [Multicore and Cache Coherence](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md), [Scheduling](../../07-operating-systems/02-process-management/scheduling.md)

## Essence

A digital design is correct only if it is fast enough and cool enough. Timing analysis checks that every signal path settles within the clock period, under every combination of manufacturing variation, voltage and temperature the chip may meet. Power analysis checks that the energy the design burns, mostly from charging and discharging capacitance plus transistor leakage, stays within what the battery and cooling can provide. The two are coupled through supply voltage: raising voltage makes transistors faster but raises dynamic power with its square. Since the mid-2000s power, not transistor count, has been the binding constraint, so this coupling now shapes everything from clock gating in a single block to the move to multicore and specialised accelerators.

## Core tenets

1. **Static Timing Analysis (STA) checks every path without simulation.** Instead of simulating input patterns, STA adds up worst-case cell and wire delays along every register-to-register path and compares them with the setup and hold constraints. Slack is required time minus arrival time; negative slack is a violation. Because it is exhaustive over paths and linear in circuit size, STA is how billion-gate designs are signed off. It is conservative: it may flag "false paths" that no real input sequence exercises, which designers must declare explicitly.

2. **Designs must work at every corner, not just nominal.** Transistor speed varies with manufacturing (process), supply voltage and temperature, together called PVT. A chip is timed at the slow corner (slow transistors, low voltage, high temperature for setup) and the fast corner (for hold). This margin is a real cost: the typical chip could run faster than its rating, which is why vendors bin parts by measured speed and why adaptive voltage schemes exist.

3. **Dynamic power is `α C V² f`.** Every switching node draws `CV²` per full charge-discharge cycle, so power is activity factor `α` times switched capacitance `C` times voltage squared times frequency `f`. Each factor is a design lever: clock gating reduces `α` for idle blocks; smaller or fewer wires and gates reduce `C`; lower voltage cuts power quadratically; lower frequency cuts it linearly.

4. **Leakage power flows even when nothing switches.** Transistors that are off still conduct subthreshold current, which grows exponentially as threshold voltage falls and as temperature rises. In modern processes leakage can be a large share of total power. The remedy is power gating: cutting the supply to idle blocks entirely with header or footer switches, at the cost of losing their state and taking time to wake.

5. **Voltage couples speed and power, so lower voltage plus more parallelism saves energy.** Gate delay rises as supply voltage approaches threshold, so maximum frequency falls roughly in proportion to `V` over the useful range. Since dynamic power goes as `V²f`, power falls roughly with `V³` and energy per operation with `V²`. Two units at half speed and lower voltage can therefore match one fast unit's throughput for much less energy. This is the core physical argument for parallel hardware.

6. **Dynamic Voltage and Frequency Scaling (DVFS) tracks the workload.** Processors expose several voltage-frequency operating points and switch between them at run time under control of hardware and the operating system: high when work is urgent, low when idle or when waiting on memory. Turbo modes temporarily exceed sustainable power while the chip is cool. The policy question, how fast to run to finish work at least energy, sits at the boundary between hardware and operating-system scheduling.

7. **Power density limits how much of the chip can be on.** With voltage no longer falling each generation, packing more transistors into the same area raises power per area. A chip can then afford to run only a fraction of its transistors at full speed at once ("dark silicon", Esmaeilzadeh and colleagues, 2011). Designers respond with heterogeneity: many specialised blocks, each used only when needed, rather than more copies of one general core.

8. **The supply network itself must be designed.** Large currents through the resistance of on-chip power wiring cause voltage drop (IR drop), and sudden current changes through package inductance cause supply noise (`L di/dt`). Both reduce effective voltage and so slow gates; the timing analysis must account for them. Thousands of power pins and on-chip decoupling capacitance keep the supply stable.

## Key concepts

| Term | Meaning |
|---|---|
| Static Timing Analysis (STA) | Exhaustive path-delay checking against timing constraints. |
| Slack | Required arrival time minus actual arrival time; negative means failure. |
| PVT corner | A combination of process, voltage and temperature extremes. |
| Activity factor (`α`) | Fraction of capacitance switched per clock cycle. |
| Leakage power | Power drawn by off transistors through subthreshold and gate leakage. |
| Clock gating / power gating | Stopping the clock / cutting the supply to idle logic. |
| Dynamic Voltage and Frequency Scaling (DVFS) | Adjusting voltage and frequency at run time to match demand. |
| Energy-delay product | Figure of merit combining energy per operation and its latency. |
| Dark silicon | Transistors that must stay off or slowed to respect the power budget. |

## How it fits

- **Below:** Delay models come from [capacitance and timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md); the `CV²` cost and exponential leakage from [thermodynamics and energy](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md) and [the MOSFET](../../00-engineering-foundations/03-semiconductor-devices/the-mosfet.md); the constraints themselves from [clocking and synchronous design](../03-sequential-logic/clocking-and-synchronous-design.md).
- **Above:** The end of voltage scaling explained here is the starting point of [power and the end of scaling](../../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md), which led to [multicore](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md) and [domain-specific accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md). Critical-path delay sets the stage depth of [pipelining](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md). DVFS policy is part of operating-system [scheduling](../../07-operating-systems/02-process-management/scheduling.md), and data-dependent power draw creates [side channels](../../11-security-and-cryptography/03-system-security/side-channels.md).
- **Siblings:** [Hardware description languages](hardware-description-languages.md) produce the design; [FPGA and ASIC](fpga-and-asic.md) choose the implementation; this analysis decides whether either meets its speed and power targets.

## Common misconceptions

- **"Power is just a battery-life concern."** Power and heat limit performance in every class of machine, including servers and supercomputers.
- **"Halving the frequency halves the energy of a task."** At fixed voltage it halves power but doubles time, leaving dynamic energy unchanged; savings come from lowering voltage too.
- **"Timing analysis means running simulations."** Sign-off timing is static and exhaustive over paths; simulation cannot cover enough cases.

## Go deeper

- Jan Rabaey, Anantha Chandrakasan and Borivoje Nikolić, *Digital Integrated Circuits* (2nd ed., 2003): delay, power and their coupling.
- Anantha Chandrakasan, Samuel Sheng and Robert Brodersen, "Low-Power CMOS Digital Design" (1992): the classic case for voltage scaling with parallelism.
- Hadi Esmaeilzadeh et al., "Dark Silicon and the End of Multicore Scaling" (2011): how power density limits future chips.
