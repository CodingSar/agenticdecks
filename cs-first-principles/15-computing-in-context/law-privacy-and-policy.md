# Law, Privacy and Policy

> **Layer:** [15 Computing in Context](README.md)
> **Builds on:** [Ethics and professional responsibility](ethics-and-professional-responsibility.md), [Public-key cryptography](../11-security-and-cryptography/02-cryptography/public-key-cryptography.md), [The relational model](../09-data-management/01-data-models/the-relational-model.md), [Layering and the end-to-end principle](../08-networking/01-principles/layering-and-the-end-to-end-principle.md)
> **Enables:** [Requirements](../12-software-engineering/02-process/requirements.md), [Observability](../12-software-engineering/04-operations/observability.md)

## Essence

Law and policy turn some expectations about technology into enforceable rules. For computing the main areas are privacy and data protection, intellectual property, liability and safety, computer crime, competition, and speech on platforms. Lawrence Lessig (*Code and Other Laws of Cyberspace*, 1999) identified four forces that regulate behaviour: law, social norms, markets and architecture. In computing, architecture (code) is unusually powerful: design can make an act impossible or trivial whatever the law says. So engineers are policymakers by default, and policymakers increasingly regulate design itself, as the European Union's General Data Protection Regulation (GDPR) does with its requirement of data protection "by design and by default".

## Core tenets

1. **Privacy is about appropriate flows, not just secrecy.** Warren and Brandeis framed privacy as "the right to be let alone" (1890). Helen Nissenbaum's contextual integrity (*Privacy in Context*, 2010) explains modern harms better: information shared in one context (with a doctor) carries norms, and a flow that breaks them (to an insurer or advertiser) violates privacy even if the information was never secret.
2. **Data protection law regulates the whole life of personal data.** The GDPR (Regulation (EU) 2016/679, applying from 25 May 2018) requires a lawful basis for every processing of personal data (consent, contract, legal obligation, vital interests, public task or legitimate interests) and sets principles: lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality; and accountability. Individuals have rights of access, rectification, erasure, portability and objection, and safeguards against significant solely automated decisions. Fines reach €20 million or 4% of worldwide annual turnover, whichever is higher, and breaches must usually be reported to the regulator within 72 hours.
3. **Law reaches into design.** GDPR Article 25 requires data protection by design and by default. In engineering terms: collect less, keep data for defined periods, pseudonymise and encrypt, make deletion propagate through backups and replicas, and log who accessed what. The EU Artificial Intelligence (AI) Act (Regulation (EU) 2024/1689) sets obligations that scale with the risk of an AI system's use.
4. **Anonymisation is much weaker than it looks.** Latanya Sweeney showed that ZIP code, birth date and sex alone uniquely identify about 87% of the United States (US) population (2000). Narayanan and Shmatikov re-identified Netflix Prize users from a few movie ratings (2008). [Differential privacy](../11-security-and-cryptography/01-security-principles/privacy-enhancing-technologies.md) (Dwork, McSherry, Nissim and Smith, 2006) offers a mathematical guarantee instead: adding calibrated noise so any one person's data changes outputs only slightly, at a measurable cost in accuracy.
5. **Encryption policy is a lasting conflict.** States want lawful access to communications; strong [public-key cryptography](../11-security-and-cryptography/02-cryptography/public-key-cryptography.md) and end-to-end encryption make that impossible without weakening security for everyone. The 1990s "crypto wars" (export controls, the 1993 Clipper chip key-escrow proposal) ended with strong cryptography widely allowed; the debate recurs. Security researchers' consensus ("Keys Under Doormats", Abelson et al., 2015) is that exceptional-access mechanisms create systemic vulnerabilities.
6. **Intellectual property shapes how software is shared.** Code is protected by copyright automatically; some jurisdictions also allow software-implemented patents. Free and open-source licences use copyright to grant freedoms: permissive licences (MIT, Berkeley Software Distribution (BSD), Apache) allow almost any reuse, while copyleft licences such as the GNU General Public License (GPL, Stallman, 1989) require that distributed derivative works carry the same freedoms. In *Google v. Oracle* (2021) the US Supreme Court held Google's reuse of the Java Application Programming Interface (API) declarations to be fair use, leaving open whether APIs are copyrightable at all.
7. **Platform and network rules decide who controls the Internet.** Intermediary liability rules, such as Section 230 of the US Communications Decency Act (1996) and the safe harbour of the Digital Millennium Copyright Act (DMCA, 1998), let platforms host user content without being treated as its publisher (intermediary liability). Net neutrality, internet service providers treating traffic equally, follows from the [end-to-end design](../08-networking/01-principles/layering-and-the-end-to-end-principle.md); its legal status in the US has changed repeatedly.
8. **Law is territorial; data is not.** A server, user and company in three countries create conflicts of jurisdiction. The GDPR applies to anyone processing data of people in the EU, and the Court of Justice of the EU's *Schrems II* ruling (2020) invalidated the EU-US Privacy Shield over US surveillance law. Data localisation rules constrain [replication](../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md) and [partitioning](../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md) choices.

## Key concepts

| Term | Meaning |
|---|---|
| Personal data | Under the GDPR, any information relating to an identified or identifiable natural person |
| Lawful basis | One of the six GDPR grounds that permit processing personal data |
| Data minimisation | Collecting and keeping only the data needed for a stated purpose |
| Contextual integrity | Privacy as conformity of information flows to the norms of their context |
| Re-identification | Linking supposedly anonymous records back to individuals |
| Differential privacy | A guarantee that outputs change little whether or not any one individual's data is included |
| Copyleft | A licence condition requiring derivative works to be distributed under the same terms |
| Net neutrality | Treating all internet traffic equally regardless of source, destination or content |

## How it fits

- **Below:** privacy duties land in [databases](../09-data-management/01-data-models/the-relational-model.md) (retention and erasure, including in [logs and backups](../09-data-management/04-transactions/recovery-and-logging.md)), in [cryptography](../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md) and [access control](../11-security-and-cryptography/03-system-security/access-control.md), and in [Machine Learning (ML) systems](../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md) trained on personal or copyrighted data. Differential privacy uses [probability](../01-mathematical-foundations/06-probability-and-statistics/probability.md).
- **Above:** this is the top of the stack; legal duties flow back down as [requirements](../12-software-engineering/02-process/requirements.md), and telemetry from [observability](../12-software-engineering/04-operations/observability.md) must itself comply.
- **Siblings:** [ethics](ethics-and-professional-responsibility.md) supplies the values law partly codifies; [history](history-of-computing.md) shows law arriving after the technology; [environmental impact](environmental-impact.md) is a newer target of disclosure and right-to-repair rules.

## Common misconceptions

- **"Removing names makes data anonymous."** Combinations of ordinary attributes identify most people; pseudonymised data remains personal data under the GDPR.
- **"Privacy law is only about consent."** Consent is one of six lawful bases, often not the right one. The principles (minimisation, purpose limitation, storage limitation) apply whatever the basis.
- **"Open source means no licence obligations."** Open-source licences are copyright licences with conditions; breaching copyleft terms is infringement.

## Go deeper

- Lawrence Lessig, *Code and Other Laws of Cyberspace* (1999; *Code: Version 2.0*, 2006): architecture as regulation.
- Helen Nissenbaum, *Privacy in Context: Technology, Policy, and the Integrity of Social Life* (2010): contextual integrity.
- Regulation (EU) 2016/679, the General Data Protection Regulation (2016): read Articles 5, 6, 17, 22 and 25 directly.
