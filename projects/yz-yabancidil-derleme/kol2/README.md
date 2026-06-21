# Kol-2 (Duyarlılık Kolu) — Tam-Metin Uygunluk Paketi

PRISMA 2020 iki-kollu tasarımda **Kol 2 = "diğer yöntemlerle bulunan kayıtlar"** (anahtar-kelime
duyarlılık taraması). Bibliyometrik korpus (3.050) DONUK kalır; bu kol senteze ek getirir.

## Akış
1. Duyarlılık taraması → 152 sınıflı kayıt (`../analysis/sensitivity_delta.csv`).
2. Dedup → **20 benzersiz** → başlık/öz ön-elemesi: `22-duyarlilik-uygunluk-on-eleme.md`.
3. Tam-metin erişim/temin: `23-tam-metin-erisim-listesi.md`, `Kol2_INDIRME_LISTESI.md`.
4. **Tam-metin uygunluk kararları (16 makale okundu): `24-tam-metin-uygunluk-kararlari.md`.**

## Nihai karar (24 numaralı dosya)
- **DAHİL = 12** (ampirik, EFL, gerçek GenAI): A01 A02 A03 A04 A06 A08 A09 A10 C01 C02 C04 C05.
- **SINIRDA = 1**: A05 (Gemini Storybook; materyal-üretim isabetli ama kavramsal/uygulama yazısı, ampirik değil) — kullanıcı kararı bekliyor.
- **DIŞLA = 4**: A07 (anadil/Endonezyaca, kapsam), B01 (Bard mizah, kapsam), C03 (Antik Yunanca AI-görsel, kapsam/odak), B02 (kitap bölümü, tür).
- Araç dağılımı (dahil): Gemini x4, Copilot x4, DALL-E/text-to-image x2, Claude x1, Grok x1.

## Tam metinler
Makale PDF'leri **repoya konmaz** (telif + `.gitignore` `pdf/`). Yerelde:
`makaleler/TAM_METIN_KOL2/<ID>_Yazar_Yil.pdf` (16 orijinal PDF). Zotero koleksiyonu: `YZ-YabanciDil-Derleme`.

## Siradaki adim
DAHIL 12(-13) kaydi C1-C8 (kodlama kitabi) ile kodla; PRISMA iki-kollu diyagrami guncelle (Kol 2 = +12); RQ4-RQ5 sentezine isle. Devir: `_DEVIR-2026-06-20.md`.
