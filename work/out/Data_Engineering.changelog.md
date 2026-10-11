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
