# Yöntem (Method) — Taslak v1

> Brif §5/§6 + PRISMA protokol `03`'ün yayına hazır prose hâli. Yayın dili İngilizce; yönlendirme
> notları Türkçe (> blok). **Gerçek sayılar** elimizdekiler: geniş korpus n=3.050, odaklı n=329
> (328 özetli), ön-uygun n=223. **Nihai dahil n + κ değeri = insan tam-metin doğrulaması sonrası
> doldurulacak** ([N] / [κ] yer tutucuları — uydurma YOK). PRISMA 2020'ye uyumlu yazıldı.

## 2.1 Research design
This study employs a two-pronged design combining a **bibliometric analysis** with a **systematic
review**, reported in accordance with the PRISMA 2020 statement [ATIF: Page et al., 2021, PRISMA
2020]. The bibliometric component maps the structure and evolution of the field (RQ1–RQ3); the
systematic-review component synthesizes how generative AI is conceptualized in foreign-language
material production and what this implies for the teacher's role (RQ4–RQ5). The study analyzes
published literature only; no human participants were involved.

> Not: İki katmanlı tasarım brifin "korpus inceliği" riskini yönetir — geniş katman bibliyometri,
> odaklı katman sentez. RQ = AS (research questions/araştırma soruları).

## 2.2 Research questions
> Brif §3'ten birebir. (RQ1–RQ3 bibliyometrik; RQ4–RQ5 sentez.)
- **RQ1.** What is the publication landscape (volume, growth, country/institution/source
  distribution) of generative AI in foreign language education?
- **RQ2.** What are the intellectual (co-citation, bibliographic coupling) and conceptual
  (keyword co-occurrence, thematic mapping) structures of the field?
- **RQ3.** Is the thematic focus shifting from a "conversational/tutoring tool" toward a
  "material-production/development tool"?
- **RQ4.** With what roles is generative AI conceptualized in foreign-language material design and
  production?
- **RQ5.** What evidence, claims, and gaps exist regarding the relocation of the center of
  production from publishers/experts toward language teachers, and what are the implications for
  teacher role and agency?

## 2.3 Information sources and search strategy
Two databases were searched: **Web of Science Core Collection** and **Scopus**. The search was
conducted on [SEARCH DATE — fiili tarih]. A **two-layer search strategy** was used to balance
corpus robustness against topical precision:
- **Broad layer (bibliometric corpus):** the intersection of a *generative AI* concept block (A)
  and a *foreign language education* concept block (D), i.e., `A AND D`.
- **Focused layer (synthesis subset):** the broad query further constrained by a
  *material/production* concept block (C), i.e., `A AND D AND C`.

The full Boolean strings (WoS `TS=`; Scopus `TITLE-ABS-KEY`) are provided in Appendix A and were
applied identically across both databases. [ATIF gerekmez — kendi metodumuz.]

> Not: A/C/D blokları brif §4'te. Appendix A'ya tam dizgeler konacak (zaten `00-PROJE-BRIFI.md §4`).
> "[SEARCH DATE]" = cowork'ün fiili çalıştırma günü; ondan alınacak.

## 2.4 Eligibility criteria
**Inclusion.** Records addressing generative AI in foreign/second language education; published
from January 2018 to the search date; in English; peer-reviewed and indexed. For the **synthesis
subset**, records additionally had to concern the design or production of materials, content, or
tools (the C block). **Document types:** the bibliometric corpus comprised articles, reviews, and
conference papers; the synthesis subset was restricted to journal articles and reviews.

**Exclusion.** AI studies outside language education; editorials, letters, notes, and errata (for
synthesis); records without retrievable full text (for synthesis); and cross-database duplicates.

**Time-window rationale.** A 2018 start captures the pre-ChatGPT "conversational tool" baseline;
thematic evolution is analyzed across slices (2018–2021 / 2022–2023 / 2024–) that bracket the
late-2022 inflection, rendering the hypothesized shift analytically visible.

> Not: 2018 başlangıcının gerekçesi AS3'ün kalbi. (Bulgularda göreceğiz: üretim literatürü ağırlıkla
> 2024+ — bu, kaymanın empirik kanıtı olarak yorumlanacak.)

