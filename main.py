"""Program entry V3 ni26 — penyalin-saja (rebuild dari nol).

Menyalin entry.png yang sudah jadi (dibangun di sesi build oleh
compose.py) ke folder keluaran penilai. Pustaka standar saja (os,
shutil, sys): tanpa PIL, tanpa font sistem, tanpa jaringan, tanpa
pemeriksaan hash sendiri.

Folder keluaran: MAKEFUN_OUTPUT_DIR bila disetel, kalau tidak /output.
Izin hasil salinan: 0o644. Bila entry.png tidak ada, keluar dengan
pesan galat yang jelas. Sebelum menyalin, isi entry.png diperiksa:
harus berkas PNG yang tidak kosong (tanda tangan PNG 8 byte);
berkas kosong atau bukan PNG ditolak dengan pesan galat sendiri,
supaya penilai tidak menerima salinan rusak. Setelah menyalin,
ukuran hasil dibandingkan dengan sumber; bila tidak sama, keluar
dengan galat.
"""
import os
import shutil
import sys

ENTRY = "entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ENTRY)
    if not os.path.isfile(src):
        print("error: %s tidak ditemukan (dicari di %s, direktori tempat "
              "main.py berjalan); bangun dulu entry final dengan perintah "
              "'cd %s && python3 compose.py', lalu jalankan lagi main.py"
              % (ENTRY, src, here), file=sys.stderr)
        sys.exit(1)
    try:
        with open(src, "rb") as fh:
            head = fh.read(len(PNG_SIGNATURE))
    except OSError as exc:
        print("error: tidak bisa membaca %s: %s" % (src, exc),
              file=sys.stderr)
        sys.exit(1)
    if head != PNG_SIGNATURE:
        print("error: %s bukan berkas PNG yang valid (tanda tangan PNG "
              "tidak cocok atau berkas kosong); bangun ulang entry dengan "
              "compose.py" % src, file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print("error: tidak bisa membuat folder keluaran %s: %s"
              % (out_dir, exc), file=sys.stderr)
        sys.exit(1)
    dst = os.path.join(out_dir, ENTRY)
    try:
        shutil.copyfile(src, dst)
        os.chmod(dst, 0o644)
    except OSError as exc:
        print("error: gagal menyalin %s ke %s: %s" % (src, dst, exc),
              file=sys.stderr)
        sys.exit(1)
    if os.path.getsize(dst) != os.path.getsize(src):
        print("error: ukuran salinan %s (%d byte) tidak sama dengan sumber "
              "%s (%d byte); salinan tidak lengkap"
              % (dst, os.path.getsize(dst), src, os.path.getsize(src)),
              file=sys.stderr)
        sys.exit(1)
    print("disalin: %s -> %s" % (src, dst))


if __name__ == "__main__":
    main()
