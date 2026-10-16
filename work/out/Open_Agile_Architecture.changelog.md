# Open Agile Architecture changelog

- Notes in: 273; notes out: 211
- Deleted: 60; merged away: 5; splits (extra notes from one source): 3; new notes: 0
- Analogies added: 30 (notes with an analogy: 30)
- Renamed deck 'Agile Architecture' → 'Open Agile Architecture'.
- Enumerations turned into clozes (one deletion per item): Scrum values, XP values, Kanban practices, Lean principles/wastes, INVEST, CALMS, Three Ways, MoSCoW, Tuckman, data mesh, design thinking, Manifesto values, 16 axioms (4 grouped clozes replacing the 16-item list).

## Merges (source note → kept note)
- #38 "How is Part 3 (The Agile Architecture Capability) subdivided in Version 2.0?" → #39 / #51 (Part 3A styles and Part 3B deliverables clozes) (Part 3 subdivision list)
- #262 "What is Big Design Up Front (BDUF), and why do Agile approaches reject it?" → #43 (purely up-front architecture insufficient) (BDUF duplicate)
- #89 "What are the axioms for the practice of Agile Architecture, and how many are the" → #90 axiom clozes (count (16) shown in the cloze header)
- #18 "What is an outcome, as opposed to an output?" → #244 (output / outcome / impact) (O-AA output vs outcome card merged)
- #255 "What is dual-track Agile?" → #245 (discovery vs delivery) (dual-track Agile duplicate)

