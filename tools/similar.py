"""SIMDIR=work/out SIMV=-v python3 tools/similar.py 0.5 → list pairs. Find near-duplicate notes across decks (TF-IDF cosine on front+back). Usage: similar.py [threshold] [deck ...]"""
import json, glob, os, re, sys, math
from collections import Counter, defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
thr = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
only = set(sys.argv[2:])
def toks(s):
    s = re.sub(r"<[^>]+>|&\w+;", " ", s.lower())
    return [w for w in re.findall(r"[a-z0-9][a-z0-9\-]{2,}", s) if w not in STOP]
STOP = set("the and for what with that this are from which into does how its why when your you not can than they their them use used using one two each more most also between".split())
docs = []
for p in sorted(glob.glob(os.path.join(ROOT, os.environ.get("SIMDIR", "work/source") + "/*.json"))):
    d = os.path.basename(p)[:-5]
    if only and d not in only: continue
    for n in json.load(open(p))["notes"]:
        docs.append((d, n["guid"], n["front"] or n["text"], Counter(toks((n["front"] or n["text"]) + " " + (n["back"] or "")))))
df = Counter(w for *_, c in docs for w in c)
N = len(docs)
vecs = []
for d, g, f, c in docs:
    v = {w: (1 + math.log(k)) * math.log(N / df[w]) for w, k in c.items()}
    nrm = math.sqrt(sum(x * x for x in v.values())) or 1
    vecs.append({w: x / nrm for w, x in v.items()})
inv = defaultdict(list)
for i, v in enumerate(vecs):
    for w in v: inv[w].append(i)
pairs = Counter()
for i, v in enumerate(vecs):
    sc = defaultdict(float)
    for w, x in v.items():
        if df[w] > 200: continue
        for j in inv[w]:
            if j > i: sc[j] += x * vecs[j][w]
    for j, s in sc.items():
        if s >= thr: pairs[(i, j)] = s
deckpair = Counter()
for (i, j), s in sorted(pairs.items(), key=lambda x: -x[1]):
    deckpair[tuple(sorted((docs[i][0], docs[j][0])))] += 1
    if "-v" in os.environ.get("SIMV", ""):
        print(f"{s:.2f} [{docs[i][0]}] {docs[i][2][:90]}\n     [{docs[j][0]}] {docs[j][2][:90]}")
for k, v in deckpair.most_common(80): print(v, *k)
