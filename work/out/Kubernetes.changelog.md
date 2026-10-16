# Kubernetes changelog

Sources: Kubernetes_in_Action (64 notes) + Golden_Kubestronaut (225 notes) = 289 notes in.
Output: **252 notes** in one deck `Kubernetes` with 12 concept subdecks (exam labels moved to `source` and `Exam::*` tags).

| Subdeck | Notes |
|---|---|
| 01 Architecture & Control Plane | 18 |
| 02 Workloads & Pods | 24 |
| 03 Scheduling, Resources & Autoscaling | 15 |
| 04 Networking & Services | 18 |
| 05 Storage | 7 |
| 06 Config & Secrets | 5 |
| 07 Security & Hardening | 39 |
| 08 Cluster Operations & Troubleshooting | 16 |
| 09 Observability | 35 |
| 10 Service Mesh & Cilium | 28 |
| 11 Cloud Native Ecosystem | 26 |
| 12 Linux Admin (LFCS) | 21 |

## Summary
- Kept/rewritten (original guid): 222
- Merged away: 20 source notes folded into other cards
- Deleted: 47
- Split-off cards (guid null): 26
- New cards (contrast/pitfall, guid null): 4
- Analogies: 62 cards carry one (sources had 0); ~24%
- Every card rewritten for atomicity and short answers; enumerations (control-plane parts, Service types, QoS, access modes, PSS levels, audit levels, Alertmanager, etc.) became per-item clozes.
- LFCS, Prometheus (PCA), OpenTelemetry (OTCA), Istio (ICA) and Cilium (CCA) kept as their own concept subdecks; GitOps/Argo/Backstage/Kyverno/platform cards that duplicate the Platform Engineering deck were deleted, unique ones kept in `11 Cloud Native Ecosystem`.

## Merges (kept card ← merged notes)
- KIA#44 "Explain the watch mechanism and reconciliation loop." ← GK#55 "What is the reconciliation loop / controller pattern?"; GK#145 "What is the difference between the desired state and the observed/actu"; GK#148 "What does "reconciliation is continuous, not one-shot" mean?"
- GK#54 "What is the difference between imperative and declarative management?" ← GK#198 "What does "declarative resource management" mean for platforms?"
- KIA#62 "What is a Custom Resource Definition (CRD)?" ← GK#59 "What is a CRD?"
- KIA#63 "What is the Operator pattern?" ← GK#58 "What is an Operator in Kubernetes?"; GK#204 "In platform work, why prefer Operators/controllers for day-2 automatio"
- KIA#11 "How does a ReplicaSet differ from a ReplicationController?" ← KIA#10 "What does a ReplicationController do?"
- KIA#32 "Compare the RollingUpdate and Recreate deployment strategies." ← GK#223 "What deployment strategies does the built-in Deployment support?"
- KIA#12 "What is a DaemonSet?" ← GK#20 "What is the difference between a DaemonSet and a Deployment for placem"
- KIA#13 "Difference between a Job and a CronJob?" ← GK#224 "What is the difference between a Job and a CronJob?"
- KIA#56 "LimitRange vs ResourceQuota?" ← GK#17 "What does a ResourceQuota vs a LimitRange control?"
- KIA#58 "HPA vs Vertical Pod Autoscaler (VPA) vs Cluster Autoscaler?" ← GK#50 "Name the three autoscalers and what each scales."
- KIA#45 "What networking guarantee must a Kubernetes pod network satisfy?" ← GK#10 "In CKA cluster networking, what must every CNI plugin guarantee?"
- GK#60 "What are the main Kubernetes Service types?" ← KIA#15 "What does a ClusterIP Service provide?"
- KIA#50 "What are the three stages a request passes through at the API server?" ← GK#66 "What are the four phases of the request path the API server enforces?"
- GK#39 "What are admission controllers and the two webhook types?" ← GK#185 "How do mutate and validate rules order during admission?"
- GK#63 "What is the Kubernetes threat model framework often referenced (the 4A" ← GK#64 "What are the main trust boundaries in a Kubernetes cluster?"
- GK#43 "How do you minimize a container image's attack surface?" ← GK#72 "What categories of controls reduce container-layer risk?"
- GK#129 "How does Cilium's identity-based security differ from IP-based?" ← GK#135 "What is a Cilium Endpoint and Identity?"

