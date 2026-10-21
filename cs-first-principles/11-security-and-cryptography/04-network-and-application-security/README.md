# Network and Application Security

> **Layer:** [11 Security and Cryptography](../README.md) › Network and application security
> **Children:** [Authentication](authentication.md) · [Web security](web-security.md) · [Network attacks and defenses](network-attacks-and-defenses.md) · [Software supply chain security](software-supply-chain-security.md)

## What this area is about

Most attacks arrive over a network and target an application: a login form, a web page, an exposed service, a routing protocol. This area asks how parties prove who they are to each other across a network, how applications that process untrusted input from anywhere in the world stay in control, how the network's own protocols, mostly designed in a cooperative era, are attacked and defended, and how the code an application is built from can be trusted.

The unifying idea is **never trust input or origin without verification**. The Internet delivers packets from anyone, claiming to be from anyone; web pages mix code and data from many sources in one browser; users can be tricked into acting for attackers. Each child applies the same remedy in a different place: authenticate the party (authentication), keep untrusted data from being interpreted as code or as authority (web security), and authenticate or filter traffic that the network itself does not (network defences), and verify where the code came from and how it was built (supply chain security).

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Authentication](authentication.md) | Proving identity: passwords, multi-factor, public-key credentials, sessions and federated login | Hashing, public-key cryptography |
| [Web security](web-security.md) | The browser's security model and the classic application attacks: injection, cross-site scripting, request forgery | Authentication, access control, Transport Layer Security (TLS) |
| [Network attacks and defenses](network-attacks-and-defenses.md) | Spoofing, interception, hijacking and denial of service at network layers, and firewalls, encryption and filtering against them | Networking protocols, cryptography |
| [Software supply chain security](software-supply-chain-security.md) | Trusting the dependencies, toolchain and build that produce the code: signatures, provenance, reproducible builds, bills of materials | Hashes, signatures, authentication |

```
   user  --(authentication: who are you?)-->  application
                                               |   web security: is this input code?
                                               |   is this request really the user's?
   network path  <-- network attacks: spoofing, hijacking, flooding
                 <-- defences: encryption, filtering, authenticated routing
```

Authentication comes first because both other topics depend on knowing who is acting. Web security then covers the dominant application platform, where most authentication tokens live and most injection bugs occur. Network attacks and defences cover the layer underneath, where the attacker manipulates delivery itself. Supply chain security comes last because it turns the same question, "is this input trustworthy?", onto the application's own code: dependencies and updates are input that runs with full privilege, and their defences reuse authentication (of maintainers and builders) and authenticated delivery. In practice the three meet constantly: a stolen session cookie (web) is an authentication failure; a hijacked route (network) is defeated only if the application authenticates the server with TLS.

## Connections to sibling areas

- **[Security principles](../01-security-principles/README.md):** threat modeling identifies trust boundaries, and here they are concrete: the network edge, the browser's origins, the login form.
- **[Cryptography](../02-cryptography/README.md):** supplies password hashing, signatures for public-key credentials and software artifacts, and the TLS protocol that most network defences ultimately rely on.
- **[System security](../03-system-security/README.md):** authentication supplies the identities that access control checks; the browser's process sandbox is isolation; injection attacks are close relatives of memory corruption, since both make data act as code; sandboxing build steps limits what a malicious dependency can reach.

## Connections across layers

This area sits on top of [08 Networking](../../08-networking/README.md): [Internet Protocol (IP) addressing](../../08-networking/03-network-layer/ip-addressing-and-forwarding.md), [Border Gateway Protocol (BGP) routing](../../08-networking/03-network-layer/internet-routing-and-bgp.md), [Transmission Control Protocol (TCP)](../../08-networking/04-transport-layer/udp-and-tcp.md), [Domain Name System (DNS)](../../08-networking/05-application-layer/naming-and-dns.md) and [Hypertext Transfer Protocol (HTTP)](../../08-networking/05-application-layer/http-and-the-web.md) are each attack surfaces with their own hardened variants. Injection attacks target [Structured Query Language (SQL)](../../09-data-management/01-data-models/relational-algebra-and-sql.md) and other interpreters built from [parsers](../../06-programming-languages/03-compilers/lexing-and-parsing.md). Usability findings from [human-computer interaction](../../14-human-and-visual-computing/01-human-computer-interaction/usability-evaluation.md) decide whether authentication and warnings work in practice. [Large-scale systems](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md) absorb denial-of-service attacks with the same tools that handle load spikes. [Software engineering](../../12-software-engineering/README.md) practices such as [testing](../../12-software-engineering/03-quality/testing.md) and [code review](../../12-software-engineering/03-quality/static-analysis-and-code-review.md) find these flaws before deployment, and [build and delivery pipelines](../../12-software-engineering/04-operations/build-and-continuous-delivery.md) are where supply chain defences run. Thompson's trusting-trust attack reaches down to [compilers](../../06-programming-languages/03-compilers/README.md).

## Cross-cutting threads

- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): authenticate every party and validate every input.
- [The end-to-end argument](../../CROSS-CUTTING.md#the-end-to-end-argument): network filtering helps, but only endpoint authentication and encryption are sufficient.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): injection happens when data and code share a representation.
- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): DNS and BGP attacks redirect names and addresses.
- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): rate limiting and adaptive filtering against floods.
