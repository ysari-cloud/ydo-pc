# Anahtar-Kelime Duyarlılık Testi — Sonuç ve Özet Not

**Çalıştırma:** 2026-06-20 · WoS Core Collection + Scopus (İÜC kurumsal erişim, vetisonline/proxy).
**Yöntem:** "Doğrudan delta" sorgusu = (artırılmış A terimleri) AND (brif §4 dil bloğu) **NOT** (orijinal A bloğu),
LA=English, PY 2018–2026. İlk ham sürüm aşırı gürültülü çıktı (WoS 2.920 / Scopus 1.783; jenerik
"image generation/AI-generated/generative model" + çift-anlamlı L2/CALL, ML literatürünü çekti).
**Kesinlik-odaklı** sürümde jenerik terimler ve L2/CALL çıkarıldı, yalnız spesifik araç adları
(Gemini, Bard, Claude, Copilot, ERNIE Bot, Qwen, Wenxin, Doubao, Llama, Perplexity, Grok, Sora,
DALL-E, Midjourney, stable diffusion, text-to-image) + net dil-eğitimi ifadeleri tutuldu →
**WoS 72 + Scopus 116 = 152 benzersiz kayıt.** Tümü gözle tarandı (`sensitivity_delta.csv`).

## Özet (1 paragraf)
152 aday kaydın büyük çoğunluğu (**130**) gürültüdür: "LLAMA" terimi GenAI aracı değil **LLAMA
dil-yatkınlık testini** (Lognostics) yakaladı; "Bard"=Shakespeare, "Claude"=Claude Mauger/Lévi-Strauss,
"Grok"=deyim ("kavramak"), "CLIP/BERT/text-to-image synthesis" saf ML çalışmaları. Gürültü ayıklandıktan
sonra geriye **12 gerçekten ilgili** (yabancı/ikinci dil eğitimi + adlandırılmış GenAI aracı) makale ve
**~7 sınırda** (özet doğrulaması gereken) kayıt kaldı; ayrıca **1 makale RETRACTED** (Poe/Gemini, Japonca
yazma — geri çekildiği için dışlanır). İlgili 12'nin yakaladığı araçlar: **Gemini (5), Copilot (3),
Grok (1), Bard (1), text-to-image (1, görsel-üretim), AI-üretimi geri bildirim (1)**. Kritik nokta:
bunların önemli kısmı **2024–2025** yayınıdır (Bard 2024, Gemini 2024, Copilot×2 2025, Gemini 2025,
text-to-image 2025) — yani bu **güncellik kaynaklı değil, gerçek bir anahtar-kelime açığıdır**: orijinal
dizgemiz yalnızca "ChatGPT/GenAI/LLM/chatbot" türü terimler içerdiği için, sadece bir araç adıyla
(ör. "Gemini", "Copilot") anılan ve "generative AI" demeyen dil-eğitimi makalelerini kaçırmıştır.

## HÜKÜM (karar kuralı uygulandı)
**Delta ANLAMLI** (≥12 ilgili + ~7 sınırda; tez-merkezli yazma/konuşma/sözcük + görsel-üretim içeriyor).
Öneri:
1. **Kalıcılaştır (yüksek-kesinlik alt-kümesi):** A bloğuna ekle → Gemini, Copilot, Grok, Bard, Poe,
   "ERNIE Bot", Qwen, Wenxin, Doubao, DALL-E, Midjourney, "stable diffusion", "text-to-image".
   **EKLEME:** "Llama", "Claude", GAI, "image generation", "AI-generated", "generative model" (gürültü).
2. Aramayı bu A bloğuyla **yeniden koş**, gelen ilgili kayıtları tam-metin tara, korpusa kat.
3. **PRISMA n'leri güncelle** (ek kaynak: anahtar-kelime duyarlılık taraması; +~12–19 aday).
4. Retracted makaleyi (Poe/Gemini) dışlama gerekçesiyle kaydet.

## Dosyalar
- `analysis/sensitivity_delta.csv` — 152 kayıt, sütunlar: relevant(Y/?/EXCL/N), new_term_hit, modal,
  year, journal, doc_type, title, doi, db, recency, note.
- Ham export'lar: `analysis/raw_data/` (yerelde; WoS tam-kayıt + Scopus başlık listesi) — repoya konmadı.
