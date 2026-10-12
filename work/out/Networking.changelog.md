# Networking changelog

Sources: `Networking_Fundamentals_Tanenbaum` (166, prefix T) + `networking-below-cni` (69, prefix K) = **235 notes in → 166 out**.

Subdecks: 01 Models & Layering · 02 Physical Layer & Media · 03 Data Link & Ethernet · 04 IP, Addressing & Routing · 05 BGP & Fabric Routing · 06 Transport & TCP · 07 DNS & Application Protocols · 08 TLS & Crypto · 09 Load Balancing · 10 Linux & Kubernetes Datapath · 11 Troubleshooting & Triage.

## Summary
- Deleted: 26 (21 Tanenbaum, 5 below-CNI)
- Merges: 31 groups (49 notes absorbed into a surviving note)
- Splits: 3 (K5 MTU → +PMTUD black hole; T129 UDP → +when to pick UDP; K63 half-open → +detection/keepalive)
- New contrast/practice cards: 3 (IGP vs EGP, rwnd vs cwnd, DNS TTL cut-over)
- Analogies: 48 in total. 8 new (OSI mnemonic, bandwidth/latency, FDM/TDM, CDMA, routing/forwarding, flow/congestion, leaky/token bucket, recursive/iterative DNS). Kept 40 of the 69 below-CNI analogies, all trimmed to one or two sentences; dropped the weaker ones to stay near 30%.
- Below-CNI incidents kept in `extra` as `<b>Incident:</b>` lines, trimmed.
- Enumerations turned into clozes: OSI layers, TCP/IP layers, delivery modes, framing methods, CSMA variants, ALOHA, DHCP DORA, DNS record types, BGP best-path order, eBPF hooks, port ranges, subnet sizes.

## Merges (surviving guid's note listed first)
- T13 + T12 + T14 + T15 + T16 + T17 + T18 + T19 + T20 + T31 + T55 + T125 → "OSI model, bottom → top: L1 {{c1::Physical}}: raw bits on a medium<"
- T21 + T22 → "TCP/IP model, bottom → top: {{c1::Link}} → {{c2::Internet}} (IP, best-"
- T10 + T8 + T9 → "Delivery modes: {{c1::unicast}} = one receiver; {{c2::multicast}} = a "
- T5 + T4 + T2 → "LAN vs WAN: what is the defining difference?"
- T29 + T30 → "Bandwidth vs latency?"
- T42 + T43 → "GEO vs LEO satellites: why does the orbit matter for networking?"
- T49 + T50 → "FDM vs TDM multiplexing?"
- T46 + T47 → "Why is ADSL asymmetric, and what makes DSL possible on phone lines?"
- T63 + T64 → "CRC vs a simple checksum: why does Ethernet use a CRC?"
- T67 + T71 → "How big should a sliding window be?"
- T68 + T69 → "Go-Back-N vs Selective Repeat: what happens after one lost frame?"
- T75 + T76 → "What problem does the MAC (Medium Access Control) sublayer solve?"
- T77 + T78 + T79 → "ALOHA: stations send whenever they like. Pure ALOHA peaks at {{c1::~18"
- T81 + T82 + T83 → "CSMA variants when the channel is busy: {{c1::1-persistent}} waits and"
- T87 + T88 → "What is the hidden terminal problem, and what mitigates it?"
- T91 + T94 → "Hub vs switch vs router?"
- T95 + T96 + T97 → "Datagram vs virtual-circuit network layer?"
- T114 + T119 → "An IPv4 address is {{c1::32}} bits (dotted decimal); an IPv6 address i"
- T121 + K4 → "How does ARP resolve an IP to a MAC?"
- T108 + T109 + T65 → "Flow control vs congestion control?"
- T110 + T111 → "Leaky bucket vs token bucket?"
- T105 + K12 → "What is BGP in one sentence?"
- T106 + K13 → "What is an autonomous system (AS), and why does a BGP-peered cluster n"
- T128 + T129 + T23 → "TCP vs UDP: what does each give you?"
- T136 + T137 → "What is AIMD in TCP congestion avoidance?"
- T146 + T147 → "How is DNS structured?"
- T148 + T149 → "Recursive vs iterative DNS query?"
- T150 + T151 + T152 → "DNS record types: {{c1::A}} → IPv4 address; {{c2::AAAA}} → IPv6 addres"
- T153 + T156 → "HTTP is stateless. How do web apps keep sessions?"
- T157 + T158 → "SMTP vs IMAP/POP3?"
- K52 + K62 → "What does <code>externalTrafficPolicy: Local</code> change compared wi"

