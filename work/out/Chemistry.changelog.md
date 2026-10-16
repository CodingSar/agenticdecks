# Chemistry changelog

New deck, **304 notes** (284 basic, 20 cloze), 346 cards, 12 subdecks, 122 analogies (40%), 13 SVG diagrams (`media/chem_*.svg`, 14 references), all `guid: null`.

Scope: chemistry from the high-school picture to a master's-level grasp of the ideas, for a technically literate adult. Each subdeck climbs from first principles to graduate-level concepts (Slater's rules, Bent's rule, Raoult/azeotropes, Ellingham diagrams, Pourbaix, Marcus theory, Hammond postulate, Curtin–Hammett, Woodward–Hoffmann, ligand field vs crystal field, Hartree–Fock vs DFT, CCSD(T), machine-learned potentials). Every subdeck is anchored in everyday and practical chemistry: kitchen, body, bathroom cabinet, garage, garden, lab bench, industry and environment.

Written by six parallel writer agents (two subdecks each) to `work/WRITER_BRIEF.md` plus a chemistry brief; merged, deduplicated and validated afterwards.

Subdecks: 01 Atoms, Elements & the Periodic Table (25) · 02 Chemical Bonding & Molecular Structure (25) · 03 States of Matter, Solutions & Mixtures (26) · 04 Thermochemistry, Equilibrium & Spontaneity (23) · 05 Acids, Bases & Electrochemistry (26) · 06 Reaction Kinetics & Catalysis (26) · 07 Organic Chemistry: Structure & Reactivity (26) · 08 Organic Synthesis, Spectroscopy & Natural Products (26) · 09 Inorganic, Coordination & Materials Chemistry (25) · 10 Quantum & Computational Chemistry (26) · 11 Biochemistry & Polymers (26) · 12 Analytical, Environmental & Industrial Chemistry (24).

Diagrams: periodic trends, O₂ molecular-orbital diagram, water phase diagram, thermodynamic vs kinetic control, galvanic cell, catalysed vs uncatalysed energy profile, SN2 transition state, cyclohexane chair, ¹H NMR of ethanol, octahedral crystal-field splitting (high vs low spin), 2s/2p radial nodes, chromatography column and trace, weak-acid titration curve. Hand-drawn SVG, 2–8 KB each, all rendered and checked.

## Merge pass
Six pairs written independently by two agents were resolved: ice floats (kept one, re-angled the other to H₂O vs H₂S boiling points), CO toxicity (merged into one, cooperative effect kept in `extra`), Maillard vs caramelisation (one dropped), Haber–Bosch compromise (one dropped), 4s/3d order (one dropped), HSAB toxicity (re-angled to lead in bone). Two catalyst cards were kept as different angles (equilibrium vs mechanism). Bare `<`/`>` outside MathJax are HTML-escaped.

## Deliberately left out
- Nomenclature drills, reaction tables, formula sheets and problem-solving procedures.
- Biography and dates; names stay only where they are the vocabulary (Haber, Le Chatelier, Diels–Alder, Grignard, Suzuki).
- Glass, ceramics, superconductors, gel electrophoresis, eutrophication, acid-rain mechanism and some cooking cards (ceviche, sauces) were cut by the writers to keep subdecks atomic and 23–26 notes; candidates for a later pass.
- Numbers beyond anchor values (Avogadro, Kw, Faraday, blood pH, N≡N bond energy, C–H bond energy, 22.4 L/mol).

## Overlap with existing decks avoided
- Physics: no cards on the laws of thermodynamics, entropy = log Ω, Boltzmann distribution, kinetic theory, ideal gas derivation, Schrödinger equation, hydrogen orbitals as standing waves, Pauli exclusion, blackbody, nuclear binding or decay types. Chemistry takes the chemical angle (dissolution, ΔG and K, orbital nodes and penetration, Born–Oppenheimer, Hückel, DFT). `similar.py` at 0.4: one cross pair (surface tension, different angle), kept.
- Physics for Datacenters, Quantitative Foundations, Foundations: no pairs above 0.4.
