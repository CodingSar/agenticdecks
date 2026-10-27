# Pipeline Security & SOC Monitoring — changelog

New deck (Oct 2026), written from scratch to `work/WRITER_BRIEF.md`. 163 notes / 173 cards, 12 subdecks, 42 analogies (26%), 5 cloze notes, 2 hand-drawn SVG diagrams (`media/psoc_*.svg`).

## Scope
How CI/CD pipelines are attacked and defended, and how a Security Operations Center (SOC) monitors them. Built for a platform architect who has to hand a SOC a concrete set of pipeline detection use-cases.

## Subdecks
1. **Why Pipelines Are Targets** — blast radius, the four stages, SLSA threat groups, OWASP CI/CD Top 10, Poisoned Pipeline Execution; SolarWinds, Codecov and xz as *lessons*, not history trivia.
2. **Source & Dependencies** — branch protection, signed commits vs author spoofing, dependency confusion, typosquatting, lockfiles, install scripts, push protection, fork pull requests.
3. **Build & Workflow Attacks** — script injection, pwn requests, SHA pinning, cache poisoning, log leaks, hermetic and reproducible builds, trusted/untrusted stage split.
4. **Identity & Secrets in Pipelines** — OIDC workload federation and `sub`-claim trust policies, job-scoped tokens, environment-scoped secrets, secrets managers, dynamic secrets, deploy keys.
5. **Runners & Build Infrastructure** — ephemeral vs persistent runners, self-hosted on public repos, segmentation and egress, Docker socket, metadata endpoint, runner tokens.
6. **Artifacts, Registries & Deploy Gates** — digests vs tags, immutability, admission verification (who signed, not just that it is signed), pull-through caches, GitOps, drift, promotion, break-glass.
7. **SOC Basics for Pipelines** — detection use-case definition and lifecycle, MITRE ATT&CK mapping, SIEM vs SOAR, detection-as-code, Sigma, fidelity vs volume, MTTD/MTTR, co-ownership.
8. **Telemetry Sources** — SCM audit logs, CI job events, Kubernetes audit, admission denials, registry, cloud audit, secrets-manager access, eBPF runtime, correlation keys, log integrity.
9. **Detection Use-Cases: Source & Build** — 15 concrete rules (branch protection weakened, workflow changed by outsider, force-push, new PAT/deploy key, fork run with secrets, token in logs, new egress, credential-file reads, fresh dependency, pin loosened, bulk secret reads, new runner…).
10. **Detection Use-Cases: Deploy & Runtime** — 14 rules (digest never pushed by pipeline, admission denial, OIDC role with no matching run, credential from non-runner IP, manual change in GitOps namespace, privileged pod from deploy identity, tag overwrite, shell in prod container, SBOM hit, GitOps controller changed…).
11. **Triage, Response & Recovery** — first triage question, containment order, pause-don't-delete, scoping via provenance, "runner is lost", evidence capture, SOAR-safe actions, downstream notification, postmortem.
12. **Maturity & Governance** — NIST SSDF vs SLSA, CIS supply-chain guide, EU CRA, coverage measurement, purple-team exercises, inventory, golden path, exceptions, two-person rule, AI coding agents as untrusted automation.

## Deliberately left out
- Definitions of Sigstore, Cosign, Fulcio, Rekor, SBOM formats, SLSA build levels, hermetic builds and in-toto: already in **Platform Engineering** `12 Supply-Chain Security`; this deck references them and adds the SOC angle only.
- Kubernetes audit-log flags and levels, Falco rule syntax, Pod Security levels: **Kubernetes** and **Linux Internals for K8s Security**.
- SIEM/SOAR product comparisons, vendor features and pricing (product-content rule).
- Generic application security (OWASP Web Top 10, SAST internals) and generic incident-response frameworks: **CISSP** deck covers the frameworks.

## Overlap check
Grepped existing decks for SLSA, Sigstore, SBOM, SIEM, Falco, OIDC, audit log, cache poisoning, typosquatting. The only near-neighbours were the Platform Engineering supply-chain subdeck (definitions, avoided as above), one CISSP card "why is the CI/CD pipeline a high-value target" (this deck's version asks the *blast-radius* question and goes one level deeper rather than repeating it), and the Kubernetes KCSA supply-chain-vectors card.
