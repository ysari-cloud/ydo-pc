# Kodlama Kitabı (Codebook) — Sentez Katmanı

> Brif §8b'deki C1–C8 şemasının uygulanabilir hâli: her boyut için **tanım, kategoriler,
> karar kuralı ve örnek**. Tümdengelimli başlangıç; kodlama sırasında tümevarımlı düzeltilir
> (yeni kategori çıkarsa buraya eklenir + versiyon notu düşülür). Her dahil edilen çalışma bu
> şemayla kodlanır; kodlayıcılar-arası uyum κ ile raporlanır.

## Kullanım
- Birim = tek çalışma (makale/derleme).
- Her boyut için EN UYGUN kategori(ler) seçilir; C7/C8 çoklu olabilir.
- Belirsizse → tam metinden alıntı + "karar notu" sütununa gerekçe.
- Kodlama tablosu sütunları (v1.0): `ID | Yazar-Yıl | Araç | Üretici | Artefakt türü | Dil | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | Alıntı/Not`.

## Hibrit kodlama yordamı (tümdengelim + tümevarım)
1. **Tümdengelimli geçiş:** her makaleyi C1–C8 iskeletiyle kodla (a priori = tezin C1 tipolojisi).
2. **Tümevarımlı kapı:** makale mevcut kategoriye OTURMUYORSA zorlama → "yeni kod adayı" + tam-metin alıntısı işaretle.
3. **Uzlaşı + güncelleme:** yeni kod adayları toplanır → cloud ile gözden geçirilir → şemaya eklenir (tarih + versiyon notu). ("Doğrula → örtmezse ekle" döngüsü.)
4. **Doğrulama:** ≥%20 alt-kümede ikinci kodlayıcı (insan ↔ YZ) → kodlayıcılar-arası uyum (κ); anlaşmazlık tam-metinle çözülür.
5. **İz:** her hücre kararı için kısa alıntı/not (denetlenebilirlik).

---

