# Version Control

> **Layer:** [12 Software Engineering](../README.md) › [Process](README.md)
> **Builds on:** [Hash functions and MACs](../../11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md), [Graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md), [Eventual consistency and CRDTs](../../10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md)
> **Enables:** [Build and continuous delivery](../04-operations/build-and-continuous-delivery.md), [Static analysis and code review](../03-quality/static-analysis-and-code-review.md), [Debugging](../03-quality/debugging.md)

## Essence

A version control system (VCS) records every change to a set of files, who made it, when and why, and lets many people change the same files in parallel and combine their work. It turns a codebase from a mutable thing into a history of immutable snapshots, so any past state can be recovered, compared or rebuilt. Modern distributed systems such as Git (Torvalds, 2005) store that history as a directed acyclic graph (DAG) of commits, each named by a cryptographic hash of its content. Parallel work becomes branches in the graph, and combining work becomes a merge, a node with two parents. Every other engineering practice (review, continuous integration, release, bisecting a bug) is built on this history.

## Core tenets

1. **History makes change safe.** If every past state is recoverable, a bad change is cheap to undo and an experiment costs nothing. This lowers the fear of change, which is what allows small, frequent commits. The commit message records *why*, which the code itself cannot.
2. **Git stores snapshots addressed by content.** Each file version (blob), directory (tree) and commit is stored under the hash of its bytes (Secure Hash Algorithm 1 (SHA-1) historically, with SHA-256 support added). Identical content is stored once. A commit's hash covers its tree and its parent hashes, so it fixes the entire history behind it: altering any old commit changes every later hash, the same structure as a Merkle tree.
3. **Branches are cheap names for commits.** In Git a branch is a pointer to one commit that moves forward as you commit. Creating one copies nothing. Tags are pointers that do not move. Because names are separate from content, many views of one history cost almost nothing.
4. **Merging is reconciling concurrent edits.** Given two branches and their common ancestor, a three-way merge takes each change made on either side; if both sides changed the same region differently, it reports a conflict for a human to resolve. The merge is textual: two changes that merge cleanly can still break the program together (one renames a function, another adds a call to the old name), which is why merged code must be built and tested.
5. **Distributed means every clone is a full repository.** In centralised systems (Concurrent Versions System (CVS), Subversion) history lives on a server; in distributed ones (Git, Mercurial) every developer has the whole graph and can commit offline. Synchronisation exchanges missing commits, which is easy because content-addressed objects never conflict: the same hash always means the same bytes.
6. **Long-lived branches accumulate merge risk.** The longer two branches diverge, the more their changes interact, and the harder and riskier the merge. Trunk-based development (everyone integrates into one main branch at least daily, hiding unfinished features behind flags) keeps divergence small. *Accelerate* (2018) found it associated with higher delivery performance.
7. **Repository layout is an organisational choice.** A monorepo holds many projects in one history, allowing atomic changes across projects and one version of each dependency; Google keeps billions of lines in one (Potvin and Levenberg, 2016) but needed custom tooling. Many repositories give teams independence but make cross-cutting changes and version alignment harder. Both are valid; the trade-off is coordination cost against autonomy.

## Key concepts

| Term | Meaning |
|---|---|
| Commit | An immutable snapshot of the tree plus metadata (author, message, parent commits) |
| Content addressing | Naming an object by a hash of its content, so the name verifies the data |
| Branch | A movable name pointing to a commit |
| Merge | A commit with two or more parents that combines their changes |
| Three-way merge | Merging by comparing both versions against their common ancestor |
| Rebase | Replaying commits onto a new base, rewriting their hashes to give a linear history |
| Trunk-based development | Integrating all work into one main branch frequently, using short-lived branches |
| Monorepo | A single repository holding many projects |

## How it fits

- **Below:** commit identity rests on [cryptographic hash functions](../../11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md) (collision resistance is why SHA-1's 2017 practical collision prompted the move to SHA-256). History is a DAG, a structure from [graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md); finding a merge base is a common-ancestor search. Distributed clones that sync later are a form of [eventual consistency](../../10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md), with humans resolving conflicts that a Conflict-free Replicated Data Type (CRDT) would resolve automatically.
- **Above:** every [code review](../03-quality/static-analysis-and-code-review.md) is a diff between commits; [continuous integration](../04-operations/build-and-continuous-delivery.md) builds every commit; `git bisect` turns [debugging](../03-quality/debugging.md) a regression into binary search over history.
- **Siblings:** version control is what makes short [lifecycles](development-lifecycles.md) workable; repository and ownership boundaries reflect [team structure](conways-law-and-teams.md).

## Common misconceptions

- **"Git stores diffs."** Git's model is snapshots; diffs are computed on demand. Pack files do use delta compression for storage, but that is an encoding detail.
- **"A clean merge means the code works."** Merging is textual and knows nothing about semantics. Only building and testing the merged result checks it.
- **"Version control is only for code."** Configuration, infrastructure definitions, database schemas and documentation all benefit; "everything as code" puts them under the same review and history.

## Go deeper

- Scott Chacon and Ben Straub, *Pro Git* (2nd ed., 2014): especially the chapter on Git internals.
- Rachel Potvin and Josh Levenberg, "Why Google Stores Billions of Lines of Code in a Single Repository", *Communications of the ACM* (2016): the monorepo trade-offs at scale.
- Titus Winters, Tom Manshreck and Hyrum Wright, *Software Engineering at Google* (2020): chapters on version control and the "one version" rule.
