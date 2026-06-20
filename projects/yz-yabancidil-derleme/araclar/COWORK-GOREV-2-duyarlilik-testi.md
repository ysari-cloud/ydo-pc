# COWORK GÖREVİ 2 — Anahtar Kelime Duyarlılık Testi (PRESS)

> Amaç: `20-arama-denetimi-keyword-audit.md`'de saptanan açığı ölçmek — **adlandırılmış GenAI araçları
> + görsel/çok-kipli üretim** terimleri eklenince korpusa KAÇ yeni ilgili kayıt giriyor?
> Bu bir **recall duyarlılık analizi**; sonuç ne olursa olsun makaleye metodolojik güç katar.
> Bu işi SADECE cowork yapabilir (WoS/Scopus kurumsal erişim). Cloud egress kapalı.

## Değiştirme YOK — sadece A bloğunu genişlet
**Dil bloğu** (brif §4) AYNEN kalır. **Pencere/dil/DB** AYNEN kalır (Scopus + WoS). Yalnız A bloğu:

### Artırılmış A bloğu (WoS `TS=` / Scopus `TITLE-ABS-KEY`)
```
("generative artificial intelligence" OR "generative AI" OR "Gen AI" OR GenAI OR GAI
 OR "large language model*" OR LLM* OR ChatGPT OR "GPT-*" OR "GPT*"
 OR "conversational agent*" OR chatbot* OR "AI assistant*"
 OR Gemini OR Bard OR Claude OR Copilot OR "ERNIE Bot" OR ERNIE OR Qwen OR Wenxin OR Doubao
 OR Llama OR Perplexity OR Grok OR Sora
 OR "DALL-E" OR DALLE OR Midjourney OR "stable diffusion" OR "text-to-image" OR "image generation"
 OR "AI-generated" OR "AI-generated content" OR "generative model*")
AND
( <BRİF §4 DİL BLOĞU — AYNEN> )
```

## Adımlar
1. **Geniş katman:** Artırılmış-A `AND` dil bloğu → Scopus'ta ve WoS'ta ayrı ayrı koş. Çalıştırma
   **tarihini kaydet** (orijinal 2026-06-19 idi; fark olacak).
2. Her DB'den **DOI + başlık + yıl + dergi** export et; DB'ler arası dedup.
3. **DELTA = (artırılmış sonuç) ∖ (mevcut geniş 3.050 korpus)** — DOI ile küme-farkı al (DOI yoksa
   normalize-başlık eşleşmesi). Yani "yeni A terimleri sayesinde GELEN, daha önce OLMAYAN" kayıtlar.
4. DELTA'yı sınıfla: her kayıt için **(a)** gerçekten yabancı-dil + GenAI mı (ilgili Y/H), **(b)** hangi
   yeni terim yakaladı, **(c)** **görsel/çok-kipli üretim** alt-kümesini ayrıca işaretle (en kritik).
5. **Recency'i ayır:** DELTA'da yayın/erişim tarihi > 2026-06-19 olanları işaretle → bunlar "kelime
   açığı" değil "güncellik" kaynaklı; ikisini karıştırma.
6. (Opsiyonel) Artırılmış-A `AND` dil `AND` C-bloğu (odaklı) → mevcut 328 ile farkı al (materyal-üretim
   açığı buradan görünür).

## Çıktı (repoya push)
- `analysis/sensitivity_delta.csv` — sütunlar: `doi, title, year, journal, new_term_hit, relevant(Y/N), modal(image?), recency(>0619?)`
- 1 paragraf özet not: kaç yeni kayıt, kaçı ilgili, görsel-üretim alt-kümesi var mı.
→ Sonra ben relevansı denetleyip **karar kuralını** uygularım (delta önemsiz → duyarlılık-analizi notu;
  delta anlamlı → terimleri kalıcılaştır + yeniden koş + PRISMA n güncelle).

## Dikkat
- Adlandırılmış araçlar tek başına gürültülü (Gemini=astronomi, Bard=Shakespeare, Copilot=GitHub,
  ERNIE=BERT-türevi/isim) → AMA `AND dil bloğu` gürültüyü pratikte çökertir. Yine de DELTA'yı gözle tara.
- `"AI tool*"/"AI application*"` (Griche'de var) BİLEREK eklenmedi (GenAI-öncesi CALL araçlarını çeker) —
  istersen AYRI bir kontrol koşusunda dene, ana teste karıştırma.
- A bloğu dışında HİÇBİR şeyi değiştirme; aksi halde delta yorumlanamaz.
