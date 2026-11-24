"""Look things up while reviewing (the same tools the systems had).

    python3 pipeline/look.py pb 进口 恢复                PropBank rolesets of the lemmas (--lang en for English; others have none)
    python3 pipeline/look.py gl modal strength --max 3   passages of the full guidelines
    python3 pipeline/look.py ann zh-0005 进口-01 --max 5  training-data sentences with the keyword (never from zh-0005 itself)
"""
import os
import sys

PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PKG)
os.chdir(os.environ.get("TMPDIR", "/tmp"))      # tools/cli.py writes a call log into the current directory
from tools import cli  # noqa: E402

LANG = "zh"
if "--lang" in sys.argv:
    i = sys.argv.index("--lang")
    LANG = sys.argv[i + 1]
    del sys.argv[i:i + 2]
if len(sys.argv) < 3 or sys.argv[1] not in ("pb", "gl", "ann"):
    raise SystemExit(__doc__)
if sys.argv[1] == "pb":
    cli.main("propbank_lookup", "", ["--language", LANG] + sys.argv[2:])
elif sys.argv[1] == "gl":
    cli.main("search_guidelines", "", sys.argv[2:])
else:
    cli.main("search_annotations", sys.argv[2], ["--language", sys.argv[2].split("-")[0]] + sys.argv[3:])
