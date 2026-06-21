# Duyarlılık Adaylarının Uygunluk Ön-Elemesi (Başlık/Öz Düzeyi)
> Tarih: 2026-06-21 (rev. — iki-kapı tutarlılık düzeltmesi) · Girdi: `makaleler/sensitivity_delta.csv` (152 sınıflı) · Ölçüt: `docs/03-prisma-protokol.md` §3 + `docs/04-kodlama-kitabi.md`.
> Hiçbir öz uydurulmadı; kararlar başlık + dergi + tür + anahtar-sözcük üst-verisine dayanır.

## 0. İKİ KAPI — kavramsal netlik (önceki tutarsızlığın düzeltmesi)
Bu projede iki ayrı eleme kapısı vardır; karıştırılmamalıdır:

1. **Relevans kapısı (duyarlılık testi):** "Adlandırılmış GenAI aracı bir dil bağlamında geçiyor mu?" — anahtar-kelime açığını saptar. Bu kapıdan **12 kesin ilgili** kayıt geçti (Gemini ×5, Copilot ×3, Grok ×1, Bard ×1, text-to-image ×1, AI-üretimi geri bildirim ×1). Bu sayı **değişmedi**.
2. **Sentez uygunluğu kapısı (bu belge):** PICo — yabancı/ikinci dil eğitimi bağlamı + makale/derleme türü + materyal/üretim odağı + ampirik/derleme. **Daha katı** ve relevanstan ayrıdır.

> **Düzeltme:** Önceki devirde "12 ilgili → senteze katılacak" ifadesi iki kapıyı birleştirerek fazla ileri gitti. Doğrusu: 12'si relevans-onaylı; bunların **10'u doğrudan uygun**, **2'si (Bard=kapsam, Grok=tür)** uygunluk kararı **tam-metinde** verilir. Bu iki kayıt 'şüpheli/dışlanacak' diye **önyargılanmaz** — tam metni okumadan dışlama kararı verilmez.

## 1. Dedup ve havuz
- 22 db-isabeti → WoS↔Scopus mükerrerleri birleşti (Nexia Tutor, Poe/Gemini-retracted) → **20 benzersiz**.
- 20 = 12 relevans-onaylı (Y) + 7 belirsiz (?) + 1 retracted.

## 2. Karar özeti (4 katman)
| Katman | Açıklama | Sayı |
|---|---|---|
| A | Doğrudan uygun — tam-metin kodlamaya ilerlet | 10 |
| B | Relevans-onaylı '12'nin 2'si; uygunluk kararı tam-metinde (Bard=kapsam, Grok=tür) | 2 |
| C | Gerçekten belirsiz (orijinal '?') — tam metin gerekli | 5 |
| D | Başlık/öz aşamasında dışla (gerekçeli) | 3 (benzersiz) |
| | **Benzersiz toplam** | **20** |

- Tutarlılık kontrolü: **A + B = 10 + 2 = 12** = relevans kapısının '12 kesin ilgili'si. ✓

