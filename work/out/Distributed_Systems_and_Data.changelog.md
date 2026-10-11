# Distributed Systems & Data — changelog

**Sources:** Designing_Data-Intensive_Applications (65) + distributed_systems_aws_azure_k8s (98) = 163 notes, plus 10 storage/streaming notes moved in from data-engineering-basics.
**Output:** 220 notes in 12 concept subdecks (01 Foundations … 12 Cloud & Kubernetes Case Studies).

## Merges (overlapping notes combined; each original guid kept on the card it fed)
- DDIA "LSM engine" + DE "LSM tree" → LSM write path (`ur$;mysp33`) + LSM read path (`nd_V^O,QK7`).
- DDIA "LSM vs B-tree trade-offs" + DE "B-tree vs LSM" → "when LSM wins" (`hZ;i>DyTHR`) / "when B-tree wins" (`k.4tsJ6I_J`).
- DDIA "write amplification" + DE "write/read/space amplification" → write-amp card + read/space-amp cloze + new RUM-conjecture card.
- DDIA "column storage" + DE "row vs column" → column-storage card + "why column writes are expensive".
- DDIA FLP + DistSys FLP → "state FLP" (`u[abqK?V#U`) and "how Raft/Paxos coexist with FLP" (`g-`iV9MP-l`).
- DDIA CAP + DistSys CAP (Gilbert & Lynch) → precise statement, "pick 2 of 3" misreading, "C means linearizability" card.
- DDIA linearizability + DistSys linearizability → definition + scope cards.
- DDIA process pauses + DistSys fencing token + GC-pause scenario → fencing token / GC scenario / "why check-then-write fails" (3 cards, no duplication).
- DDIA 2PC + DistSys 2PC/Paxos commit → "why 2PC blocks" + "how Paxos commit removes it".
- DDIA Lamport limitation + DistSys Lamport/vector/HLC → three separate clock cards.
- DDIA replication-lag guarantees + DistSys session guarantees → one 4-deletion session-guarantee cloze, consistent-prefix cloze, "causal for one client" card.
- DistSys partial-partition + PreVote/CheckQuorum → partition types, disruptive-server, PreVote, CheckQuorum cards.
- DE MVCC → transactions subdeck (operational cost of MVCC); DE watermark → streams subdeck; DE Aurora storage → "log is the database" card; DE DynamoDB/Cosmos hot partition → hot-key fix card; DE Cosmos DB consistency levels (`iiSh2|S2LM`) folded into the Cosmos cloze (`i;224UOI`J`).

## Deletions
- `DDR4w)f5Gy` "Name the three modes of dataflow the chapter analyzes": chapter-structure taxonomy, little use at work.
- Dropped trivia inside kept cards: Datalog (graph models), Raft paper's exact timeout range moved to extra, AWS Paxos product list reduced to the shared pattern, S3 "old model" history.

## Splits and rewrites
- 48 new cards from splits (multi-part answers such as Raft election/log matching/membership, Paxos phases, etcd fsync, Cosmos session, retries, thundering herd, lambda architecture, PACELC classification).
- Enumerations turned into clozes: ACID, replication approaches, serializable implementations, failure models, stream windows, batch joins, Paxos roles, Raft sub-problems, Cosmos levels, Azure LRS/ZRS/GRS/RA-GRS, delivery semantics.
- All answers trimmed to ≤ ~45 words; product numbers moved to `extra`.

## Analogies
- 37 analogies added (sources had none), e.g. sloppy-quorum hinted handoff (neighbour takes your parcel), 2PC (officiant faints), shuffle sharding (dealt hands), cells (watertight compartments).
