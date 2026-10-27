# Transmission and the chain of infection

> **Layer:** [07 Microbiology and Immunology](../README.md) › [Microbes and infection](README.md)
> **Builds on:** [Pathogenesis, virulence and toxins](pathogenesis-virulence-and-toxins.md), [Viruses](viruses.md), [Compartment models and exponential processes](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md), [Pregnancy, placenta and lactation](../../06-physiology/09-reproduction-and-the-life-course/pregnancy-placenta-and-lactation.md)
> **Enables:** [Infectious disease dynamics](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md), [Surveillance and outbreak investigation](../../10-epidemiology-and-evidence/01-epidemiology/surveillance-and-outbreak-investigation.md), [Infection control and healthcare-associated infection](../../12-organ-system-specialties/08-infectious-diseases/infection-control-and-healthcare-associated-infection.md), [Global health and pandemics](../../15-medicine-in-society/03-populations-and-the-future/global-health-and-pandemics.md)

## Essence

An infectious disease persists only if each case produces, on average, at least one more. The path from one host to the next is a chain with six links: an agent, a reservoir where it lives, a portal of exit, a mode of transmission, a portal of entry and a susceptible host. Every control measure breaks one link, and the biology of the microbe decides which links are weak: an enveloped virus that dies in minutes on a dry surface must pass directly between people; a spore-former can wait in soil for decades. Seen quantitatively, transmission is a branching process whose growth rate, the reproduction number, determines whether an outbreak explodes, smoulders or dies, and what fraction of a population must be immune to stop it.

## Core tenets

1. **The chain has six links and control breaks one of them.** Agent (kill it: antimicrobials, disinfection), reservoir (remove it: cull, treat carriers, clean water), portal of exit (cover it: masks, wound dressings), mode (interrupt it: hand hygiene, ventilation, bed nets, condoms, needle exchange), portal of entry (protect it: gloves, intact skin, mucosal barriers) and susceptible host (immunise, correct malnutrition). Hand hygiene, shown to work by Semmelweis in 1847, remains the single most effective hospital measure.

2. **The mode of transmission follows from where the microbe replicates and how long it survives outside.** Respiratory pathogens leave in droplets and aerosols, a continuum in which small particles stay airborne for hours in poorly ventilated rooms. Gut pathogens take the faecal-oral route through water, food and hands. Bloodborne agents (hepatitis B and C, Human Immunodeficiency Virus (HIV)) need blood or sexual contact because they do not survive the environment. Vector-borne agents have made an insect part of their life cycle. Enveloped viruses are destroyed by soap and drying; non-enveloped viruses (norovirus, hepatitis A) and spores survive on surfaces for days to years.

3. **The reservoir decides whether a disease can be eradicated.** Smallpox was eradicated (1980) because humans were its only reservoir and the vaccine was good; polio and measles are candidates for the same reason. Zoonoses can only be controlled: an estimated 60% of emerging infectious diseases and most pandemics (influenza, HIV, Ebola, COVID-19) originate in animals, so land use, farming and wildlife trade are infection-control variables. Environmental reservoirs (*Legionella* in water systems, *Clostridium tetani* in soil) can never be removed, only engineered around.

4. **Transmission is a branching process summarised by the reproduction number.** The basic reproduction number, R0, is the average number of secondary cases produced by one case in a fully susceptible population: R0 = (contacts per unit time) x (probability of transmission per contact) x (duration of infectiousness). Each term is a lever. Below 1 the disease dies out; above 1 it grows exponentially until susceptibles are depleted. The effective number, R, falls as immunity accumulates, and transmission stops when the immune fraction exceeds 1 - 1/R0: ~95% for measles (R0 ~12 to 18), ~50 to 70% for influenza. This is herd immunity; the full dynamics are in [infectious disease dynamics](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md).

5. **The timing of infectiousness relative to symptoms sets what control can achieve.** The incubation period is the time from exposure to symptoms; the latent period is the time to becoming infectious. If infectiousness begins after symptoms (SARS in 2003, smallpox), isolating the sick stops transmission. If it begins before, or if many infections are asymptomatic (SARS-CoV-2, polio, HIV, hepatitis B), isolation of cases alone fails and testing, contact tracing or population measures are needed. Carriers, people who shed without symptoms for months or years (*Salmonella* Typhi, hepatitis B, meningococcus), sustain diseases that would otherwise burn out.

