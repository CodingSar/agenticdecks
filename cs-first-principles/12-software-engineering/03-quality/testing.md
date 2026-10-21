# Testing

> **Layer:** [12 Software Engineering](../README.md) › [Quality](README.md)
> **Builds on:** [Abstraction and interfaces](../01-design/abstraction-and-interfaces.md), [Halting problem and undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), [Combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md)
> **Enables:** [Debugging](debugging.md), [Build and continuous delivery](../04-operations/build-and-continuous-delivery.md), [Development lifecycles](../02-process/development-lifecycles.md)

## Essence

Testing runs a program on chosen inputs and checks the results against an **oracle**, some independent statement of what the right result is. It is the main way software teams gain confidence that code works and keeps working as it changes. Its fundamental limit was stated by Edsger Dijkstra: "Program testing can be used to show the presence of bugs, but never to show their absence" (1969). The input space of even a small function is astronomically large, so a test suite is a sample. The craft of testing is choosing samples that are likely to reveal faults, making them cheap and reliable enough to run on every change, and writing them so that a failure points at its cause.

## Core tenets

1. **Testing samples; it cannot prove.** A function taking two 64-bit integers has 2^128 (about 3 × 10^38) input pairs. Testing all is impossible; testing a few hundred well-chosen ones finds most real bugs, because faults cluster at boundaries (zero, empty, maximum, off-by-one) and at special cases. Partitioning inputs into classes that should behave alike, then testing each class and its edges, is the basic technique.
2. **A test is only as good as its oracle.** The oracle may be a hand-computed expected value, a property that must hold (sorting returns a permutation in order), a reference implementation, or an earlier version's output. Without a reliable oracle, a test only checks that code does not crash. Choosing the oracle is often harder than choosing the input.
3. **The main value of a test suite is regression detection.** Most tests pass most of the time. Their job is to fail when a later change breaks something that used to work, so that engineers can change code without fearing silent breakage. This is what makes refactoring and short [lifecycles](../02-process/development-lifecycles.md) safe.
4. **Tests come at different scales with different trade-offs.** Unit tests check one module in isolation: fast (milliseconds), precise about cause, but blind to integration problems. Integration and end-to-end tests check real interactions: realistic, but slow, flaky and vague about cause. The "test pyramid" (Cohn, 2009) recommends many small tests and few large ones; Google classifies tests by resource use (small, medium, large) for the same reason.
5. **Test doubles trade fidelity for speed and control.** Replacing a database or network service with a fake, stub or mock makes tests fast and deterministic and lets you simulate failures. But a mock encodes your assumptions about the dependency, which may be wrong. Prefer real implementations or faithful fakes where affordable, and test against the contract rather than incidental call sequences.
6. **Flaky tests destroy trust.** A test that sometimes fails without a code change, usually because of timing, ordering, shared state or network calls, teaches engineers to ignore failures. Even a small flake rate is serious at scale: with 1,000 tests each failing 0.1% of the time, about 63% of runs see at least one failure. Determinism (fixed seeds, fake clocks, isolated state) is a design requirement.
7. **Coverage measures what was run, not what was checked.** Line or branch coverage shows code no test executes, which is useful. High coverage does not show that assertions are meaningful. Mutation testing, which injects small faults and checks whether tests catch them, measures the suite's fault-finding power more directly.
8. **Generated inputs find what humans miss.** Property-based testing (QuickCheck, Claessen and Hughes, 2000) states a property and generates hundreds of random inputs, shrinking any failure to a minimal case. Fuzzing (Miller et al., 1990) feeds random or mutated inputs to find crashes; coverage-guided fuzzers such as American Fuzzy Lop (AFL) and libFuzzer have found many thousands of security bugs in widely used software.

## Key concepts

| Term | Meaning |
|---|---|
| Test oracle | The mechanism that decides whether an output is correct |
| Equivalence partitioning | Grouping inputs expected to behave the same and testing one from each group |
| Regression test | A test that guards against a previously working behaviour breaking |
| Unit / integration / end-to-end test | Tests of one module / several cooperating modules / the whole system as a user sees it |
| Test double | A stand-in for a real dependency (fake, stub, mock) |
| Flaky test | A test whose result varies without any code change |
| Code coverage | The fraction of code (lines, branches) executed by a test suite |
| Property-based testing | Testing a stated property over many generated inputs |
| Fuzzing | Automatically generating large numbers of inputs to find crashes or violations |

## How it fits

- **Below:** the impossibility of exhaustive checking follows from [undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) and from the [combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md) of input spaces. Randomised testing borrows from [randomized algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md); contracts from [Hoare logic](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md) make good properties.
- **Above:** [continuous integration](../04-operations/build-and-continuous-delivery.md) runs the suite on every change; [fuzzing](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md) is a main defence against memory-safety vulnerabilities.
- **Siblings:** [static analysis](static-analysis-and-code-review.md) covers all paths for a narrow property, while testing covers a few paths for any property; [debugging](debugging.md) starts from a failing test and ends by adding one.

## Common misconceptions

- **"100% coverage means the code is tested."** Coverage shows execution, not checking. A test with no assertions can reach full coverage.
- **"Mocks make tests better because they isolate."** Over-mocked tests pass while the real integration is broken, and break on harmless refactors. Isolation is a means, not the goal.
- **"Testing is a phase after coding."** Tests written with or before the code (test-driven development) shape testable design and catch errors when they are cheapest to fix.

## Go deeper

- Glenford J. Myers, *The Art of Software Testing* (1979; later editions with Badgett and Sandler): the classic on test-case design.
- Titus Winters, Tom Manshreck and Hyrum Wright, *Software Engineering at Google* (2020): chapters on unit testing, test doubles and large tests.
- Koen Claessen and John Hughes, "QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs" (ICFP 2000): property-based testing.
