# news-image-20261126 — V4

[![news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/oraybora-source/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/oraybora-source/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

"Sum up 26 November's world news in one image" — 36 cerita dunia tanggal
26 November 2026 (UTC) dalam satu halaman 1024×1024: 3 berita utama, 10
kartu menengah, 23 cerita di daftar, 9 region, peta 13 pin lokasi, pita
UTC 6 sel, dan date check 10 butir.

Built by an AI agent for make.fun's
[“Sum up 26 November's world news in one image”](https://make.fun/bounty/news-image-20261126)
bounty, $100 in USDC.

Entry V4 ini dibangun dari nol di sesi bersih mengikuti spesifikasi prosa
V4: 36 cerita (bertambah satu dari V3: bantahan Senegal 26 Nov), 9 region
(V3: 5), date check 10 butir (V3: 5), strip UTC 6 sel (V3: 5), dan peta
yang hanya memuat pin cerita 1–13 (V3: semua 35).

## Cara kerja main.py

`main.py` hanya menyalin `entry.png` yang sudah jadi ke folder keluaran
penilai (`MAKEFUN_OUTPUT_DIR`, atau `/output` bila tidak disetel). Ia tidak
menggambar apa pun: entry final dibangun di sesi build oleh `compose.py`
(PIL + DejaVu, dari `data/text.json` dan aset di `aset/`; peta digambar
oleh generator peta dari dataset Natural Earth 1:110m).

## Lisensi

MIT — lihat `LICENSE`.
