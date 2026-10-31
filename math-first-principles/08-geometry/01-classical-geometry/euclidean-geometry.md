# Euclidean Geometry

> **Layer:** [08 Geometry](../README.md) › [Classical Geometry](README.md)
> **Builds on:** [Axioms, definitions and theorems](../../00-logic-and-proof/03-the-axiomatic-method/axioms-definitions-and-theorems.md), [The real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md), [Inner products and orthogonality](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md)
> **Enables:** [Non-Euclidean geometry](non-euclidean-geometry.md), [Projective geometry](projective-geometry.md), [The Erlangen programme](the-erlangen-programme.md), [Ruler-and-compass constructions](../../05-abstract-algebra/03-galois-theory/ruler-and-compass-constructions.md)

## Essence

Euclid's *Elements*, written in Alexandria about 2,300 years ago, derives plane geometry from five postulates, and the fifth, the parallel postulate, never looked as obvious as the rest. Two thousand years of attempts to deduce it from the others failed, and the failure became a discovery: it is independent. Close reading also showed that Euclid's proofs use facts the diagrams supply but the postulates do not, such as two circles meeting. Hilbert's axioms of 1899 made every such assumption explicit, and with a completeness axiom they have a single model, the plane ℝ² with its usual distance.

## Core tenets

1. **The fifth postulate is a different kind of statement from the other four.** The first four let us join two points, extend a segment, draw any circle and compare right angles. The fifth says that if a line crossing two others makes interior angles on one side summing to less than two right angles, those lines meet on that side: a claim about arbitrarily distant points that no drawing can check. Euclid avoids it in Propositions I.1 to I.28 and first uses it in I.29. What can be proved without it is called neutral geometry, and it is shared with the hyperbolic plane of [non-Euclidean geometry](non-euclidean-geometry.md).

2. **The parallel postulate has many equivalent forms.** Given the other axioms, Archimedes' axiom among them, each of these is equivalent to it: through a point off a line there is exactly one parallel (Playfair's axiom); some triangle has angle sum π; a rectangle exists; two triangles can be similar without being congruent. In neutral geometry every angle sum is at most π (the Saccheri–Legendre theorem): Legendre's construction halves one angle while keeping the angle sum, and after enough halvings Archimedes' axiom leaves no room for an excess. Dehn showed that Archimedes' axiom is needed, by building planes where every angle sum is π yet parallels are not unique.

3. **Euclid's proofs have gaps that the diagrams fill.** Proposition I.1 builds an equilateral triangle by intersecting two circles, but no postulate says they meet; in the rational plane ℚ², the unit circles about (0, 0) and (1, 0) would meet at (½, √3/2), which is missing. Betweenness is never defined, so the fact that a line entering a triangle must leave it (Pasch's axiom, 1882) is used silently. The side–angle–side congruence of I.4 is "proved" by laying one triangle on the other, a motion the axioms never introduce.

4. **Hilbert turned each hidden assumption into an axiom.** *Grundlagen der Geometrie* (1899) leaves point, line, plane, "lies on", "between" and "congruent" undefined and groups its axioms into incidence, order (with Pasch's axiom), congruence (with side–angle–side as an axiom), parallels and continuity (Archimedes' axiom, with a completeness axiom added in later editions). Proofs may use only the axioms, never the meaning of the words; Hilbert said one should be able to read "tables, chairs and beer mugs" for "points, lines and planes". This is the modern [axiomatic method](../../00-logic-and-proof/03-the-axiomatic-method/axioms-definitions-and-theorems.md): a theory and its models, not self-evident truths.

5. **With completeness the axioms are categorical: the Cartesian plane is their only model.** Hilbert's arithmetic of segments defines sums and products of lengths by construction, and the axioms make these an ordered field; Archimedes' axiom and completeness force it to be [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md). So coordinates are a theorem, not an assumption. Without completeness there are other models: the plane over the numbers constructible by ruler and compass satisfies every other axiom and all of Euclid's Book I, which is why [ruler-and-compass constructions](../../05-abstract-algebra/03-galois-theory/ruler-and-compass-constructions.md) become a question about fields.

