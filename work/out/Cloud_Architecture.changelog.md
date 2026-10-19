# Cloud Architecture — changelog

**Sources:** `cloud_aws_azure_gcp` (54) + `Cloud_AI_Infrastructure` (86) = **140 notes in → 114 notes out**.
10 concept subdecks: Cloud Models, Regions & Trade-offs · Identity & Governance · Networking · Compute, Virtualization & Containers · Storage · Databases & Analytics · Cost & Capacity · CPU & Server Hardware · AI Accelerators · AI Cluster Networking & Datacenter.

## Restructuring
- The AWS/Azure/GCP service-mapping cards (3-part answers) became **3-deletion clozes** (one card per provider): object/block storage, VMs, FaaS, serverless containers, managed K8s, registry, IaC, observability, relational/NoSQL/warehouse, queues/streams, IAM, guardrails, workload identity, secrets, confidential computing, private connectivity, hybrid links, LB, CDN, DNS, commitments, ARM CPUs, spot eviction notice.
- Glossary-style "What is X?" cards turned into why/when/trade-off prompts where possible (oversubscription → noisy neighbours, bin packing vs blast radius, vCPU = hyperthread except Graviton, branch misprediction cost, memory-bound inference, BF16 vs FP16, erasure coding vs replication/RAID).
- Updated churn: GCP IaC → Infrastructure Manager, Cloud Functions → Cloud Run functions, App Mesh end of support (Sept 2026) now past tense, AKS free control plane / EKS & GKE fees restated structurally.

## Merges (23 notes folded into 20 survivors)
- Region/AZ definitions (3 notes, both decks) → one "what failure does each protect against" contrast.
- VPC mapping → GCP global VPC trade-off card.
- SATA vs NVMe → NVMe; NAS → SAN-vs-NAS contrast; RAID + RAID 5 → erasure-coding card.
- CPU core + "CPU stands for" → core vs SMT; socket → NUMA; ISA → x86 vs ARM; clock speed → TDP; pipeline → branch misprediction.
- "GPU/TPU stands for" → why-GPU / TPU-vs-GPU; CUDA cores → CUDA vs Tensor Cores; PCIe-vs-NVLink → NVLink; ICI → TPU Pod; ASIC definition → why custom ASICs.
- ToR → spine-leaf; NIC/SmartNIC → DPU; immersion → direct-to-chip vs immersion; UPS → Tier III/IV.

## Splits: 4
- Multi-cloud → pays off / hidden costs. Kubernetes portability → what it equalizes / where it leaks.
- IAM model comparison → AWS no-inheritance + SCPs / AWS explicit deny / GCP binding inheritance (2 extra cards).

## New cards: 2
- IOPS vs throughput (DB vs backup/data loader). Data vs model parallelism.

## Deletions (9)
- Cosmos DB five consistency levels: duplicate, kept in AZ-305 (exam) and Distributed Systems & Data.
- Serverless DB scale-to-low product list: churny, low signal.
- Kubernetes PersistentVolume: Kubernetes deck owns it.
- Rack unit (U): trivia.
- PDU definition: low signal.
- PUE: Physics for Datacenters owns it (fuller card).
- Why liquid cooling: Physics for Datacenters owns it.
- Rack density in kW: Physics for Datacenters owns it.
- Container vs VM: covered by the Linux internals and CISSP decks.

## Analogies: 18 cards (~16%)
Existing analogies kept (source decks had none). New ones include: serviced flat (managed vs self-run), data gravity, power adapter (K8s portability), campus vs cities (AZ vs region), airline overbooking (oversubscription), minibar (egress), bucket brigade (systolic array), fast cook / slow waiter (memory-bound), roundabout (NVSwitch), espresso machine (ASIC), in-tray note (RDMA).

## Product-content review

Reviewed card by card for vendor-catered content: 1 deleted, 9 rewritten to the underlying concept, 2 scrubbed of marketing/dated phrasing.

### Deleted (1)
- "Datacenter AI accelerators: NVIDIA {{c1::H100 / H200}} (Hopper) and {{c2::B200}} (Blackwell); AMD {{c3::MI300X}}." — vendor product lineup (current flagship accelerator model names); churns yearly, no lasting lesson

