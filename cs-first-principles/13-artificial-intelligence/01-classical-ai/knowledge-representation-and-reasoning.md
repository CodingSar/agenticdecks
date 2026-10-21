# Knowledge Representation and Reasoning

> **Layer:** [13 Artificial Intelligence](../README.md) › [Classical AI](README.md)
> **Builds on:** [Predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md), [Proof techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md), [Halting problem and undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), [Logic and declarative programming](../../06-programming-languages/01-paradigms/logic-and-declarative.md)
> **Enables:** [Probabilistic reasoning](probabilistic-reasoning.md), [Search and planning](search-and-planning.md), [The relational model](../../09-data-management/01-data-models/the-relational-model.md)

## Essence

Knowledge Representation and Reasoning (KR&R) asks how to write down what an agent knows so that a machine can derive what follows from it. The bet of classical Artificial Intelligence (AI), the "physical symbol system" hypothesis, was that intelligence is the manipulation of explicit symbols according to sound rules of inference. A representation is a formal language with a precise semantics (what each sentence says about the world) and an inference procedure (how to derive new sentences). The central tension is **expressiveness versus tractability**: the more a language can say, the harder, and eventually impossible, it becomes to answer questions in it. Practical systems such as rule engines, description logics and knowledge graphs each pick a point on that curve.

## Core tenets

1. **Entailment is defined by semantics, inference by syntax, and the two must agree.** A knowledge base KB entails a sentence α (KB ⊨ α) if α is true in every model where KB is true. An inference procedure derives α (KB ⊢ α) by rewriting symbols. It is *sound* if it derives only entailed sentences and *complete* if it derives all of them. Resolution is sound and refutation-complete for first-order logic.

2. **First-order reasoning is semi-decidable.** If KB ⊨ α, a complete prover will eventually find a proof; if not, it may run forever (Church and Turing, 1936). So no general-purpose reasoner can answer every question in full first-order logic. Every practical KR system restricts the language to recover decidability or efficiency.

3. **Restricted languages buy tractability.** Horn clauses (rules with at most one positive conclusion) admit linear-time forward chaining in the propositional case and underpin Prolog and Datalog. Description logics, the basis of the Web Ontology Language (OWL), restrict quantifiers so that subsumption ("is every A a B?") is decidable. Choosing the language is choosing the complexity class.

4. **Classical logic is monotonic, but common sense is not.** In standard logic, adding facts never retracts a conclusion. Yet "birds fly" must be withdrawn on learning "Tweety is a penguin". Default logic, negation as failure and the closed-world assumption (what is not known to be true is false, as in databases) model this, at the cost of more complex semantics.

5. **The frame problem shows how much is left unsaid.** When an action changes one thing, a logical description must also say that everything else stays the same. Writing those "frame axioms" explicitly explodes in size. Planning languages solve it by convention: whatever an action does not mention is unchanged.

6. **Structured knowledge is a graph of entities and relations.** Semantic networks, frames, ontologies and modern knowledge graphs store facts as (subject, relation, object) triples with type hierarchies and inheritance. They trade the full power of logic for fast lookup and easy curation, and are widely used in search engines and data integration.

7. **Hand-written knowledge hits a bottleneck.** Projects such as Cyc (from 1984) showed that encoding common sense by hand is enormously expensive and still brittle at the edges. This "knowledge acquisition bottleneck" is a main reason the field shifted to learning representations from data. As of the mid-2020s, large language models hold broad knowledge implicitly but cannot guarantee soundness, so explicit KR survives where correctness and auditability matter.

## Key concepts

| Term | Meaning |
|---|---|
| Model | An assignment of meaning to symbols under which sentences are true or false |
| Entailment (⊨) | α is true in every model of the knowledge base |
| Soundness / completeness | Derives only true consequences / derives all of them |
| Resolution | Inference rule combining two clauses with complementary literals |
| Horn clause | Clause with at most one positive literal; a rule "if A and B then C" |
| Forward / backward chaining | Data-driven derivation from facts / goal-driven search from the query |
| Closed-world assumption | Anything not derivable is taken to be false |
| Ontology | Formal vocabulary of types, relations and axioms for a domain |
| Frame problem | Difficulty of stating concisely what an action does *not* change |

## How it fits

- **Below:** The languages are [propositional](../../01-mathematical-foundations/01-logic/propositional-logic.md) and [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md); the limits are [undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) results; the execution model is [logic programming](../../06-programming-languages/01-paradigms/logic-and-declarative.md).
- **Above:** Datalog-style rules power [query languages](../../09-data-management/01-data-models/relational-algebra-and-sql.md), static analysers and access-control policies. Knowledge graphs feed retrieval systems around [large language models](../04-advanced-paradigms/large-language-models.md).
- **Siblings:** [Constraint satisfaction](constraint-satisfaction.md) is the engine many reasoners compile into. [Probabilistic reasoning](probabilistic-reasoning.md) replaces true/false with degrees of belief. [Planning](search-and-planning.md) uses logical state descriptions.

## Common misconceptions

- **"Symbolic AI failed."** It did not scale to open-ended perception and common sense, but its descendants (Boolean satisfiability (SAT) and Satisfiability Modulo Theories (SMT) solvers, type checkers, databases, rule engines) run everywhere, usually no longer called AI.
- **"More expressive is always better."** Each gain in expressiveness can push reasoning from linear time to exponential time to undecidable. The right language is the weakest one that says what you need.
- **"A database is just a store, not a reasoner."** A relational database under the closed-world assumption with recursive queries is a restricted logic engine.

## Go deeper

- Ronald Brachman and Hector Levesque, *Knowledge Representation and Reasoning* (2004): the expressiveness-versus-tractability trade-off made systematic.
- Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach* (4th ed., 2020), chapters 7–10: logic-based agents and inference.
- Allen Newell and Herbert Simon, "Computer Science as Empirical Inquiry: Symbols and Search" (1976): the physical symbol system hypothesis in its authors' words.
