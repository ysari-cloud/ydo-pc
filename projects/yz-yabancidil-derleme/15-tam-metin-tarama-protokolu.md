# Tam-Metin Tarama & κ Protokolü (Sentez Alt-Kümesi)

> Sentez (AS4–AS5) için 56 aday kaydın tam-metin elemesi. Amaç: **nihai N** (sentez örneklemi)
> + **Cohen κ** (tarayıcılar-arası uyum). Bu dosya, iki tarayıcının **aynı karar kuralını**
> kullanmasını sağlar — κ'nın anlamlı olması için şart. Tarih: 2026-06-19.

## 0. Rol & bağımsızlık (KESİN)
- **Tarayıcı 1 = Doç. Dr. Yunus Emre Sarı (insan):** kararı **tam metinden** verir.
- **Tarayıcı 2 = Claude (YZ):** kararı **yalnızca başlık+özetten**, cowork ön-kodlamasına **kör** verdi.
  Kararlar `15b-screener2-AI-muhurlu-kararlar.md` dosyasında **tarama öncesi** commit'lendi
  (bağımsızlık kanıtı; git tarih damgası).
- **Anlaşmazlık çözümü (adjudikasyon):** insan tarayıcı, tam metne karşı yeniden okuyup karar verir.
- **Bilgi-asimetrisi (sınırlama):** YZ tarayıcı tam metne erişemediği için başlık+özetle çalıştı;
  bu, manuscript'te **açıkça beyan edilir** (aşağıda §6). İnsan tarayıcı tam metin kullandı.

## 1. Uygunluk birimi
Her kayıt **sentez alt-kümesine dahil mi?** → İkili karar: **INCLUDE / EXCLUDE.**
("Belirsiz" → geçici INCLUDE + tam-metin önceliği bayrağı; tam metinle kesinleşir.)

## 2. Dahil/dışla karar kuralı (ortak)
**INCLUDE** — kayıt şu ölçütlerin TÜMÜNÜ karşılıyorsa:
1. **Konu:** yabancı/ikinci dil eğitimi (EFL/ESL/DaF/CFL/Arapça-yabancı-dil vb.). *Doğal dil*;
   programlama "dili" DEĞİL.
2. **Teknoloji:** üretken YZ (LLM/ChatGPT/AIGC) **veya** onun öncülü sayılan diyalog/chatbot sistemi
   (AS3 sürekliliğinin "konuşma kutbu" için).
3. **İçerik bloğu (C):** çalışma, dil öğretim **materyali/içeriği/aracının üretimi, tasarımı,
   geliştirilmesi veya değerlendirilmesi** ile **ya da** bu üretimde **öğretmen rolü/failliği** ile
   esaslı biçimde ilgili.
4. **Tür:** hakemli dergi makalesi **veya** derleme. (Editöryel/mektup/not/errata = dışla.)
5. **Dil:** İngilizce. **Tarih:** 2018–arama tarihi.

**EXCLUDE** — biri bile geçerliyse:
- Dil eğitimi DIŞI (genel eğitim/başka alan) ya da programlama-dili eğitimi.
- Üretken YZ ile de konuşma-öncülü chatbot ile de ilgisi yok.
- Materyal/araç üretimi-tasarımı-değerlendirmesi YOK **ve** öğretmen-üretim rolü YOK
  (yalnız öğrenci-kullanım etkisi / yalnız tutum ölçümü / yalnız değerlendirme-puanlama kullanımı).
- Tam metin erişilemiyor (sentezde).

## 3. ⚠️ KARARLAŞTIRILACAK: kapsam varyantı (taramadan ÖNCE sabitle)
"Konuşma kutbu" çalışmaları (saf chatbot/konuşma-partneri, üretim yok — örn. Fryer 2019,
konuşma-ajanları) sentez alt-kümesine girsin mi?

- **(A) Kapsayıcı (süreklilik) — ÖNERİLEN:** konuşma-kutbu çalışmaları **karşıt/temel-hat (contrast)**
  olarak DAHİL; sentezde "konuşma → üretim" sürekliliğinin "önce" ucunu temsil eder. Köprü-set
  gerekçesini korur. Bu çalışmalar `C1b/konuşma-kutbu` alt-etiketiyle ayrılır.
- **(B) Katı (yalnız-üretim):** yalnız materyal **üretim/tasarım/geliştirme** odaklı çalışmalar dahil;
  saf konuşma-partneri çalışmaları dışlanır (bunlar bibliyometrik korpusta zaten temsil ediliyor).

