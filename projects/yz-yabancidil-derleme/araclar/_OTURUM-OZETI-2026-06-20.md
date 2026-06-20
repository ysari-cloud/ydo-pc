# Oturum Özeti — 2026-06-20 (PDF toplama + Anahtar-Kelime Duyarlılık Testi)

Bu dosya, oturumda yapılan tüm işlerin kalıcı kaydıdır.

---
## A) Tam-Metin (OA + kapalı) Toplama
- Klasör: `makaleler/TAM_METIN/` · ad biçimi `<n>_Yazar_Yıl.pdf` · hepsi DOI ile doğrulandı.
- **Durum: 44 / 45 dahil makale elde edildi.**
- **Dışlananlar (gerekçeli, bkz. `20-dahil-disi-karar-notlari.md`):**
  - #22 Wardat 2025 — dergi (Forum for Linguistic Studies) Scopus'tan 2025'te çıkarıldı, WoS'ta yok.
  - #10 Guo 2026 — tam metin elde edilemedi (IJACSA sayısı yayımlanmadı).
- **Erişim engeli (bkz. `21-erisim-engelleri.md`):**
  - #27 Shin 2026 (ELT Journal/Oxford) — İÜC aboneliği yok; ayrıca ampirik değil "feature" yazısı (tür uygunluğu da gözden geçirilmeli). ILL/yazardan isteme.
- **İkincil kaynaklar (atıf için, korpusa değil):** `makaleler/00_ikincil_kaynaklar/`
  - Deng & Jamaludin 2026 (SAGE Open) · Griche & Bennis 2026 (TLTL).
- **Snowball adayı:** Mi vd. 2025 (ECNU Review of Education) — `makaleler/_kontrol_snowball/`.

---
## B) Anahtar-Kelime Duyarlılık Testi (PRESS)
Soru: A bloğuna **adlandırılmış GenAI araçları + görsel/çok-kipli üretim** terimleri eklenince
korpusa kaç YENİ ilgili kayıt giriyor? (Tetik: iki komşu SLR — Deng, Griche.)

### Koşulan sorgular ve sayılar (İÜC kurumsal WoS+Scopus, vetisonline proxy)
| Aşama | WoS | Scopus |
|---|---|---|
| Ham doğrudan-delta (jenerik terimler dahil; gürültülü) | 2.920 | 1.783 |
| **Kesinlik-odaklı doğrudan-delta** (sadece spesifik araç adları, NOT eski-A) | **72** | **116** |
| Tam birleşik broad — araçlı | 7.770 | 7.178 |
| Tam birleşik broad — KONTROL (araçsız) | 7.217 | 6.914 |
| **Araçların net katkısı (araçlı − kontrol)** | **+553** | **+264** |

### Sınıflama (72 + 116 = 152 benzersiz kayıt, hepsi gözle tarandı → `analysis/sensitivity_delta.csv`)
- **İlgili (gerçek GenAI aracı + dil eğitimi): 12** — Gemini ×5, Copilot ×3, Grok ×1, Bard ×1, text-to-image ×1 (görsel), AI-üretimi geri bildirim ×1.
- **Sınırda (özet gerekli): ~7.**
- **RETRACTED: 1** (Poe/Gemini, Japonca yazma) → dışlanır.
- **Gürültü: 130.** Ana tuzak: "LLAMA" = Meta modeli değil, **LLAMA dil-yatkınlık testi**; "Bard"=Shakespeare, "Claude"=Mauger/Lévi-Strauss, "Grok"=deyim, "CLIP/BERT/text-to-image synthesis"=ML.

### Yorum
- Araç terimlerinin **net katkısı küçük** (WoS +553 / Scopus +264, çoğu gürültü → ~12 gerçek ilgili).
- İlgili makalelerin önemli kısmı **2024–2025** → bu **güncellik değil, gerçek bir anahtar-kelime açığı**: orijinal dizge yalnız "ChatGPT/GenAI/LLM/chatbot" içerdiği için, sadece araç adıyla (Gemini/Copilot) anılan makaleleri kaçırmış.
- **Önemli ikincil bulgu:** Rekonstrüksiyon (kontrol) WoS 7.217 / Scopus 6.914, tarihsel orijinal broad'tan (≈1.932 / 2.824) çok büyük → **asıl korpus brif §4 dizgelerinden daha dar bir konfigürasyonla kurulmuş** (muhtemelen ek konu/belge-türü filtresi veya daha dar dil bloğu). Metot yazımında bu tutarlılık netleştirilmeli.

### HÜKÜM (karar kuralı)
Araç adları korpusu **kökten değiştirmiyor → baştan koşmaya gerek YOK.** Yapılacak:
1. 12 ilgili (+~7 sınırda) makaleyi tam-metin tara; uygun olanları **"ek kaynak/snowball"** olarak korpusa kat (PRISMA "diğer yöntemlerle bulunan kayıtlar" kutusu +N).
2. Dahil sayısı 45 → ~50 civarına güncellenir; bir paragraf metodoloji/duyarlılık notu yazılır.
3. (Opsiyonel ağır yol) Yüksek-kesinlik araç adlarını (Gemini, Copilot, Grok, Bard, Poe, ERNIE Bot, Qwen, Wenxin, Doubao, DALL-E, Midjourney, "stable diffusion", "text-to-image") A bloğuna kalıcılaştırıp tüm aramayı yeniden koşmak. "Llama/Claude/generic" EKLENMEZ.
4. RETRACTED makaleyi dışlama gerekçesiyle kaydet.

### Dosyalar
- `analysis/sensitivity_delta.csv` (152 kayıt, sınıflı) · `analysis/scripts/sensitivity_delta.py`
- `araclar/duyarlilik-augmented-search-strings.md`, `araclar/duyarlilik-DELTA-DOGRUDAN-dizgeler.md`
- Ham export'lar: `analysis/raw_data/` (yerelde; repoya konmadı).

### Sıradaki adım (yeni/temiz oturumda)
12+7 adayın tam-metin uygunluk taraması → korpusa katılacak nihai liste + güncel PRISMA n'leri.
