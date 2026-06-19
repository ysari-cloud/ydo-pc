# PRISMA 2020 Protokolü (ön-kayıt taslağı / a priori)

> Brif §5 + §6'nın resmileştirilmiş hâli. Veri toplanmadan ÖNCE sabitlenir (a priori) — bu,
> sistematik derlemenin metodolojik meşruiyetinin temelidir. OSF'ye ön-kayıt için hazır
> iskelet. Arama sonrası yalnızca n'ler (akış şeması sayıları) ve fiili arama tarihi eklenir.

## 1. Başlık & kayıt
- **Çalışma:** From Conversation to Creation: Generative AI and the Transformation of Material
  Production and the Teacher's Role in Foreign Language Education — A Bibliometric and
  Systematic Review.
- **Tür:** Bibliyometrik analiz + sistematik derleme (PRISMA 2020).
- **Ön-kayıt:** OSF (opsiyonel ama önerilir — a priori protokol bağımsızlığı kanıtı).
- **Arama tarihi:** [doldurulacak — fiili çalıştırma günü].

## 2. Gerekçe & araştırma soruları
Bibliyometrik (betimleyici): **AS1** yayın manzarası; **AS2** entelektüel + kavramsal yapı;
**AS3** "konuşma/öğretici araç → materyal üretim/geliştirme aracı" tematik kayması.
Sentez: **AS4** YZ'nin materyal tasarım/üretiminde rolleri; **AS5** üretim merkezinin
yayıncı/uzmandan öğretmene kayması — kanıt, iddia, boşluk; öğretmen failliği sonuçları.

## 3. Uygunluk ölçütleri (PICo / kavramsal)
**Dahil:**
- Konu: yabancı/ikinci dil eğitiminde üretken yapay zekâ.
- Tarih: Ocak 2018 – arama tarihi.
- Dil: İngilizce.
- Statü: hakemli ve indeksli.
- Belge türü — **bibliyometrik korpus:** makale + derleme + bildiri (proceeding).
- Belge türü — **sentez alt-kümesi:** dergi makalesi + derleme; **ayrıca** materyal/içerik/araç
  tasarımı veya üretimini konu edinmiş olmak (C bloğu ölçütü).

**Dışla:**
- Dil eğitimi dışı YZ çalışmaları.
- Editöryel / mektup / not / errata (sentezde).
- Tam metni erişilemeyen kayıtlar (sentezde).
- Çapraz tekrarlar (WoS↔Scopus mükerrerleri).

**Zaman penceresi gerekçesi:** 2018 başlangıcı ChatGPT-öncesi "konuşma temelli araç" temel
hattını yakalar. Tematik evrim üç dilimle çözümlenir: **2018–2021 / 2022–2023 / 2024–**
(2022 sonu kırılmasını bracketler — kaymayı görünür kılan analitik araç budur).

## 4. Bilgi kaynakları
- Web of Science Core Collection.
- Scopus.
- (Tamamlayıcı: gerekirse dahil edilen çalışmaların kaynakçalarından ileri/geri izleme —
  yalnızca sentez alt-kümesi için, raporlanarak.)

## 5. Arama stratejisi
Tam dizgeler → brif §4 ve `02-export-rehberi.md`. İki katman: geniş (A AND D) bibliyometri
için; odaklı (A AND D AND C) sentez için. Tüm export'lar tarih damgalı saklanır (yeniden
üretilebilirlik). Kalibrasyon kuralları §4'te.

## 6. Eleme süreci (PRISMA 2020 akışı)
1. **Identification:** WoS + Scopus kayıtları birleştirilir → **çapraz tekilleştirme**
   (DOI + başlık eşleştirme).
2. **Screening (başlık-özet):** iki bağımsız tarayıcı; ölçütlere göre dahil/dışla.
3. **Eligibility (tam metin):** sentez alt-kümesi için tam metin değerlendirmesi.
4. **Included:** bibliyometrik korpus (geniş) + sentez alt-kümesi (odaklı).
- **Güvenilirlik:** iki bağımsız tarayıcı; tarayıcılar-arası uyum **Cohen κ** ile raporlanır;
  anlaşmazlık üçüncü hakemle çözülür.
- **Akış şeması:** Identification → Screening → Eligibility → Included; her kutunun n'i ve
  dışlama gerekçeleri arama sonrası doldurulur.

> Not: Tek-araştırmacı pratikte iki "tarayıcı" rolü, zaman-ayrık çift kodlama + κ ile
> simüle edilebilir; ancak ikinci bir insan tarayıcı SSCI inandırıcılığı için tercih edilir.
> (Karar kullanıcıya — sabah netleştirilecek.)

## 7. Veri çıkarımı (data extraction)
- **Bibliyometrik:** veri tabanı meta-verisi (yazar, kurum, ülke, kaynak, yıl, anahtar
  sözcük, atıf, kaynakça) doğrudan export'tan.
- **Sentez:** `04-kodlama-kitabi.md`'deki C1–C8 şemasıyla yapılandırılmış çıkarım.

## 8. Analiz planı
**Bibliyometrik (AS1–AS3):**
- *Performans analizi:* yıllık üretim, atıf, üretken yazar/kurum/ülke/kaynak; (ops.) Bradford/Lotka.
- *Bilim haritalama:* eş-atıf, bibliyografik eşleşme, anahtar-sözcük eş-oluşumu, Callon
  merkezilik/yoğunluk tematik haritası, **zaman-dilimli tematik evrim** (AS3'ün empirik testi).
- *Araçlar:* Bibliometrix/biblioshiny (R) + VOSviewer. Tarih damgalı export'larla yeniden üretilebilir.

**Sentez (AS4–AS5):**
- Tümdengelimli kodlama (C1–C8) + tümevarımlı düzeltme; nitel içerik analizi.
- Bulguların "konuşma → üretim" sürekliliğine eşlenmesi.

## 9. Raporlama & bütünlük
- PRISMA 2020 (27 madde) kontrol listesi.
- **Değişmez ilke:** hiçbir kaynak/atıf/DOI/sayı uydurulmaz; doğrulanamayan kaynak girmez.
- AI-destek beyanı manuscript'e eklenir.
- Çeyreklik/indeks bilgileri JCR/Scopus + dergi sayfasından teyitli yazılır.

## 10. Açık kararlar (sabah netleştirilecek)
- [ ] İkinci insan tarayıcı olacak mı? (κ için) Yoksa zaman-ayrık çift kodlama + üçüncü-hakem simülasyonu.
- [ ] OSF ön-kaydı yapılacak mı? (önerilir)
- [ ] Odaklı alt-küme: aramayla mı, yoksa geniş korpusu kodlama aşamasında C ile süzerek mi? (sonuç sayısına bağlı)
