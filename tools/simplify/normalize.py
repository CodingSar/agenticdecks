"""Export every deck to work/cards/<deck_id>.jsonl.

  normalize.py --pin   write the build-derived guid into every note that lacks one
                       (build output is unchanged; edited cards keep their identity)
  normalize.py         export work/cards/<deck_id>.jsonl
Each line: {id, deck, front, back, tags, src, type, analogy, extra, source}.
"""
import os, sys, json
from common import *

def main():
    pin = "--pin" in sys.argv
    outdir = os.path.join(SCRATCH, "cards"); os.makedirs(outdir, exist_ok=True)
    for p in deck_files():
        d = load(p); did = deck_id_of(p); changed = 0
        for n in d["notes"]:
            if pin and not n.get("guid"):
                n["guid"] = computed_guid(d["deck_name"], n); changed += 1
        if changed: save(p, d)
        with open(os.path.join(outdir, did + ".jsonl"), "w") as f:
            for i, n in enumerate(d["notes"]):
                f.write(json.dumps({
                    "id": card_id(d["deck_name"], n), "deck": n["deck"],
                    "front": n["text"] if n["type"] == "cloze" else n["front"],
                    "back": "" if n["type"] == "cloze" else n["back"],
                    "tags": n.get("tags", []), "src": f"work/out/{did}.json#{i}", "type": n["type"],
                    "analogy": n.get("analogy", ""), "extra": n.get("extra", ""), "source": n.get("source", "")},
                    ensure_ascii=False) + "\n")
        print(did, len(d["notes"]), "pinned" if changed else "", changed or "")
main()
