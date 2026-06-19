# Proje: Sohbetten Üretime — YZ & Yabancı Dil (Bibliyometri + Sistematik Derleme)

> Akademik proje. Web sitesi operasyonlarından **bağımsız**. Tam brif:
> `projects/yz-yabancidil-derleme/00-PROJE-BRIFI.md` (kilitli kararlar, PRISMA protokolü,
> arama dizgeleri, STORM çıktısı, kodlama şeması, iş akışı — hepsi orada).

## 🧭 ROL DAĞILIMI (kullanıcı kararı, 2026-06-19 — KESİN)
- **Cowork (kullanıcı PC'si) = TÜM YÜRÜTME + TÜM YAZIM.** Bibliyometri, sentez, makale metni
  hepsi orada yazılır. Yazım TEK yerde olacak.
- **Bu oturum (cloud) = TAKİP + YÖNLENDİRME + DENETİM.** Metodoloji/bütünlük kontrolü, dergi/atıf
  doğrulama (web erişimi var), yönerge hazırlama, kalıcı hafıza. **Cloud makale metni YAZMAZ.**
- `06-yontem-taslak.md` = cowork'ün kullanabileceği REFERANS iskelet (paralel taslak değil).

## 🔖 DEVAM NOKTASI
- **✅ AŞAMA 2 GELDİ + DENETLENDİ (cloud, 2026-06-19) → `09-cloud-denetim-ve-yonerge.md`.**
  Cowork tam bibliyometriyi push etti (`analysis/`: 14-sayfa xlsx, 13 figür, PRISMA diyagramı,
  VOSviewer dosyaları, scriptler, repro manifest, `08-bibliometri-bulgu-ozeti.md`).
  - **PRISMA tam:** geniş 4.760→3.050 (retracted 4 çıktı); odaklı 477→329→223→40 öncelik→+16 köprü
    =56 insan-set. Arama tarihi 2026-06-19. κ uydurulmadı. Bütünlük örnek düzeyde (sha256, WoS-CR).
  - **Yıl dağılımı:** 2018-21=72 · 2022-23=246 · 2024-26=2.732 (%89,6). AS3 = "doğuş anı hızlı kayma".
  - **🔴 KRİTİK CATCH:** AS3 çerçeve niceliği (`run_full.py` CONV_LEX/PROD_LEX) KİRLİ → `'generative'`
    PROD_LEX'te olduğu için 2024-26 üretim sayısı yapay şişmiş; jenerik terimler + `oral` substring
    hatası + substring eşleşme. **Temizlenip AS3 yeniden çalıştırılmadan yazıya GİRMEMELİ.** SliceKeywords
    nitel olarak kaymayı bağımsız destekliyor → tez muhtemelen DOĞRU, sadece temiz nicelik gerek.
  - Performans güvenilir (Çin 957/…/Türkiye 121; kaynaklar System 66+CALL 59 = hedef merdiven tepesi).
- **Sıradaki:** (cowork) AS3 temiz re-run→Bulgular yaz · (kullanıcı) 56-set tam-metin+2.tarayıcı→κ ·
  (cloud) taslakta atıf/DOI bütünlük + dergi çeyreklik teyidi. **Güvenlik:** GitHub token REVOKE edilsin.
- **✅ EXPORT YAPILDI (kullanıcı, kurumsal erişim).** Korpus sayıları (gerçek veri, 2026-06-19):
  **Geniş katman (A AND D) = 3.050 kayıt** · **Odaklı katman (A AND D AND C) = 328 kayıt.**
  Geniş ≫300 → brif kalibrasyonu sağlandı, C aramada kalır. Dedup + PRISMA-identification tamam.
- **KARAR (brif §4/§6 ile sabit): Tam bibliyometri = GENİŞ set (3.050) üzerinde** (AS1–AS3:
  performans + eş-atıf/eşleşme/eş-oluşum + tematik evrim — büyük korpus ister). **Odaklı 328 =
  SENTEZ hattı** (AS4–AS5); tam-metin elemesiyle 20–60'a inecek, bibliyometriye SOKULMAZ.
- **Ortam notu:** Bibliyometri yürütümü kullanıcının cowork/yerel oturumunda; R/bibliometrix YOK
  → Python (pandas/matplotlib) + VOSviewer ağ dosyaları. WoS ham dosyaları zengin alanlı
  (AU/AF/C1/C3/DE/ID/CR/TC); minimal dedup CSV yerine HAM dosyalardan tam metadata re-parse.
- **Önceki blokaj (§10.1 export) ÇÖZÜLDÜ;** sıradaki = analiz yürütümü (cowork oturumu).
- **🔄 ANALİZ UÇUYOR (cowork, 2026-06-19):** biblio_analysis.py yazıldı; 6 adım = (1) ham
  metadata parse → (2) performans AS1 → (3) bilim haritalama AS2 → (4) tematik evrim AS3
  (2018-21/2022-23/2024-) → (5) çıktı derleme (Excel/figür/VOSviewer/Word) → (6) figür-tablo
  doğrulama. Brife uygun. **Teknik watch-out (cowork'e relay edildi):** eş-atıf=WoS `CR`
  üzerinden (Scopus refs ayrı); haritalar için ham dosya→VOSviewer doğrudan; keyword thesaurus
  normalizasyonu (ChatGPT/GPT, AI, tekil-çoğul); ülke/kurum C1/C3 parse'ı gözle doğrula.
  Cowork çıktıları (tablolar + dahil-liste) bu repoya commit edilecek → ben yazım+doğrulamaya geçeceğim.
- **✅ SENTEZ ÖN-TARAMASI İNCELENDİ (cloud, 2026-06-19) → `synthesis_screening.xlsx` repoda.**
  Odaklı 329 (328 özetli) → 223 ön-uygun (journal+review, prod_score≥2, özet var) → 40 kısa liste
  (relevans sıralı; atıf medyanı 2.5 → atıf SÜRMEMİŞ, relevans sürmüş — atıf-yanlılığı endişesi
  GEÇERSİZ, geri çekildi). **Kısa liste %95 2024+ (38/40); tüm odaklı korpusun %92'si 2024+ —
  KUSUR DEĞİL, üretim çerçevelemesinin 2024+ olgusu olması = teze BULGU.** C1: 28 içerik üreticisi
  +6 eş-tasarımcı+4 özerk → teze birebir; 22 empirik. **Geçerli 2 rafine (cowork'e):** (1) 223→40
  PRISMA'da "tam-metin öncelikli kısa liste" diye çerçevele, dışlama değil; (2) 2022-23'te 13 uygun
  varken kısa listede 2 → erken-üretim makaleleri (kayma köprüsü) kaybolmasın, insan taramasına
  40+kalan ~11 erken girsin. **AÇIK SORU:** AS3 (zaman-içi kayma) için GENİŞ korpusun (3.050) yıl
  dağılımı kritik — "öncesi" temel hattı orada; cowork'ten o dağılımı iste.

## ⚖️ Değişmez ilkeler (brif §1)
- Hiçbir kaynak/atıf/DOI/sayı UYDURULMAZ. Doğrulanamayan kaynak rapora girmez.
- Çeyreklik/indeks bilgisi her zaman JCR/Scopus + dergi sayfasından teyit edilerek yazılır.
- STORM yalnızca girişin kavramsal çerçevesi için; yöntem omurgası = PRISMA 2020.
- Hedef indeks: SSCI. Birincil dergi: Interactive Learning Environments (ILE).

## ✅ Dergi merdiveni teyit EDİLDİ (§10.2 TAMAM, 2026-06-19) → `01-dergi-merdiveni.md`
Tüm adaylar SSCI Q1. Önerilen sıra: **ILE → ReCALL → CALL → JCAL → System.**
- **ILE** (T&F) — Q1(2024), IF ~5.3, 2025'te 382 makale, GenAI kapsamda → **BİRİNCİL.**
- **ReCALL** (Cambridge/EUROCALL) — Q1; kapsamında "meta-analiz/sentez/survey" AÇIKÇA davet →
  sistematik derlemeye en açık sözel uyum. GÜÇLÜ CALL-özel 2. basamak.
- **CALL** (T&F) — Q1, kapsam birebir. Yukarı-oynama yedeği (rekabetçi).
- **JCAL** (Wiley) — Q1(2024), eğitim-tek. · **System** (Elsevier) — ~IF 4.9, dilbilim ağırlıklı.
- ~~Education and Information Technologies~~ — derleme kabul ETMİYOR, merdiven dışı.
- ⚠️ Aggregator IF'leri şişik olabilir (JCAL/ReCALL); manuscript'e yazılacak KESİN IF/çeyreklik
  + her derginin review-article kelime limiti = kullanıcının kurumsal JCR + dergi sayfasıyla
  son doğrulanacak (bazı dergi sayfaları bu ortamda 403).

## 📁 Üretilen dosyalar (projects/yz-yabancidil-derleme/)
- `00-PROJE-BRIFI.md` — tam brif (değişmez referans).
- `01-dergi-merdiveni.md` — SSCI dergi teyidi (§10.2 TAMAM).
- `02-export-rehberi.md` — kullanıcının sabah izleyeceği WoS+Scopus arama&indirme kılavuzu.
- `03-prisma-protokol.md` — a priori PRISMA 2020 protokolü (OSF-hazır iskelet).
- `04-kodlama-kitabi.md` — C1–C8 codebook (tanım+karar kuralı+örnek), v0.1.
- `05-giris-cercevesi-taslak.md` — §8a giriş argüman iskeleti, 12 `[ATIF:]` yuvası (uydurma YOK).
- `06-yontem-taslak.md` — Yöntem bölümü prose taslağı v1 (İngilizce, PRISMA 2020). Gerçek sayılar
  gömülü (3.050/329/223); `[SEARCH DATE]`/`[κ]`/`[N]` + atıf yuvaları doğrulamaya açık.
- `synthesis_screening.xlsx` — cowork sentez ön-taraması (incelendi).

## ⏭️ Kullanıcı sabah dönünce
1. `02-export-rehberi.md`'yi izle → WoS+Scopus geniş katman sonuç SAYILARINI bana söyle (kalibrasyon).
2. Export dosyalarını yükle → §10.3: dedup → PRISMA eleme (κ) → Bibliometrix/VOSviewer.
3. `03`/`04`/`05` taslaklarını birlikte gözden geçir; açık kararlar (protokol §10): ikinci
   tarayıcı? OSF ön-kayıt? odaklı alt-küme arama mı süzme mi?
4. Atıf yuvaları SADECE doğrulanmış kaynakla doldurulur (DOI teyitli).

> ⚠️ Araç notu: brif §9'daki `academic-paper`, `academic-paper-reviewer`,
> `systematic-review` skill'leri kullanıcının YEREL PC kurulumundandı. Bu bulut ortamında
> mevcut olan: `deep-research`. Yazım aşamasında skill yerine doğrudan üretim + bütünlük
> doğrulaması yapılır.
