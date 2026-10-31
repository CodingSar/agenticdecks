# Mathematical Practice and Discovery

> **Layer:** [15 Mathematics in Context](README.md)
> **Builds on:** [What a Proof Is](../00-logic-and-proof/02-methods-of-proof/what-a-proof-is.md), [Cases, Constructions and Counterexamples](../00-logic-and-proof/02-methods-of-proof/cases-constructions-and-counterexamples.md), [The Euler Characteristic](../07-topology/02-algebraic-topology/the-euler-characteristic.md), [History of Mathematics](history-of-mathematics.md), [Philosophy of Mathematics](philosophy-of-mathematics.md)
> **Enables:** [Computers and Proof](computers-and-proof.md), [Open Problems](open-problems.md), [Learning and Teaching Mathematics](learning-and-teaching-mathematics.md), [Research Integrity and Publication Bias (Medicine)](../../medicine-first-principles/10-epidemiology-and-evidence/02-evidence-based-medicine/research-integrity-and-publication-bias.md)

## Essence

Published mathematics looks like a chain of definitions, lemmas and proofs, but that is the finished product, not the process. Results are found by computing examples, spotting patterns, guessing, testing guesses against special cases, and failing many times; proofs are found by heuristics, analogies and partial arguments, and definitions are often adjusted to make a proof work. Proofs, once written, are checked by people, imperfectly: errors are common and are caught by refereeing, by readers and by later work. This leaf describes that practice and the mechanisms that make its output reliable despite individual fallibility.

## Core tenets

1. **Discovery often begins with data.** As a teenager, Gauss studied tables of primes and guessed that their density near x is about 1/ln x; the prime number theorem was proved a century later, in 1896. In 1995 David Bailey, Peter Borwein and Simon Plouffe found, by a computer search for integer relations, a new series for π that allows its hexadecimal digits to be computed individually, and then proved it by hand. Experiment proposes; proof disposes.

2. **Numerical evidence can mislead, so it never replaces proof.** Pólya conjectured in 1919 that at least half the numbers up to any n have an odd number of prime factors; the smallest counterexample, found in 1980, is 906,150,257. Every computed value of the prime-counting function π(x) lies below the logarithmic integral li(x), yet Littlewood proved in 1914 that the inequality reverses infinitely often. The Mertens conjecture was disproved in 1985 by Andrew Odlyzko and Herman te Riele, although no explicit counterexample is known. Patterns among small numbers can fail far beyond any computation.

3. **Problem solving has teachable heuristics.** George Pólya's *How to Solve It* (1945) divides solving into four phases: understand the problem, devise a plan, carry it out, and look back. His heuristics include: solve a special case, generalise, work backwards, find a related problem already solved, introduce auxiliary elements, and draw a figure. They do not guarantee success, but they turn being stuck into a list of moves to try.

4. **Proofs and counterexamples refine concepts: Lakatos's lesson.** Imre Lakatos's *Proofs and Refutations* (1976) reconstructs the history of Euler's formula V − E + F = 2 for polyhedra. A cube with a cubical hole inside, or a picture-frame polyhedron with V − E + F = 0, refutes it. Responses include "monster-barring" (that is not a polyhedron), exception-barring, and "lemma-incorporation": find the hidden assumption the proof used, here that the surface can be stretched onto a sphere, and make it an explicit hypothesis. The concept of polyhedron is sharpened by the proof, and the modern answer is the Euler characteristic, a topological invariant. Definitions are often outputs of research, not inputs.

5. **Errors are common, and correction is a collective process.** Alfred Kempe published a proof of the four colour theorem in 1879; in 1890 Percy Heawood found a fatal gap, while salvaging a proof that five colours suffice. Andrew Wiles announced a proof of Fermat's last theorem in 1993; refereeing found a gap, which he closed with Richard Taylor in 1994. Vladimir Voevodsky's discovery of errors in work of his own, including published work, led him to advocate computer-checked proofs. The system does not prevent mistakes; it makes important ones likely to be found.

6. **Refereeing certifies plausibility, and acceptance is social.** A journal referee checks that a result is new, interesting and, as far as is practical, correct; for long proofs, line-by-line checking is rarely possible. Acceptance therefore comes through use: others read, teach, simplify and build on a result, and confidence grows as they do. Richard De Millo, Richard Lipton and Alan Perlis (1979) argued that this social process is what makes mathematical proofs trusted. William Thurston's essay "On Proof and Progress in Mathematics" (1994) argued that what mathematicians produce is understanding, of which proofs are one vehicle.

7. **Open, large-scale collaboration works for some problems.** In January 2009 Timothy Gowers asked on his blog whether massively collaborative mathematics was possible. The first Polymath project found a new combinatorial proof of the density Hales–Jewett theorem for three letters within weeks, published under the pseudonym D. H. J. Polymath. After Yitang Zhang proved in 2013 that infinitely many pairs of primes differ by at most 70,000,000, the Polymath8 project reduced the bound to 4,680 and then, using James Maynard's new method, to 246. Collaboration exposes the messy process that publication usually hides.

## Key concepts

| Term | Meaning |
|---|---|
| Conjecture | A statement believed true on evidence but not yet proved |
| Heuristic | A rule of thumb that suggests a line of attack without guaranteeing success |
| Counterexample | An instance showing a general statement false |
| Monster-barring | Excluding a counterexample by redefining the objects concerned |
| Lemma-incorporation | Turning a hidden assumption of a proof into an explicit hypothesis |
| Refereeing | Expert review of a submitted paper for correctness and significance |
| Experimental mathematics | Using computation to discover patterns and identities later proved |

## How it fits

- **Below:** the standards of [proof](../00-logic-and-proof/02-methods-of-proof/what-a-proof-is.md) and of counterexamples; the Euler characteristic is Lakatos's central case; [history](history-of-mathematics.md) and [philosophy](philosophy-of-mathematics.md) frame what practice is aiming at.
- **Above:** nothing; this is the top layer.
- **Siblings:** [computers and proof](computers-and-proof.md) changes how checking is done; [open problems](open-problems.md) are where the process is visible in progress; [learning and teaching](learning-and-teaching-mathematics.md) asks how to pass these habits on.

## Common misconceptions

- **"Mathematicians proceed by pure deduction."** Discovery is inductive and experimental; deduction is how results are secured and presented.
- **"A published proof is a checked proof."** Refereeing is fallible, and errors in published papers are found regularly.
- **"Enough examples prove a theorem."** Pólya's conjecture and li(x) show that patterns can fail far beyond any computation.

## Go deeper

- G. Pólya, *How to Solve It* (1945): the classic account of heuristics.
- I. Lakatos, *Proofs and Refutations* (1976): a dialogue on how proofs and concepts evolve.
- W. P. Thurston, "On Proof and Progress in Mathematics" (1994): a working mathematician on what mathematics produces.
