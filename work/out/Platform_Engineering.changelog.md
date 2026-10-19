# Platform Engineering — changelog

**Notes in:** 224 from platform_gitops (116), iac_control_plane_abstraction (30), idp_platform_engineering (39), policy_as_code_supply_chain_security (39), plus 18 generic GitOps/fleet/tenancy notes moved in from STACKIT_Hybrid_Cloud_Architect (16 kept, 2 merged). Total 242 in.
**Notes out:** 242 (216 keep an original guid, 26 new with `guid: null`).
**Subdecks (13):** 01 GitOps Principles · 02 Argo CD · 03 Flux · 04 Terraform & IaC · 05 Ansible & Config Management · 06 Crossplane & Control Planes · 07 Helm · 08 Operators & Controllers · 09 Platform as a Product · 10 Developer Portals & Workload Specs · 11 Policy as Code · 12 Supply-Chain Security · 13 Fleet & Multi-Tenancy.

## Merges (20 notes folded into another)
- Ansible idempotency `IY:>kwR8Ls` → IaC idempotency `M&Z`Q>#VAH` (Ansible point moved to extra)
- "What is Terraform state file / why sensitive" `n^4v;RTE&I` → state security `B*g1ovz}R^`
- Terraform provider `NN@ar@B.uQ` + module `AG7aR3fQ{7` → resource/data source/module/provider cloze `kIrh:BbVbo`
- Terraform workspaces `zD!+jP!5/(` → workspaces + caveat `g~A]T@Q:+r`
- OpenTofu `ce4gwlVG8L` + BSL vs MPL licensing `N.?%hd9Ixo` → "Why does OpenTofu exist?" `fj((&=2sOu`
- Terraform drift `r,=gG6[c:H` → configuration drift `x/46/>H*sp`
- Crossplane vs Terraform reconciliation `kPu^hKU+cV` → Crossplane vs Terraform `tG.sv1bw_5`
- GenerationChangedPredicate `Qe$Qa)]A{&` → "don't write status unconditionally" `OA2UD88Cte` (extra)
- Scaffolder & golden paths `O<Ww:r<=v3` → Scaffolder `b;ntM|JEi_`
- Why RHDH over Backstage `Q6>>Y.,Z=Y` → RHDH `h$_.,<aOhT`
- Humanitec "integrate and embrace" `zHLD==NqHu` → Humanitec Orchestrator vs Backstage/Argo `$-R~]8E(S`
- Gatekeeper Constraint `D!:`OM$#nn` → ConstraintTemplate/Constraint cloze `gKy`M`rmz_`
- Grype `wEtlT6%$6v` → Syft/Grype cloze `j1N*DpRiE9`
- ACS admission `B.<1X0qthI` + ACS vs SLSA chain `P;F.H7*6)P` → ACS scope `q4.//zAEBE`
- "Single admission check unifying signatures/attestations" `n2dGl4l}D=` → end-to-end supply-chain cloze `vY5yua??Sw`
- STACKIT Argo CD multitenancy `pk:v*k@ERi` → AppProject `k^Tn<8UP,b` (tenancy pattern in extra)
- STACKIT Argo CD vs Flux `Q@mOM@H/ca` → Argo CD vs Flux `h(.0Wca=ZM`
- Terraform state locking (iac) `g?Z?234I?3` kept as the S3-locking half of the split locking card.

## Moved in from STACKIT (generic, no STACKIT specifics)
Soft vs hard tenancy, namespace-per-tenant mechanisms, what namespaces don't isolate, vCluster, Capsule/HNC, tenancy decision matrix, shared ingress/monitoring tenancy, reasons for multiple clusters, hub/management cluster, push vs pull fleet GitOps, Helm/Kustomize layering, multi-cluster networking options, data gravity, upgrade rings (→ 13 Fleet & Multi-Tenancy); Terraform vs GitOps boundary (→ 04); ApplicationSets for fleets (→ 02).

## Deletions (6)
- `rRm6;^h_5E` "What is Terraform?" — trivial definition, covered by the Terraform cards.
- `w)|AJq1G?/` informers/cache/workqueue — client-go implementation detail, owned by the Go deck.
- `h@~;z;l0y.` controller-runtime Reconcile return values — Go implementation detail (Go deck).
- `N|*E?uL~Us` For/Owns/Watches builder — controller-runtime code (Go deck).
- `IaPBd2^Y+` RHDH marketplace's three plugin categories — vendor taxonomy, no work impact.
- `qdssE2ztt5` Red Hat Developer Lightspeed — product marketing.

