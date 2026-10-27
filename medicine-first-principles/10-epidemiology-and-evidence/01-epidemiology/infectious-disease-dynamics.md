# Infectious disease dynamics

> **Layer:** [10 Epidemiology and Evidence](../README.md) › [Epidemiology](README.md)
> **Builds on:** [Compartment models and exponential processes](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md), [Transmission and the chain of infection](../../07-microbiology-and-immunology/01-microbes-and-infection/transmission-and-the-chain-of-infection.md), [Immunological memory and vaccination](../../07-microbiology-and-immunology/03-adaptive-immunity/immunological-memory-and-vaccination.md), [Measures of frequency and association](measures-of-frequency-and-association.md)
> **Enables:** [Surveillance and outbreak investigation](surveillance-and-outbreak-investigation.md), [Infection control and healthcare-associated infection](../../12-organ-system-specialties/08-infectious-diseases/infection-control-and-healthcare-associated-infection.md), [Global health and pandemics](../../15-medicine-in-society/03-populations-and-the-future/global-health-and-pandemics.md)

## Essence

Infectious disease breaks the assumption behind the rest of epidemiology: that one person's risk is independent of another's. Whether you catch influenza depends on how many people around you have it, so the incidence of an infection depends on its own prevalence. This feedback makes epidemics grow exponentially, peak and fade while many people remain susceptible, and it makes vaccination protect the unvaccinated. The number that captures the feedback is the **basic reproduction number** (R0): the mean number of secondary cases one infectious person generates in a fully susceptible population. Growth rate, final size, herd immunity threshold and the effect of control all follow from R0 and the fraction still susceptible.

## Core tenets

1. **R0 is a product of contact rate, transmission probability per contact and duration of infectiousness.** R0 = c × p × D. Every intervention acts on one factor: distancing lowers c; masks, condoms and clean water lower p; treatment and isolation shorten D. R0 belongs to the pathogen *and* the population: the same virus has a different R0 in a crowded city and a scattered village. Measles (R0 roughly 12–18 in historical populations) and seasonal influenza (around 1–2) sit at opposite ends.

2. **An epidemic grows only while the effective reproduction number exceeds one.** R = R0 × s, where s is the susceptible fraction. Early on s ≈ 1 and cases grow exponentially, with a doubling time set by R0 and the generation interval. As infection depletes susceptibles R falls; once s < 1/R0, incidence declines even though many susceptibles remain. Epidemics end for want of susceptibles, not of pathogen.

3. **Herd immunity is the threshold at which chains can no longer sustain themselves.** Setting R0 × s = 1 gives the critical immune fraction 1 − 1/R0: about 50% for R0 = 2, about 94% for R0 = 16. Immunity in some protects others by breaking chains before they arrive. This is why vaccine coverage is a public good, why measles returns when coverage falls a few points, and why pockets of low coverage matter more than the national average.

4. **The compartment model turns these ideas into equations.** The Susceptible–Infectious–Recovered (SIR) model (Kermack and McKendrick, 1927) moves people S → I at rate β S I / N and I → R at rate γ I, with R0 = β/γ. It is a [compartment model](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md) with one nonlinear term, and that term is the whole story: the force of infection on each susceptible is proportional to the prevalence of infectious people.

   ```
   S  --(beta * I / N)-->  I  --(gamma)-->  R
   susceptible          infectious        immune or dead
   ```

5. **Final size exceeds the herd immunity threshold because the epidemic overshoots.** Incidence peaks when s = 1/R0, but the many people infected at the peak go on to infect others. For R0 = 2 the threshold is 50% but the final size in a closed population is about 80%. Reaching herd immunity by infection therefore costs far more than reaching it by vaccination.

6. **Heterogeneity and superspreading make the mean misleading.** The distribution of secondary cases is usually highly skewed: most infected people transmit to nobody, a few to dozens (the dispersion parameter k is small for coronaviruses and measles). So introductions often die out by chance, and measures aimed at high-transmission settings achieve more than uniform ones. Age structure and contact networks also violate the homogeneous mixing the simple model assumes.

