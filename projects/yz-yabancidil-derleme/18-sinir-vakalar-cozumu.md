# Sınır Vakaların Çözümü — Derin-Arama Adjudikasyonu (10 kayıt)

> 3-YZ triangülasyonundan çıkan 10 tartışmalı kayıt, geniş-özet + çoklu-kaynak derin-arama ile
> çözüldü (Claude WebSearch + 3 paralel ajan, 2026-06-19). Tam-metin PDF'leri bulut ağında 403'lü;
> kararlar yayıncı özet sayfası + ERIC/ResearchGate/DOAJ/PubMed snippet'lerinden çapraz doğrulandı.
> **Bunlar ÖNERİdir; karar otoritesi İnsan tarayıcıdır (Screener-1), tam-metinde teyit edilecek.**

## Çözüm tablosu
| # | Yazar-Yıl | Karar | Güven | Belirleyici olgu |
|---|---|---|:---:|---|
| 4 | Xu T. 2025 | **INCLUDE** | high | AIIV: GPT+TTS+lip-sync hattıyla üretim; 76 öğrenci **İngilizce kelime** → dil-eğitimi kesin (C1d) |
| 13 | Lin 2025 | **EXCLUDE** | high | **TAM METİN okundu (24s):** RQ1/RQ2 tamamen öğrenci-odaklı (YZ kullanımı + öğrenci çıktısı); bulgular öğrenci kompozisyonu. Öğretmen materyal co-development yalnız 1 yöntem cümlesi, analiz edilmiyor (öğrenci 220 vs öğretmen 50 geçiş). 19/35 ile aynı öğrenen-kutbu → tutarlılık gereği DIŞLA |
| 19 | Risang Baskara 2024 | EXCLUDE | high | Öğrenci-üretimi podcast; öğretmen materyal üretimi yok (öğrenen kutbu) |
| 24 | Bal 2024 | EXCLUDE | high | Yalnız opinion mining + duygu analizi (66 video); tutum ölçümü |
| 25 | Mizumoto 2025 | **INCLUDE** | high | Auto Error Analyzer (Llama 3.3) **araç geliştirme+doğrulama**; kural-3 "aracın geliştirilmesi" |
| 29 | Bao 2026 | **INCLUDE** | high | Tam başlık "...for **EFL** content generation"; RAG+çok-ajan ile ortaokul EFL alıştırma üretimi — dile özgü |
| 35 | Guo 2026 | EXCLUDE | high | Öğrenci GFL yazma çıktısı + rubrik puanlama; materyal üretimi yok |
| 36 | Karaceper 2026 | EXCLUDE | high | Yalnız ChatGPT-4o otomatik PUANLAMA (240 essay, IELTS rubrik); materyal üretimi yok |
| 46 | Li 2023 | **INCLUDE** | high | Netnografi (140 video); **üretim pratikleri + locus kayması + eğitimci failliği** (RQ5 çekirdek) |
| 56 | Nugroho 2023 | EXCLUDE | high | Yalnız öğrenci algı/fayda görüşü (18 öğrenci) |

**Sınır vaka sonucu:** INCLUDE 4 {4,25,29,46} · EXCLUDE 6 {13,19,24,35,36,56}

## Güncellenmiş N (provizyonel, insan teyidi öncesi)
- 3/3 sağlam INCLUDE: 43
- Sınır → INCLUDE: +4 (4,25,29,46)
- **TOPLAM DAHİL = 47**
- DIŞLA = 9 → {13, 19, 24, 33, 35, 36, 49, 55, 56}
- (43+4)+(3+6) = 47+9 = 56 ✓
- **#13 Lin tam metinle çözüldü (EXCLUDE) → artık "med"/belirsiz kayıt KALMADI; 10 sınır vakanın hepsi yüksek güvenle karara bağlı.**

> Not: N=48, Claude'un katı(B) varyantıyla **sayıca** aynı ama **bileşimce farklı** — B konuşma-kutbunu
> (31,41,42,45) dışlıyordu; bu çözüm konuşma-kutbunu A gereği DAHİL tutup bunun yerine öğrenen-kutbu
> (19,35) + tutum (24,56) + puanlama (36) dışlıyor.

## Tam-metin durumu
- **#13 Lin: ÇÖZÜLDÜ** — kullanıcı tam metni buldu, okundu, EXCLUDE (yukarıda). Belirsiz kayıt kalmadı.
- Tam metin bundan sonra yalnızca DAHİL edilen 47'nin **veri-çıkarımı / "included studies" tablosu** için gerekli (tarama kararı için değil).
- Hiçbir kayıt "bulunamadı" değil; hepsi geniş-özet/tam-metin düzeyinde görüldü.

## Kaynak izleri (seçili)
- Xu 2025: bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13530 ; eric.ed.gov EJ1473804
- Li 2023: mdpi.com/2226-471X/8/3/197 ; Bal 2024: journals.plos.org PMC11426429
- Mizumoto 2025: cambridge.org SSLA 631312E8 ; Bao 2026: tandfonline 10.1080/10494820.2026.2634138
- Karaceper 2026: files.eric.ed.gov/fulltext/EJ1495977.pdf ; Risang Baskara: eric.ed.gov EJ1457238
