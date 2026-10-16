# SRE & Observability — changelog (new deck)

**Scope.** The reasoning behind Site Reliability Engineering (Google SRE Book, SRE Workbook, Implementing SLOs) and
modern observability (Prometheus data model, Honeycomb-style wide events and high cardinality, W3C Trace Context,
OpenTelemetry, Kubernetes platform signals). 207 notes, 12 subdecks, 55 analogies (27%), 23 cloze notes, 7 SVG diagrams.

**Subdecks.** 01 SRE Principles · 02 SLIs, SLOs & SLAs · 03 Error Budgets & Burn Rate · 04 Monitoring & Alerting
Philosophy · 05 Metrics & Prometheus Model · 06 Logs & Structured Events · 07 Distributed Tracing · 08 OpenTelemetry ·
09 Incident Response · 10 Postmortems & Learning · 11 Capacity, Load & Release · 12 Observability for Kubernetes & Platforms.

**Diagrams** (`media/sre_*.svg`): SLI/SLO/SLA nesting, burn-rate lines + multi-window alert, cumulative histogram
buckets with SLO edge, trace with spans/links/critical path, OTel Collector agent→gateway pipeline, incident command
roles, symptom-vs-cause alerting.

**Deliberately left out.** Product/vendor trivia (Grafana panels, Datadog pricing), PromQL syntax drills, OTel SDK
code per language, history (OpenTracing/OpenCensus merger), publication trivia, Alertmanager routing config, Kubernetes
probe mechanics, queueing theory.

**Overlap avoided.** Resilience patterns (circuit breaker, bulkhead, backoff/jitter, retry budgets) stay in
*Distributed Systems & Data* 10; here only "retry at one layer" and deadline propagation from the SRE angle, with pointers.
*Kubernetes* 09 already has metric types, histogram vs summary, pull model, rate vs irate, PromQL p95, recording rules,
`for:`, Alertmanager, USE/RED cloze, OTel definitions (API/SDK, pipeline cloze, agent+gateway, OTLP, Resource,
semconv, head vs tail sampling, exemplar) and node_exporter vs kube-state-metrics vs metrics-server. This deck takes the
SLO/alerting angle instead: counter resets, extrapolation, SLO bucket edges, native histograms, staleness, cardinality
math, recording rules for burn rates, why tail sampling needs a trace-aware tier, exemplars for SLO alerts, Views,
temporality, spanmetrics, memory_limiter ordering, k8sattributes, Operator/Target Allocator, cAdvisor vs KSM.
Little's law and utilisation curves stay in *Quantitative Foundations* 09 (also "percentiles vs mean", so here only
"why percentiles don't average"). Progressive-delivery and GitOps mechanics stay in *Platform Engineering*; here only
canary statistics, bake time and feature flags as mitigation.
