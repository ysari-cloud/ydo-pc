# Duyarlılık Testi — Çalıştırılacak Artırılmış Dizgeler (kopyala-yapıştır)

> A bloğu genişletildi (adlandırılmış araçlar + görsel/çok-kipli üretim). **Dil bloğu, pencere,
> DB (Scopus+WoS) AYNEN brif §4.** Çalıştırma tarihini not edin (orijinal: 2026-06-19).
> Export: tam kayıt + atıf bilgisi. WoS → "Other File Formats / Plain Text (Full Record + Cited Refs)".
> Scopus → CSV (Export, tüm alanlar). Dosyaları `analysis/raw_data/` içine koyun:
>   wos_aug_1.txt … wos_aug_N.txt   ·   scopus_aug.csv

## WoS Core Collection — Artırılmış GENİŞ katman
```
TS=(
("generative artificial intelligence" OR "generative AI" OR "Gen AI" OR GenAI OR GAI
 OR "large language model*" OR LLM* OR ChatGPT OR "GPT-*" OR "GPT*"
 OR "conversational agent*" OR chatbot* OR "AI assistant*"
 OR Gemini OR Bard OR Claude OR Copilot OR "ERNIE Bot" OR ERNIE OR Qwen OR Wenxin OR Doubao
 OR Llama OR Perplexity OR Grok OR Sora
 OR "DALL-E" OR DALLE OR Midjourney OR "stable diffusion" OR "text-to-image" OR "image generation"
 OR "AI-generated" OR "AI-generated content" OR "generative model*")
AND
("foreign language" OR "second language" OR "language learning" OR "language teaching"
 OR "language education" OR "language teacher*" OR CALL OR "computer-assisted language learning"
 OR EFL OR ESL OR L2 OR "applied linguistics" OR "language classroom")
)
```

## Scopus — Artırılmış GENİŞ katman
```
TITLE-ABS-KEY(
("generative artificial intelligence" OR "generative AI" OR "Gen AI" OR GenAI OR GAI
 OR "large language model*" OR LLM* OR ChatGPT OR "GPT-*" OR "GPT*"
 OR "conversational agent*" OR chatbot* OR "AI assistant*"
 OR Gemini OR Bard OR Claude OR Copilot OR "ERNIE Bot" OR ERNIE OR Qwen OR Wenxin OR Doubao
 OR Llama OR Perplexity OR Grok OR Sora
 OR "DALL-E" OR DALLE OR Midjourney OR "stable diffusion" OR "text-to-image" OR "image generation"
 OR "AI-generated" OR "AI-generated content" OR "generative model*")
AND
("foreign language" OR "second language" OR "language learning" OR "language teaching"
 OR "language education" OR "language teacher*" OR CALL OR "computer-assisted language learning"
 OR EFL OR ESL OR L2 OR "applied linguistics" OR "language classroom")
)
```

## (Opsiyonel) Odaklı kontrol: yukarıdakine `AND (C bloğu)` ekleyin (brif §4 C bloğu).

## Notlar
- Adlandırılmış araçlar tek başına gürültülü; AND dil-bloğu gürültüyü çökertir. Yine de DELTA'yı gözle tarayın.
- "AI tool*"/"AI application*" KASITLI eklenmedi (GenAI-öncesi CALL araçlarını çeker) → ayrı kontrol koşusu.
