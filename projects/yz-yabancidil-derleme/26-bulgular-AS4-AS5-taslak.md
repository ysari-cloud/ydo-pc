# 26 — Findings: Synthesis (RQ4–RQ5) · full-text draft prose (Görev-9)

> **Çıktı türü:** Bulgular (sentez) düzyazısı, AS4–AS5. Cowork üretimi (Görev-9); cloud denetledi + işledi.
> **Kaynaklar (birebir):** iskelet `25-sentez-iskelet-AS4-AS5`; kodlama `kol2/27-kodlama-tablosu` (v1.2 + Görev-8, **KİLİTLİ, N = 25**); kod tanımları `04-kodlama-kitabi`; İz teyitleri `kol2/33`.
> **Dil/üslup:** `Makale_Taslak_v3.docx` ile aynı (English; hedef dergi *Interactive Learning Environments*, SSCI). Bu metin v3'teki **"4. Preliminary Synthesis"** (özet-temelli, priority-40) bölümünün **yerine** geçecek tam-metin, kilitli-kodlama sürümüdür. **AS4 = RQ4, AS5 = RQ5.**
> **İlke:** her sayı / makale ID / İz alıntısı `kol2/27` + iskeletten birebir; uydurma yok. Yazar-yıl etiketleri `kol2/27` "Yazar-Yıl" sütunundan; tam DOI/atıf bütünlüğü AYRI görevdir (bkz. §Açık noktalar). Bu görev yalnız AS4–AS5 bulgular düzyazısıdır; Giriş/Yöntem/Tartışma ayrı görevlerdir.

---

## 4. Findings: Synthesis (RQ4–RQ5)

The qualitative synthesis draws on the 25 studies that met all three eligibility criteria — primary empirical work, generative AI, and the production of a language-teaching or language-learning artefact — and survived full-text screening (Kol-1 main set 22 plus Kol-2 keyword set 3). Coding applied the locked C1–C8 scheme (Appendix B), with the AI-role, teacher-agency, and critical dimensions (C1, C3, C6) reconciled against full text in the Task-8 adjudication; the reported distributions are the post-adjudication, locked values. Findings are organized by research question: RQ4 reads the corpus through the AI-role dimension (C1), and RQ5 through the center-of-production and teacher-agency dimensions (C2, C3), with the critical (C6) and evidence (C8) dimensions used to separate what the field claims from what it demonstrates.

### 4.1 How generative AI is conceptualized in material production (RQ4)

Read through the AI-role dimension (C1), the 25 studies distribute across six of the scheme's role types: iterative co-designer (C1c, n = 11); learner–AI co-creation (C1c′, n = 5); one-shot content generator (C1a, n = 5); human-configured generation pipeline or system (C1e, n = 2); assessment-item generator (C1a′, n = 1); and autonomous producer-developer (C1d, n = 1). One role type — the conversational tutor (C1b) — is empty, for reasons set out in the caveat that closes this section.

