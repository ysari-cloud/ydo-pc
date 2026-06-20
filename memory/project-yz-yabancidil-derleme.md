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

### 🆕 2026-06-20 ÇÖZÜMLER (arama denetimi turu)
- **Q2 TEKRARLANABİLİRLİK = ÇÖZÜLDÜ.** Dünkü "yazılı dizge 7.217 ≠ korpus 1.932" tutarsızlığı PROJE
  KUSURU DEĞİL, eksik-okumaydı: korpus **kalibre as-run dizgeyle** kuruldu (GPT sürüm-spesifik
  `GPT-3*/4*/5*`, çıplak CALL/L2 ÇIKARILDI, Scopus GPT JOKERSIZ). Bu dizgeler cowork yerel
  `PROJECT_STATE.md`'deydi (REPODA DEĞİLDİ=risk) → **kalıcılaştırıldı:**
  `araclar/ARAMA-DIZGELERI-FINAL-as-run.md` (makale-hazır, kanonik) + brief §4'e pointer. **Metot'ta
  AS-RUN dizge raporlanır, niyet-edilen §4 değil; kalibrasyon=PRESS iyi pratiği, GÜÇ.** Yeniden analiz YOK.
- **KEYWORD AÇIĞI (PRESS):** komşu 2 SLR (Deng & Jamaludin 2026 `10.1177/21582440261418315`; Griche &
  Bennis 2026 `10.29140/tltl.2026.102827`) A bloğumuzda adlandırılmış araç (Gemini/Copilot/ERNIE/DALL-E…)
  olmadığını gösterdi. Cowork delta: 152 ham → ~12 kesin ilgili (Gemini×5,Copilot×3…2024-25 = gerçek açık,
  güncellik değil). AMA cowork delta'sı B'de çıplak L2/CALL kullandı (as-run'da yok)→gürültü şişti
  (LLAMA=dil-yatkınlık testi). **TEMİZ TEKRAR talimatı: `araclar/COWORK-GOREV-3-temiz-delta.md`**
  (artırılmış-A AND **as-run B** NOT as-run-A). **KARAR Q1=(a) other-methods:** temiz-ilgili kayıtlar
  PRISMA "diğer yöntemlerle bulunan" yolundan → ~50 sentez seti; bibliyometrik 3.050 DONUK kalır
  (rebuild YOK — 12/3050 marjinal). Artefaktlar: `20-arama-denetimi-keyword-audit.md`,
  `21-komsu-calismalar-2026-landscape.md` (2026 rakipler — "bibliyometrik" tek başına artık ayırt edici
  değil; ayrışma=materyal-üretimi+çok-dilli+GenAI-özgül). **İLKE (kullanıcıyla netleşti): esas =
  tekrarlanabilir sorgu (A), "tüm literatüre hâkimiyet" DEĞİL; başıboş makale kovalama YOK, tek yapısal
  kontrol yapılır, kilitlenir.** **BEKLEYEN:** cowork temiz-delta → ben denetler → ~50 netleşir → arama KAPANIR.

### ⏩ ŞU AN NEREDEYİZ (2026-06-20, son durum)
**Aşama: 47 dahil makalenin TAM METNİNİ toplama — OA indirme TURU yapıldı.**
- Erişim haritası: `19-tam-metin-erisim-listesi.md` → ~29 OA (linkli) + **18 kapalı** (vetis).
- Araçlar (`araclar/`): `pdf_indir.sh`, `zotero_doi_listesi.txt`, `COWORK-GOREV.md`, **`_INDIRME_RAPORU.md`** (commit `1d9f9ac`).
- **Zotero kullanıcı PC'sinde KURULU** (giriş: emre_sari). Connector + masaüstü tamam.
- **PDF'ler YALNIZ YEREL/sandbox'ta** (`pdf/` → `.gitignore`'da). Buluta PDF YÜKLENMEZ.
- **✅ OA İNDİRME RAPORU GELDİ (`_INDIRME_RAPORU.md`):** sandbox'tan **14/29 OA indi+doğrulandı**
  (her dosya `%PDF` + pypdf sayfa kontrolü; 08,11,12,16,17,25,26,32,34,37,39,44,47,54 — ~11MB,
  ⚠️ bu PDF'ler sandbox'ta kaldı, kullanıcı PC'sinde DEĞİL). **15/29 OA inmedi** = bu bulut IP'si
  yayıncı bot-duvarında (ScienceDirect/MDPI/Wiley/T&F 403, ResearchGate giriş, 22/41/43 host
  erişim) → **gerçek OA, kullanıcı kendi ağı+Connector ile saniyede indirir** (öncelik kolaylar:
  03,07,14,22,38,41,43,46,48,50,51). **18 kapalı** dokunulmadı (vetis): 1,2,4,5,6,9,15,18,20,21,
  27,29,30,31,40,45,52,53 (#21 ERIC EJ1457846=404, #4 ERIC tam-metin yok → ikisi de vetis).
- **BEKLEYEN:** (a) kullanıcı 15 OA'yı kendi ağından + 18 kapalıyı vetis/Connector ile indirir;
  (b) **insan tarama formu** (`tam-metin-tarama-FORMU.xlsx`, `15b`'ye kör) tam metinden doldurulur;
  (c) Gemini screener-3 (`16-...PROMPT.md`) çalıştırılır → çıktı bana → ben **Fleiss+çiftli Cohen κ +
  nihai N**; (d) v3'teki `[κ]`/`[N]` dolar; (e) tam metinlerden **C1–C8 kodlama + "included studies"
  tablosu**; (f) ops: `raw_data` push → tam özetler (xlsx özetleri 300 krktr kırpık, kaynak tam).

### Kalıcı kararlar
- **🟩 YÖNTEMSEL KARAR SABİT (kullanıcı yönergesi, 2026-06-19): "Hakemde sorun çıkarmayacak,
  en savunulabilir yoldan git."** → **Klasik ikili tarama:** Screener-1 = İNSAN (otorite, tam-metin),
  Screener-2 = TEK YZ (Claude, `15b` mühürlü), birbirine kör. **Raporlanan güvenilirlik = bu ikisi
  arası Cohen κ.** Gemini (`16b`) + Manus (`16c`) + derin-arama (`18`) yalnızca **Ek'te robustluk/
  şeffaflık** — multi-LLM ANA YÖNTEM diye SUNULMAZ (risk orada). **Nihai N = insan kararları**;
  YZ paneli N=48 yalnız öneri girdisi. Bunu bir daha kullanıcıya SORMA, bu çizgide ilerle.
- **Sınır vakalar çözüldü (`18`):** 10 tartışmalı kayıt derin-arama + #13 için tam-metin ile karara
  bağlandı → **provizyonel N=47** (DAHİL +4: 4,25,29,46 · DIŞLA +6: 13,19,24,35,36,56).
  **#13 Lin TAM METİNLE EXCLUDE** (RQ'lar öğrenci-odaklı, öğrenen-kutbu; 19/35 ile tutarlı). Belirsiz
  kayıt KALMADI. DIŞLA(9) = {13,19,24,33,35,36,49,55,56}. κ-paradoksu: INCLUDE yaygınlığı yüksek →
  ham anlaşma + κ birlikte raporla. Nihai N hâlâ insan tarama formuna bağlı (otorite insan).
- **🟦 META-ANALİZ KARARI (kullanıcı, 2026-06-19): AYRI 2. MAKALE** (aynı korpustan), bu makaleye
  EKLENMEZ. Makale 1 = bibliyometri + sistematik derleme (nitel sentez), odaklı kalır; meta-analiz
  Makale 1 gönderilince başlar. Plan: `17-makale2-meta-analiz-plani.md` (feasibility kapısı: geniş
  korpusta aynı-sonuç + kontrol grubu + çıkarılabilir efekt-size ≥~10 çalışma kümesi VAR MI? — teyit
  edilmedi). **NOT: meta-analiz metadatadan çıkmaz; empirik alt-küme tam metinlerinden istatistik ister.**
  Bu makalenin türü sabit: *"A bibliometric analysis and systematic review"* (meta-analiz DEĞİL).
- **🟡 κ/N TARAMASI KURULDU (cloud, 2026-06-19) — kullanıcı kararı: YZ ikinci tarayıcı (ben)+beyan.**
  56 kaydı bağımsız (özet-temelli, cowork ön-kodlamasına kör) taradım. 3 artefakt üretildi:
  - `15-tam-metin-tarama-protokolu.md` — ortak karar kuralı + κ planı + **kapsam varyantı kararı (§3:
    A kapsayıcı [önerilen] vs B katı)** + YZ-beyan taslağı + asimetri sınırlama notu.
  - `15b-screener2-AI-muhurlu-kararlar.md` — benim MÜHÜRLÜ kararlarım (bağımsızlık kanıtı, git damgalı).
    **INC_kapsayıcı(A)=53/56** (dışla 33,49,55) · **INC_katı(B)=48/56** (dışla 31,33,36,41,42,45,49,55).
    Kesin dışlama her iki varyant: #49 programlama-dili (konu-dışı), #55 genel-eğitim ajan-metodoloji,
    #33 genel-eğitim tutum (dil-özgü değil). Konuşma-kutbu (31,41,42,45) + puanlama (36) = varyanta bağlı.
  - `tam-metin-tarama-FORMU.xlsx` — kullanıcının dolduracağı boş form (KÖR: 15b'ye bakmadan).
  - **KARARLAR (kullanıcı):** kapsam = **A (kapsayıcı)** ✔ · **3 değerlendirici** ✔ (insan tam-metin +
    Claude özet-mühürlü + **Gemini** özet). Gemini istemi: `16-gemini-screener3-PROMPT.md` (kör, A, 56 özet).
    HTML pano üretildi: `sentez-tarama-PANO.html` (kullanıcıya gönderildi).
  - **κ planı (güncel):** Fleiss κ (3 değerlendirici) + çiftli Cohen κ (İnsan–Claude, İnsan–Gemini,
    Claude–Gemini). Uzlaşı=2/3 çoğunluk; azınlık/anlaşmazlık → insan tam-metin adjudikasyonu → nihai N.
  - **SIRADA (kullanıcı):** (1) FORMU tam metinden doldur (15b'ye kör) · (2) Gemini'ye `16`'yı yapıştır,
    çıktıyı bana ver → ben Fleiss+çiftli κ + anlaşmazlık listesi + **nihai N** hesaplarım → v3 [N]/[κ] dolar.
- **✅ KIYAS YAPILDI: v2 (doğrudan) vs skill → `13-kiyas-raporu-v2-vs-skill.md`.**
  `Makale_Taslak_skill.docx` (commit 67ae855) geldi, bağımsız doğrulandı (12 atıf, 15 [CITE:],
  κ/N yer tutucu, temiz AS3, kirli %38 yok). Hüküm:
  - **En iyi YAZIM = skill** (4-move giriş, tam Tartışma 5.1–5.4 + Sonuç, anti-ai prozası).
  - **En iyi VERİ ARTEFAKTI = v2** (4 tablo + 5 figür/VOSviewer; skill'de figür YOK → tek başına gönderilemez).
  - **ÖNERİ: Hibrit v3** = skill iskelet/proza + v2 figür/tablo/Appendix C-D. Karar kullanıcıda.
  - Sonra: insan tam-metin (56) → κ+N → Sentez (RQ4-5) → v3 tamam.
- **✅ TASLAK v2 GELDİ + DENETLENDİ → GEÇER (cloud, 2026-06-19) → `12-cloud-denetim-taslak-v2.md`.**
  `Makale_Taslak_v2.docx` (commit 2a6cebd). Cowork 09/10 engelleyici düzeltmeleri uyguladı:
  - **AS3 DÜRÜST düzeltildi:** konuşma %58,3→%35,0→%14,3 (sağlam düşüş); üretim emergent (2→7→51,
    oran 0,05→0,13, GEÇMEDİ). Yapay "%38" manşeti kaldırıldı (cloud endişesi 09 DOĞRULANDI).
    Duyarlılık paragrafı + Appendix C sözlükler + dürüst "qualified support" çerçeve. Örnek bütünlük.
  - **Atıf bütünlüğü: 12/12 web'den DOĞRULANDI** (Law, Zhai, Huang, Kohnke, Jeon×2, Ji, Davar +
    4 metodolojik). APA tam yazar düzeltmeleri uygulanmış. PRISMA 27-madde checklist (Appendix D) eklendi.
  - κ/nihai N hâlâ yer tutucu (uydurulmamış). Dergi çeyreklik teyitli (01).
- **Kalan (ENGELLEYİCİ DEĞİL, insan işi):** (1) 56-set tam-metin + 2.tarayıcı → **κ + nihai N** ·
  (2) cowork: sentez bulguları (RQ4-5) → v3 · (3) opsiyonel skill-kıyas (`11`, baz=v2).
- **Skill-kıyas hazır:** `11-cowork-skill-yazim-yonergesi.md` (v2'ye göre güncel) — kullanıcı yeni
  cowork penceresinde çalıştıracak; ben sonra v2 vs skill kıyaslarım.
- **✅ WRITE GELDİ + DENETLENDİ (cloud, 2026-06-19) → `10-cloud-denetim-taslak-v1.md`.**
  `Makale_Taslak_v1.docx` (commit 49e40a2, 69 paragraf): Abstract+Giriş(4-move)+Yöntem+Bulgular-
  Bibliyometri+ön-Sentez+Tartışma iskeleti+12 kaynak. Atıf bütünlüğü GEÇER (Law 2024, Zhai&Wibowo
  2023 web'den doğrulandı; 4 metodolojik standart). κ/N/klasik atıflar yer tutucu (uydurma yok).
  - **🔴 ENGELLEYİCİ: AS3 düzeltmesi (09) UYGULANMAMIŞ** — taslak hâlâ kirli sayılarda (üretim
    %5,6→%38,0, para 46/5/52). Cowork CONV/PROD_LEX temizleyip **AS3 re-run** etmeli, sonra Abstract/
    §3.3/§4 sayılarını güncellemeli. Re-run CowORK'te (ham veri repoda yok). Kayma yönü muhtemelen
    korunur (SliceKeywords bağımsız destekliyor) ama değerler değişecek → bu hâliyle revize'ye gitmez.
  - Küçük: APA "Davar et al." girişi düzelt; PRISMA 27-madde checklist ekle; kalan korpus DOI'leri teyit.
- **Sıra:** (cowork) AS3 re-run+taslak güncelle+APA/checklist · (kullanıcı) 56-set tam-metin+2.tarayıcı→
  κ/N→sentez · (cloud) kalan DOI doğrula, v2'de tam bütünlük+PRISMA-27 denetimi. Token REVOKE.
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
