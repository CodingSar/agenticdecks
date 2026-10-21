# Environmental Impact

> **Layer:** [15 Computing in Context](README.md)
> **Builds on:** [Thermodynamics and energy](../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md), [Power and the end of scaling](../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md), [Cloud computing](../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md), [Training at scale](../13-artificial-intelligence/03-deep-learning/training-at-scale.md)
> **Enables:** [Ethics and professional responsibility](ethics-and-professional-responsibility.md), [Law, privacy and policy](law-privacy-and-policy.md)

## Essence

Every computation turns electricity into heat, and every device is made from mined, refined and fabricated materials that eventually become waste. Computing's environmental footprint therefore has two parts: **operational** impact (the energy to run and cool hardware, and the emissions of the grid that supplies it) and **embodied** impact (the energy, water and materials spent making the hardware, plus its disposal). Efficiency per operation has improved by many orders of magnitude, but total use keeps rising because cheaper computation invites more of it. The useful mental model is a product: footprint = demand × energy per unit of work × carbon per unit of energy, plus the embodied cost of the hardware amortised over its life. Each factor is a different lever, owned by a different layer of the stack.

## Core tenets

1. **Data centres are a small but fast-growing share of electricity.** The International Energy Agency (IEA) estimated data centres used roughly 400 terawatt-hours (TWh) in 2024, about 1.5% of world electricity, and projected that this could roughly double by 2030, driven largely by Artificial Intelligence (AI). The share is much higher locally: about 4% of United States (US) electricity in 2023 by one Lawrence Berkeley National Laboratory estimate, and far more in a few hub regions. Such figures are uncertain by tens of percent and should always be read with their date and source.
2. **Power Usage Effectiveness (PUE) measures overhead, not usefulness.** PUE is total facility energy divided by the energy delivered to Information Technology (IT) equipment, so 1.0 means no cooling or power-conversion overhead. Typical facilities were around 2 in the mid-2000s; survey averages were about 1.5–1.6 in the early 2020s, and the best hyperscale fleets report about 1.1. PUE says nothing about whether the servers do useful work, and it ignores water use, which evaporative cooling can make substantial.
3. **Embodied carbon often dominates for personal devices.** Manufacturing a chip takes energy-hungry lithography, ultra-pure water and chemicals. For smartphones and laptops, life-cycle assessments typically attribute most of the lifetime emissions, often around three quarters, to manufacturing rather than use (Gupta et al., "Chasing Carbon", 2021). For servers on fossil-heavy grids operation dominates, but as grids decarbonise the embodied share grows. So keeping hardware in use longer is often the biggest single lever for devices.
4. **E-waste is large and mostly unrecovered.** The Global E-waste Monitor 2024 counted about 62 million tonnes of electronic waste in 2022, with under a quarter documented as properly collected and recycled. Devices contain scarce and toxic materials; short replacement cycles, sealed designs and software support that ends early all turn working hardware into waste.
5. **Efficiency alone does not cut totals: the Jevons paradox.** William Stanley Jevons (*The Coal Question*, 1865) noted that more efficient steam engines increased coal use, because cheaper work found more uses. Computing shows the same rebound. Masanet et al. (*Science*, 2020) estimated that data-centre computing output grew about sixfold between 2010 and 2018 while energy use rose only about 6%, an efficiency triumph; but when demand grows faster than efficiency, as with AI in the mid-2020s, totals rise anyway.
6. **AI training is costly per run, but inference dominates over a model's life.** Patterson et al. (2021) estimated that training GPT-3 (2020) used about 1.3 gigawatt-hours (GWh). Disclosed hardware hours for the largest mid-2020s runs imply tens of GWh, though most developers do not publish energy figures. Per query, inference is small: published estimates for a text chatbot prompt in 2023–2025 range from about 0.3 to 3 watt-hours, depending on model, hardware and what is counted. But queries number in the billions, and Google reported in 2022 that inference was about three fifths of its Machine Learning (ML) energy. All such numbers are estimates that age quickly.
7. **Carbon depends on where and when electricity is used.** Grid carbon intensity ranges from tens of grams of carbon dioxide (CO2) per kilowatt-hour (kWh) on hydro- or nuclear-heavy grids to over 700 g on coal-heavy ones, and it varies hour by hour with sun and wind. The same job can therefore differ in emissions by more than ten times. Carbon-aware scheduling moves flexible work, such as batch jobs and training, to cleaner places and times.
8. **The levers are spread across the whole stack.** In [physics](../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md), switching energy scales as `CV²`, so voltage is the strongest knob. In [architecture](../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md), moving data from Dynamic Random-Access Memory (DRAM) costs on the order of a thousand times more than an arithmetic operation, so locality and specialised accelerators save most. In [distributed systems](../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md), idle servers still draw a large fraction of peak power (Barroso and Hölzle, "The Case for Energy-Proportional Computing", 2007), so consolidation and high utilisation matter. In [AI](../13-artificial-intelligence/03-deep-learning/training-at-scale.md), smaller compute-optimal models, distillation, quantisation and caching cut energy per answer.

