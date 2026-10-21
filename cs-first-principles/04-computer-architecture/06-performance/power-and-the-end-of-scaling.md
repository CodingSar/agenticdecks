# Power and the End of Scaling

> **Layer:** [04 Computer Architecture](../README.md) › [Performance](README.md)
> **Builds on:** [CMOS](../../00-engineering-foundations/03-semiconductor-devices/cmos.md), [Fabrication and scaling](../../00-engineering-foundations/03-semiconductor-devices/fabrication-and-scaling.md), [Thermodynamics and energy](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md), [Timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md)
> **Enables:** [Multicore and cache coherence](../04-parallel-architecture/multicore-and-cache-coherence.md), [Domain-specific accelerators](../04-parallel-architecture/domain-specific-accelerators.md), [SIMD and GPUs](../04-parallel-architecture/simd-and-gpus.md), [Cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md)

## Essence

For about thirty years, each new chip generation gave more transistors, faster transistors and the same power per unit area, all at once. Moore's law supplied the transistor count; Dennard scaling supplied the rest, because shrinking a transistor also let its voltage drop, so power density stayed constant while frequency rose. Around 2005 voltage stopped scaling, because leakage current grows sharply as threshold voltage falls. From then on, more transistors switching faster meant more heat per square millimetre than a package can remove. Clock rates flattened near 3–5 GHz, and performance growth had to come from parallelism, specialisation and efficiency rather than frequency. Power, not transistor count, is now the binding constraint of computer architecture, from phones to data centres.

## Core tenets

1. **Dynamic power is proportional to activity × capacitance × voltage² × frequency.** Each time a CMOS (Complementary Metal-Oxide-Semiconductor) gate switches, it charges or discharges a capacitance through the supply voltage V, costing energy proportional to CV². Multiply by how often gates switch (activity factor and frequency) to get power. The V² term makes voltage the most powerful lever: lowering V by 10% cuts dynamic power by about 19% at the same frequency.

2. **Dennard scaling made each generation free.** Dennard et al. (1974) showed that if all dimensions and the voltage shrink by a factor k, circuit delay shrinks by k, and power per transistor falls by k² while transistor density rises by k², so power per area stays constant. From the 1970s to the early 2000s this meant roughly 40% higher frequency per generation and double the transistors, with no increase in power density.

3. **Voltage scaling stopped because of leakage.** A transistor switches cleanly only if its supply voltage is well above its threshold voltage, and lowering the threshold makes subthreshold leakage grow exponentially (roughly tenfold for each ~60–100 mV of reduction at room temperature). By the 90–65 nm generations (2004–2006), leakage had become a large share of total power and supply voltages stalled around 1 V. Without falling voltage, shrinking transistors raises power density.

4. **The power wall ended the frequency race.** A desktop or server chip can dissipate on the order of 100–300 W with practical cooling. Intel's Pentium 4 reached 3.8 GHz in 2004 and Intel cancelled its 4 GHz-plus successor (Tejas) the same year; mainstream clock rates have moved only from about 3–4 GHz to about 4–6 GHz in boost since. Performance per core still improves, but by roughly 10–20% per year rather than the ~50% per year of the late 1980s to early 2000s.

5. **Transistors became cheaper than the power to run them (dark silicon).** Moore's law continued to double transistor counts, more slowly, for another two decades. But at fixed power, only a shrinking fraction of a chip can switch at full speed at the same time. The rest must be idle, clocked slowly, or powered off. This "dark silicon" makes specialised blocks attractive: a unit that is idle most of the time costs little power but is very efficient when used.

6. **Energy per operation is the new figure of merit.** Under a fixed power budget, performance = power × operations per joule. Architects now optimise energy per operation: running more cores at lower voltage and frequency (dynamic voltage and frequency scaling), using simpler cores for parallel work, cutting data movement (which costs far more energy than arithmetic), and using reduced-precision arithmetic.

