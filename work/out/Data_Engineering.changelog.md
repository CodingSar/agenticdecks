# Data Engineering — changelog

**Source:** data-engineering-basics (59 notes). **Output:** 82 notes in 6 subdecks
(01 Cloud Storage & Table Formats, 02 Stateful Data on Kubernetes, 03 Kafka Core, 04 Kafka Ecosystem & Managed Streaming, 05 Analytics & Warehousing, 06 Data Gravity & Cost).

## Moved to Distributed Systems & Data (to avoid duplication; guids kept there)
- `nd_V^O,QK7` LSM tree, `k.4tsJ6I_J` B-tree vs LSM, `niK?WfLt.:` amplification, `F&sjWx_<%7` Bloom filters, `N5v{!z2NhY` WAL,
  `LgC~S44[<0` row vs column, `iFp;{|s;tN` MVCC, `k$Y49PfQ55` event time/watermark, `x3Y8C$d*Ql` Aurora storage, `eJTV><c)~p` DynamoDB/Cosmos partition keys.

## Merges / deletions
- `iiSh2|S2LM` Cosmos DB five consistency levels: duplicate of the Distributed Systems deck's Cosmos cloze, so deleted here.
- `O>I*S=b+@{` "Characterize OLAP" merged with `i65X;[#uX(` "Characterize OLTP" into one sizing cloze (OLTP vs OLAP contrast lives in Distributed Systems & Data).
- Trivia removed: "coined by Dave McCrory (2010)" (data gravity), long service-name lists (moved to `extra` or dropped).

## Splits
- 35 new cards from splits. Original notes were ~590 chars; e.g. block/file/object → 3 cards; Redshift → leader/compute, RA3, dist/sort keys; consumer groups → division, parallelism limit, choosing partition count; Kafka exactly-once → commit order cloze, ingredients, scope; placement checklist → 3 cards; Event Hubs → Kafka endpoint, vocabulary cloze, Capture.
- Enumerations turned into clozes: topic/partition/offset, durability settings, Schema Registry modes, Synapse distributions, lake/warehouse/lakehouse, storage tiers, zonal vs regional storage.

## Analogies
- 14 added (e.g. partitions as checkout lanes, ISR as understudies, retention vs compaction as CCTV vs contacts list, ETL vs ELT as central kitchen vs groceries).

## Product-content review

Reviewed card by card for vendor-catered content: 3 deleted, 6 rewritten to the underlying concept, 0 scrubbed of marketing/dated phrasing.

### Deleted (3)
- "Event Hubs ↔ Kafka vocabulary: namespace ≈ {{c1::cluster}}, event hub ≈ {{c2::topic}}; partitions and consumer groups keep their names." — single-vendor naming taxonomy (Event Hubs ↔ Kafka terms); folded into the Kafka-compatible-services card's extra
- "What do Redshift RA3 nodes change?" — single-vendor SKU (Redshift RA3 node type); the concept is already the 'separation of storage and compute' card
- "How does an Azure Synapse dedicated SQL pool lay out data?" — single-vendor SKU internals (Synapse 60 distributions, DWU levels) plus dated successor note; nothing transferable

### Rewritten (6)
- "Amazon MSK vs Kinesis Data Streams?" → "Managed open-source Kafka vs a provider-proprietary streaming service: trade-off?"
- "How does Azure Event Hubs relate to Kafka?" → "Kafka-protocol-compatible services that aren't Kafka: what works, and what doesn't?"
- "What is Event Hubs Capture?" → "What is the 'stream capture to lake' pattern?"
- "Amazon Redshift: what do the leader node and compute nodes do?" → "MPP warehouse architecture: what do the leader (coordinator) node and the compute nodes do?"
- "What do Redshift distribution keys and sort keys control?" → "In an MPP warehouse, what do distribution keys and sort/cluster keys control?"
- "Synapse table distribution: {{c1::HASH(column)}} for large fact tables (high-cardinality join key); {{c2::ROUND_ROBIN}} (default, fastest load, joins shuffle); {{c3::REPLICATE}} for small dimensions." → "MPP table distribution strategies: {{c1::hash on a column}} for large fact tables (high-cardinality join key); {{c2::round-robin}} (fastest load, joins shuffle); {{c3::replicate}} for small dimensions."

## Abbreviations expanded
Notes touched: 48
AZ → availability zone; OLTP → online transaction processing; OLAP → online analytical processing; PV → persistent volume; PVC → persistent volume claim; CSI → container storage interface; ELT → extract, load, transform; ETL → extract, transform, load; CDC → change data capture; ZRS → zone-redundant storage; LRS → locally redundant storage; MPP → massively parallel processing; ISR → in-sync replica set; ACID → atomicity, consistency, isolation, durability; KIP → Kafka Improvement Proposal; GDPR → General Data Protection Regulation; WAL → write-ahead log; RTO → recovery time objective; MVCC → multi-version concurrency control; SCP → service control policy; VPC → virtual private cloud; VNet → virtual network; NAT → network address translation; ERP → enterprise resource planning; IA → infrequent access (in extra); RF → replication factor; JDBC → Java Database Connectivity; HPA → horizontal pod autoscaler; ORC → Optimized Row Columnar; RLE → run-length encoding; SDK → software development kit; CNCF → Cloud Native Computing Foundation; 2PC → two-phase commit; EBS → Elastic Block Store; EFS → Elastic File System; ADLS → Azure Data Lake Storage; MSK → Managed Streaming for Apache Kafka; EKS → Elastic Kubernetes Service; AKS → Azure Kubernetes Service; DMS → Database Migration Service; RDS → Relational Database Service; GCS → Google Cloud Storage; KEDA → Kubernetes Event-driven Autoscaling
