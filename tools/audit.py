from pathlib import Path
import xml.etree.ElementTree as ET
import re

root = Path(".")
svgs = list(root.glob("assets/**/*.svg"))
ok = True
for p in svgs:
    try:
        ET.parse(p)
    except Exception as e:
        print("INVALID", p, e)
        ok = False
print("svg_count", len(svgs), "xml_ok", ok)

readme = (root / "README.md").read_text(encoding="utf-8")
paths = re.findall(r"\./assets/[^\s\"'>]+", readme)
missing = [p for p in paths if not Path(p).exists()]
print("readme_asset_refs", len(paths), "missing", missing)

urls = sorted(set(re.findall(r"https://[^\s\"')]+", readme)))
print("external_urls")
for u in urls:
    print(" ", u)

wf = Path(".github/workflows/snake.yml")
text = wf.read_text(encoding="utf-8")
for key in ("workflow_dispatch", "schedule", "contents: write", "Platane/snk/svg-only@v3", "subrata-code"):
    print("workflow", key, key in text)