7. **Parallelism converts transistors into performance at better energy.** Because power rises much faster than frequency once voltage must rise with it, two cores at a lower frequency and voltage can deliver more throughput than one core at higher frequency for the same power. This is why multicore arrived across the industry in 2005–2006 (AMD Athlon 64 X2, Intel Core Duo) and why GPUs and accelerators, which spend energy mostly on arithmetic, dominate throughput computing.

8. **The constraint reaches up to data centres and down to phones.** A phone is limited by battery and by skin temperature (a few watts sustained); a large data centre by tens to hundreds of megawatts of electrical and cooling capacity. Turbo modes run briefly above sustainable power when thermal headroom exists. Large AI training clusters are now planned around power availability as much as chip supply.

```
 era              transistors    frequency         power density   source of speedup
 1975-2005        x2 / ~2 yr     up ~40% / gen     ~constant       Dennard + Moore + ILP
 2005-2020s       x2 / ~2-3 yr   ~flat (3-5 GHz)   at the limit    multicore, SIMD, GPUs
 2015-2020s       slowing        ~flat             at the limit    specialisation (TPUs, NPUs)
```

## Key concepts

| Term | Meaning |
|---|---|
| Dynamic power | Power spent charging and discharging capacitance when gates switch, ~αCV²f |
| Static (leakage) power | Power lost through transistors that are nominally off |
| Threshold voltage | Gate voltage at which a transistor begins to conduct strongly |
| Dennard scaling | Shrinking dimensions and voltage together keeps power density constant |
| Moore's law | Observation (1965, revised 1975) that transistor counts double about every two years |
| Power wall | The limit on chip performance set by the heat that can be removed |
| Dark silicon | Portion of a chip that cannot be powered at full speed at the same time as the rest |
| DVFS | Dynamic Voltage and Frequency Scaling: lowering V and f when full speed is not needed |
| Thermal Design Power (TDP) | Sustained power a cooling system is designed to remove |

## How it fits

- **Below:** CV² switching energy and leakage come from [CMOS](../../00-engineering-foundations/03-semiconductor-devices/cmos.md) and [the MOSFET](../../00-engineering-foundations/03-semiconductor-devices/the-mosfet.md); scaling trends from [fabrication and scaling](../../00-engineering-foundations/03-semiconductor-devices/fabrication-and-scaling.md); heat removal from [thermodynamics](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md); circuit-level power from [timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md).
- **Above:** it forced [multicore](../04-parallel-architecture/multicore-and-cache-coherence.md), [GPUs](../04-parallel-architecture/simd-and-gpus.md) and [accelerators](../04-parallel-architecture/domain-specific-accelerators.md), which in turn forced software into [parallel programming models](../../10-distributed-and-parallel-computing/01-parallel-computing/parallel-programming-models.md); power and cooling shape [cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) economics and [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md); the OS manages DVFS in [scheduling](../../07-operating-systems/02-process-management/scheduling.md).
- **Siblings:** it explains why the clock-period factor in [the performance equation](the-performance-equation.md) stopped shrinking, and why [Amdahl's law](amdahls-law.md) became the central limit of the multicore era.

## Common misconceptions

- **"Moore's law ended in 2005."** Dennard scaling ended; transistor counts kept growing for two more decades, though more slowly and at rising cost per new process.
- **"Clock speed stopped rising because transistors stopped getting faster."** Transistors kept getting faster; chips could not afford the power to switch all of them faster.
- **"Power is only an issue for batteries."** The largest systems are the most power-limited: data centres are built around megawatts of supply and cooling.

## Go deeper

- Dennard et al., *Design of Ion-Implanted MOSFETs with Very Small Physical Dimensions* (IEEE Journal of Solid-State Circuits, 1974): the scaling rules.
- Esmaeilzadeh et al., *Dark Silicon and the End of Multicore Scaling* (ISCA 2011): quantifies the power limit on parallel scaling.
- Hennessy and Patterson, *A New Golden Age for Computer Architecture* (Communications of the ACM, 2019): how the end of scaling reshaped the field.
- Horowitz, *Computing's Energy Problem (and What We Can Do About It)* (ISSCC 2014): energy per operation and per data movement.
