# OA Tam-Metin PDF İndirme Raporu

> Çalıştırma: 2026-06-20 · Ortam: bulut/cowork sandbox (egress allowlist'li)
> Hedef klasör: `projects/yz-yabancidil-derleme/pdf/` (**yalnız yerelde; repoya gitmedi**)
> Doğrulama: her dosya ilk 4 bayt `%PDF` + pypdf ile sayfa sayısı kontrolü (truncated/HTML reddedildi)

## ✅ İNEN — 14 / 29 OA (doğrulandı)
| # | Dosya | Boyut | Sayfa | Kaynak |
|---|---|---|---|---|
| 08 | 08_Park_2026.pdf | 1.3M | 17 | Springer Open (content/pdf) |
| 11 | 11_Michelson_2026.pdf | 992K | 28 | eScholarship |
| 12 | 12_Bataineh_2026.pdf | 632K | 16 | JITE |
| 16 | 16_Karakaya_2025.pdf | 568K | 19 | ERIC |
| 17 | 17_Setiyawan_2025.pdf | 688K | 15 | UIN Malang OJS (galley) |
| 25 | 25_Mizumoto_2025.pdf | 600K | 18 | Cambridge Core (OA pdf) |
| 26 | 26_Pack_2023.pdf | 232K | 21 | ERIC |
| 32 | 32_Williyan_2024.pdf | 220K | 17 | ERIC |
| 34 | 34_Zaiarna_2024.pdf | 940K | 16 | IITTA OJS (galley) |
| 37 | 37_GetinoDiez_2026.pdf | 644K | 21 | Castledown |
| 39 | 39_NguyenPT_2024.pdf | 836K | 27 | EnPress |
| 44 | 44_Haristiani_2019.pdf | 1.2M | 16 | JESTEC |
| 47 | 47_Bonner_2023.pdf | 708K | 19 | ERIC |
| 54 | 54_Katsarou_2023.pdf | 1.2M | 21 | online-journals.org OJS (galley) |

Toplam: ~11 MB, 14 dosya. Hepsi geçerli PDF (HTML/eksik dosya yok).

## ❌ İNMEYEN OA — 15 / 29 (bu ortamın IP'si yayıncı tarafından engelli / host ulaşılamaz)
Bunlar **OA (ücretsiz)** ama bu bulut sunucusunun IP'si yayıncı bot-duvarına takıldığı veya
host sandbox'tan ulaşılamadığı için inmedi. **Vetis'e gerek yok** — kullanıcı kendi tarayıcısı +
Zotero Connector ile saniyeler içinde indirebilir.

| # | Yazar-Yıl | Neden inmedi | Doğrudan link |
|---|---|---|---|
| 03 | Ngo 2026 | Taylor & Francis → HTTP 403 (IP engeli) | https://www.tandfonline.com/doi/full/10.1080/17501229.2026.2662397 |
| 07 | Lenko-Szymanska 2026 | ScienceDirect → 403 (PerimeterX) | https://www.sciencedirect.com/science/article/pii/S2666799125000504 |
| 14 | Zheng 2024 | ScienceDirect → 403 | https://www.sciencedirect.com/science/article/pii/S2666920X24000249 |
| 38 | Law 2024 | ScienceDirect → 403 | https://www.sciencedirect.com/science/article/pii/S2666557324000156 |
| 51 | Zhai 2023 | ScienceDirect → 403 | https://www.sciencedirect.com/science/article/pii/S2666920X23000139 |
| 46 | Li 2023 | MDPI → 403 "Access Denied" (IP engeli; headless Chromium de geçemedi) | https://www.mdpi.com/2226-471X/8/3/197 |
| 50 | Mageira 2022 | MDPI → 403 "Access Denied" | https://www.mdpi.com/2076-3417/12/7/3239 |
| 48 | Huang 2022 | Wiley → 403 (IP engeli) | https://onlinelibrary.wiley.com/doi/10.1111/jcal.12610 |
| 23 | Wu 2025 | ResearchGate → 403 (giriş duvarı) | https://www.researchgate.net/publication/395280021 |
| 28 | Ursa 2025 | ResearchGate → 403 | https://www.researchgate.net/publication/392604404 |
| 42 | Fryer 2019 | ResearchGate → 403 | https://www.researchgate.net/publication/329749402 |
| 22 | Wardat 2025 | bilpubgroup host bu IP'yi ~6 KB/s'ye kısıyor, ~260 KB'da kopuyor (dosya 1.1 MB; tamamlanamadı). Truncated kopya silindi. | https://journals.bilpubgroup.com/index.php/fls/article/view/9644 |
| 41 | Haristiani 2020 | kjpupi.id linki artık 404 (IJOST host değiştirmiş) → ejournal.upi.edu'da ara | https://ejournal.upi.edu/index.php/ijost (Vol.5'te ara) |
| 43 | Haristiani 2021 | ejournal.upi.edu sandbox'tan ulaşılamadı (HTTP 000) | https://ejournal.upi.edu/index.php/ijost/article/view/39150 |
| 10 | Guo 2026 | IJACSA Vol.17/4 henüz indekslenmedi (GOLD-bekliyor) | https://thesai.org/Publications/IJACSA |

> Not: 22, 41, 43 **gerçek OA** ve kullanıcının kendi ağından kolayca iner; sorun yalnız bu
> sandbox'ın IP/erişim kısıtı. 46/50 (MDPI) için headless Chromium da denendi, IP "Access Denied".

## 🔒 KAPALI — vetis/kütüphane gerekli (18, dokunulmadı)
`1, 2, 4, 5, 6, 9, 15, 18, 20, 21, 27, 29, 30, 31, 40, 45, 52, 53`

Talimat gereği bu paywall makalelere dokunulmadı. İki "hızlı dene" ipucu sonucu:
- **#21 Liu** — listede önerilen ERIC EJ1457846 kaydı `files.eric.ed.gov`'da **404** (tam metin yok) → vetis.
- **#4 Xu** — ERIC'te tam metin bulunamadı; ResearchGate 403 → vetis.

## Özet
- **İnen (yerelde, doğrulanmış): 14**
- **İnmeyen OA (kullanıcının ağından alınmalı): 15** → öncelik kolayları: 03, 07, 14, 22, 38, 41, 43, 46, 48, 50, 51
- **Kapalı (vetis): 18** → 1,2,4,5,6,9,15,18,20,21,27,29,30,31,40,45,52,53
- PDF'ler repoya **yüklenmedi**; yalnız bu rapor commit'lendi.