## Key concepts

| Term | Meaning |
|---|---|
| Operational emissions | Emissions from the electricity used to run and cool hardware |
| Embodied emissions | Emissions from manufacturing, transporting and disposing of hardware |
| PUE | Total facility energy / IT equipment energy; 1.0 is the ideal |
| Carbon intensity | Grams of CO2-equivalent emitted per kWh of electricity, varying by grid and hour |
| Life-cycle assessment | Accounting of impacts from raw material extraction to disposal |
| Jevons paradox (rebound effect) | Efficiency gains lowering cost and so raising total consumption |
| Energy proportionality | Power draw that scales with load, so idle machines use little |
| Carbon-aware computing | Shifting flexible work in time or space towards low-carbon electricity |

## How it fits

- **Below:** the floor and the main cost of computation come from [thermodynamics](../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md); the [end of Dennard scaling](../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md) made energy the binding constraint on chips and data centres; [cloud computing](../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) concentrates load where efficiency is highest; [training at scale](../13-artificial-intelligence/03-deep-learning/training-at-scale.md) is the fastest-growing new demand.
- **Above:** nothing sits above this layer. Energy and carbon budgets flow back down as non-functional [requirements](../12-software-engineering/02-process/requirements.md) and as measurements in [observability](../12-software-engineering/04-operations/observability.md).
- **Siblings:** [ethics](ethics-and-professional-responsibility.md) asks who bears the costs (local grids, water, the places e-waste is shipped); [law and policy](law-privacy-and-policy.md) increasingly requires disclosure, for example EU rules on data-centre energy reporting and right-to-repair; [history](history-of-computing.md) shows each cost drop expanding total use.

## Common misconceptions

- **"A low PUE means a green data centre."** PUE ignores the carbon of the electricity, the water used, the embodied hardware and whether the computing is useful.
- **"More efficient hardware will shrink computing's footprint."** Only if demand grows more slowly than efficiency improves; the rebound effect often absorbs the gain.
- **"The energy of one AI query is either trivial or catastrophic."** Per query it is small; in aggregate it is significant and growing. Both scales matter, and single headline numbers hide wide uncertainty.

## Go deeper

- Luiz André Barroso, Urs Hölzle and Parthasarathy Ranganathan, *The Datacenter as a Computer* (3rd ed., 2018): energy, PUE and efficiency at warehouse scale.
- Udit Gupta et al., "Chasing Carbon: The Elusive Environmental Footprint of Computing" (HPCA 2021): why embodied carbon matters.
- Eric Masanet et al., "Recalibrating Global Data Center Energy-Use Estimates", *Science* (2020): measured efficiency versus growth.
- David Patterson et al., "Carbon Emissions and Large Neural Network Training" (2021): method and figures for AI training energy.
