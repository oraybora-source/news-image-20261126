#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261126 (Python 3.13, stdlib only).

The entry image is the file entry.png beside this program. This program
copies it to the evaluator's output folder: MAKEFUN_OUTPUT_DIR when set,
otherwise /output. It reads nothing else, uses no network, no system
binary, no system font and no third-party library. It always exits 0
on a successful copy and never inspects the copied bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    # Fail loudly (instead of a bare FileNotFoundError) if the image is missing.
    if not os.path.exists(src):
        raise SystemExit(f"entry.png not found beside main.py: {src}")
    shutil.copyfile(src, dst)
    os.chmod(dst, 0o644)


if __name__ == "__main__":
    main()
