# Proje Brifi & Devam Dokümanı
## Sohbetten Üretime: Yabancı Dil Öğretiminde Üretken Yapay Zekâ — Bibliyometrik Analiz ve Sistematik Derleme

> Bu doküman yeni bir oturuma taşımak için hazırlanmıştır. Çalışmanın tüm kilitli kararlarını, PRISMA protokolünü, kopyala-yapıştır arama dizgelerini, STORM girişe-yönelik çıktısını, kodlama şemasını ve iş akışını içerir.
> **Yeni pencerede kullanım:** bu dosyayı yükle ve "Bu brifteki Aşama X'ten devam edelim" de. Kaldığımız yerden sürdürürüz.
> **Son durum:** Aşama 1 (RESEARCH) hazırlığı tamamlandı. Bir sonraki somut iş, §4'teki dizgelerin WoS + Scopus'ta çalıştırılıp dışa aktarılmasıdır (bkz. §10, Adım 1 — kurumsal erişim gerektirir).

---

## 0. Tek cümlede proje
Üretken yapay zekânın *danışılan/konuşulan bir araç* olmaktan *üretim/geliştirme aracına* evrilmesinin, yabancı dil öğretiminde materyal üretiminin merkezini ve öğretmenin rolünü nasıl dönüştürdüğünü, PRISMA 2020 temelli bir **bibliyometrik analiz + sistematik derleme** ile ortaya koymak.

## 1. Kilitlenen kararlar
- **Tür:** Bibliyometrik analiz + sistematik derleme (PRISMA 2020). Katılımcı yok; veri = yayımlanmış literatür. (Tartışmaya en kapalı, en yüksek kabul olasılıklı yöntem.)
- **Kapsam:** Yabancı dil eğitimi/öğretimi. *DaF-özel DEĞİL* (korpusu daraltıyor), *disiplinler-üstü DEĞİL* (SSCI yerleşimini zorluyor).
- **Hedef indeks:** SSCI (Türk akademik sisteminde makale başına getirisi en yüksek indeks).
- **Birincil dergi:** Interactive Learning Environments. **Yukarı-oynama yedeği:** Computer Assisted Language Learning. (+ SSCI gönderim merdiveni — §7.)
- **Yöntem omurgası:** PRISMA. **STORM yalnızca girişin kavramsal çerçevesi için** kullanılır, yöntemin yerine değil.
- **Değişmez ilke:** Hiçbir kaynak / atıf / DOI / sayı uydurulmaz. Doğrulanamayan kaynak kullanılmaz.
- **Dil:** İngilizce korpus. **Veri tabanları:** WoS Core Collection + Scopus.

## 2. Başlık (kesinleşen)
- **TR:** *Sohbetten Üretime: Üretken Yapay Zekânın Yabancı Dil Öğretiminde Materyal Üretimini ve Öğretmen Rolünü Dönüştürmesi — Bibliyometrik Analiz ve Sistematik Derleme*
- **EN:** *From Conversation to Creation: Generative AI and the Transformation of Material Production and the Teacher's Role in Foreign Language Education — A Bibliometric and Systematic Review*
- Alternatif EN: *From Dialogue to Development: …*
- **Reddedilen ifadeler:** TR'de "muhatap" (zorlama kalıp); EN'de "fabricator" (İngilizcede "uydurma/tahrif" çağrışımı taşır ve yapay zekâ bağlamında "halüsinasyon" anlamına gelir — kullanılmaz).

## 3. Araştırma soruları
**Bibliyometrik (betimleyici, deterministik):**
- **AS1.** Yabancı dil eğitiminde üretken yapay zekâya ilişkin yayın manzarası (hacim, büyüme, ülke/kurum/kaynak dağılımı) nedir?
- **AS2.** Alanın entelektüel (eş-atıf, bibliyografik eşleşme) ve kavramsal (anahtar-sözcük eş-oluşumu, tematik harita) yapısı nasıldır?
- **AS3.** Tematik odak "konuşma/öğretici araç"tan "materyal üretim/geliştirme aracı"na doğru kayıyor mu? (tematik evrim — tezin empirik sınanması)

