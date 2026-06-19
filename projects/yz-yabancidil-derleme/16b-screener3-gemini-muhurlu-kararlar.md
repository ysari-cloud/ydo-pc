# Screener-3 (Gemini) — MÜHÜRLÜ Kararlar + Erken Uyum Kontrolü

> Tarayıcı 3 (Gemini) bağımsız kararları. `16-gemini-screener3-PROMPT.md` istemiyle, yalnız başlık+özetten,
> Claude (15b) ve cowork kararlarına **kör**. Tarih: 2026-06-19. Kapsam: **A (kapsayıcı)** kuralı verildi.
> Bu dosya, 3-yönlü Fleiss κ'nın denetlenebilir kanıtıdır (verbatim çıktı + ilk kıyas).

## Gemini ham çıktısı (verbatim)

| n | decision | c1 | conf | rationale (özet) |
|---|----------|----|------|------------------|
| 1 | INCLUDE | a | high | EFL öğretmenleri GenAI ile okuma materyali geliştiriyor |
| 2 | INCLUDE | a | high | Üretken YZ'nin ELT materyal geliştirmedeki potansiyeli |
| 3 | INCLUDE | c | high | ESAP materyal geliştirmede GenAI desteği/tasarımı |
| 4 | **EXCLUDE** | - | high | başlık/özette dil eğitimi bilgisi yok |
| 5 | INCLUDE | a | high | Arapça için AI-üretimi okuma anlama materyali değerlendirmesi |
| 6 | INCLUDE | other | high | L2 Çince'de GenAI içerik üretimi + öğretmen kimliği |
| 7 | INCLUDE | c | high | Aday öğretmenlerin ders tasarımında GenAI |
| 8 | INCLUDE | d | high | Söz-varlığı-kontrollü okuma materyali otomatik üretim hattı |
| 9 | INCLUDE | d | high | XR+YZ görev-tabanlı tasarım/yaygınlaştırma |
| 10 | INCLUDE | c | high | GenAI ile ders/materyal hazırlığı |
| 11 | INCLUDE | other | high | L2 materyallerinde GenAI — kavramsal/yansıtıcı |
| 12 | INCLUDE | b | high | EFL'de çok-araçlı (chatbot dahil) tasarım etkililiği |
| 13 | **EXCLUDE** | - | high | sadece öğrenci yazma kullanım etkisi |
| 14 | INCLUDE | c | high | ChatGPT ile kültürel materyal eş-üretimi |
| 15 | INCLUDE | d | high | NLP/YZ ile İngilizce materyal otomatik üretimi |
| 16 | INCLUDE | other | high | Öğretmen GenAI yeterlikleri haritalama |
| 17 | INCLUDE | d | high | Arapça için YZ öğretim materyali geliştirme/tasarım |
| 18 | INCLUDE | a | high | Global Englishes ELT materyallerinde GenAI |
| 19 | **EXCLUDE** | - | high | öğrenci YZ ile podcast üretimi (öğretmen üretimi yok) |
| 20 | INCLUDE | a | high | ChatGPT-üretimi okuma materyali leksikal profili |
| 21 | INCLUDE | other | high | Öğretmenlerin farklı aşamalarda GenAI etkileşimi |
| 22 | INCLUDE | a | high | Öğretmen materyal geliştirme + kişiselleştirme |
| 23 | INCLUDE | a | high | Dinamik materyallerde GenAI etkisi |
| 24 | **EXCLUDE** | - | high | sadece içerik üreticilerinin tutum/görüşü |
| 25 | **EXCLUDE** | - | high | üretken YZ/chatbot değil; hata/puanlama otomasyonu |
| 26 | INCLUDE | other | high | GenAI+chatbot olanakları gösterim/değerlendirme |
| 27 | INCLUDE | other | high | Kodsuz GenAI ile materyal geliştirme (derleme) |
| 28 | INCLUDE | a | high | ChatGPT ile Romence-yabancı-dil materyal tasarımı |
| 29 | **EXCLUDE** | - | high | genel K-12; yabancı/ikinci dil odağı yok |
| 30 | INCLUDE | a | high | Öğretmen AI-üretimi kültürel içeriği değerlendirme |
| 31 | INCLUDE | b | high | YZ konuşma-ajanları + edimbilim (konuşma-kutbu) |
| 32 | INCLUDE | c | high | EFL öğretmenleriyle AI eş-yaratım |
| 33 | **EXCLUDE** | - | high | genel eğitimde GenAI tutum analizi (dil-özgü değil) |
| 34 | INCLUDE | a | high | ChatGPT ile EFL ölçme-değerlendirme materyali |
| 35 | **EXCLUDE** | - | high | Almanca yaratıcı yazmada LLM kullanım etkisi (öğrenci) |
| 36 | **EXCLUDE** | - | high | sadece otomatik yazma puanlaması/değerlendirme |
| 37 | INCLUDE | a | high | L2 başlangıç için dilsel kontrollü metin üretimi |
| 38 | INCLUDE | other | high | GenAI dil öğretimi kapsam-belirleme derlemesi |
| 39 | INCLUDE | c | high | Çince karakter öğretiminde insan-makine iş birliği |
| 40 | INCLUDE | a | high | Genç EFL için AI içerik-üretici teknolojiler |
| 41 | INCLUDE | b | high | Chatbot+sosyal medya PLE (konuşma-kutbu) |
| 42 | INCLUDE | b | high | Chatbot pratik ortağı (konuşma-kutbu) |
| 43 | INCLUDE | d | high | Otonom öğrenim için chatbot uygulama geliştirme |
| 44 | INCLUDE | d | high | Mobil mesajlaşmada chatbot dilbilgisi uygulaması |
| 45 | INCLUDE | b | high | Hikaye-anlatımı chatbot, L2 çıktı (konuşma-kutbu) |
| 46 | **EXCLUDE** | - | high | YouTube içerik üreticilerinin görüş/eğilimi |
| 47 | INCLUDE | other | high | Sınıfta LLM pratik fikirler + metin üretimi |
| 48 | INCLUDE | other | high | Dil öğreniminde chatbot sistematik derlemesi |
| 49 | **EXCLUDE** | - | high | programlama dili öğrenimi (doğal dil değil) |
| 50 | INCLUDE | b | high | CLIL'de eğitsel YZ chatbotları (konuşma-kutbu) |
| 51 | INCLUDE | other | high | EFL'de YZ diyalog sistemleri sistematik derleme |
| 52 | INCLUDE | b | high | Chatbot-destekli dinamik değerlendirme (L2 söz varlığı) |
| 53 | INCLUDE | other | high | ELT'de YZ genel değerlendirme (kavramsal) |
| 54 | INCLUDE | other | high | EFL'de ses-tabanlı sanal ajanlar sistematik derleme |
| 55 | **EXCLUDE** | - | high | genel eğitim sohbet robotu (dil-özgü değil) |
| 56 | **EXCLUDE** | - | high | sadece öğrenci algı/fayda/sınırlılık görüşleri |

