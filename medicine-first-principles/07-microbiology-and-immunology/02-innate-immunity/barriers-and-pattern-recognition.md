# Barriers and pattern recognition

> **Layer:** [07 Microbiology and Immunology](../README.md) › [Innate immunity](README.md)
> **Builds on:** [Pathogenesis, virulence and toxins](../01-microbes-and-infection/pathogenesis-virulence-and-toxins.md), [Receptors and ligands](../../02-biochemistry-and-molecular-biology/04-cell-signalling/receptors-and-ligands.md), [Second messengers and kinase cascades](../../02-biochemistry-and-molecular-biology/04-cell-signalling/second-messengers-and-kinase-cascades.md), [Epithelium](../../05-tissues-and-anatomy/01-tissues/epithelium.md), [The skin as barrier and sensor](../../06-physiology/10-musculoskeletal-system-and-skin/the-skin-as-barrier-and-sensor.md)
> **Enables:** [Complement, phagocytes and the inflammatory cascade](complement-phagocytes-and-the-inflammatory-cascade.md), [Antigen presentation and MHC](../03-adaptive-immunity/antigen-presentation-and-mhc.md), [Acute inflammation](../../08-pathology/01-cell-and-tissue-injury/acute-inflammation.md), [Immunological memory and vaccination](../03-adaptive-immunity/immunological-memory-and-vaccination.md)

## Essence

The first defence is to keep microbes out; the second is to recognise, within minutes, that one has got in. Barriers stop the vast majority of encounters without any immune cell being involved, and most infections begin where a barrier has been breached. Behind the barrier, innate immunity does not recognise individual microbes. It recognises *patterns*: a few dozen germline-encoded receptors that bind molecular motifs shared by whole classes of microbe and absent from the host, such as lipopolysaccharide, flagellin or double-stranded RNA. Because the receptors are inherited rather than generated, the response is immediate but cannot learn. The same receptors also detect the debris of the body's own damaged cells, which is why injury without infection still produces inflammation.

## Core tenets

1. **Barriers do most of the work, and most infections are barrier failures.** Keratinised skin, the mucus and ciliary escalator of the airway, gastric acid at pH 1 to 2, the flushing of urine and tears, lysozyme and defensins in secretions, epithelial tight junctions and a resident flora that occupies every niche mean that the body is exposed constantly and infected rarely. Burns, intravenous lines, urinary catheters, ventilator tubes, the thick mucus of cystic fibrosis and loss of stomach acid all cause infection by removing a barrier, not by adding a pathogen ([the skin as barrier](../../06-physiology/10-musculoskeletal-system-and-skin/the-skin-as-barrier-and-sensor.md), [the human microbiome](../01-microbes-and-infection/the-human-microbiome.md)).

2. **Innate recognition is of patterns, not antigens.** Janeway (1989) proposed that innate cells carry Pattern Recognition Receptors (PRRs) tuned to Pathogen-Associated Molecular Patterns (PAMPs): structures that are conserved because the microbe cannot do without them, shared by whole groups, and absent from the host. Lipopolysaccharide (LPS) marks Gram-negative bacteria, lipoteichoic acid and peptidoglycan Gram-positives, flagellin motile bacteria, beta-glucan fungi, unmethylated CpG DNA bacteria and DNA viruses, double-stranded RNA replicating RNA viruses. A few dozen receptors therefore cover most microbes, in contrast with the ~10^11 receptors of the adaptive system that each see one shape.

3. **Receptor location encodes where a molecule should not be.** Toll-Like Receptors (TLRs) on the cell surface (TLR4 for LPS, TLR2 for lipopeptides, TLR5 for flagellin) detect extracellular bacteria; TLRs inside endosomes (TLR3 for double-stranded RNA, TLR7 and 8 for single-stranded RNA, TLR9 for CpG DNA) detect nucleic acid of viruses that have been taken up; NOD-Like Receptors (NLRs) sense peptidoglycan fragments in the cytosol; RIG-I-like receptors sense cytosolic viral RNA; the cGAS-STING pathway senses cytosolic DNA, which belongs only in the nucleus or mitochondrion. Self nucleic acid is normally kept away from these compartments, and when it is not, as in lupus, the same sensors drive autoimmunity.

4. **Recognition converges on a few transcription factors and a few outputs.** Most PRRs signal through adaptor proteins (MyD88 for most TLRs, TRIF for TLR3 and TLR4) and kinase cascades to the transcription factor NF-kappaB, which switches on tumour necrosis factor, interleukin-1 and interleukin-6, and to interferon regulatory factors, which switch on type I interferons. The output is inflammation, an antiviral state, and the maturation of dendritic cells ([cytokines, interferons and NK cells](cytokines-interferons-and-nk-cells.md)). Inflammasomes, cytosolic complexes built on NLRP3 and other NLRs, activate caspase-1, which cleaves interleukin-1 beta into its active form and triggers pyroptosis, an inflammatory cell death that spills the contents of an infected cell.