> Benim mühürlü kararlarımda **her iki varyant için ayrı sütun** var (`INC_kapsayıcı`, `INC_katı`).
> Sen hangisini seçersen, κ o varyanttaki sütunuma karşı hesaplanır. **Öneri: (A) Kapsayıcı** —
> köprü-set gerekçesiyle tutarlı, SSCI'da daha savunulabilir, AS3 anlatısını besler.

## 4. C1 rolü (ikincil kodlama — opsiyonel κ #2)
Dahil edilen her çalışma için baskın C1 rolü (kodlama kitabı): C1a içerik üreticisi · C1b konuşma-öğretici ·
C1c eş-tasarımcı/yardımcı · C1d özerk üretici-geliştirici. (C1 için ayrı bir kodlama-κ'sı, dahil set
üzerinde sonradan hesaplanabilir.)

## 5. κ hesap planı
1. Sen `01-Tarama-FORMU`'nu **benim mühürlü sütunuma bakmadan** doldur (INCLUDE/EXCLUDE, C1, gerekçe,
   tam-metin-erişim Y/N).
2. Bana geri ver → seçilen kapsam varyantındaki mühürlü sütunumla eşleştirip **Cohen κ** hesaplarım
   (2×2 mutabakat tablosu + gözlenen/şans uyumu + κ + %95 GA).
3. **Anlaşmazlık listesi** çıkar → sen tam metne karşı çözersin → **uzlaşı = nihai dahil/dışla**.
4. **Nihai N** = uzlaşılan INCLUDE sayısı → PRISMA "Included (synthesis)" kutusuna yazılır;
   dışlananlar **gerekçe sayımıyla** PRISMA "Eligibility → excluded" kutusuna girer.

κ yorum eşikleri (Landis & Koch): <0 yok · 0–0,20 önemsiz · 0,21–0,40 zayıf · 0,41–0,60 orta ·
0,61–0,80 iyi · 0,81–1,00 mükemmel. Hedef ≥0,60 (raporlanabilir); düşükse → kural netleştir + yeniden tara.

## 6. YZ-beyanı için taslak ifade (manuscript'e)
> "Title/abstract screening reliability was assessed with two independent screeners. The first
> screener (the author) assessed full texts; a generative-AI assistant served as an independent
> second screener operating on titles and abstracts, blind to prior coding. Inter-rater agreement
> was quantified with Cohen's κ (κ = [N], 95% CI [..]). All disagreements were adjudicated by the
> author against the full text, and the AI second screener's role is disclosed in the AI-use
> statement. The information asymmetry (abstract-level AI vs. full-text human screening) is
> acknowledged as a limitation."

## 6b. ➕ EK: Üçüncü tarayıcı (Gemini) — 3-değerlendirici tasarımı (2026-06-19)
Kullanıcı kararı: ikinci bir LLM (Gemini) **bağımsız Tarayıcı-3** olarak eklendi.
- **Tarayıcı-3 = Gemini (YZ):** Claude'un mühürlü kararlarına ve cowork'e **kör**, aynı protokol +
  kapsam A + aynı 56 başlık/özetle karar verir. İstem: `16-gemini-screener3-PROMPT.md` (kullanıcı
  Gemini'ye yapıştırır, çıktıyı bana geri verir).
- **κ planı (güncel):** 3 değerlendirici için **Fleiss κ** (genel uyum) + **çiftli Cohen κ**
  (İnsan–Claude, İnsan–Gemini, Claude–Gemini). Claude–Gemini = modeller-arası güvenilirlik alt-bulgusu.
- **Uzlaşı:** geçici karar = 3'ten 2 çoğunluk; **anlaşmazlık/azınlık** kayıtlarını insan tam metne
  karşı adjudike eder → **nihai N**.
- **Beyan (güncel):** "İki farklı büyük dil modeli (Claude, Gemini) başlık+özet düzeyinde bağımsız
  ikinci/üçüncü tarayıcı olarak görev aldı; insan tarayıcı tam metni kullandı ve tüm anlaşmazlıkları
  tam metne karşı adjudike etti." Asimetri (YZ=özet, insan=tam metin) sınırlama olarak belirtilir.

## 7. Değişmez ilke
κ ve nihai N **uydurulmaz**; gerçek iki-tarayıcı kararlarından hesaplanır. Bu protokol, sürecin
yeniden-üretilebilir ve denetlenebilir olmasını sağlar.
