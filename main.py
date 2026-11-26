"""main.py — program entry V4 ni26. Ditulis baru di sesi ini.

Hanya menyalin entry.png yang sudah jadi ke folder keluaran.
Pustaka standar saja; tanpa jaringan, tanpa font.
"""

import os
import shutil
import sys

NAMA_BERKAS = "entry.png"
# Tanda tangan PNG: 137, 'PNG', CR, LF, 26, LF.
TANDA_TANGAN_PNG = b"\x89PNG\r\n\x1a\n"


def gagal(pesan):
    print(f"main.py: galat: {pesan}", file=sys.stderr)
    sys.exit(1)


def utama():
    folder = os.path.dirname(os.path.abspath(__file__))
    sumber = os.path.join(folder, NAMA_BERKAS)
    if not os.path.isfile(sumber):
        gagal(
            f"berkas {NAMA_BERKAS} tidak ditemukan di {sumber} "
            f"(folder main.py: {folder}). "
            "Bangun dulu: pindah ke folder itu lalu jalankan "
            "'python3 compose.py'."
        )
    try:
        with open(sumber, "rb") as f:
            awal = f.read(8)
    except OSError as e:
        gagal(f"tidak bisa membaca {sumber}: {e}")
    if awal != TANDA_TANGAN_PNG:
        gagal(
            f"{sumber} bukan berkas PNG yang sah "
            "(8 byte pertama tidak cocok dengan tanda tangan PNG). "
            "Bangun ulang dengan 'python3 compose.py'."
        )
    keluaran = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(keluaran, exist_ok=True)
    except OSError as e:
        gagal(f"tidak bisa membuat folder keluaran {keluaran}: {e}")
    tujuan = os.path.join(keluaran, NAMA_BERKAS)
    try:
        shutil.copyfile(sumber, tujuan)
        os.chmod(tujuan, 0o644)
    except OSError as e:
        gagal(f"tidak bisa menyalin {sumber} ke {tujuan}: {e}")
    ukuran_sumber = os.path.getsize(sumber)
    ukuran_tujuan = os.path.getsize(tujuan)
    if ukuran_sumber != ukuran_tujuan:
        gagal(
            f"ukuran salinan {ukuran_tujuan} byte tidak sama dengan "
            f"sumber {ukuran_sumber} byte."
        )
    try:
        with open(tujuan, "rb") as f:
            awal_tujuan = f.read(8)
    except OSError as e:
        gagal(f"tidak bisa membaca ulang salinan {tujuan}: {e}")
    if awal_tujuan != TANDA_TANGAN_PNG:
        gagal(
            f"salinan {tujuan} rusak: 8 byte pertamanya tidak cocok "
            "dengan tanda tangan PNG. Salin ulang."
        )
    print(f"main.py: disalin {sumber} -> {tujuan} ({ukuran_tujuan} byte)")


if __name__ == "__main__":
    utama()
