# §10.1 — WoS + Scopus Arama & Export Rehberi (sabah yapılacak)

> Amaç: brif §4 dizgelerini iki veri tabanında çalıştırıp, bibliyometrik analiz araçlarının
> (Bibliometrix / VOSviewer) okuyabileceği **tam kayıt + atıf bilgili** dosyaları indirmek.
> Bu adım kurumsal erişim gerektirir (İÜ-Cerrahpaşa). Aşağıyı sırayla izle; her adımda
> **sonuç sayısını not al** (kalibrasyon için kritik — brif §4).

---

## ⚙️ Önce ortak filtreler (her iki veri tabanında da, export ÖNCESİ uygula)
Brif §5'e göre, dosyayı küçültmek ve gürültüyü azaltmak için aramadan SONRA şu sınırları koy:
- **Yıl:** 2018 – bugün
- **Dil:** İngilizce (English)
- **Belge türü (geniş katman):** Article + Review + Conference Paper/Proceedings

---

## 1) Web of Science (Core Collection)

1. `webofscience.com` → kurumsal giriş (üniversite ağı / Shibboleth).
2. Üstte veri tabanı seçici: **"Web of Science Core Collection"** seçili olsun.
3. **Advanced Search** sekmesine geç.
4. Şu dizgeyi **olduğu gibi** yapıştır (geniş katman — AS1–AS3):

```
TS=(
("generative artificial intelligence" OR "generative AI" OR GenAI OR "large language model*" OR LLM OR ChatGPT OR "GPT*" OR "conversational agent*" OR chatbot* OR "AI assistant*")
AND
("foreign language" OR "second language" OR "language learning" OR "language teaching" OR "language education" OR "language teacher*" OR CALL OR "computer-assisted language learning" OR EFL OR ESL OR L2 OR "applied linguistics" OR "language classroom")
)
```

5. **Search** → çıkan sonuç sayısını NOT AL (ör. "1.180 results"). ➜ _Bu sayıyı bana söyle._
6. Sol panelden filtreleri uygula: **Publication Years 2018–2026**, **Languages: English**,
   **Document Types: Article + Review Article + Proceeding Paper**.
7. **Export** butonu (sonuç listesinin üstünde):
   - Format: **"Plain text file"** _veya_ **"BibTeX"** (Bibliometrix ikisini de okur; plaintext en sağlamı).
   - **Record Content: "Full Record and Cited References"** ← ATIF analizi için ŞART, bunu seç.
   - Aralık: WoS bir seferde max ~1000 kayıt verir. Çok sonuç varsa parça parça indir
     (1–1000, 1001–2000, …) ve dosyaları sakla (`wos_1.txt`, `wos_2.txt`, …).

---

## 2) Scopus

1. `scopus.com` → kurumsal giriş.
2. **Documents** araması → **Advanced document search**.
3. Şu dizgeyi yapıştır (geniş katman):

```
TITLE-ABS-KEY(
("generative artificial intelligence" OR "generative AI" OR GenAI OR "large language model*" OR LLM OR ChatGPT OR "GPT*" OR "conversational agent*" OR chatbot* OR "AI assistant*")
AND
("foreign language" OR "second language" OR "language learning" OR "language teaching" OR "language education" OR "language teacher*" OR CALL OR "computer-assisted language learning" OR EFL OR ESL OR L2 OR "applied linguistics" OR "language classroom")
)
```

4. **Search** → sonuç sayısını NOT AL. ➜ _Bunu da bana söyle._
5. Filtreler: **Year ≥ 2018**, **Language: English**, **Document type: Article, Review, Conference paper**.
6. Sonuçları seç (**Select all**) → **Export**:
   - Format: **CSV** (Bibliometrix için) _veya_ **BibTeX** / **RIS**.
   - İşaretle: **Citation information + Bibliographical information + Abstract & keywords + References.**
     (References = eş-atıf analizi için ŞART.)
   - Scopus abstract+references içeren export'u parça parça ister (genelde 2.000'lik dilimler).
     Çok sonuç varsa dilimleyerek indir (`scopus_1.csv`, …).

---

## 3) (Opsiyonel) Odaklı alt-küme — sentez katmanı (AS4–AS5)
Geniş katman **≥300** kayıt verdiyse, ayrıca odaklı aramayı da çalıştır: yukarıdaki dizgeye
`AND (C bloğu)` ekle. C bloğu:

```
AND
("instructional design" OR "material* design" OR "materials development" OR "content creation" OR "content generation" OR courseware OR "learning material*" OR "teaching material*" OR "educational technolog*" OR "learning object*" OR "application development" OR "app development" OR "no-code" OR "low-code" OR "tool development")
```
Bu daha küçük bir liste verir (hedef 20–60 çalışma) → onu da ayrı export et (`wos_focus.txt`, `scopus_focus.csv`).

> **Kalibrasyon (brif §4):** Geniş katman <300 ise C'yi aramadan çıkar, yalnızca kodlama
> aşamasında uygula. `GPT*` aşırı gürültüyse `"GPT-4*" OR "GPT-3*"` ile daralt.

---

## 4) Bana ne getireceksin
1. İki sonuç sayısı (WoS geniş + Scopus geniş) — ilk mesajda yeter, ona göre kalibre ederiz.
2. İndirilen dosyalar: `wos_*.txt`/`.bib` + `scopus_*.csv`/`.bib` (varsa odaklı sürümler de).
   Bu oturuma yükle → ben dedup + PRISMA eleme + bibliyometriye geçerim (§10.3).

> İpucu: format konusunda emin değilsen, **WoS→"Plain text, Full Record and Cited References"**
> ve **Scopus→"CSV, tüm kutular işaretli"** en güvenli ikilidir.
