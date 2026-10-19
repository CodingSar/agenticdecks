# Changelog: CISSP (Cloud & Kubernetes Grounded)

Source: `cissp_cloud_k8s_grounded.json` (82 notes, avg about 650 chars plus a long Grounding block) → **145 notes**
(95 basic, 50 cloze), organised into the 8 CISSP domains (01 Security & Risk Management … 08 Software Development Security).

## Splits and new cards (62 cards added)
- 57 cards split off from multi-part notes, e.g. BIA/RTO/RPO/MTD → BIA, RTO-vs-RPO cloze, RTO+WRT≤MTD cloze;
  symmetric vs asymmetric → strengths card, key-count cloze (n(n−1)/2 vs 2n), hybrid-crypto card; PKI → CA vs RA, CRL vs OCSP,
  short-lived certs; Kerberos → components cloze, clock sync, KDC weakness; DNS → poisoning, DNSSEC vs DoH/DoT, tunneling;
  NIS2 → what/how it binds, 24h/72h reporting cloze, management accountability.
- 5 new exam or contrast cards from the source content: risk rejection is not valid, Delphi technique, why HMAC lacks non-repudiation,
  K8s RBAC has no deny (use admission policy), GitOps as Clark-Wilson.
- Long enumerations became clozes (CIA, STRIDE letters with hints, STRIDE → property, control functions/types, data roles, sanitization,
  firewall types, SOC 1/2/3, SAST/DAST/SCA/IAST, DR test ladder, backups, RAID, DR sites, CMMI levels).

