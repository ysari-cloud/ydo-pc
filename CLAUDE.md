# Kalıcı Hafıza Deposu

Bu depo, **bulut Claude Code oturumları arasında kalıcı hafıza** tutmak içindir.
Bulut konteyneri her oturum/sıfırlamadan sonra silinir; **yalnızca bu git deposuna
commit + push edilenler kalıcıdır.** Hafıza buradan beslenir.

Kullanıcı: Doç. Dr. Yunus Emre Sarı (`y.sari@iuc.edu.tr`). Dil: **Türkçe**.

## 🟢 OTURUM BAŞINDA — her zaman yap

`memory/` klasöründeki dosyaları oku (önce indeks):

1. `memory/MEMORY.md` — indeks / tüm projelerin haritası (ÖNCE bunu oku)
2. `memory/project-almancaeskisehir.md` — ana site (almancaeskisehir.com) operasyon notları
3. `memory/marka-landing-akademie.md` — marka kanadı (almancaakademie.com)

## 🔵 OTURUM BOYUNCA / SONUNDA — hafızayı koru

Önemli bir karar, ilerleme veya yeni "ders" oluştuğunda **ilgili `memory/*.md`
dosyasını güncelle**, sonra mutlaka kaydet:

```bash
git add memory/ && git commit -m "memory: <kısa özet>" && git push -u origin <dal>
```

> ⚠️ Push edilmeyen hafıza, oturum kapanınca **kaybolur**. Önemli değişiklikten
> sonra commit + push etmek alışkanlık olmalı.

## ⚙️ Çalışma kuralları

- Geliştirme dalı: `claude/youthful-franklin-wszezx` (kullanıcı aksini söylemedikçe).
- Hafızanın HER yeni oturumda otomatik gelmesi için bu dosyaların deponun
  **varsayılan (default) dalında** olması gerekir — feature dalı merge edilince sağlanır.
- Sahte içerik/yorum üretme yasak; resmî sınav logoları kullanılabilir (kullanıcı onaylı).

## 📌 Ortam notu

- Bu bulut ortamından WordPress'e doğrudan REST erişimi **ağ politikasına** bağlıdır
  ("Default" profil kısıtlı olabilir). Operasyonel WP işleri çoğunlukla kullanıcının
  **yerel PC'sindeki** Claude Code ile yürütülüyor; bu depo ortak hafıza/araç eviidir.
