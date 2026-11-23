"""Build dist/critical-thinking-junior.zip for upload to Gemini, Claude or any Agent Skills host.

SKILL.md sits at the root of the archive with references/ beside it, which is the layout
Gemini's Skills page and claude.ai both accept. The human-facing README.md is left out.

Usage: python build_zip.py
"""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL = ROOT / "skills" / "critical-thinking-junior"
OUT = ROOT / "dist" / "critical-thinking-junior.zip"
MAX_DESCRIPTION = 1024  # Gemini Enterprise rejects longer descriptions


def check_frontmatter() -> None:
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        sys.exit("SKILL.md has no YAML frontmatter")
    front = match.group(1)
    for field in ("name", "description"):
        if not re.search(rf"^{field}: \S", front, re.M):
            sys.exit(f"SKILL.md frontmatter is missing '{field}'")
    description = re.search(r"^description: (.*)$", front, re.M).group(1)
    if len(description) > MAX_DESCRIPTION:
        sys.exit(f"description is {len(description)} characters; the limit is {MAX_DESCRIPTION}")


def main() -> None:
    check_frontmatter()
    files = [SKILL / "SKILL.md", *sorted((SKILL / "references").glob("*.md"))]
    OUT.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(f, f.relative_to(SKILL).as_posix())  # forward slashes, whatever the OS
    print(f"Wrote {OUT.relative_to(ROOT)}:")
    for f in files:
        print("  " + f.relative_to(SKILL).as_posix())


if __name__ == "__main__":
    main()
