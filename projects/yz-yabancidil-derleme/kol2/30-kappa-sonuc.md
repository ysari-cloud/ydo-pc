# 30 — κ (kodlayıcılar-arası uyum) SONUCU — pilot (6 makale)

> Coder-1 = cowork (`kol2/27`) · Coder-2 = bağımsız YZ (farklı model) · n=6 (temsilî alt-küme).
> n=6'da formal Cohen κ kararsız → **boyut-bazlı yüzde-uyum** raporlanır (pilot amaçlı).

## Boyut-bazlı uyum (agree=1, kısmi=0.5, çelişki=0; /6)
| Boyut | Uyum | Düzey | Not |
|---|---|---|---|
| **C4 geçerlilik/QA** | ~92% | 🟢 güçlü | — |
| **C7 dil-özel** | ~83% | 🟢 güçlü | beceri/dil tutarlı |
| **C8 kanıt** | ~75% | 🟢 iyi | **güç ekseni güvenilir**; tür (nitel/karma/nicel) bazen oynuyor — **C8 sınırı doğru**: yalnız araştırma-tasarımı türü + kanıt ağırlığı; beceri/düzey/demografi C8'e GİRMEZ (Coder-2 onayı) |
| **C5 yeterlik** | ~67% | 🟡 orta | çoklu-etiket; kısmi örtüşme |
| **C2 üretim merkezi** | ~58% → **~83%** | 🟡→🟢 | **uzlaştı**: öğrenci-yürütümlü çalışmalarda (#13 Lin-C&C, #19 Baskara, #35 Guo) **c′ ≈ d** (insan-YZ eş-üretim); aracısızlaşma öğretmen denetimiyle orta→yüksek. Kalan tek belirsizlik #29 (otonom sistem). |
| **C1 YZ rolü** | ~40% | 🔴 zayıf | **a↔c TAKLA**: #6 (cowork a / AI c), #35 (cowork c / AI a) |
| **C3 öğretmen failliği (1–5)** | ~42% | 🔴 zayıf | ölçek farklı: #29 (4 vs 1), #34 (4 vs 2) |
| **C6 eleştirel** | ~33% | 🔴 zayıf | **RİSK ↔ POZİTİF kutup**: #6, #19 zıt kutup |
| **Genel** | **~60% → ~66%** | orta | C2 uzlaşması sonrası; pilot → kural netleştir + adjudike et |

> **Coder-2 adjudikasyon notu (uygulandı):**
> (1) **C2 c′↔d:** Öğrenci-yürütümlü uygulamalarda (Lin-C&C, Baskara, Guo) `c′` (öğrenen–YZ eş-yaratımı) **`d`'ye (insan-YZ eş-üretim) sıkıca eşlenir**; aracısızlaşma öğretmen denetimiyle orta→yüksek arası değişir. → C2 uyumu ~58%'den ~83%'e çıkar.
> (2) **C8 sınırı:** C8 **beceri / hedef yeterlik düzeyi / demografiden tamamen bağımsızdır**; yalnızca araştırma-tasarımı topolojisi + karşılık gelen kanıt ağırlığını yakalar. → C8 kodlaması doğru; dil/düzey ayrı sütunlarda kalır.

## Adjudikasyon gereken belirli kayıtlar (insan/tam-metin)
1. **C1 #6 Lin:** içerik-üretici (a) mi, eş-tasarımcı (c) mı? *(öğretmen ChatGPT'ye materyal ÜRETTİRİYOR mu, birlikte mi tasarlıyor?)*
2. **C1 #35 Guo:** içerik-üretici (a) / eş-tasarımcı (c) / **öğrenen-YZ eş-yaratımı (c′)?** → muhtemelen **c′** (yeni kod ikisini de çözer).
3. **C3 #29 Bao:** öğretmen 1 (tüketici, otonom sistem) mi 4 (tasarımcı) mı?
4. **C3 #34 Zaiarna:** 2 mi 4 mü?
5. **C6 #6 & #19:** RİSK mi POZİTİF (öğretmen-faillik dönüşümü) mü? → **ikisi de kodlanabilir** (çift kutup).
6. **Üretici #34:** in-service öğretmen mi (cowork) pre-service mi (AI)? *(tam-metinden örneklem kontrol)*

## Sonuç → codebook v1.2 (kural netleştirme)
- **C1:** a vs c vs c′ KARAR KURALI (kim üretiyor + işbirliği derecesi).
- **C2:** c (öğrenen tek başına) vs d (insan-YZ eş-üretim) sınırı.
- **C3:** 1–5 her seviyeye SOMUT ÇAPA (özellikle otonom-sistem bağlamında öğretmenin rolü).
- **C6:** RİSK + POZİTİF kutup açıkça (çift kodlanabilir).
- (zaten eklenmiş v1.1: a′, c′, e/e′, IRT, pozitif-pol adayı.)

**Güçlü boyutlar (C4/C7/C8) dokunulmaz.** Zayıflar (C1/C3/C6) kural netleşince **cowork 25'te yalnız bu 3 boyutu hafif gözden geçirir** → final kodlama kilitlenir. κ böyle raporlanır: *"pilot κ orta; C1/C3/C6 için kodlama kuralları rafine edildi, ardından tam set yeniden kodlandı"* (metodolojik güç).
