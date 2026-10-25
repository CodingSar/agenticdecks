# Immunological memory and vaccination

> **Layer:** [07 Microbiology and Immunology](../README.md) › [Adaptive immunity](README.md)
> **Builds on:** [B cells and antibodies](b-cells-and-antibodies.md), [T cells](t-cells.md), [Barriers and pattern recognition](../02-innate-immunity/barriers-and-pattern-recognition.md), [Transmission and the chain of infection](../01-microbes-and-infection/transmission-and-the-chain-of-infection.md), [Time courses](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md)
> **Enables:** [Infectious disease dynamics](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md), [Levels of prevention](../../10-epidemiology-and-evidence/03-screening-and-prevention/levels-of-prevention.md), [Common childhood illness](../../14-life-course-mind-and-integrative-care/01-paediatrics/common-childhood-illness.md), [Global health and pandemics](../../15-medicine-in-society/03-populations-and-the-future/global-health-and-pandemics.md)

## Essence

Memory is what makes the adaptive system worth its slowness. A first encounter with a pathogen takes one to two weeks to produce useful antibody and T cells, which is long enough for most infections to cause disease. It leaves behind expanded clones of memory cells and plasma cells that secrete antibody indefinitely, so the second encounter is met within hours by a response that is larger, faster and better aimed, often before symptoms appear. Vaccination is the deliberate creation of that state without the disease: present the antigen together with the innate signal that makes the immune system take it seriously. The design and limits of every vaccine follow from how memory is made and lost.

## Core tenets

1. **Memory is more cells, pre-armed, with a lower threshold.** After a primary response, antigen-specific precursors are 10 to 1,000 times more frequent than in a naive person, already class-switched and affinity-matured (B cells) or differentiated into effector programmes (T cells), need less co-stimulation, and include tissue-resident cells waiting at the site of entry. The secondary response therefore peaks in days rather than weeks and consists of high-affinity Immunoglobulin G (IgG) rather than low-affinity Immunoglobulin M (IgM). A pathogen whose incubation period is longer than the recall time never gets to cause disease.

2. **Protection has two components with different time courses.** Pre-existing antibody from long-lived plasma cells acts instantly and can prevent infection altogether (sterilising immunity); its level decays with a half-life that ranges from months (pertussis, mumps) to effectively lifelong (measles, smallpox, tetanus toxoid after boosting) depending on how durable the plasma cells are. Memory cells act within days and limit disease even when antibody has waned. Serum antibody is the usual correlate of protection, but falling titres often overstate the loss of immunity ([time courses](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md)).

3. **A vaccine is antigen plus a danger signal.** Pure protein injected alone induces little, because dendritic cells are not activated and tend toward tolerance ([pattern recognition](../02-innate-immunity/barriers-and-pattern-recognition.md)). Live vaccines supply the signal by replicating; everything else needs an adjuvant: aluminium salts (which activate the inflammasome), oil emulsions, or defined Toll-like receptor agonists such as monophosphoryl lipid A.

4. **Vaccine platforms trade potency against safety and control.**

   | Platform | Examples | Strengths | Limits |
   |---|---|---|---|
   | Live attenuated | Measles, mumps, rubella, yellow fever, oral polio, BCG, varicella | Replicates, so strong, broad (antibody and CD8), often one or two doses, lifelong | Unsafe in severe immunodeficiency and some pregnancies; can revert (vaccine-derived polio) |
   | Inactivated whole organism | Injected polio, hepatitis A, whole-cell pertussis | Safe in all hosts | Needs adjuvant and boosters; antibody mostly |
   | Subunit, toxoid, recombinant | Tetanus, diphtheria, hepatitis B, acellular pertussis, HPV | Defined, safe, scalable | Needs adjuvant; immunity may wane |
   | Conjugate | Hib, pneumococcal, meningococcal | Converts a sugar into a T-dependent antigen; works in infants | Serotype-specific; replacement by uncovered serotypes |
   | Nucleic acid and viral vector | mRNA (SARS-CoV-2), adenoviral vectors | Host cells make the antigen, so both antibody and CD8; fast to design | Durability still being defined (2020s); storage |

5. **Herd immunity protects those who cannot be protected directly.** Each immune person removes a link from transmission chains; when the immune fraction exceeds 1 - 1/R0, each case produces fewer than one successor and incidence falls, protecting infants too young for vaccination and people with immunodeficiency. For measles that fraction is about 95%, so small drops in uptake bring outbreaks; for less transmissible diseases it is lower ([transmission](../01-microbes-and-infection/transmission-and-the-chain-of-infection.md), [infectious disease dynamics](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md)). Smallpox was eradicated in 1980 and two of three wild poliovirus types by 2019; both needed a human-only reservoir and a vaccine that interrupts transmission.

