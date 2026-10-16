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