**Sentez (sistematik derleme):**
- **AS4.** Üretken yapay zekâ, yabancı dil materyali tasarım/üretiminde hangi rollerle kavramsallaştırılıyor?
- **AS5.** Üretim merkezinin yayıncı/uzmandan dil öğretmenine kaymasına dair kanıt, iddia ve boşluklar; öğretmen rolü/failliği açısından sonuçları nelerdir?

## 4. İki katmanlı arama stratejisi
Yabancı dil × üretim × yapay zekâ kesişimi dar olduğundan, korpus inceliği riskini önlemek için iki katman:
- **Bibliyometrik katman (geniş):** `A AND D` → büyük, sağlam korpus (AS1–AS3).
- **Sentez katmanı (odaklı):** geniş korpus `C` bloğuyla süzülür → 20–60 çalışmalık alt-küme (AS4–AS5).

**Kavram blokları:**

```
A (üretken YZ):
"generative artificial intelligence" OR "generative AI" OR GenAI OR "large language model*"
OR LLM OR ChatGPT OR "GPT*" OR "conversational agent*" OR chatbot* OR "AI assistant*"

D (yabancı dil eğitimi):
"foreign language" OR "second language" OR "language learning" OR "language teaching"
OR "language education" OR "language teacher*" OR CALL OR "computer-assisted language learning"
OR EFL OR ESL OR L2 OR "applied linguistics" OR "language classroom"

C (materyal/üretim):
"instructional design" OR "material* design" OR "materials development" OR "content creation"
OR "content generation" OR courseware OR "learning material*" OR "teaching material*"
OR "educational technolog*" OR "learning object*" OR "application development"
OR "app development" OR "no-code" OR "low-code" OR "tool development"
```

**Çalıştırılacak dizgeler (kopyala-yapıştır):**

WoS Core Collection — geniş katman (Topic):
```
TS=(
("generative artificial intelligence" OR "generative AI" OR GenAI OR "large language model*" OR LLM OR ChatGPT OR "GPT*" OR "conversational agent*" OR chatbot* OR "AI assistant*")
AND
("foreign language" OR "second language" OR "language learning" OR "language teaching" OR "language education" OR "language teacher*" OR CALL OR "computer-assisted language learning" OR EFL OR ESL OR L2 OR "applied linguistics" OR "language classroom")
)
```
WoS — odaklı alt-küme: yukarıdakine `AND (C bloğu)` eklenir.

Scopus — geniş katman:
```
TITLE-ABS-KEY(
("generative artificial intelligence" OR "generative AI" OR GenAI OR "large language model*" OR LLM OR ChatGPT OR "GPT*" OR "conversational agent*" OR chatbot* OR "AI assistant*")
AND
("foreign language" OR "second language" OR "language learning" OR "language teaching" OR "language education" OR "language teacher*" OR CALL OR "computer-assisted language learning" OR EFL OR ESL OR L2 OR "applied linguistics" OR "language classroom")
)
```
Scopus — odaklı alt-küme: yukarıdakine `AND (C bloğu)` eklenir.

**Kalibrasyon notları:** Geniş katman <300 kayıt verirse `C` aramadan çıkarılıp yalnızca kodlama aşamasında uygulanır. `GPT*` aşırı gürültü yaparsa `"GPT-4*" OR "GPT-3*"` ile daraltılır. `L2` ve `CALL` gürültüsü kontrol edilmeli (alan-dışı eşleşmeler için başlık-özet taramasında gözden geçir).

