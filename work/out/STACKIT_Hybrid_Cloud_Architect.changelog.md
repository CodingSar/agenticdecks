# STACKIT Hybrid Cloud Architect — changelog

**Notes in:** 90. **Notes out:** 158 (72 keep an original guid, 86 new from splits with `guid: null`).
**Subdecks (6):** 01 STACKIT Foundations · 02 SKE Core · 03 IaaS & Networking · 04 Identity, Access & Secrets · 05 Tenancy, Multi-Cluster & DR · 06 Hybrid & Central Management (old 05 Multitenancy + 06 Multi-Cluster & GitOps merged after the generic cards moved out).

## Moved out to Platform Engineering (18)
Generic platform/K8s cards with no STACKIT specifics now live in `Platform Engineering` (guids kept there): soft vs hard tenancy `IP&D[{}k.s`, namespace mechanisms `G8t^2YpSSs`, namespace limits `ku-Y;:W-7P`, vCluster `In#Q}QYD.f`, Capsule/HNC `wPr<gm?V.X`, tenancy decision matrix `ryw)p3-|I*`, shared-services tenancy `k,eI?_a`#G`, reasons for multiple clusters `H`YSf%{0aB`, hub cluster `kgoKg9(XDz`, push vs pull fleet `]cdLhh8W4`, ApplicationSets `wi(TaawJ,.`, Terraform vs GitOps line `K(po^UN:]R`, values layering `I*,VI&vp*}`, multi-cluster networking `bkTa<Qttdg`, data gravity `B6W!B=Bc2b`, upgrade rings `hiEnPu1|fl`; merged there: Argo CD multitenancy `pk:v*k@ERi` (→ AppProject), Argo CD vs Flux `Q@mOM@H/ca` (→ Argo vs Flux).

## Deletions
No whole notes deleted. Redundant fragments dropped during splits: Object Storage "keep backups cloud-local" (kept once as extra), VPN "no NAT" line (covered by the CIDR-planning card), SKE L7 ingress line (covered by NLB vs ALB), SKE API hardening in the hybrid card (kept once in SKE Core), data-services architectural note (moved to the managed-DB heuristic), cost-model tenancy note (extra).

## Merges
- IAM auth flows from `C&i_JR%oU+` folded into the machine-auth cloze `IwxYGb[&f]`.
- NetworkPolicy defaults from `e7++:4k{N$` folded into SKE NetworkPolicy `c9(2-ENGk:`; `e7++:4k{N$` now carries the VPN-egress-governance point.
- STACKIT DNS hybrid note (`MWrY.|l17P`) folded into split-horizon DNS `EuoKP.GYTp`.

## Splits
55 notes split into 86 extra cards (avg source note ~730 chars). Bulleted lists became per-question cards or clozes (21 cloze notes: hierarchy, compute/data/storage/security/networking portfolios, Gardener Garden/Seed/Shoot, node pool settings, autoscaling layers, extensions, day-2 stack, identity planes, machine-auth preference order, quota layers, new-cluster lifecycle, split-horizon DNS, PKI, seven pillars in two halves). Trade-off tables/bullets became one card per option plus a heuristic card.

## Analogies
18 notes (~11%), all new: Gardener seeds/shoots, SNA as shared VPC, Pinniped passport office, admin kubeconfig master key, break-glass fire axe, JWKS hologram check, ESO pantry, registry warehouse, split-horizon phonebook, hub location, and others.
