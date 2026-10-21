# Writer brief

You are writing part of a first-principles knowledge base of Computer Science (CS). Read [`PLAN.md`](PLAN.md) (why the tree has this shape) and [`TAXONOMY.md`](TAXONOMY.md) (every path that exists) first.

## The reader

A capable engineer who wants the *essence* of each topic: what is true, why it is true, and how it connects to everything else. They can follow mathematics and code but should never need a textbook open to follow a file.

## Rules for every file

1. **Create exactly the paths in `TAXONOMY.md`.** Do not add, rename or skip files. If you think the taxonomy is wrong, write the file anyway and add your suggestion to your final report.
2. **Abbreviations:** spell out each abbreviation on its first use *in each file*, then use the short form: "Translation Lookaside Buffer (TLB)", then "TLB". Every file may be the first one a reader opens. This includes common ones (Central Processing Unit (CPU), Operating System (OS)) in the first file where they appear in body text. Do not expand abbreviations inside headings.
3. **Links are relative** and point only to paths in `TAXONOMY.md` (or `README.md` of a directory listed there, or `../CROSS-CUTTING.md` style paths to the root files). Check the number of `../` carefully: a leaf at `07-operating-systems/03-concurrency/deadlock.md` links to `../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md`.
4. **Mechanism over vocabulary.** Every tenet explains *why* or *what force* produces it. "Caches exploit locality" is a label; "Programs reuse recently touched data and touch nearby addresses, so keeping a small fast copy of recent neighbourhoods serves most accesses at small-memory speed" is a tenet.
5. **Accuracy is non-negotiable.** Use well-established facts. Give numbers with their order of magnitude and context ("~100 ns DRAM access, ~1 ns L1 hit, circa 2020s hardware"). No invented citations: cite only real, canonical works you are sure of (author, title, year).
6. **Plain, direct English.** Short sentences. Active voice. No filler ("It is important to note that…"), no marketing tone. Use a small example, equation or code fragment when it makes a tenet concrete. Use Markdown tables where they compare things.
7. **Length.** Leaves: 500–1,100 words. Parent READMEs: 400–900 words. Layer READMEs (top-level `NN-*/README.md`): 600–1,200 words. Be dense, not long.
8. **No front matter, no emoji, no HTML.** ASCII diagrams in fenced code blocks are welcome when they show structure (a pipeline, a protocol stack, a state machine).

## Leaf template

```markdown
# <Title>

> **Layer:** [NN Layer name](<relative path to layer README>) › [Parent name](README.md)
> **Builds on:** [Topic](<rel path>), [Topic](<rel path>)
> **Enables:** [Topic](<rel path>), [Topic](<rel path>)

## Essence

One paragraph (3–6 sentences): what this is, the problem it solves, and the single idea that makes it work. A reader who reads only this paragraph should come away with the right mental model.

## Core tenets

1. **<Tenet stated as a claim.>** Two to four sentences of mechanism: why it is true, what follows from it.
2. ...
(5–9 tenets. These are the heart of the file: the load-bearing ideas without which the topic is misunderstood.)

## Key concepts

| Term | Meaning |
|---|---|
| ... | ... |

(5–12 terms that the tenets rely on. Precise one-line definitions.)

## How it fits

- **Below:** what this topic takes from the layers beneath, and which assumption it relies on.
- **Above:** what higher layers build with it.
- **Siblings:** how it contrasts with or complements the other leaves in the same parent.

## Common misconceptions

- **"<Misconception>"**: why it is wrong, in one or two sentences.
(2–4 items.)

## Go deeper

- Author, *Title* (year): one phrase on why it is the right next read.
(2–4 canonical sources.)
```

"Builds on" and "Enables" each list 1–5 links to other leaves or READMEs, *anywhere* in the tree (cross-layer links are the point). At least one of them should cross a layer boundary.

## Parent README template (directories below the top level)

```markdown
# <Name>

> **Layer:** [NN Layer name](<rel path>) › <this node>
> **Children:** [Child](child.md) · [Child](child.md) · ...

## What this area is about

The question this area answers and the one idea that unifies its children (1–2 paragraphs).

## How the children fit together

Explain the internal logic: the order to read them, which child depends on which, and how together they make up the parent. A table (Child | Its role in the whole | Depends on) followed by a short narrative works well. An ASCII diagram is welcome if it shows real structure.

## Connections to sibling areas

For each sibling directory under the same layer: one short paragraph or bullet on how this area and that sibling connect (shared ideas, data flowing between them, tension between them). Link to the sibling's README.

## Connections across layers

What this area takes from lower layers and gives to higher ones, with links.

## Cross-cutting threads

Bullets linking to `CROSS-CUTTING.md` anchors (see list below) for the principles visible here, each with one phrase on how it shows up.
```

## Layer README template (`NN-*/README.md`)

Same as the parent template, plus, before "How the children fit together":

```markdown
## Why this layer sits here

What it needs from the layers below (with links) and what the layers above need from it. State the one abstraction or interface this layer contributes to the stack.
```

and the "Connections to sibling areas" section becomes **"Connections to neighbouring layers"**: how this layer connects to each other top-level layer it touches meaningfully (not all 15; the 4–8 that matter), with links to their READMEs.

## Cross-cutting principle anchors

`CROSS-CUTTING.md` will be written last, with these anchors. Link to them as `<rel path>/CROSS-CUTTING.md#<anchor>`:

| Anchor | Principle |
|---|---|
| `abstraction-and-layering` | Hide detail behind an interface; build layers that each use only the one below |
| `interface-vs-implementation` | Separate what something promises from how it does it |
| `indirection-and-naming` | Refer to things by names resolved later (pointers, DNS, virtual memory, vtables) |
| `caching-and-locality` | Keep a small fast copy of what is likely to be used soon |
| `pipelining-and-parallelism` | Overlap independent work in time or space |
| `batching-and-amortization` | Pay a fixed cost once for many operations |
| `redundancy-and-fault-tolerance` | Use extra copies or extra bits to survive failures |
| `the-end-to-end-argument` | Put a function where it can be done completely and correctly |
| `tradeoffs` | Time vs space, latency vs throughput, consistency vs availability, generality vs speed |
| `invariants-and-correctness` | State what must always hold, and keep it holding |
| `recursion-and-self-reference` | Define things in terms of smaller instances; programs that talk about programs |
| `virtualization` | Make one resource look like many, or many look like one |
| `state-and-time` | Who changed what, in what order: the root of concurrency and distribution problems |
| `encoding-and-representation` | Choosing how to represent information decides what is cheap |
| `limits-and-impossibility` | Physical, computational and information-theoretic bounds that no cleverness escapes |
| `feedback-and-control` | Measure the output and adjust the input (congestion control, autoscaling, training) |
| `composition` | Build big things from small things whose properties combine predictably |
| `trust-and-verification` | Decide what you rely on and check what you can |

## Your final report (to the coordinator)

When done, report: files written (count), any taxonomy suggestions, any link you were unsure about, and any claim you were not fully sure of so the reviewer can check it. Do not paste the files.
