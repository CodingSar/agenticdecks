# Identity & Zero Trust — changelog (new deck)

**Scope.** Conceptual, protocol- and architecture-level identity for a cloud/Kubernetes platform architect: how the auth protocols relate, why each design decision exists, and how to tell look-alikes apart (authn/authz, ID vs access token, state vs nonce, SP vs RP, PEP vs PDP, ZTNA vs VPN, secret vs identity, trust vs permission policy). No vendor SKUs or console trivia.

**Size.** 207 notes (185 basic, 22 cloze), 60 analogies (29 %), 8 hand-drawn SVGs (`media/idz_*.svg`, 2–4 KB each), 12 subdecks.

**Subdecks.** 01 Identity Concepts (13) · 02 Credentials & Authentication (17) · 03 PKI & Certificates (17) · 04 OAuth 2.0 (20) · 05 OpenID Connect (16) · 06 Tokens: JWT, Opaque & Introspection (18) · 07 SAML & Legacy Federation (17) · 08 Authorization Models (17) · 09 Zero Trust Architecture (18) · 10 Workload & Machine Identity (17) · 11 Cloud IAM Patterns (17) · 12 Sessions, Threats & Operations (20).

**Diagrams.** authorization-code + PKCE sequence, OIDC token relationships, PKI chain and validation path, PDP/PEP/PIP/PAP, SPIFFE/SPIRE two-step attestation, NIST 800-207 control/data plane, SAML SP- vs IdP-initiated, cross-account assume-role with trust vs permission policy.

**Deliberately left out.** TLS handshake and cipher mechanics; crypto primitives; Kubernetes RBAC objects and Istio configuration; vendor-specific IAM syntax (AWS/GCP/Azure named only in one cross-provider mapping card); LDAP schema/filters; SAML XML syntax; OAuth extensions beyond PKCE, device flow, token exchange, DPoP/mTLS binding, introspection/revocation; passwordless UX details; biometrics science; detailed XACML.

**Overlaps avoided (checked by grep before writing).**
- `Networking` 08 TLS & Crypto: no handshake cards; "CRL vs OCSP vs stapling" contrast exists there, so PKI cards here cover revocation *failure modes* (soft-fail, Must-Staple, short-lived certs as the alternative) and chain/trust-store/CA-hierarchy architecture instead; mTLS mentioned only as the consumer of workload identity.
- `Kubernetes` 07 Security: no RBAC/Role/RoleBinding mechanics, no Istio PeerAuthentication/AuthorizationPolicy; K8s cards here are about projected SA tokens as OIDC credentials, per-pod vs node identity and federation trust policies.
- `CISSP_Cloud_K8s` 05: it already has "OAuth isn't authn", SAML/OAuth/OIDC one-line cloze, Kerberos KDC/TGT + clock sync + weakness, "what is workload identity federation", break-glass definition, JML privilege creep, access recertification, zero-trust three tenets. This deck instead covers the OIDC ID-token mechanics, Kerberos vs token contrast and delegation risk, federation *trust-policy* conditions (iss/sub/aud), break-glass *design*, mover-stage design and SCIM, the seven NIST 800-207 tenets and its components.
- `Linux_Internals_for_K8s_Security`: capabilities untouched.

**Checks.** `tools/check.py`: 0 errors, 0 warnings; all `back` fields ≤ 34 words. `guid: null` throughout. build.py not run.

## Abbreviations expanded

141 notes touched. First occurrence per note written as "full name (ABBR)"; skipped where already expanded, inside code/cloze deletions, or when the expansion would leak the answer (ABAC, LDAP expanded in back). NIST SP 800 expanded as Special Publication (SP). Left bare: SHA-256, SHA, UX, HR, DB, UID, CRLSets/CRLite, field names (NameID etc.).

- IdP → identity provider
- OIDC → OpenID Connect
- SAML → Security Assertion Markup Language
- JWT → JSON Web Token
- NIST → National Institute of Standards and Technology
- CA → certificate authority
- MFA → multi-factor authentication
- SSO → single sign-on
- AS → authorization server
- FIDO2 → Fast IDentity Online 2
- PEP → policy enforcement point
- PKCE → Proof Key for Code Exchange
- SP → service provider
- XML → Extensible Markup Language
- DPoP → Demonstrating Proof-of-Possession
- IAM → identity and access management
- OCSP → Online Certificate Status Protocol
- TOTP → time-based one-time password
- AAL3 → authenticator assurance level 3
- AAL1 → authenticator assurance level 1
- AAL2 → authenticator assurance level 2
- AAL → authenticator assurance level
- CSRF → cross-site request forgery
- JWS → JSON Web Signature
- LDAP → Lightweight Directory Access Protocol
- RP → relying party
- SAN → subject alternative name
- SVID → SPIFFE Verifiable Identity Document
- URI → uniform resource identifier
- VPN → virtual private network
- ABAC → attribute-based access control
- ACME → Automatic Certificate Management Environment
- CAEP → Continuous Access Evaluation Profile
- CRL → certificate revocation list
- CTAP → Client to Authenticator Protocol
- EDR → endpoint detection and response
- IAL1 → identity assurance level 1
- IAL2 → identity assurance level 2
- IAL3 → identity assurance level 3
- IAL → identity assurance level
- JIT → just-in-time
- JWE → JSON Web Encryption
- KDC → key distribution center
- OTP → one-time password
- PDP → policy decision point
- PII → personally identifiable information
- PIV → personal identity verification
- PKI → public key infrastructure
- RFC → Request for Comments
- SCIM → System for Cross-domain Identity Management
- SMS → short message service
- SPA → single-page application
- TPM → trusted platform module
- ZTA → zero trust architecture
- AiTM → adversary-in-the-middle
- BCP → best current practice
- BLE → Bluetooth Low Energy
- CDN → content delivery network
- CSR → certificate signing request
- DN → distinguished name
- FAL → federation assurance level
- HMAC → hash-based message authentication code
- HS256 → HMAC with SHA-256
- HSM → hardware security module
- JVM → Java virtual machine
- JWKS → JSON Web Key Set
- KDF → key derivation function
- LAN → local area network
- MDM → mobile device management
- NFC → near-field communication
- PBKDF2 → password-based key derivation function 2
- PSAT → projected service account token
- ROPC → resource owner password credentials
- RS256 → RSA with SHA-256
- SA → service account
- SIM → subscriber identity module
- SS7 → Signaling System No. 7
- SSRF → server-side request forgery
- TGT → ticket-granting ticket
- TTL → time-to-live value
- VLAN → virtual local area network
- W3C → World Wide Web Consortium
- XSS → cross-site scripting
- ZTNA → zero trust network access
- mTLS → mutual TLS
- SPIFFE → Secure Production Identity Framework for Everyone
- SPIRE → SPIFFE Runtime Environment
- RS → resource server
- PAP → policy administration point
- PIP → policy information point
- EKU → extended key usage
- ReBAC → relationship-based access control
- FIPS → Federal Information Processing Standards
- CN → common name
- WebAuthn → Web Authentication
- L7 → Layer 7
- IMDSv2 → instance metadata service version 2