**Theme 1. The dominant conceptualization is the iterative co-designer, not the one-shot generator.** The most common role is the teacher-side iterative co-designer (C1c), coded in 11 of 25 studies (#1, #3, #5, #6, #7, #14, #23, #28, #30, #37, #C04). Adding the learner-side co-creation variant (C1c′, n = 5: #13, #19, #35, #40, #A06) places 16 of 25 studies in a co-creative register, in which the artefact emerges through repeated human–AI exchange rather than a single prompt; pure one-shot generation (C1a) accounts for only 5. The defining mechanism is a loop of prompting, inspecting, and revising. In Lenko-Szymanska (2026; #7), "students refined it in subsequent iterations to increase its precision" when an initial prompt underspecified the task (p. 7); Lin (2025; #6) likewise describes a workflow that turns on the need to "refine/adjust prompts iteratively." Production with GenAI, in this corpus, is a supervised design process rather than an act of automation: the human stays in the loop as the agent who specifies, judges, and re-specifies.

**Theme 2. Teacher-side and learner-side co-creation are distinct, and the learner-side raises authorship.** Within the co-creative register, the corpus separates a teacher-led majority (C1c, n = 11) from a smaller learner-led strand (C1c′, n = 5: #13, #19, #35, #40, #A06) in which the producing agent is the student rather than the teacher. In Risang Baskara (2024; #19), the artefact is built by learners — "students produce EFL podcasts (script→ideas→editing)" — relocating the production act itself. This learner-as-producer configuration is precisely where questions of authorship and ownership begin to surface, a tension carried forward to RQ5 (Theme 4).

**Theme 3. The upper bound — human-configured pipelines and autonomous development — exists but is rare.** At the most automated end, two studies conceptualize GenAI as a human-configured generation pipeline or system (C1e: #8, #29) and one as an autonomous producer-developer (C1d: #17). Bao (2026; #29) reports that "we designed and implemented the CCGF," a retrieval-augmented, multi-agent generation framework, while Park (2026; #8) builds an "automated pipeline" coupled to a validation step. Software-level, system-scale production is therefore demonstrably possible, but it is uncommon — 3 of 25 studies — and in every case it is bounded by human configuration rather than genuine autonomy. As Theme 2 of RQ5 shows, this same scaling can lower, not raise, the teacher's agency.

**Theme 4. The lower bound — assessment generation and pure content generation.** One study conceptualizes GenAI specifically as an assessment-item generator (C1a′: #34), generating evaluation tasks filtered for accuracy, a role distinct from the five pure content-generator cases (C1a: #2, #4, #18, #20, #C02). The latter are illustrated by Nguyen (2026; #20), in which "ChatGPT develops extensive reading materials." What varies here is not only the role but the artefact type: assessment is a thin but present slice of the production landscape.

**Theme 5. The production turn spans languages and modalities.** The 25 studies address at least four target languages beyond the EFL majority — Chinese as a foreign language (#6), Arabic (#5, #17), Romanian as a foreign language (#28), and German as a foreign language (#35) — and both textual and visual artefacts. Visual production is represented by image-generation tools, as in Temiz (2025; #C02), where "DALL-E generates vocabulary cards," and in the comic-book digital stories of Le & Le (2025; #A06). The production turn is thus not confined to English prose; it extends across languages and into multimodal artefacts, although the non-English and visual cases remain a minority of the corpus.

> **Boundary condition (circularity caveat).** The conversational-tutor role (C1b) is coded zero times, but this absence is an artefact of the eligibility criteria, not a finding. Studies in which GenAI functioned only as a conversational partner were removed at screening, because criterion 3 requires the production of an artefact. The evidence that the field is moving *from* conversation *toward* production therefore rests on the bibliometric thematic-evolution analysis (RQ3; 3,050-record corpus), not on the C1 distribution reported above. What RQ4 establishes is the complementary and narrower point: among studies that already produce artefacts, the role typology is dominated by iterative co-design rather than one-shot automation.

### 4.2 The center of production, teacher agency, and the evidence behind the claims (RQ5)

Read through the center-of-production and teacher-agency dimensions (C2, C3), the corpus supports a qualified relocation of production. On C2, the producing agent is the teacher in roughly 16 studies, the student in 4 (#13, #19, #40, #A06), the pre-service teacher in 2 (#7, #23), a human–AI co-production dyad in 1 (#35), and a human-configured system in 2 (#8, #29). On C3, the designer level of agency (C3 = 4) is the modal code, in 17 studies; the facilitator level (C3 = 3) appears in 5 (#13, #19, #34, #40, #A06), the adapter level (C3 = 2) in 1 (#4), and the consumer-of-autonomous-system level (C3 = 1) in 1 (#29); one co-production case sits between facilitator and designer (#35, C3 = 3–4). The developer level (C3 = 5) is coded zero times.

**Theme 1. Production shifts toward the teacher-as-designer, but stops at a "designer ceiling."** The center of production moves from the publisher or expert toward the teacher acting as a designer: the designer level (C3 = 4) is modal, in 17 of 25 studies, and the teacher is the producing agent in roughly 16. In Lo (2025; #18), "teachers select GenAI to generate GE materials" with explicit agency over the process. The distribution, however, has a ceiling — the developer level (C3 = 5) is never reached, and only one study attains autonomous, software-level development (C1d; #17). Teachers become designers of materials, not developers of software: the relocation is real but bounded.

**Theme 2. A paradox — system-scale production can reduce teacher agency.** The most automated configurations do not maximize teacher agency; they can compress it. Bao (2026; #29) is coded at the lowest agency level (C3 = 1) because the teacher functions only as a blind evaluator of system output, and Park (2026; #8) names the shift directly: teachers' "roles may be shifting from simple content creators to content curators and editors" (p. 15). As production scales up through pipelines, the teacher's locus moves from making toward curating and checking — an agency trade-off the field rarely frames as a loss.

**Theme 3. Agency is framed positively, but the evidence is thin and sometimes only declared.** Where studies discuss role change, they tend to frame it as empowerment or transformation: the risk-and-positive dual pole on the critical dimension (C6) appears in 10 of 25 studies (#2, #6, #7, #8, #13, #17, #18, #19, #23, #30), while the remaining 15 discuss risk only. Two cautions temper this positive framing. First, the evidence behind agency and effectiveness claims is weak: on the evidence dimension (C8), only one study — Guo (2026; #35), a controlled experiment with three conditions and 40 participants, examining "Human-LLM creative writing" — provides strong causal evidence, while the majority are medium-strength, self-report or single-cohort designs. Second, agency is at times asserted rather than observed: in Zaiarna (2024; #34), teacher agency is survey-declared rather than behaviorally demonstrated, and the study sits at the facilitator ceiling (C3 = 3). The field's confidence in teacher empowerment currently runs ahead of the evidence that supports it.

**Theme 4. A learner-producer sub-current brings authorship and over-reliance into view.** A minority of studies relocate production to the learner (C2c with C1c′: #13, #19, #35, #40, #A06), and this is where authorship and dependency concerns concentrate. Learner production is explicit in Lee (2023; #40), where "participants created storybooks" (Fig. 3). Authorship and ownership are coded in five studies (#14, #19, #35, #40, #C04), and over-reliance or learner de-skilling in three (#30, #A06, #C04). Moving the production act to learners therefore redistributes more than labor: it reopens the unresolved question of who counts as the author, and of the point at which assistance becomes substitution.

**Theme 5. The gaps are the contribution — structural critique is nearly absent, and evidence trails claims.** Three gaps define the field's current limits, and a negative result is still a finding. First, structural critique is almost empty: across C6, ethics, bias, and labor recur, but platform dependency, value capture, and solutionism are largely unexamined. The closest any study comes is Al-Maawali (2026; #30), which observes that "AI-generated outputs often reflected Western-centric perspectives unless prompts were carefully crafted" (p. 10) — yet frames the problem as one of prompt craft rather than of structure. Second, evidence trails claims: with a single strong study (#35), the corpus asserts workload reduction, authenticity, and engagement far more often than it demonstrates them, and the "last-mile" validity and labor costs of checking AI output — the convenience-versus-validity tension visible on C4 — remain thinly studied. Third, agency is under-observed: the declared-versus-demonstrated gap (for example, #34) means the literature reports teachers' *sense* of agency more reliably than their actual practice. Taken together, these gaps mark out what this review adds. The field conceptualizes GenAI predominantly as an iterative co-designer rather than as an automaton or a conversational partner; it relocates the center of production toward the teacher-as-designer, but below the developer level and on thin evidence; and it leaves the structural-critical dimension — value capture, platform dependency, solutionism — as an empty cell, which is this review's distinctive gap finding.

---

## Ek 1 — İz alıntısı izleği (hangi tema → hangi alıntı)

Her İz birebir; kaynak `kol2/27` "Alıntı/İz" sütunu veya iskeletin kanıt haritası (kol2/27 + kol2/33'ten türetilmiş). Sayfa numaraları korunmuştur.

| Tema | Makale (#ID, Yazar-Yıl) | Birebir İz alıntısı | Kaynak |
|---|---|---|---|
| AS4-T1 (ana) | #7 Lenko-Szymanska 2026 | "students refined it in subsequent iterations to increase its precision" (p. 7) | iskelet / kol2/33 |
| AS4-T1 (destek) | #6 Lin 2025 | "refine/adjust prompts iteratively" | kol2/27 |
| AS4-T2 | #19 Risang Baskara 2024 | "students produce EFL podcasts (script→ideas→editing)" | kol2/27 |
| AS4-T3 (ana) | #29 Bao 2026 | "we designed and implemented the CCGF" | kol2/27 |
| AS4-T3 (destek) | #8 Park 2026 | "automated pipeline" | kol2/27 |
| AS4-T4 | #20 Nguyen N.H. 2026 | "ChatGPT develops extensive reading materials" | kol2/27 |
| AS4-T5 | #C02 Temiz 2025 | "DALL-E generates vocabulary cards" | kol2/27 |
| AS5-T1 | #18 Lo 2025 | "teachers select GenAI to generate GE materials" | kol2/27 |
| AS5-T2 | #8 Park 2026 | "their roles may be shifting from simple content creators to content curators and editors" (p. 15) | iskelet / kol2/33 |
| AS5-T3 | #35 Guo 2026 | "Human-LLM creative writing" (kontrollü deney; 3 koşul, 40 katılımcı) | kol2/27 |
| AS5-T4 | #40 Lee 2023 | "participants created storybooks" (Fig. 3) | kol2/27 |
| AS5-T5 | #30 Al-Maawali 2026 | "AI-generated outputs often reflected Western-centric perspectives unless prompts were carefully crafted" (p. 10) | iskelet / kol2/33 |

İki zorunlu kural izlenebilirliği:
- **C1b = 0 döngüsellik kuralı:** AS4 §4.1 sonundaki "Boundary condition" kutusunda açıkça uygulandı — kayma kanıtı AS3'e (bibliyometri) bağlandı, C1 dağılımına değil.
- **İddia↔kanıt (C8) ayrımı:** AS5-T3 ve AS5-T5'te açıkça vurgulandı — tek güçlü kanıt #35; çoğunluk orta/öz-bildirim; "iddia edilen" ≠ "gösterilen".

## Ek 2 — Açık / belirsiz noktalar (uydurma YOK)

1. **Yazar-yıl etiketleri** yalnızca `kol2/27` "Yazar-Yıl" sütunundan alınmıştır; **tam kaynakça + DOI doğrulaması AYRI bir bütünlük görevidir.** v3 taslağının bütünlük notu uyarınca şu an yalnız 12 referans doğrulanmış/gerçek sayılıyor; bu 25 dahil çalışma henüz doğrulanmış kaynakça listesinde değil. *(→ sıradaki bütünlük görevi: 25 dahil çalışmanın DOI/künye doğrulaması.)*
2. **İki ayrı "Lin 2025":** #6 (öğretmen, CFL okuma materyali) ve #13 (öğrenci, çok-kipli kompozisyon) — metin boyunca ID ile ayrıştırıldı.
3. **Bakım uyarısı — ÇÖZÜLDÜ (cloud):** Cowork'ün gördüğü bundle (`42c95a7`) eski; `kol2/27`'nin dağılım-özeti bloğu cloud tarafından **Görev-8'de zaten senkronlandı** (C1c = 11; C6 çift-kutup = 10; origin commit `e21f9de`). Bu düzyazı da aynı Görev-8 sonrası kilitli sayıları kullanıyor → tutarlı, ek işlem gerekmez.
4. **#35 C3 = "3–4"** (eş-üretim) olarak kodlanmıştır; C3 = 4 (17) toplamından ayrı sayılmıştır (iskeletle tutarlı).
5. **Çözülmüş İz bayrakları:** `kol2/27`'deki tüm ⚠ İz-teyit bayrakları (#2, #4, #7, #8, #34) Görev-8'de (`kol2/33`) kapatıldı; açık kodlama bayrağı kalmadı.
6. **Yerleştirme:** bu bölüm v3'teki "4. Preliminary Synthesis / 4.1 (RQ4) / 4.2 (RQ5)" (özet-temelli, priority-40) içeriğinin yerine geçmek üzere yazılmıştır; v3'e işlenmesi (taslak v4) ayrı bir yazım adımıdır.

---

## 🛡️ CLOUD DENETİM NOTU (Görev-9, 2026-06-24)
- Cowork düzyazısı `kol2/27` (v1.2+G8 kilitli) + iskelet ile **birebir denetlendi**: tüm C1/C2/C3/C6/C8 sayıları, makale ID grupları ve 12 İz alıntısı doğru.
- **İki zorunlu kural yerinde:** C1b=0 döngüselliği (Boundary condition kutusu, kayma kanıtı=AS3) + iddia↔kanıt ayrımı (AS5-T3/T5, tek güçlü #35).
- **Cloud düzeltmeleri:** (a) AS4-T5 "five→four target languages beyond EFL" (4 dil sayılıyordu: Çince/Arapça/Romence/Almanca); (b) iskelet yol referansı `kol2/25→25` (kök); (c) Ek-2 #3 bakım uyarısı "çözüldü" olarak güncellendi (özet bloğu Görev-8'de senkronlandı).
- **Sıradaki:** (1) v4 taslağına işleme (cowork); (2) **bütünlük görevi: 25 dahil çalışmanın DOI/künye doğrulaması** (cloud web erişimi var — kaynakça kilidi için kritik); (3) Tartışma + Giriş güncellemesi (C4↔C6 gerilimi, "what this paper adds").
