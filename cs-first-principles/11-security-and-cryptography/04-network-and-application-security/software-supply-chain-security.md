# Software Supply Chain Security

> **Layer:** [11 Security and Cryptography](../README.md) › [Network and application security](README.md)
> **Builds on:** [Security design principles](../01-security-principles/security-design-principles.md), [Hash functions and message authentication codes](../02-cryptography/hash-functions-and-macs.md), [Public-key cryptography](../02-cryptography/public-key-cryptography.md), [Compilers](../../06-programming-languages/03-compilers/README.md), [Linking and loading](../../06-programming-languages/04-runtime-systems/linking-and-loading.md)
> **Enables:** [Build and continuous delivery](../../12-software-engineering/04-operations/build-and-continuous-delivery.md), [Version control](../../12-software-engineering/02-process/version-control.md), [Static analysis and code review](../../12-software-engineering/03-quality/static-analysis-and-code-review.md)

## Essence

The program you run is not the source you reviewed. Between them stand third-party packages, their maintainers, a registry, a compiler, a build server, a signing key and an update channel, and any of them can insert code that runs with your program's privileges. Software supply chain security is the work of making that chain **verifiable**: knowing what went into an artifact (a bill of materials), how it was built and by whom (provenance), and whether the binary really corresponds to the source (reproducible builds). Attackers favour the chain because one upstream compromise reaches every downstream user through the update mechanism they trust most.

## Core tenets

1. **You cannot fully trust code you did not create, including your tools.** Ken Thompson's Turing Award lecture "Reflections on Trusting Trust" (1984) described a compiler modified to insert a backdoor into the login program and to re-insert the same modification whenever it compiled a clean compiler source. After one bootstrap the backdoor lives only in binaries, invisible to source review. Trust is transitive, so a program's trusted computing base includes its whole toolchain.

2. **Trust can be checked with independent, diverse paths.** Thompson's attack needs every path to the binary to be compromised. Wheeler's *diverse double-compiling* (2005) rebuilds a compiler's source with an unrelated second compiler and checks that the results match bit for bit; agreement shows the binary matches its source unless both toolchains are compromised alike. The principle is redundancy without a shared failure mode.

3. **Package registries resolve names, and names can be hijacked.** A dependency is fetched by name and version, and installing it often runs its scripts at once. *Typosquatting* uses near-miss names. *Dependency confusion* (Birsan, 2021) publishes a public package named like a company's internal one with a higher version, which misconfigured resolvers prefer. Defences are namespaced names, lockfiles pinning each dependency's version *and* content hash, and private registries that never fall back to public ones.

4. **Maintainers are part of the attack surface.** Most open-source packages have one or a few volunteer maintainers. Attackers steal their credentials, take over abandoned packages (in the 2018 event-stream incident a new maintainer added code targeting a cryptocurrency wallet), or earn trust over years. Multi-factor authentication helps, but the deeper problem is economic: critical infrastructure rests on unpaid work.

5. **Signatures prove who signed, not that the content is good.** A signature detects tampering *after* signing. In the SolarWinds attack, disclosed in December 2020, intruders implanted the SUNBURST backdoor during the build of the Orion network-management product; the update was signed with the vendor's genuine key and installed by roughly 18,000 customers. Sigstore (2021) makes signing cheap with short-lived certificates tied to an OpenID Connect identity, and records every signature in a public transparency log so misuse is visible.

6. **Provenance records how an artifact was built.** A provenance attestation is a signed statement of which source revision, build steps, builder and dependencies produced an artifact. The Supply-chain Levels for Software Artifacts (SLSA) framework grades build integrity; higher levels require a hardened, isolated build service that generates provenance the build steps cannot forge, so a compromised developer machine cannot produce an artifact that verifies.

7. **Reproducible builds let anyone check the binary against the source.** If the same source and toolchain always yield bit-identical output, independent rebuilders can confirm a published binary, and a tampered build server is caught by disagreement. This requires removing nondeterminism such as embedded timestamps, file ordering and build paths; Debian and other distributions have made most packages reproducible.

8. **The xz-utils backdoor (2024) shows the gap between repository and release.** Over about two years a contributor using the name "Jia Tan" became co-maintainer of the xz compression library, then shipped versions 5.6.0 and 5.6.1, in which a build script present only in the release tarballs, not the Git repository, extracted a payload hidden in binary test files. On some Linux distributions the library is loaded into the Secure Shell (SSH) server, and the payload let the holder of the attacker's key run commands. Andres Freund caught it in March 2024 by investigating a half-second login slowdown, before most stable releases shipped it. Checking that release artifacts match the reviewed repository would have exposed it.

9. **A software bill of materials (SBOM) answers "are we affected?"** An SBOM lists every component and version inside an artifact, in a standard format such as Software Package Data Exchange (SPDX) or CycloneDX. When the Log4Shell flaw in the Log4j logging library was disclosed in December 2021, many organisations spent weeks finding where they used it, often several dependency levels deep. An SBOM does not prevent compromise; it speeds response.

## Key concepts

| Term | Meaning |
|---|---|
| Trusting trust attack | Self-reproducing backdoor in a toolchain binary, absent from all source |
| Typosquatting | Publishing malicious packages under names similar to popular ones |
| Dependency confusion | Public package shadowing a private one with the same name |
| Lockfile | Recorded exact versions and hashes of every resolved dependency |
| Provenance | Signed record of the source, builder and steps that produced an artifact |
| SLSA | Framework of increasing build-integrity requirements |
| Reproducible build | Build whose output is bit-identical given the same inputs |
| SBOM | Inventory of the components and versions in an artifact |

## How it fits

- **Below:** artifacts are named by [hashes](../02-cryptography/hash-functions-and-macs.md) and signed with [public-key signatures](../02-cryptography/public-key-cryptography.md); toolchain attacks run through [compilers](../../06-programming-languages/03-compilers/README.md) and [linking](../../06-programming-languages/04-runtime-systems/linking-and-loading.md); defences apply [least privilege and defence in depth](../01-security-principles/security-design-principles.md).
- **Above:** [build and continuous delivery](../../12-software-engineering/04-operations/build-and-continuous-delivery.md) pipelines generate provenance and enforce pinning; [version control](../../12-software-engineering/02-process/version-control.md) histories are hash-linked and can be signed; [code review](../../12-software-engineering/03-quality/static-analysis-and-code-review.md) of dependency changes is the human check.
- **Siblings:** [authentication](authentication.md) protects maintainer and registry accounts; [web security](web-security.md) faces the same problem with third-party scripts; [network attacks](network-attacks-and-defenses.md) explain why update channels must be authenticated, not just encrypted.

## Common misconceptions

- **"Open source is safe because anyone can read it."** Few read dependency code, and the shipped artifact may not match the repository.
- **"Signed means safe."** A signature proves origin, not intent; a compromised build is signed like a clean one.
- **"Pinning a version is enough."** Without a content hash, a registry or mirror can serve different bytes under the same version.

## Go deeper

- Thompson, "Reflections on Trusting Trust", *Communications of the ACM* (1984): the founding argument, in three pages.
- Wheeler, "Countering Trusting Trust through Diverse Double-Compiling", Annual Computer Security Applications Conference (2005).
- Torres-Arias et al., "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes", USENIX Security (2019): verifying every step of a supply chain.
- The SLSA specification (slsa.dev) and the Reproducible Builds project (reproducible-builds.org): current practice.