## Özet sayılar
- **Gemini:** INCLUDE = 43/56 · EXCLUDE = 13/56 {4,13,19,24,25,29,33,35,36,46,49,55,56}
- **Claude (15b), A-varyant:** INCLUDE = 53/56 · EXCLUDE = 3/56 {33,49,55}

## Erken uyum (Claude-A ↔ Gemini, 2-yönlü)
- **Ham anlaşma (Po): 46/56 = %82.1**
- **Cohen κ ≈ 0.31** (fair). DÜŞÜK görünmesi κ-paradoksu: INCLUDE yaygınlığı çok yüksek (Claude 53/56) → marjinal dengesizlik κ'yı bastırır. Ham %82 daha bilgilendirici.
- **10 anlaşmazlığın TAMAMI tek yönlü:** Gemini DIŞLA / Claude DAHİL. Gemini'nin dışlamaları Claude'unkini tam kapsıyor (nested) → rastgele gürültü değil, **sistematik eşik farkı** (Gemini daha katı).
- **10 anlaşmazlığın 7'si Claude'un zaten ⚑ işaretlediği belirsiz kayıt** (4,13,24,25,29,36,56) → süreç tasarlandığı gibi çalışıyor; bu kayıtlar tam-metinde çözülecek.
- **3 "temiz" anlaşmazlık (19,35,46):** hepsi kapsam-tanımı kararı — öğrenen-üretim kutbu (19,35) ve içerik-üretici/locus (46). İnsan tarayıcının hakemlik etmesi gereken sınır.

## İnsan tarayıcının (Screener-1) açıkça karara bağlaması gereken KAPSAM noktaları
1. **Öğrenen-üretim kutbu** (13,19,35): öğrenci YZ ile üretiyor (öğretmen değil) → dahil mi?
2. **İçerik-üretici/locus** (24,46): YouTuber/içerik üreticisi perspektifi → dahil mi?
3. **Yalnız tutum/algı** (24,56) ve **yalnız puanlama** (36): kuralın açık dışlama ölçütü — uygula mı?
4. **Kapsam-teyidi tam-metin** (4,29,25): dil-eğitimi odağı / üretken-YZ niteliği özetten belirsiz.

> C1 kodları: ortak-dahillerde net üretim vakalarında (a/d) uyumlu; c-vs-a ve "other" kovasında
> bir miktar kayma var — C1 ikincil, tam-metin kodlamasında netleşir, κ (dahil/dışla) ilgilendirmez.
