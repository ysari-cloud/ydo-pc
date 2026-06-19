# Cloud Denetim Raporu + Yönerge — Aşama 2 bibliyometri (2026-06-19)

> Rol: cloud = denetim/yönlendirme (yazmaz). Cowork Aşama-2 çıktısı (`analysis/`) denetlendi.

## ✅ GÜÇLÜ — onaylanan
- **Bütünlük örnek düzeyde:** sha256 manifest, tarih damgalı script arşivi, κ UYDURULMAMIŞ
  (nihai n insana bırakılmış), eş-atıf yalnız WoS `CR` (Scopus refs dışlanmış — doğru).
- **PRISMA sayıları tam ve tutarlı:** geniş 4.760→dedup→3.054→retracted 4→**3.050**; odaklı
  477→**329**→ön-uygun **223**→öncelik **40**→köprü **16**→insan-set **56**. Arama tarihi 2026-06-19.
- **Yıl dağılımı (AS3 açık sorusu çözüldü):** 2018-21=72(%2,4) · 2022-23=246(%8,1) · 2024-26=2.732(%89,6).
  Yorum doğru: "doğuş anındaki hızlı çerçeve kayması"; 2024 öncesi taban 318(%10,4) dengesiz, dikkatle.
- **Performans güvenilir:** ülke (Çin 957/ABD 391/…/Türkiye 121) ilk-10 elle doğrulanmış; kaynaklar
  System 66 + CALL 59 (= dergi merdivenimizin tepesi — hedef seçimini doğruluyor).
- **SliceKeywords nitel olarak kaymayı BAĞIMSIZ destekliyor:** 2018-21 = chatbot/conversational agent
  (konuşma); 2024-26 = chatgpt/generative AI/LLM + writing/academic writing/educational technology
  (üretim/çıktı). Bu, kusurlu sözlükten BAĞIMSIZ kanıt — tez büyük olasılıkla DOĞRU.

## 🔴 KRİTİK DÜZELTME — AS3 çerçeve niceliği (yazıma girmeden ÖNCE)
`run_full.py` satır 207–213 `CONV_LEX`/`PROD_LEX` kirli; manşet bulguyu yapay üretiyor:
1. **`'generative'` PROD_LEX'te → en baskın hata.** 2024-26'da "generative artificial intelligence"
   588 kez geçiyor; bu terimi içeren her kayıt üretimle ilgili olmasa da "üretim" sayılıyor.
   1037 üretim kaydının büyük kısmı bu yüzden şişmiş olabilir. **`'generative'` ÇIKARILMALI.**
2. **Jenerik PROD terimleri:** `tool, development, design, creation, automatic, automated` →
   çıkar veya üretim-özel hâle getir (materials development, content creation/generation, courseware,
   lesson plan, instructional design, test/item/question generation, authoring).
3. **CONV substring hatası:** `oral` → "behavioral/temporal" yanlış pozitif. `interaction, voice,
   listening, speaking` jenerik. Konuşma-özel bırak (chatbot, conversational agent, dialogue system,
   intelligent tutoring, spoken dialogue, voice/virtual assistant, pronunciation, conversation practice).
4. **Eşleştirme:** substring yerine **kelime-sınırı / tam-keyword** eşleşmesi kullan.

### Yapılacak (cowork)
- Sözlükleri temizle (yukarısı) → **AS3'ü yeniden çalıştır** (Table 11 + fig11 yenilensin).
- **Sözlükleri manuscript Appendix'ine** koy (şeffaflık — hakem ister).
- **Duyarlılık (sensitivity) kontrolü:** sözlüğün makul varyasyonlarında kayma yönü korunuyor mu?
  (1 paragraf rapor; korunursa AS3 sağlamlaşır.)
- **Payda netliği:** Conv%+Prod% 100 etmiyor (kategoriler örtüşebilir, ~%40 sınıfsız). Metinde
  "çerçeve-özel anahtar sözcük taşıyan belgelerin payı; kategoriler münhasır değil" de.

> Not: Düzeltme sonrası kayma yönü büyük olasılıkla KORUNUR (SliceKeywords bağımsız destekliyor),
> ama nicel değerler değişecek. Temiz sayı çıkana dek AS3'ün niceliği yazıya GİRMEMELİ.

## ⏭️ Sıradaki adımlar
- **Cowork:** AS3 temiz yeniden-çalıştırma → sonra Bulgular-Bibliyometri'yi yaz (08 + tablolar).
  (Diğer tablolar — performans, ağlar, PRISMA — temiz; onlar şimdi yazılabilir.)
- **Kullanıcı (insan):** 56'lık set (40+16) tam-metin uygunluk doğrulaması + 2. tarayıcı → Cohen κ.
- **Cloud:** taslak gelince atıf bütünlüğü (DOI tek tek) + dergi indeks/çeyreklik son teyidi.

## 🔐 Güvenlik
- Push için kullanılan **GitHub token'ı GitHub'da REVOKE et** (bir kez ifşa oldu; gerektiğinde yeniden üret).
