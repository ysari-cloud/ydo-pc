# Screener-4 (Manus AI) — MÜHÜRLÜ Kararlar + 3-YZ Triangülasyonu

> Manus AI bağımsız kararları. `16-...PROMPT.md` istemiyle, A (kapsayıcı) kuralı, yalnız başlık+özet,
> Claude/Gemini/cowork kararlarına kör. Tarih: 2026-06-19. (Dosya başlığında "Tarayıcı-3" yazıyor ama
> bu, sıradaki 3. YZ modeli; proje numaralandırmasında Screener-4.)

## Manus ham kararları (özet)
INCLUDE = **51/56** · EXCLUDE = **5/56** → {24, 33, 36, 49, 55}
- 24 EXCLUDE: YouTube içerik üreticisi tutum/algı; üretim/öğretmen rolü yok.
- 33 EXCLUDE: GenAI tutum madenciliği (dil-özgü değil).
- 36 EXCLUDE: yalnız otomatik puanlama; materyal üretimi yok.
- 49 EXCLUDE: programlama dili (doğal dil değil).
- 55 EXCLUDE: Brezilya konuşma-ajanı sistem değerlendirmesi (dil-eğitimi odağı belirsiz).
- C1 notu: Manus 25 ve 46'yı INCLUDE etti (Gemini dışlamıştı); 4,13,19,29,35,56 da INCLUDE.

## Üç YZ tarayıcının kararları (A-varyant)
| Tarayıcı | INCLUDE | EXCLUDE |
|---|:---:|---|
| Claude (15b) | 53 | {33, 49, 55} |
| Gemini (16b) | 43 | {4,13,19,24,25,29,33,35,36,46,49,55,56} |
| Manus (16c) | 51 | {24, 33, 36, 49, 55} |

## 3-YZ Triangülasyon (konsensüs haritası)
- **3/3 INCLUDE (sağlam çekirdek): 43 kayıt.**
- **3/3 EXCLUDE (sağlam dışlama): 33, 49, 55.**
- **2/3 EXCLUDE (Gemini+Manus, Claude tek başına dahil): 24 (yalnız tutum), 36 (yalnız puanlama)**
  → kuralın AÇIK dışlama ölçütüyle örtüşür → güçlü EXCLUDE adayı.
- **1/3 EXCLUDE (yalnız Gemini): 4, 13, 19, 25, 29, 35, 46, 56** → çoğunlukla INCLUDE; sınır vakalar,
  tam-metin/insan hakemliğine kalır.

## Uyum istatistikleri
- **Oybirliği (3/3): 46/56 = %82.1**
- **Fleiss κ (3 YZ) ≈ 0.46** (moderate). Düşük görünüm κ-paradoksu: INCLUDE yaygınlığı %87.5.
- İkili anlaşma / Cohen κ:
  - **Claude ↔ Manus: %96.4 · κ ≈ 0.73** (substantial) — en yakın çift.
  - **Gemini ↔ Manus: %85.7 · κ ≈ 0.49** (moderate).
  - **Claude ↔ Gemini: %82.1 · κ ≈ 0.31** (fair).
- **Örüntü:** Gemini = katı uç (43); Claude = en kapsayıcı (53); **Manus = orta (51) = tam olarak
  YZ çoğunluk-oyu** (24,33,36,49,55 dışla).

## N senaryoları (insan formu öncesi)
- YZ çoğunluk-oyu (= Manus): **N = 51**
- Claude-kapsayıcı: **N = 53**
- Gemini-katı: **N = 43**

> Karar otoritesi hâlâ İnsan tarayıcı (Screener-1). YZ paneli = triangülasyon + sınır vakaların
> önceliklendirmesi. Nihai N ve raporlanacak κ tasarımı, insan formu gelince netleşecek.
