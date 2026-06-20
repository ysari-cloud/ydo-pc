# 20 — Arama Duyarlılık Denetimi (Keyword Audit): Komşu 2 derlemeye karşı

> Tarih: 2026-06-20 · Tetik: kullanıcı iki güncel komşu SLR'nin tam metnini verdi (Deng & Jamaludin
> 2026; Griche & Bennis 2026). Soru: "anahtar kelime noktasında yanlış/eksik hareket etmiş olabilir
> miyiz?" · Yöntem: iki derlemenin **fiili Boolean dizgeleri** çıkarıldı (PyMuPDF) ve bizim
> brif §4 dizgemizle karşılaştırıldı. Bu = PRESS tarzı arama-eş-değerlendirme.

## 0) Komşu derlemelerin künyesi
| | Deng & Jamaludin 2026 | Griche & Bennis 2026 |
|---|---|---|
| Başlık | Roles of GenAI in EFL Instruction: SLR | GenAI Integration in FL Education in Higher Ed |
| Yer | SAGE Open, Jan–Mar 2026 | TLTL/Castledown 2026 |
| DOI | 10.1177/21582440261418315 | 10.29140/tltl.2026.102827 |
| DB | Scopus + WoS | Scopus + WoS + **Springer Nature** |
| Çerçeve | PRISMA + Modified TBL Model | PICo + PRISMA |
| Pencere | 2020–2024 | (2021/22 sonrası vurgu) |
| N | 284 → **51** | **152** |
| Belge türü | **yalnız ampirik** (review/commentary/tez DIŞLA) | **yalnız ampirik** (+ book chapter DIŞLA) |
| Odak | EFL'de GenAI rolleri; YÖ + writing ağırlık; GenAI=değerlendirici | FL+YÖ fırsat/risk; 14 tema |

## 1) Üç arama dizgesi yan yana

**BİZİM (brif §4) — A bloğu:**
`"generative artificial intelligence" OR "generative AI" OR GenAI OR "large language model*" OR LLM OR ChatGPT OR "GPT*" OR "conversational agent*" OR chatbot* OR "AI assistant*"`

**DENG A:** `"Generative Artificial Intelligence" OR GenAI OR GAI OR LLMs OR "Large Language Models" OR ChatGPT`

**GRICHE A:** `"generative AI" OR "artificial intelligence" OR GenAI OR "large language model*" OR LLM* OR ChatGPT OR Bard OR grok OR gemini OR DALL-E OR midjourney OR "stable diffusion" OR "AI tool*" OR "AI application*" OR "AI writing tool*" OR "AI grammar checker*"`