## 5. Dahil etme / dışlama ölçütleri
**Dahil:** yabancı/ikinci dil eğitiminde üretken yapay zekâyı ele alan kayıtlar; Ocak 2018 – arama tarihi; İngilizce; hakemli ve indeksli. *Sentez alt-kümesi için ayrıca:* materyal/içerik/araç tasarımını veya üretimini konu edinmiş olmak.
**Belge türü:** bibliyometrik korpus = makale + derleme + bildiri; sentez alt-kümesi = dergi makalesi + derleme.
**Dışla:** dil eğitimi dışı YZ çalışmaları; editöryel/mektup/not/errata (sentezde); tam metni erişilemeyen kayıtlar (sentezde); çapraz tekrarlar.
**Zaman penceresi gerekçesi:** 2018 başlangıcı, ChatGPT öncesi "konuşma temelli araç" temel hattını yakalar; tematik evrim 2022 sonu kırılmasını bracketleyen dilimlerle (2018–2021 / 2022–2023 / 2024–) çözümlenir — kaymayı görünür kılan analitik araç budur.

## 6. PRISMA iş akışı + analiz planı
**Eleme (PRISMA 2020):** Identification (WoS + Scopus, çapraz tekilleştirme) → Screening (başlık-özet) → Eligibility (tam metin) → Included (bibliyometrik korpus + sentez alt-kümesi). İki bağımsız tarayıcı; uyuşmazlık **κ** ile raporlanır, anlaşmazlık üçüncü hakemle çözülür. PRISMA akış şeması n'leri arama sonrası doldurulur.

**Bibliyometrik analiz (AS1–AS3):** performans analizi (yıllık üretim, atıf, üretken yazar/kurum/ülke/kaynak; Bradford/Lotka opsiyonel) + bilim haritalama (eş-atıf, bibliyografik eşleşme, anahtar-sözcük eş-oluşumu, Callon merkezilik/yoğunluk tematik haritası, zaman dilimli tematik evrim). **Araçlar:** Bibliometrix/biblioshiny (R) + VOSviewer. Tarih damgalı export'larla yeniden üretilebilir.

**Sentez (AS4–AS5):** §8'deki tümdengelimli kodlama şeması + tümevarımlı düzeltme; nitel içerik analizi; bulguların "konuşma → üretim" sürekliliğine eşlenmesi.

**Raporlama:** PRISMA 2020 (27 madde). Ön-kayıt opsiyonel (OSF). AI-destek beyanı manuscript'e eklenir.

## 7. SSCI dergi merdiveni
**Doğrulanmış:**
- **Computer Assisted Language Learning** (T&F) — SSCI, JCR Q1; kapsam birebir (courseware tasarım/geliştirme, müfredata entegrasyon, öğretmen eğitimi, yeni teknolojiler). *Rekabetçi → yukarı-oynama yedeği.*
- **Interactive Learning Environments** (T&F) — SSCI; derleme yayımlıyor; daha erişilebilir. *→ Birincil hedef.*
- **Education and Information Technologies** (Springer) — SSCI Q1 ama **derleme türü kabul ETMİYOR** → merdiven dışı.

**Yeni oturumda ilk iş (teyit edilecek):** ILE'nin güncel çeyrekliği + derleme kabul politikası; ayrıca System, ReCALL, Journal of Computer Assisted Learning için indeks + güncel çeyreklik + derleme politikası. (Çeyreklik/politika ezberden YAZILMAZ; JCR/Scopus + dergi sayfasından teyit edilir.)

## 8. STORM çok-bakışlı tur → giriş çerçevesi + kodlama şeması
Tez altı uzman perspektifinden sorgulandı (STORM mantığı: tek bakış değil, çok bakış):