## 2.5 Selection process
Records from both databases were merged and **de-duplicated** by DOI and title matching, yielding
**3,050** unique records in the broad corpus and **329** in the focused layer. Screening followed
the PRISMA 2020 stages: Identification → Screening (title–abstract) → Eligibility (full text) →
Included. Title–abstract screening was conducted by **two independent reviewers**; inter-rater
agreement is reported using **Cohen's κ = [κ]**, with disagreements resolved by a third reviewer.

For the synthesis layer, an abstract-level eligibility pass (journal article/review; demonstrable
material-production relevance; abstract available) identified **223** candidate records; these
were prioritized for full-text screening, from which **[N]** studies met final eligibility for
synthesis. The PRISMA flow diagram (Figure 1) reports counts and exclusion reasons at each stage.

> ⚠️ BÜTÜNLÜK: κ ve nihai [N] **insan tam-metin taraması sonrası** girilecek. Şu an ön-tarama
> aşamasındayız (özet temelli). Metni "two independent reviewers / κ" diye yazıyoruz çünkü
> PLANLANAN yöntem bu; sayıyı uydurmuyoruz, yer tutucu bırakıyoruz. (Brif §6 + protokol §6.)

## 2.6 Data extraction
Bibliometric metadata (authors, affiliations, countries, sources, years, keywords, citations, and
cited references) were extracted directly from the database exports. For the synthesis subset,
structured extraction followed an **a priori coding scheme** spanning eight dimensions (C1–C8;
Appendix B / `04-kodlama-kitabi.md`): AI role, center of production, teacher role and agency,
pedagogical validity and quality assurance, competencies and teacher education, critical/structural
dimensions, language-specific dimensions, and claim/evidence type. The scheme was applied
deductively and refined inductively during coding.

## 2.7 Analysis
**Bibliometric analysis (RQ1–RQ3).** Performance analysis (annual output, citations, productive
authors/institutions/countries/sources; Bradford/Lotka as optional) and science mapping
(co-citation, bibliographic coupling, keyword co-occurrence, a Callon centrality–density thematic
map, and time-sliced thematic evolution). Analyses were implemented in **Python (pandas)** for
performance metrics and thematic evolution, with **VOSviewer** for network visualization; co-citation
and coupling were derived from Web of Science cited-reference (`CR`) fields. [ATIF: VOSviewer — van
Eck & Waltman, 2010; bibliometric method — Donthu et al., 2021 / Aria & Cuccurullo, 2017.]

**Qualitative synthesis (RQ4–RQ5).** A qualitative content analysis applied the C1–C8 scheme; findings
were mapped onto the "conversation → production" continuum to address the relocation of the production
center and its implications for teacher agency.

> Not: R/bibliometrix yerine Python+VOSviewer kullandık (ortam kararı) — yöntemde bunu açıkça
> belirtmek şeffaflık. Atıf yuvaları (VOSviewer, bibliyometrik yöntem) export sonrası doğrulanacak.

## 2.8 Reporting, reproducibility, and research integrity
Reporting follows the PRISMA 2020 checklist (27 items). All analyses are reproducible from
date-stamped database exports and archived analysis scripts. Consistent with a strict integrity
standard, **no source, citation, DOI, or figure was fabricated**; unverifiable sources were
excluded, and journal indexing/quartile information was confirmed against JCR/Scopus and journal
pages. An AI-assistance disclosure is provided.

> Not: Bu paragraf brifin "değişmez ilke"sinin manuscript'teki karşılığı — hakem güveni için kritik.

---

## ⚠️ Bu taslakta doldurulacaklar (uydurma YOK)
- `[SEARCH DATE]` — cowork'ün fiili arama günü.
- `[κ]` — iki tarayıcı insan doğrulaması sonrası Cohen κ.
- `[N]` — tam-metin sonrası nihai sentez dahil sayısı.
- Atıf yuvaları: PRISMA (Page 2021), VOSviewer (van Eck & Waltman 2010), bibliyometrik yöntem
  (Donthu 2021 / Aria & Cuccurullo 2017) — bütünlük aşamasında DOI ile doğrulanacak.
- Appendix A (tam dizgeler) + Appendix B (codebook) eklenecek.
