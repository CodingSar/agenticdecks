# Social Choice and Voting

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Games, Decisions and Finance](README.md)
> **Builds on:** [Relations and Orders](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md), [Finite Probability Spaces](../../03-combinatorics-and-graph-theory/03-discrete-probability/finite-probability-spaces.md), [Game Theory](game-theory.md)
> **Enables:** [Mathematics and Society](../../15-mathematics-in-context/mathematics-and-society.md), [Philosophy of Mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md)

## Essence

Social choice theory asks how individual preferences should be combined into a collective decision. Each voter ranks the alternatives, and a rule must turn the list of rankings into a social ranking or a winner. With two alternatives, majority rule is ideal, and May's theorem says it is the only rule with the obvious fairness properties. With three or more, everything goes wrong. Majorities can cycle (Condorcet's paradox), Arrow's theorem (1951) shows that no ranking rule meets a short list of reasonable conditions except dictatorship, and the Gibbard–Satterthwaite theorem shows that every non-dictatorial rule electing one of at least three candidates rewards some voter for lying. The theorems do not say voting is futile; they say every rule must give something up, and they say exactly what.

## Core tenets

1. **Majority preference can be cyclic (Condorcet, 1785).** Three voters ranking A > B > C, B > C > A and C > A > B produce majorities A over B, B over C and C over A, each by two votes to one. Individual rankings are transitive; the majority relation need not be. With three candidates and many voters whose rankings are independent and uniform, a cycle occurs with probability about 9%. A Condorcet winner, one beating every rival head to head, may therefore not exist.

2. **With two alternatives, majority rule is characterised by fairness (May, 1952).** A rule deciding between two options for any profile of votes is anonymous (voters are treated alike), neutral (options are treated alike) and positively responsive (extra support for the winner, or for a tied option, makes it the sole winner) if and only if it is simple majority. Proof idea: anonymity means only the vote counts matter, neutrality makes the rule symmetric in the two counts, and positive responsiveness forces the cut-off to be exactly at a tie.

3. **Arrow's theorem: with at least three alternatives, no rule except a dictatorship satisfies unrestricted domain, Pareto and independence of irrelevant alternatives (IIA).** The rule must take any profile of rankings from finitely many voters to a transitive social ranking; Pareto requires that if everyone prefers x to y, so does society; IIA requires that society's ranking of x and y depend only on individual rankings of x and y. Call a group decisive for a pair if society follows it whenever all its members agree. Pareto makes the whole electorate decisive. Using a third alternative and IIA, one shows a group decisive for one pair is decisive for every pair, and that if a decisive group is split in two, one part is decisive. Halving a finite electorate ends with a single decisive voter: a dictator.

4. **The decisive groups form an ultrafilter, and the finiteness of the electorate is essential.** The argument shows that decisive groups are closed under supersets and intersections, and of any group or its complement one is decisive: that is an ultrafilter on the set of voters. On a finite set every ultrafilter consists of the sets containing one fixed element, the dictator. With infinitely many voters a non-principal ultrafilter gives a rule satisfying all of Arrow's conditions without a dictator, though such ultrafilters exist only by the axiom of choice and cannot be written down.

5. **Each other hypothesis can be dropped, at a price.** With two alternatives, majority rule satisfies all the conditions. The Borda count, which scores 2, 1, 0 for first, second and third place, violates IIA: removing a losing candidate can change the order of the others. If preferences are single-peaked along one axis, such as left to right (Duncan Black, 1948), the majority relation is transitive and the median voter's peak wins. A rule that ignores voters and imposes a fixed ranking escapes by violating Pareto.

6. **Every reasonable single-winner rule can be manipulated (Gibbard, 1973; Satterthwaite, 1975).** Suppose a rule picks one winner from any profile, every one of at least three candidates can win, and no voter can ever gain by misreporting their ranking. Then the rule is a dictatorship. The proof reduces to Arrow's theorem: strategy-proofness forces an IIA-like monotonicity on the induced ranking. Escapes mirror Arrow's: random rules, restricted domains such as single-peaked preferences (where the median rule is strategy-proof), and rules for which computing a profitable lie is computationally hard.

7. **The theorems are design constraints, not counsel of despair.** Plurality voting, run-off systems, ranked choice, Borda and approval voting each violate some axiom, and the theory identifies which. Choosing a voting system is choosing which failure to tolerate, informed by how often each occurs in realistic electorates.

## Key concepts

| Term | Meaning |
|---|---|
| Profile | A list of the voters' rankings of the alternatives |
| Social welfare function | A rule from profiles to a social ranking |
| Condorcet winner | An alternative beating every other in pairwise majority votes |
| Pareto condition | Unanimous preference for x over y makes society prefer x over y |
| Independence of irrelevant alternatives | The social ranking of x and y depends only on individual rankings of x and y |
| Dictator | A voter whose strict preferences always become society's |
| Single-peaked preferences | Rankings that fall away on both sides of each voter's favourite along a fixed axis |
| Strategy-proof | No voter can ever gain by reporting a false ranking |

## How it fits

- **Below:** preferences are total orders, so the subject is combinatorics of [relations and orders](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md); probabilities of paradoxes come from finite probability; the ultrafilter view uses the axiom of choice.
- **Above:** [mathematics and society](../../15-mathematics-in-context/mathematics-and-society.md) discusses electoral reform and districting, where these limits bind in practice.
- **Siblings:** [game theory](game-theory.md) supplies the strategic view behind Gibbard–Satterthwaite; [mathematical finance](mathematical-finance.md) aggregates beliefs through prices rather than votes.

## Common misconceptions

- **"Arrow proved that democracy is impossible."** He proved that no ranking rule meets all his conditions at once; majority rule on two options, or on single-peaked preferences, works well.
- **"Ranked-choice voting avoids the paradoxes."** It violates monotonicity and IIA, and it can fail to elect a Condorcet winner.
- **"If everyone votes sincerely, the problem disappears."** Condorcet cycles and Arrow's theorem concern sincere preferences; manipulation is a further problem.

## Go deeper

- K. J. Arrow, *Social Choice and Individual Values* (1951; 2nd ed. 1963): the original theorem and its framing.
- A. K. Sen, *Collective Choice and Social Welfare* (1970): the classic broader treatment, including Sen's own impossibility result.
- A. D. Taylor, *Social Choice and the Mathematics of Manipulation* (2005): a clear account of the manipulation theorems.
