# ARAMA DİZGELERİ — FİNAL / AS-RUN (kanonik, makale-hazır)

> ⭐ **TEK DOĞRULUK KAYNAĞI.** Korpusu (3.050 geniş / 328 odaklı) fiilen üreten dizgeler bunlardır.
> Kaynak: cowork yerel `PROJECT_STATE.md` + "WoS/Scopus search export" oturum transkripti (çapraz teyitli, 2026-06-20).
> Metot bölümünde ve Appendix'te **bunlar** raporlanır — brif §4'teki *niyet edilen* dizge DEĞİL.
> Brif §4 = tasarım niyeti; aşağısı = uygulanan. Fark = bilinçli kalibrasyon (aşağıda gerekçeli).

## Ortak filtreler (her iki veri tabanı)
- **Yıl:** 2018–2026
- **Dil:** İngilizce
- **Belge türü:** Article + Review + Conference/Proceedings paper
- **Arama günü:** 2026-06-19 (PRISMA'da raporlanacak)

## A bloğu — üretken YZ
```
"generative artificial intelligence" OR "generative AI" OR GenAI OR "large language model*"
OR LLM OR ChatGPT OR "GPT-3*" OR "GPT-4*" OR "GPT-5*"
OR "conversational agent*" OR chatbot* OR "AI assistant*"
```
> ⚠️ Scopus istisnası: tırnaklı+joker `"GPT-3*"` Scopus'ta tüm sorguyu SIFIRLIYOR → Scopus'ta GPT
> **jokersiz**: `"GPT-3" OR "GPT-4" OR "GPT-5"`. WoS'ta joker korunur.

## B bloğu — yabancı dil eğitimi
```
"foreign language" OR "second language" OR "language learning" OR "language teaching"
OR "language education" OR "language teacher*"
OR "computer-assisted language learning" OR "computer assisted language learning"
OR EFL OR ESL OR "applied linguistics" OR "language classroom"
```
> ⚠️ Çıplak `CALL` ve çıplak `L2` BİLEREK YOK (kalibrasyon — aşağıya bak). Brif §4'te vardı; korpusta yok.

## C bloğu — materyal/üretim (yalnız odaklı/sentez katmanı)
```
"instructional design" OR "material* design" OR "materials development" OR "content creation"
OR "content generation" OR courseware OR "learning material*" OR "teaching material*"
OR "educational technolog*" OR "learning object*" OR "application development"
OR "app development" OR "no-code" OR "low-code" OR "tool development"
```

## Sorgu kurulumu ve sonuç (PRISMA identification)
| | Geniş = (A AND B) | Odaklı = (A AND B AND C) |
|---|---|---|
| WoS `TS=` | **1.932** | 173 |
| Scopus `TITLE-ABS-KEY` | **2.824** | 303 |
| **Dedup sonrası** | **3.050** | **328** |

## Kalibrasyon notları (Metot'ta gerekçeli raporlanacak — bu bir GÜÇTÜR)
1. **Gürültü azaltma (WoS ~7.609 → 1.932):** çıplak `CALL` (=telefon "call"), çıplak `L2` (alan-dışı),
   ve çıplak `GPT*` (enzim "GPT" vb.) yüksek gürültü üretti → CALL/L2 çıkarıldı, GPT **sürüm-spesifik**
   yapıldı. Bu, standart **arama kesinlik kalibrasyonu** (PRESS uyumlu); precision için meşru.
2. **Scopus joker hatası:** `"GPT-3*"` Scopus'ta sıfır sonuç → Scopus'ta GPT jokersiz kullanıldı.

## Dünkü "tutarsızlık" — ÇÖZÜLDÜ
Rekonstrüksiyonun 7.217/6.914 vermesinin nedeni: brif §4'teki *niyet edilen* dizge (çıplak GPT*/CALL/L2)
ile koşulmasıydı. Korpus ise **yukarıdaki kalibre dizgeyle** kuruldu (PROJECT_STATE.md'de yazılı).
→ Tutarsızlık projede değil, eksik okumadaydı. **Korpus tekrarlanabilir; sadece doğru dizge raporlanmalı.**

## Bunun bugünkü duyarlılık testine etkisi
Cowork'ün delta sorgusu B bloğunda **çıplak L2/CALL** kullandı (as-run B'de yok) → "LLAMA dil-yatkınlık
testi / L2 vocabulary" gürültüsü kısmen bundan şişti. **Temiz tekrar:** artırılmış-A `AND` **as-run B**
(L2/CALL'sız) `NOT` as-run-A. Karar (12 makale → "other methods") bu temiz delta üzerinden verilecek.