6. **Every isometry of ℝⁿ is a rigid motion x ↦ Ax + b with A orthogonal.** An isometry f fixing the origin preserves lengths, and polarisation turns lengths into [inner products](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md), so f preserves ⟨x, y⟩. Expanding ‖f(x + y) − f(x) − f(y)‖² then gives 0, so f is linear and orthogonal. Euclid's congruence, "one figure can be moved onto the other", therefore means "related by an element of the Euclidean group", the starting point of [the Erlangen programme](the-erlangen-programme.md).

   ```
   ⟨x, y⟩ = ( ‖x‖² + ‖y‖² − ‖x − y‖² ) / 2
   ```

7. **Elementary geometry is decidable.** Tarski axiomatised plane geometry in first-order logic, using only points, betweenness and equidistance, and showed the theory complete and decidable by translating it into the ordered field of real numbers and eliminating quantifiers, as in [quantifier elimination](../../13-structure-and-metamathematics/03-model-theory-and-independence/quantifier-elimination-and-decidable-theories.md). Arithmetic is undecidable; first-order geometry escapes because it cannot define the integers.

## Key concepts

| Term | Meaning |
|---|---|
| Parallel postulate | Euclid's fifth postulate; equivalent, given the others, to Playfair's axiom |
| Playfair's axiom | Through a point not on a line there is exactly one parallel to it |
| Neutral geometry | What follows from the axioms without the parallel postulate |
| Pasch's axiom | A line entering a triangle through one side, missing the vertices, leaves through another |
| Side–angle–side | Two sides and the included angle fix a triangle up to congruence; an axiom for Hilbert |
| Archimedes' axiom | Enough copies of any segment exceed any other segment |
| Completeness axiom | No points can be added while keeping the other axioms; forces the coordinate field to be ℝ |
| Isometry | A distance-preserving map; in ℝⁿ, x ↦ Ax + b with A orthogonal |
| Categorical | Having exactly one model up to isomorphism |

## How it fits

- **Below:** The [axiomatic method](../../00-logic-and-proof/03-the-axiomatic-method/axioms-definitions-and-theorems.md) supplies theories and models, the real numbers the unique model, and inner products length and angle.
- **Above:** Euclidean space is the flat model space of [Riemannian manifolds](../02-differential-geometry/riemannian-manifolds.md) and the setting of [convex sets](../03-convex-and-discrete-geometry/convex-sets-and-separation.md).
- **Siblings:** [Non-Euclidean geometry](non-euclidean-geometry.md) proves the fifth postulate independent; [projective geometry](projective-geometry.md) adds points at infinity; [symmetry groups and tilings](symmetry-groups-and-tilings.md) classifies the discrete groups of rigid motions.

## Common misconceptions

- **"Euclid's proofs are rigorous by modern standards"**: They are careful but rely on diagrams for continuity and betweenness; Hilbert needed new axioms to complete them.
- **"The parallel postulate was eventually proved"**: It was proved unprovable. The hyperbolic plane satisfies every other axiom and denies it.
- **"Euclidean geometry is a fact about physical space"**: It is a mathematical theory. Which geometry space obeys is an empirical question, and [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md) says space-time is curved.

## Go deeper

- Heath, *The Thirteen Books of Euclid's Elements* (1908): the standard English translation, with commentary on each gap.
- Hilbert, *Grundlagen der Geometrie* (1899): the axioms themselves, translated as *Foundations of Geometry*.
- Hartshorne, *Geometry: Euclid and Beyond* (2000): Euclid read through Hilbert's axioms, including the field of segments.
- Greenberg, *Euclidean and Non-Euclidean Geometries* (1974): a gentler route through neutral geometry and the fifth postulate.