### Rewritten (9)
- "Managed service mesh in 2026: what replaced AWS App Mesh and Azure Open Service Mesh?" → "Managed (provider-branded) service meshes: what is the durable pattern behind the churn?"
- "Managed Kubernetes cost: which of EKS / AKS / GKE does not charge for the control plane by default?" → "Managed Kubernetes cost: what do you pay for besides the worker nodes?"
- "GKE Autopilot vs Standard: what do you give up for not managing nodes?" → "Node-less (fully managed node) mode of a managed Kubernetes service vs standard node pools: what do you give up?"
- "Is S3 eventually consistent?" → "Are cloud object stores (S3, Blob Storage, GCS) eventually consistent?"
- "Which automatic, no-commitment discount is unique to GCP?" → "Commitment-based vs automatic usage-based discounts: what is the difference?"
- "AWS custom AI chips: {{c1::Trainium}} for training, {{c2::Inferentia}} for inference." → "Cloud providers split custom AI silicon into {{c1::training}} chips (throughput, large memory, fast interconnect) and {{c2::inference}} chips (latency and cost per query at low precision)."
- "What does GCP VM live migration do that AWS/Azure typically don't?" → "VM live migration during host maintenance: what does it do, and why does it matter for stateful VMs?"
- "In AWS IAM policy evaluation, what wins when an Allow and a Deny both match?" → "In cloud IAM policy evaluation, what wins when an Allow and a Deny both match?"
- "What is a GCP IAM binding, and how far does it reach?" → "In a hierarchical IAM model, what is a role binding/assignment, and how far does it reach?"

### Scrubbed (2)
- "Managed KubernetesAWS: {{c1::EKS}}Azure: {{c2::AKS}}GCP: {{c3::GKE}}": removed extra 'GKE is generally seen as the most mature' (promotional claim)
- "DynamoDB vs Cosmos DB: how does each go multi-region, and how much consistency choice do you get?": 'turnkey global distribution' → 'built-in global distribution'

## Abbreviations expanded

Notes touched: 67

- IAM → identity and access management
- TPU → tensor processing unit
- VPC → virtual private cloud
- NIC → network interface card
- IOPS → input/output operations per second
- FP16 → 16-bit floating point
- BF16 → brain floating point
- ASIC → application-specific integrated circuit
- HA → high availability
- AZ → availability zone
- L7 → layer 7
- L4 → layer 4
- KVM → kernel-based virtual machine
- NFS → network file system
- SMB → server message block
- PCIe → peripheral component interconnect express
- NVMe → non-volatile memory express
- SMT → simultaneous multithreading
- NUMA → non-uniform memory access
- FLOPS → floating-point operations per second
- FP8 → 8-bit floating point
- FP32 → 32-bit floating point
- RoCE → remote direct memory access over converged Ethernet
- RDMA → remote direct memory access
- SDK → software development kit
- CSI → container storage interface
- DR → disaster recovery
- SCP → service control policy
- RG → resource group
- OU → organizational unit
- IRSA → identity and access management (IAM) roles for service accounts
- TDX → Trust Domain Extensions
- SEV → Secure Encrypted Virtualization
- ACL → access control list
- LB → load balancer
- CDN → content delivery network
- WAF → web application firewall
- FaaS → function as a service
- SLA → service level agreement
- HDD → hard disk drive
- SATA → Serial ATA
- AHCI → Advanced Host Controller Interface
- RAID → redundant array of independent disks
- SAN → storage area network
- NAS → network-attached storage
- CUD → committed use discount
- UPI → Ultra Path Interconnect
- DPDK → Data Plane Development Kit
- RISC → reduced instruction set computer
- INT8 → 8-bit integer
- VRAM → video random access memory
- GDDR → graphics double data rate
- DRAM → dynamic random access memory
- FSDP → fully sharded data parallel
- MIG → Multi-Instance GPU
- vGPU → virtual GPU
- FPGA → field-programmable gate array
- NCCL → NVIDIA Collective Communications Library
- HPC → high-performance computing
- PFC → priority flow control
- ECN → explicit congestion notification
- DPU → data processing unit
- UPS → uninterruptible power supply
- EKS → Elastic Kubernetes Service
- AKS → Azure Kubernetes Service
- GKE → Google Kubernetes Engine
- S3 → Simple Storage Service
- EBS → Elastic Block Store
- KMS → Key Management Service
- ECS → Elastic Container Service
- ECR → Elastic Container Registry
- EC2 → Elastic Compute Cloud
- RDS → Relational Database Service
- SQS → Simple Queue Service
- ALB → Application Load Balancer
- NLB → Network Load Balancer
- CDK → Cloud Development Kit
- ACI → Azure Container Instances
- VNet → virtual network
- NSG → network security group
- TDP → thermal design power
- HBM → high-bandwidth memory
- ZeRO → Zero Redundancy Optimizer
- GPFS → General Parallel File System
- iSCSI → Internet Small Computer Systems Interface
- TCO → total cost of ownership
- IA → infrequent access
- ARM → Azure Resource Manager
- GCS → Google Cloud Storage

Where an abbreviation occurs only inside a cloze answer (EC2, ECR, EKS/AKS/GKE, ALB/NLB, L4/L7, OU, IA, IRSA, SEV/TDX, LB/WAF) or would leak the answer (EBS/NFS in the storage-models cloze), it is expanded in `extra` instead.
