#!/usr/bin/env python3
"""Program entry V5 ni26 — ditulis baru di sesi build V5.

Hanya menyalin entry.png yang sudah jadi ke folder keluaran penilai.
Pustaka standar saja: tanpa jaringan, tanpa font, tanpa alat sistem.
Hasilnya deterministik: byte yang disalin sama di setiap run.
"""
import os
import shutil
import sys

NAMA = "entry.png"
# Delapan byte pertama sebuah PNG yang sah.
AWALAN_PNG = b"\x89PNG\r\n\x1a\n"


def salin():
    folder = os.path.dirname(os.path.abspath(__file__))
    asal = os.path.join(folder, NAMA)
    if not os.path.isfile(asal):
        print(f"main.py: {NAMA} tidak ada di {folder}", file=sys.stderr)
        return 1
    with open(asal, "rb") as f:
        kepala = f.read(8)
    if kepala != AWALAN_PNG:
        print(f"main.py: {asal} bukan PNG yang sah", file=sys.stderr)
        return 1
    tujuan_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(tujuan_dir, exist_ok=True)
    tujuan = os.path.join(tujuan_dir, NAMA)
    shutil.copyfile(asal, tujuan)
    os.chmod(tujuan, 0o644)
    if os.path.getsize(tujuan) != os.path.getsize(asal):
        print("main.py: ukuran salinan tidak sama dengan sumber", file=sys.stderr)
        return 1
    with open(tujuan, "rb") as f:
        kepala_tujuan = f.read(8)
    if kepala_tujuan != AWALAN_PNG:
        print("main.py: salinan rusak (bukan PNG yang sah)", file=sys.stderr)
        return 1
    print(f"main.py: {asal} -> {tujuan} ({os.path.getsize(tujuan)} byte)")
    return 0


if __name__ == "__main__":
    sys.exit(salin())