7. **Incubation, latent and infectious periods are different clocks, and their alignment decides what control is possible.** Incubation runs from infection to symptoms; latency from infection to infectiousness. When infectiousness precedes symptoms (SARS-CoV-2, influenza), isolating the symptomatic comes too late and control depends on tracing or population measures. When it follows them (SARS in 2003, smallpox), isolating cases at onset suffices.

8. **Births, waning immunity and pathogen evolution make dynamics oscillate.** Births replenish susceptibles, so endemic childhood infections cycle (biennial measles in pre-vaccine cities). Antigenic drift ([host–pathogen coevolution](../../04-genetics-evolution-and-development/02-evolution/host-pathogen-coevolution-and-resistance.md)) does the same for influenza. Partial vaccination can raise the average age at infection, which matters when severity depends on age (rubella in pregnancy). Infection is a [nonlinear oscillating system](../../01-quantitative-and-scientific-foundations/03-systems-and-models/nonlinear-dynamics-oscillations-and-networks.md), and intuition built on static risk fails on it.

## Key concepts

| Term | Meaning |
|---|---|
| Basic reproduction number (R0) | Mean secondary cases from one case in a wholly susceptible population |
| Effective reproduction number (R) | R0 × susceptible fraction, given current immunity and behaviour |
| Herd immunity threshold | Immune fraction 1 − 1/R0 above which R < 1 |
| Generation interval | Time from one person's infection to the infection of those they infect |
| Serial interval | Time between symptom onset in an infector and in their infectee; what field data give |
| Incubation period | Infection to symptom onset |
| Latent period | Infection to onset of infectiousness |
| Force of infection | Per-susceptible rate of acquiring infection; proportional to infectious prevalence |
| Dispersion (k) | How unevenly secondary cases are distributed; low k means superspreading |
| Attack rate | Proportion of an exposed population that becomes ill over the outbreak |

## How it fits

- **Below:** the mathematics is a [compartment model](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md) with a feedback term; who is susceptible and for how long is [immunological memory](../../07-microbiology-and-immunology/03-adaptive-immunity/immunological-memory-and-vaccination.md); the routes that set c and p are the [chain of infection](../../07-microbiology-and-immunology/01-microbes-and-infection/transmission-and-the-chain-of-infection.md).
- **Above:** [surveillance](surveillance-and-outbreak-investigation.md) estimates R from case counts and acts on it; [infection control](../../12-organ-system-specialties/08-infectious-diseases/infection-control-and-healthcare-associated-infection.md) applies these principles inside a hospital; [pandemic response](../../15-medicine-in-society/03-populations-and-the-future/global-health-and-pandemics.md) is these equations under political constraint.
- **Siblings:** the rest of this parent assumes independent risks; this leaf is where that assumption fails and the [measures of frequency](measures-of-frequency-and-association.md) acquire feedback.

## Common misconceptions

- **"An epidemic ends when everyone has been infected."**: it ends when R falls below 1, which happens once the susceptible fraction falls below 1/R0; a substantial fraction remains uninfected.
- **"R0 is a fixed property of the virus."**: it depends on contact patterns, so it differs between populations and seasons.
- **"A vaccine only protects the person who receives it."**: by lowering the susceptible fraction it lowers R for everyone, which is why infants too young for measles vaccine are safe in a well-vaccinated population and exposed in a poorly vaccinated one.

## Go deeper

- Roy M. Anderson and Robert M. May, *Infectious Diseases of Humans: Dynamics and Control* (1991): the foundational text for R0, herd immunity and age-structured models.
- Matt J. Keeling and Pejman Rohani, *Modeling Infectious Diseases in Humans and Animals* (2008): the modern computational treatment.
- W. O. Kermack and A. G. McKendrick, "A contribution to the mathematical theory of epidemics", *Proceedings of the Royal Society A* (1927): the original SIR model and threshold theorem.
