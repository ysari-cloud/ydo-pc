# ydo-pc — Kalıcı Hafıza Deposu

Bulut Claude Code oturumları arasında hafızanın kaybolmaması için kullanılan depo.

Bulut konteyneri geçicidir (her sıfırlamada silinir). Kalıcı olan tek şey bu git
deposudur: buraya `commit + push` edilen her şey, sonraki oturumda repo yeniden
klonlandığında geri gelir.

## Yapı

- `CLAUDE.md` — oturum başında otomatik okunan talimat dosyası (hafıza nasıl kullanılır).
- `memory/`
  - `MEMORY.md` — tüm projelerin indeksi/haritası.
  - `project-almancaeskisehir.md` — ana site (almancaeskisehir.com) notları.
  - `marka-landing-akademie.md` — marka kanadı (almancaakademie.com) notları.

## Kullanım

Yeni oturum: Claude `CLAUDE.md`'yi okur → `memory/` dosyalarını yükler → kaldığı yerden
devam eder. Önemli değişikliklerden sonra `memory/` güncellenir ve push edilir.
