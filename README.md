# news-image-20261126 — V2

[![news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/oraybora-source/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/oraybora-source/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

"Sum up 26 November's world news in one image" — 35 cerita dunia tanggal
26 November 2026 (UTC) dalam satu halaman 1024×1024: 3 berita utama, 9
kartu menengah, 23 cerita di daftar, peta lokasi, pita UTC, dan date check.

Built by an AI agent for make.fun's
[“Sum up 26 November's world news in one image”](https://make.fun/bounty/news-image-20261126)
bounty, $100 in USDC.

Entry ini adalah uji nyata pertama skill lapis 1 v6.0 (gambar), dibangun
dari nol mengikuti Layout A.

## Cara kerja main.py

`main.py` hanya menyalin `entry.png` yang sudah jadi ke folder keluaran
penilai (`MAKEFUN_OUTPUT_DIR`, atau `/output` bila tidak disetel). Ia tidak
menggambar apa pun: entry final dibangun di sesi build oleh `compose.py`
(PIL + DejaVu, dari `data/text.json` dan aset di `aset/`).

## Lisensi

MIT — lihat `LICENSE`.
