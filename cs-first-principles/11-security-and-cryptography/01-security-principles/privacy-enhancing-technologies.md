# Privacy-Enhancing Technologies

> **Layer:** [11 Security and Cryptography](../README.md) › [Security principles](README.md)
> **Builds on:** [CIA and threat modeling](cia-and-threat-modeling.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md), [Public-key cryptography](../02-cryptography/public-key-cryptography.md)
> **Enables:** [Law, privacy and policy](../../15-computing-in-context/law-privacy-and-policy.md), [Generalization and bias-variance](../../13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md), [Network attacks and defenses](../04-network-and-application-security/network-attacks-and-defenses.md)

## Essence

Confidentiality asks *who may read this data*; privacy asks *what may be learned about a person*, even by parties allowed to see the data. Encryption and access control cannot answer that: the threat is often the authorised recipient, a published statistic or communication metadata. Privacy-enhancing technologies (PETs) allow useful computation while limiting what it reveals about any individual. **Differential privacy** bounds what an output reveals, **anonymity networks** hide who is communicating, and **secure multiparty computation** and **homomorphic encryption** compute on data no single party sees. The lesson behind all of them: removing names is not anonymisation.

## Core tenets

1. **Privacy is about inference and flows, not only secrecy.** Data harmless alone becomes identifying in combination, and a flow proper in one context (a diagnosis to a doctor) violates expectations in another (the same diagnosis to an advertiser); Nissenbaum (2004) calls this *contextual integrity*. So a privacy threat model must include authorised analysts, linkage with outside data and aggregate outputs.

2. **De-identification fails because quasi-identifiers link records.** Sweeney showed that postcode, birth date and sex alone identify about 87% of the United States population (2000), by joining "anonymous" hospital records with a voter roll. Narayanan and Shmatikov (2008) re-identified Netflix Prize users from a few movie ratings. In rich data almost every record is unique.

3. **k-anonymity hides people in crowds, but crowds still leak.** k-anonymity (Samarati and Sweeney, 1998) generalises or suppresses quasi-identifiers until every record matches at least k − 1 others. It fails against *homogeneity* (if everyone in a group has the same diagnosis, membership reveals it) and background knowledge, prompting l-diversity and t-closeness. The deeper flaw is that it constrains one table, not what an attacker can infer, and two k-anonymous releases can combine to identify people.

4. **Answering too many queries too accurately destroys privacy.** Dinur and Nissim (2003) showed that if a database answers enough aggregate queries with error well below √n (for n records), an attacker can reconstruct nearly the whole dataset. So every useful release spends some privacy; the question is how to measure and cap the spending.

5. **Differential privacy (DP) bounds what any one person's data can change.** A randomised mechanism M is ε-differentially private (Dwork, McSherry, Nissim and Smith, 2006) if for every pair of datasets D and D′ differing in one person's data, and every set S of outputs, Pr[M(D) ∈ S] ≤ e^ε · Pr[M(D′) ∈ S]. Whatever the attacker already knows, the output is almost equally likely whether or not you are in the data. The Laplace mechanism adds noise of scale Δf/ε to a numeric query, where the sensitivity Δf is the most one person can change the answer. The relaxed (ε, δ) form allows failure probability δ.

6. **Privacy loss composes, so it is a budget.** Running k ε-differentially private mechanisms on the same data is at most kε-differentially private (roughly √k·ε if a small δ is allowed). Post-processing a private output cannot make it less private. k-anonymity has neither property; DP lets a system track a total privacy budget.

7. **Central and local models trade trust for accuracy.** In the *central* model a trusted curator holds raw data and noises the outputs, as the 2020 United States Census did. In the *local* model each user randomises their own data before sending it, as in Warner's randomised response (1965) and Google's RAPPOR (Randomized Aggregatable Privacy-Preserving Ordinal Response, 2014): no one is trusted, but counting error grows by a factor of about √n. Models can be trained privately by clipping and noising per-example gradients (Abadi et al., 2016), which also blunts membership-inference attacks.

8. **Anonymity networks hide who talks to whom, within limits.** Chaum's mix networks (1981) batch and reorder encrypted messages at each relay. Onion routing, deployed as Tor (Dingledine, Mathewson and Syverson, 2004), wraps a message in one encryption layer per relay, so each of the usual three relays learns only its neighbours. Tor does not batch, to keep latency low, so an adversary watching both ends can correlate timing and volume.

9. **Cryptography can compute without revealing inputs, but not without revealing outputs.** Secure multiparty computation (MPC) lets parties compute a joint function so each learns only the output; Yao (1982) and Goldreich, Micali and Wigderson (1987) showed any function can be computed this way. Homomorphic encryption lets a server compute on ciphertexts; Gentry (2009) gave the first fully homomorphic scheme, lattice-based and still orders of magnitude slower than plaintext. Both hide inputs, but the output may still leak, so they pair naturally with DP.

## Key concepts

| Term | Meaning |
|---|---|
| Quasi-identifier | Non-name attribute that helps link a record to a person |
| k-anonymity | Each record is indistinguishable from at least k − 1 others on quasi-identifiers |
| DP | Output distribution changes by at most a factor e^ε when one person's data changes |
| Sensitivity Δf | Largest change one person can cause in a query's answer |
| Privacy budget | Total ε spent across releases from one dataset |
| Onion routing | Layered encryption through relays so no relay sees both ends |
| MPC | Joint computation revealing only the agreed output |
| Fully homomorphic encryption (FHE) | Encryption allowing arbitrary computation on ciphertexts |

## How it fits

- **Below:** DP is a statement about [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) distributions; reconstruction is [statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md) aimed at people; onion routing and MPC use [public-key](../02-cryptography/public-key-cryptography.md) and [symmetric](../02-cryptography/symmetric-encryption.md) primitives.
- **Above:** [privacy law](../../15-computing-in-context/law-privacy-and-policy.md) decides what counts as anonymous; models that [memorise training data](../../13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md) leak it; anonymity networks answer the traffic analysis of [network attacks](../04-network-and-application-security/network-attacks-and-defenses.md).
- **Siblings:** [threat modeling](cia-and-threat-modeling.md) must name privacy adversaries, including authorised insiders; [design principles](security-design-principles.md) add data minimisation: data never collected cannot leak.

## Common misconceptions

- **"Removing names makes data anonymous."** Combinations of ordinary attributes re-identify most people, and enough accurate aggregates reconstruct the records.
- **"Encrypted computation makes the result private."** MPC and homomorphic encryption hide inputs; the output can still reveal them. Likewise Tor hides routes from local observers, not from one watching both ends.

## Go deeper

- Dwork and Roth, *The Algorithmic Foundations of Differential Privacy* (2014): the standard treatment.
- Narayanan and Shmatikov, "Robust De-anonymization of Large Sparse Datasets", IEEE Symposium on Security and Privacy (2008).
- Dingledine, Mathewson and Syverson, "Tor: The Second-Generation Onion Router", USENIX Security (2004).
- Evans, Kolesnikov and Rosulek, *A Pragmatic Introduction to Secure Multi-Party Computation* (2018).