## Deletions
- GK#34 "What is image signing with Cosign and why does it matter?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Cosign, keyless signing)
- GK#35 "What is an SBOM and why generate one?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (SBOM, formats)
- GK#68 "What is SLSA?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (SLSA)
- GK#183 "How does Kyverno verify image signatures?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Kyverno verifyImages)
- GK#45 "What is OPA Gatekeeper and how does its policy model work?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Gatekeeper ConstraintTemplate/Constraint)
- GK#176 "What is Kyverno and how does it differ from OPA/Gatekeeper?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Kyverno vs OPA/Gatekeeper)
- GK#177 "What are Kyverno's rule types?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Kyverno rule types)
- GK#180 "What is background scanning in Kyverno?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Kyverno background scan)
- GK#187 "What are Kyverno's controllers in v3.x?": Kyverno v3 internal controller split: version-specific internals, no work impact
- GK#56 "What is Helm and what is a chart?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Helm chart/release)
- GK#142 "What are the four OpenGitOps principles?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (four OpenGitOps principles)
- GK#143 "Push-based vs pull-based deployment, and which is GitOps-native?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (push vs pull deployment)
- GK#144 "What is drift and how does GitOps handle it?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (configuration drift)
- GK#146 "Why is Git the source of truth advantageous for operations?": generic 'Git as source of truth benefits' list; overlaps GitOps definition card and Platform Engineering deck
- GK#150 "What are common GitOps tools?": tool-name enumeration (Argo CD/Flux/…); no retrievable insight, Platform Engineering covers tools
- GK#151 "What is a key challenge GitOps must solve around secrets?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (secrets in GitOps repos)
- GK#208 "What is Argo CD and its core object?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Argo CD Application)
- GK#209 "What do Argo CD sync status and health status mean?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Argo CD sync vs health status)
- GK#210 "What is the "app of apps" pattern in Argo CD?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (app of apps)
- GK#211 "What are Argo CD sync waves and hooks?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (sync waves/hooks)
- GK#212 "What does auto-sync with self-heal and prune do in Argo CD?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (auto-sync prune/self-heal)
- GK#218 "What is an Argo CD Project (AppProject)?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (AppProject)
- GK#215 "What is Argo Rollouts?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Argo Rollouts definition)
- GK#152 "What problem does Backstage solve?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Backstage: what is Backstage)
- GK#153 "What are the core entity kinds in the Backstage Software Catalog?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Backstage: catalog entity kinds)
- GK#154 "What is the catalog-info.yaml file?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Backstage: catalog-info.yaml)
- GK#155 "What is the Scaffolder / Software Templates feature?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Backstage: Scaffolder)
- GK#156 "What is TechDocs?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Backstage: TechDocs)
- GK#158 "What is the ownership model in the catalog?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Backstage: spec.owner)
- GK#159 "How does Backstage discover and keep the catalog up to date?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Backstage: catalog ingestion)
- GK#160 "What is the relationship between System, Component, and API entities?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Backstage: System/Component/API/Domain)
- GK#157 "How is Backstage extended?": Backstage plugins: generic marketing-level statement; Backstage depth owned by Platform Engineering
- GK#161 "Why does Backstage matter for platform engineering?": Backstage-for-platform-engineering: restates IDP/portal cards owned by Platform Engineering
- GK#189 "What is a "golden path" / paved road?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (golden path)
- GK#190 "What does "treat the platform as a product" mean?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (platform as a product)
- GK#191 "What is an Internal Developer Platform (IDP)?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Internal Developer Platform)
- GK#192 "What does Team Topologies contribute to platform engineering?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Team Topologies platform team)
- GK#195 "What is Crossplane and why does it matter for platforms?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (Crossplane)
- GK#196 "What is the "thinnest viable platform" idea?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (thinnest viable platform)
- GK#206 "How should a platform expose infrastructure provisioning safely?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (self-service provisioning abstractions (Crossplane/Operators))
- GK#202 "How do you measure a platform's success beyond DORA?": duplicate of Platform Engineering deck (owner of GitOps/Argo/Backstage/policy-as-code/IDP), which covers it in more depth (platform success metrics)
- GK#193 "What are the DORA metrics?": DORA metrics: already covered in Agile Architecture / Architect Craft / Platform Engineering decks
- GK#199 "What does developer experience (DevEx) optimize for, and what's the en": DevEx/cognitive load: duplicate of Platform Engineering (IDP) cognitive-load cards
- GK#200 "What does "secure by default" mean in a platform context?": 'secure by default' platform slogan: marketing-level, no retrievable fact ('CNPA exam phrasing cue')
- GK#201 "What platform capabilities map to observability/conformance?": vague capability list (observability/conformance) with no single answer
- GK#203 "What does the CNPE certification add over CNPA?": exam-meta: what the CNPE certification format is
- GK#138 "What is XDP and where does it run?": XDP internals: owned by Linux/Networking decks (eBPF internals); Cilium eBPF card kept

## New contrast / pitfall cards (split-derived ones are counted under splits)
Labels vs annotations; taints vs node affinity; quota-without-requests rejection; liveness probe on a dependency (cascading restarts); default-deny egress breaks DNS; CrashLoopBackOff `logs --previous`; histogram vs summary; node_exporter vs kube-state-metrics vs metrics-server; init containers; Secrets are not encrypted by default (split).

## Product-content review
Reviewed card by card: no product-catered cards found (tools present are open-source subjects or short examples in `extra`); nothing deleted, rewritten or scrubbed.
