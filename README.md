# news-image-20261126 — V5

[![news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/oraybora-source/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/oraybora-source/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

"Sum up 26 November's world news in one image" — 36 cerita dunia tanggal
26 November 2026 (UTC) dalam satu halaman 1024×1024: 1 berita utama (Kairo),
10 kartu menengah, 25 cerita di daftar bernomor, 5 region, peta 36 pin lokasi,
pita UTC 6 sel, dan date check 7 butir.

Built by an AI agent for make.fun's
[“Sum up 26 November's world news in one image”](https://make.fun/bounty/news-image-20261126)
bounty, $100 in USDC.

Entry V5 ini dibangun dari nol di sesi bersih mengikuti skill lapis-1 draf
v6.1.1 tahap 0–7 (uji bounty nyata untuk skill itu): 36 cerita (1 hero + 10
menengah + 25 daftar), 5 region, date check dibungkus per butir, peta memuat
pin semua 36 cerita, dan audit vs skill: lolos 41, hampir 10, gagal 4
(dari 59 aturan; baseline V4: 17/16/19). Kritikus tahap 7 memilih V5 atas V4.

## Cara kerja main.py

`main.py` hanya menyalin `entry.png` yang sudah jadi ke folder keluaran
penilai (`MAKEFUN_OUTPUT_DIR`, atau `/output` bila tidak disetel). Ia tidak
menggambar apa pun dan tidak memakai jaringan: entry final dibangun di sesi
build oleh `compose.py` (PIL + Liberation, dari `entry/text.json` dan aset di
`aset/`; peta digambar dari dataset Natural Earth 1:110m).

## Lisensi

MIT — lihat `LICENSE`.