## 3. Katman A — Doğrudan uygun (10)
| ID | Yıl | DB | Tür | Dergi | Araç | Karar | Başlık (kısalt.) |
|---|---|---|---|---|---|---|---|
| A01 | 2024 | Scopus | Article | World Journal of English Languag | Gemini | ILERLET | Challenges and Motivation: Assessing Gemini's Impact o |
| A02 | 2025 | WoS | Article | Computers and Education Open | Gemini | ILERLET | Grammar and engagement in focus: Evaluating Gemini AI' |
| A03 | 2025 | Scopus | Article | CALL-EJ | Copilot | ILERLET | Using Copilot to Foster Utterance Fluency of Undergrad |
| A04 | 2025 | Scopus | Article | World Journal of English Languag | Copilot | ILERLET | Unveiling the Role of Copilot in Enhancing EFL Learner |
| A05 | 2025 | Scopus | Article | Childhood Education | Gemini | ILERLET | Gemini Storybook for Language Teaching and Learning |
| A06 | 2025 | Scopus | Article | CALL-EJ | Text-to-image | ILERLET | Digital Storytelling with AI Text-to-Image: A Creative |
| A07 | 2026 | WoS | Article | IJOLE (Int. J. of Language Educa | Gemini | ILERLET | Students' Perceptions on Digital Literacy and Writing  |
| A08 | 2026 | WoS | Article | IJACSA | AI-üretimi geri bildirim | ILERLET | Pedagogical Mediation Through Prompt Engineering: An E |
| A09 | 2026 | WoS | Article | Arab World English Journal | Gemini | ILERLET | Enhancing Engineering Students' English-Speaking Skill |
| A10 | 2026 | Scopus | Article | Int. J. of Learning, Teaching an | Copilot | ILERLET | Reimagining Writing Feedback: The Effect of Copilot AI |

**Gerekçeler:**

- **A01** — Challenges and Motivation: Assessing Gemini's Impact on Undergraduate EFL Students in Classroom Settings · DOI yok
  - EFL + Gemini + ampirik görünüm; tam metinde tasarım/etki teyidi.
- **A02** — Grammar and engagement in focus: Evaluating Gemini AI's impact on an educational environment · DOI: 10.1016/j.caeo.2025.100302
  - Eğitim ortamında Gemini etkisi (dilbilgisi/katılım); DOI doğrulu, ampirik.
- **A03** — Using Copilot to Foster Utterance Fluency of Undergraduates: A Multiple Case Study · DOI yok
  - CALL dergisi + Copilot + konuşma akıcılığı; çoklu örnek olay = ampirik.
- **A04** — Unveiling the Role of Copilot in Enhancing EFL Learners' Writing Skills: A Content Analysis · DOI yok
  - EFL yazma + Copilot + içerik analizi; tür uygun.
- **A05** — Gemini Storybook for Language Teaching and Learning · DOI yok
  - Dil öğretimi için materyal (storybook) üretimi — C-bloğu güçlü.
- **A06** — Digital Storytelling with AI Text-to-Image: A Creative Path to Vocabulary Retention · DOI yok
  - Metinden-görsele GenAI + söz varlığı + dijital öyküleme; C-bloğu güçlü.
- **A07** — Students' Perceptions on Digital Literacy and Writing Skills Using Local Indigenous Poem: Google Gemini Interactive Multimedia Approach · DOI: 10.26858/ijole.v10i1.83711
  - Dil eğitimi dergisi + Gemini çok-ortamlı materyal + yazma; DOI doğrulu.
- **A08** — Pedagogical Mediation Through Prompt Engineering: An Expert Evaluation of AI-Generated Feedback on Islamic-Integrated EFL Argumentative Writing · DOI yok
  - EFL yazma + prompt mühendisliği + AI-üretimi geri bildirim; uzman değerlendirmesi = ampirik.
- **A09** — Enhancing Engineering Students' English-Speaking Skills via Role-plays through Google Gemini 2.5 Flash, CEFR in Assessment, Blended Learning · DOI: 10.24093/awej/vol17no1.25
  - Konuşma + Gemini 2.5 + CEFR hizalama (C4); DOI doğrulu.
- **A10** — Reimagining Writing Feedback: The Effect of Copilot AI on EFL Students' Written Performance · DOI yok
  - EFL yazma performansına Copilot etkisi; deneysel etki görünümü; tür uygun.

## 4. Katman B — Relevans-onaylı, uygunluk tam-metinde (2)
| ID | Yıl | DB | Tür | Dergi | Araç | Karar | Başlık (kısalt.) |
|---|---|---|---|---|---|---|---|
| B01 | 2024 | WoS | Article | European Journal of Humour Resea | Bard | TAM-METIN (kapsam) | Creative writing in the hands of artificial intelligen |
| B02 | 2026 | Scopus | Book Chapter | Overdependence on AI in Academia | Grok | TAM-METIN (tür) | The Overdependence on Grok as an AI Tool in English La |

**Gerekçeler:**

- **B01** — Creative writing in the hands of artificial intelligence: the analysis of humour in Bard-generated texts · DOI: 10.7592/EJHR2024.12.4.928
  - RELEVANS kapısından geçti (gerçek araç Bard; '12 kesin ilgili' içinde). UYGUNLUK kapısında tek soru KAPSAM: dergi=mizah araştırması, başlık=AI-üretimi metinde mizah çözümlemesi → yabancı/ikinci DİL EĞİTİMİ bağlamı tam-metinde teyit edilecek. Önyargısız.
- **B02** — The Overdependence on Grok as an AI Tool in English Language Learning · DOI yok
  - RELEVANS kapısından geçti (İngilizce öğrenimi + Grok; konu net ilgili). UYGUNLUK kapısında tek soru BELGE TÜRÜ: kitap bölümü; a priori protokol sentez alt-kümesini 'makale+derleme' ile sınırlıyor → tür kararı (katı=dışla / gerekçeli gevşet). Eleştirel boyut (C6) için değerli.

## 5. Katman C — Belirsiz, tam metin gerekli (5)
| ID | Yıl | DB | Tür | Dergi | Araç | Karar | Başlık (kısalt.) |
|---|---|---|---|---|---|---|---|
| C01 | 2025 | WoS | Article | Studies in Self-Access Learning  | (Copilot?) | TAM-METIN | AI as a Language Learning Facilitator: Examining Vocab |
| C02 | 2025 | WoS | Article | Journal of Educational Research | (görsel çıktı/AI?) | TAM-METIN | Utilization of AI-aided vocabulary teaching in K-12: A |
| C03 | 2025 | Scopus | Article | AI (Switzerland) | Görsel üretim | TAM-METIN (kapsam) | The Impact of Ancient Greek Prompts on Artificial Inte |
| C04 | 2025 | Scopus | Article | Social Sciences and Humanities O | (AI — belirsiz) | TAM-METIN | Investigating the effects of AI-assisted teacher instr |
| C05 | 2026 | Scopus | Article | Technology in Language Teaching  | (AI — belirsiz) | TAM-METIN | The Effect of AI-Based Instruction on Vocabulary Reten |

**Gerekçeler:**

- **C01** — AI as a Language Learning Facilitator: Examining Vocabulary and Self-Regulation in EFL Learners · DOI: 10.37237/202507
  - EFL + söz varlığı + öz-düzenleme; anahtar sözcükte Copilot ama başlıkta jenerik 'AI'. Aracın gerçek GenAI olduğu teyit gerekli.
- **C02** — Utilization of AI-aided vocabulary teaching in K-12: A case study · DOI: 10.1080/00220671.2025.2510400
  - Yabancı Diller YO yazarı → muhtemelen L2; 'görsel çıktı' GenAI'a işaret edebilir. Spesifik araç + L2 bağlamı teyit gerekli.
- **C03** — The Impact of Ancient Greek Prompts on Artificial Intelligence Image Generation: A New Educational Paradigm · DOI yok
  - Görsel-üretim GenAI fakat odak prompt-dili → görsel çıktı; yabancı dil öğretimi mi genel 'eğitim paradigması' mı belirsiz.
- **C04** — Investigating the effects of AI-assisted teacher instruction on online IELTS writing · DOI yok
  - IELTS yazma = L2; öğretmen-aracılı AI. Aracın üretken/GenAI olduğu teyit gerekli.
- **C05** — The Effect of AI-Based Instruction on Vocabulary Retention and Learner Motivation in Higher Education · DOI yok
  - Dil-öğretimi dergisi + söz varlığı/motivasyon; 'AI-based' jenerik. Spesifik GenAI araç teyidi gerekli.

## 6. Katman D — Dışlananlar (3 benzersiz)
| ID | Yıl | DB | Tür | Dergi | Araç | Karar | Başlık (kısalt.) |
|---|---|---|---|---|---|---|---|
| D01 | 2024 | WoS+Scopus | Proceedings/Conference | MIUCC 2024 | Özel sistem | DIŞLA | Nexia Tutor: An AI-Powered Language Personalized Learn |
| D02 | 2025 | WoS | Proceedings | MMM 2025 (Multimedia Modeling) | Özel sistem | DIŞLA | CleverFox: Integrating Visual Mnemonics with AI for En |
| D03 | 2025 | WoS+Scopus | Article (RETRACTED) | British Educational Research Jou | Gemini/Poe | DIŞLA | Poe or Gemini for fostering writing skills in Japanese |

**Gerekçeler:**

- **D01** — Nexia Tutor: An AI-Powered Language Personalized Learning System for Kids with Dyslexia and Reading Challenges · DOI: 10.1109/MIUCC62295.2024.10783640
  - DIŞLA: bildiri (sentez türü dışı) + disleksi/okuma (muhtemelen L1) + GenAI değil özel sistem. WoS+Scopus mükerreri birleştirildi.
- **D02** — CleverFox: Integrating Visual Mnemonics with AI for Enhanced Language Learning · DOI: 10.1007/978-981-96-2074-6_11
  - DIŞLA: bildiri (CS/multimedya, sentez türü dışı) + özel sistem; öğretmenin GenAI ile materyal üretimi değil.
- **D03** — Poe or Gemini for fostering writing skills in Japanese upper-intermediate learners ... (RETRACTED 2026) · DOI: 10.1002/berj.4119
  - DIŞLA: makale GERİ ÇEKİLDİ (retracted, BERJ 2026). Bütünlük gereği alınmaz. WoS+Scopus mükerreri birleştirildi.

## 7. Güncel Kol-2 PRISMA tahmini
- Diğer yöntemlerle belirlenen (benzersiz): **20** (22 isabet − 2 çapraz mükerrer).
- Başlık/öz aşamasında dışlanan: **3** (1 retracted, 2 bildiri/kapsam).
- Tam-metin için getirilecek: **17** (A 10 + B 2 + C 5).
- **Senteze öngörülen ek (Kol-2):** kesin 10 (A) + tam-metinde teyitle B'den 0–2 ve C'den ~2–4 → **toplam ≈ 12–16**.
- Tutarlılık: '12 kesin ilgili' relevans bulgusu korunur; sentez uygunluğu ondan bağımsız ve şeffaf raporlanır.

## 8. Tam-metin getirme listesi (17)
| # | ID | Katman | Başlık | Erişim ipucu |
|---|---|---|---|---|
| 1 | A01 | A | Challenges and Motivation: Assessing Gemini's  | World Journal of English Language 2024 — baslik aramasi |
| 2 | A02 | A | Grammar and engagement in focus: Evaluating Ge | DOI 10.1016/j.caeo.2025.100302 |
| 3 | A03 | A | Using Copilot to Foster Utterance Fluency of U | CALL-EJ 2025 — baslik aramasi |
| 4 | A04 | A | Unveiling the Role of Copilot in Enhancing EFL | World Journal of English Language 2025 — baslik aramasi |
| 5 | A05 | A | Gemini Storybook for Language Teaching and Lea | Childhood Education 2025 — baslik aramasi |
| 6 | A06 | A | Digital Storytelling with AI Text-to-Image: A  | CALL-EJ 2025 — baslik aramasi |
| 7 | A07 | A | Students' Perceptions on Digital Literacy and  | DOI 10.26858/ijole.v10i1.83711 |
| 8 | A08 | A | Pedagogical Mediation Through Prompt Engineeri | IJACSA 2026 — baslik aramasi |
| 9 | A09 | A | Enhancing Engineering Students' English-Speaki | DOI 10.24093/awej/vol17no1.25 |
| 10 | A10 | A | Reimagining Writing Feedback: The Effect of Co | Int. J. of Learning, Teaching and Educational Research 2026 — baslik aramasi |
| 11 | B01 | B | Creative writing in the hands of artificial in | DOI 10.7592/EJHR2024.12.4.928 |
| 12 | B02 | B | The Overdependence on Grok as an AI Tool in En | Overdependence on AI in Academia (kitap) 2026 — baslik aramasi |
| 13 | C01 | C | AI as a Language Learning Facilitator: Examini | DOI 10.37237/202507 |
| 14 | C02 | C | Utilization of AI-aided vocabulary teaching in | DOI 10.1080/00220671.2025.2510400 |
| 15 | C03 | C | The Impact of Ancient Greek Prompts on Artific | AI (Switzerland) 2025 — baslik aramasi |
| 16 | C04 | C | Investigating the effects of AI-assisted teach | Social Sciences and Humanities Open 2025 — baslik aramasi |
| 17 | C05 | C | The Effect of AI-Based Instruction on Vocabula | Technology in Language Teaching and Learning 2026 — baslik aramasi |