5. **Damage is read with the same receptors as infection.** Dying cells release molecules that are normally hidden: adenosine triphosphate, uric acid crystals, mitochondrial DNA (bacterial in origin and so CpG-rich), the nuclear protein HMGB1. These Damage-Associated Molecular Patterns (DAMPs) engage TLRs and inflammasomes exactly as PAMPs do (Matzinger's "danger model"). This is why a myocardial infarction, a crush injury or a gout crystal produces fever, neutrophilia and a raised C-reactive protein with no microbe present ([acute inflammation](../../08-pathology/01-cell-and-tissue-injury/acute-inflammation.md)).

6. **Innate recognition licenses adaptive immunity.** A dendritic cell that has engaged its PRRs matures: it stops sampling, raises its Major Histocompatibility Complex (MHC) and co-stimulatory molecules, and migrates to a lymph node to activate T cells. Antigen without a PRR signal produces tolerance rather than immunity. This is why pure proteins make poor vaccines until an adjuvant, which is a PAMP or DAMP in a bottle, is added, and why the adaptive system almost never responds to self: self has no PAMPs ([antigen presentation and MHC](../03-adaptive-immunity/antigen-presentation-and-mhc.md)).

7. **Pattern recognition carries costs in both directions.** Too much: LPS sensed by TLR4 in bulk produces septic shock, and over-active inflammasomes cause the periodic fever syndromes. Too little: inborn loss of MyD88 or IRAK4 gives recurrent pyogenic bacterial infection in childhood, loss of TLR3 signalling gives herpes simplex encephalitis. Innate immunity is fast and broad precisely because it is not very discriminating.

## Key concepts

| Term | Meaning |
|---|---|
| Pattern Recognition Receptor (PRR) | Germline-encoded receptor for conserved microbial or damage motifs |
| Pathogen-Associated Molecular Pattern (PAMP) | Conserved microbial structure absent from the host (LPS, flagellin, dsRNA) |
| Damage-Associated Molecular Pattern (DAMP) | Host molecule released by injured cells that signals danger (ATP, HMGB1, uric acid) |
| Toll-Like Receptor (TLR) | Family of membrane PRRs on the surface and in endosomes |
| NOD-Like Receptor (NLR) | Cytosolic PRR family; several assemble inflammasomes |
| Inflammasome | Cytosolic complex that activates caspase-1 to release interleukin-1 beta and cause pyroptosis |
| cGAS-STING | Sensor pathway for cytosolic DNA leading to type I interferon |
| NF-kappaB | Transcription factor switching on the inflammatory cytokine programme |
| Adjuvant | Vaccine additive that supplies the innate signal a pure antigen lacks |

## How it fits

- **Below:** PRRs are [receptors](../../02-biochemistry-and-molecular-biology/04-cell-signalling/receptors-and-ligands.md) wired to [kinase cascades](../../02-biochemistry-and-molecular-biology/04-cell-signalling/second-messengers-and-kinase-cascades.md) of layer 02; the barriers are the [epithelia](../../05-tissues-and-anatomy/01-tissues/epithelium.md) of layer 05 and the [skin](../../06-physiology/10-musculoskeletal-system-and-skin/the-skin-as-barrier-and-sensor.md) and [gut barrier](../../06-physiology/06-gastrointestinal-system/the-gut-barrier-and-microbiome.md) of layer 06; PAMPs are the conserved structures of [bacteria](../01-microbes-and-infection/bacteria.md) and [viruses](../01-microbes-and-infection/viruses.md).
- **Above:** DAMP-driven inflammation is the mechanism of [acute inflammation](../../08-pathology/01-cell-and-tissue-injury/acute-inflammation.md) after any injury; adjuvants are central to [vaccination](../03-adaptive-immunity/immunological-memory-and-vaccination.md); TLR4 and LPS begin [sepsis](../../08-pathology/02-hemodynamic-disorders/hemorrhage-shock-and-sepsis.md); inflammasome and interleukin-1 blockers are in [anti-inflammatory and immunomodulatory drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anti-inflammatory-and-immunomodulatory-drugs.md).
- **Siblings:** recognition is the trigger; [complement, phagocytes and the inflammatory cascade](complement-phagocytes-and-the-inflammatory-cascade.md) is the effector response and [cytokines, interferons and NK cells](cytokines-interferons-and-nk-cells.md) are the messengers and the antiviral arm.

## Common misconceptions

- **"Innate immunity is non-specific."** It is highly specific for molecular classes (LPS, flagellin, CpG DNA); what it lacks is specificity for individual organisms and the ability to improve.
- **"Inflammation means infection."** DAMPs from sterile injury use the same receptors; infarction, trauma and gout inflame without a microbe.
- **"The adaptive system decides what to attack."** It needs permission from innate recognition; without a PRR signal, antigen presentation tends toward tolerance.

## Go deeper

- Charles A. Janeway Jr., "Approaching the asymptote? Evolution and revolution in immunology", *Cold Spring Harbor Symposia on Quantitative Biology* (1989): the prediction of pattern recognition receptors.
- Polly Matzinger, "Tolerance, danger, and the extended family", *Annual Review of Immunology* (1994): the danger model.
- Kenneth Murphy and Casey Weaver, *Janeway's Immunobiology* (10th ed., 2022), chapters 2 and 3: the standard treatment of innate recognition.
