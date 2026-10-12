"""Build one .apkg per work/out/*.json into decks/. Usage: build.py [file ...]"""
import json, glob, os, re, sys, hashlib, genanki
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSS = """
.card{font-family:-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:19px;line-height:1.45;
 color:#1f2328;background:#fbfbfa;text-align:left;max-width:680px;margin:0 auto;padding:18px 20px}
.src{display:inline-block;font-size:12px;letter-spacing:.04em;text-transform:uppercase;color:#6e7781;
 border:1px solid #d0d7de;border-radius:999px;padding:2px 10px;margin-bottom:12px}
.q{font-size:21px;font-weight:600}
.a{margin-top:6px}
hr#answer{border:none;border-top:1px solid #d0d7de;margin:16px 0}
.box{margin-top:14px;padding:10px 14px;border-radius:8px;font-size:16px}
.analogy{background:#fff8e6;border-left:4px solid #d4a72c}
.extra{background:#eef4fb;border-left:4px solid #4a78b5}
.box .lbl{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;opacity:.7;display:block;margin-bottom:2px}
.img{text-align:center;margin-top:12px}.img img{max-width:100%;max-height:340px}
.cloze{font-weight:700;color:#0b62c4}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.9em;background:#eaeef2;padding:1px 5px;border-radius:4px}
ul,ol{margin:6px 0;padding-left:22px} b{color:#0b3d7a}
.nightMode .card,.night_mode .card{background:#1d1f23;color:#e6e6e6}
.nightMode .src{color:#9aa4ae;border-color:#3d444d}
.nightMode hr#answer{border-color:#3d444d}
.nightMode .analogy{background:#3a3220;border-color:#d4a72c}
.nightMode .extra{background:#1f2c3d;border-color:#5b8fd6}
.nightMode .cloze{color:#6cb6ff}.nightMode b{color:#9cc7ff}
.nightMode code{background:#2d333b}
.nightMode .img img{background:#fff;border-radius:6px;padding:4px}
"""
SRC = "{{#Source}}<div class='src'>{{Source}}</div><br>{{/Source}}"
BOXES = ("{{#Image}}<div class='img'>{{Image}}</div>{{/Image}}"
         "{{#Analogy}}<div class='box analogy'><span class='lbl'>Analogy</span>{{Analogy}}</div>{{/Analogy}}"
         "{{#Extra}}<div class='box extra'><span class='lbl'>Context</span>{{Extra}}</div>{{/Extra}}")

BASIC = genanki.Model(1720001001, "Agentic Basic",
    fields=[{"name": f} for f in ("Front", "Back", "Image", "Analogy", "Extra", "Source", "Reverse")],
    templates=[
        {"name": "Forward", "qfmt": SRC + "<div class='q'>{{Front}}</div>",
         "afmt": "{{FrontSide}}<hr id='answer'><div class='a'>{{Back}}</div>" + BOXES},
        {"name": "Reverse", "qfmt": "{{#Reverse}}" + SRC + "<div class='q'>Name this:</div>"
         "{{#Image}}<div class='img'>{{Image}}</div>{{/Image}}{{^Image}}<div class='a'>{{Back}}</div>{{/Image}}{{/Reverse}}",
         "afmt": "{{FrontSide}}<hr id='answer'><div class='q'>{{Front}}</div>{{#Image}}<div class='a'>{{Back}}</div>{{/Image}}"
         "{{#Extra}}<div class='box extra'><span class='lbl'>Context</span>{{Extra}}</div>{{/Extra}}"},
    ], css=CSS)
CLOZE = genanki.Model(1720001002, "Agentic Cloze", model_type=genanki.Model.CLOZE,
    fields=[{"name": f} for f in ("Text", "Image", "Analogy", "Extra", "Source")],
    templates=[{"name": "Cloze", "qfmt": SRC + "<div class='q' style='font-weight:400'>{{cloze:Text}}</div>",
                "afmt": SRC + "<div class='q' style='font-weight:400'>{{cloze:Text}}</div><hr id='answer'>" + BOXES}],
    css=CSS)

def deck_id(name): return int(hashlib.sha1(name.encode()).hexdigest()[:8], 16) + 1 << 1

def build(path, outdir):
    d = json.load(open(path)); decks = {}; media = set()
    for n in d["notes"]:
        dk = decks.setdefault(n["deck"], genanki.Deck(deck_id(n["deck"]), n["deck"],
                                                     description=d["description"] if n["deck"] == d["deck_name"] else ""))
        if n["type"] == "cloze":
            f = [n["text"], n.get("image", ""), n.get("analogy", ""), n.get("extra", ""), n.get("source", "")]
            model = CLOZE
        else:
            f = [n["front"], n["back"], n.get("image", ""), n.get("analogy", ""), n.get("extra", ""), n.get("source", ""),
                 "y" if n.get("reverse") else ""]
            model = BASIC
        guid = n.get("guid") or genanki.guid_for(d["deck_name"], *f[:2])
        dk.add_note(genanki.Note(model=model, fields=f, tags=n.get("tags", []), guid=guid))
        media.update(re.findall(r"src=[\"']([^\"']+)", "".join(f)))
    if d["deck_name"] not in decks:  # make sure the parent deck carries the description
        decks[d["deck_name"]] = genanki.Deck(deck_id(d["deck_name"]), d["deck_name"], description=d["description"])
    pkg = genanki.Package(list(decks.values()))
    pkg.media_files = [os.path.join(ROOT, "media", m) for m in sorted(media)]
    pkg.write_to_file(os.path.join(outdir, d["file"]))
    return d["file"], len(d["notes"])

if __name__ == "__main__":
    out = os.path.join(ROOT, "decks"); os.makedirs(out, exist_ok=True)
    for p in sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, "work/out/*.json"))):
        print(*build(p, out))
