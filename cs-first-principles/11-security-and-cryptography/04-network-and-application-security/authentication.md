# Authentication

> **Layer:** [11 Security and Cryptography](../README.md) › [Network and application security](README.md)
> **Builds on:** [Hash functions and message authentication codes](../02-cryptography/hash-functions-and-macs.md), [Public-key cryptography](../02-cryptography/public-key-cryptography.md), [Access control](../03-system-security/access-control.md), [Secure protocols and Transport Layer Security](../02-cryptography/secure-protocols-and-tls.md)
> **Enables:** [Web security](web-security.md), [Network attacks and defenses](network-attacks-and-defenses.md), [Cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md)

## Essence

Authentication is establishing that a party is who it claims to be, so that access-control decisions and audit records can be tied to a real principal. It rests on evidence of three kinds: something you **know** (a password), something you **have** (a phone, a hardware key holding a private key), and something you **are** (a fingerprint). Over a network, authentication is always a protocol, and the attacker can watch, replay, relay or impersonate. The strongest modern methods are therefore **challenge-response protocols with public-key credentials bound to the site's origin**, which never send a reusable secret and cannot be relayed by a phishing site. After the initial check, a **session** (a cookie or token) carries the authentication forward, and protecting it is as important as the login itself.

## Core tenets

1. **Passwords fail in predictable ways.** People choose low-entropy, reused passwords; servers leak their password databases; phishing pages collect them; and attackers try leaked credentials on other sites (credential stuffing). Mitigations are server-side: store only salted, slow hashes (Argon2, scrypt, bcrypt), rate-limit and monitor guessing, check new passwords against known-breached lists, and allow long passphrases and password managers. Current NIST (US National Institute of Standards and Technology) guidance (SP 800-63B) drops forced periodic changes and composition rules, which pushed users toward predictable patterns.

2. **Never send a reusable secret if you can prove knowledge instead.** In challenge-response, the verifier sends a fresh random challenge and the claimant returns a function of the challenge and its secret, such as a signature. An eavesdropper learns nothing reusable, and a replayed response fails because the next challenge differs. This is the pattern behind Kerberos tickets, Secure Shell (SSH) public-key login, and modern hardware keys.

3. **Multi-factor authentication works only if the factors fail independently.** Combining a password with a second factor defeats attacks on passwords alone. But one-time codes sent by SMS (Short Message Service) can be intercepted by SIM (subscriber identity module) swapping, and both SMS and authenticator-app codes can be typed into a phishing page and relayed in real time. Push approvals fall to prompt flooding.

4. **Origin-bound public-key credentials resist phishing.** FIDO2/WebAuthn (from the FIDO, Fast IDentity Online, Alliance and the World Wide Web Consortium) creates a key pair per website on the user's device or security key; the browser includes the site's origin in what is signed, so a credential for `bank.example` cannot be used by `bank-example.evil`. Nothing reusable is stored on the server (only the public key), and the private key never leaves the device. Passkeys are such credentials synchronised across a user's devices.

5. **Sessions are bearer tokens and must be protected like passwords.** After login, the server issues a session identifier, usually in a cookie; anyone holding it is the user. Tokens must be long and random, sent only over Transport Layer Security (TLS), marked `HttpOnly` (not readable by scripts) and `Secure`, given a `SameSite` policy, rotated on login (to prevent session fixation) and expired. Signed tokens such as JSON (JavaScript Object Notation) Web Tokens (JWTs) avoid server-side lookup, but then cannot be revoked before they expire without extra machinery.

6. **Federated login separates identity providers from applications.** OAuth 2.0 is a protocol for *delegated authorisation*: a user lets an application access a resource on their behalf, receiving an access token. OpenID Connect adds *authentication* on top, with a signed identity (ID) token stating who the user is. Using raw OAuth access tokens as proof of identity has caused real vulnerabilities. Single sign-on concentrates risk in the identity provider but lets one strong authentication protect many services.

7. **Machines authenticate too, and their secrets leak.** Services authenticate to each other with API (Application Programming Interface) keys, client certificates (mutual TLS) or short-lived tokens from a workload identity system. Long-lived static keys committed to source repositories or left in configuration are a leading cause of cloud breaches; short-lived, automatically rotated credentials limit the damage.

8. **Recovery is part of authentication.** Every system needs a way to recover a lost password or device, and that path is often weaker than the main one: security questions with guessable answers, support staff who can be socially engineered, an email account that is itself weakly protected. An account is only as strong as its weakest recovery route.

## Key concepts

| Term | Meaning |
|---|---|
| Authentication factor | Evidence of identity: knowledge, possession or inherence |
| Credential stuffing | Trying leaked username–password pairs on other services |
| Challenge-response | Proving possession of a secret by answering a fresh challenge |
| MFA | Multi-factor authentication: requiring two or more independent factors |
| WebAuthn / passkey | Origin-bound public-key credential standard / synchronised credential |
| Session token | Bearer secret representing an authenticated session |
| Session fixation | Forcing a victim to use a session identifier the attacker knows |
| OAuth 2.0 | Delegated authorisation via access tokens |
| OpenID Connect | Authentication layer on OAuth 2.0 using signed ID tokens |

## How it fits

- **Below:** password storage uses [slow hashes](../02-cryptography/hash-functions-and-macs.md); passkeys and certificates use [signatures](../02-cryptography/public-key-cryptography.md); sessions travel over [TLS](../02-cryptography/secure-protocols-and-tls.md) and the [Hypertext Transfer Protocol (HTTP)](../../08-networking/05-application-layer/http-and-the-web.md); human limits on memory and attention come from [perception and cognition](../../14-human-and-visual-computing/01-human-computer-interaction/perception-and-cognition.md).
- **Above:** [cloud](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) identity and access management, [privacy regulation](../../15-computing-in-context/law-privacy-and-policy.md) of personal data, and the [usability](../../14-human-and-visual-computing/01-human-computer-interaction/usability-evaluation.md) of login flows.
- **Siblings:** [web security](web-security.md) protects the session after login; [network attacks](network-attacks-and-defenses.md) such as interception are what challenge-response and TLS defeat; [access control](../03-system-security/access-control.md) consumes the identity this produces.

## Common misconceptions

- **"Any second factor stops phishing."** Codes and push prompts can be relayed; only origin-bound credentials such as WebAuthn resist real-time phishing.
- **"OAuth is a login protocol."** It is for authorisation; authentication needs OpenID Connect or equivalent checks.
- **"Complex password rules make users safer."** They produce predictable variations and reuse; length, breach checks and password managers help more.

## Go deeper

- Anderson, *Security Engineering* (3rd ed., 2020): chapters on passwords and authentication protocols.
- Bonneau, Herley, van Oorschot and Stajano, "The Quest to Replace Passwords", IEEE Symposium on Security and Privacy (2012).
- NIST Special Publication 800-63B, *Digital Identity Guidelines: Authentication and Lifecycle Management* (current revision).
- Needham and Schroeder, "Using Encryption for Authentication in Large Networks of Computers", *Communications of the ACM* (1978): the protocol behind Kerberos, and a lesson in protocol flaws.
