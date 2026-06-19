# Proje: Sohbetten Üretime — YZ & Yabancı Dil (Bibliyometri + Sistematik Derleme)

> Akademik proje. Web sitesi operasyonlarından **bağımsız**. Tam brif:
> `projects/yz-yabancidil-derleme/00-PROJE-BRIFI.md` (kilitli kararlar, PRISMA protokolü,
> arama dizgeleri, STORM çıktısı, kodlama şeması, iş akışı — hepsi orada).

## 🔖 DEVAM NOKTASI
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
