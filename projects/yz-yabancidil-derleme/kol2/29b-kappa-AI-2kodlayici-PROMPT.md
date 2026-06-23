# 29b — κ için 2. KODLAYICI (YZ aracı) PROMPT'u

> Kullanım: Bu metni FARKLI bir YZ aracına (Gemini/GPT — Claude DEĞİL, bağımsızlık için) yapıştır,
> ardından 6 makalenin TAM METNİNİ (PDF/yapıştır) ver. Çıktıyı cloud'a getir → κ hesaplanır.

---

ROL: Sistematik bir derlemede **kodlayıcılar-arası güvenilirlik (κ)** kontrolünde **BAĞIMSIZ İKİNCİ KODLAYICISIN.** Sana 6 makalenin tam metnini vereceğim. Her makaleyi aşağıdaki kod kitabıyla **C1–C8** boyutlarında kodla. **Bağımsız ol**, başka bir kaynağa/önceki kodlamaya bakma; her kodu makalenin **tam metnine** dayandır ve her hücre için **kısa kanıt cümlesi/sayfa** ver.

BAĞLAM (kapsam): Yabancı/ikinci dil eğitiminde **üretken yapay zekâ (GenAI) ile materyal/içerik/araç ÜRETİMİ.**

BETİMLEYİCİ ALANLAR (her makale için ayrıca yaz): **Araç** (ChatGPT/Gemini/Copilot/Claude/DALL-E/LLM…) · **Üretici** (öğretmen/öğrenci/aday öğretmen/eş-üretim) · **Artefakt türü** · **Dil**.

KOD KİTABI:
- **C1 — YZ'nin rolü:** C1a içerik-üretici · C1a′ değerlendirme/sınav-üreticisi · C1b konuşma-öğretici(muhatap) · C1c eş-tasarımcı/yardımcı(öğretmen-yanlı) · C1c′ öğrenen–YZ eş-yaratımı · C1d özerk üretici-geliştirici(yazılım düzeyi) · C1e insan-yapılandırmalı üretken pipeline/sistem. *(baskın işlev; gerekirse çoklu)*
- **C2 — Üretim merkezi:** C2a yayıncı/uzman · C2b öğretmen-üretici · C2b⁺ aday öğretmen · C2c öğrenen-üretici · C2d insan-YZ eş-üretimi. *(+ aracısızlaşma: düşük/orta/yüksek)*
- **C3 — Öğretmen rolü & failliği:** 1–5 ölçek (1=salt tüketici … 5=tasarımcı/geliştirici) + kimlik çerçevesi (güçlenme/dönüşüm/tehdit) + vasıf yönü (vasıfsızlaşma/yeniden-vasıflanma/karışık).
- **C4 — Pedagojik geçerlilik & kalite:** hizalama/CEFR/müfredat · erişilebilirlik · halüsinasyon/doğruluk · doğrulama pratiği (uzman-denetim/pilot/yok). Her alt-madde: var/kısmi/yok.
- **C5 — Yeterlik & öğretmen eğitimi:** AI okuryazarlığı / prompt-tasarım okuryazarlığı / çıktı değerlendirme / etik (çoklu) + kuram (TPACK vb.).
- **C6 — Eleştirel/yapısal:** emek yoğunlaşması / platform bağımlılığı / veri-mahremiyet / eşitsizlik-dijital uçurum / değer yakalama / çözümcülük / **yazarlık-özgünlük etiği** / **aşırı-bağımlılık-vasıfsızlaşma** (çoklu; yalnız açıkça tartışılanlar).
- **C7 — Dil-özel:** hedef beceri (okuma/yazma/dinleme/konuşma/söz varlığı/dilbilgisi/kültür) · yön (L2/L1→L2/genel) · düzey (A1–C2/belirsiz) · çalışılan dil.
- **C8 — İddia/kanıt:** tür (kavramsal/nicel/nitel/karma/derleme) · iddia edilen etki (serbest) · kanıt gücü (güçlü=kontrollü/yeterli örneklem · orta · zayıf=anekdot/öz-bildirim · yok).

KODLAMA KURALLARI: En uygun kategoriyi seç. C5/C6/C7 çoklu olabilir. Hiçbir kategori **oturmuyorsa zorlama** → "**YENİ KOD ADAYI:** …" diye yaz + kanıt. Her hücreye **kısa kanıt** (alıntı/sayfa).

ÇIKTI BİÇİMİ: Markdown tablo — her satır bir makale; sütunlar:
`Makale | Araç | Üretici | Artefakt | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | Kanıt(kısa)`
Tablodan sonra (varsa) "Yeni kod adayları" listesi.

KODLANACAK 6 MAKALE (tam metinlerini aşağıda/ekte veriyorum):
1. Lin (2025) — *Computer Assisted Language Learning*
2. Lin (2025) — *Computers and Composition* (öğrenci çok-kipli kompozisyon)
3. Risang Baskara (2024) — *Language Teaching Research Quarterly* (öğrenci podcast)
4. Bao (2026) — *Interactive Learning Environments* (RAG/çok-ajan içerik üretimi)
5. Zaiarna (2024) — *Information Technologies and Learning Tools* (değerlendirme görevleri)
6. Guo (2026) — *Innovation in Language Learning and Teaching* (Almanca yaratıcı yazma, kontrollü deney)

[BURAYA 6 MAKALENİN TAM METNİNİ YAPIŞTIR veya PDF olarak EKLE.]
