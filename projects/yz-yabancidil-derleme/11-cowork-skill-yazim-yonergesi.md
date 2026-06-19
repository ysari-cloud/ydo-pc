# Yeni Cowork Penceresi — Skill-Tabanlı Yazım Yönergesi (kıyas sürümü)

> Kullanıcı bunu yeni bir cowork oturumuna yapıştırır; dosya konumunu kullanıcı gösterir.
> Amaç: mevcut doğrudan-yazım taslağı (**`Makale_Taslak_v2.docx`** — AS3-düzeltilmiş, atıfları
> doğrulanmış, yüksek çıta) ile KIYASLAMAK için, aynı kapsamda SKILL-tabanlı bağımsız bir taslak üretmek.

---

**GÖREV:** Aşağıdaki akademik makalenin tam taslağını **skill-tabanlı** olarak, bağımsız (mevcut taslağa bakmadan kendi kalemde) yaz. Bu bir KIYAS sürümüdür; ayrı dosyaya yazılacak, mevcut taslağın üzerine YAZILMAYACAK.

**1) ÖNCE SKİLLERİ KONTROL ET + AKTİVE ET**
- Şu skiller kurulu mu bak: `academic-paper`, `writing-anti-ai`, (sonraki aşama için) `academic-paper-reviewer`.
- Varsa: **`academic-paper` (full mod, literature-review yapısı, APA 7.0)** + **`writing-anti-ai`** kullan.
- Yoksa: hangilerinin kurulu olduğunu bildir, kalanları kendi kalemle yaz.

**2) GİRDİ DOSYALARI (repodan oku — kullanıcı konumu gösterecek)**
`projects/yz-yabancidil-derleme/` altında:
- `00-PROJE-BRIFI.md` — kilitli kararlar, RQ'lar, başlık, kapsam (TEK doğruluk kaynağı).
- `05-giris-cercevesi-taslak.md` — giriş 4-move argüman mimarisi + 12 atıf yuvası.
- `06-yontem-taslak.md` — yöntem iskeleti + gerçek sayılar + yer tutucular.
- `04-kodlama-kitabi.md` — C1–C8 codebook.
- `analysis/08-bibliometri-bulgu-ozeti.md` — bibliyometri bulgu sayıları.
- `09-cloud-denetim-ve-yonerge.md` + `10-cloud-denetim-taslak-v1.md` — denetim notları (AS3 düzeltmesi, APA/PRISMA uyarıları, bütünlük kuralları).

**3) NE YAZILACAK (kapsam = mevcut taslakla aynı, kıyas için)**
Abstract + Keywords · Giriş (4-move) · Yöntem · Bulgular-Bibliyometri (RQ1–RQ3) · ön-Sentez (RQ4–RQ5, açıkça "ön/özet temelli" etiketli) · Tartışma iskeleti · Kaynakça. Dil: İngilizce, APA 7.0.

**4) ⚠️ AS3 — TEMİZ SAYILARI KULLAN (artık v2'de hazır)**
Tematik evrim için **temiz sözlük sonuçlarını** kullan (v2'deki gibi): konuşma %58,3→%35,0→%14,3
(sağlam düşüş); üretim emergent (mutlak 2→7→51; oran 0,05→0,13, konuşmayı GEÇMEDİ). Dürüst çerçeve:
"konuşmadan uzaklaşma güçlü; üretime kayma gerçek ama doğmakta". **ESKİ %38 manşetini KULLANMA.**

**5) BÜTÜNLÜK (pazarlık dışı)**
- Hiçbir kaynak/DOI/sayı UYDURMA. Yalnız doğrulanmış atıflar gerçek künyeyle.
- Doğrulanamayan klasik kavramsal atıflar → `[CITE: ...]` yer tutucu.
- Cohen κ ve nihai sentez N → yer tutucu (henüz insan tam-metin doğrulaması yapılmadı).
- Bütünlük + YZ-destek beyanı ekle. Çeyreklik/indeks bilgisi JCR/dergi sayfasından teyitli.
- APA: kaynakça girişlerinde "et al." kullanma (tüm yazarları yaz, ≤20).

**6) ÇIKTI + TESLİM**
- Dosya adı: **`Makale_Taslak_skill.docx`** (mevcut `Makale_Taslak_v1/v2.docx`'i EZME).
- `claude/youthful-franklin-wszezx` dalına commit + push et.
- Hangi skilleri kullandığını ve v2'den farklı/güçlü yaklaştığın noktaları kısaca raporla.

> Kıyas notu: v2 zaten AS3-düzeltilmiş + 12/12 atıf doğrulanmış + duyarlılık + PRISMA checklist
> içeriyor (yüksek çıta). Skill sürümü bunlara denk gelmeli VE üslup/argüman akışında fark yaratmalı.

> Bittiğinde cloud denetim oturumu iki taslağı (doğrudan vs skill) yan yana kıyaslayıp hangisinin
> daha güçlü olduğunu (argüman, akış, bütünlük, SSCI uygunluğu) raporlayacak.
