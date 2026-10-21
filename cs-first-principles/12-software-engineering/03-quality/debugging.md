# Debugging

> **Layer:** [12 Software Engineering](../README.md) › [Quality](README.md)
> **Builds on:** [Testing](testing.md), [Version control](../02-process/version-control.md), [Searching and selection](../../05-algorithms-and-data-structures/04-sorting-and-searching/searching-and-selection.md), [Statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md)
> **Enables:** [Observability](../04-operations/observability.md), [Reliability engineering](../04-operations/reliability-engineering.md)

## Essence

Debugging is finding the cause of an observed failure and removing it. The difficulty is that cause and symptom are separated in space and time: a wrong value written in one function may surface as a crash far away, much later. Andreas Zeller (*Why Programs Fail*, 2005) describes a chain: a **defect** in the code, when executed, creates an **infection** (a wrong program state), which propagates until it becomes a **failure** visible to the user. Debugging works backwards along that chain. Done well, it is the scientific method applied to a program: observe, form a hypothesis about the cause, design an experiment that could refute it, and narrow the search until one cause remains.

## Core tenets

1. **First make the failure reproducible.** A failure you can trigger on demand can be studied, bisected and verified as fixed; one you cannot is guesswork. Reproduction means capturing the inputs, configuration, environment and, for concurrency bugs, the interleaving. Shrinking the reproduction to a minimal case often reveals the cause directly.
2. **Debugging is search, so halve the space.** Every efficient technique is binary search over something. Over history: `git bisect` finds the commit that introduced a regression in about log2(n) builds (10 tests for 1,000 commits). Over input: delta debugging (Zeller and Hildebrandt, 2002) automatically shrinks a failing input to a minimal one. Over code: checking state halfway along the path tells you which half holds the infection.
3. **Use hypotheses and experiments, not random edits.** Write down what you believe, predict what an experiment will show, and run it. A wrong prediction is information. Changing code at random until the symptom disappears often hides the defect rather than removing it, and leaves no understanding behind.
4. **Question your assumptions; the bug is where you are not looking.** Most long debugging sessions end at something "known" to be true that was not: a library behaving differently than documented, a stale build, a configuration not loaded. Brian Kernighan's warning applies: "Everyone knows that debugging is twice as hard as writing a program in the first place" (*The Elements of Programming Style*, Kernighan and Plauger), so code written at the edge of your cleverness is code you cannot debug.
5. **Observation changes the system.** Adding print statements or running under a debugger changes timing and memory layout, so race conditions and memory-corruption bugs ("heisenbugs") may vanish when observed. Tools that record execution and replay it deterministically (such as the rr debugger), sanitizers that check memory and races at run time, and logs written in advance avoid this.
6. **Make failures loud and early.** The further an infection travels before it becomes visible, the harder the search. Assertions on invariants, input validation at boundaries, and failing fast instead of continuing with bad state shorten the chain from defect to failure. Memory-safe languages remove a whole category of long-distance infections.
7. **Production debugging relies on what was recorded beforehand.** You cannot attach a debugger to a fleet of servers mid-incident. Logs, metrics, traces and core dumps captured in advance are the only evidence. This is why [observability](../04-operations/observability.md) is designed in: it decides which questions you can answer later.
8. **Finish by preventing recurrence.** A fix is complete when a regression test fails without it and passes with it, and when you have asked why the defect was possible and whether siblings exist elsewhere. For serious incidents this becomes a blameless postmortem.

## Key concepts

| Term | Meaning |
|---|---|
| Defect (fault, bug) | An error in the code |
| Infection | An incorrect program state caused by executing a defect |
| Failure | Externally visible incorrect behaviour |
| Minimal reproduction | The smallest input and setup that still triggers the failure |
| Bisection | Binary search over versions, inputs or code locations to isolate a cause |
| Delta debugging | An algorithm that systematically reduces a failing input or change set to a minimal one |
| Heisenbug | A bug that changes or disappears when you try to observe it |
| Sanitizer | Compiler-inserted run-time checks for memory errors, undefined behaviour or data races |

## How it fits

- **Below:** bisection is [binary search](../../05-algorithms-and-data-structures/04-sorting-and-searching/searching-and-selection.md); forming and testing hypotheses is [statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md) made informal. Many hard bugs come from lower layers: [race conditions](../../07-operating-systems/03-concurrency/race-conditions-and-critical-sections.md), [memory-model](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md) surprises, [floating-point](../../03-digital-logic/01-number-representation/floating-point.md) rounding and [memory corruption](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md).
- **Above:** in production, debugging becomes incident response in [reliability engineering](../04-operations/reliability-engineering.md), using data from [observability](../04-operations/observability.md).
- **Siblings:** [testing](testing.md) supplies the reproducing case and the regression test; [version control](../02-process/version-control.md) supplies the history to bisect; [static analysis](static-analysis-and-code-review.md) can find the same defect pattern elsewhere.

## Common misconceptions

- **"The fix is done when the symptom goes away."** A symptom can disappear because timing changed or the input changed. Without understanding the cause and a regression test, the defect is likely still there.
- **"Debugging is an innate talent."** It is a learnable method: reproduce, bisect, hypothesise, test. Experienced debuggers mostly apply it more consistently.
- **"Debuggers are the main tool."** Interactive debuggers help for local, deterministic bugs. For distributed, concurrent or production failures, logs, traces and recorded executions matter more.

## Go deeper

- Andreas Zeller, *Why Programs Fail: A Guide to Systematic Debugging* (2005; 2nd ed. 2009): the infection chain, scientific debugging and delta debugging.
- David J. Agans, *Debugging: The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems* (2002): a short, practical method.
- Brian W. Kernighan and Rob Pike, *The Practice of Programming* (1999): chapter on debugging technique.