## Splits
16 notes split into 25 additional cards (e.g. Terraform locking → why/how; Helm hooks → annotations/pitfall; HelmRelease remediation/drift; spec-status/status subresource; vCluster → what/gives/doesn't/sweet spot; tenancy decision matrix → 4 cards; push vs pull fleet → 3; multi-cluster networking → 4). 1 new contrast card: Kyverno/Gatekeeper webhooks vs ValidatingAdmissionPolicy.
Enumerations turned into clozes (33 cloze notes): OpenGitOps principles, lifecycle meta-args, Helm terms, Flux/Argo components, operator capability levels, Ansible architecture, Backstage kinds, etc.

## Other
- Analogies: 48 notes, all new (sources had none), ~20%.
- Removed abbreviation-expansion noise, trimmed version trivia into `extra` (e.g. Helm 3.8 OCI GA, Helm 4 release date), added Helm 4 `--atomic` → `--rollback-on-failure` note, Crossplane v2 Claims note.

## Product-content review
Deleted (1):
- "Which commercial product is Score built to feed?" — vendor fact only (Humanitec product tie-in), nothing transferable

Rewritten to the vendor-neutral concept, product moved to `extra` as an example (10, guids kept):
- "Red Hat Ansible Automation Platform adds {{c1::Automation Controller}} (web UI/API, RBAC, scheduling), {{c2::Execution Environments}} (containerized Ansible runtimes) and {{c3::Automation Hub}} (curated, certified content)." → "A central Ansible controller (AWX and its downstream products) adds {{c1::a web UI/API with RBAC, scheduling and job history}} over the CLI, {{c2::execution environments}} (containerized, versioned Ansible runtimes) and {{c3::a curated content hub}} for approved roles and collections."
- "What is Red Hat Developer Hub (RHDH), and why pick it over vanilla Backstage?" → "Why do organisations adopt a packaged Backstage distribution instead of building on vanilla Backstage?"
- "How does RHDH load plugins differently from a classic Backstage build?" → "Backstage plugins: statically compiled vs <b>dynamic</b> loading?"
- "Humanitec Platform Orchestrator RMCD workflow: {{c1::Read}} the workload spec → {{c2::Match}} its dependencies to resource definitions → {{c3::Create}} the resources → {{c4::Deploy}} the workload." → "Platform orchestrator pattern: at deploy time it {{c1::reads}} the abstract workload spec → {{c2::matches}} each declared dependency to an environment-specific resource definition → {{c3::creates}} or updates those resources → {{c4::deploys}} the workload with the generated configuration."
- "What is Dynamic Configuration Management (DCM) in the Humanitec model?" → "What is dynamic configuration management, as opposed to static per-environment config files?"
- "How does the Humanitec Orchestrator relate to Backstage and Argo CD?" → "Where does a platform orchestrator sit relative to the developer portal and the deployment tooling?"
- "What is Red Hat Advanced Cluster Security (ACS)?" → "Which capability areas does a Kubernetes security platform typically bundle?"
- "How does ACS integrate with a CI/CD pipeline?" → "How does an image scanner act as a CI/CD gate?"
- "What does the ACS network graph provide?" → "How does an observed-traffic network graph help with NetworkPolicies?"
- "How does ACS's scope differ from Kyverno/Gatekeeper?" → "Full-lifecycle Kubernetes security platform vs admission policy engine (Kyverno/Gatekeeper): how do their scopes differ?"

Scrubbed marketing phrasing: none beyond the rewrites above ("out of the box", "enterprise RBAC" were in the RHDH card).


## Abbreviations expanded

Notes touched: 72

- CRD → custom resource definition
- OCI → Open Container Initiative
- SBOM → software bill of materials
- SLSA → Supply-chain Levels for Software Artifacts
- SDK → software development kit
- OPA → Open Policy Agent
- SSO → single sign-on
- CNCF → Cloud Native Computing Foundation
- DB → database
- WAN → wide area network
- CNI → Container Network Interface
- KMS → key management service
- IaC → infrastructure as code
- IAM → identity and access management
- GA → general availability
- CEL → Common Expression Language
- OIDC → OpenID Connect
- CVE → Common Vulnerabilities and Exposures
- CSI → Container Storage Interface
- SCM → source control management
- HPA → Horizontal Pod Autoscaler
- CR → custom resource
- PGP → Pretty Good Privacy
- MPL → Mozilla Public License
- WinRM → Windows Remote Management
- PVC → persistent volume claim
- GC → garbage collection
- DORA → DevOps Research and Assessment
- LDAP → Lightweight Directory Access Protocol
- OWASP → Open Worldwide Application Security Project
- SPDX → Software Package Data Exchange
- CIS → Center for Internet Security
- LB → load balancer
- GSLB → global server load balancing
- CIDR → Classless Inter-Domain Routing
- HCP → HashiCorp Cloud Platform
- HCL → HashiCorp Configuration Language
- KCL → Kusion Configuration Language
- XR → composite resource
- MR → managed resource
- OLM → Operator Lifecycle Manager
- ACS → Advanced Cluster Security
- CD → continuous delivery (note 2 only; "Argo CD"/"Flux CD" left as product names)

Left bare: VPN, ISO, mTLS (well known); SOPS, AWX, Argo CD (names); L1/L3/L7, INI, S3, EC2, CI (whitelist/product); acronyms already expanded on their card (HNC, TVP, SSA, XRD, CMPs, CSVs, BSL).
