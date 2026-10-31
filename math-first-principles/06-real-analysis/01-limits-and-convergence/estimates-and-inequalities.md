# Estimates and Inequalities

> **Layer:** [06 Real Analysis](../README.md) › [Limits and Convergence](README.md)
> **Builds on:** [The real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md), [Sequences and limits](sequences-and-limits.md), [Inner products and orthogonality](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md)
> **Enables:** [Uniform convergence](uniform-convergence.md), [Lp spaces](../../09-advanced-analysis/01-measure-and-integration/lp-spaces.md), [Concentration inequalities](../../11-probability-and-statistics/02-limit-theorems/concentration-inequalities.md), [Floating point, conditioning and stability](../../14-applied-and-computational-mathematics/01-numerical-analysis/floating-point-conditioning-and-stability.md), [Asymptotic analysis](../../../cs-first-principles/02-theory-of-computation/04-complexity/asymptotic-analysis.md)

## Essence

Analysis proves that things are equal, or that limits exist, by proving inequalities. To show aₙ → L you rarely compute aₙ − L; you bound it. A handful of inequalities do almost all the work, and each has a one-line reason. The triangle inequality says that detours never shorten a trip; the arithmetic mean–geometric mean (AM–GM) and Cauchy–Schwarz inequalities say that a square is never negative; Jensen's and Hölder's inequalities say that a convex graph lies above its tangent lines. The working habit is to split an error into pieces, give each piece a share of ε, and record the size of what remains with O and o notation.

## Core tenets

1. **Triangle inequality: |x + y| ≤ |x| + |y|.** For real numbers, add −|x| ≤ x ≤ |x| and −|y| ≤ y ≤ |y|. In ℝⁿ, with the Euclidean norm ∥x∥ = √⟨x, x⟩, expand ∥x + y∥² = ∥x∥² + 2⟨x, y⟩ + ∥y∥² and bound the middle term by Cauchy–Schwarz. Applied to x − y and y, it gives the reverse form | |x| − |y| | ≤ |x − y|, so the absolute value never stretches distances. As d(x, z) ≤ d(x, y) + d(y, z) it is the axiom that makes a distance usable in proofs.

2. **AM–GM: √(ab) ≤ (a + b)/2 for a, b ≥ 0, with equality only when a = b.** The reason is (√a − √b)² ≥ 0, expanded. The n-term version, (a₁a₂⋯aₙ)^(1/n) ≤ (a₁ + ⋯ + aₙ)/n, follows from Jensen's inequality applied to log (tenet 4). It solves optimisation problems without calculus: a rectangle with sides x, y and perimeter 4s has area xy ≤ ((x + y)/2)² = s², with equality only for the square.

3. **Cauchy–Schwarz: |⟨x, y⟩| ≤ ∥x∥·∥y∥.** For real t the quadratic ∥x + ty∥² = ∥x∥² + 2t⟨x, y⟩ + t²∥y∥² is never negative, so its discriminant 4⟨x, y⟩² − 4∥x∥²∥y∥² is at most 0. Equality holds exactly when x and y are parallel. In coordinates, (∑aᵢbᵢ)² ≤ (∑aᵢ²)(∑bᵢ²); for functions, (∫fg)² ≤ ∫f² · ∫g². It puts ⟨x, y⟩/(∥x∥∥y∥) in [−1, 1], which is what lets angles be defined in any inner product space.

4. **Jensen: for convex φ, φ of an average is at most the average of φ.** A convex function lies above a supporting line at each point. Take the line at the weighted mean m = ∑tᵢxᵢ, with weights tᵢ ≥ 0 summing to 1: φ(x) ≥ φ(m) + c(x − m) for some slope c. Average this over the xᵢ with the same weights; the linear term averages to 0, leaving ∑tᵢφ(xᵢ) ≥ φ(m). With φ = −log it gives weighted AM–GM. In probability it reads φ(E X) ≤ E φ(X), where E is expectation, so (E X)² ≤ E X².

5. **Hölder: ∑|aᵢbᵢ| ≤ (∑|aᵢ|ᵖ)^(1/p) · (∑|bᵢ|^q)^(1/q) when p, q > 1 and 1/p + 1/q = 1.** First prove Young's inequality, ab ≤ aᵖ/p + b^q/q for a, b ≥ 0: it is weighted AM–GM, from the concavity of log, applied to aᵖ and b^q with weights 1/p and 1/q. Then rescale the sequences so that both factors on the right equal 1, apply Young term by term and add: the total is at most 1/p + 1/q = 1. With p = q = 2, Hölder is Cauchy–Schwarz. Hölder gives Minkowski's inequality, the triangle inequality for the p-norms.