## Grounding
- Each Grounding paragraph (40–60 words) trimmed to one short `<b>K8s:</b>` example in `extra`, or turned into its own card when it taught
  something testable (webhook failurePolicy = fail secure/open; don't delete a compromised pod first; secret leak → rotate; workload identity federation).

## Merges (1)
- Linux deck #77 (DAC vs MAC) merged into the DAC-vs-MAC card here (keeps that guid; Linux SELinux/AppArmor example moved to `extra`).

## Deletions (content dropped from inside notes, no whole notes deleted)
- ISC2 "list core secure design principles" laundry list → replaced by a Saltzer & Schroeder cloze + fail-securely card.
- OWASP Top 10 category listing (changes every edition) → kept only injection defense and SSRF-in-cloud.
- TCP handshake detail in the TCP/IP note (owned by Networking deck); hardened-runtime detail in VM-vs-container note (owned by Linux deck).
- Reciprocal agreements / mobile sites (low signal).

## Analogies
- 24 added (about 17%): e.g. due diligence vs due care (home inspection vs repair), Bell-LaPadula (spy), RPO/RTO (save point),
  SOC 2 Type I vs II (photo vs CCTV), SBOM (ingredients label).

## Product-content review
Reviewed card by card: no product-catered cards found (tools present are open-source subjects or short examples in `extra`); nothing deleted, rewritten or scrubbed.

## Abbreviations expanded

89 notes touched. First occurrence per note written as "full name (ABBR)"; answer-bearing cloze deletions and answer-leaking fronts expanded in `back`/`extra` instead (`Terms:` line in `extra` where the abbreviation occurs only inside a deletion).

- IdP → identity provider
- OIDC → OpenID Connect
- KMS → key management service
- MFA → multi-factor authentication
- NIS2 → Network and Information Security Directive 2
- RTO → recovery time objective
- RPO → recovery point objective
- MTD → maximum tolerable downtime
- SSO → single sign-on
- ALE → annualized loss expectancy
- SLE → single loss expectancy
- AV → asset value
- EF → exposure factor
- IPsec → internet protocol security
- OSI → Open Systems Interconnection
- SA → service account
- SBOM → software bill of materials
- SCA → software composition analysis
- SAST → static application security testing
- DAST → dynamic application security testing
- IAST → interactive application security testing
- AES → advanced encryption standard
- CDI → constrained data item
- TP → transformation procedure
- IVP → integrity verification procedure
- UDI → unconstrained data item
- DEK → data encryption key
- KEK → key encryption key
- DNSSEC → DNS security extensions
- DR → disaster recovery
- HMAC → hash-based message authentication code
- HSM → hardware security module
- TPM → trusted platform module
- JWT → JSON Web Token
- KDC → key distribution center
- SAML → security assertion markup language
- SIEM → security information and event management
- SOAR → security orchestration, automation and response
- SLSA → supply-chain levels for software artifacts
- SOC → System and Organization Controls
- VPN → virtual private network
- mTLS → mutual TLS
- ABAC → attribute-based access control
- DAC → discretionary access control
- AH → authentication header
- ESP → encapsulating security payload
- IKE → internet key exchange
- BIO2 → Baseline Informatiebeveiliging Overheid
- BSIMM → Building Security In Maturity Model
- SAMM → Software Assurance Maturity Model
- C2 → command and control
- C5 → Cloud Computing Compliance Criteria Catalogue
- CASB → cloud access security broker
- CMMI → Capability Maturity Model Integration
- CNI → container network interface
- COTS → commercial off-the-shelf
- CRL → certificate revocation list
- OCSP → online certificate status protocol
- CVSS → common vulnerability scoring system
- DLP → data loss prevention
- DMZ → demilitarized zone
- DoH → DNS over HTTPS
- DoT → DNS over TLS
- DoS → denial of service
- ECC → elliptic curve cryptography
- ECDHE → elliptic curve Diffie-Hellman ephemeral
- FIDO2 → Fast Identity Online 2
- GDPR → General Data Protection Regulation
- HA → high availability
- IMDSv2 → instance metadata service version 2
- IPS → intrusion prevention system
- IR → incident response
- IRSA → identity and access management (IAM) roles for service accounts
- KPI → key performance indicator
- KRI → key risk indicator
- LSM → Linux security module
- MTTD → mean time to detect
- NAT → network address translation
- PAT → port address translation
- NGFW → next-generation firewall
- PKI → public key infrastructure
- PV → persistent volume
- RAID → redundant array of independent disks
- RSA → Rivest-Shamir-Adleman
- SDLC → software development life cycle
- SDN → software-defined networking
- SEV → secure encrypted virtualization
- TDX → trust domain extensions
- SPDX → Software Package Data Exchange
- SQLi → SQL injection
- SSRF → server-side request forgery
- TCB → trusted computing base
- TGT → ticket-granting ticket
- WAF → web application firewall
- XSS → cross-site scripting
- TEE → trusted execution environment
- ACL → access control list
- VLAN → virtual local area network
- PCR → platform configuration register
- SPIFFE → Secure Production Identity Framework for Everyone
- SPIRE → SPIFFE Runtime Environment
- SVID → SPIFFE Verifiable Identity Document
- WAL → write-ahead log
- NL → Netherlands
- NIST → National Institute of Standards and Technology
- SP → Special Publication
- OWASP → Open Worldwide Application Security Project
- CIS → Center for Internet Security
- FIPS → Federal Information Processing Standards
- RFC → Request for Comments
- CIA → confidentiality, integrity and availability
- ATT&CK → MITRE Adversarial Tactics, Techniques, and Common Knowledge
- CLOUD → Clarifying Lawful Overseas Use of Data
- CVE → common vulnerabilities and exposures
- CA / RA → Certificate Authority / Registration Authority
- (ISC)² → International Information System Security Certification Consortium
- STRIDE → spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege
- MAC → message authentication code (HMAC note) / mandatory access control (DAC vs MAC note)
- Left bare on purpose: STRIDE in its own cloze (expansion is the answer), BOLA (expansion is the answer), IAAA, DAD, CISSP, RBAC/TLS/API etc. (whitelist), OAuth, XML, ISO, L3/L4/L7.
