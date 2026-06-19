# Bibliyometri & Sentez — Bulgu Özeti (Aşama 2)

**Fiili arama/export tarihi:** 2026-06-19 (WoS `DA` alanı, 2105 kayıtta tutarlı).
**Veri tabanları:** WoS Core Collection + Scopus · **Filtreler:** 2018–2026 · İngilizce · Article/Review/Conference.
**Ortam:** Python (pandas/matplotlib/networkx); R yok. Haritalar için VOSviewer (ham WoS + thesaurus) önerilir.

## PRISMA kademe sayıları (akış şeması için)
### Geniş katman (bibliyometrik korpus, A∧D)
- Tanımlanan: WoS 1.936 + Scopus 2.824 = **4.760**
- Çıkarılan mükerrer (DOI + normalleştirilmiş başlık-yıl): **1.706**
- İkilemeden arındırılmış (taranan): **3.054**
- Taramada dışlanan — geri çekilmiş (retracted): **4**
- **Bibliyometrik korpus (dahil): 3.050**
- Atıflanan referansı bulunan WoS kaydı (eş-atıf/eşleşme tabanı): **1.929**

### Odaklı katman (sentez alt-kümesi, A∧D∧C)
- Tanımlanan: WoS 174 + Scopus 303 = **477**
- Çıkarılan mükerrer: **148** → benzersiz: **329** (özetli 328)
- Ön-uygun aday (dergi makale/derleme + üretim ilgisi prod_score≥2 + özet): **223**
- Öncelikli kısa liste (tam-metin önceliği; nihai DEĞİL): **40**
- Erken-üretim köprü makaleleri (2018–2023 ön-uygun, kısa liste dışı): **16**
- İnsan tam-metin tarama seti: **40 + 16 = 56**
- **Nihai n:** tam-metin uygunluk + Cohen κ + 2. insan tarayıcı ile belirlenecek (UYDURULMADI).

## ③ Geniş korpus yıl-dilimi dağılımı (3.050; AS3 için kritik)
| Dilim | Kayıt | Pay |
|---|---|---|
| 2018–2021 | 72 | %2,4 |
| 2022–2023 | 246 | %8,1 |
| 2024–2026 | 2.732 | %89,6 |
| **Toplam (yıllı)** | **3.050** | — |

2024 öncesi taban: **318 (%10,4)**. 2026 kısmîdir (yılın ilk yarısı).

**Yorum (AS3):** Geniş set %89,6 oranında 2024+ olduğundan tematik kayma esas olarak
**"doğuş anındaki hızlı çerçeve kayması"** niteliğindedir. 2018–2023 tabanı (318) klasik
zaman-dilimli tematik-evrim haritası için kullanılabilir ancak dengesiz dilim büyüklükleri
nedeniyle dikkatle yorumlanmalıdır; baskın anlatı 2024 patlamasıdır.

## Öne çıkan performans bulguları
- En üretken ülkeler: Çin 957 · ABD 391 · Suudi Arabistan 192 · BK 158 · G. Kore 144 · Japonya 140 · Türkiye 121 (ilk 10 elle doğrulandı).
- En üretken kaynaklar: System 66 · Computer Assisted Language Learning 59 · Arab World English Journal 55.
- Tematik evrim (TEMİZ sözlük, kelime-sınırı; 2024-06 düzeltmesi): **konuşma çerçevesi %58,3→%35,0→%14,3** (sağlam düşüş); **üretim çerçevesi emergent — mutlak 2→7→51, üretim/konuşma oranı 0,05→0,13** (konuşmayı GEÇMEDİ). ⚠️ Eski "%5,6→%20,3→%38,0 (üretim geçti)" değerleri `'generative'` sözlük şişmesinin yapay sonucuydu — KULLANILMAZ (bkz. `12-cloud-denetim-taslak-v2.md`).

## Sentez ön-kodlama (özet temelli; insan doğrulaması şart)
- Öncelikli-40'ta C1 dağılımı: içerik üreticisi 28 · eş-tasarımcı 6 · özerk geliştirici 4 · konuşma-öğretici 1.
- C8: empirik 22 · kavramsal 10 · belirsiz 6 · derleme 2.
