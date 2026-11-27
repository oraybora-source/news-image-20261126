#!/usr/bin/env python3
"""V9 entry program: copy the pre-rendered image to the output directory.
Build: uji skill Lapis 1 v6.8.1, dari nol, 27 Nov 2026.

The image (entry.png) is the finished front page for Thursday
26 November 2026, drawn by the build program in the build session.
This program only copies it, so it runs identically twice, uses only
the standard library, and needs no network, fonts, or binaries.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isfile(SRC):
        print(f"error: required file missing: {SRC}", file=sys.stderr)
        print("the repository must contain entry.png beside main.py",
              file=sys.stderr)
        return 2
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
