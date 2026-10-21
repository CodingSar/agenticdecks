# Privacy-Enhancing Technologies

> **Layer:** [11 Security and Cryptography](../README.md) › [Security principles](README.md)
> **Builds on:** [CIA and threat modeling](cia-and-threat-modeling.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md), [Public-key cryptography](../02-cryptography/public-key-cryptography.md)
> **Enables:** [Law, privacy and policy](../../15-computing-in-context/law-privacy-and-policy.md), [Generalization and bias-variance](../../13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md), [Network attacks and defenses](../04-network-and-application-security/network-attacks-and-defenses.md)

## Essence

Confidentiality asks *who may read this data*; privacy asks *what may be learned or done about a person*, even by parties who are allowed to see the data. Encryption and access control cannot answer the second question, because the threat is often the authorised recipient, the published statistic or the metadata of who talks to whom. Privacy-enhancing technologies (PETs) are mechanisms that let a useful computation happen while limiting what it reveals about any individual. Each protects a different thing: **differential privacy** bounds what an output reveals, **anonymity networks** hide who is communicating, and **secure multiparty computation** and **homomorphic encryption** let parties compute on data that no single party sees. The hard lesson behind all of them is that removing names is not anonymisation.

## Core tenets

1. **Privacy is about inference and flows, not only secrecy.** Data that is harmless alone becomes identifying in combination, and data shared properly in one context (a diagnosis to a doctor) violates expectations in another (the same diagnosis to an advertiser). Nissenbaum's *contextual integrity* (2004) frames privacy as appropriate information flow. So a privacy threat model must include authorised analysts, linkage with outside datasets, and aggregate outputs, not just eavesdroppers.

2. **De-identification fails because quasi-identifiers link records.** Sweeney showed that postcode, birth date and sex alone identify about 87% of the United States population (2000), and re-identified a governor's medical record by joining "anonymous" hospital data with a voter roll. Narayanan and Shmatikov (2008) re-identified Netflix Prize users from a handful of movie ratings and dates. In high-dimensional data almost every record is unique, so any attribute can act as an identifier.

3. **k-anonymity hides people in crowds, but crowds still leak.** k-anonymity (Samarati and Sweeney, 1998) generalises or suppresses quasi-identifiers until every record matches at least k − 1 others. It fails against *homogeneity* (if everyone in a group has the same diagnosis, membership reveals it) and *background knowledge*, which led to l-diversity and t-closeness. Deeper problems remain: the guarantee is a property of one table, not of what an attacker can infer, and it breaks under composition when two k-anonymous releases are combined.

4. **Answering too many queries too accurately destroys privacy.** Dinur and Nissim (2003) showed that if a database answers enough aggregate queries with error well below √n (for n records), an attacker can reconstruct nearly the whole dataset. This "fundamental law of information recovery" means every useful release spends some privacy, and the only question is how to measure and cap the spending.

5. **Differential privacy bounds what any one person's data can change.** A randomised mechanism M is ε-differentially private (Dwork, McSherry, Nissim and Smith, 2006) if for every pair of datasets D and D′ differing in one person's data, and every set S of outputs, Pr[M(D) ∈ S] ≤ e^ε · Pr[M(D′) ∈ S]. Whatever the attacker already knows, the output is almost equally likely whether or not you are in the data. The Laplace mechanism achieves it for a numeric query by adding noise with scale Δf/ε, where the sensitivity Δf is the most one person can change the answer. The relaxed (ε, δ) form allows failure probability δ.

6. **Privacy loss composes, so it is a budget.** Running k mechanisms that are each ε-differentially private on the same data is at most kε-differentially private (advanced composition gives roughly √k growth for small δ). Post-processing a private output cannot make it less private. These two properties, which k-anonymity lacks, let a system track a total privacy budget across many releases. Choosing ε is a policy decision: smaller is more private and noisier.

