# Static Analysis and Code Review

> **Layer:** [12 Software Engineering](../README.md) › [Quality](README.md)
> **Builds on:** [Type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md), [Semantic analysis](../../06-programming-languages/03-compilers/semantic-analysis.md), [Halting problem and undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), [Version control](../02-process/version-control.md)
> **Enables:** [Build and continuous delivery](../04-operations/build-and-continuous-delivery.md), [Memory-safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md)

## Essence

Static analysis and code review both examine code without running it. Static analysis does it by machine: type checkers, linters, data-flow analysers and verifiers reason about all possible executions of a program at once, for a narrow set of properties. Code review does it by people: a second engineer reads each change before it is merged, judging correctness, design, clarity and fit. Each covers the other's blind spots. A machine never tires and checks every path, but only for what it was built to check and with false alarms. A reviewer understands intent and design, but misses details and tires quickly. Both are cheapest when they run on every change, before the code ships.

## Core tenets

1. **Perfect static analysis is impossible.** By Rice's theorem, every non-trivial semantic property of programs is [undecidable](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md). So every analyser must give up one of soundness (never missing a real bug), completeness (never raising a false alarm) or termination. Type checkers and verifiers lean sound; bug-finding tools lean toward few false positives and accept missed bugs.
2. **Abstraction makes analysis tractable.** Abstract interpretation (Cousot and Cousot, 1977) runs the program over simplified values, such as "positive, zero or negative" or "null or non-null" instead of exact numbers, so that loops reach a fixed point in finite time. The result over-approximates every real execution: if the abstract run shows no error, no real run has one, at the cost of some false alarms.
3. **Types are the most successful static analysis.** A [type system](../../06-programming-languages/02-semantics-and-types/type-systems.md) is a sound, fast, compositional analysis that every programmer runs on every build. Moving checks into types (non-null references, ownership in Rust, units of measure) eliminates whole bug classes for all future code, which is why memory-safe languages are the strongest defence against [memory-safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md).
4. **False positives decide whether a tool is used.** Engineers ignore tools that cry wolf. Experience at Coverity (Bessey et al., "A Few Billion Lines of Code Later", 2010) and Google (Sadowski et al., "Lessons from Building Static Analysis Tools at Google", 2018) shows that checks must have low false-positive rates, give actionable fixes, and appear at the right moment, ideally during code review, or they will be disabled.
5. **Code review's main benefit is shared understanding, not bug-catching.** Bacchelli and Bird ("Expectations, Outcomes, and Challenges of Modern Code Review", 2013) found at Microsoft that developers expected review to find defects, but most comments were about code improvements, understanding and knowledge transfer. Review spreads knowledge of the codebase, keeps style and design consistent, and ensures at least two people understand each change.
6. **Small changes get better reviews.** A reviewer reading a 50-line change can understand it; one reading 2,000 lines skims. Studies of inspection, from Fagan's formal inspections at International Business Machines (IBM) (1976) onward, find that defect detection falls as review size and speed rise. Small, frequent changes enabled by [version control](../02-process/version-control.md) make effective review possible.
7. **Automate what can be automated, so people review what only people can.** Formatting, style rules and known bug patterns should be enforced by tools before a human looks. Reviewers then spend attention on design, naming, missing cases, test adequacy and whether the change should exist at all.

## Key concepts

| Term | Meaning |
|---|---|
| Static analysis | Reasoning about a program's possible behaviours without executing it |
| Soundness | The analysis never misses a real violation of the property it checks |
| Completeness | The analysis never reports a violation that cannot occur |
| False positive | A reported problem that is not real |
| Abstract interpretation | Executing a program over an abstract domain to over-approximate all behaviours |
| Linter | A tool that flags suspicious or non-conforming code patterns; named after Johnson's `lint` for C (1978) |
| Data-flow analysis | Computing facts about values along all control-flow paths (for example, possibly-null variables) |
| Code review | Examination of a change by other engineers before it is merged |

## How it fits

- **Below:** static analysis reuses compiler machinery: parsing, [semantic analysis](../../06-programming-languages/03-compilers/semantic-analysis.md), [intermediate representations](../../06-programming-languages/03-compilers/intermediate-representations.md) and the data-flow analyses of [optimization](../../06-programming-languages/03-compilers/optimization.md). At the strong end it merges with [model checking](../../06-programming-languages/05-formal-methods/model-checking.md) and [program proofs](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md). Its limit is [undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md).
- **Above:** both run as gates in [continuous integration](../04-operations/build-and-continuous-delivery.md); security teams use static analysis to find injection and memory bugs ([web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md)).
- **Siblings:** [testing](testing.md) checks real behaviour on a few inputs; static analysis checks all inputs for narrow properties; review checks intent and design. [Debugging](debugging.md) often ends by writing a new static check so the bug class cannot recur.

## Common misconceptions

- **"A clean static-analysis report means the code is correct."** Bug-finding tools are deliberately unsound; they check specific patterns. A clean report means those patterns are absent.
- **"Review is for catching bugs, so if tests pass it adds nothing."** Review's larger value is design quality and shared knowledge, which tests do not measure.
- **"More rules make better code."** Rules that produce noise train people to ignore warnings, including the important ones.

## Go deeper

- Patrick Cousot and Radhia Cousot, "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs" (POPL 1977): the theory behind sound analysers.
- Al Bessey et al., "A Few Billion Lines of Code Later: Using Static Analysis to Find Bugs in the Real World", *Communications of the ACM* (2010): what happens when analysis meets real users.
- Alberto Bacchelli and Christian Bird, "Expectations, Outcomes, and Challenges of Modern Code Review" (ICSE 2013): what review actually achieves.
