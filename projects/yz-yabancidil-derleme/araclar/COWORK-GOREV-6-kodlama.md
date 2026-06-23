# COWORK GÖREVİ 6 — C1–C8 KODLAMA (nihai 25 set) + bağlam

> ⚠️ ÖNCE SENKRON: `git pull origin claude/youthful-franklin-wszezx` — son kararlar cloud tarafından eklendi.
> Bu dosya tek başına yeterli bağlamı verir; ayrıca oku: `04-kodlama-kitabi.md` (v1.0), `kol2/25`, `kol2/26`, `23-dahil-olcutu-ve-derlemeler.md`.

## 0) GÜNCEL DURUM (kilitli)
- **NİHAİ DAHİL N = 25.** ana 22 + Kol-2 3 (A06, C02, **C04**). Liste: `kol2/25-nihai-included-listesi.md`.
- **C04 = İÇERİ** (mühürlü), **#35 Guo = tam-metin teyitli İÇERİ**, **#39 = DIŞLA** (JIPD predatory).
- **Ölçüt (kilitli):** (1) birincil ampirik (2) üretken/generative YZ (3) **GenAI ile artefakt üretimi — üreten öğretmen VEYA öğrenci VEYA eş-üretim**; salt kullanım/feedback/konuşma DIŞARI. Detay: `23-dahil-olcutu-ve-derlemeler.md`.
- **Sentez yaklaşımı = HİBRİT** (tümdengelim C1–C8 + tümevarım kapısı + κ).
- **Bibliyometri 3.050 DONUK** (predatory sınırlılığı: EnPress-ailesi 23 kayıt, `kol2/26 §F`).

## 1) ÖN İŞ — eksik 2 PDF geldi → final artefakt-teyidi
Kullanıcı indirdi (TAM_METIN klasörüne koy):
- **#13 Lin 2025** (Computers and Composition, DOI 10.1016/j.compcom.2024.102895) — öğrenci çok-kipli kompozisyon.
- **#19 Risang Baskara 2024** (LTRQ) — öğrenci podcast.
→ İkisinde de tam metinden **"gerçekten GenAI ile artefakt üretiliyor mu (yalnız öğrenme çıktısı değil)"** son teyidini yap. Geçerse N=25 sabit; geçmezse not düş, cloud'a bildir. (#35 Guo zaten cloud'ca teyitli.)

## 2) ANA İŞ — 25 makaleyi kodla (kodlama kitabı v1.0, HİBRİT)
Her makale için `04-kodlama-kitabi.md` v1.0 ile:
- **Betimleyici alanlar:** Araç · Üretici (öğretmen/öğrenci/aday öğretmen/eş-üretim) · Artefakt türü · Dil.
- **C1–C8** boyutları (tanım+karar kuralları dosyada).
- **Tümevarım kapısı:** bir makale mevcut kategoriye OTURMUYORSA zorlama → **"yeni kod adayı"** + tam-metin alıntısı işaretle (cloud şemaya ekleyecek).
- **İz:** her önemli hücrede kısa **alıntı/sayfa** (denetlenebilirlik).

## 3) κ (kodlayıcılar-arası uyum)
- Cowork = 1. kodlayıcı (25'in tamamı). **Kullanıcı = 2. kodlayıcı, ≥%20 alt-küme (≈5-6 makale), bağımsız** → cloud κ hesaplayacak. (Tarama'daki insan↔YZ mantığı.)

## 4) ÇIKTI (push)
- `kol2/27-kodlama-tablosu.md` (+ mümkünse `.xlsx`) — tüm 25, sütunlar: `ID | Yazar-Yıl | Araç | Üretici | Artefakt | Dil | C1..C8 | Alıntı/Not`.
- `kol2/28-yeni-kod-adaylari.md` — tümevarımla çıkan kategori önerileri (varsa).
- 1 paragraf: araç/üretici/artefakt/dil + C1 rol dağılımı özeti.
- `git add . && git commit -m "akademik: gorev-6 C1-C8 kodlama tablosu (25 set)" && git push origin claude/youthful-franklin-wszezx`

## 5) PARALEL (cloud yapıyor, cowork'ü bağlamaz)
Cloud, **komşu SSCI derlemelerin yöntem-analizini** yapıyor (Deng, Griche, Two Years of Innovation, hedef-dergi örnekleri) → makale iskeleti + ayrışma haritası. Kullanıcı o PDF'leri cloud'a yüklüyor.

## SONRA
Kodlama + κ bitince → cloud yeni kod adaylarını şemaya işler, κ raporlar, **sentez (AS4–AS5)** yazıma hazır → **hibrit v3 makale** (yazım cowork, iskelet/denetim cloud). Hedef dergi: **ILE** (merdiven ILE→ReCALL→CALL→JCAL→System).