1. **Dil öğretmeni-uygulayıcı:** Üretebilmek, müfredata uygun ve düzeye uygun (CEFR, L1 etkisi) *kullanılabilir* materyal demek mi? → Üretim kapasitesi ≠ pedagojik geçerlilik; "son kilometre" uyarlama ve iş yükü sorunu.
2. **Öğretim tasarımcısı:** Öğretmen yazılım nitelikli ürün üretebiliyorsa, uzmanlık alanı olarak öğretim tasarımına ve tasarım kalitesine (hedef hizalama, erişilebilirlik) ne olur? → Tasarımcı rolünün aracısızlaşması; "tasarım borcu" (cilalı ama pedagojik temeli zayıf ürün) riski.
3. **Eleştirel eğitim-teknolojisi araştırmacısı:** "Öğretmen-üretici" anlatısı kimin işine yarıyor, neyi gizliyor? → Emek yoğunlaşması, platform bağımlılığı, veri/mahremiyet, ücretsiz emek; çözümcülük (solutionism) eleştirisi. *SSCI inandırıcılığı için zorunlu karşı-ağırlık.*
4. **Yayıncı/endüstri ekonomisti:** Kim kazanıyor; değer nereye kayıyor? → Değer içerikten (yayıncı) altyapıya (YZ platform sağlayıcısı) göçüyor olabilir; *üretim demokratikleşiyor ama değer yakalama demokratikleşmeyebilir.*
5. **Öğretmen eğitimcisi:** Hangi yeni yeterlikler gerekiyor (YZ okuryazarlığı, prompt/tasarım okuryazarlığı, çıktı değerlendirme, etik)? → Öğretmen mesleki bilgisinin yeniden kavramsallaştırılması ("YZ-çağı TPACK"); öğretmen failliği/kimliği — *SSCI'nin değer verdiği kuram bağlantısı.*
6. **Eğitim-teknolojisi tarihçisi:** Hangi geçmiş döngüye benziyor (dil laboratuvarları, CALL dalgaları, akıllı tahtalar, MOOC'lar, Web 2.0 "öğretmen içerik üreticisi")? → "Devrim" söylemi tekrar ediyor; üretim aracının demokratikleşmesini (masaüstü yayıncılık, Web 2.0) eşitsiz benimseme ve nitelik değişkenliği izledi. *Teknolojik-determinizmden korur.*

**(a) Girişin kavramsal mimarisi (atıf yuvaları aramadan sonra doldurulacak):**
1. Yabancı dil eğitiminde öğretmen-yapımı materyal yeni değildir; ancak üretim tarihsel olarak bir **üretim tavanıyla** (beceri, zaman, araç) sınırlıydı ve yüksek-nitelikli, yazılım düzeyindeki kaynakların üreticisi konumunda yayıncılar/uzmanlar vardı.
2. Üretken yapay zekânın *konuşma aracından üretim/geliştirme motoruna* evrimi bu tavanı çökertir ve öğretmeni materyal *tüketicisinden/uyarlayıcısından* potansiyel materyal *üreticisine/geliştiricisine* taşır.
3. Bu, topyekûn bir "devrim" değil, **üretim merkezinin kayması**dır; ve bir dizi çözülmemiş soruyu (üretim kolaylığı ↔ pedagojik geçerlilik; öğretim tasarımı uzmanlığının geleceği; değerin platformlara göçü; yeni öğretmen yeterlikleri; eşitsizlik) gündeme getirir.
4. Mevcut GAI-eğitim sentezleri evrimi "araç → öğrenen-merkezli" okuyor; **üretim/öğretmen-rolü** boyutu eksik kalıyor — bu derlemenin gerekçesi budur.

**(b) Tümdengelimli kodlama şeması (sentez katmanı; başlangıç, tümevarımlı düzeltilecek):**
- **C1. YZ rolü:** içerik üreticisi / konuşma-öğretici (muhatap) / eş-tasarımcı-yardımcı / özerk üretici-geliştirici (uygulama, site, courseware).
- **C2. Üretim merkezi:** yayıncı-uzman → öğretmen-üretici → öğrenen-üretici; aracısızlaşma derecesi.
- **C3. Öğretmen rolü & failliği:** tüketici/uyarlayıcı ↔ tasarımcı/geliştirici; mesleki kimlik; vasıfsızlaşma ↔ yeniden vasıflanma.
- **C4. Pedagojik geçerlilik & kalite güvencesi:** hedef/CEFR hizalama; erişilebilirlik; hata/halüsinasyon; değerlendirme pratikleri.
- **C5. Yeterlikler & öğretmen eğitimi:** YZ okuryazarlığı, prompt/tasarım okuryazarlığı, çıktı değerlendirme, etik.
- **C6. Eleştirel/yapısal boyutlar:** emek yoğunlaşması, platform bağımlılığı, veri/mahremiyet, eşitsizlik/dijital uçurum, değer yakalama.
- **C7. Dil-özel boyutlar:** hedef beceri (okuma/yazma/dinleme/konuşma), L1/L2, yeterlik düzeyi, çalışılan dil(ler).
- **C8. İddia/kanıt türü:** kavramsal/empirik; iddia edilen etki; kanıt gücü.

> Not: STORM'un birincil işlevi **giriş çerçevesidir** (senin belirttiğin gibi). Kodlama şemasının zenginleşmesi bu turun ikincil bir kazanımıdır; sentez tasarımını bağlamaz, yalnızca güçlendirir.

## 9. İş akışı (academic-pipeline omurgası, checkpoint'li)
| Aşama | Skill / mod | Çıktı | Checkpoint |
|---|---|---|---|
| 1 RESEARCH | deep-research → `systematic-review` modu | Protokol, korpus, bibliyometri, sentez | tam onay |
| 2 WRITE | academic-paper (`full`, lit-review yapısı, APA 7.0) + writing-anti-ai | Taslak | onay |
| 2.5 INTEGRITY | bütünlük doğrulaması (%100 referans + DOI) | Doğrulama raporu | zorunlu |
| 3 / 3′ REVIEW | academic-paper-reviewer (5 hakem + Devil's Advocate; sonra doğrulama) | Hakem raporları + revizyon yol haritası | zorunlu |
| 4 / 4′ REVISE | academic-paper (`revision`) | Revize taslak | onay |
| 4.5 FINAL INTEGRITY | bütünlük doğrulaması (son) | %100 doğrulama | zorunlu |
| 5 FINALIZE | academic-paper (`format-convert`) | APA 7.0; MD + DOCX (+ PDF) | zorunlu |

## 10. Sıradaki somut adımlar (öncelik sırası)
1. **(Senin kurumsal erişiminle) §4 dizgelerini WoS Core Collection + Scopus'ta çalıştır, sonuçları dışa aktar** — tam kayıt + atıf bilgisi (CSV / RIS / BibTeX). *Önemli: WoS ve Scopus kurumsal oturum/erişim ardındadır; bu veri tabanlarına ben giriş yapamıyorum, bu yüzden arama ve export adımı sende. Dizgeleri tam da bu nedenle kopyala-yapıştır hazır bıraktım.*
2. **Dergi merdiveni teyidi** (§7) — ILE + 3-4 SSCI yedeğinin güncel çeyrekliği ve derleme kabul politikası.
3. **Export geldiğinde:** çapraz tekilleştirme → PRISMA eleme (κ) → bibliyometrik analiz (Bibliometrix/VOSviewer) → sentez kodlaması (§8b).
4. **Yazım:** §8a çerçevesiyle giriş + yöntem + bulgular taslağı (academic-paper, APA 7.0).
5. **Kapanış:** bütünlük doğrulaması → iki aşamalı hakem → revizyon → sonlandırma.

---

### Çalışma notları / hatırlatmalar
- Bibliyometri ve sistematik derleme genel "GAI-eğitim" alanında doygun; **ayırt edici açı** ("sohbet → üretim", yabancı dil odağı) öne çıkarılmazsa "bir bibliyometri daha" riski var.
- Korpus inceliği en büyük teknik risk; iki katmanlı arama (§4) bunu yönetmek içindir.
- Hiçbir aşamada atıf/sayı/künye uydurulmaz; doğrulanamayan kaynak rapora girmez.
- Çeyreklik ve indeks bilgileri her zaman JCR/Scopus + dergi sayfasından teyit edilerek yazılır.
