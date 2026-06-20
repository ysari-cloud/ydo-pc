# Duyarlılık Testi — Delta Durumu ve Özet Not

**Durum: VERİ BEKLENİYOR (uydurma yapılmadı).** Bu testin iki girdisi de bu bulut ortamında
mevcut değildir: (1) artırılmış sorgu, WoS + Scopus'ta **kurumsal oturumla** çalıştırılmalıdır
(brif §10; bu DB'lere bulut ortamından/erişimsiz giriş yapılamaz), ve (2) mevcut 3.050'lik ham
korpus (`analysis/raw_data/`) repoya commit edilmemiştir, yalnız yerel PC'dedir. Bu nedenle gerçek
delta üretilemedi; sahte satır yazmaktansa boş şema bırakıldı.

## Tamamlamak için (yerel PC / cowork, kurumsal erişimle)
1. `araclar/duyarlilik-augmented-search-strings.md` içindeki **WoS** ve **Scopus** artırılmış
   dizgelerini çalıştır; çalıştırma tarihini not et.
2. Export'ları `analysis/raw_data/` içine koy: `wos_aug_1..N.txt`, `scopus_aug.csv`
   (orijinal `wos_broad_*.txt` + `scopus_broad.csv` de orada olmalı).
3. `python3 analysis/scripts/sensitivity_delta.py` → `analysis/sensitivity_delta.csv` otomatik dolar.
   Sütunlar: doi, title, year, journal, new_term_hit, relevant(boş→insan denetimi), modal(image?), recency.
4. CSV'yi (gerekirse `relevant` ve `recency` kolonlarını gözle denetleyip) commit et.

## Karar kuralı (delta geldikten sonra)
- **Delta önemsiz / ilgisiz** → "anahtar-kelime duyarlılık analizi yapıldı; sonuç sağlam" notu;
  PRISMA n değişmez.
- **Delta anlamlı (özellikle görsel/çok-kipli üretim alt-kümesi varsa)** → artırılmış A bloğunu
  kalıcılaştır, aramayı yeniden koş, PRISMA n'lerini güncelle, korpusu yenile.

> Script yalnız gerçek export'lardan okur; hiçbir kayıt elle uydurulmaz.
