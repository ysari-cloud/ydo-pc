# COWORK GÖREVİ 7 — codebook v1.2 ile HAFİF YENİDEN-KOD (yalnız C1/C3/C6)

> ⚠️ ÖNCE SENKRON: `git pull origin claude/youthful-franklin-wszezx` — κ pilotu + v1.2 cloud tarafından eklendi.
> Oku: `04-kodlama-kitabi.md` **v1.2** (karar kuralları), `kol2/27-kodlama-tablosu.md` (mevcut kodlar + adjudikasyon logu), `kol2/30-kappa-sonuc.md` (κ pilotu).

## 0) NEDEN BU GÖREV
κ pilotu (6 makale) **C1/C3/C6**'yı zayıf-uyum buldu (~33–42%). Cloud, 6 anlaşmazlığı tam-metinle uzlaştırıp **codebook v1.2 karar kurallarını** yazdı. Şimdi bu kuralları **tüm 25 makaleye** tutarlı uygulamak gerekiyor. **YALNIZ 3 boyut** gözden geçirilecek; **C2/C4/C5/C7/C8 DOKUNULMAZ** (güçlü-uyum, sabit).

## 1) UYGULANACAK v1.2 KURALLARI (özet — tam tanım `04`'te)
- **C1 a/c/c′ ayracı:** "kim üretiyor?" (öğretmen→a/c · öğrenci→c′) × "yinelemeli mi?" (tek-atımlı generate→use = **a** · yinelemeli ortak-kurgu = **c/c′**).
- **C3 1–5 somut çapa:**
  - **1** = salt tüketici / hazır-otonom sistemin çıktısını yalnız **değerlendiren** (sistemi başkası kurmuş).
  - **2** = uyarlayıcı (çıktıyı düzenler).
  - **3** = üretici-uyarlayıcı (üretir + doğruluk için süzer). **Anket-temelli BEYAN edilen faillik (gözlenmemiş) burada TAVANLANIR.**
  - **4** = tasarımcı (etkin tasarım). **5** = geliştirici (sistem/pipeline düzeyi).
  - Not: *gözlenen* mi *beyan edilen (anket)* mi — ayır.
- **C6 çift kutup:** RİSK kutbu (emek/platform/mahremiyet/eşitsizlik/değer-yakalama/çözümcülük/yazarlık/aşırı-bağımlılık) **VE/VEYA** POZİTİF kutup (mesleki rol yeniden-yapılandırması / öğretmen-öğrenci faillik dönüşümü). Her ikisi de açıkça tartışılıyorsa **ikisini de** kodla.

## 2) ZATEN UZLAŞILMIŞ 6 KAYIT (bunları değiştirme — referans)
| # | Boyut | Son değer |
|---|---|---|
| 6 Lin (CALL) | C1 | **c** |
| 35 Guo | C1 | **c′** |
| 29 Bao | C3 | **1** |
| 34 Zaiarna | C3 | **3** |
| 6 & 19 | C6 | **çift kutup** |

## 3) YAPILACAK İŞ
`kol2/27`'deki 25 makaleyi tek tek geç; **YALNIZ C1, C3, C6** sütunlarını v1.2 ile yeniden değerlendir:
- Mevcut kod v1.2 kuralına uyuyorsa **DOKUNMA**.
- Değişmesi gerekiyorsa **değiştir + kısa tam-metin gerekçesi** (alıntı/iz) ekle.
- Emin değilsen "yeni kod adayı" / "cloud'a sor" diye işaretle, zorlama.
- **Diğer 5 boyut (C2/C4/C5/C7/C8) sabit — dokunma.**

## 4) ÇIKTI (push)
- `kol2/27-kodlama-tablosu.md` güncellenir (değişen hücreler `(v1.2)` etiketli + gerekçe).
- `kol2/31-v1.2-yeniden-kod-degisiklik-logu.md` — hangi makalede C1/C3/C6 ne değişti (özet tablo: # · boyut · eski → yeni · gerekçe). Değişmeyenler "değişmedi" satırıyla.
- 1 paragraf: kaç hücre değişti, C1/C3/C6 yeni dağılım.
- `git add . && git commit -m "akademik: gorev-7 v1.2 yeniden-kod (C1/C3/C6, 25 set)" && git push origin claude/youthful-franklin-wszezx`

## SONRA (cloud)
Cloud değişiklik logunu denetler → **final kodlama kilitlenir** → sentez (AS4–AS5) + yöntem/giriş (`24-komsu-derleme-yontem-analizi.md` şablonu) → **hibrit v3 makale** (yazım cowork, iskelet/denetim cloud). Hedef dergi: **ILE**.
