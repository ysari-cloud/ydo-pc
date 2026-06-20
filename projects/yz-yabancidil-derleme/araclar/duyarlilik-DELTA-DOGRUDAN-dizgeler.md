# Duyarlılık Testi — DOĞRUDAN DELTA dizgeleri (küçük export)

> Mantık: DELTA = "yalnız YENİ terimler" AND "dil bloğu" **NOT** "eski A bloğu".
> Bu, eski aramanın hiç yakalayamayacağı (yalnız adlandırılmış araç / görsel-üretim terimi
> içeren) kayıtları DOĞRUDAN verir. Eski terimlerden birini de içeren kayıtlar zaten
> orijinal korpustaydı → otomatik dışlanır. Böylece export küçük ve temiz olur.
> **Tarih / dil / DB / belge-türü filtreleri orijinaldekiyle AYNI tutulur; sadece A bloğu değişir.**
> Çalıştırma tarihini not edin. Export: WoS → Plain Text (Full Record); Scopus → CSV (tüm alanlar).
> Dosya adları: `wos_aug_1..N.txt`, `scopus_aug.csv` → `raw_data/` (veya Downloads, ikisini de okuyorum).

## WoS Core Collection
```
TS=(
("Gen AI" OR GAI OR "LLM*" OR Gemini OR Bard OR Claude OR Copilot OR "ERNIE Bot" OR ERNIE
 OR Qwen OR Wenxin OR Doubao OR Llama OR Perplexity OR Grok OR Sora
 OR "DALL-E" OR DALLE OR Midjourney OR "stable diffusion" OR "text-to-image" OR "image generation"
 OR "AI-generated" OR "AI-generated content" OR "generative model*")
AND
("foreign language" OR "second language" OR "language learning" OR "language teaching"
 OR "language education" OR "language teacher*" OR CALL OR "computer-assisted language learning"
 OR EFL OR ESL OR L2 OR "applied linguistics" OR "language classroom")
NOT
("generative artificial intelligence" OR "generative AI" OR GenAI OR "large language model*"
 OR LLM OR ChatGPT OR "GPT*" OR "conversational agent*" OR chatbot* OR "AI assistant*")
)
```

## Scopus
```
TITLE-ABS-KEY(
("Gen AI" OR GAI OR "LLM*" OR Gemini OR Bard OR Claude OR Copilot OR "ERNIE Bot" OR ERNIE
 OR Qwen OR Wenxin OR Doubao OR Llama OR Perplexity OR Grok OR Sora
 OR "DALL-E" OR DALLE OR Midjourney OR "stable diffusion" OR "text-to-image" OR "image generation"
 OR "AI-generated" OR "AI-generated content" OR "generative model*")
AND
("foreign language" OR "second language" OR "language learning" OR "language teaching"
 OR "language education" OR "language teacher*" OR CALL OR "computer-assisted language learning"
 OR EFL OR ESL OR L2 OR "applied linguistics" OR "language classroom") )
AND NOT TITLE-ABS-KEY("generative artificial intelligence" OR "generative AI" OR GenAI
 OR "large language model*" OR LLM OR ChatGPT OR "GPT*" OR "conversational agent*"
 OR chatbot* OR "AI assistant*")
```

## Sonraki adım
Export'ları koyduğunuzda: `python3 analysis/scripts/sensitivity_delta.py` →
`analysis/sensitivity_delta.csv` (doi, başlık, yıl, dergi, new_term_hit, relevant, modal, recency).
Ben ilgililik (relevant) ve görsel-üretim (modal) kolonlarını gözle denetleyip karar kuralını uygularım.
