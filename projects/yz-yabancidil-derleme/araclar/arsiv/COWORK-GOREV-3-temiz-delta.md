# COWORK GÖREVİ 3 — TEMİZ keyword duyarlılık delta'sı (as-run B ile)

> Görev-2'yi (`COWORK-GOREV-2-duyarlilik-testi.md`) **tek bir düzeltmeyle tekrarla.** Önceki delta
> B bloğunda **çıplak L2/CALL** kullanmıştı (as-run korpusta YOK) → "LLAMA dil-yatkınlık testi /
> L2 vocabulary" gürültüsü şişti. Bu sefer **as-run B bloğu** kullan → gürültü düşer, sonuç gerçek
> protokolle karşılaştırılabilir olur.

## Değişen TEK şey: B bloğu = AS-RUN (L2/CALL YOK)
Kaynak: `araclar/ARAMA-DIZGELERI-FINAL-as-run.md` → "B bloğu". Yani:
```
"foreign language" OR "second language" OR "language learning" OR "language teaching"
OR "language education" OR "language teacher*"
OR "computer-assisted language learning" OR "computer assisted language learning"
OR EFL OR ESL OR "applied linguistics" OR "language classroom"
```
**Çıplak `L2` ve çıplak `CALL` KULLANMA.** (Önceki gürültünün ana kaynağı buydu.)

## Sorgu: doğrudan delta (yeni-araç terimleri ∖ as-run A)
```
( YENİ_ARAÇ_TERİMLERİ )  AND  ( AS-RUN B )  NOT  ( AS-RUN A )
```
- **AS-RUN A** = `ARAMA-DIZGELERI-FINAL-as-run.md` → A bloğu (GPT sürüm-spesifik; Scopus jokersiz).
- **YENİ_ARAÇ_TERİMLERİ** (kesinlik-odaklı — domain'le çakışan belirsizleri ELE):
  - **Tut (düşük belirsizlik):** Gemini, Copilot, "ERNIE Bot", ERNIE, Qwen, Wenxin, Doubao,
    "DALL-E", DALLE, Midjourney, "stable diffusion", "text-to-image", "image generation",
    "AI-generated", "AI-generated content", "generative model*", Perplexity, Sora
  - **ELE / çok dikkatli (domain gürültüsü):** **Llama/LLAMA** (= dil-yatkınlık testi Lognostics →
    as-run B ile bile "second language"a takılır), **Bard** (Shakespeare), **Grok** (deyim),
    **Claude** (özel ad) → ya hiç koyma ya da sürüm-spesifik tırnakla ("Llama 3" vb.) ve sonucu gözle.
- Scopus'ta GPT jokersiz kuralını burada da uygula (A bloğu NOT tarafında).

## Adımlar
1. WoS + Scopus'ta yukarıdaki temiz delta'yı koş, dedup.
2. Sonucu mevcut 3.050 ile de farkla (zaten NOT as-run-A var ama emniyet için kontrol).
3. **Elle tara:** her kayıt ilgili mi (Y/H) + hangi terim yakaladı + görsel/çok-kipli mi + retracted mı.
4. Önceki 12 kesin + ~7 sınırda makaleyi bu temiz sonuç içinde **yeniden doğrula** (hangileri kaldı?).

## Çıktı (push)
- `analysis/sensitivity_delta_CLEAN.csv` — sütunlar: `doi,title,year,journal,new_term_hit,relevant,modal,retracted`
- 1 paragraf: temiz delta kaç kayıt, kaçı kesin ilgili (vs önceki 12), gürültü ne kadar düştü.

## Sonra (ben — cloud)
Temiz listeyi denetlerim → kesin ilgili olanlar **PRISMA "diğer yöntemlerle bulunan kayıtlar"** yolundan
tam-metin uygunluğa → **~50 sentez seti.** (Karar Q1=(a) other-methods; bibliyometrik 3.050 DONUK kalır.)

## Not
- A bloğu/B bloğu/filtreler dışında HİÇBİR şeyi değiştirme.
- Bu, korpusu yeniden kurmak DEĞİL — yalnız "kaçan ilgili var mı" teyidi. Bitince arama faslı KAPANIR.
