"""Entry ni26 V3: salin entry.png yang sudah jadi ke folder keluaran.

Hanya memakai pustaka standar, tanpa jaringan dan tanpa font.
Cara build: pindah ke folder ini lalu jalankan compose.py.
"""

import os
import shutil
import sys

ENTRY_NAME = "entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print("galat: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, ENTRY_NAME)
    if not os.path.isfile(source):
        fail(
            "berkas %s tidak ditemukan di %s (folder %s). "
            "Bangun dulu dengan perintah: cd %s && python3 compose.py"
            % (ENTRY_NAME, source, here, here)
        )
    try:
        with open(source, "rb") as fh:
            head = fh.read(8)
    except OSError as exc:
        fail("tidak bisa membaca %s: %s" % (source, exc))
    if head != PNG_SIGNATURE:
        found = "kosong" if not head else "0x" + head.hex()
        fail(
            "berkas %s bukan PNG yang sah "
            "(8 byte pertama %s, bukan tanda tangan PNG 0x89504e470d0a1a0a)."
            % (source, found)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        fail("tidak bisa membuat folder keluaran %s: %s" % (out_dir, exc))
    dest = os.path.join(out_dir, ENTRY_NAME)
    try:
        shutil.copyfile(source, dest)
        os.chmod(dest, 0o644)
    except OSError as exc:
        fail("tidak bisa menyalin %s ke %s: %s" % (source, dest, exc))
    try:
        src_size = os.path.getsize(source)
        dst_size = os.path.getsize(dest)
    except OSError as exc:
        fail("tidak bisa memeriksa ukuran salinan %s: %s" % (dest, exc))
    if src_size != dst_size:
        fail(
            "ukuran salinan %s (%d byte) tidak sama dengan sumber %s (%d byte)"
            % (dest, dst_size, source, src_size)
        )
    print("disalin %s -> %s (%d byte)" % (source, dest, dst_size))


if __name__ == "__main__":
    main()
