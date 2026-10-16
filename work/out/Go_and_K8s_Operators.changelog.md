# Go & Kubernetes Operators: changelog

Source: `work/source/Go_Intricacies_and_K8s_Operators.json` (one flat deck)

- **Notes in → out:** 204 → 176
- **Deleted:** 11 (all listed below)
- **Merged:** 19 notes folded into another note (guid of the survivor kept)
- **Split:** 0 (source answers were already short; several were trimmed instead)
- **New cards:** 2 (an `errors.As` usage card and an informer resync-vs-relist contrast card)
- **Analogies added:** 36 (~20% of cards; source had none)
- **Subdecks (10):** 01 Types & Interfaces, 02 Errors & Panics, 03 Generics, 04 Goroutines & Channels, 05 sync & context, 06 Memory & Performance, 07 Stdlib, Testing & Tooling, 08 client-go & apimachinery, 09 controller-runtime & Kubebuilder, 10 Operator Testing & Observability

## Merges (source note # → kept note #)
- 21 (structural vs duck typing) → 1 (how a type satisfies an interface)
- 31 (typed nil returned as error) → 3 (nil-interface trap)
- 101 (`map[string]interface{}` payloads) → 4 (cost of `any`)
- 95 (field shadowing a promoted method) → 6 (embedding vs inheritance)
- 96 (ignoring `, ok` in type assertions) → 11 (two-value type assertion)
- 24 (`errors.Is` vs `==`) → 23 (sentinel errors)
- 33 (idiomatic error context) → 26 (`%w` wrapping)
- 98 (libraries panicking) → 28 (panic vs error)
- 89 (pointer to range variable) → 49 (Go 1.22 loop variables)
- 87 (read nil map) → 86 (write nil map), now one two-deletion cloze
- 123 (why vendor in K8s projects) → 122 (`go mod tidy` vs `vendor`)
- 141 (`unstructured.Unstructured`) → 125 (dynamic client)
- 158 (leader election) → 148 (Manager), as extra
- 185 (stale cached reads) → 151 (cached client vs APIReader)
- 183 (watching by reference) → 154 (`Watches()` with map func)
- 187 (exponential backoff rationale) → 161 (workqueue backoff)
- 193 (testable decision logic) → 163 (separate logic from Reconcile plumbing)
- 195 (envtest vs kind scope) → 194 (kind), now one contrast card
- 196 (no `time.Sleep` in tests) → 192 (Gomega `Eventually`)

## Deletions
Generic operator concepts already owned by Platform Engineering::Operators (`work/source/platform_gitops.json`):
- 150 Why Reconcile must be idempotent: duplicates PE "Why must Reconcile() be idempotent".
- 174 Level-triggered vs edge-triggered: duplicates PE card of the same name.
- 175 What a finalizer is: duplicates PE finalizer card. The Go-specific handling (`controllerutil.AddFinalizer`/`RemoveFinalizer`, deletionTimestamp branch) lives on in rewritten note 176.
- 178 Finalizer vs OwnerReference for external resources: covered by the PE finalizer card.
- 179 Status conditions structure: duplicates PE "Conventional structure of a status condition".
- 181 409 Conflict / `RetryOnConflict`: duplicates PE "How do you handle a 409 Conflict".
- 182 Server-side apply: duplicates PE "What is Server-Side Apply".
- 186 Periodic drift correction: a generic self-healing concept covered by PE GitOps/Operators.
- 143 CRD conversion webhook: duplicates PE "CRD versioning: served vs storage, conversion".
- 147 resourceVersion and optimistic concurrency: duplicates the PE generation-vs-resourceVersion and 409 cards.

Signal filter:
- 173 Contents of the Kubebuilder `PROJECT` file: tooling trivia with no effect on work.

## Notable rewrites
- 177 (OwnerReference concept) now asks about `controllerutil.SetControllerReference`; 184 (no delete/recreate) adds `controllerutil.CreateOrUpdate`; 172 (served/storage) now asks about the `+kubebuilder:storageversion` marker. Each keeps its guid.
- Accuracy fixes: 131 (informer resync replays the local cache and does not relist), 100 (`time.After` leak fixed for Go 1.23+ modules), 37 (`cmp.Ordered`, not `constraints.Ordered`), 52 (Go 1.25 GOMAXPROCS respects cgroup CPU limits), 83 (`GOMEMLIMIT` added), 156 (`Requeue` deprecated in favour of `RequeueAfter`).
- Tags and `source` labels kept from the source notes.

## Product-content review
Reviewed card by card: no product-catered cards found (tools present are open-source subjects or short examples in `extra`); nothing deleted, rewritten or scrubbed.
