# VOSviewer ile Bilim Haritalama — Önerilen İş Akışı

**İlke (metodolojik inceleme uyarınca):** Haritalar için en temiz sonuç, VOSviewer'ın
**ham WoS/Scopus dosyalarını kendi parser'ıyla** okumasından gelir. Python ağ dosyaları
(`*_map.txt`, `*_network.txt`, `*.net`) yalnızca rapordaki şekiller ve hızlı önizleme için
üretilmiştir; yayın görselleri için aşağıdaki yol tercih edilmelidir.

## 1) Anahtar-sözcük eş-oluşumu (AS2 — kavramsal yapı)
1. VOSviewer → **Create → Create a map based on bibliographic data**.
2. **Read data from bibliographic database files** → sekme **Web of Science** →
   `raw_data/wos_broad_1..4.txt` dosyalarını birlikte seç. (İstenirse Scopus için
   ayrı sekmede `scopus_broad.csv` eklenebilir; eş-oluşum/keyword katmanı her iki tabandan beslenebilir.)
3. **Type of analysis: Co-occurrence** · **Unit: Author keywords** · Counting: **Full**.
4. **Thesaurus file** alanına bu klasördeki **`thesaurus_keywords.txt`** dosyasını verin
   (ChatGPT/GPT, AI/artificial intelligence, EFL, tekil-çoğul birleştirmeleri uygular).
5. Min. occurrences eşiğini ~5–10 arası ayarlayıp haritayı oluşturun.
6. **Overlay visualization** ile *avg. pub. year* renklendirmesi → tematik kayma (AS3) görsel desteği.

## 2) Eş-atıf (co-citation) ve bibliyografik eşleşme (AS2 — entelektüel yapı)
> **Yalnızca WoS.** Scopus export'unda referanslar yok/dağınık (export sırasında HTTP 503);
> naif birleştirme eş-atıf ağını bozar. Bu iki analiz **sadece** WoS dosyalarıyla yapılır.
1. Create map → bibliographic data → **yalnızca** `wos_broad_1..4.txt`.
2. **Co-citation** · Unit: **Cited references** (veya Cited sources / Cited authors).
3. Bibliyografik eşleşme için: **Bibliographic coupling** · Unit: **Documents / Sources / Countries**.

## 3) Ülke iş birliği
Create map → WoS dosyaları → **Co-authorship** · Unit: **Countries** · Counting: Full.

## Dosyalar
- `thesaurus_keywords.txt` — VOSviewer thesaurus (anahtar-sözcük birleştirme).
- `keyword_cooccurrence_*`, `cocitation_*`, `country_collaboration_*` — Python önizleme ağları
  (Pajek `.net` + VOSviewer `map/network`). İsteğe bağlı; yayın için 1–3. adımları izleyin.