6. **Vaccines fail where the pathogen outruns or hides from memory.** Influenza drifts, so the vaccine is reformulated yearly and protects partially. Human Immunodeficiency Virus (HIV) mutates faster still, integrates into the genome and hides its conserved sites; forty years of effort have produced no licensed vaccine (2025). Malaria cycles through antigenically distinct stages and variants, and its first vaccines (2021 onward) give partial protection. BCG induces the granuloma-based control of tuberculosis only incompletely. Infants under six months respond poorly to many antigens and are protected instead by maternal IgG, which is why pregnant women are vaccinated against pertussis and tetanus.

7. **Vaccines are judged like any intervention, by harm against benefit, at population scale.** Serious adverse events exist and are rare: anaphylaxis at roughly one per million doses, intussusception with the first rotavirus vaccine, vaccine-derived poliomyelitis at about one per million first doses of oral vaccine, rare clotting and myocarditis signals with specific COVID-19 vaccines (2021). Against them stand the diseases prevented: measles alone killed an estimated 2.6 million people a year before vaccination and about 100,000 a year in the 2020s. Because the benefit is partly to other people, vaccination is both an individual decision and a public programme; see [global health and pandemics](../../15-medicine-in-society/03-populations-and-the-future/global-health-and-pandemics.md).

## Key concepts

| Term | Meaning |
|---|---|
| Primary and secondary response | First, slow, IgM-dominated response; later fast, IgG-dominated recall |
| Memory B and T cells | Long-lived, expanded, pre-differentiated antigen-specific lymphocytes |
| Long-lived plasma cell | Marrow-resident antibody factory that maintains titres for years |
| Correlate of protection | A measurable quantity (usually antibody titre) that predicts protection |
| Adjuvant | Component supplying the innate signal that makes antigen immunogenic |
| Live attenuated vaccine | Weakened replicating organism; strong but unsafe in immunodeficiency |
| Conjugate vaccine | Polysaccharide linked to protein to obtain T-cell help |
| Herd immunity threshold | Immune fraction 1 - 1/R0 above which transmission declines |
| Passive immunisation | Transfer of ready-made antibody for immediate, temporary protection |

## How it fits

- **Below:** the cells of memory are made by the processes in [B cells](b-cells-and-antibodies.md) and [T cells](t-cells.md); the danger signal is [innate recognition](../02-innate-immunity/barriers-and-pattern-recognition.md); herd immunity is a property of the [chain of infection](../01-microbes-and-infection/transmission-and-the-chain-of-infection.md); antibody decay is an exponential [time course](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md).
- **Above:** vaccination is the paradigm of primary prevention in [levels of prevention](../../10-epidemiology-and-evidence/03-screening-and-prevention/levels-of-prevention.md); its population effects are modelled in [infectious disease dynamics](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md); the schedule and the diseases it prevents are in [common childhood illness](../../14-life-course-mind-and-integrative-care/01-paediatrics/common-childhood-illness.md); programmes and eradication are in [global health](../../15-medicine-in-society/03-populations-and-the-future/global-health-and-pandemics.md).
- **Siblings:** memory is the product of the [germinal centre](b-cells-and-antibodies.md) and of [T-cell](t-cells.md) contraction; live vaccines are contraindicated in the conditions described in [immunodeficiency](../04-immunity-in-disease/immunodeficiency.md).

## Common misconceptions

- **"Natural infection gives better immunity than vaccination."** Sometimes it gives longer immunity, at the price of the disease; for tetanus, papillomavirus and pneumococcus the vaccine gives better immunity than infection does.
- **"Falling antibody means immunity is gone."** Memory cells persist after titres fall and recall in days; for many vaccines protection outlasts measurable antibody.

## Go deeper

- Stanley A. Plotkin, Walter A. Orenstein, Paul A. Offit and Kathryn M. Edwards (eds.), *Plotkin's Vaccines* (8th ed., 2023): the reference on every vaccine and the immunology behind it.
- Stanley A. Plotkin, "Correlates of protection induced by vaccination", *Clinical and Vaccine Immunology* (2010): what antibody titres do and do not tell us.
- Rafi Ahmed and David Gray, "Immunological memory and protective immunity: understanding their relation", *Science* (1996): the two components of protection.