6. **Route and dose change the disease as much as the organism does.** *Yersinia pestis* through a flea bite causes bubonic plague; inhaled, it causes pneumonic plague with near-certain death and person-to-person spread. A few *Shigella* suffice to infect but millions of *Vibrio cholerae* are needed, so cholera needs contaminated water whereas shigellosis spreads on hands.

7. **Vertical transmission crosses the one barrier the fetus cannot defend.** Some agents cross the placenta (rubella, cytomegalovirus, *Toxoplasma*, syphilis, Zika), causing malformation when they hit organogenesis; others are acquired at birth (hepatitis B, HIV, herpes simplex, group B streptococcus) or in breast milk. Because maternal Immunoglobulin G (IgG) crosses the placenta, the mother's immunity is the fetus's, which is why immunising pregnant women protects newborns against pertussis and tetanus.

8. **Hospitals are transmission engines.** They concentrate susceptible hosts, breach barriers with catheters and wounds, select resistant organisms with antibiotics, and move staff between patients. Healthcare-associated infection affects roughly 5 to 10% of inpatients in high-income countries (2010s to 2020s estimates), higher elsewhere. The counter-measures are the chain again: standard precautions for every patient, extra precautions by route, and surveillance.

## Key concepts

| Term | Meaning |
|---|---|
| Reservoir | Where an agent normally lives and multiplies: human, animal or environment |
| Zoonosis | Infection transmitted from animals to humans |
| Vector | An arthropod that carries an agent between hosts, mechanically or as part of its life cycle |
| Droplet versus aerosol | Large particles that fall within metres versus small ones that remain suspended |
| Basic reproduction number (R0) | Mean secondary cases from one case in a fully susceptible population |
| Herd immunity threshold | Immune fraction, 1 - 1/R0, above which transmission declines |
| Incubation period | Exposure to symptom onset |
| Latent period | Exposure to onset of infectiousness |
| Carrier | A person who sheds an agent without symptoms |
| Vertical transmission | From mother to child across the placenta, at birth or by breast milk |

## How it fits

- **Below:** exponential growth and compartment (susceptible-infected-recovered) models come from [compartment models](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md); placental transfer of IgG and of some pathogens follows the physiology of [pregnancy and the placenta](../../06-physiology/09-reproduction-and-the-life-course/pregnancy-placenta-and-lactation.md); environmental survival depends on microbial structure described in [bacteria](bacteria.md) and [viruses](viruses.md).
- **Above:** R0, generation intervals and herd immunity are developed in [infectious disease dynamics](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md); finding and stopping chains is [surveillance and outbreak investigation](../../10-epidemiology-and-evidence/01-epidemiology/surveillance-and-outbreak-investigation.md); the hospital case is [infection control](../../12-organ-system-specialties/08-infectious-diseases/infection-control-and-healthcare-associated-infection.md); pandemics and eradication are in [global health and pandemics](../../15-medicine-in-society/03-populations-and-the-future/global-health-and-pandemics.md).
- **Siblings:** transmission is the last step of [pathogenesis](pathogenesis-virulence-and-toxins.md); the susceptible-host link is the whole of immunology, and making hosts non-susceptible is [vaccination](../03-adaptive-immunity/immunological-memory-and-vaccination.md).

## Common misconceptions

- **"A deadly pathogen spreads fastest."** Spread depends on R0 and on the timing of infectiousness; Ebola, with high lethality and transmission only from the obviously ill, is easier to contain than a mild virus shed before symptoms.
- **"Herd immunity is reached when most people have been infected."** It is reached when the immune fraction exceeds 1 - 1/R0, and for measles that is ~95%, achievable only by vaccination.

## Go deeper

- Roy M. Anderson and Robert M. May, *Infectious Diseases of Humans: Dynamics and Control* (1991): the mathematics of R0 and herd immunity.
- Kate E. Jones et al., "Global trends in emerging infectious diseases", *Nature* (2008): the zoonotic share of emerging infections.
- David L. Heymann (ed.), *Control of Communicable Diseases Manual* (21st ed., 2022): the chain of infection applied, disease by disease.