(Griche ayrıca AND `higher education/universit*/college/tertiary` AND `opportunit*/challenge*/benefit*/risk*/impact*…` blokları ekler — onları YÖ'ye daraltır.)

## 2) İki yönlü karşılaştırma

### Bizim GÜÇLÜ olduğumuz (gap DEĞİL — koru)
- **Dil bloğumuz her ikisinden GENİŞ:** bizde `foreign/second language, language learning/teaching/education, language teacher*, CALL, EFL, ESL, L2, applied linguistics, language classroom`. Deng yalnız EFL; Griche EFL+SLA. → dil tarafında açık YOK.
- **Konuşma kutbu yalnız bizde:** `chatbot*`, `conversational agent*`, `AI assistant*` — iki derlemede de yok. "Konuşma→üretim" tezimizin temel-hattı için kritik. ✅
- **`GPT*`** (GPT-4/4o/3.5) yalnız bizde. ✅
- **Korpus büyüklüğü:** bizim geniş 3.050 ≫ Deng 284 (EFL-dar) / Griche 152 (YÖ-dar) → ağımız daha geniş.

### Onlarda olup bizde OLMAYAN (gerçek aday açıklar — risk sırasıyla)
| # | Eksik terim | Kaynak | Risk | Tez-ilgisi |
|---|---|---|---|---|
| **1** | **Adlandırılmış araçlar:** Gemini, Claude, Copilot, Bard, **ERNIE Bot**, Llama, Perplexity, Grok, Qwen/Wenxin/Doubao | Griche (kısmen) | **YÜKSEK** | 2024-26 makaleleri tek bir aracı adıyla anabilir; ERNIE Bot=Mi 2025 örneğinde geçti; Çin-ağırlıklı korpusta Çin araçları (Qwen/ERNIE) önemli |
| **2** | **Görsel/çok-kipli üretim:** DALL-E, Midjourney, "stable diffusion", "text-to-image", "image generation" | Griche | **YÜKSEK** | Materyal üretimi tezimizin tam merkezi (görsel materyal/flashcard) — şu an SIFIR kapsama |
| **3** | "AI-generated" / "AI-generated content" | — (ikisi de değil) | ORTA | Materyal-üretim makalelerinde çok yaygın ifade |
| **4** | `LLM*` (çoğul/türev) — bizde `LLM` (tam) | Deng/Griche | DÜŞÜK | "LLMs" tek başına geçen başlığı kaçırabiliriz (ama "large language model*" yedekler) |
| **5** | "GAI", "Gen AI" (boşluklu) | Deng | DÜŞÜK | nadir yazım varyantları |
| — | "artificial intelligence" (genel AI) | Griche | **EKLEME** | gürültü patlatır + GenAI-özgül kapsamı bozar — KASITLI dışarıda bırak |

> ⚠️ Çift-anlam notu: Gemini/Bard/Grok/Claude/Copilot/ERNIE gibi adlar tek başına gürültülüdür
> (astronomi, Shakespeare, GitHub Copilot, isimler) — AMA dizgemiz **AND dil-bloğu** (ve odaklıda
> AND C-bloğu) ile birleştiği için gürültü pratikte çöker. Bu yüzden çok-bloklu AND'de adlandırılmış
> araçları eklemek GÜVENLİ. "AI tool*"/"AI application*" daha risklidir (GenAI-öncesi CALL araçlarını
> çekebilir) → ayrı test et.

## 3) HÜKÜM
1. **İki derleme "kaçtı" çünkü anahtar kelime DEĞİL:** ikisi de GenAI+EFL/FL başlıklı → bizim dizgemiz
   onları **yakalardı**. Yokluk nedeni: (a) **güncellik** (2026 derlemeleri, 2026-06-19 anlık
   görüntümüzden sonra indekslenmiş olabilir) + (b) **ikincil kaynak** (derleme → birincil korpusa
   girmez) + (c) odaklı C-bloğundan geçmezlerdi. → Arama açığı kanıtı DEĞİL.
2. **AMA terim-listesi kıyası gerçek bir kuyruk-riski ortaya çıkardı:** adlandırılmış araçlar (#1) +
   görsel/çok-kipli üretim (#2). Bunlar yalnızca tek-araç-adıyla anılan, hele **materyal üretimi için
   görsel-üreten** makaleleri kaçırmamıza yol açabilir — ve hakemin tam soracağı şey budur.
3. **Ampirik-only kararınız ALAN-STANDARDI:** her iki derleme de yalnız ampirik (Deng review/commentary/
   tez dışlar; Griche non-empirical + book chapter dışlar). #27 Shin türü feature'ları dışlama kararınız
   bu iki emsalle desteklenir.
4. **Hediye atıf:** Deng, GenAI-**değerlendirme** çalışmalarını "evaluation, instructional design'ın
   çekirdek bileşenidir (Tyler, 1975)" gerekçesiyle DAHİL eder → bizim sınır vakalarımız (#36 Karaceper
   otomatik puanlama vb.) için savunulabilir dahil-etme gerekçesi.

## 4) ÖNERİLEN AKSİYON — hedefli duyarlılık testi (full re-do DEĞİL)
Aşağıdaki **artırılmış A bloğunu** AYNI dil(+C) bloğu, AYNI pencere, AYNI DB (Scopus+WoS) ile koştur;
yeni gelen kayıtları mevcut 3.050 (geniş) / 328 (odaklı) ile karşılaştır.

**Artırılmış A (test için — WoS TS / Scopus TITLE-ABS-KEY):**
```
("generative artificial intelligence" OR "generative AI" OR "Gen AI" OR GenAI OR GAI
 OR "large language model*" OR LLM* OR ChatGPT OR "GPT-*" OR "GPT*"
 OR "conversational agent*" OR chatbot* OR "AI assistant*"
 OR Gemini OR Bard OR Claude OR Copilot OR "ERNIE Bot" OR ERNIE OR Qwen OR Wenxin OR Doubao
 OR Llama OR Perplexity OR Grok OR Sora
 OR "DALL-E" OR DALLE OR Midjourney OR "stable diffusion" OR "text-to-image" OR "image generation"
 OR "AI-generated" OR "AI-generated content" OR "generative model*")
```

**Karar kuralı:**
- Yeni-eklenen kayıtlar **önemsiz/zaten-kapsanmış** → bunu **bir duyarlılık analizi** olarak yaz:
  "GenAI-çekirdek dizge yeterliydi" (zayıflığı metodolojik GÜCE çevirir, hakemi önceler).
- Yeni-eklenen kayıtlar **anlamlı sayıda ilgili** → gerçek recall açığı; terimleri kalıcılaştır,
  yeniden koş, PRISMA n'lerini güncelle. (Görsel-üretim kümesi en kritik kontrol.)

**Ek (opsiyonel):** 3. veri tabanı olarak Springer Nature (Griche kullandı) — Scopus büyük ölçüde
kapsar, marjinal; istenirse kontrol.

## 5) Komşu-derleme konumlandırması (özgünlük)
İkisi de **nitel-tematik**. Bizim ayrışmamız: **bibliyometrik + (olası) meta-analitik eksen +
çok-dillilik (Almanca/Arapça/Japonca) + materyal-üretimi/öğretmen-rolü odağı.** Hakemin "farkınız ne?"
sorusuna net cevap. Sıradaki somut iş: iki derlemenin **referans listeleri ↔ bizim 47 korpus** örtüşme/
boşluk analizi (ortak / onlarda-var-bizde-yok=snowball adayı / bizde-var-onlarda-yok=özgünlük kanıtı) —
PDF'ler + DOI listesi yerelde olduğundan cloud'da yapılabilir (egress gerektirmez).