## Deletions
- T0 "What is a computer network?": trivial definition (computer network)
- T1 "Define PAN (Personal Area Network).": PAN definition: no work/exam impact
- T3 "Define MAN (Metropolitan Area Network).": MAN definition: no work/exam impact
- T6 "What is the internet (lowercase i) as defined by Tanenbaum?": internet = network of networks: trivial
- T7 "What is a subnet in the WAN context?": "subnet" in old WAN sense, confusing next to IP subnetting
- T24 "What key criticism does Tanenbaum raise about the OSI model'": OSI adoption history: trivia
- T32 "What is Fourier analysis used for in the context of signal t": Fourier analysis: theory with no job impact (Nyquist/Shannon kept)
- T37 "What is coaxial cable?": coax cable: legacy
- T41 "What is the electromagnetic spectrum's role in wireless tran": EM spectrum: vague, no retrievable answer
- T44 "What is PSTN (Public Switched Telephone Network)?": PSTN: legacy telephony
- T45 "What is a modem?": modem definition: legacy
- T48 "What is DOCSIS (Data Over Cable Service Interface Specificat": DOCSIS: cable-ISP trivia
- T53 "What is switching in the context of the phone system?": phone switching: covered by circuit switching
- T54 "What is a local loop?": local loop: telco trivia
- T73 "What is HDLC (High-level Data Link Control)?": HDLC: legacy protocol
- T74 "What is PPP (Point-to-Point Protocol)?": PPP: legacy for this audience
- T141 "What is the TCP header's checksum used for?": TCP checksum pseudo-header: low value (CRC vs checksum card kept)
- T159 "What is FTP (File Transfer Protocol)?": FTP: legacy
- T162 "What is a BitTorrent 'tracker'?": BitTorrent tracker: trivia
- T163 "What is streaming media, and how does it differ from downloa": streaming vs download: trivial
- T165 "What is the purpose of a URL (Uniform Resource Locator)?": URL parts: trivial
- K2 "What is a Linux network namespace?": network namespace: owned by Linux deck
- K39 "What is extended Berkeley Packet Filter (eBPF)?": what is eBPF: owned by Linux deck (networking hooks kept)
- K40 "What does the eBPF verifier guarantee?": eBPF verifier: Linux-deck internals
- K48 "What are Compile Once – Run Everywhere (CO-RE) and BPF Type ": CO-RE/BTF: Linux-deck internals
- K49 "How do you see what eBPF programs are attached on a node?": bpftool listing: Linux-deck tooling

## Cross-cluster notes (left alone)
- Kubernetes deck: the K8s Service datapath cards (kube-proxy iptables DNAT, hairpin, externalTrafficPolicy, ingress vs LB, preStop draining, CNI responsibilities, Cilium identity policy) are kept here as datapath mechanics. K62 (Service types) was folded into the externalTrafficPolicy card. Dedupe against Kubernetes if it covers the same mechanics.
- Linux deck: network namespaces, the eBPF definition, the verifier, CO-RE/BTF and bpftool were deleted here because the Linux deck owns eBPF internals. The networking-facing eBPF cards (XDP/TC/socket hooks, XDP_DROP, maps-as-datapath-state, kube-proxy replacement, observability) stay.
- Cloud/AZ-305: TLS/LB idle-timeout numbers (ALB/NLB) are mentioned only as examples.