## Deletions
- #10 "Which three audiences does Version 2.0 name?": audience list (who the standard is for): no impact on practice
- #20 "Which four topics make up Part 2 (The Agile Enterprise) in Version 2.0?": standard table-of-contents/meta list; parts and areas are covered by the clozes on the structure
- #23 "What is a stream-aligned team?": duplicate: owned by Team Topologies deck (stream-aligned / platform team definitions); O-AA taxonomy kept as cloze #22
- #24 "What is a platform team?": duplicate: owned by Team Topologies deck (stream-aligned / platform team definitions); O-AA taxonomy kept as cloze #22
- #46 "What is an architectural runway?": duplicate: SAFe construct owned by SAFe for Architects deck (architectural runway)
- #48 "What is a fitness function in evolutionary architecture?": duplicate: owned by Software Architecture & DDD deck (Fundamentals of Software Architecture) (fitness function)
- #58 "What is event-driven architecture?": duplicate: owned by Software Architecture & DDD deck (Fundamentals of Software Architecture) (event-driven architecture)
- #59 "What is event sourcing?": duplicate: owned by Distributed Systems & Data deck (event sourcing, CQRS)
- #60 "What is Command Query Responsibility Segregation (CQRS)?": duplicate: owned by Distributed Systems & Data deck (event sourcing, CQRS)
- #61 "What makes a service a microservice in the architectural sense?": duplicate: owned by Software Architecture & DDD deck (Fundamentals of Software Architecture) (microservices, saga/choreography vs orchestration)
- #62 "What is a saga, and what are its two coordination styles?": duplicate: owned by Software Architecture & DDD deck (Fundamentals of Software Architecture) (microservices, saga/choreography vs orchestration)
- #64 "Which techniques does Part 4 (The Ways of Supporting) cover in Version 2.0?": standard table-of-contents/meta list; parts and areas are covered by the clozes on the structure
- #78 "What is the ubiquitous language in Domain-Driven Design (DDD)?": duplicate: DDD strategic/tactical pattern owned by Software Architecture & DDD deck
- #79 "What is a bounded context?": duplicate: DDD strategic/tactical pattern owned by Software Architecture & DDD deck
- #80 "Domain-Driven Design (DDD) classifies subdomains as {{c1::core}} (source of comp": duplicate: DDD strategic/tactical pattern owned by Software Architecture & DDD deck
- #81 "What is a context map?": duplicate: DDD strategic/tactical pattern owned by Software Architecture & DDD deck
- #82 "Name the main context-mapping relationship patterns of Domain-Driven Design (DDD": duplicate: DDD strategic/tactical pattern owned by Software Architecture & DDD deck
- #83 "What is an anticorruption layer?": duplicate: DDD strategic/tactical pattern owned by Software Architecture & DDD deck
- #84 "Conformist versus Customer-Supplier: what distinguishes these context relationsh": duplicate: DDD strategic/tactical pattern owned by Software Architecture & DDD deck
- #85 "What is an aggregate in Domain-Driven Design (DDD)?": duplicate: DDD strategic/tactical pattern owned by Software Architecture & DDD deck
- #107 "The Agile Manifesto was written in {{c1::February 2001}} at {{c2::Snowbird, Utah": history/attribution trivia with no lesson for practice (date, place, number of authors)
- #119 "Which 1986 article gave Scrum its name and core idea?": history/attribution trivia with no lesson for practice (who named Scrum)
- #121 "John Boyd's decision loop has four steps: {{c1::Observe, Orient, Decide, Act}}.": duplicate: owned by Adaptive Systems deck (OODA loop)
- #122 "What are the domains of the Cynefin framework, and the fitting response in each?": duplicate: owned by Adaptive Systems deck (Cynefin)
- #154 "State Little's Law as applied to a workflow.": duplicate: owned by Quantitative Foundations deck (Little's Law)
- #160 "What is Weighted Shortest Job First (WSJF)?": duplicate: SAFe construct owned by SAFe for Architects deck (WSJF)
- #163 "What are the five focusing steps of the Theory of Constraints?": duplicate: owned by Architect Craft deck (mental models) (Theory of Constraints)
- #183 "What is the cycle of Test-Driven Development (TDD)?": duplicate: owned by Software Testing deck (TDD cycle)
- #191 "What is the Given-When-Then format?": duplicate: owned by Software Testing deck (Given-When-Then / BDD)
- #196 "What does the test pyramid recommend?": duplicate: owned by Software Testing deck (test pyramid)
- #199 "DevOps Research and Assessment (DORA) measures software delivery performance wit": duplicate: owned by Platform Engineering / Kubernetes decks (DORA metric definitions)
- #200 "DevOps Research and Assessment (DORA) measures software delivery performance wit": duplicate: owned by Platform Engineering / Kubernetes decks (DORA metric definitions)
- #205 "What is a blue-green deployment?": duplicate: owned by Platform Engineering / Kubernetes decks (blue-green, canary)
- #206 "What is a canary release?": duplicate: owned by Platform Engineering / Kubernetes decks (blue-green, canary)
- #207 "What is Infrastructure as Code?": duplicate: owned by Platform Engineering / Kubernetes decks (Infrastructure as Code)
- #209 "In Site Reliability Engineering (SRE): a {{c1::Service Level Indicator (SLI)}} i": duplicate: owned by Distributed Systems & Data deck (SLI/SLO/SLA)
- #213 "What are the three culture types in Westrum's typology?": duplicate: owned by Architect Craft deck (mental models) (Westrum culture typology)
- #215 "What is an internal developer platform?": duplicate: owned by Platform Engineering / Kubernetes decks (internal developer platform)
- #216 "State Conway's Law.": duplicate: owned by Team Topologies deck / Architect Craft (Conway's Law, inverse Conway); O-AA framing kept in axiom 'Organization Mirroring Architecture'
- #217 "What is the inverse Conway manoeuvre?": duplicate: owned by Team Topologies deck / Architect Craft (Conway's Law, inverse Conway); O-AA framing kept in axiom 'Organization Mirroring Architecture'
- #218 "Team Topologies defines four team types: {{c1::stream-aligned}}, {{c2::enabling}": duplicate: owned by Team Topologies deck
- #219 "Team Topologies defines three team interaction modes: {{c1::collaboration}}, {{c": duplicate: owned by Team Topologies deck
- #220 "In Team Topologies, when is the collaboration interaction mode appropriate, and ": duplicate: owned by Team Topologies deck
- #221 "In Team Topologies, what is an enabling team?": duplicate: owned by Team Topologies deck
- #222 "In Team Topologies, what is a complicated-subsystem team?": duplicate: owned by Team Topologies deck
- #223 "Why does Team Topologies treat team cognitive load as the main design constraint": duplicate: owned by Team Topologies deck
- #224 "Cognitive load theory distinguishes three kinds of load: {{c1::intrinsic}} (inhe": duplicate: cognitive load theory owned by Architect Craft (learning science) / Team Topologies
- #225 "What is a Thinnest Viable Platform?": duplicate: owned by Team Topologies deck
- #226 "What is a team Application Programming Interface (API)?": duplicate: owned by Team Topologies deck
- #227 "State Brooks's Law.": duplicate: owned by Architect Craft deck (mental models) (Brooks's Law)
- #230 "What is Dunbar's number, and why does it matter for organisation design?": duplicate: owned by Team Topologies deck (Dunbar's number)
- #233 "State Goodhart's Law and its consequence for Agile metrics.": duplicate: owned by Architect Craft deck (mental models) (Goodhart's Law)
- #236 "In the Scaled Agile Framework (SAFe), what is an Agile Release Train (ART)?": duplicate: SAFe construct owned by SAFe for Architects deck (ART, PI Planning, enabler)
- #237 "In the Scaled Agile Framework (SAFe), what are a Planning Interval (PI) and PI P": duplicate: SAFe construct owned by SAFe for Architects deck (ART, PI Planning, enabler)
- #238 "In the Scaled Agile Framework (SAFe), what is an enabler?": duplicate: SAFe construct owned by SAFe for Architects deck (ART, PI Planning, enabler)
- #260 "What is an Architecture Decision Record (ADR)?": duplicate: owned by Software Architecture & DDD deck (Fundamentals of Software Architecture) / Architect Craft (Architecture Decision Record)
- #264 "Coupling versus cohesion: what does good modular design aim for?": duplicate: owned by Software Architecture & DDD deck (Fundamentals of Software Architecture) (coupling vs cohesion)
- #265 "What is the strangler fig pattern?": duplicate: owned by Adaptive Systems deck (strangler fig)
- #268 "The four levels of the C4 model for describing software architecture are {{c1::C": duplicate: owned by Architect Craft deck (mental models) (C4 model)
- #270 "What does Gregor Hohpe's architect elevator metaphor say about the architect's r": duplicate: owned by Architect Craft deck (mental models) (architect elevator)

## Product-content review

Reviewed all cards for product-catered content (vendor feature lists, tool plugs, certification marketing, dated news, promotional phrasing): nothing applied, no changes made.
