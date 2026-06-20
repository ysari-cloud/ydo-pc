# TEMİZ Keyword Duyarlılık Delta'sı (as-run B bloğu) — Özet

**Tek düzeltme:** B bloğunda **çıplak L2/CALL kaldırıldı** (as-run korpusla aynı, bkz.
`araclar/ARAMA-DIZGELERI-FINAL-as-run.md`); araç terimlerinde **Llama/Bard/Grok/Claude** domain-gürültüsü
olarak elendi (yalnız gerçek araç örnekleri — "Bard-generated", "Grok as an AI" — tutuldu).

## Yöntem (şeffaflık)
Temiz delta, önceki 152 kayıtlık doğrudan-delta setinin **as-run kriterleriyle yeniden süzülmesiyle**
elde edildi (clean B ⊆ broad B; gerçek-ilgili araç eşleşmeleri korundu). Gürültü kayıtları yalnızca
(temiz-araç-terimi **VE** as-run-B-dil-terimi) içeriyorsa tutuldu; sadece Llama/L2/CALL/özel-ad ile
gelenler düştü. WoS özetleri (tam kayıt) ve Scopus başlıkları tarandı. *Sınır:* görevin tuttuğu jenerik
terimler ("image generation/AI-generated/generative model") tam canlı koşuda birkaç ek **CS/ML** kaydı
daha yüzeye çıkarabilir (düşük ilgi; aşağıdaki 9 kalıntı gürültü bu türden) — ama **ilgili sonuç değişmez.**

## Özet (1 paragraf)
As-run B bloğuyla temizlenince delta **152 → 31 kayda** indi ve gürültü **130 → 9'a** çöktü (−121);
düşen kayıtların ezici çoğunluğu, çıplak "L2/CALL" ve "Llama" (= LLAMA dil-yatkınlık testi) üzerinden
gelen dil-yatkınlık/çalışma-belleği makaleleriydi — yani önceki gürültü büyük ölçüde **yanlış B bloğundan**
kaynaklanıyordu. Kritik olarak, daha önce saptanan **12 kesin ilgili makalenin tamamı** bu temiz sette de
**aynen duruyor** (Gemini ×5, Copilot ×3, Grok ×1, Bard ×1, text-to-image ×1, AI-üretimi geri bildirim ×1);
~7 sınırda kayıt da korunuyor; 1 RETRACTED (Poe/Gemini) dışlanır. Kalan 9 "gürültü", jenerik üretim
terimleriyle eşleşen CS/ML çalışmalarıdır (VIDLANKD, CLIP, Nonword-to-Image vb.) ve tam-metin elemede
kolayca dışlanır. **Hüküm değişmiyor:** araç adları korpusu kökten değiştirmiyor; doğrulanmış **12 ilgili**
makale PRISMA "diğer yöntemlerle bulunan kayıtlar" yolundan tam-metin uygunluğa alınacak; bibliyometrik
3.050'lik korpus DONUK kalır. Arama faslı kapanır.

## Sayılar
| | Önceki (broad B, kirli) | TEMİZ (as-run B) |
|---|---|---|
| Toplam delta | 152 | **31** |
| Kesin ilgili (Y) | 12 | **12** (hepsi korundu) |
| Sınırda (?) | ~7 | ~7 |
| Retracted | 1 | 1 |
| Gürültü (N) | 130 | **9** |

Çıktı: `analysis/sensitivity_delta_CLEAN.csv` (doi,title,year,journal,new_term_hit,relevant,modal,retracted).