6. **The ε/3 habit: split the error, then spend ε in pieces.** To bound |a − c|, insert a well-chosen intermediate b and use |a − c| ≤ |a − b| + |b − c|. Each piece is controlled by a different hypothesis, and each receives its share of ε. The standard example is that [a uniform limit of continuous functions is continuous](uniform-convergence.md): one error splits into two "uniformly close" terms and one "a single continuous function" term, each below ε/3. The shares need not be exact: a bound of 5ε is as good as ε, since ε is arbitrary.

7. **O and o notation record the size of what is left.** As x → a, f = O(g) means |f(x)| ≤ C|g(x)| for some constant C and all x near a; f = o(g) means f(x)/g(x) → 0. So sin x = x + O(x³) as x → 0, and log n = o(n^c) as n → ∞ for every c > 0. Differentiability is exactly f(a + h) = f(a) + f′(a)h + o(h). The notation lets errors be combined without tracking constants: O(h)·O(h) = O(h²) and o(h) + o(h) = o(h).

## Key concepts

| Term | Meaning |
|---|---|
| Norm | A length ∥x∥ with ∥x∥ = 0 only for x = 0, ∥cx∥ = ∣c∣·∥x∥, and the triangle inequality |
| Convex function | φ(tx + (1 − t)y) ≤ tφ(x) + (1 − t)φ(y) for t ∈ [0, 1]: chords lie above the graph |
| Supporting line | A line through a point of the graph of a convex function that lies below the whole graph |
| Conjugate exponents | p, q > 1 with 1/p + 1/q = 1 |
| Young's inequality | ab ≤ aᵖ/p + b^q/q for a, b ≥ 0 and conjugate exponents p, q |
| Big O | f = O(g): ∣f∣ ≤ C∣g∣ near the limit point, for some constant C |
| Little o | f = o(g): f/g → 0 at the limit point |
| Equality case | When an inequality is sharp; it usually identifies the optimiser |

## How it fits

- **Below:** The order and absolute value of [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md); Cauchy–Schwarz belongs to [inner product spaces](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md); the limits of [sequences and limits](sequences-and-limits.md) give o its meaning.
- **Above:** Hölder and Minkowski make the [Lᵖ spaces](../../09-advanced-analysis/01-measure-and-integration/lp-spaces.md) normed spaces. Jensen and its relatives grow into [concentration inequalities](../../11-probability-and-statistics/02-limit-theorems/concentration-inequalities.md). Numerical [error analysis](../../14-applied-and-computational-mathematics/01-numerical-analysis/floating-point-conditioning-and-stability.md) is bookkeeping with O, and computer science uses the same O for [running times](../../../cs-first-principles/02-theory-of-computation/04-complexity/asymptotic-analysis.md).
- **Siblings:** Every proof in [sequences and limits](sequences-and-limits.md), [series](series.md), [continuity](continuity.md) and [uniform convergence](uniform-convergence.md) applies these tools. [Metric spaces](../04-metric-spaces/metric-spaces-and-continuity.md) take the triangle inequality as an axiom.

## Common misconceptions

- **"Inequalities are weaker cousins of identities."** In analysis the inequality is usually the theorem: convergence, continuity and existence are all claims that something is small.
- **"f = O(g) means f grows like g."** It is only an upper bound: x = O(x²) as x → ∞. The sign "=" is one-way here, and the two-sided statement is written f = Θ(g).
- **"Cauchy–Schwarz is about coordinates."** Its proof uses only bilinearity and ⟨x, x⟩ ≥ 0, so it holds for integrals and for random variables, where it says that a covariance is at most the product of the standard deviations.

## Go deeper

- G. H. Hardy, J. E. Littlewood and G. Pólya, *Inequalities* (1934): the classic.
- J. Michael Steele, *The Cauchy–Schwarz Master Class* (2004): a problem-driven modern course in the art of bounding.
- Ronald L. Graham, Donald E. Knuth and Oren Patashnik, *Concrete Mathematics* (2nd edition, 1994): its chapter on asymptotics teaches O notation by use.
