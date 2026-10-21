# Quality

> **Layer:** [12 Software Engineering](../README.md) › Quality
> **Children:** [Testing](testing.md) · [Debugging](debugging.md) · [Static analysis and code review](static-analysis-and-code-review.md)

## What this area is about

Quality engineering asks: **how do we gain justified confidence that software does what it should, and find out quickly when it does not?** Proof of correctness is possible for small, critical parts, but for most code it is too expensive, and for arbitrary programs it is impossible in general: by [Rice's theorem](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), no algorithm can decide a non-trivial property of program behaviour for all programs. So quality comes from layering several imperfect checks, each catching a different kind of fault at a different cost.

The unifying idea is **defence in depth against defects**. Static analysis and type checking examine code without running it and catch whole classes of errors cheaply. Code review brings human judgement about design and intent. Testing runs the code on chosen inputs and compares results with expectations. Debugging is what happens when a defect gets through: a systematic search from symptom back to cause. Each layer misses things the others catch, and the earlier a defect is caught, the cheaper it is.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Static analysis and code review](static-analysis-and-code-review.md) | Find defects by examining code without running it, by machine and by people | [Type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md), [version control](../02-process/version-control.md) |
| [Testing](testing.md) | Find defects by running code on selected inputs against an oracle | [Interfaces](../01-design/abstraction-and-interfaces.md) as contracts, [requirements](../02-process/requirements.md) as oracles |
| [Debugging](debugging.md) | Locate and fix the cause of an observed failure | Testing (reproduction), version control (history) |

```
   write code --> static checks --> review --> tests (unit, integration, end-to-end) --> ship
                  (cheapest, broad)  (judgement)  (behaviour on samples)
                                                                     failure observed
                                                                            |
                                     debugging: reproduce -> isolate -> fix -> add regression test
```

The children form a pipeline and a loop. Static checks run first because they are fast and need no test inputs. Review catches what tools cannot: wrong design, unclear naming, missing cases. Tests exercise behaviour; they check only the inputs they try, but they check the real thing. When a failure gets through, debugging finds its cause, and the fix ends with a new test so the same defect cannot quietly return. Read [testing](testing.md) first, since both other files refer to its ideas of oracles and regression tests.

## Connections to sibling areas

- **[Design](../01-design/README.md):** testability is a design property. Modules with narrow interfaces and injected dependencies can be tested alone; hidden global state makes tests slow and flaky.
- **[Process](../02-process/README.md):** review runs on version-control diffs; [requirements](../02-process/requirements.md) define the oracle that tests check against; short [lifecycles](../02-process/development-lifecycles.md) are only safe with automated tests.
- **[Operations](../04-operations/README.md):** [continuous integration](../04-operations/build-and-continuous-delivery.md) runs the quality pipeline on every change; canary releases and [observability](../04-operations/observability.md) are testing in production, catching what pre-release tests missed.

## Connections across layers

The limits of this area come from [computability](../../02-theory-of-computation/03-computability/README.md): testing samples an infinite input space, and sound static analysis must over-approximate. Its strongest tools come from [programming languages](../../06-programming-languages/README.md): [type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md), [model checking](../../06-programming-languages/05-formal-methods/model-checking.md) and [proof assistants](../../06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md). [Security](../../11-security-and-cryptography/README.md) depends on it, since many vulnerabilities, such as [memory-safety bugs](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md), are found by fuzzing and static analysis. [Machine-learning evaluation](../../13-artificial-intelligence/02-machine-learning-foundations/evaluation-and-experimentation.md) is testing for components whose specification is a dataset.

## Cross-cutting threads

- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): each check reduces what must be trusted; none removes the need for the others.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): Rice's theorem forces every analysis to be unsound, incomplete or non-terminating.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): assertions and contracts state what must hold; tests and analysers check it.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): several independent checks catch more than one perfect-seeming check.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): false positives against false negatives, test speed against fidelity.
