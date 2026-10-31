# Game Theory

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Games, Decisions and Finance](README.md)
> **Builds on:** [Fixed-Point Theorems](../../07-topology/02-algebraic-topology/fixed-point-theorems.md), [Convex Sets and Separation](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md), [Linear Programming](../02-optimisation/linear-programming.md), [Expectation and Variance](../../03-combinatorics-and-graph-theory/03-discrete-probability/expectation-and-variance.md)
> **Enables:** [Social Choice and Voting](social-choice-and-voting.md), [Mathematics and Society](../../15-mathematics-in-context/mathematics-and-society.md), [Reinforcement Learning (CS)](../../../cs-first-principles/13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md)

## Essence

Game theory studies decisions whose outcome depends on what others decide. A game lists players, their strategies and their payoffs, and the basic question is what rational players will do when each knows the others are also reasoning. Two theorems anchor the subject. John von Neumann's minimax theorem (1928) says that in a two-player zero-sum game, randomising lets each player guarantee the same value, so the game has a well-defined solution. John Nash's theorem (1950) says that every finite game has an equilibrium, a profile of mixed strategies from which no player gains by deviating alone; its proof is a fixed-point theorem. The prisoner's dilemma shows the catch: equilibria need not be good for anyone.

## Core tenets

1. **In a zero-sum game, randomisation closes the gap between max min and min max.** Let player 1 choose a row, player 2 a column, and player 1 receive a_ij from an m × n matrix A. With mixed strategies x and y (probability vectors) the expected payoff is xᵀAy, and von Neumann proved

   ```
   max_x min_y  xᵀAy  =  min_y max_x  xᵀAy        (x, y range over probability simplices)
   ```

   The inequality ≤ always holds: what you can guarantee by moving first cannot exceed what your opponent concedes by moving first. Equality needs mixing. In matching pennies the pure-strategy values are −1 and +1, while the mixed value is 0, reached by each player choosing heads with probability ½.

2. **Minimax is linear programming duality, which is convex separation.** Player 1's problem, maximise v subject to xᵀA ≥ v in every column, is a linear programme, and player 2's problem is exactly its dual. Strong duality, proved by separating a point from a closed convex set with a hyperplane, gives the equality. So zero-sum games are solved in polynomial time, and an optimal strategy is a certificate that anyone can check.

3. **Every finite game has a Nash equilibrium in mixed strategies (Nash, 1950).** Each player's best responses to the others' mixed strategies form a nonempty, convex, closed set that depends upper-semicontinuously on them. The product of simplices is compact and convex, so Kakutani's fixed-point theorem gives a profile that is a best response to itself: an equilibrium. Nash's 1951 paper used Brouwer's theorem instead. Each hypothesis matters: matching pennies has no equilibrium in pure strategies, and "name the larger whole number" has no equilibrium at all, because its strategy set is not compact.

4. **Equilibria can be bad for everyone: the prisoner's dilemma.** Each of two players cooperates or defects, with payoffs T > R > P > S (temptation, reward, punishment, sucker). Whatever the other does, defecting pays more, so defection is a strictly dominant strategy and (defect, defect) is the unique equilibrium. Yet both prefer mutual cooperation, R > P. Individual rationality and collective welfare diverge, which is the shape of arms races, overfishing and price wars.

5. **Repetition can sustain cooperation, but only with an open future.** If the prisoner's dilemma is repeated a known finite number of times, backward induction from the last round gives defection throughout. If it is repeated indefinitely and players value the future enough, the folk theorem shows that any feasible outcome giving each player more than their guaranteed minimum is an equilibrium, enforced by the threat of punishment. Robert Axelrod's computer tournaments, reported in *The Evolution of Cooperation* (1984), found the simple tit-for-tat strategy highly successful.

6. **Existence is not computation.** Nash's proof is non-constructive. Finding an equilibrium of a general game is complete for the class PPAD (Polynomial Parity Arguments on Directed graphs), a result established in 2006 and extended to two-player games: such problems are believed not to be solvable in polynomial time. Zero-sum games, by contrast, are linear programmes. If equilibria are hard to compute, it is unclear why real players would find them.

7. **In evolution, payoffs are fitness and equilibria are stable strategies.** John Maynard Smith and George Price (1973) defined an evolutionarily stable strategy (ESS): one that, if adopted by a population, cannot be invaded by a rare mutant. Every ESS is a Nash equilibrium of the symmetric game, and the replicator dynamics, in which strategies grow in proportion to their payoff, connect game theory with population dynamics. No assumption of rationality is needed: selection does the optimising.

## Key concepts

| Term | Meaning |
|---|---|
| Mixed strategy | A probability distribution over a player's pure strategies |
| Zero-sum game | One player's gain is exactly the other's loss |
| Value | The common max min and min max of a zero-sum game |
| Best response | A strategy maximising payoff given the others' strategies |
| Nash equilibrium | A profile in which every strategy is a best response to the rest |
| Dominant strategy | A strategy that is best whatever the others do |
| Pareto efficient | No outcome makes someone better off and nobody worse off |
| Folk theorem | Cooperative outcomes are equilibria of indefinitely repeated games |

## How it fits

- **Below:** Brouwer and Kakutani fixed points prove existence; separation of convex sets and linear programming duality prove minimax; expectation turns mixed strategies into payoffs.
- **Above:** [mathematics and society](../../15-mathematics-in-context/mathematics-and-society.md) meets game theory in auctions, arms control and climate negotiations.
- **Siblings:** [social choice](social-choice-and-voting.md) asks which rule a group should use, and game theory predicts how voters will game it; [mathematical finance](mathematical-finance.md) replaces the opponent by a market and the equilibrium by no arbitrage.

## Common misconceptions

- **"A Nash equilibrium is the best outcome."** It is only stable against one player deviating; the prisoner's dilemma equilibrium is worse for both players than cooperation.
- **"Game theory assumes people are selfish."** Payoffs can encode any preferences, including altruism; the theory assumes only that players act on them.
- **"Mixed strategies mean playing randomly for no reason."** Randomising is what prevents an opponent from exploiting predictability, and it is the only way to reach the value in many games.

## Go deeper

- J. von Neumann and O. Morgenstern, *Theory of Games and Economic Behavior* (1944): the founding book.
- M. J. Osborne and A. Rubinstein, *A Course in Game Theory* (1994): a rigorous, concise graduate text.
- M. Maschler, E. Solan and S. Zamir, *Game Theory* (2013): a modern textbook with full proofs.
