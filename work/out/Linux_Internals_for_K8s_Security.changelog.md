# Changelog: Linux Internals for Kubernetes & Security

Source: `Linux_OS_Internals_for_K8s_Security.json` (193 notes) → **185 notes** (169 basic, 16 cloze), 12 concept subdecks
(01 Processes & Scheduling … 12 systemd & Tools).

## Merges (12 groups, 13 notes absorbed; the kept note's guid is retained)
- #177 "What two responsibilities make PID 1 special" → #7 (PID 1 duties)
- #50 memory.max → #20 "How is a K8s memory limit enforced" (adds OOMKilled / exit 137)
- #123 "Concretely, what does a network namespace isolate" → #30
- #170 rootless containers via user namespace → #34
- #188 nsenter debugging → #38 (now a task-style prompt)
- #171 hostPID breakout risk → #65 CAP_SYS_PTRACE + hostPID
- #168 CAP_SYS_ADMIN escape → #61
- #165 privileged ≈ host root → #70 --privileged
- #103 Cilium eBPF networking → #133 Cilium kube-proxy replacement
- #164 why sandboxed runtimes exist → #173 kernel is the trust boundary
- #143 /proc/[pid]/maps → #22 VMA
- #145 perf overview → #191 perf top vs record/report

## Deletions / moves (1)
- #77 DAC vs MAC: moved to the CISSP deck (access-control models) and merged with the CISSP DAC/MAC card, which keeps this guid.

## Splits and new cards (5)
- Split: #7 → plus "Why is a plain app as PID 1 a problem?"; #47 → plus cloze "namespaces = see, cgroups = use"; #159 → plus cloze "dockershim removed in 1.24".
- New contrast cards: Falco vs Tetragon (detect vs enforce); gVisor vs Kata (user-space kernel vs micro-VM).

## Rewrites
- Every answer cut to about 25 words or fewer, with the nice-to-know details moved to `extra` (e.g. QoS → oom_score_adj, `lsof +L1`, VXLAN symptoms).
- "List…" enumerations became clozes: process states (now focused on D/Z), capability sets, SELinux modes, seccompProfile types, eBPF hooks, Coffman conditions, systemd units, kube-proxy modes, man sections. The 8 namespace types became a mnemonic card (PUMIC NUT), and each type keeps its own card.
- Prompts turned into how/why/what-breaks questions (e.g. "Why can df show more than du?", "How can a binary bind port 80 without setuid?", "What can a seccomp filter not inspect?").
- Dropped date and edition trivia from answers (kernel/K8s versions kept only when they matter operationally).

## Analogies
- 38 added (about 21% of cards): e.g. copy-on-write (shared textbook), OverlayFS (projector transparencies), CPU vs memory limit (speed governor vs wall), shared kernel (apartment foundation).
