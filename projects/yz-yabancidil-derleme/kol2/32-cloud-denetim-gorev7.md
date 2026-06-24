# 32 — Cloud Denetim Raporu: Görev-7 (v1.2 yeniden-kod C1/C3/C6)
> Tarih: 2026-06-24 · Denetleyen: cloud · Girdi: cowork `kol2/27` (revize tablo) + `kol2/31` (değişiklik logu) + codebook v1.2 (`04`) + önceki `kol2/27` (v1.1+adjudikasyon).
> Yöntem: yeni tablo ↔ eski tablo farkı + her değişikliğin v1.2 karar kuralına uyumu + 5 sabit boyutun dokunulmadığının teyidi.

## ✅ DOĞRULANANLAR
- **C1 (18 hücre):** a→c (yinelemeli eş-tasarım), c→c′ (öğrenci eş-yaratım), →e (#8/#29 pipeline), a→a′ (#34 sınav). Hepsi v1.2 codebook §C1 a/c/c′/e/a′ kurallarına uygun.
- **C3 (#4→2, #29→1, #34→3):** v1.2 §C3 somut-çapa kurallarına uygun (#4 araştırmacı-kurmalı→uyarlayıcı; #29 kör-değerlendirici→1; #34 anket-beyan tavanı→3).
- **C6 çift-kutup (13):** sayım log ile tutarlı; çift-kutup açık kuralı (codebook §C6 v1.2) uygulanmış.
- **5 sabit boyut (C2/C4/C5/C7/C8):** değer düzeyinde DEĞİŞMEMİŞ (teyit). *(Yeni tabloda bazı İz/metadata kısaltmaları kozmetikti; cloud, daha zengin önceki içeriği koruyacak biçimde birleştirdi.)*

## ⚠️ BULGULAR ve ÇÖZÜMLER

### Bulgu 1 — C3'te 2 belgesiz değişiklik (ÇÖZÜLDÜ, cloud)
- Yeni tabloda **#6 (5→4)** ve **#18 (5→4)** uygulanmış; `kol2/31` logunda **yoktu**.
- **Değerler DOĞRU:** v1.2'de C3=5 = yalnız "sistem/pipeline düzeyinde kurucu". #6 (materyal tasarlayan öğretmen) ve #18 (faillik açık, materyal tasarlayan öğretmen) → **4 (tasarımcı)** doğru. Korpusta C3=5 = 0 (pipeline çalışmaları #8 C3=4, #29 C3=1 olarak konumlandı; tutarlı).
- **Çözüm:** İki satır `kol2/31`'e `(cloud)` etiketiyle eklendi (gerekçeli). Tablo `kol2/27`'de `4 (v1.2)` olarak işaretli.

### Bulgu 2 — C6 standardizasyonu v1.1 alt-kodlarını sildi (ÇÖZÜLDÜ, cloud)
- Yeni tablo C6'yı "RİSK (etik/bias/emek)" diye genelleştirince codebook §C6 v1.1'in tanımladığı **YAZARLIK** (#14,19,35,40,C04) ve **AŞIRI-BAĞIMLILIK** (#30,A06,C04) alt-kodları kayboldu → tablo ↔ codebook çelişkisi + AS5 (yazarlık/aşırı-bağımlılık) verisi zayıflıyor.
- **Çözüm:** Alt-kodlar eski tablodan `kol2/27`'ye **geri yüklendi**, çift-kutup polaritesi korunarak (RİSK: …alt-kodlar… + POZİTİF: …).

### Bulgu 3 — Tam-metin teyidi gerektiren (COWORK'E AÇIK)
Cloud metadatadan doğrulayamaz; cowork tam-metinden teyit etmeli:
1. **#2, #7, #30 — `C1a→c`:** İz'de **yineleme** kanıtı yok (#1/#3/#5/#23/#28/#37'de "iteratively/iterative" var, bunlarda yok). c (eş-tasarım) kodunu savunmak için İz'e yineleme alıntısı eklensin; yoksa a'da kalmalı.
2. **#1, #4, #8, #34 — C6 POZİTİF kutup:** önceki kodlamada bu 4'te pozitif sinyal yoktu (diğer 9 çift-kutupta C3'te güçlenme/faillik vardı). codebook §C6 "yalnızca açıkça tartışılanlar (geçer-değinme değil)" diyor → bu 4 için açık tam-metin alıntısı eklensin; yoksa yalnız-RİSK'e dönsün.

## Durum
- `kol2/27` (düzeltilmiş tablo), `kol2/31` (tamamlanmış log), `kol2/32` (bu rapor) origin'e push edildi.
- **Kodlama, Bulgu 3 çözülünce KİLİTLENİR.** Bulgu 3'ün AS4/AS5 yönüne etkisi sınırlı (C1c baskınlığı 3 hücre oynasa da değişmez; C6 4 hücre tek-kutba dönse de çift-kutup deseni durur). → Cowork teyidi paralelinde **sentez (AS4–AS5) iskeleti** başlayabilir.
