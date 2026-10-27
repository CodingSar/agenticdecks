"""Validate edited decks. Usage: validate.py [deck_id ...]  (default: all)
Checks schema (tools/check.py), identifier preservation against the base commit, prints before/after counts."""
import os, sys, subprocess, json
from common import *

BASE = os.environ.get("SIMPLIFY_BASE", "deck-simplification-base")

def base_ids(did):
    r = subprocess.run(["git", "show", f"{BASE}:work/out/{did}.json"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode: return None, None
    d = json.loads(r.stdout)
    return [card_id(d["deck_name"], n) for n in d["notes"]], d

def main():
    ids = sys.argv[1:] or [deck_id_of(p) for p in deck_files()]
    ok = True
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "check.py")] + [os.path.join(OUT, i + ".json") for i in ids],
                       capture_output=True, text=True)
    errs = [l for l in r.stdout.splitlines() if not l.startswith(("  WARN",)) and "notes," not in l and not l.startswith("ERRORS")]
    if r.returncode: ok = False; print("\n".join(errs[:30]))
    gone = {}
    for did in ids:
        d = load(os.path.join(OUT, did + ".json")); cur = [card_id(d["deck_name"], n) for n in d["notes"]]
        if any(not n.get("guid") for n in d["notes"]): ok = False; print(did, "FAIL: note without explicit guid")
        if len(set(cur)) != len(cur): ok = False; print(did, "FAIL: duplicate guids inside deck")
        old, _ = base_ids(did)
        lost = sorted(set(old) - set(cur)) if old else []
        print(f"{did}: {len(old) if old else '?'} -> {len(cur)} cards, {len(lost)} ids absent, {len(set(cur) - set(old or []))} new")
        gone[did] = lost
    os.makedirs(os.path.join(SCRATCH, "absent"), exist_ok=True)
    for did, lost in gone.items(): json.dump(lost, open(os.path.join(SCRATCH, "absent", did + ".json"), "w"))
    print("OK" if ok else "FAILED"); sys.exit(0 if ok else 1)
main()
