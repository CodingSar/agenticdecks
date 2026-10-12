# Brief for cluster review agents

You are improving Anki flashcard decks in /home/user/agenticdecks for one learner: a cloud/Kubernetes platform
and enterprise architect. Goal: **learn effectively**. Fewer, sharper, high-signal cards that hold up in real work
(and in the named exams).

Read first: `work/GUIDELINES.md` (card rules + output field schema) and `work/PLAN.md` (overall plan).
Inputs: `work/source/<deck>.json` (normalized notes; fields: guid,type,deck,tags,front,back,text,image,analogy,extra,source[,reverse]).
Media files live in `media/`. Don't rename them.

## Do these passes over YOUR decks only
1. **Map:** read every note. Group them by concept. Find duplicates and overlaps within and across your decks.
2. **Combine/split:** merge duplicates into the best single card. Split any card that asks more than one thing or whose
   answer goes over the length rule (~25 words target, ~60 max). Enumerations become clozes or per-item cards.
3. **Best practices:** rewrite prompts to be precise and context-cued, answers minimal, with tidy HTML (`<b>`, `<code>`,
   short `<ul>`). Turn "what" into "why/when/what breaks" where that adds understanding. Add contrast cards for
   concepts that are easy to confuse.
4. **Analogies:** add accurate 1–2 sentence analogies in `analogy` where an abstract idea needs a hook. Keep existing good
   analogies and intuitions. Don't force them onto every card. Roughly 15–35% of cards is about right for technical decks.
5. **Signal filter:** delete meta/trivia (author, publication year, edition, "chapter N covers", "who coined" unless the
   name itself is the vocabulary people use at work, deck-meta, marketing fluff) and anything with no impact on work
   or exam performance.

Organise each output deck into a sensible set of concept subdecks (`Parent::01 Topic`, ...), roughly 4–12 of them.
Exam-related labels belong in `source` or `tags`. Keep MathJax and image references intact.
Keep the original `guid` on any card that descends from an original note (on a split, the first part keeps it and the
others get `null`). When merging two notes, keep one of their guids. Never invent guids.

## Output (only write these files)
- `work/out/<OutputName>.json` = `{"deck_name": ..., "file": "<OutputName>.apkg", "description": "<1–2 sentence HTML deck description: scope + who it's for>", "notes": [...]}`
  Every note's `deck` must start with `deck_name`. Every note carries all schema keys (empty string if unused).
- `work/out/<OutputName>.changelog.md` = short changelog: notes in/out, merges (which into which, a few examples),
  deletions with a reason (list them, one line each), number of splits, analogies added.

Work efficiently: you may write a Python script in the scratchpad that loads the sources and emits the output.
Hand-writing the rewritten notes in Python dicts/JSON is expected. Write in chunks if large.
Then run `python3 tools/check.py work/out/<OutputName>.json` until there are **0 errors** and few or no long-answer warnings.
Don't run build.py, don't touch other files, and don't commit.
Final reply (short): for each output deck, notes before → after, # deleted, # merged, # split, # analogies, plus any
cross-cluster overlap you noticed but left alone because another agent owns it.

## Ownership boundaries (to avoid cross-cluster duplicates)
- Linux kernel mechanisms (namespaces, cgroups, seccomp, capabilities, eBPF internals) → Linux deck. Kubernetes deck covers the K8s API/objects that use them.
- Operators/controllers: concept + reconciliation pattern → Platform Engineering. Go implementation details (controller-runtime, client-go, informers code) → Go deck.
- GitOps/Helm/IaC/policy-as-code → Platform Engineering. Kubernetes deck covers core K8s and the CKA/CKAD/CKS/KCNA/KCSA exam material, but not Argo/Flux depth.
- TCP/IP/BGP/TLS/LB → Networking. CNI plugins and K8s Services/Ingress → Kubernetes.
- Consensus/CAP/replication → Distributed Systems & Data.
- Cognitive biases/influence/learning science → Architect Craft. Complexity/evolution → Adaptive Systems.
- Probability/statistics → Quantitative Foundations. Transformers/LLMs → LLMs & Agentic Engineering.
