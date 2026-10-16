# Pass 6: duplicates removed between decks

| Removed from | Card | Kept in |
|---|---|---|
| Distributed_Systems_and_Data | Cosmos DB consistency levels | AZ-305_Solutions_Architect_Expert |
| Linux_Internals_for_K8s_Security | What happens when a container exceeds its CPU limit vs its memory limi | Kubernetes |
| Kubernetes | Hard link vs symbolic link? | Linux_Internals_for_K8s_Security |
| Kubernetes | systemctl start vs enable? | Linux_Internals_for_K8s_Security |
| Kubernetes | Tetragon vs Falco? | Linux_Internals_for_K8s_Security |
| Kubernetes | gVisor vs Kata Containers? | Linux_Internals_for_K8s_Security |
| Kubernetes | kill vs kill -9? | Linux_Internals_for_K8s_Security |
| Linux_Internals_for_K8s_Security | containerd vs runc? | Kubernetes |
| Architect_Craft | Nygard ADR sections | Software_Architecture_and_DDD |
| Architect_Craft | State Conway's Law. | Team_Topologies |
| Networking | How does Cilium's identity-based network policy differ | Kubernetes |
| Linux_Internals_for_K8s_Security | How does a typical CNI plugin wire up a new pod? | Networking |
| Linux_Internals_for_K8s_Security | What is a veth pair? | Networking |
| Linux_Internals_for_K8s_Security | Why does a VXLAN overlay reduce MTU | Networking |
| Linux_Internals_for_K8s_Security | What is conntrack? | Networking |
| Software_Testing | pass@k vs pass^k? | LLMs_and_Agentic_Engineering |
| CISSP_Cloud_K8s | CRL vs OCSP? | Networking |
| CISSP_Cloud_K8s | Kubernetes RBAC is additive only. | Kubernetes |
| CISSP_Cloud_K8s | What is SLSA? | Platform_Engineering |
| CISSP_Cloud_K8s | How do GitOps setups keep secrets out of Git? | Platform_Engineering |
| Kubernetes | What is the Operator pattern? | Platform_Engineering |
| Kubernetes | Argo CD vs Argo Rollouts: who does progressive delivery? | Platform_Engineering |
| Platform_Engineering | Team Topologies cognitive load: | Team_Topologies |
| Networking | What does Metcalfe's law claim? | Adaptive_Systems |
| Quantitative_Foundations | Why is "extraordinary claims require extraordinary evidence" just Baye | Adoption_Epistemics_Governance |
| Adoption_Epistemics_Governance | What is Simpson's paradox? | Quantitative_Foundations |
| Distributed_Systems_and_Data | Why measure response time with percentiles | Quantitative_Foundations |

## New decks (Oct 2026)
Art History → Architecture Styles: 8 building-architecture cards removed from Art History (orders, Parthenon refinements, pointed arch, Gothic system, Romanesque vs Gothic, Pantheon dome, Greek vs Roman temple).

## Integration of new decks (Identity & Zero Trust, SRE & Observability, Software Engineering Classics)

Removed after `similar.py 0.55` scan:

- **Software_Engineering_Classics**: "Hickey 2011, Simple Made Easy: {{c1::simple}} is objective (one braid, un-complected); {{c" — repeats own card on Hickey simple vs easy
- **Software_Engineering_Classics**: "Norvig 1996, Design Patterns in Dynamic Languages: {{c1::16 of 23}} GoF patterns are invis" — repeats own card on Norvig critique
- **Software_Engineering_Classics**: "Naur 1985, Programming as Theory Building: a program is {{c1::the theory in its developers" — repeats own card on Naur theory building
- **Software_Engineering_Classics**: "Parnas 1979, Designing Software for Ease of Extension and Contraction: design a loop-free " — repeats own card on Parnas uses hierarchy
- **Software_Engineering_Classics**: "GOOS: why mock only types you own?" — duplicates Software Testing#37 (don't mock what you don't own)
- **Software_Engineering_Classics**: "XP values: {{c1::communication}}, {{c2::simplicity}}, {{c3::feedback}}, {{c4::courage}}, a" — duplicates Open Agile Architecture#155 (XP values)
- **Software_Engineering_Classics**: "Fowler's definition of refactoring?" — duplicates Open Agile Architecture#40 (definition of refactoring)
- **Identity_and_Zero_Trust**: "What is OPA (Open Policy Agent) in this model, and what is Rego?" — duplicates Platform Engineering#180 (OPA)
- **Identity_and_Zero_Trust**: "Authentication factors: {{c1::something you know}} (password, PIN), {{c2::something you ha" — duplicates CISSP#80 (authentication factors)
- **SRE_and_Observability**: "Why do you need remote write and a long-term store (Thanos, Mimir, Cortex) at all?" — duplicates Kubernetes#158 (Prometheus remote write / long-term storage)
