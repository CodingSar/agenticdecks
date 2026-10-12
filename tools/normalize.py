"""Extract every .apkg in the repo root into normalized JSON (work/source/<deck>.json)."""
import sqlite3, json, glob, os, sys, zipfile, tempfile, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONT = {"Front", "Question", "Vraag", "Element", "Name"}
BACK = {"Back", "Answer", "Antwoord", "Definition"}
TEXT = {"Text", "Tekst"}
IMAGE = {"Image", "Figure", "Notation"}
ANALOGY = {"Analogy", "Intuition"}
SOURCE = {"Source", "Bron", "Chapter", "Topic", "Exam", "Section", "Module", "Category", "Tag", "Tags", "TagsLine"}
EXTRA_LABEL = {"Extra": "", "Notes": "", "Example": "Example", "Investor": "Investor lens", "Connection": "Connection",
               "InPractice": "In practice", "Grounding": "Grounding", "Geometry": "Geometry", "Incident": "Incident",
               "Layer": "Layer", "Aspect": "Aspect", "LineStyle": "Line style"}

def normalize(path, outdir, mediadir):
    name = os.path.basename(path)[:-5]
    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(path) as z:
        z.extractall(tmp)
    media = json.load(open(os.path.join(tmp, "media")))
    for k, v in media.items():
        shutil.copy(os.path.join(tmp, k), os.path.join(mediadir, v))
    c = sqlite3.connect(os.path.join(tmp, "collection.anki2"))
    models = json.loads(c.execute("select models from col").fetchone()[0])
    decks = json.loads(c.execute("select decks from col").fetchone()[0])
    notes = []
    for nid, guid, mid, tags, flds in c.execute("select id,guid,mid,tags,flds from notes order by id"):
        m = models[str(mid)]
        vals = dict(zip([f["name"] for f in m["flds"]], flds.split("\x1f")))
        did = c.execute("select did from cards where nid=? order by ord limit 1", (nid,)).fetchone()[0]
        n = {"guid": guid, "type": "cloze" if m["type"] == 1 else "basic", "deck": decks[str(did)]["name"],
             "tags": tags.split(), "front": "", "back": "", "text": "", "image": "", "analogy": "", "extra": "", "source": ""}
        extras, sources = [], []
        for k, v in vals.items():
            v = v.strip()
            if not v: continue
            if k in FRONT: n["front"] = v
            elif k in BACK: n["back"] = v
            elif k in TEXT: n["text"] = v
            elif k in IMAGE: n["image"] = v
            elif k in ANALOGY: n["analogy"] = v
            elif k in SOURCE: sources.append(v)
            elif k in EXTRA_LABEL:
                extras.append((f"<b>{EXTRA_LABEL[k]}:</b> " if EXTRA_LABEL[k] else "") + v)
            else:
                extras.append(f"<b>{k}:</b> {v}")
        n["extra"] = "<br><br>".join(extras)
        n["source"] = " · ".join(dict.fromkeys(sources))
        if len(m["tmpls"]) > 1 and n["image"]:
            n["reverse"] = True  # also ask image -> name
        notes.append(n)
    json.dump({"source_file": os.path.basename(path), "notes": notes}, open(os.path.join(outdir, name + ".json"), "w"), indent=1, ensure_ascii=False)
    shutil.rmtree(tmp)
    return name, len(notes)

if __name__ == "__main__":
    out = os.path.join(ROOT, "work/source"); med = os.path.join(ROOT, "media")
    os.makedirs(out, exist_ok=True); os.makedirs(med, exist_ok=True)
    for p in sorted(glob.glob(os.path.join(ROOT, "*.apkg"))):
        print(*normalize(p, out, med))
