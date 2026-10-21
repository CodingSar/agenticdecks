# Environmental Impact

> **Layer:** [15 Computing in Context](README.md)
> **Builds on:** [Thermodynamics and energy](../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md), [Power and the end of scaling](../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md), [Cloud computing](../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md), [Training at scale](../13-artificial-intelligence/03-deep-learning/training-at-scale.md)
> **Enables:** [Ethics and professional responsibility](ethics-and-professional-responsibility.md), [Law, privacy and policy](law-privacy-and-policy.md)

## Essence

Every computation turns electricity into heat, and every device is made from mined and refined materials that eventually become waste. So computing's footprint has two parts: **operational** (energy to run and cool hardware, and its grid emissions) and **embodied** (energy, water and materials to make the hardware, plus disposal). Efficiency per operation has improved by many orders of magnitude, but cheaper computation invites more of it. The useful model is a product: footprint = demand × energy per unit of work × carbon per unit of energy, plus embodied cost amortised over the hardware's life. Each factor is a lever owned by a different layer.

## Core tenets

1. **Data centres are a small but fast-growing share of electricity.** The International Energy Agency (IEA) estimated data centres used roughly 400 terawatt-hours (TWh) in 2024, about 1.5% of world electricity, and projected that this could roughly double by 2030, driven largely by Artificial Intelligence (AI). Locally the share is higher: about 4% of United States (US) electricity in 2023 by a Lawrence Berkeley National Laboratory estimate. Such figures carry tens of percent of uncertainty; always note date and source.
2. **Power Usage Effectiveness (PUE) measures overhead, not usefulness.** PUE is total facility energy divided by the energy delivered to Information Technology (IT) equipment, so 1.0 means no cooling or power-conversion overhead. Typical facilities were around 2 or worse in the mid-2000s; survey averages were about 1.5–1.6 in the early 2020s, and the best hyperscale fleets report about 1.1. It ignores whether servers do useful work and how much water evaporative cooling consumes.
3. **Embodied carbon often dominates for personal devices.** For smartphones and laptops, life-cycle assessments typically attribute most lifetime emissions, often around three quarters, to manufacturing (Gupta et al., "Chasing Carbon", 2021). For servers on fossil-heavy grids operation dominates, but the embodied share grows as grids decarbonise. Keeping devices in use longer is often the biggest single lever.
4. **E-waste is large and mostly unrecovered.** The Global E-waste Monitor 2024 counted about 62 million tonnes of electronic waste in 2022, with under a quarter documented as properly collected and recycled. Short replacement cycles, sealed designs and early end of software support turn working hardware, with its scarce and toxic materials, into waste.
5. **Efficiency alone does not cut totals: the Jevons paradox.** William Stanley Jevons (*The Coal Question*, 1865) noted that more efficient steam engines increased coal use, because cheaper work found more uses. Computing shows the same rebound: Masanet et al. (*Science*, 2020) estimated that data-centre computing output grew about sixfold between 2010 and 2018 while energy use rose only about 6%; but when demand outgrows efficiency, as with AI in the mid-2020s, totals rise.
6. **AI training is costly per run, but inference dominates over a model's life.** Patterson et al. (2021) estimated that training GPT-3 (2020) used about 1.3 gigawatt-hours (GWh). Disclosed hardware hours for the largest mid-2020s runs imply tens of GWh; most developers publish no energy figures. Published estimates for one text chatbot prompt in 2023–2025 range from about 0.3 to 3 watt-hours, depending on model, hardware and what is counted. But queries number in the billions, and Google reported that in 2019–2021 inference was about three fifths of its Machine Learning (ML) energy (Patterson et al., 2022).
7. **Carbon depends on where and when electricity is used.** Grid carbon intensity ranges from tens of grams of carbon dioxide (CO2) per kilowatt-hour (kWh) on hydro- or nuclear-heavy grids to over 700 g on coal-heavy ones, and it varies hourly with sun and wind, so the same job's emissions can differ more than tenfold. Carbon-aware scheduling moves flexible work, such as batch jobs and training, to cleaner places and times.
8. **The levers are spread across the whole stack.** In physics, switching energy scales as `CV²`, so voltage is the strongest knob. In [architecture](../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md), moving data from Dynamic Random-Access Memory (DRAM) costs on the order of a thousand times more than an arithmetic operation, so locality and specialised accelerators save most. In distributed systems, idle servers still draw a large fraction of peak power (Barroso and Hölzle, "The Case for Energy-Proportional Computing", 2007), so consolidation and high utilisation matter. In AI, smaller compute-optimal models, distillation, quantisation and caching cut energy per answer.

## Key concepts

| Term | Meaning |
|---|---|
| Operational emissions | Emissions from the electricity used to run and cool hardware |
| Embodied emissions | Emissions from manufacturing, transporting and disposing of hardware |
| PUE | Total facility energy / IT equipment energy; 1.0 is the ideal |
| Carbon intensity | Grams of CO2-equivalent emitted per kWh of electricity, varying by grid and hour |
| Jevons paradox (rebound effect) | Efficiency gains lowering cost and so raising total consumption |
| Energy proportionality | Power draw that scales with load, so idle machines use little |
| Carbon-aware computing | Shifting flexible work in time or space towards low-carbon electricity |

## How it fits

- **Below:** [thermodynamics](../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md) sets the cost of computation; the [end of Dennard scaling](../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md) made energy the binding constraint; [cloud computing](../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) concentrates load where efficiency is highest; [training at scale](../13-artificial-intelligence/03-deep-learning/training-at-scale.md) is the fastest-growing demand.
- **Above:** nothing sits above this layer; energy and carbon budgets flow back down as non-functional [requirements](../12-software-engineering/02-process/requirements.md).
- **Siblings:** [ethics](ethics-and-professional-responsibility.md) asks who bears the costs (local grids, water, places e-waste is shipped); [law and policy](law-privacy-and-policy.md) increasingly mandates disclosure and repair, as in European Union (EU) data-centre reporting rules; [history](history-of-computing.md) shows each cost drop expanding total use.

## Common misconceptions

- **"A low PUE means a green data centre."** PUE ignores grid carbon, water, embodied hardware and whether the work is useful.
- **"More efficient hardware will shrink computing's footprint."** Only if demand grows more slowly than efficiency improves; the rebound effect often absorbs the gain.
- **"The energy of one AI query is either trivial or catastrophic."** It is small per query and significant in aggregate; single headline numbers hide wide uncertainty.

## Go deeper

- Luiz André Barroso, Urs Hölzle and Parthasarathy Ranganathan, *The Datacenter as a Computer* (3rd ed., 2018): energy, PUE and efficiency at warehouse scale.
- Udit Gupta et al., "Chasing Carbon: The Elusive Environmental Footprint of Computing" (HPCA 2021): why embodied carbon matters.
- David Patterson et al., "Carbon Emissions and Large Neural Network Training" (2021): method and figures for AI training energy.
