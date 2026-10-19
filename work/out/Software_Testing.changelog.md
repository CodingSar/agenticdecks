# Software Testing: changelog

**In:** 138 notes → **Out:** 121 notes in 8 subdecks (01 Foundations & Principles · 02 Test Types & Levels · 03 Unit Tests, Doubles & TDD · 04 Test Strategy & Portfolio · 05 BDD & Gherkin · 06 Test Design & Edge Cases · 07 Test Suite Quality · 08 Testing with Coding Agents).

## History subdeck (22 notes) dissolved
Only history that explains *why* a practice exists was kept, and it was moved into the concept subdecks:
- Dijkstra's limit on testing
- testing vs debugging
- Myers' "a successful test finds a bug"
- the mutation-testing hypotheses (why mutation testing works)
- why BDD says "behaviour"
- test pyramid / trophy
- chaos engineering
- characterization tests
- shift-left/right

Names and years were cut down to context.

## Merges
- "Who coined test double" → test-double cloze.
- "Who coined exploratory testing" → exploratory testing card.
- QuickCheck origin → property-based testing card (tools in extra).
- Fuzzing origin → fuzz testing card (the "why it works" fact goes in extra).
- Scenario naming → good test name card.
- Past incidents → error guessing card.
- "Confirm it fails first with agents" → red/green TDD agent card.

## Deletions
- 1947 moth / "bug" origin: trivia.
- Gelperin & Hetzel five eras: history list with no practical use.
- 1972 Chapel Hill symposium: trivia.
- IEEE 829 / ISO 29119: standards trivia.
- SUnit/JUnit creators: trivia.
- When/by whom TDD was popularised: trivia.
- Cucumber/Gherkin origin: trivia.
- Who created the Agile Testing Quadrants: trivia (the quadrants card is kept).
- "Systematically find edge cases" 7-step list: redundant with the individual technique cards.
- Adversarial mutation with agents (AdverTest): research niche, already covered by the mutation and "prove it can fail" cards.
- "Make an agent's suite more trustworthy than green": a summary list that repeats other cards.
- 7 more notes merged (see above).

## Splits: 0
- The Gherkin keyword list was reduced to one targeted card (Scenario Outline + Examples).
- The Gherkin anti-pattern list was cut to a cloze of the 3 smells no other card covers.
- Enumerations (ISTQB principles, FIRST, doubles, performance tests, quadrants, coverage ladder, ZOMBIES/CORRECT/Right-BICEP, edge-case lists, PBT patterns, agent gates, reward hacks) became clozes.

## New contrast card: 1
Mock vs stub.

## Fixes
The pesticide paradox no longer says bugs "adapt" (inaccurate). It now says the tests only probe the paths they were written for.

**Analogies added: 20.**

## Product-content review

**Rewritten** (guid kept; product moved to a short example in `extra`)
- "Why are hooks better than CLAUDE.md instructions for test discipline?" → "Why are hooks better than instruction-file guidance (CLAUDE.md / AGENTS.md) for test discipline?"

## Abbreviations expanded

Notes touched: 26

- E2E → end-to-end
- TDD → test-driven development
- BDD → behaviour-driven development
- SAST → static application security testing
- DAST → dynamic application security testing
- SCA → software composition analysis
- UAT → user acceptance testing
- ISTQB → International Software Testing Qualifications Board
- WCAG → Web Content Accessibility Guidelines
- GA → general availability
- DRY → don't repeat yourself
- RTL → right-to-left
