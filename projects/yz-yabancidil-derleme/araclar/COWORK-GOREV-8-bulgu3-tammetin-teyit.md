# COWORK GÖREV-8 — Bulgu-3 Tam-Metin Teyidi (C1 + C6) + xlsx yeniden üretim
> Bağlam: Görev-7 v1.2 yeniden-kodu cloud tarafından denetlendi (`kol2/32`). C1/C3/C6 değerleri v1.2 codebook'a uygun bulundu; cloud 2 bütünlük açığını kapattı (C6 alt-kodları geri yüklendi; #6/#18 C3 5→4 loglandı). **Geriye yalnız tam-metin gerektiren 3 kalem var — bu görev odur.** İş bitince kodlama KİLİTLENİR → sentez (AS4–AS5).
> ⚠️ Push yok: çıktıyı METİN olarak ver (cowork kum-havuzu GitHub'a push edemiyor); kullanıcı yapıştırır, cloud push eder.

## Kaynak kurallar (codebook v1.2 — `04-kodlama-kitabi.md`)
- **C1 c (eş-tasarımcı):** YİNELEMELİ süreç — *"refine/adjust prompts iteratively"*, gidip-gelme, ortak-kurgu. Tek-atımlı *generate→use* ise **a**.
- **C6 çift kutup:** RİSK + POZİTİF **yalnızca AÇIKÇA tartışılıyorsa** ikisi de kodlanır. "Geçer değinme (mention) ≠ analiz" — geçer değinme yalnız-RİSK kalır. POZİTİF = mesleki rol yeniden-yapılandırması / öğretmen-öğrenci faillik dönüşümü.

## GÖREV A — C1a→c teyidi (#2 Agus, #7 Lenko-Szymanska, #30 Al-Maawali)
Bu 3 makalede Görev-7 `C1a→C1c` yaptı ama İz'de yineleme kanıtı YOK (kıyas: #1/#3/#5/#23/#28/#37'de "iteratively/iterative" alıntısı var).
Her biri için tam metne bak:
- **Yinelemeli prompt/çıktı düzeltme / gidip-gelme VAR mı?**
  - VARSA → **C1c KALIR**; İz'e birebir alıntı ekle (sayfa/cümle).
  - YOKSA (tek-atımlı üret-kullan) → **C1a'ya GERİ DÖN**; `kol2/27` + log güncelle.

## GÖREV B — C6 POZİTİF kutup teyidi (#1 Xin, #4 Xu, #8 Park, #34 Zaiarna)
Bu 4'te Görev-7 çift-kutup (RİSK+POZİTİF) işaretledi ama önceki kodlamada pozitif sinyal yoktu (diğer 9 çift-kutupta C3'te güçlenme/faillik açıkça vardı; bu 4'te yoktu).
Her biri için tam metne bak:
- **Mesleki rol dönüşümü / faillik güçlenmesi AÇIKÇA tartışılıyor mu (analiz düzeyinde, geçer değinme değil)?**
  - EVET → **çift-kutup KALIR**; İz'e birebir alıntı ekle.
  - HAYIR / yalnız geçer-değinme → C6'yı **yalnız-RİSK**'e döndür (alt-kodlar korunur); `kol2/27` + log güncelle.

## GÖREV C — xlsx yeniden üretim
`kol2/27-kodlama-tablosu.md` (cloud-düzeltilmiş, güncel) → `kol2/27-kodlama-tablosu.xlsx` yeniden üret (xlsx hâlâ eski v1.1 kodlarında; md ile senkron değil).

## ÇIKTI (metin olarak ver)
1. **`kol2/33-bulgu3-teyit-logu.md`** (yeni): 7 kalem (A:3 + B:4) için satır satır → *Karar (kaldı/geri-döndü) · birebir tam-metin alıntısı · sayfa*.
2. **Güncellenmiş `kol2/27`** — yalnız değişen hücreler (A/B kararına göre) + ilgili İz alıntıları.
3. **`kol2/27.xlsx`** yeniden üretildi (md ile birebir).
4. Kısa özet: kaç hücre değişti, C1/C6 yeni dağılım.

## İLKE
- **Alıntı UYDURMA.** Belirsizse daha tutucu koda dön (c→a, çift-kutup→yalnız-risk). Bu, hakem savunulabilirliği için emniyet yönüdür.
- Yalnız bu 7 hücre + xlsx; başka boyut/makaleye dokunma.
