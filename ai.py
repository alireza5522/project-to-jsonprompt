import os
import json
from pathlib import Path
import pathspec

IGNORE_TEXT = """
__pycache__/
*.pyc
*.pyd
*.pyo
*.egg-info/
.pytest_cache/
env/
venv/
.env/
.idea/
.vscode/*
!.vscode/settings.json
*.swp
*.swo
*.bak
db.sqlite3
*.sqlite3-journal
media/
static_collected/
local_settings.py
.env
*.log
logs/
.DS_Store
Thumbs.db
.coverage
htmlcov/
dist/
build/
*.pot
/.git
/venv
node_modules/
migrations/
"""

TEXT_EXTENSIONS = {
    ".js",".jsx",".py"
}

spec = pathspec.PathSpec.from_lines("gitwildmatch", IGNORE_TEXT.strip().splitlines())

def is_probably_text_file(filepath: str) -> bool:

    ext = Path(filepath).suffix.lower()
    if ext in TEXT_EXTENSIONS:
        return True
    # try:
    #     with open(filepath, "rb") as f:
    #         chunk = f.read(2048)
    #     if b"\x00" in chunk:
    #         return False
    #     chunk.decode("utf-8")
    #     return True
    # except Exception:
    #     return False

def insert_nested(result, parts, content):
    cur = result
    for p in parts[:-1]:
        cur = cur.setdefault(p, {})
    cur[parts[-1]] = content

def folder_to_json(root_dir="."):
    result = {}
    for dirpath, _, filenames in os.walk(root_dir):
        rel_dir = os.path.relpath(dirpath, root_dir).replace("\\", "/")
        if rel_dir == ".":
            rel_dir = ""

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            relpath = (f"{rel_dir}/{filename}" if rel_dir else filename).replace("\\", "/")

            if spec.match_file(relpath):
                continue

            if not is_probably_text_file(filepath):
                continue

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                insert_nested(result, relpath.split("/"), content)
            except Exception as e:
                print(f"⚠️ cant read {relpath}: {e}")

    return result

if __name__ == "__main__":
    data = folder_to_json(".")
    with open("project_prompt.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("✅ nested project_prompt.json created")
