# 25 — SENTEZ İSKELETİ (AS4–AS5) · Bulgular bölümü omurgası
> 2026-06-24 · **Cloud üretti (iskelet + kanıt haritası + denetim).** Yazım = cowork.
> Kaynak veri: `kol2/27-kodlama-tablosu.md` (v1.2 + Görev-8, KİLİTLİ, N=25). Kod tanımları: `04-kodlama-kitabi.md`.
> Bu dosya **iskelettir**: her tema için araştırma-sorusu bağı, kanıt haritası (ID + kodlanmış veri + İz alıntısı), paragraf planı ve boşluk/uyarı notu verir. `[YAZIM: cowork]` etiketli yerlere düzyazı cowork tarafından yazılır. Cloud düzyazı YAZMAZ.

---

## 0. KULLANIM & ZORUNLU ÇERÇEVE KURALLARI (yazımdan önce oku)

**Kod→AS eşlemesi (codebook §Sentez eşlemesi):**
- **C1 + C2 → AS4** (YZ'nin rolleri + üretim öznesi)
- **C2 + C3 → AS5** (üretim merkezinin kayması + öğretmen failliği)
- **C4 + C6 → Tartışma** (kolaylık↔geçerlilik gerilimi + yapısal riskler) — *AS5 boşluk analizini besler*
- **C8 → kanıt-boşluk haritası** (gelecek gündem)

> ⚠️ **KRİTİK DÖNGÜSELLİK KURALI (codebook satır 103) — yazımda ihlal etme:**
> Sentez setinde **C1b (konuşma-öğretici) = 0** olması **ÖLÇÜT GEREĞİDİR** (salt-konuşma çalışmaları E3/E4 ile dışlandı). Bu yüzden "konuşma→üretim kayması"nın ampirik kanıtı **AS4'ün C1 dağılımı DEĞİLDİR** (döngüsel olur). O kaymanın kanıtı = **bibliyometrik AS3** (geniş 3.050 korpus, tematik evrim). AS4 yalnızca **üretim İÇİNDEKİ rol tipolojisini** betimler; "kayma kanıtı" iddiası kurma.

> ⚠️ **İddia↔kanıt ayrımı (C8):** Her tema cümlesinde "iddia edilen" ile "gösterilen"i ayır. Korpusta tek **GÜÇLÜ** kanıt #35 (kontrollü deney); çoğu orta. Bu, AS5 boşluk argümanının belkemiği.

---

## AS4 — GenAI yabancı dil materyali tasarım/üretiminde hangi rollerle kavramsallaştırılıyor?
*(Ana eksen: C1; destek: C2 + artefakt/araç çeşitliliği C7)*

### AS4 — Kanıt haritası (C1 dağılımı, v1.2+G8, N=25)
| Rol (C1) | n | Makaleler | Çekirdek İz |
|---|---|---|---|
| **C1c — Eş-tasarımcı (yinelemeli, öğretmen-yanlı)** | **11 (BASKIN)** | 1,3,5,6,7,14,23,28,30,37,C04 | #6 'refine/adjust prompts iteratively'; #7 'students refined it in subsequent iterations' (s.7); #30 'modify the outputs'+'significant prompting' (s.8/10) |
| **C1c′ — Öğrenen–YZ eş-yaratımı** | 5 | 13,19,35,40,A06 | #35 40 GFL öğrenci üretici; #19 script→ideas→editing |
| **C1a — İçerik üreticisi (tek-atımlı üret-kullan)** | 5 | 2,4,18,20,C02 | #2 yineleme yok—yalnız DBR döngüsü+atıf (G8); #20 'ChatGPT develops extensive reading materials' |
| **C1e — İnsan-yapılandırmalı pipeline/sistem** | 2 | 8,29 | #8 'automated pipeline'+validation; #29 'we designed and implemented the CCGF' |
| **C1a′ — Değerlendirme/sınav üreticisi** | 1 | 34 | #34 ChatGPT-gen değerlendirme görevi + doğruluk süzme |
| **C1d — Özerk üretici-geliştirici** | 1 | 17 | #17 develop/produce/test instructional media (Ar-Ge/ADDIE) |
| **C1b — Konuşma-öğretici** | **0** | — | ⚠️ ÖLÇÜT GEREĞİ (yukarıdaki döngüsellik kuralı) |

**Destek dağılımlar:**
- **C2 (üretici):** öğretmen ≈16 · öğrenci 4 (13,19,40,A06) · aday öğretmen 2 (7,23) · eş-üretim 1 (35) · sistem 2 (8,29 insan-yapılandırmalı).
- **Artefakt çeşitliliği (C7):** okuma/öğretim materyali · ders planı · storybook · podcast · yaratıcı yazma · öğretim videosu · kelime kartı · dijital öykü/çizgi-roman · sınav görevi · model deneme · öğretim medyası → **çok-kipli, çok-beceri**.
- **Araç:** ChatGPT/jenerik GenAI ≈18 · DALL-E/text-to-image 2 (C02,A06) · LLM+RAG 1 (29) · CopyAI/GPT-3 1 (40) · LLM-genel 1 (35).

### AS4 — Tema yapısı + paragraf planı
**AS4-T1. Baskın rol: tek-atımlı "üretici" değil, YİNELEMELİ EŞ-TASARIMCI.**
- Kanıt: C1c (11) + C1c′ (5) = **16/25 yinelemeli ortak-kurgu**; saf tek-atımlı C1a yalnız 5.
- Argüman: Alan GenAI'yi "düğmeye bas, materyal çıksın" otomatı olarak DEĞİL, öğretmenin/öğrenenin gidip-gelerek biçimlendirdiği **eş-tasarım ortağı** olarak kavramsallaştırıyor.
- `[YAZIM: cowork]` — açış cümlesi + #6/#7/#30 alıntılarıyla örnekleme.

**AS4-T2. Öğretmen-yanlı (C1c) vs öğrenen-yanlı (C1c′) eş-yaratım ayrımı.**
- Kanıt: C1c 11 (öğretmen üretici) ↔ C1c′ 5 (öğrenci üretici: 13,19,35,40,A06).
- Argüman: "kim üretiyor" ekseni AS5'in üretim-merkezi tartışmasına köprü; öğrenen-üretici alt-akımı yazarlık etiğini gündeme getiriyor (→ C6 YAZARLIK, AS5-T3'e bağla).
- `[YAZIM: cowork]`

