# Cowork Yönergesi (2026-06-19) — bibliyometri tamamlama + sentez rafine + yazım

> ROL: **Cowork = tüm yürütme + tüm yazım.** **Cloud = takip/yönlendirme/denetim** (metin yazmaz).
> Cloud, sentez ön-taramasını inceledi; sonuç sağlam. Aşağıdaki adımları sırayla uygula.

## ① BİBLİYOMETRİ — GENİŞ set (3.050) üzerinde tamamla
- **RQ1 Performans:** yıllık üretim, atıf, üretken yazar/kurum/ülke/kaynak.
- **RQ2 Bilim haritalama:** eş-atıf + bibliyografik eşleşme **WoS `CR` alanından** (Scopus refs
  ayrı). Anahtar-sözcük eş-oluşumu öncesi **thesaurus normalizasyonu** (ChatGPT/GPT/GPT-4→tek;
  AI/artificial intelligence→tek; EFL/ESL; tekil-çoğul).
- **RQ3 Tematik evrim:** dilimler **2018-21 / 2022-23 / 2024-**.
- Haritalar için **ham WoS/Scopus dosyalarını doğrudan VOSviewer'a** ver; Python = performans +
  tematik evrim. Ülke/kurum (C1/C3) parse'ından sonra ilk 10 ülkeyi gözle doğrula.

## ② SENTEZ — 2 rafine
- **223→40 çerçevelemesi:** top-40 *nihai dahil-küme değil*; **"tam-metin için öncelikli kısa
  liste"** olarak raporla. 223'ün tamamı eligible-aday kalsın; nihai n tam-metin + κ ile belirlenir.
- **Erken-üretim makalelerini koru:** 2022-23'te 13 ön-uygun var, kısa listede 2. İnsan taramasına
  **40 + kalan ~11 erken-üretim** birlikte girsin (kayma köprüsü).

## ③ YENİ ÇIKTI — geniş korpus yıl dağılımı (AS3 için kritik)
- **3.050'in yıl dağılımını** çıkar (2018-21 / 2022-23 / 2024-) ve bildir.
- %90+ 2024+ ise AS3 = "doğuş anındaki hızlı çerçeve kayması"; taban makulse klasik tematik-evrim.

## ④ BÜTÜNLÜK (değişmez)
- κ / tam-metin okuması **uydurma yok**. Fiili **arama tarihini** kaydet+bildir.
- Her PRISMA kademesinde **n + dışlama gerekçesi** kayıt altına al (akış şeması).
- Tarih damgalı export + analiz script'leri arşivle (yeniden üretilebilirlik).

## ⑤ YAZIM (cowork'te)
- Pipeline (brif §9): WRITE → INTEGRITY → REVIEW → REVISE → FINALIZE.
- Yöntem için referans iskelet hazır: `06-yontem-taslak.md` (yapı + gerçek sayılar +
  `[SEARCH DATE]`/`[κ]`/`[N]` yer tutucuları). İstersen temel al.
- Giriş için kavramsal çerçeve + 12 atıf yuvası: `05-giris-cercevesi-taslak.md`.
- Kodlama referansı: `04-kodlama-kitabi.md`. Dergi hedefi: `01-dergi-merdiveni.md`.

## ⑥ CLOUD'UN DENETLEYECEĞİ NOKTALAR (yazım ilerledikçe buraya getir)
- Atıf bütünlüğü: her referans gerçek mi + DOI doğru mu (cloud web ile teyit eder).
- Dergi indeks/çeyreklik son teyidi (JCR + dergi sayfası).
- Metodoloji tutarlılığı (PRISMA 27 madde, korpus sayıları, κ framing).
- "Uydurma yok" ilkesi denetimi.

> Repo senkronu: önemli çıktıları/taslakları `claude/youthful-franklin-wszezx` dalına push et;
> cloud oradan okuyup denetler ve bir sonraki yönergeyi verir.
