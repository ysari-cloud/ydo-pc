# Cloud Denetim — Makale Taslağı v1 (`Makale_Taslak_v1.docx`, commit 49e40a2)

> Rol: cloud = denetim (yazmaz). WRITE çıktısı denetlendi. 69 paragraf.

## ✅ GEÇER
- **Atıf bütünlüğü:** spot-check edilen korpus derlemeleri GERÇEK ve konu-uyumlu:
  Law 2024 (Comput. Educ. Open 6, 100174) ✓; Zhai & Wibowo 2023 (Comput. Educ. AI 4, 100134) ✓.
  4 metodolojik atıf (PRISMA/VOSviewer/bibliometrix/Donthu) standart + DOI doğru. Boşluk argümanını
  destekliyor (mevcut derlemeler konuşma/öğrenen-merkezli — üretim boyutu eksik).
- **Bütünlük disiplini:** κ, nihai N, doğrulanamayan klasik kavramsal atıflar **yer tutucu** olarak
  bırakılmış (uydurulmamış); bütünlük/YZ beyanı var; arama tarihi 2026-06-19; PRISMA sayıları gerçek.
- Yapı tam: Abstract+Keywords, Giriş (4-move), Yöntem, Bulgular-Bibliyometri, ön-Sentez (açıkça
  "ön/özet temelli" etiketli), Tartışma iskeleti, Kaynakça (12).

## 🔴 KRİTİK — taslak v2'ye geçmeden ÖNCE (engelleyici)
**AS3 sayıları KİRLİ — düzeltme (09) UYGULANMAMIŞ.** Taslak şu kirli değerleri kullanıyor:
- Para 46 (§3.3): konuşma %70,8→39,4→22,2; üretim %5,6→20,3→**38,0**; "production frame surpassing…".
- Para 5–6 (Abstract/Keywords) ve Para 52 (§4 "central thesis supported") bu sayıya dayanıyor.

Bu değerler `run_full.py` CONV_LEX/PROD_LEX kirliliğinden (`'generative'` PROD'da → "generative AI"
588 kayıt otomatik üretim sayılıyor; `oral` substring; jenerik terimler). **Manşet bulgu yapay
şişmiş; bu hâliyle yayına/revize'ye GİDEMEZ.** (Ayrıntı: `09-cloud-denetim-ve-yonerge.md`.)

> ⚠️ Re-run cowork'te yapılmalı: ham WoS/Scopus dosyaları yalnız cowork'te (repoda yok, sadece
> sha256). Cloud bu yüzden AS3'ü kendisi yeniden çalıştıramaz.

### Cowork yapacak
1. CONV_LEX/PROD_LEX temizle (09'daki liste) + kelime-sınırı eşleşme → **AS3 re-run** (Table 3 + Fig 5).
2. **Güncelle:** Abstract (para 5), §3.3 (para 46), §4 (para 52) yeni temiz sayılarla. Kayma yönü
   korunursa (SliceKeywords bağımsız destekliyor) tez ayakta; değerler değişir.
3. Sözlükleri Appendix'e + 1 paragraf duyarlılık (sensitivity) sonucu.

## 🟡 KÜÇÜK düzeltmeler
- **APA:** "Davar, N. F., et al. (2025)" — kaynakça girişinde "et al." OLMAZ; tüm yazarları yaz (≤20).
- PRISMA 2020 **27-madde kontrol listesi** henüz yok → cowork eklesin (submission şartı).
- Kalan korpus atıflarının (Huang, Jeon×2, Ji, Kohnke, Davar) DOI'leri de teyit edilsin (korpustan
  geldikleri için risk düşük; cloud sırada doğrular).

## ⏭️ Sıra
- **Cowork:** AS3 re-run + taslak sayı güncelleme + APA/PRISMA-checklist.
- **Kullanıcı:** 56-set tam-metin + 2. tarayıcı → κ, nihai N → sentez bulguları (taslak v2'nin RQ4–RQ5).
- **Cloud:** kalan DOI'leri doğrula; v2 gelince tam bütünlük + PRISMA 27-madde denetimi.
