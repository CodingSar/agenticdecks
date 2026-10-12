"""Validate work/out/*.json against the schema in work/GUIDELINES.md. Usage: check.py [file ...]"""
import json, glob, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = set(os.listdir(os.path.join(ROOT, "media")))
KEYS = {"guid", "type", "deck", "tags", "front", "back", "text", "image", "analogy", "extra", "source", "reverse"}
def words(s): return len(re.sub(r"<[^>]+>|\\\(.*?\\\)", " ", s or "").split())
files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, "work/out/*.json")))
errs = 0; guids = {}
for p in files:
    d = json.load(open(p)); warn = []
    for k in ("deck_name", "file", "description", "notes"):
        if k not in d: print(f"{p}: missing top-level '{k}'"); errs += 1
    for i, n in enumerate(d.get("notes", [])):
        tag = f"{os.path.basename(p)}#{i}"
        bad = set(n) - KEYS
        if bad: print(tag, "unknown keys", bad); errs += 1
        if n.get("type") not in ("basic", "cloze"): print(tag, "bad type"); errs += 1
        if n.get("type") == "cloze" and not re.search(r"\{\{c\d+::", n.get("text", "")): print(tag, "cloze without deletion"); errs += 1
        if n.get("type") == "basic" and not (n.get("front") and n.get("back")): print(tag, "basic missing front/back"); errs += 1
        if not n.get("deck", "").startswith(d.get("deck_name", "")): print(tag, "deck not under deck_name:", n.get("deck")); errs += 1
        if not isinstance(n.get("tags", []), list) or any(" " in t for t in n.get("tags", [])): print(tag, "tags must be list without spaces"); errs += 1
        for src in re.findall(r"src=[\"']([^\"']+)", json.dumps(n).replace('\\"', '"')):
            if src not in MEDIA: print(tag, "missing media", src); errs += 1
        g = n.get("guid")
        if g:
            if g in guids: print(tag, "duplicate guid with", guids[g]); errs += 1
            guids[g] = tag
        w = words(n.get("back")) if n.get("type") == "basic" else words(re.sub(r"\{\{c\d+::(.*?)(::.*?)?\}\}", r"\1", n.get("text", "")))
        if w > 60: warn.append(f"{tag} long answer ({w} words): {(n.get('front') or n.get('text'))[:70]}")
        if words(n.get("extra")) > 80: warn.append(f"{tag} long extra ({words(n.get('extra'))} words)")
    print(f"{os.path.basename(p)}: {len(d.get('notes', []))} notes, {len(warn)} warnings")
    for w in warn[:40]: print("  WARN", w)
print("ERRORS:", errs); sys.exit(1 if errs else 0)
