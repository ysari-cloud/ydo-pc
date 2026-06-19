# COWORK GÖREVİ — 47 dahil makalenin tam-metin PDF'lerini topla

Sen yerel PC'deki Claude Code'sun (ağ erişimin açık). Bu, bir sistematik derlemenin dahil edilen
47 makalesinin tam metnini toplama görevi. Kullanıcı yorgun; mümkün olduğunca çok şeyi
**tek başına, sormadan** hallet, sonunda tek rapor ver.

## 0) Hazırlık
```
cd <bu-repo>
git pull
```
Erişim haritası: `projects/yz-yabancidil-derleme/19-tam-metin-erisim-listesi.md`
(GOLD/GREEN = ücretsiz, doğrudan link var · CLOSED = paywall, vetis gerek)
DOI listesi: `projects/yz-yabancidil-derleme/araclar/zotero_doi_listesi.txt`

## 1) OA PDF'leri indir → `projects/yz-yabancidil-derleme/pdf/`
Adlandırma: `<n>_<Yazar>_<Yıl>.pdf` (örn. `16_Karakaya_2025.pdf`).
- Önce hazır script: `bash projects/yz-yabancidil-derleme/araclar/pdf_indir.sh`
  (ERIC/MDPI/Springer-Open/Cambridge-OA/OJS/Castledown/JESTEC/JITE/EnPress ~16 makaleyi çeker)
- Script'in "BAŞARISIZ → tarayıcı/Zotero" dediği **bot-korumalı OA** kaynaklar için DAHA ÇOK DENE:
  03 Ngo, 07 Lenko-Szymanska, 14 Zheng, 22 Wardat, 23 Wu, 28 Ursa, 34 Zaiarna, 38 Law,
  41 Haristiani20, 51 Zhai, 54 Katsarou.
  Bunlar ScienceDirect/T&F/Springer/RG/OJS — düz curl engellenebilir. Sırayla şunları dene:
  (a) gerçekçi User-Agent + Referer ile curl;
  (b) varsa `curl-impersonate` / `yt-dlp` değil ama **Playwright/Chromium headless** ile sayfayı aç,
      PDF linkini bul (genelde `.../pdf`, `/content/pdf/<doi>.pdf`, OJS `download/<id>/<galley>`),
      indir;
  (c) ScienceDirect-OA için: makale `pii` ile `https://www.sciencedirect.com/science/article/pii/<PII>/pdfft?isDTMRedir=true` dene;
  (d) MDPI için: `<makale-url>/pdf`; Springer-Open için `https://link.springer.com/content/pdf/<doi>.pdf`.
- Her indirilen dosyanın gerçekten PDF olduğunu doğrula (`file` veya ilk 4 bayt `%PDF`). HTML inmişse sil, başarısız say.

## 2) Kapalı (paywall) olanlara DOKUNMA — kullanıcıya bırak
Bunlar vetis/kütüphane girişi ister, script bypass edemez (yasal değil):
`1, 2, 4, 5, 6, 9, 15, 18, 20, 21, 27, 29, 30, 31, 40, 45, 52, 53`
(#4 Xu ve #21 Liu için önce hızlı bir ResearchGate/ERIC denemesi yap; CC/ERIC ipucu vardı.)

## 3) (Opsiyonel) Zotero'ya aktar
Kullanıcının Zotero'su kurulu (giriş: emre_sari). İstersen indirdiğin PDF'leri Zotero'ya da
ekleyebilirsin, ama ZORUNLU DEĞİL — öncelik `pdf/` klasörünü doldurmak.

## 4) Rapor (YALNIZ rapor commit'lenir — PDF'LER ASLA buluta gitmez)
⚠️ **PDF'leri repoya EKLEME/PUSH ETME.** PDF'ler yerel PC'de `pdf/` klasöründe kalacak
(depo şişmesin). `pdf/` zaten `.gitignore`'da; öyle kalsın.
- Sadece şu küçük markdown raporu commit'le:
  `projects/yz-yabancidil-derleme/araclar/_INDIRME_RAPORU.md` — hangi n indi (boyut),
  hangisi inmedi/neden, kullanıcının vetis'ten indireceği nihai kapalı liste.
- Push:
  `git add projects/yz-yabancidil-derleme/araclar/_INDIRME_RAPORU.md && git commit -m "akademik: OA PDF indirme raporu (PDF'ler yerelde)" && git push -u origin claude/youthful-franklin-wszezx`
  (Push ağ hatası verirse 2s/4s/8s/16s bekleyerek 4 kez dene.)

## Sınır
Sahte/eksik PDF koyma; HTML'i PDF diye kaydetme. Bulamadığını "bulunamadı" yaz, uydurma.
**PDF'ler yalnız yerel PC'de durur; buluta/repoya yüklenmez.** Sentez aşamasında tam metin
gerektiğinde kullanıcı ilgili PDF'i tek tek paylaşır.