7. **Central and local models trade trust for accuracy.** In the *central* model a trusted curator holds raw data and adds noise to outputs; the 2020 United States Census used this. In the *local* model each user randomises their own data before sending it, as in Warner's randomised response (1965) and Google's RAPPOR (2014), so no one is trusted, but for counting queries the error is larger by a factor of about √n. Machine learning can be trained privately by clipping and noising per-example gradients (Abadi et al., 2016), which also limits membership-inference attacks on trained models.

8. **Anonymity networks hide who talks to whom, within limits.** Chaum's mix networks (1981) relay encrypted messages through servers that batch and reorder them. Onion routing, deployed as Tor (Dingledine, Mathewson and Syverson, 2004), wraps a message in one encryption layer per relay, so each of the typically three relays learns only its predecessor and successor. Tor keeps latency low by not batching, so an adversary who watches both ends of a circuit can correlate timing and volume; it defends against local observers, not a global passive adversary.

9. **Cryptography can compute without revealing inputs, but not without revealing outputs.** Secure multiparty computation (MPC) lets parties compute a joint function so that each learns only the output: Yao (1982, garbled circuits from 1986) and Goldreich, Micali and Wigderson (1987) showed any function can be computed this way. Homomorphic encryption lets a server compute on ciphertexts; Gentry (2009) gave the first fully homomorphic scheme, built on lattices, still orders of magnitude slower than plaintext computation. Both protect the computation, while the output itself may still leak, so they pair naturally with differential privacy.

## Key concepts

| Term | Meaning |
|---|---|
| Quasi-identifier | Attribute that is not a name but helps link a record to a person |
| k-anonymity | Each record is indistinguishable from at least k − 1 others on quasi-identifiers |
| Differential privacy (DP) | Output distribution changes by at most a factor e^ε when one person's data changes |
| Sensitivity Δf | Largest change one person can cause in a query's answer |
| Privacy budget | Total ε spent across all releases from one dataset |
| Local DP | Each user randomises data before collection; no trusted curator |
| Onion routing | Layered encryption through relays so no relay sees both ends |
| MPC | Joint computation revealing only the agreed output |
| Fully homomorphic encryption (FHE) | Encryption allowing arbitrary computation on ciphertexts |

## How it fits

- **Below:** DP is a statement about [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) distributions, and reconstruction attacks are [statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md) used against people; onion routing and MPC use [public-key](../02-cryptography/public-key-cryptography.md) and [symmetric](../02-cryptography/symmetric-encryption.md) primitives defined in the [foundations of cryptography](../02-cryptography/foundations-of-modern-cryptography.md).
- **Above:** [privacy law](../../15-computing-in-context/law-privacy-and-policy.md) decides what counts as anonymous data; models that [memorise training data](../../13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md) leak it, which private training limits; anonymity networks are a response to the traffic analysis described in [network attacks](../04-network-and-application-security/network-attacks-and-defenses.md).
- **Siblings:** [threat modeling](cia-and-threat-modeling.md) must name privacy adversaries, including authorised insiders; [design principles](security-design-principles.md) add data minimisation: data never collected cannot leak.

## Common misconceptions

- **"Removing names and identifiers makes data anonymous."** Combinations of ordinary attributes re-identify most people.
- **"Aggregate statistics are safe to publish."** Enough accurate aggregates reconstruct the underlying records.
- **"Encrypted computation makes the result private."** MPC and homomorphic encryption hide inputs during computation; the output can still reveal them.
- **"Tor makes you anonymous against anyone."** It does not resist an adversary who can observe traffic entering and leaving the network.

## Go deeper

- Dwork and Roth, *The Algorithmic Foundations of Differential Privacy* (2014): the standard rigorous treatment.
- Narayanan and Shmatikov, "Robust De-anonymization of Large Sparse Datasets", IEEE Symposium on Security and Privacy (2008): why de-identification fails.
- Dingledine, Mathewson and Syverson, "Tor: The Second-Generation Onion Router", USENIX Security (2004).
- Evans, Kolesnikov and Rosulek, *A Pragmatic Introduction to Secure Multi-Party Computation* (2018).
