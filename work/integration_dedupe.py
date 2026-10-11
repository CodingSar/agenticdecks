"""Pass 6: remove duplicates between decks. Each entry says (deck to drop from, prompt prefix, deck that keeps it)."""
import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DROP = [
    ("Distributed_Systems_and_Data", "Cosmos DB consistency levels", "AZ-305_Solutions_Architect_Expert"),
    ("Linux_Internals_for_K8s_Security", "What happens when a container exceeds its CPU limit vs its memory limit?", "Kubernetes"),
    ("Kubernetes", "Hard link vs symbolic link?", "Linux_Internals_for_K8s_Security"),
    ("Kubernetes", "<code>systemctl start</code> vs <code>enable</code>?", "Linux_Internals_for_K8s_Security"),
    ("Kubernetes", "Tetragon vs Falco?", "Linux_Internals_for_K8s_Security"),
    ("Kubernetes", "gVisor vs Kata Containers?", "Linux_Internals_for_K8s_Security"),
    ("Kubernetes", "<code>kill</code> vs <code>kill -9</code>?", "Linux_Internals_for_K8s_Security"),
    ("Linux_Internals_for_K8s_Security", "containerd vs runc?", "Kubernetes"),
    ("Architect_Craft", "Nygard ADR sections", "Software_Architecture_and_DDD"),
    ("Architect_Craft", "State <b>Conway's Law</b>.", "Team_Topologies"),
    ("Networking", "How does Cilium's identity-based network policy differ", "Kubernetes"),
    ("Linux_Internals_for_K8s_Security", "How does a typical CNI plugin wire up a new pod?", "Networking"),
    ("Linux_Internals_for_K8s_Security", "What is a veth pair?", "Networking"),
    ("Linux_Internals_for_K8s_Security", "Why does a VXLAN overlay reduce MTU", "Networking"),
    ("Linux_Internals_for_K8s_Security", "What is conntrack?", "Networking"),
    ("Software_Testing", "<b>pass@k</b> vs <b>pass^k</b>?", "LLMs_and_Agentic_Engineering"),
    ("CISSP_Cloud_K8s", "CRL vs OCSP?", "Networking"),
    ("CISSP_Cloud_K8s", "Kubernetes RBAC is additive only.", "Kubernetes"),
    ("CISSP_Cloud_K8s", "What is SLSA?", "Platform_Engineering"),
    ("CISSP_Cloud_K8s", "How do GitOps setups keep secrets out of Git?", "Platform_Engineering"),
    ("Kubernetes", "What is the Operator pattern?", "Platform_Engineering"),
    ("Kubernetes", "Argo CD vs Argo Rollouts: who does progressive delivery?", "Platform_Engineering"),
    ("Platform_Engineering", "Team Topologies cognitive load:", "Team_Topologies"),
    ("Networking", "What does Metcalfe's law claim?", "Adaptive_Systems"),
    ("Quantitative_Foundations", "Why is \"extraordinary claims require extraordinary evidence\" just Bayes?", "Adoption_Epistemics_Governance"),
    ("Adoption_Epistemics_Governance", "What is <b>Simpson's paradox</b>?", "Quantitative_Foundations"),
    ("Distributed_Systems_and_Data", "Why measure response time with percentiles", "Quantitative_Foundations"),
]
log = ["# Pass 6: duplicates removed between decks", "", "| Removed from | Card | Kept in |", "|---|---|---|"]
for deck, prefix, keeper in DROP:
    p = os.path.join(ROOT, "work/out", deck + ".json"); d = json.load(open(p))
    hits = [n for n in d["notes"] if (n["front"] or n["text"]).startswith(prefix)]
    if not hits: continue  # already applied
    assert len(hits) == 1, (deck, prefix, len(hits))
    kp = json.load(open(os.path.join(ROOT, "work/out", keeper + ".json")))  # keeper deck must exist
    d["notes"].remove(hits[0])
    json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)
    log.append(f"| {deck} | {re.sub(r'<[^>]+>', '', prefix)[:70]} | {keeper} |")
open(os.path.join(ROOT, "work/out/INTEGRATION.changelog.md"), "w").write("\n".join(log) + "\n")
print(len(DROP), "removed")
