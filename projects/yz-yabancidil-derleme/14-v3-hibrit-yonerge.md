# v3 HİBRİT YÖNERGE — Skill Chat İçin

> Skillerin aktif olduğu cowork oturumu yürütür (token ile `ysari-cloud/ydo-pc`,
> dal `claude/youthful-franklin-wszezx`). Amaç: **en iyi yazım (skill) + en iyi figür/tablo (v2)**
> birleşimi → `Makale_Taslak_v3.docx`. Kıyas raporu: `13-kiyas-raporu-v2-vs-skill.md`.

## TEMEL = senin skill taslağın
`Makale_Taslak_skill.docx` v3'ün **iskeleti, prozası ve argüman akışıdır** — KORU:
4-move Giriş (1.1–1.4) · Yöntem (2.1–2.7) · Bulgular (3.1–3.3) · ön-Sentez (4) ·
tam Tartışma (5.1–5.4) · Sonuç (6) · AI Disclosure · References. **Şablon prozaya DÖNME.**

## v2'DEN İÇERİ AL (`Makale_Taslak_v2.docx` repoda)
v2'de **4 tablo + 5 görsel** var; skill taslağında HİÇ figür yok (bu yüzden tek başına SSCI'ye
gönderilemez). Bunları skill metnine doğru çapalara göm:
- **5 figür** (görseller `word/media/` içinde — docx'i unzip ederek çıkar):
  yıllık üretim / ülke dağılımı → **§3.1**; VOSviewer anahtar-sözcük eş-oluşum + tematik harita → **§3.2**;
  **iki-panelli temiz-AS3 Şekil 5** (konuşma düşüşü + üretim emergent) → **§3.3**.
- **4 tablo** (v2'den içeriğiyle yeniden kur): yıl-dilimi (72/246/2.732), ülke (Çin 957…),
  kaynak (System 66…), AS3/kodlama tablosu → ilgili bölümlere.
- **Appendix C** (tematik-çerçeve sözlükleri + sınırlama) ve **Appendix D** (PRISMA 2020 27-madde
  kontrol listesi) → sonuna ekle. Skill taslağındaki "Appendices to be attached" yerine bunlar geçer.
- Figür/tablo **numaralarını ve başlıklarını** skill taslağının bölüm sırasına göre tutarlı yap;
  metinde her birine gönderme (Figure X, Table Y) ekle.

## YÖNTEM AYRINTISI
v2'nin §2.6 (sözlük temizleme/AS3 düzeltme kaydı) ve PRISMA n-akışı ayrıntısını, skill prozasını
bozmadan §2'ye taşı/güçlendir (skill sürümü daha derli toplu; v2'nin denetim-kanıtı değerli).

## BÜTÜNLÜK (değişmez)
- Yalnız **12 doğrulanmış atıf** gerçek (bkz. `SKILL-KIYAS-GIRDI-PAKETI.md §4`); gerisi `[CITE:...]`.
- **Cohen κ ve nihai sentez N = yer tutucu** (insan tam-metin doğrulaması yapılmadı).
- **Temiz AS3** sayıları: konuşma %58,3→%35,0→%14,3; üretim mutlak 2→7→51; oran 0,05→0,13
  (konuşmayı GEÇMEDİ). Eski %38 manşetini KULLANMA.
- Hiçbir sayı/DOI/figür uydurma. **AI Disclosure**'da AS3 düzeltmesinin belgelenmesini koru.

## ÇIKTI
- `projects/yz-yabancidil-derleme/Makale_Taslak_v3.docx` (v1/v2/skill'i EZME) → commit + push.
- Bitince: hangi figür/tabloların taşındığını ve v3'ün skill+v2'ye göre durumunu kısaca raporla.

> Sonra cloud-denetim v3'ü kontrol eder; ardından tek beklenen insan adımı: 56-set tam-metin
> (κ + nihai N) → Sentez (RQ4–RQ5) kesinleşir → gönderime hazır.