**AS4-T3. Üst-uç: insan-yapılandırmalı pipeline/sistem (C1e) ve özerk geliştirici (C1d).**
- Kanıt: C1e 2 (#8 Park pipeline, #29 Bao LLM+RAG çok-ajan); C1d 1 (#17 ADDIE/Ar-Ge).
- Argüman: "yazılım düzeyinde üretim" mümkün ama NADİR (3/25) ve **insan yapılandırmasına bağlı**; bu, AS5'teki "tavan" bulgusunu kurar.
- `[YAZIM: cowork]`

**AS4-T4. Alt-uç: değerlendirme-üreticisi (C1a′) + saf içerik-üreticisi (C1a).**
- Kanıt: C1a′ 1 (#34 sınav/değerlendirme — materyalden ayrı artefakt); C1a 5.
- `[YAZIM: cowork]` — kısa.

**AS4-T5. Çeşitlilik vurgusu: çok-dil + çok-kip + çok-araç.**
- Kanıt: 5 dil (EFL çoğunluk + Çince-CFL, Arapça, Romence-RFL, Almanca-GFL); metin+görsel (DALL-E) artefaktlar.
- `[YAZIM: cowork]` — "kapsam genişliği" cümlesi.

> 🔒 **AS4 boşluk/uyarı:** C1b=0 döngüsellik uyarısını burada AÇIKÇA yaz (kaymanın kanıtı=AS3 demektir). Aksi halde hakem "circular reasoning" yakalar.

---

## AS5 — Üretim merkezinin kaymasına dair kanıt/iddia/boşluklar; öğretmen rolü & failliği sonuçları
*(Ana eksen: C2 + C3; eleştirel: C6; kanıt gücü: C8; gerilim: C4)*

### AS5 — Kanıt haritası
**C3 (öğretmen faillik sürekliliği 1–5):**
| C3 | Anlam | n | Makaleler |
|---|---|---|---|
| 4 | tasarımcı | **17 (BASKIN)** | (çoğunluk) |
| 3 | kolaylaştırıcı/üretici-uyarlayıcı | 5 | 13,19,34,40,A06 |
| 2 | uyarlayıcı | 1 | 4 |
| 1 | salt tüketici (otonom sistem) | 1 | 29 |
| 3-4 | — | 1 | 35 |
| 5 | geliştirici | **0** | ⚠️ v1.2: gözlenen öğretmen-tasarımcı tavanı = 4 |

**C6 (eleştirel, çift-kutup, v1.2+G8):**
- **çift-kutup (RİSK+POZİTİF) = 10:** 2,6,7,8,13,17,18,19,23,30 · **yalnız-RİSK = 15**
- POZİTİF kutup = mesleki rol yeniden-yapılandırması / faillik dönüşümü (yalnız 10 çalışma AÇIKÇA tartışıyor).
- Alt-kodlar: **YAZARLIK** = 14,19,35,40,C04 · **AŞIRI-BAĞIMLILIK** = 30,A06,C04.
- **BOŞ HÜCRE:** platform-bağımlılığı / değer-yakalama / çözümcülük (solutionism) → **ZAYIF/yok**.

**C8 (kanıt gücü):** tek **GÜÇLÜ** = #35 (kontrollü deney); çoğu **ORTA** (empirik-karma/nitel, öz-bildirim). C4 halüsinasyon/doğrulama güçlü = #4,8,20,28,29,35.

### AS5 — Tema yapısı + paragraf planı
**AS5-T1. Üretim merkezi yayıncı/uzmandan öğretmen-tasarımcıya kayıyor — AMA "tasarımcı tavanı"nda duruyor.**
- Kanıt: C3=4 ×17 baskın; ama C3=5 (geliştirici) = 0; C1d=1. Yazılım-düzeyi özerklik yalnız insan-yapılandırmalı sistemle (#8,#29).
- Argüman: kayma GERÇEK ama "geliştirici" değil "**tasarımcı**" düzeyinde; demokratikleşme kısmî.
- `[YAZIM: cowork]`

**AS5-T2. Paradoks: sistem-düzeyi üretim failliği AZALTABİLİR.**
- Kanıt: #29 Bao C3=1 — otonom RAG sistemi; öğretmen yalnız **kör-değerlendirici** ('we designed and implemented the CCGF'). #8 Park pipeline'da rol 'content creators→curators and editors' (s.15).
- Argüman: en yüksek otomasyon, öğretmeni üreticiden denetleyiciye/küratöre indirebilir → faillik tek-yönlü artmıyor.
- `[YAZIM: cowork]`

**AS5-T3. Faillik çoğunlukla POZİTİF çerçeveleniyor ama (a) kanıt zayıf, (b) bazen yalnız BEYAN.**
- Kanıt: C6 pozitif kutup 10/25; ama C8 tek güçlü #35; #34 faillik **anket-beyanı (gözlenmedi)**, C3=3 tavanında.
- Argüman: "güçlenme" anlatısı **iddia düzeyinde**; gözlemlenmiş kanıt seyrek = AS5 boşluğu.
- `[YAZIM: cowork]` — iddia↔kanıt ayrımını burada vurgula.

**AS5-T4. Öğrenen-üretici alt-akımı + yazarlık etiği.**
- Kanıt: C2c/C1c′ 4-5 çalışma (13,19,35,40,A06); C6 YAZARLIK = 14,19,35,40,C04; AŞIRI-BAĞIMLILIK = 30,A06,C04.
- Argüman: üretim merkezi öğretmeni de aşıp öğrenene kayınca "kim yazar?" ve aşırı-bağımlılık/vasıfsızlaşma soruları çıkıyor.
- `[YAZIM: cowork]`

**AS5-T5. BOŞLUKLAR — bu derlemenin özgün katkısı (negatif bulgu = bulgu).**
- **(a) Yapısal eleştiri neredeyse boş:** platform-bağımlılığı/değer-yakalama/çözümcülük C6'da ZAYIF. STORM persp. 3 (eleştirel edtech) & 4 (yayıncı ekonomisti) bunu öngördü → literatür büyük ölçüde sessiz.
- **(b) Kanıt < iddia:** 1 güçlü çalışma; "son kilometre" pedagojik geçerlilik & iş yükü, üretim-kolaylığı coşkusuna kıyasla az incelenmiş (C4 gerilimi).
- **(c) Faillik beyan ↔ gözlem açığı** (#34 örneği).
- `[YAZIM: cowork]` — gelecek-araştırma gündemine bağla.

> 🎯 **"What this paper adds" çengelleri (cowork giriş/sonuç kutusuna):**
> 1. Alan GenAI'yi baskın olarak **yinelemeli eş-tasarımcı** olarak kavramsallaştırıyor (tek-atımlı otomat veya konuşma-partneri değil).
> 2. Üretim merkezi öğretmen-**tasarımcıya** kayıyor ama yazılım-geliştirici düzeyinin ALTINDA kalıyor ve **az kanıtlanmış**.
> 3. **Yapısal/eleştirel boyut (değer-yakalama, platform-bağımlılığı) bir boş hücre** = derlemenin ayırt edici boşluk-bulgusu.

---

## Yazım notları (cowork)
- Tablo/sayılar bu dosyadan birebir; **uydurma yok** (codebook değişmez ilke).
- Her tema → 1 İz alıntısıyla örneklenir (denetlenebilirlik); alıntı `kol2/27` "Alıntı/İz" sütunundan.
- Bölüm sırası önerisi: AS4 (T1→T5) → AS5 (T1→T5) → Tartışma (C4↔C6 gerilimi) → Boşluk/gelecek gündem.
- Üslup: writing-anti-ai; iddia↔kanıt ayrımı her temada görünür olsun.
- Komşu-derleme şablonu (`24-komsu-derleme-yontem-analizi.md`): κ raporla, "What this paper adds" kutusu kullan.

## Cloud denetim teyidi
- Tüm n'ler `kol2/27` v1.2+G8 ile doğrulandı: C1 (11+5+5+2+1+1=25 ✓); C6 çift-kutup 10 ✓; C3 dağılımı ✓.
- Döngüsellik (C1b=0) ve iddia↔kanıt (C8) uyarıları iskelete gömüldü.
- **Sıradaki:** cowork bu iskeletten AS4–AS5 düzyazısını yazar → cloud bütünlük/metodoloji denetimi.
