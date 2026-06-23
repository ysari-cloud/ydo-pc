# 24 — Komşu SSCI Derlemelerin YÖNTEM ANALİZİ + Yazım Şablonu + Ayrışma Haritası

> Tarih: 2026-06-21 · Cloud · Kaynak: 5 exemplar tam metin (3 SR + 2 bibliyometrik), fitz ile çıkarıldı.
> Amaç: makalemizin yapı/yöntem/raporlamasını yerleşik örneklere göre kurmak + ayrışmayı netleştirmek.

## 1) Exemplar yöntem profilleri
| Çalışma | Tür | DB | Tarama/Eleme | Kalite değerlendirme | Sentez/Analiz | Araçlar | N |
|---|---|---|---|---|---|---|---|
| **Two Years (Li 2025, C&E:AI)** | SR (empirik GenAI, dil L&T) | WoS+Scopus+**ERIC** | PRISMA; **Rayyan**; 2 tur arama; **inter-rater %82,14 (Landis-Koch)** | yok (peer-review+empirik) | **tematik; kodlama çerçevesi yinelemeli/EMERGENT + codebook** | — | 1214→144 |
| **Deng 2026 (SAGE Open)** | SR (EFL rolleri) | WoS+Scopus | PRISMA 4-adım; empirik-only | yok (örneklem-boyutu sınıflaması) | tematik; bağlam/yöntem/konu ekseni | — | 284→51 |
| **Griche 2026 (TLTL)** | SR (FL+YÖ) | WoS+Scopus+**Springer** | **PICo**; Rayyan; QDA Miner | ✅ **EPHPP (nicel)+CASP (nitel)** | **in vivo + axial coding; 14 tema** | Zotero | 329→152 |
| **Biblio AI-Review (Rahman 2023)** | bibliyometri **+ içerik analizi** | Scopus | PRISMA; 606 doc | yok | **performans + 7 küme + DEDÜKTİF içerik kodlama (NVivo)** | **VOSviewer + R/Biblioshiny** | 606 |
| **Biblio EFL (Educ&InfoTech 2025)** | bibliyometri | **WoS-only** (sınırlılık) | — | yok | performans + eş-oluşum 5 küme | **Bibliometrix R + VOSviewer** | 3.300 |

## 2) Gözlenen NORMLAR (hakem beklentisi → biz neye uymalıyız)
- **Veri tabanı:** WoS+Scopus standart (±ERIC/Springer). **Bizde WoS+Scopus ✓.**
- **Eleme aracı:** Rayyan yaygın (Two Years, Griche). *(Biz manuel; Rayyan/araç adını raporlamak iyi olur.)*
- **Kodlayıcı güvenilirliği:** Two Years **%82,14 agreement (Landis-Koch)**; Griche zayıf ("shop talk", standart test yok). → **Bizim κ planımız Griche'den GÜÇLÜ; Two Years seviyesinde rapor et.**
- **Kalite değerlendirme:** yalnız **Griche** formal araç (EPHPP+CASP); diğer 4'ü kullanmamış. → **EPHPP/CASP eklemek bizi çoğundan ÜSTÜN yapar** (opsiyonel ama güçlü).
- **Bibliyometri araçları:** her iki bibliyometrik de **VOSviewer + Bibliometrix/R**. → Biz VOSviewer + **Python (pandas)** kullandık; hakem Bibliometrix/Biblioshiny bekleyebilir → ya Biblioshiny ekle ya Python'u açıkça gerekçelendir.
- **Sentez:** tematik norm; Two Years "kodlama çerçevesi yinelemeli emergent" = bizim **tümevarım kapısına** çok yakın → **HİBRİT (dedüktif C1–C8 + tümevarım) savunulabilir ve Two Years ile hizalı.**

## 3) YAZIM ŞABLONU (bizim hibrit bibliyometri + SR makalesi)
1. **Giriş** + Two Years'taki **"What this paper adds"** kutusu (katkıyı net çerçevele).
2. **Yöntem:** PRISMA 2020 + **iki katman** (geniş bibliyometri 3.050 / odaklı sentez 25) · as-run kalibre arama dizgesi (Appendix) · eleme + **κ** · (opsiyonel **EPHPP/CASP**) · bibliyometri araçları (VOSviewer + Bibliometrix/Python) · **hibrit kodlama** (C1–C8 + tümevarım).
3. **Bulgular:** Bibliyometri (AS1 performans · AS2 bilim haritalama · AS3 tematik evrim) **+** Sentez (AS4 roller · AS5 öğretmen/öğrenci-üretici dönüşümü).
4. **Tartışma** → **Implications (teori+pratik)** → **Sınırlılıklar** (predatory/EnPress dahil) → **Sonuç** → Appendix (arama dizgesi, PRISMA, kod kitabı, dahil-liste).

## 4) AYRIŞMA HARİTASI (hakemin "farkınız ne?" sorusuna)
| Boyut | Two Years | Deng | Griche | Biblio'lar | **BİZ** |
|---|---|---|---|---|---|
| Bibliyometri + SR (aynı korpus) | – | – | – | yalnız biblio | ✅ **ikisi birlikte** |
| Odak | genel empirik | EFL rolleri | FL+YÖ fırsat/risk | AI/EFL haritası | ✅ **materyal ÜRETİMİ + öğretmen/öğrenci-üretici** |
| Çok-dillilik | EFL ağırlık | EFL | FL | EFL/AI | ✅ **Çince/Arapça/Romence/Almanca** |
| Analitik mercek | tema | rol | fırsat/risk | küme | ✅ **C1 rol tipolojisi + "konuşma→üretim"** |
| Kalite + predatory denetim | – | – | EPHPP/CASP | – | ✅ **κ + (EPHPP/CASP) + predatory tarama** (bizde özgün) |

**Net ayrışma cümlesi (taslak):** *"Mevcut derlemeler GenAI'yi ya genel empirik (Two Years), ya rol (Deng), ya fırsat/risk (Griche) ekseninde; bibliyometrikler ise AI/EFL'yi haritalıyor. Hiçbiri **materyal üretimi / öğretmen-öğrenci üretici dönüşümü**ne odaklı, **çok-dilli**, ve **bibliyometri + odaklı sentezi tek korpusta** birleştiren bir tasarım sunmuyor."*

## 5) Somut öneriler (yazım kararları)
1. **κ'yı belirgin raporla** (Two Years %82,14 emsali) — Griche'nin zayıf noktasını biz kapatırız.
2. **EPHPP/CASP eklemeyi değerlendir** — çoğu eksik; eklersek metodolojik üstünlük.
3. **Bibliometrix/Biblioshiny** ekle ya da Python'u gerekçelendir (araç beklentisi).
4. **Rayyan/araç adını** yöntemde an.
5. **Predatory tarama (EnPress 23)** = özgün metodolojik katkı, sınırlılık+güç olarak yaz.
6. **"What this paper adds"** kutusu kullan.

> Sıradaki: kodlama (cowork Görev-6) bitince bu şablon + ayrışma ile **yöntem & giriş bölümleri** yazıma hazırlanır (yazım cowork, iskelet/denetim cloud).
