"""개인 참고자료의 로컬 위치만 확인한다. 네트워크 및 파일 쓰기 없음."""
import argparse
import json
import os
from pathlib import Path
import sys

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path)
    args = parser.parse_args()
    codex_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    explicit = args.root or os.environ.get("SUPER_REAL_IMAGEN_MATERIALS")
    candidates = [Path(explicit)] if explicit else [
        codex_home / "super-real-imagen-private" / "references",
        codex_home / "skills" / "super-real-imagen" / "references",
    ]
    for candidate in candidates:
        root = candidate.expanduser().resolve()
        pdfs = [root / "originals" / name for name in ("guidebook.pdf", "lecture.pdf")]
        if all(path.is_file() for path in pdfs):
            print(json.dumps({
                "root": str(root),
                "pdfs": [str(path) for path in pdfs],
                "source_map": str(root / "source-map.md") if (root / "source-map.md").is_file() else None,
                "pages": str(root / "pages") if (root / "pages").is_dir() else None,
            }, ensure_ascii=False, indent=2))
            return 0
    print("개인 자료를 찾지 못했습니다. --root 또는 SUPER_REAL_IMAGEN_MATERIALS로 자료 폴더를 지정하세요.")
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
