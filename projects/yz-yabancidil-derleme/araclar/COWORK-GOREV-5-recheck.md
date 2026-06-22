# COWORK GÖREVİ 5 — Hedefli re-check (fazla-budama + generative + geri-alma)

> Cloud denetimi (kol2/25) sonrası. **Tek karar kuralı:** GenAI ile **somut bir öğretim artefaktı**
> (materyal / değerlendirme-sınav / ders planı / içerik / kompozisyon / podcast / kart / görsel) **ÜRETİLDİYSE
> → İÇERİ** — çıktı/etki/algı da ölçülmüş olsa bile. Yalnız **kullanım** (pratik/konuşma/feedback/tutum/
> beceri-etkisi) ve **somut artefakt YOK** → E4 DIŞARI. "Üretim çalışmanın merkezi mi?" SORMA; "artefakt
> üretildi mi?" SOR.

## A) Fazla-budama re-check (6) — tam metinden "artefakt üretildi mi?" (E/H)
15b'de "üretim" kodlanmış ama Görev-4'te E4'e taşınmış. Her birini bu testle yeniden değerlendir:
| # | Yazar | Soru (tam metinden) |
|---|---|---|
| 34 | Zaiarna 2024 | ChatGPT ile somut **değerlendirme/sınav (test/rubrik/quiz) artefaktı** üretildi mi? |
| 40 | Lee 2023 | AI ile somut **içerik/materyal** üretildi mi? |
| 7 | Lenko-Szymanska 2026 | Aday öğretmenler korpus+GenAI ile somut **ders/materyal** ürettiler mi? |
| 23 | Wu 2025 | GenAI ile somut **dinamik öğretim materyali** üretildi mi? |
| 21 | Liu 2025 | GenAI ile somut **materyal** üretildi mi, yoksa sadece entegrasyon/görüş mü? |
| 12 | Bataineh 2026 | AI ile somut **öğretim materyali** tasarlandı/üretildi mi? |
→ "Evet" olan → **İÇERİ** (üretici etiketi + artefakt türüyle). "Hayır, sadece kullanım/algı" → **E4 kalır.**

## B) Generative-eksen teyidi (1)
| 15 | Shen 2025 | Kullanılan model **üretken mi (GPT/LLM/üreten)** yoksa **BERT (encoder)** tabanlı mı? **BERT-only ise generative DEĞİL → DIŞARI (E3-benzeri).** |

## C) B-grubu artefakt-vs-algı (2)
| 18 | Lo 2025 | Somut materyal üretildi mi yoksa sadece algı/refleksiyon mu? |
| 32 | Williyan 2024 | Somut içerik/materyal üretildi mi yoksa sadece görüşme/algı mı? |
(29 Bao = İÇERİ kesin; bunlar kalan ikisi.)

## D) Geri-alma temin + teyit (2) — önce İNDİR (yerel PDF yok)
| 19 | Risang Baskara 2024 | indir → öğrenci **podcast artefaktı** üretildi mi? |
| 35 | Guo 2026 | indir → insan-LLM **yaratıcı yazma artefaktı** üretildi mi? (Almanca) |

## E) Veri bütünlüğü (1)
| 39 | Nguyen P.T. 2024 | PDF **doğru makale mi**? Öz = Çince-karakter öğretim sistemi ama gövde = sürdürülebilirlik anketi görünüyor → **yanlış dosya mı**? Doğru PDF'i bul/teyit et; uyuşmuyorsa DIŞLA. |

## Çıktı (push)
- `kol2/26-recheck-sonuclari.md` — her madde için karar (İÇERİ/E4/E3/DIŞLA) + tam-metin kanıt cümlesi.
- `kol2/25`'i güncelle: nihai DAHİL listesi + güncel **N**.
> Not: C04 = kullanıcı mührü bekliyor (cloud oyu: İÇERİ). Onu "SINIR" bırak.

---

## EK (2026-06-21) — #39 kararı + PREDATORY dergi taraması

### #39 Nguyen P.T. → **DIŞLA (karar verildi)**
- Doğru PDF (6269) teyit edildi: ChatGPT ile **Çince-L2 ders planı/materyal üretimi** → içerik 4 kriteri geçiyordu.
- **AMA dergi = JIPD (EnPress):** 17 Ocak 2025'te **Scopus'tan ÇIKARILDI** (predatory pattern: 1.200+ makale/yıl, yüksek APC), **WoS'ta yok.** → **#22 Wardat ile tutarlı → DIŞLA** (dergi/indeks+kalite). Sebep içerik değil, dergi.

### YENİ — predatory/discontinued dergi taraması (önemli, korpus bütünlüğü)
JIPD Scopus'taydı (2024'e dek) ve yılda 1.200+ basıyordu → aramamız Scopus'u taradığı için korpusta başka JIPD/EnPress kaydı olabilir.
1. **Sentez setindeki** tüm DAHİL kayıtların **dergilerini kontrol et:** JIPD veya başka **Scopus-discontinued/predatory** dergi (özellikle EnPress) var mı? Varsa #22/#39 mantığıyla **DIŞLA.**
2. **Geniş 3.050 korpusta** kaç JIPD / predatory-discontinued kayıt var? **Listele** → bibliyometriden temizle ya da en azından **sınırlılık** olarak raporla (predatory şişme riski; özellikle AS1 yayın-hacmi ve kaynak-dağılımını bozabilir).
- Çıktı: `kol2/26-recheck-sonuclari.md`'ye **"Predatory tarama"** bölümü + etkilenen kayıt listesi + temizlenmiş n.