## C1. YZ'nin rolü
Çalışmada üretken YZ hangi işlevle kavramsallaştırılıyor?
- **C1a — İçerik üreticisi:** metin/alıştırma/materyal *üretir* (öğretmen yönlendirir).
- **C1b — Konuşma-öğretici (muhatap):** öğrenenle diyalog/pratik partneri (sohbet ucu).
- **C1c — Eş-tasarımcı / yardımcı:** öğretmenle birlikte tasarlar, taslak/öneri verir.
- **C1d — Özerk üretici-geliştirici:** uygulama/site/courseware gibi *yazılım düzeyinde* ürün üretir.
- **C1a′ — Değerlendirme/sınav üreticisi (v1.1):** test/rubrik/quiz = değerlendirme artefaktı (materyalden ayrı). İz: #34 Zaiarna.
- **C1c′ — Öğrenen–YZ eş-yaratımı (v1.1):** YZ öğrenenin yaratıcı sürecinde ortak/yardımcı (öğretmen-yanlı C1c'den ayrı). İz: #13, #19, #40, A06.
- **C1e — İnsan-yapılandırmalı üretken pipeline/sistem (v1.1):** öğretmen yapılandırır, sistem seri üretir (C1a↔C1d arası). İz: #8 Park, #29 Bao.
- *Karar kuralı:* baskın işlev seçilir; birden çok belirginse en üst düzey üretim (d>c>a>b) işaretlenir, not düşülür.
- **🔧 v1.2 a/c/c′ KARAR KURALI (κ pilotundan):**
  - **a (içerik-üretici):** tek-atımlı *generate→use* — öğretmen prompt verir, çıktıyı alır/kullanır (yinelemeli ortak-kurgu YOK).
  - **c (eş-tasarımcı):** **yinelemeli** süreç — *"refine/adjust prompts iteratively"*, gidip-gelme, ortak-kurgu (öğretmen-yanlı). İz: #6 Lin.
  - **c′ (öğrenen–YZ eş-yaratımı):** üreten ÖĞRENCİ + yinelemeli eş-yaratım. İz: #35 Guo, #13, #19, #40, A06.
  - **Ayraç:** "kim üretiyor?" (öğretmen→a/c, öğrenci→c′) × "yinelemeli mi?" (hayır→a, evet→c/c′).
- *Korpus-gözlemli artefakt türleri (25):* okuma/öğretim materyali · ders planı · storybook · podcast · yaratıcı yazma · öğretim videosu · kelime kartı · dijital öykü/çizgi-roman · sınav/değerlendirme görevi · örnek metin (model deneme) · öğretim medyası. *(tümevarımla genişletilebilir.)*
- *Korpus araçları:* ChatGPT/GPT · Gemini · Copilot · Claude · DALL-E/text-to-image · LLM+RAG.

## C2. Üretim merkezi (kim üretiyor?)
Materyal/ürün üretiminin ağırlık merkezi kimde?
- **C2a — Yayıncı/uzman.** **C2b — Öğretmen-üretici.** **C2b⁺ — Aday öğretmen (öğretmen eğitimi).** **C2c — Öğrenen-üretici.** **C2d — İnsan-YZ eş-üretimi.** *(Korpusta: öğretmen çoğunluk · öğrenci 3 · aday öğretmen 2 · eş-üretim 1.)*
- **Aracısızlaşma derecesi:** düşük / orta / yüksek (uzman aracı ne kadar devre dışı?).
- *Karar kuralı:* çalışmanın betimlediği fiili üretim öznesi esas alınır (öneri değil, uygulama).
- **🔧 v1.2 c-vs-d KURALI:** öğrenci tek başına üretirse **c**; öğrenci+YZ **yinelemeli eş-yaratım** ise (C1c′ ile eşleşir) → **d** (aracısızlaşma öğretmen denetimiyle orta→yüksek). İz: #35 Guo (c′→d). *Not: üretici kimliği (in-service/pre-service/öğrenci) yalnız b/b⁺/c ETİKETİDİR — dahil/amaç filtresi DEĞİL.*

## C3. Öğretmen rolü & failliği
- **Süreklilik:** tüketici/uyarlayıcı ↔ tasarımcı/geliştirici (5'li: 1=salt tüketici … 5=geliştirici).
- **Mesleki kimlik:** güçlenme / dönüşüm / tehdit olarak çerçeveleniyor mu?
- **Vasıf yönü:** vasıfsızlaşma (deskilling) / yeniden vasıflanma (reskilling) / karışık / belirsiz.
- *Karar kuralı:* yazarın açık çerçevelemesi + örtük ima ayrı not edilir.
- **🔧 v1.2 1–5 SOMUT ÇAPA (κ pilotundan):**
  - **1 = salt tüketici:** hazır/otonom sistemin çıktısını kullanır veya **yalnız değerlendirir** (sistemi başkası kurmuş). İz: #29 Bao (öğretmen kör-değerlendirici).
  - **2 = uyarlayıcı:** YZ çıktısını düzenler/uyarlar.
  - **3 = kolaylaştırıcı/üretici-uyarlayıcı:** YZ ile üretir + doğruluk için süzer. **Anket-temelli BEYAN edilen faillik (gözlenmemiş) burada tavanlanır.** İz: #34 Zaiarna.
  - **4 = tasarımcı:** materyali/görevi etkin tasarlar.
  - **5 = geliştirici:** sistem/pipeline düzeyinde kurar.
  - **Çapa notu:** *gözlemlenen* faillik mi, *beyan edilen* (anket) mi — ayır; otonom-sistem bağlamında "öğretmen son-kullanıcı=1".

## C4. Pedagojik geçerlilik & kalite güvencesi
- **Hizalama:** hedef/CEFR/müfredat hizalaması ele alınıyor mu? (evet/kısmen/hayır)
- **Erişilebilirlik:** a11y/kapsayıcılık değiniliyor mu?
- **Hata/halüsinasyon:** çıktı doğruluğu/halüsinasyon riski tartışılıyor mu?
- **Değerlendirme pratiği:** üretilen materyal nasıl doğrulanıyor? (uzman denetimi / pilot / yok)
- *Karar kuralı:* her alt-madde ayrı işaretlenir; "son kilometre uyarlama/iş yükü" vurgusu not.

## C5. Yeterlikler & öğretmen eğitimi
- YZ okuryazarlığı / prompt-tasarım okuryazarlığı / çıktı değerlendirme / etik —
  hangileri gerekli görülüyor? (çoklu işaret)
- **Kuram bağı:** TPACK / "YZ-çağı TPACK" / başka çerçeve anılıyor mu? (yaz)
- *Karar kuralı:* önerilen yeterlikleri liste hâlinde çıkar; öğretmen eğitimi önerisi var mı?

## C6. Eleştirel / yapısal boyutlar
Çalışma şunlardan hangilerine değiniyor? (çoklu)
- emek yoğunlaşması / platform bağımlılığı / veri-mahremiyet / eşitsizlik-dijital uçurum /
  değer yakalama (value capture) / çözümcülük (solutionism) eleştirisi.
- **(v1.1) Yazarlık/özgünlük/sahiplik etiği:** üretilen artefaktta "kim yazar?" — özellikle öğrenen/eş-üretimde. İz: #14, #19, #35, #40, C04.
- **(v1.1) Aşırı-bağımlılık / öğrenen vasıfsızlaşması:** GenAI'ye aşırı güven, özerklik kaybı. İz: #30, A06, C04.
- **🔧 (v1.2) ÇİFT KUTUP — açık kural:** C6 iki kutuplu kodlanır:
  - **RİSK kutbu:** emek / platform bağımlılığı / mahremiyet / eşitsizlik / değer-yakalama / çözümcülük / yazarlık / aşırı-bağımlılık.
  - **POZİTİF kutup:** mesleki rol yeniden-yapılandırması / öğretmen-öğrenci faillik dönüşümü.
  - Bir çalışma **her iki kutbu da** açıkça tartışıyorsa **ikisi de** kodlanır. İz: #6 Lin (TPI dönüşümü + bias/emek), #19 Baskara (yaratıcı işbirlikçi + yazarlık/mahremiyet).
- *Karar kuralı:* yalnızca açıkça tartışılanlar; geçer değinme ("mention") vs. analiz ayrımı not edilir.
  (Bu boyut SSCI karşı-ağırlığı için kritik — boş kalan çalışmalar da bulgudur.)

## C7. Dil-özel boyutlar (çoklu)
- **Hedef beceri:** okuma / yazma / dinleme / konuşma / söz varlığı / dilbilgisi / kültür.
- **Yön:** L1→L2 / L2 / genel.
- **Yeterlik düzeyi:** A1–C2 / belirtilmemiş.
- **Çalışılan dil(ler):** [serbest metin]. *Korpus-gözlemli (25):* İngilizce-EFL/ESL (çoğunluk) · **Çince-CFL · Arapça · Romence-RFL · Almanca-GFL** (çok-dillilik kozu).

## C8. İddia / kanıt türü
- **Tür:** kavramsal / empirik (nicel / nitel / karma) / derleme.
- **İddia edilen etki:** [serbest metin — örn. "iş yükünü azaltır", "özgünlük artar"].
- **Kanıt gücü:** güçlü (kontrollü/yeterli örneklem) / orta / zayıf (anekdot/öz-bildirim) / yok (kavramsal).
- *Karar kuralı:* iddia ile kanıtı AYIR; "iddia edilen ama gösterilmeyen" etkiler ayrıca işaretlenir
  (AS5 boşluk analizi için altın veri).

---

## Sentez eşlemesi (analiz aşamasında)
> ⚠️ **C1b=0 NOTU (kritik, yazımda):** Dahil sette C1b (konuşma-öğretici)=0 olması **ölçüt-gereğidir** (salt konuşma E3/E4 ile dışlandı) → tezin BAĞIMSIZ kanıtı DEĞİL (döngüsel olur). "Konuşma→üretim" kaymasının ampirik kanıtı = **bibliyometrik AS3 (geniş 3.050 tematik evrim)**; sentez C1 dağılımı değil.
- C1+C2 → **"konuşma → üretim" sürekliliği** (AS3/AS4 ana eksen).
- C2+C3 → **üretim merkezinin kayması & öğretmen failliği** (AS5).
- C4+C6 → **kolaylık ↔ geçerlilik / yapısal riskler** gerilimi (tartışma omurgası).
- C5 → öğretmen eğitimi sonuçları (uygulama/öneri bölümü).
- C8 → kanıt-boşluk haritası (gelecek araştırma gündemi).

## Versiyon
- v0.1 (2026-06-19) — tümdengelimli başlangıç.
- **v1.0 (2026-06-21)** — nihai 25-set; hibrit yordam + betimleyici alanlar + korpus kategorileri.
- **v1.1 (2026-06-21)** — Görev-6 kodlamasından tümevarımlı eklemeler: **C1a′** (değerlendirme-üreticisi), **C1c′** (öğrenen-YZ eş-yaratımı), **C1e** (insan-yapılandırmalı pipeline); **C6'ya yazarlık-etiği + aşırı-bağımlılık**; **C1b=0 döngüsellik notu**. Kaynak: `kol2/28-yeni-kod-adaylari.md`.
- **v1.2 (2026-06-24)** — κ pilotu (`kol2/30`) zayıf bulunan **C1/C3/C6** için KARAR KURALI netleştirmesi: **C1** a/c/c′ ayracı (kim üretiyor × yinelemeli mi); **C2** c-vs-d (öğrenci eş-yaratım→d); **C3** 1–5 somut çapa (otonom-sistem son-kullanıcı=1; anket-beyanı=3 tavan; gözlenen vs beyan ayrımı); **C6** risk+pozitif **çift kutup** açık kuralı. 6 anlaşmazlık tam-metinle uzlaştı (`kol2/27` adjudikasyon logu). Üretici kimliği = dağılım etiketi, amaç filtresi değil.
