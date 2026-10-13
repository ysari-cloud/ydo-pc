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
git add memory/ && git commit -m "memory: <kısa özet>" && git push origin HEAD:claude/youthful-franklin-wszezx
```

Bu commit + push'u Claude kendisi yapar; kullanıcıya push işi bırakılmaz.

> ⚠️ Push edilmeyen hafıza, oturum kapanınca **kaybolur**. Önemli değişiklikten
> sonra commit + push etmek alışkanlık olmalı.

## ⚙️ Çalışma kuralları

- **TEK DAL KURALI (kullanıcı kararı, 2026-10-13):** Depoda yalnızca default dal
  `claude/youthful-franklin-wszezx` var ve tüm işler DOĞRUDAN buna commit + push edilir.
  Oturum sistemi farklı bir `claude/...` dalı atasa bile o dala push etme, yeni dal
  açma, PR açma. Yan dal oluşursa içeriği default'a alınıp dal silinir.
- Hafıza her yeni oturumda default daldan otomatik gelir.
- Sahte içerik/yorum üretme yasak; resmî sınav logoları kullanılabilir (kullanıcı onaylı).

## 📌 Ortam notu

- Bu bulut ortamından WordPress'e doğrudan REST erişimi **ağ politikasına** bağlıdır
  ("Default" profil kısıtlı olabilir). Operasyonel WP işleri çoğunlukla kullanıcının
  **yerel PC'sindeki** Claude Code ile yürütülüyor; bu depo ortak hafıza/araç eviidir.
