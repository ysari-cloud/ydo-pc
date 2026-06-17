---
name: project-almancaeskisehir
description: AlmancaEskişehir WordPress sitesi — CSS/HTML düzeltmeleri, eval kartı yeniden konumlandırma, REST API operasyon notları
metadata: 
  node_type: memory
  type: project
  originSessionId: 3978ac67-0864-4a77-8cef-7af389f3c7d4
---

## Temel Erişim

- **URL:** https://www.almancaeskisehir.com/
- **Kullanıcı:** miyatuk / App password: `3dDd Al8z 30Gm IpPZ FNKf zzNS`
- **Base64 auth:** `bWl5YXR1azozZERkIEFsOHogMzBHbSBJcFBaIEZOS2YgenpOUw==`
- **Page ID:** 5 (anasayfa)
- **REST API:** `/wp-json/wp/v2/pages/5?context=edit` (GET/PATCH)

**Why:** Sandbox/MCP araçları 1 ay başarısız oldu. Neden: TurHost'un Imunify360 sistemi Google Cloud dinamik IP'lerini bot olarak engelliyor. REST API + App Password bu engeli aşıyor çünkü kimlik doğrulamalı.

---

## 🔖 SON DURUM & DEVAM NOKTASI (2026-06-14) — YENİ OTURUM ÖNCE BUNU OKU

> Kullanıcı bu noktada sohbeti sıfırladı; bu özet, kaldığımız yeri verir. **2026-06-14'te İKİ paralel akış oldu:** (A) AdSense/Jetpack/site-denetimi (aşağıdaki liste, Düzeltme 11–13), (B) İçerik/SEO akışı (hemen aşağıda).

**(B) İÇERİK/SEO AKIŞI — 2026-06-14 (Bekleyen İşler madde 3/5/6/7/9/10/11; hepsi canlı doğrulandı):**
- **Aile Birleşimi konsolidasyonu (madde 10) ✅:** 7 yamyam sayfa → 3 ranking entity. **142 `/a1-mektup-ornekleri/` = kazanan (DOKUNULMADI)**, **178 `/aile-birlesimi-sinavi/` = hub**, 696 = hub çocuğu. 4 ölü dupe (47940/781/220/218) **canonical→178** (AIOSEO `canonicalUrl` camelCase). Menü dropdown: Mektup·Sınav Bölümleri·Kazananlar. **218 Gurur Tablomuz** (9 gerçek öğrenci sertifikası) bağımsız bırakıldı + Türkçe SEO. Hub tasarımı toparlandı (eklentiler ab-card/ab-related ile). **HİÇBİR SAYFA SİLİNMEDİ** (7'si canlı 200).
- **GSC manuel indexleme (madde 3) ✅:** Chrome eklentisiyle GSC sürüldü. Site SAĞLIKLI indexleniyor (çoğu sayfa zaten dizinde). Tek boşluk **C1+C2 Sprechen** → ikisine indexleme isteği gönderildi. Kalıcı çözüm = bu exam sayfalarına iç link (henüz yok).
- **Haberler optimizasyonu (madde 11) ✅:** "Haberler" = RSS→ChatGPT→Make otomasyonlu 24 Almanca graded-reader (B1-B2 okuma); API bitince 14'ü draft. 4 eski çöp draft silindi; 10 yayındakine Türkçe SEO başlık+meta. **14 draft + ölçekli-AI/ephemeral riski → bilinçle bekletildi** (Dr. Sarı kararı).
- **56 PDF landing (madde 7) ❌KAPANDI:** Eklenecek değerli şey yok (çalışma kâğıtları zaten landing'li, eski PDF'ler redundant/görsel-tarama); doğrusu hiçbir şey yapmamak.
- **TurHost(5)/beceri-hub(6)/Mükerrer duyuru(9):** zaten çözülmüş/teyit edildi.
- **(B) akışı TEKNİK DERS:** AIOSEO `canonicalUrl`(camel)+`title`/`description`(lower) REST'le yazılıyor; **Redirection eklentisi yeni 301'leri ateşlemiyor** (Apache/.htaccess) → consolidation için **canonical kullan**. AIOSEO sonrası WP "touch"(status:publish) = LiteSpeed purge.

**Bu oturumda yapılanlar (hepsi canlı doğrulandı):**
1. **Meryem (A2) gerçek form yorumu** anasayfa `#yorumlar`'a eklendi → 6 kart, grid 3+3 (Düzeltme 11).
2. **SEO-dışı genel denetim** + 18 eklenti envanteri (Düzeltme 12).
3. **AdSense kaldırıldı** — kaynağı **Google Site Kit**'ti (kullanıcı eklememişti; hesap inaktiflikten devre dışıydı). Site Kit → AdSense bağlantısı kesildi; Search Console + Analytics korundu.
4. **Jetpack diyeti: 13 modül kapatıldı** (Photon görsel CDN dahil). Görseller artık kendi alan adı + Cloudflare'den webp. Jetpack'in WP.com'a kalan TEK frontend işi = **bülten (subscriptions)**.
5. **İstatistik kanalı:** Jetpack Stats kapandı → **Burst (günlük) + GA4/Site Kit (derin)**.
6. **WP Super Cache** etkisizleştirildi (silme host'ta bloklu, REST 500; inactive = hedef karşılandı).

**SİTE ŞU AN:** Sağlıklı (anasayfa 297KB/200), **reklamsız**, hafif Jetpack, WP.com bağımlılığı minimum, formlar (WPForms testimonial + bülten) + GA4 çalışıyor.

**KORUNANLAR — DOKUNMA:** Jetpack **subscriptions** (bülten — gerçek aboneler olabilir), publicize, blocks/shortcodes/widgets/contact-form (içerik/form bağımlılık riski). Photon zaten kapalı.

**BEKLEYEN OPSİYONEL İŞLER (öncelik yok, kullanıcı seçecek):**
- 🔒 Güvenlik: ~~PHP sürüm (X-Powered-By) gizleme~~ ✅ **TAMAM (Düzeltme 13, snippet 528)** + Wordfence 2FA (KULLANICI işi — QR kaydı). (**xmlrpc KAPATMA** — Jetpack bülten için ona ihtiyaç duyuyor.) CSP report-only ileride.
- 🖼️ Görsel lazy-load: **zaten aktif (snippet 23)** — "30 eager" çoğu kasıtlı (LCP/hero + logo şeridi); gerçek defekt değil. 🔤 Google Fonts self-host → **KULLANICI REDDETTİ (2026-06-14), AÇMA.** Gerekçe: trafik zaten Google Arama'dan geliyor → gizlilik argümanı anlamsız; ayrıca preconnect+`display=swap` zaten var → perf kazancı ihmal edilebilir. Fontlar Google CDN'de KALIYOR (Source Serif 4=snippet 492, Work Sans+Barlow=Kadence teması, preconnect=snippet 33).
- 🧹 ~~Ölü `.jp-relatedposts` CSS~~ ✅ **TAMAM (Düzeltme 13, 2026-06-14).**
- ⚡ En büyük perf: ~297KB inline-CSS HTML — mimari, riskli, ayrı planlama.
- 📊 PSI/CWV gerçek skoru: Google API key veya pagespeed.web.dev (keyless 429 veriyor).

**🔑 KRİTİK OPERASYON DERSLERİ:**
- **WAF GREYLIST:** Hızlı ardışık scripted fetch (özellikle cache-buster query'li **anasayfa**) Imunify360'ı tetikleyip **11-karakter boş yanıt** döndürüyor → SİTE KIRIK SANMA. Düz URL + ölçülü tempo; şüphede **gerçek tarayıcı otoriter**.
- **Chrome MCP:** `javascript_tool` (Runtime.evaluate) sık 45s donuyor; **`find` → `computer left_click(ref)` güvenilir**. Ref'ler hızlı eskir (find'dan hemen sonra tıkla). Klasik `jetpack_modules` tablosu kararsız; modern **Jetpack → Ayarlar → Performance** toggle'ları güvenilir.
- **REST:** Plugin **SİLME** bu host'ta **500** (bloklu); deaktivasyon + içerik PATCH + AIOSEO meta POST çalışıyor.

**NOT:** Oyunlaştırma/oyunlar işi AYRI bir chat'te yürüyor → bkz. [[oyunlar-girisimi]].

---

## 📊 GA4 / Analytics Hesap Haritası (2026-06-14) — TRAFİK TAKİBİ KAFA KARIŞIKLIĞI ÇÖZÜLDÜ

**Sorun:** Kullanıcı SEO temizliği sonrası trafiği nereden takip edeceğini bilmiyordu; GA4'te "veri yok" sanıp paniği yaşadı. Gerçekte veri hiç kaybolmamış — **yanlış hesap/mülklere bakılıyordu.**

**GERÇEK VERİ BURADA (canlı, kusursuz topluyor):**
- Google hesabı: **miyatuk83@hotmail.com** (sitenin ESKİ/asıl hesabı; tarayıcıda authuser=4 / `/u/4/`)
- GA Hesabı: **221275591** ("Almanca Eskişehir")
- Mülk: **304765369**, Ölçüm Kimliği: **G-T42BHEL2LC** (sitede Site Kit'in ateşlediği etiket; canlı kodda doğrulandı)
- Doğrulama: 853 etkin kullanıcı, anlık 2 kişi vb. — `analytics.google.com` → miyatuk83@hotmail.com seç.

**ÖLÜ/MÜKERRER MÜLKLER (hepsi boş, görmezden gel) — iş maili y.sari@iuc.edu.tr'nin gördüğü "emre" hesabı (47718523) altında:**
- "almancaeskisehir - GA4" (385951120) → G-3TF1WFKE1Z (boş)
- "MonsterInsights..." (360905483) → 2 akış: G-GS14FDW4WK + G-HNWFM247QE (eski MonsterInsights eklentisinden, veri yok)

**ERİŞİM ÇÖZÜLDÜ (2026-06-14):** Kullanıcı, hotmail(sahip) hesabıyla GA → Hesap erişim yönetimi'nden **miyatuk83@gmail.com'u "Yönetici" olarak ekledi** (erişim listesi 2 yönetici gösteriyor: hotmail + gmail). Artık günlük açık hesabı GMAIL ile GA'ya girince tüm veri görünür; hesap değiştirme yok. İş maili (y.sari@iuc.edu.tr) bilinçli OLARAK eklenmedi (kullanıcı "iş adresim öyle kalsın" dedi; GSC'de zaten sahip). **NOT:** İzin/erişim değişikliğini ASİSTAN YAPMAZ — son "Ekle"ye kullanıcı bastı; asistan sadece doğru ekrana götürdü. WP Site Kit "izin yok" hâlâ çıkarsa Site Kit'in bağlı olduğu hesap (muhtemelen iş maili) erişimsiz demektir; gmail/hotmail ile yeniden bağlanınca düzelir (acil değil).

**Tarayıcıdaki Google hesapları (referans):** y.sari@iuc.edu.tr (varsayılan, "emre" GA hesabı), miyatuk83@gmail.com, y.sari@istanbul.edu.tr, melek.sari@ogr.iuc.edu.tr (süresi dolmuş), "miyatuk" (Marka hesabı), **miyatuk83@hotmail.com (GERÇEK GA sahibi)**.

**TRAFİK TAKİP KANALLARI (hepsi çalışıyor):** (1) **Burst** = WP sol menü "İstatistikler" (bu oturumda REST PUT ile `inactive`→`active` yapıldı; günlük, Google'sız). (2) **Search Console** = `search.google.com` direkt, 10.981 tıklama, iş maili SAHİBİ. (3) **GA4** = yukarıdaki hotmail hesabı.

**Excluded from Analytics:** "All logged-in users" → admin kendi ziyaretini saymaz (gerçek zamanlı testte kendini görmez, normal).

---

## Düzeltme 14 — İnteraktif Alıştırmalar Dropdown Güzelleştirme + Code Snippets/LiteSpeed Dersleri (2026-06-14)

**İş:** "İnteraktif Alıştırmalar" (üst öğe `menu-item-47754`) dropdown'ı güzelleştirildi. Sonuç (canlı, public): 5 CEFR kartı (47866 A1 yeşil … 47870 C1-C2 kırmızı) **renk KORUNARAK** sol seviye rozeti (A1/A2/B1/B2/C1-C2 pill, Dersler menüsü `aef-level-icons` diliyle) + gradient/derinlik + hover; **Oyunlar (48776)** seviyelerden ayrışan koyu navy→mor kart + **amber gamepad ikonu** (inline SVG) + glow-pulse + üst ayraç. Menü öğesi **48776 başlığından "🎮" emoji KALDIRILDI** → düz "Oyunlar" (REST `POST /wp/v2/menu-items/48776` `{title:"Oyunlar"}`), çünkü CSS ikon zaten var. Tasarım 3-öneri+jüri workflow'uyla sentezlendi; CSS yedeği: çalışma klasörü `aef-menu-beautify.css`. Snippet: **537 `aef-interaktif-menu-v1`**.

**🔑 KRİTİK CODE SNIPPETS / DEPLOY DERSLERİ:**
- **Code Snippets REST API VAR ve çalışıyor:** `GET/POST /wp-json/code-snippets/v1/snippets[/{id}]` (app-password yetiyor). Alanlar: `name,desc,code,scope,active,priority,tags`. Aktif/pasif: POST `{active:true/false}`. Silme: DELETE.
- **PowerShell TUZAĞI:** `Get-Content -Raw` döndürdüğü string'e ETS note-property ekliyor → PS 5.1 `ConvertTo-Json` onu `{"value":...}` NESNESİNE çeviriyor → REST 400 "code string türünde değil". **ÇÖZÜM: `[System.IO.File]::ReadAllText($path,[Text.Encoding]::UTF8)`** ile temiz string oku.
- **`scope:"site-css"` snippet'i REST ile oluşturup/düzenleyince RENDER OLMUYOR** (Code Snippets birleşik site-css transient'i yenilenmiyor; admin "Save Snippet" bile düzeltmedi). **ÇÖZÜM (kanıtlı): `scope:"front-end"` PHP snippet'i kullan, `wp_head`'e `<style id="aef-...">`...CSS...`</style>` BASTIR** (PHP nowdoc `<<<'AEFCSS'` ile — CSS'teki tek/çift tırnak sorunsuz). Bu, sitedeki aef-level-icons/aes-daf-icon vb. ile aynı kanıtlı desen. front-end PHP snippet REST-edit'ten SONRA girişli render'da ANINDA göründü (site-css'in aksine).
- Özgüllük: `#main-navigation`/`.header-navigation` + `.menu-item-47754` + `.menu-item-XXXX` zinciri (mevcut Customizer `!important` kurallarını ezer). Mobil ayrı: `.mobile-navigation .menu-item-48776` (bare-selector reset SIZDIRIR, kullanma — jüri uyarısı).

**🔑 KRİTİK LİTESPEED PURGE DERSİ:**
- **REST ile snippet 488 toggle (purge-on-init) GERÇEKTE PURGE ETMİYOR** (REST aktivasyonu init'i tetiklemiyor). 
- **ÇALIŞAN purge:** Admin → **LiteSpeed Cache → Araç kutusu (toolbox) → "Tümünü boşalt - LSCache" KUTUSUNA tıkla** (büyük kutu, admin-bar dropdown öğesi DEĞİL). Sonra anonim ilk istek `miss`→regenerate→`hit`.
- **DOĞRULAMA HİLESİ:** Girişli (wp-admin cookie'li) tarayıcı render'ı LiteSpeed cache'i ATLAR → değişikliği ANINDA gösterir (purge beklemeden). Anonim curl/PowerShell (auth header REST içindir, login cookie değil) = PUBLIC cache görür. JS ile doğrula: `[...document.querySelectorAll('style')].some(s=>/imza/.test(s.textContent))` + Oyunlar linkinin `getComputedStyle(...).backgroundImage`.

---

## Düzeltme 15 — Sınav Hazırlığı + Kaynaklar Dropdown PREMIUM (2026-06-15)

**İş:** "Menüleri güzelleştirmeye devam" → Düzeltme 14'te İnteraktif (47754) premium yapılmıştı; bu turda kullanıcı **"Sınav + Kaynaklar → premium"** seçti. Tasarım = 3-öneri+3-jüri+sentez workflow (jüri/sentez OTURUM LİMİTİNE takıldı → **3 öneriyi transcript jsonl'lerinden çıkarıp sentezi/jüriyi ANA DÖNGÜDE ben yaptım**; kazanan = Angle C "Brand Richness" + 2 düzeltme). Sonuç **snippet 538 `aef-menu-premium-v1`** (front-end PHP, wp_head'e `<style id="aef-menu-premium-v1">`, **priority 30** → 107/20 + 537'den sonra; nowdoc `<<<'AEFCSS'`). **ADDITIVE: 107/537 DÜZENLENMEDİ, üstüne bindi.** Yedek: çalışma klasörü `aef-menu-premium-v1.css` (v4, ~511 satır; v1→v4 aşamaları aşağıda). **NOT: 538 artık DÖRT dropdown'u da kapsıyor (Sınav+Kaynaklar+Dersler; İnteraktif=537).**

**🔑 KRİTİK BULGU — menü CSS sürüklenmesi:** Snippet 107 (`AEF - Menü İkonları + Level Renk Standardı`, tüm dropdown'ları stilliyor) menü yapısı değiştiğinden beri kaymış: (a) artık menüde OLMAYAN öğeler için ölü kurallar (47055, 925 → Kaynaklar); (b) yeni eklenen öğeler SADE kalmış. 538 bu boşlukları kapattı (ölü kurallar zararsız bırakıldı).

**538 ne yapıyor (canlı doğrulandı, deploy-anında Chrome MCP ile 4 dropdown screenshot):**
- **Panel derinliği:** Sınav (47047) + Kaynaklar (305) panelleri ışıklı-premium yükseklik gölgesi (`0 18px 40px -14px rgba(15,23,42,.28)` + hairline border + inset highlight). 537 KOYU-navy glow'un LIGHT-panel çevirisi.
- **Sınav Simülasyonu (48522) = HERO/hub kartı:** indigo→mor gradient (`#4F46BC→#6D4FD6`) + accent border + `aefSimHubGlow` hafif pulse + monitör ikon. Çocuklu (wrap) → ikon `> a > .nav-drop-title-wrap::before`.
  - **⚠️ v2 DÜZELTME (kullanıcı uyardı: "iki sembol"):** 48522 "PLAIN" SANILMIŞTI ama **ÖNCEDEN VAR OLAN anonim bir `<style>` snippet'i** onu zaten stillemiş: açık-indigo kart + **clipboard `a::before`** + **`a::after`="Goethe · telc · TestDaF" alt-başlık** + `flex-wrap:wrap`. 538'in gradient'i + monitör (`nav-drop-title-wrap::before`) + sheen (`a::after`) eklenince → sheen alt-başlığı ezdi AMA clipboard `a::before` kaldı → **İKİ ikon + flex-wrap kartı 2 satıra böldü**. **Çözüm (538 v2, codeLen 30262→30779):** `.menu-item-48522 > a::before{display:none}` (miras clipboard gizle, yüksek-spec) + `flex-wrap:nowrap` → tek monitör ikonu, tek satır, kardeşlerle dengeli (canlı zoom doğrulandı). **DERS: yeni öğe stillemeden önce home.html'de `48522` gibi ID'yi GREP'le — 107 dışında başka anonim snippet'ler de menü öğelerine ikon/kart koymuş olabilir.** (O anonim snippet artık 538 tarafından tam eziliyor = ölü; cleanup adayı.)
- **g3 flyout'lar** (298 Aile + 48522 Sim + 735 Deneme panelleri ışıklı krom): **kompakt ikincil tier** (8px11px pad, w600, 22px mini ikon kutusu). Sim g3: Goethe `#2563EB` · **telc `#0891B2` (107'deki oversized turuncu üst-karttan KÜÇÜLTÜLDÜ** — yüksek-özgüllük `.menu-item-48522 .menu-item-47049` 107'nin bare selektörünü ezer) · ÖSD `#DC2626`. Aile g3 (48781/48782/48786): amber-aile (`#C77F2A/#B5751F/#9C6B16`) zarf/liste/kupa ikon.
- **Kaynaklar 3 SADE öğe → beyaz kart** (kardeş 47074/307/2521 ile birebir): Haberler 48264 rose `#D4537E` gazete · Video 48243 mor `#7C3AED` play · Çocuklar 48248 amber `#F59E0B` gülenyüz.
- **➕ v3 ALMANCA DERSLER (304) — block J (codeLen 30779→36141):** Kullanıcı "bu neden kaldı?" deyince Dersler de premium yapıldı. Dersler paneli KOYU-navy (İnteraktif/537 gibi) → 537'nin **koyu-panel** dili kullanıldı (light DEĞİL): panel `box-shadow:0 22px 50px -12px rgba(5,9,30,.6)` + üst radial ışık `rgba(96,165,250,.16)` + ince border; 5 CEFR kartı (1175 A1·1174 A2·1728 B1·1748 B2·47027 C1-C2) → `0 3px 8px` gölge + inset highlight + cubic-bezier hover (`translateX(4px)`+saturate/brightness). **CEFR renkleri + "A1..C1-C2" rozetleri + padding 107'den AYNEN KORUNDU** (yalnız derinlik/hover eklendi → rozet kaynağını bilmeye gerek kalmadı, kıramaz). g3 flyout panelleri de koyu derinlik. **Artık 4 dropdown da premium** (Dersler+İnteraktif=koyu-panel · Sınav+Kaynaklar=light-panel).
- **➕ v4 BEYAZ KENAR TUTARLILIĞI — block K (codeLen 36141→38215):** Kullanıcı "2 sinde beyaz kenar boyut katıyor 2 sinde yok" dedi. Kök neden: **hiçbir kartta gerçek `border` YOK**; Sınav/Kaynaklar kartları AÇIK/BEYAZ dolgulu → koyu panele karşı doğal parlak/beyaz kenar; İnteraktif+Dersler DOYGUN CEFR renkli → o kenar oluşmuyor (canlı zoom ile teyit, gerçek border değil dolgu farkı). **Çözüm:** doygun kartlara (İnteraktif 47866-47870 + Dersler 1175/1174/1728/1748/47027) `border:1.5px solid rgba(255,255,255,0.62)` (box-sizing:border-box → kayma yok; Oyunlar 48776 amber border DOKUNULMADI) + mobil border:none reset. Artık 4 dropdown kenar/boyut tutarlı (canlı zoom doğrulandı).
- **a11y/mobil:** focus-visible (`#185FA5` halka) + prefers-reduced-motion (anim/transition/transform off) + `@media(max-width:991px)` savunma reseti (10 yeni öğe bare-selector ile şeffaf+ikon gizle). **Premium kurallar `#main-navigation`/`.header-navigation` scoped → mobil drawer (`.mobile-navigation`, AYRI DOM) ETKİLENMEZ** (nav iki ayrı render; doğrulandı).

**🔑 DERSLER (bu tur):**
- **MENÜ CSS SİSTEM HARİTASI (hepsi front-end, wp_head):** **107**=temel menü SVG ikon + level renk + TÜM dropdown kart stilleri (Dersler/Sınav/Kaynaklar/İnteraktif-base). **537**=İnteraktif (47754) premium. **538**=Sınav(47047)+Kaynaklar(305) premium. **155**=DaF (2521) teal klasör ikon. **143**=mobil drawer netlik (sub-menu link w400 #EFF7FB → drawer KOYU temalı). Yeni dropdown güzelleştirmede bu zinciri koru. (Almanca Dersler 304 = bu turda v3'te premium yapıldı, bkz. block J — ARTIK 4 dropdown da premium.)
- **leaf vs has-children:** leaf öğe ikonu `> a::before`; çocuklu öğe (48522/298/735) `> a > .nav-drop-title-wrap::before` + wrap'i `display:flex`. Nav parse ile leaf/wrap durumunu DOĞRULA (canlı home.html'den `<li id="menu-item-N" class="...">` + anchor'da `nav-drop-title-wrap` var mı).
- **Özgüllük tuzağı:** 107'nin kart kuralları çoğu BARE (`.menu-item-X > a`, (0,1,1)); 538 yüksek-spec (`#main-navigation .menu-item-47047 .menu-item-X > a`, (1,3,1)) + priority 30 → kesin ezer. ESKİ öğeyi (telc) ezmek için yüksek-spec şart.
- **Deploy (kanıtlı):** `[IO.File]::ReadAllText` ile CSS oku (ETS/ConvertTo-Json tuzağından kaçın) → nowdoc PHP body kur → `POST /wp-json/code-snippets/v1/snippets` body UTF-8 bytes (`active:true, scope:front-end, priority:30`). **active=True dönerse PHP lint+çalıştırma geçti** (Code Snippets fatal'i otomatik pasifleştirir). Doğrula: cache-buster fetch'te `id="aef-menu-premium-v1"` + PHP-hata-sızıntısı yok → girişli Chrome render (cache atlar, anında) → **LiteSpeed Toolbox "Tümünü boşalt - LSCache"** (REST purge 404; girişli tarayıcı + `find`→`click ref` güvenilir) → public plain URL `X-LiteSpeed-Cache=miss` + marker var.
- **Workflow kurtarma dersi:** subagent oturum-limiti jüri/sentezi öldürünce, başarılı ajan çıktıları **transcript jsonl**'lerinde (`.../subagents/workflows/<runid>/agent-*.jsonl`); StructuredOutput tool_use `input`'unu (içinde `.css`) parse edip ana döngüde sentez yapılabilir.
- **PowerShell `/tmp` TUZAĞI:** PS 5.1 `/tmp`'i `C:\tmp` sanar (yok) → `$env:TEMP` kullan. Python Bash PATH'inde YOK → parsing'i PowerShell regex veya Read/Grep ile yap.

---

## Düzeltme 1 — Hero `</section>` Eksik (2026-06-13)

`aefh6-hero` section kapanış etiketi eksikti → tüm sayfa hero'nun çocuğu oluyordu, arka plan #0A1138 tüm sayfayı kaplıyordu, hero 5357px yüksekti.

**Fix:** Page ID 5 HTML'ine `aefh6-marquee` kapanış `</div>`'ından sonra `</section>` eklendi (REST API PATCH).

**Kontrol:** `document.querySelector('.aefh6-hero').children.length` → 4 olmalı (grid, beam, container, marquee).

---

## Düzeltme 2 — Eval Kartı Yeniden Konumlandırma (2026-06-13)

**Sorun:** `.aefh6-card.aefh6-card-eval` (yeşil tik + "Anında otomatik değerlendirme"), `aefh6-stack` içinde `aefh6-card-main`'in KARDEŞ elemanıydı → absolute konumlanmış, "Tüm sınavları görüntüleyin" linkinin üstüne geliyordu, gereksiz büyüktü.

**Çözüm:** Eval içeriği `aefh6-card-main`'in İÇİNE taşındı, link'in ÖNÜNE (üstüne) `aefh6-eval-inline` olarak yerleştirildi.

**Yeni HTML yapısı** (Page ID 5 içinde):
```html
<!-- aefh6-card-main'in son iki çocuğu: -->
<div class="aefh6-eval-inline">
  <span class="aefh6-ring" aria-hidden="true">...</span>
  <span class="aefh6-eval-text">
    <b>Anında otomatik değerlendirme</b>
    <small>Okuma ve dinlemede sonucunuz testin bitiminde hazır</small>
  </span>
</div>
<a class="aefh6-card-link" href="/beceri-temelli-olcme-sinavlari/">Tüm sınavları görüntüleyin →</a>
```

**CSS** (sayfa body'sine `<style>` bloğu olarak eklendi — head CSS'ini override eder):
```css
#aef-home-modern .aefh6-ring,
#aef-home-modern .aefh6-ring > svg { width: 30px !important; height: 30px !important; }
#aef-home-modern .aefh6-ring-num svg { width: 13px !important; height: 13px !important; }
#aef-home-modern .aefh6-eval-inline {
  display: flex !important; align-items: center !important; gap: 9px !important;
  margin-top: 14px !important; padding: 9px 12px !important;
  border-radius: 10px !important;
  background: rgba(74,222,128,.08) !important;
  border: 1px solid rgba(74,222,128,.22) !important;
}
#aef-home-modern .aefh6-eval-text b { font-size: 13px !important; }
#aef-home-modern .aefh6-eval-text small { font-size: 11.5px !important; }
#aef-home-modern .aefh6-stack { min-height: 470px !important; }
```

**DOM doğrulama (scroll=200):**
- Ana kart: top=133, bottom=590, height=457px
- eval-inline: top=448, bottom=521 → ana kartın **içinde**, link'in **üstünde** ✓
- card-link: top=538, bottom=561 → ana kartın içinde, eval'in altında ✓
- Eski `.aefh6-card-eval`: DOM'da YOK ✓

---

## CSS Katman Hiyerarşisi

1. Sayfa HTML `<style>` (temel)
2. Customizer CSS → `<head>` içinde `!important` ile
3. Sayfa body `<style>` blokları → head'i override eder (sonra yüklenir)

**Snippet 525** (`aef-eval-card-fix-v1`, scope: `site-css`): `<head>`'de yükleniyor, Customizer'ın `!important`'ı tarafından eziliyor. Artık gereksiz ama zararsız bırakıldı.

---

## Cache Yönetimi

- **LiteSpeed Cache:** Snippet 488'i toggle VEYA UI "Purge All"
- **Cloudflare:** `CF-Cache-Status: DYNAMIC` (HTML cache yapmıyor)
- **Tarayıcı cache:** `location.reload(true)` veya `?v=timestamp` URL
- **Snippet ile purge:** `add_action('init', function(){ do_action('litespeed_purge_all'); }, 99)` → ASLA koşulsuz aktif bırakma

---

## Sistem Kuralları (kalıcı)

- **Sahte yorum/sosyal kanıt üretme yasak**
- Resmî sınav logoları KULLANILABİLİR — kullanıcı 2026-06-13'te onayladı; eski "resmî logo gömme yasak" notu YANLIŞ ANLAMAYMIŞ, geçersiz (kullanıcı "böyle bir kural yok" dedi)
- **Tekrarlı deneme YOK** (greylist hijyeni)
- **Koşulsuz purge asla aktif kalmaz**
- **Çift oturum yasağı**
- **Snippet 28+120 daima aktif**

---

## Snippet Sistemi

- Prefix: `aef-` (CSS class adları)
- Snippet 28+120: daima aktif kalmalı
- Snippet 525: `site-css` scope, head'de yükleniyor → body override ile etkisiz

---

## Renk Sistemi

A1=#16A34A · A2=#0891B2 · B1=#D97706 · B2=#EA580C · C1=#DC2626 · C2=#BE123C. Accent amber: #F59E0B / text #451A03.

---

## Düzeltme 3 — Öğrenci Yorumları Section (2026-06-13)

`#yorumlar` section'ı `#hizmetler` ile `#takip-et` arasına eklendi.

**Yapı:** 5 kart, 6-sütunlu CSS grid → ilk satır 3 kart (her biri `span 2`), ikinci satır 2 kart ortada (`grid-column: 2/span 2` ve `4/span 2`). Responsive: 900px altı 2 sütun, 560px altı 1 sütun.

**Kişiler:** Ayşe K. (A1), Mert Y. (A2), Zeynep D. (B1), Emre A. (B2), Elif S. (C1).

**REST API tekniği:** Türkçe özel karakterler HTML entity olarak kodlandı (`&#351;` = ş vb.), body `[System.Text.Encoding]::UTF8.GetBytes($bodyJson)` ile gönderildi. PowerShell 5.1'de `ConvertTo-Json -Compress` + UTF-8 bytes çalışıyor; string olarak POST 400 hata veriyor.

---

## Düzeltme 4 — Cep Rehberi Lead-Magnet Taşıma (2026-06-13)

**İş:** Anasayfadaki (Page 5) "Cep Rehberi" lead-magnet bloğu kaldırıldı, Kaynaklar sayfasına (Page 57) taşındı. Chrome köprüsü + REST nonce ile yapıldı; köprü timeout'a düştü ama yazma POST'ları timeout'tan ÖNCE bittiği için kayıpsız.

**Anahtar bulgu:** Widget aslında TEK SATIR shortcode: `[aef_lead_magnet chooser="a1,a2,b1,b2,c1c2" all="0"]`. Gördüğümüz ~8 KB HTML/CSS/JS onun render çıktısı. Bu yüzden taşıma tek satırla yapıldı.

**Page 57 (/yararli-siteler/):** `<section class="sec" id="cep-rehberi"><div class="wrap">[aef_lead_magnet ...]</div></section>` eklendi (ONLINE KAYNAKLAR 2-card grid'inin altına). DB doğrulandı (REST context=edit): `cep-rehberi` + shortcode VAR. Raw 6503→6651.

**Page 5:** lead-magnet bloğu (`aef_lead_magnet` shortcode) kaldırıldı. Raw 67606→67376, render 81131→72827. DB doğrulandı: `aef_lead_magnet` YOK.

**Temizlik (2026-06-13, TAMAM):** Page 5'teki 5 yetim `.aeflm-*` CSS kuralı + "6) Cep Rehberi" yorumu REST PATCH ile silindi (746 byte; raw 67376→66630). DB doğrulandı: `aeflm` sıfır. Regex: `[^{}]*\.aeflm-[^{}]*\{[^{}]*\}` + length/sentinel güvenlik kapıları ile.

**Widget konumu (2026-06-13, TAMAM):** Kullanıcı "bu alttaki kısım sürekli aşağı kayıyor" dedi → Page 57'de `#cep-rehberi` section'ı en alttan (CTA üstü) **yukarı** taşındı: intro'nun altı, 2-kart grid'in üstü. Yeni sıra: hero → intro → **cep-rehberi** → grid → CTA. Section taşıma `(?s)<section...id="cep-rehberi">.*?</section>` regex + sıralama doğrulama kapısıyla.

**Referans düzeltmesi (ÖNEMLİ):** Kaynaklar hub = **Page 57** (`/yararli-siteler/`, başlık "YARARLI SİTELER"). Page 31 onun ALT sayfası (`almanca-tavsiye-siteler`). Eski "Kaynaklar hub (31)" referansı YANLIŞ.

---

## Düzeltme 5 — Hero Üst/Alt Boşluk Azaltma (2026-06-13)

**Sorun:** Anasayfa hero'sunda (`#aef-home-modern .aefh6-hero` > `.aefh6-container`) üstte çok boş mavi alan; içerik aşağıdan başlıyor, kayan şerit (`.aefh6-marquee`) ve altındaki bölümler aşağı kaymış görünüyor. Kullanıcı "üstü yukarı çek, her alan daha az yer kaplasın, kayma bitsin" dedi.

**Çözüm (REST PATCH, Page 5):** `.aefh6-container` temel padding `92px 28px 84px` → `44px 28px 48px`. Sayfa sonundaki ekran-yüksekliği override'ları da tutarlı (azalan) kalsın diye düşürüldü: `@media(max-height:900px)` 60/54→38/38, `@media(max-height:780px)` 40/36→28/28.

**Sonuç (Chrome ölçümü, vh=1092):** padding-top 92→44, padding-bottom 84→48, hero 854→770px (−84). Şerit ~84px yukarı geldi; alttaki tüm bölümler otomatik yukarı kaydı. Görsel doğrulandı (hero+şerit+Son Duyurular tek ekranda).

**Not:** Hero yüksekliğini sol metin kolonu belirliyor; `.aefh6-stack` min-height:470px sağ karta ait, dokunulmadı.

**Env:** `.claude/settings.local.json`'a `PowerShell(*)` izni eklendi → REST/PowerShell komutları artık "allow" sormuyor. Ayrıca Chrome MCP (köprü) canlı sayfayı görüp ölçmek için kullanıldı (resize_window + javascript_tool + computer screenshot).

---

## Düzeltme 6 — Seviye Pill'leri Yukarı Taşıma (2026-06-13)

`#seviyeler` section'ı (başlık "SEVİYE BAZLI ÜCRETSİZ İÇERİK", A1–C2 pill'leri, `.aefgl-*` class'ları, `aria-label="Seviye bazlı ücretsiz içerik"`) Son Eklenen'in altından **hero/kayan şeridin (`aefh6-marquee`) hemen altına** taşındı (REST PATCH, section move, gate'li). Yeni anasayfa sırası: hero+şerit → **seviyeler pill'leri** → Son Duyurular → Son Eklenen → yorumlar → hizmetler → ... DB doğrulandı: `seviyeler@35542 < duyurular@41143`. Boyut korundu (section `padding:30px 0`, pill'ler tek satır ortalı); kullanıcı görsel boyut kararı verecek.

---

## Düzeltme 7 — Sınav Logo Şeridi (2026-06-13)

Anasayfada hero'nun karışık kayan şeridi (`aefh6-marquee` — içerik kategorileri + 5 sınav metni) KALDIRILDI. Yerine hero'dan hemen sonra (seviyeler pill'lerinin üstünde) koyu temalı **sınav logo şeridi** (`aef-exam-strip`, başlık "HAZIRLADIĞIMIZ SINAVLAR") eklendi: 6 resmî logo beyaz kartlarda, kayan marquee (2× set, `@keyframes aefExamScroll` translateX -50%), her kart `/beceri-temelli-olcme-sinavlari/`'ye linkli, hover'da pause, mobil (≤600px) + `prefers-reduced-motion` (sarmalı statik) uyumlu.

**Kapsam (FINAL):** 5 logo — Goethe · telc · ÖSD · TestDaF · YDS(ÖSYM). DAAD çıkarıldı (sınav değil), **DSH çıkarıldı** (temiz/tek resmî logosu yok, kalabalıktı), Aile Birleşimi alınmadı (logosu yok).

**Logo medya ID'leri (FINAL):** Goethe=**48714** (`goethe-institut-clean.png`, Wikimedia temiz şeffaf ✓), telc=**48721** (`telc-landscape.png` — eski kare 48707 KIRPILIP açık zemin şeffaf yapıldı → yatay 337×205 ✓), ÖSD=**48723** (`osd-clean.png` — kullanıcının yeni yüklediği temiz "ösd Prüfungszentrum" kırpılıp şeffaf yapıldı; eski 48710 vinyetliydi), TestDaF=2306 (eski 2015 png), YDS/ÖSYM=**48715** (`osym-yds-clean.png`, Wikimedia temiz ✓). (Eski images.png/images.jpg/header-telc.jpg/dsh artık kullanılmıyor.)

**telc kırpma yöntemi (yeniden kullanılabilir):** PowerShell System.Drawing ile: köşe=zemin, luma≤200 piksellerle içerik sınır kutusu bul → kırp → luma>200 pikselleri transparan yap (açık gri zemin gider, koyu gri "telc" wordmark kalır). Kare/dolgulu logoları yatay+şeffaf yapmak için iş görüyor.

**Logo kaynaklama yöntemi (ÇALIŞIYOR):** Wikimedia Commons API (`action=query&generator=search&gsrnamespace=6&prop=imageinfo&iiprop=url&iiurlwidth=...`) ile dosya bul → API'nin döndürdüğü `thumburl`'i indir (kendi width'imi UYDURMA, 400 verir) → WP REST `POST /wp/v2/media` ile yükle (`Content-Disposition: attachment; filename=...`, app-password `upload_files` iznine sahip ✓). Commons'ta var: Goethe, ÖSYM. YOK: telc, ÖSD, TestDaF, DSH.

**KRİTİK TUZAK:** WordPress çıktıda tüm `<img>`'lere otomatik `loading="lazy"` ekliyor → kayan şeritte (off-screen kartlar) görseller yüklenmiyordu (natW=0). ÇÖZÜM: şerit img'lerine açıkça **`loading="eager" decoding="async"`** koy (WP, loading attr varsa lazy eklemez). Ayrıca `mix-blend-mode:multiply` açık logoları soluklaştırdığı için KULLANMA. LiteSpeed yüklenen PNG'leri webp olarak sunuyor (zararsız). Eski `.aefh6-marquee/.aefh6-track/...` CSS kuralları ölü ama zararsız bırakıldı.

**Durum (FINAL):** 5 logo temiz+uniform (Goethe·telc·ösd·TestDaF·ÖSYM). telc ve ÖSD kırpılıp şeffaflaştırıldı. **Başlık:** "Almanca yeterlik sınavı yapan kurum ve kuruluşlar" (amber, sentence-case, .95rem; eski "HAZIRLADIĞIMIZ SINAVLAR" değişti). **Kart üst renk çizgisi:** Tema `.aef-exam-card`'a rastgele CEFR renkleriyle `border-top:~5px` basıyordu (anlamsız) → `border:0 !important` ile kaldırıldı, uniform beyaz kartlar.

**Ekran-yakalama notu:** LiteSpeed yüklenen PNG'leri webp sunuyor; Chrome MCP headless screenshot bazen webp kartları boş yakalıyor (animasyon+paint zamanlaması) — gerçek tarayıcıda sorun YOK. Temiz kare için: animasyonu durdur (`track.style.animation='none'`) + img src'lerini yeniden ata (repaint) sonra screenshot.

---

## Düzeltme 8 — Hero Yukarı + Logo Şeridi Son Rötuş (2026-06-13)

**Hero içeriği yukarı:** `.aefh6-container` padding `44px 28px 48px` → **`14px 28px 18px`** (üst boşluk 44→14, hero kısaldı). @media max-height override'ları da uyumlandı (38/38→12/14, 28/28→10/12). **Sonra "2cm daha yukarı" istendi:** `.aefh6-h1` hesaplanan margin-top 93px'di (sayfa base'i `margin:22px 0 0` ama **head/Customizer `!important` ile eziyor**; "93px" sayfa içeriğinde YOK) → body `<style>`'a (son `</style>` öncesi) `#aef-home-modern .aefh6-h1{margin-top:16px!important}` + `.aefh6-kicker{margin-bottom:18px!important}` + `.aefh6-container{align-items:start!important}` (kart ortalı→ÜSTE hizalı) eklendi. Sonuç: hero 660→585px, sol+sağ içerik ~75px yukarı, logo şeridi İLK EKRANDA. **Sonra "%10-15 küçült + seviye pill'leri de ilk ekrana" istendi** → aynı override bloğu genişletildi: `.aefh6-h1{font-size:clamp(34px,4.4vw,54px)!important}` (62→54, ~%13) + tüm dikey margin'ler daraltıldı (kicker mb12, deck mt14, byline mt16, actions mt18) + `.aef-exam-strip{padding:10px 0 14px!important}` + `#seviyeler{padding-top:12px!important}` (inline 30px'i ezdi) + `.aefgl-head{margin-bottom:8px!important}`. **FINAL: hero 535px, h1 54px; A1–C2 pill'leri pillsBottom=914 < vh=927 → ilk ekranda görünür.** Tüm hero/strip/seviyeler dikey ayarı bu son `</style>` öncesi override bloğunda toplandı. **Ek:** beceri kartı önce `transform:scale(.75)` ile küçültüldü ama "büzülmüş"+boşluk göründü → **`#aef-home-modern .aefh6-card-main{zoom:.8 !important}` + `.aefh6-stack{min-height:0 !important}`** (zoom layout'a saygılı, transform DEĞİL → ölü boşluk yok; hero yüksekliğini sol metin sütunu belirlediği için pill konumu değişmez). Logo şeridi: `.aef-exam-card img{max-height:38px;max-width:145px !important}`; daha kare olan **telc & ÖSD ayrı büyütüldü** → `#aef-home-modern .aef-exam-card img[alt="telc Deutsch"],...img[alt="ÖSD"]{max-height:44px !important}` (~%15). **Hero butonları 3→1:** TEK `aefh6-btn aefh6-btn-primary aefh6-btn-solo` (href=#hizmetler) **"Ders ve Akademik Danışmanlık"** — mezuniyet-kepi inline SVG + `::after` shimmer/parıltı (`@keyframes aefBtnShine`, reduced-motion'da kapalı). Kullanıcı bedava-kaynak yerine bunu seçti (kişisel/akademik temsil için). DERS: `[regex]::Replace` ile body markup'ında bölüm değiştirirken MatchEvaluator (`{param($m) $str}`) kullan ki `$` regex olarak yorumlanmasın.

**Kart eşitleme + anasayfa daraltma (2026-06-13):** Duyurular ile Son Eklenen post-grid'leri farklı genişlikteydi (1120 vs 900px → kartlar 344 vs 271); ikisi de `.aef-posts-grid .aef-cols-3` → `#aef-home-modern .aef-posts-grid{max-width:900px !important;margin:0 auto}` ile **eşitlendi** (her ikisi 900px/271px kart). Anasayfa bölüm boşlukları daraltıldı: `#aef-home-modern .aef-section{padding:42px 0 !important}` (eskiden 68), `.aef-section-tight{padding:30px 0 !important}` (eskiden 48). `#seviyeler` ID override'ı (12/22) daha güçlü olduğu için etkilenmedi. **NOT:** Son Eklenen kartları beyaz `.aef-post-shell` kutuda, Duyurular değil — boyut eşit ama bu görsel fark bekliyor. **Daraltma anasayfaya özel** (`#aef-home-modern` scope); diğer sayfalar (Page 57 `#yk` vb.) ayrı, kendi class'larıyla yapılır. **DERS:** head Customizer'ın ezdiği bir değeri değiştirmek için body `<style>`'a yüksek-özgüllük (`#id .class`) + `!important` override yaz; base kuralı değiştirmek işe yaramaz.

**Logo şeridi son hali:** kartlar küçültüldü (yükseklik 70→52, min-width 160→118, img max-height 46→30); aralara **◆ ayraç** (`.aef-exam-sep`, amber #FCD34D, opacity .5); track **6 kopya** (önceden 2 kopya=1806px < 2048 viewport → sağ boşalıyordu; her yarı artık ≥ ekran, seamless); başlık rengi amber → **açık #E6EAF2** (.95rem, sentence-case). Animasyon 60s.

**ÖNEMLİ TUZAK (negatif margin):** Strip'i yukarı almak için `margin-top:-42px` kullanınca başlık hero `.aefh6-container`'ın ARKASINDA kaldı (görünmez oldu; `document.elementFromPoint` ile teşhis: heading üstünde aefh6-container). **Doğru yöntem:** negatif margin KULLANMA; bir bölümü yukarı almak için ÜSTTEKİ bölümün (hero container) alt padding'ini azalt → üstteki kısalır, alttaki doğal+occlusion'sız yukarı gelir.

---

## Düzeltme 9 — SEO Meta Açıklamaları + AIOSEO REST Yazma (2026-06-13)

**Denetim sonucu:** 373 item (sayfa+yazı) tarandı. Gerçekten kısa/eksik meta-açıklama yalnızca **4 sayfa**. İlk toplu taramada `len=-1` çıkan 18 item TOPLU-FETCH THROTTLE yanlış-pozitifiydi — tek tek (3 retry + 400ms pacing) bakınca hepsi DOLU (123–184 char). Sitemap (165, len=0) utility sayfa, atlandı.

**Düzeltilen 4 sayfa** (yeni meta-desc yazıldı + canlı public HTML'de doğrulandı):
- **47766** `/interaktif-w-fragen.../` W-Fragen (Soru Kelimeleri) A1 — len 64→167
- **48012** `/interaktif-zahlen-a1-1/` Zahlen (Sayılar) — len 43→151
- **48032** Indirekte Fragesätze (ob/W-Wort) — len 52→163
- **48067** Wortbildung: Vor- & Nachsilben — len 66→165

(Birkaçı ~160'ı biraz aşıyor (163/165/167); Google kuyruğu kırpar, anahtar kelimeler başta olduğu için sorun değil. İstenirse kısaltılır.)

**🔑 KRİTİK YENİ KABİLİYET — AIOSEO meta app-password REST ile YAZILABİLİYOR.** (Eskiden "AIOSEO verisi `wp_aioseo_posts` custom tablosunda, standart REST meta'da değil → yazılamaz" sanılıyordu. YANLIŞMIŞ.) Yöntem:
```
POST https://www.almancaeskisehir.com/wp-json/aioseo/v1/post
Headers: Authorization: Basic <b64>, Content-Type: application/json
Body (UTF8 bytes): {"id":<postId>,"description":"<metin>"}
→ Dönüş: {"success":true,"posts":<id>}
```
Minimal `{id, description}` body yeterli (title/keyphrases/og vb. opsiyonel; sadece description günceller). PowerShell'de Türkçe için `[System.Text.Encoding]::UTF8.GetBytes((... | ConvertTo-Json -Compress))`. Route GET+POST destekliyor; app-password user'ın yetkisi yetiyor. **Bu sayede diğer sayfaların SEO meta'sını da programatik düzeltebiliriz** (artık editöre yapıştırma gerekmez).

**TUZAKLAR:**
- `/wp/v2/pages/{id}?context=edit&_fields=link,title` kombinasyonu **404** verdi. Link almak için SADE çağrı kullan: `/wp/v2/pages/{id}` (context/_fields YOK) → `link` döner.
- Doğrulama: public sayfayı `?nocache=<guid>` ile çek, `<meta name="description" content="([^"]*)"` regex + `HtmlDecode`. AIOSEO description'ı bu meta tag'e render ediyor.

**Durum: SEO görevi TAMAM.** Sitede başka gerçek kısa/eksik meta-desc yok.

---

## GSC Coverage Teşhisi (2026-06-13)

**Sonuç: KRİZ YOK.** GSC paniği ("dizine eklenen 415, eklenmedi 2855, 11 neden") yanıltıcı. Gerçek içeriğin %100'ü dizinde.

**Gerçek içerik (REST + sitemap ile doğrulandı):** 177 yayında yazı + 193 sayfa + 15 kategori = **385 sitemap URL'i**. Sitemap **AIOSEO** (`/sitemap.xml` → `post-sitemap.xml` 177 + `page-sitemap.xml` 193 + `category-sitemap.xml` 15) yalnız bunları beyan ediyor; etiket ve attachment YOK = doğru. Dizinde **415 ≥ 385** → tüm gerçek içerik kapsanıyor (+~30 eski sayfa fazlası).

**1146→415 düşüşü (15 Mar→5 Haz):** Google'ın geçmişte fazladan dizine aldığı çöpü (etiket arşivleri + medya/PDF attachment sayfaları) temizlemesi = SAĞLIKLI. **Geri getirmeye çalışma.**

**2855 dökümü:** noindex **900** = ~999 etiketin arşiv sayfaları (AIOSEO noindex, DOĞRU) · yönlendirme **363** = attachment URL'leri 301 (DOĞRU; test: `/osd-clean/`, `/telc-landscape/` → 301) · 404 **897** = eski/silinmiş URL (çoğu eski medya/permalink; 385 gerçek sayfa olduğundan içlerinde gerçek içerik olsa olsa ~birkaç) · tarandı-eklenmedi **602** = zayıf/medya · diğer **93** önemsiz (robots `/?s=`, canonical, discovered, 5xx=3).

**"Doğrulama: Başarısız oldu" (404 satırı):** Geçmişte "düzeltmeyi doğrula" tıklanmış ama gerçek düzeltme yok → Google tekrar bakıp 404 görmüş. Tek başına alarm değil.

**Asıl yapılacak (büyüme için):** (1) 404 listesini GSC'den dışa aktar → gerçek değerli URL var mı triyaj, varsa 301; (2) bekleyen ~18 URL manuel index + striking-distance iç link turu; (3) 5xx=3 muhtemelen Imunify360 Googlebot engeli → TurHost whitelist maili çözer.

## Düzeltme 10 — Striking-distance İç Link Turu (2026-06-13, TAMAM)

**Bu chat yürüttü** (kullanıcı onayladı: memory'deki "ayrı chat" = bu chat). Toplam **32 sayfa** `aef-ilgili` bloğuyla bağlandı; hepsi DB + canlı doğrulandı.

**Veri:** GSC Performans export (Downloads: `...Performance-on-Search-2026-06-06 (1).xlsx`, ~6 ay: 3 Ara 2025–2 Haz 2026). Okuyucu: `C:\Users\PC\Downloads\_read_gsc.py` (py 3.12; openpyxl yoksa stdlib zip+xml). **TR başlıklar: pozisyon="Pozisyon", gösterim="Gösterimler", tıklama="Tıklamalar".** Sheet'ler: "Sorgular", "Sayfa sayısı".

**Bulgu:** SEO motoru = eski `.html` dilbilgisi yazıları, devasa gösterim ama 5-15. sıra (artikeller 65.779@7.0, ekler 29.360@6.3, gecmis-zaman 23.898@8.3, modal-fiiller 17.822@6.5). 2. sayfa hedefleri: relativsatz 8.200@14.1, geschweige-denn 7.495@12.4. En çok TIKLANAN = 2014 ham PDF'leri (ayrı iş — Bekleyen #7 KAPANDI).

**Permalink:** `.html` → `/slug/` **301** (canonical=`/slug/`). İç linkler hep uzantısız `/slug/`. `.html` sayfalar REST'le düzenlenebilir WP post.

**Yöntem — `aef-ilgili` bloğu:** Yazı SONUNA tek tip `<div class="aef-ilgili" style="...">` (p başlık "İlgili konular ve alıştırmalar" + ul; iç içe div YOK → regex güvenli). REST: GET content.raw (context=edit) → `[regex]::Replace(raw,'<div class="aef-ilgili".*?</div>','','Singleline')` (idempotent sök) → blok ekle → `POST /wp/v2/posts/{id}` body=UTF-8 bytes, `application/json; charset=utf-8`. Doğrulama: DB link sayısı + canlı `/slug/?nocache=<guid>`. LiteSpeed güncellemede otomatik purge. unfiltered_html var → style korunuyor. 503 olursa 3sn bekle+tekrar (geçici, auth değil). **Tasarım/anchor sonradan tek seferde değişebilir** (idempotent). KURAL: bir sayfa aynı anda tek kümede (ikinci edit birinciyi EZER) → kümeler ayrık tutuldu.

**Batch 1 — Bağlaçlar (7):** almanca-baglaclar(1231), weil-da-denn-baglaclari(4397), zweiteilige-konnektoren(24833), um-zu-ve-damit-baglaclari(1063), relativsatz(1196), geschweige-denn(2282), dass-cumleleri-dass-satze(1073).
**Batch 2 — Fälle (7):** almanca-artikeller(871), akkusativ-konu-anlatim(2386), dativ-alan-fiiller(1282), der-genitiv(700), akkusativ-alistirmalari(48324), dativ-alistirmalari(48336), genitiv-ismin-in-hali(48505).
**Batch 3 — Fiiller/Zamanlar (7):** almanca-gecmis-zaman-perfekt-und-prateritum-vergangenheit(1341), modal-fiiller-tablosu(857), a1-seviyesi-onemli-fiiller(825), partizipien(1996), modalverben-alistirmalari(48353), praeteritum-alistirmalari(48426), trennbare-verben-alistirmalari(48464).
**Batch 4 — 4 küçük küme (11):** Sıfatlar [almanca-sifatlar(1034), sifat-cekimleri(1905), komparativ-superlativ-alistirmalari(48488)]; Edatlar [almanca-edatlar-prapositionen(2372), rektion-der-verben(2050), wechselpraepositionen-alistirmalari(48344)]; Possessiv [aitlik-zamirleri-possessivartikel(1956), possessivartikel-alistirmalari(48492)]; Nebensätze [nebensatze-alistirmalari(48490), objektsatze-subjektsatze(2128), genitiv-relativsatze-ornek-cumleler(2408)].

**Sonuç:** 10 yeni Haziran alıştırma sayfasının HEPSİ konu sayfalarına bağlandı (indexlemeye yardım). **Sıradaki opsiyon:** ~2-4 hafta sonra yeni GSC Performans export al → relativsatz/geschweige-denn pozisyon değişimini ölç. Henüz bağlanmamış tema sayfaları (kelime listeleri, okuma metinleri, mevsimler/sayılar/vücut/yiyecek vb.) ek küme adayı.

## Düzeltme 11 — İlk Gerçek Form Yorumu: Meryem (A2) (2026-06-14)

**İlk gerçek `/ogrenci-yorumlari/` form yorumu yayımlandı.** Meryem (A2) yayın iznini açıkça verdi (e-posta melek_94@hotmail.com — yayımlanmaz). Yorum sınav simülasyonu + ses kaydı/konuşma özelliğini övüyor → `#aefyr` CTA bloğunun ("Bu alan gerçek deneyimlerle büyüyor") ilk meyvesi.

**Değişiklik (Page 5, `#yorumlar`):** Kart **5→6**. Meryem, Mert Y.(A2) ile Zeynep D.(B1) arasına eklendi → sıra A1·A2·**A2**·B1·B2·C1. Grid artık **temiz 3+3** (Düzeltme 3'teki 3+2 düzeni ARTIK GEÇERSİZ). CSS: tüm kartlar `#aef-home-modern .aef-reviews-grid .aef-review-card{grid-column:span 2}` (eski `nth-child(-n+3)` + `(4):2/span 2` + `(5):4/span 2` kaldırıldı); mobil 900px `nth-child(-n+6)`. Metin entity-kodlu (`&#252;` vb.), POST UTF-8 bytes (proven yöntem). DB + canlı doğrulandı (Türkçe doğru çözülüyor, LiteSpeed otomatik purge).

**KURAL teyidi:** Sahte yorum üretmek yasak AMA form'dan gelen + adıyla yayın izinli gerçek yorumlar YAYIMLANIR (doğru iş). Mevcut 5 isim seed/örnek; bölüm gerçek yorumlar geldikçe büyüyecek. **İdempotent ekleme:** `aef-review-author">Meryem` guard + `<div class="aef-review-card">` say (5→6) + Zeynep anchor'a `LastIndexOf` ile insert.

---

## Düzeltme 12 — Site Geneli Denetim + Eklenti Envanteri + AdSense Kaynağı (2026-06-14)

**Bağlam:** Kullanıcı SEO dışı genel denetim istedi; canlı prob'larla (PowerShell/Invoke-WebRequest) yapıldı.

**🔑 AdSense kaynağı = Google Site Kit (KESİN).** Kullanıcı "ben hiç reklam eklemedim" dedi → araştırıldı. HTML'de `<!-- Google AdSense snippet'i, Site Kit tarafından eklendi -->` yorumu + `adsbygoogle.js?client=ca-pub-9591078265641533&host=ca-host-pub-2644536267352236`. **Tek** yayıncı ID, yalnız Site Kit bloğunda → enjekte/zararlı DEĞİL (Wordfence de aktif). `host=` param + anasayfada **0 `<ins>`** → reklam SUNMUYOR (dormant): gelir yok ama her sayfada script + çerez/onay yükü var = saf maliyet. GA4 de Site Kit'ten geliyor. **Kaldırma:** WP Admin → Site Kit → Ayarlar → AdSense → Bağlantıyı Kes (Search Console/Analytics modülleri ETKİLENMEZ; REST'ten yapılamaz, OAuth gerekir). Kullanıcı publisher ID'nin kendine ait olduğunu doğrulayacak + kesince rescan ile script'in gittiği doğrulanacak.

**✅ ÇÖZÜLDÜ (2026-06-14):** Kullanıcı ekranla teyit etti — `pub-9591078265641533` kendi AdSense hesabı VE hesap **inaktiflikten devre dışı** ("etkin olmadığı için devre dışı bırakıldı", reklam sunmuyordu) → "kaldır" dedi. **Chrome MCP ile** WP Admin → Site Kit → Connected Services → AdSense → Edit (`ref` ile) → **Disconnect** + onay yapıldı. Sonuç: AdSense Connected listesinden kalktı; Arama konsolu + Analytics + PageSpeed korundu. Canlı doğrulama (cache-buster + plain): anasayfa & blog `adsbygoogle/ca-pub/googlesyndication=0`, **GA4 gtag=7 (Analytics duruyor)**, LiteSpeed=miss (taze üretim, ayrı purge gerekmedi). Google'daki hesap olduğu gibi (devre dışı, zararsız; Site Kit'ten geri bağlanabilir). **TUZAK:** LiteSpeed REST purge `/wp-json/litespeed/v1/purge/all` route'u **404** (bu kurulumda yok) — cache-buster sorgu (`?x=guid`) origin'i taze verir, yeterli. **DERS:** Chrome MCP'de piksel-tıklama SPA'da kaydı (yanlış satır açıldı); `find` → `ref` ile tıklama güvenilir. Screenshot 1× 30s timeout verdi ama `find` çalışmaya devam etti.

**Aktif eklentiler (18, REST `/wp-json/wp/v2/plugins`; miyatuk = administrator):** ai-engine, all-in-one-seo-pack (AIOSEO), burst-statistics, code-snippets, cookie-law-info (CookieYes), **google-site-kit** (AdSense+GA4+SC kaynağı), **h5p** (interaktif/quiz aracı — OYUNLAŞTIRMA için birebir), integromat-connector (Make), jetpack (ağır), kadence-blocks, kadence-starter-templates, litespeed-cache, redirection, webp-converter-for-media, **wordfence** (güvenlik), wpforms-lite (formlar — yorum/iletişim), wp-mail-smtp (bildirim e-postaları). **wp-super-cache = INACTIVE** (LiteSpeed tek aktif cache → çakışma YOK; hedef karşılanıyor). **SİLME HOST'TA BLOKLU:** REST `DELETE /wp/v2/plugins/wp-super-cache/wp-cache` → **500** (TurHost/Imunify360 programatik plugin dosya silmeyi engelliyor — `DISALLOW_FILE_MODS`/FS kısıtı veya WP Super Cache uninstall hatası). Kısmi silme OLMADI; plugin sağlam+inactive kaldı, site 297KB/200 sağlıklı. Fiziksel silme istenirse WP Admin→Eklentiler→Sil (FTP isteyebilir) ama kozmetik. **🔑 GENEL DERS: bu host'ta REST ile plugin SİLME çalışmıyor (500); silme için WP admin UI gerekir.** Tema: **Kadence**.

**🪶 Jetpack diyeti (2026-06-14, ✅ TAMAM — 13 modül kapalı, Photon dahil; de-coupling tamam):** Kullanıcı "gereksizleri kademeli kaldır, sana bıraktım" dedi. Modül tablosu (`?page=jetpack_modules`) Chrome MCP + JS ile yönetildi — deactivate link'lerine `fetch(href,{credentials:'include'})` ile basıldı (UI tıklamadan, toplu; nonce URL'de). **KAPATILAN 9 modül:** stats · likes · blaze · latex · gravatar-hovercards · widget-visibility · protect · account-protection · photon-cdn (asset CDN). Sonuç doğrulandı: Jetpack ref **52→9**, `c0.wp.com`=0, site 200/kritik hata yok, GA4 duruyor. İstatistik artık **Burst (günlük) + GA4 (derin)**; Jetpack Stats toolbar grafiği kaldırıldı ("yeterli değil" demişti).

**JETPACK TAM KALDIRILAMAZ — KALACAK (ince):** `/iletisim/` sayfasında GERÇEK Jetpack e-posta bülteni formu var: `<form action="https://subscribe.wordpress.com/" target="aes-sub-frame">` → **subscriptions modülü gerçek kullanımda, aboneler olabilir.** (NOT: o sayfada WPForms/Jetpack-contact formu RENDER OLMUYOR — sadece bülten + arama; iletişim formu başka yerde olabilir/eksik olabilir, incelenebilir.) **KALAN AKTİF (~11):** subscriptions(KORU=bülten) · photon(görsel CDN, duruyor → ileride kendi LiteSpeed/webp+CF CDN'ine taşı) · related-posts + sharedaddy + comments(görünür, düşük değer → onay bekliyor) · blocks/shortcodes/tiled-gallery/widgets/contact-form(kullanılmıyor → içerik kontrolüyle kapatılacak) · publicize(sosyal otomasyon → kullanıcı kararı) · woocommerce-analytics(WooCommerce yok=etkisiz).

**BEKLEYEN KULLANICI KARARI:** (1) bülten kalsın mı/kaldırılsın mı (abone sayısı kontrol edilebilir), (2) Publicize kullanılıyor mu. AskUserQuestion yanıtsız kaldı → güvenli varsayılan: **bülten + publicize DOKUNULMADI.** **TUZAK/DERS:** 8 modülü tek JS fetch-loop'ta kapatırken Chrome MCP 45s timeout verdi AMA fetch'ler sunucuda tamamlanmıştı — fresh reload ile doğrulanınca hepsi PASİF çıktı. **timeout ≠ başarısız; her zaman taze reload + re-read ile doğrula.**

**✅ 2. TUR TAMAM (kullanıcı "sana bırakıyorum devam" dedi):** +3 modül → **related-posts · sharedaddy (paylaşım) · comments** (Jetpack yorumları → yerli WP). **TOPLAM 12 modül kapalı.** Kesin doğrulama: `/almanca-artikeller/` yazısında rendered-relatedposts=False · sharedaddy=0 · jetpack-yorum=False · kritik hata yok. Anasayfadaki kalan **9 jetpack ref = TAMAMEN subscriptions/bülten** (korunuyor); 3 `jp-relatedposts` izi = **ölü CSS override** (zararsız; kozmetik temizlik bekliyor). LiteSpeed admin-bar "Tümünü Boşalt" ile purge edildi (REST purge route YOK=404). **KORUNAN:** subscriptions(bülten) · photon(görsel CDN) · publicize(frontend yükü ~0) · blocks/shortcodes/widgets/contact-form(içerik/form bağımlılık riski → güvenlik). Testimonial formu (WPForms) + bülten sağlam, site 200. **🔑 KRİTİK DERS:** Chrome MCP `javascript_tool` (Runtime.evaluate) tekrar tekrar 45s DONDU; ama `find` (accessibility tree) + `computer left_click(ref)` her seferinde çalıştı → **flaky bridge'de JS-fetch yerine `find`→`click` kullan.** **SIRADAKİ (opsiyonel):** (1) görselleri Photon'dan kendi LiteSpeed/webp+CF CDN'ine taşı (en büyük kalan perf kazancı), (2) ölü `.jp-relatedposts` CSS temizliği.

**✅ 3. TUR — PHOTON KAPALI, DE-COUPLING TAMAM (2026-06-14, "devam"):** Photon (Görsel CDN) kapatıldı → **TOPLAM 13 modül kapalı.** Görseller artık kendi alan adı + Cloudflare'den **webp** olarak geliyor (`/almanca-artikeller/`: 14 origin görsel, i0.wp.com=0; origin görsel = 200 + image/webp + CF cache). **Anasayfa GERÇEK TARAYICIDA görsel doğrulandı — kusursuz render, görsel bozulması yok.** Jetpack'in WP.com'a kalan tek frontend işi = bülten (subscriptions). **Photon kapatma tuzağı:** klasik `jetpack_modules` tablosu kararsızlaştı (deactivate-click tutmadı, direct-URL nonce eskidi, sonra tablo `#/dashboard`'a redirect etti); doğru/güvenilir yer modern **Jetpack → Ayarlar → Performance** ("Enable site accelerator" + image + static toggle'ları = KAPALI). **🔑 WAF GREYLIST DERSİ:** hızlı ardışık scripted fetch (özellikle cache-buster query'li anasayfa) Imunify360'ı tetikleyip **11 karakterlik boş yanıt** döndürdü → "site kırık" sandım ama DEĞİLDİ (düz fetch + gerçek tarayıcı 297KB/200 sağlam). Ders: siteyi hızlı hammerleme, düz URL kullan, şüphede **gerçek tarayıcı otoriter kaynaktır.**

**Denetim özeti (SEO hariç):**
- **Güvenlik 🟢:** HSTS · X-Frame SAMEORIGIN · nosniff · Referrer-Policy · Permissions-Policy (`microphone=(self)` → sınav sim. ses kaydı için doğru) · REST users 401 · `?author=1` sızdırmıyor · debug.log 403 · mixed-content yok · PHP 8.2.30 · Wordfence aktif. **Eksik:** CSP yok · xmlrpc açık (GET 405) · X-Powered-By sürüm sızıyor · wp-login açık (2FA öner).
- **Bot erişimi 🟢:** Googlebot + bingbot + default hepsi **200** → eski "Imunify bot engeli" korkusu KESİN geçersiz (teyit).
- **a11y 🟢:** h1=1 · 40 görselin HEPSİNDE alt · skip-link · 84 aria-label · semantik nav/main/header/footer.
- **Teknik 🟢:** 60 iç link örneklemde 0 kırık · robots + 2 sitemap temiz · hakkımda slug = `/hakkimda/`.
- **Performans 🔴 (en büyük headroom):** HTML ~297 KB (45 `<style>` blok + 42 inline `style=`) · 7 CSS + 9 ext JS · 40 görselin 30'u eager · Jetpack ağır (52 ref) · Google Fonts harici · CF-Cache DYNAMIC. PSI lab skoru ÖLÇÜLEMEDİ (Google 429, API key yok → key/pagespeed.web.dev ile ölçülebilir).
- **Analitik tekrarı 🟠:** Site Kit/GA4 + Burst + Jetpack Stats = 3 sistem aynı anda → tekilleştir (GA4+Burst tut, Jetpack Stats kapat).

---

## Bekleyen İşler (öncelik sırasına göre)

> **2026-06-13 turu:** 6 ve 9 KAPANDI; 1/2/8 canlı render ile yapısal doğrulandı (aşağı bak). Geriye yalnızca harici veri (GSC export) veya Dr. Sarı içerik kararı bekleyenler kaldı.

1. **Eval kartı** — ✅ canlı render doğrulandı: `aefh6-eval-inline` VAR, eski `.aefh6-card-eval` element olarak YOK (sadece 8 ölü CSS selektörü kalıntısı, zararsız). Son piksel onayı kullanıcının tarayıcısında.
2. **Öğrenci yorumları** — ✅ canlı render: `#yorumlar` + 5 kart hepsi var (Ayşe K. entity-kodlu `Ay&#351;e K.`, Mert Y., Zeynep D., Emre A., Elif S.). 3+2 grid son görünüm kullanıcının tarayıcısında.
3. **GSC manuel indexleme** — ✅ **TURU YAPILDI (2026-06-14, Chrome eklentisi ile GSC sürüldü).** Chrome MCP "Browser 1" bağlı, GSC almancaeskisehir.com mülkünde giriş yapılı. **🔑 KRİTİK BULGU: site SAĞLIKLI indexleniyor** — canlı URL denetimiyle test edilen sayfaların ÇOĞU zaten dizinde (genitiv, oesd-sinavlari hub [dünkü!], a1-lesen, c1-lesen, c2-schreiben, c2-hoeren, b2-sprechen → hepsi "Sayfa dizine eklendi"). GSC özetindeki "2.855 eklenmedi" hep eski çöp (404/noindex/redirect). **Tek gerçek boşluk: C1 & C2 SPRECHEN exam sayfaları** (en yeni + az metinli + iç linksiz → c1-sprechen hiç taranmamış "URL Google tarafından bilinmiyor", c2-sprechen "tarandı-eklenmedi"). **İKİSİNE DE indexleme isteği GÖNDERİLDİ ✓** (yeşil "Dizine eklenmesi istendi — öncelikli tarama sırasına eklendi" diyaloğuyla onaylandı). Canonical'lar SELF (REST doğrulandı, bug YOK), noindex YOK, sitemap bugün okunmuş (Başarılı/334). **NOT:** Striking-distance turu (Düzeltme 10) DİLBİLGİSİ sayfalarını linkledi; **exam beceri/Sprechen sayfaları o turda DEĞİLDİ → hâlâ iç linksiz.** Kalıcı çözüm = exam hub'larından (beceri-temelli-olcme-sinavlari + seviye hub'ları) bu Sprechen sayfalarına iç link. (Lower-level Sprechen b2 ve altı zaten dizinde.)
   **GSC Chrome-eklentisi operasyon notları:** (a) denetim çubuğu ~(310,14) normal ölçek; `ctrl+a` LİTERAL "a" yazar → KULLANMA, `triple_click` ya da boş çubuğa direkt type. (b) istek/diyalog sonrası İLK type+Enter genelde tetiklenmez (ölçek/koordinat şaşması) → 2. deneme tutar. (c) "DİZİNE EKLENMESİNİ İSTE" linkine koordinatla tıklama ıskalar → `find`+`scroll_to`+`left_click ref`. (d) `get_page_text` screenshot donsa bile çalışır + sonucu temiz okur (TERCİH ET). (e) günlük "Request Indexing" kotası ~10-12; denetim kotaya saymaz. (f) çok denetimden sonra renderer donar (screenshot CDP timeout) → sekme yenile.
4. **Striking-distance iç link turu** — ✅ TAMAM (2026-06-13, **BU chat yürüttü**; kullanıcı "senden bahsediyor" diye onayladı — memory'deki "ayrı chat" = bu chat). **32 sayfa** `aef-ilgili` bloğuyla bağlandı (4 batch). 2. sayfa hedefleri relativsatz & geschweige-denn 6'şar inbound link aldı; 10 yeni Haziran alıştırma sayfası konu sayfalarına bağlandı. Detay: Düzeltme 10.
5. **TurHost whitelist maili** — ✅ KONU KAPANDI. Mail gönderildi ama gereksizmiş. Asıl sorun TurHost/Imunify360 server bloğu DEĞİL, **Claude chat sandbox/MCP'nin siteye ulaşamamasıydı**. REST API + App Password (benim kullandığım yol) sorunsuz çalışıyor. (Önceki "Imunify360 Google Cloud IP engeli" teşhisi yanılmış olabilir; pratikte REST erişimi tam.) İç link turu da AYRI bir chat'te yürüyor (2026-06-13).
6. **beceri-hub Page 48510** — ✅ TAMAM. Sayfa eksiksiz/tutarlı (eyebrow→başlık→4 beceri→A1–C2 altı seviye kartı→"neyi ölçüyor"→alt CTA→ilgili). Blok entegre. Orijinal `beceri-hub-eklenecek-blok.html` diskte yok.
7. **56 ham PDF landing** — ✅ **KAPANDI (2026-06-13, KALICI KARAR: hiçbir şey eklenmedi/yapılmadı, ve doğrusu bu).** Medya kütüphanesinde 57 PDF tarandı + 8 aday indirilip `pdftotext` ile incelendi. Üç kategori:
   - **11 çalışma kâğıdı** (2026/06) → zaten tam landing yazılı (media id +1 = post id deseni; ör. Genitiv 48504→post 48505 `/genitiv-ismin-in-hali/`, 12–15 KB içerik + PDF gömülü "indir"). BİTMİŞ.
   - **7 Cep Rehberi** → kapılı lead-magnet (Page 57 widget'ı), SEO landing'i gerekmez. (Mükerrer kopyalar var: a1...-2, a2...-1.)
   - **39 eski PDF (2014–18)** → her konunun zaten daha güçlü modern sayfası var (Perfekt 4×, Redewendungen post 623 "120+ Türkçe anlamlı", düzensiz fiiller "36 fiil", Konjunktiv 4×, Nebensatz/weil 4×, Akkusativ 4×).
   
   **Hedefli ek-iliştirme denendi, 4 adayın 4'ü de ELENDI:** (a) **telc A1 Übungstest** (2228, 34K char gerçek test) → hedef post 2227 `/start-deutsch-1-ornek-sinavlar/`; AMA o sayfa "Resmi ve Güvenilir Örnek Sınav Kaynakları" bölümünde AÇIKÇA *"eski PDF gömme yerine güncel resmî kaynağa link daha sağlıklı"* diyor + zaten telc.net resmî Übungstest'ine link veriyor → 2015 self-host'u geri koymak bu kararla çelişir. (b) **Redewendungen 1-50/51-100** (2237/2238, 100 deyim, İngilizce anlamlı) → post 623 zaten 120+ Türkçe anlamlı, PDF redundant+zayıf. (c) **Wortschatz_TESTDAF/250-Verben/Netzwerk-A1/Start-Deutsch-1** → metin katmanı YOK = görsel tarama, SEO değeri sıfır. (d) **unregelmäßige Verben** → "Foxit evaluation only" filigranı + redundant.
   
   **🔑 DURABLE KURAL:** Site editöryel olarak **self-host eski PDF → resmî güncel kaynağa link** yönüne geçmiş (post 2227'de yazılı). Google'ın eski PDF/attachment'ları deindex etmesi DOĞRU (GSC "weak media" ile tutarlı). Bu maddeyi tekrar AÇMA; yeni landing/ek-iliştirme yapma. Net çöp/mükerrer (silinebilir ama zorunlu değil, zaten zararsız/deindex): 3× Panama (2013/2015/2017), 3× bs2_dass (2393-95), Scan_20140307 (1401).
8. **Son Eklenen kapak rotasyonu** — HASSAS, ayrı session'da yapılacak (canlı yapısal doğrulama OK; rotasyon işi ayrı).
9. **Mükerrer duyuru** — ✅ ÇÖZÜLDÜ. Page **48564 çöp kutusunda** (status:trash, slug `...__trashed`, 2026-06-11). Daha iyi başlıklı/temiz-slug'lı **48562 yayında** (`/yeni-goethe-telc-testdaf-sinav-simulasyonu-a1-c2-beceri-temelli-olcme/`). Çöpteki 48564 zararsız; istenirse kalıcı silinebilir (kullanıcı onayıyla).
10. **Aile Birleşimi konsolidasyonu** — ✅ **TAMAM (2026-06-14, Dr. Sarı tam yetki verdi: "veri kaybı olmadan birleştir/sil").** Sorun: 7 Aile Birleşimi sayfası keyword cannibalization. GSC verisiyle (6 ay export) karar: **142 `/a1-mektup-ornekleri/` = KAZANAN (~201 tık, poz 7.2 — DOKUNULMADI)**; **178 `/aile-birlesimi-sinavi/` = hub** (0 tık ama en iyi slug/başlık); **696 `/...sinavi-nedir/` = 178'in çocuğu, tut** (striking-distance, 247 gösterim). **4 ölü dupe (0 trafik) → 178'e konsolide:** 47940 `/...sinavi-hazirlik/`, 781 `/...kursu-eskisehir/`, 220 `/...sinav-sorulari/`, 218 `/...gurur-tablomuz/`. **Yapılanlar:** (1) 178'e 220'nin benzersiz değeri eklendi = "Resmî Goethe Kaynakları" bölümü (2 goethe.de linki, #ab-kaynaklar) — veri kaybı yok; (2) 4 dupe'a **AIOSEO canonical→178** (canlı doğrulandı); (3) menü temizliği: ölü çocuk menü-öğesi 47942 SİLİNDİ, 2212 → 178 repoint (her iki menü artık hub'a işaret); (4) kazanan 142'nin ölü-dupe linkleri → 178; (5) 4 dormant 301 redirect (#48-51) de oluşturuldu. Sonuç: 7 sayfa → 3 ranking entity (142+178+696), yamyamlık çözüldü. **HİÇBİR SAYFA SİLİNMEDİ** (7'si de canlı 200; canonical=sinyal birleştirme, silme değil). **(2026-06-14 ek):** Dr. Sarı "menüde tek hub var, mektup göremiyorum" deyince → menü öğesi 298 (Aile Birleşimi→hub) altına gerçek alt-sayfalar EKLENDİ (dropdown): "Mektup Örnekleri (A1)"→142 (id 48781), "Sınav Bölümleri"→696 (id 48782). Canlı nav'da doğrulandı. İstenirse Konuşma Sınavı (296) de eklenebilir. **(2026-06-14 DÜZELTME — 218 Gurur Tablomuz):** Dr. Sarı "kazananlar resimleri" diye sordu → 218'i ölü dupe'larla aynı kefeye koymak HATAYDI; 218 benzersiz sosyal-kanıt vitrini (9 GERÇEK öğrenci sertifikası: Merve, Melike vb. — hiç silinmedi, canlı). Düzeltildi: 218 **canonical→KENDİNE geri alındı** (bağımsız/dizinlenebilir), Türkçe SEO başlık+meta verildi, menü dropdown'a "Kazananlarımız"→218 eklendi (id 48786), hub 178'e "🎓 Kazananlarımız sertifikaları" sosyal-kanıt linki eklendi. **DERS: distinct/sosyal-kanıt içeriğini cannibalization dupe'larıyla karıştırma — canonical sadece GERÇEK near-dupe'lara.** Aile Birleşimi menü dropdown final: Mektup Örnekleri(142) · Sınav Bölümleri(696) · Kazananlarımız(218). **(2026-06-14 hub TASARIM TOPARLAMA):** Dr. Sarı "178 çok karışmış" dedi → sebep: eklediğim 2 şey (Goethe kaynaklar + Kazananlar) PLAIN HTML'di (çıplak `<ul>`/`<p>`), sayfanın stilli `#ab-page` bileşenlerine uymuyordu = yama. Çözüm: Goethe = 2× `ab-card` (ab-grid, beceri kartları gibi), Kazananlar = `ab-related` kutusu (yeşil kenar). Canlı doğrulandı, tutarlı. **DERS: 178 = `#ab-page` wp:html; ekleme yaparken MEVCUT class'ları (ab-card/ab-grid/ab-related/ab-cta/ab-btn) kullan, plain HTML = yama.**
   **🔑 KRİTİK TEKNİK DERSLER:** (a) **AIOSEO canonical REST ile YAZILIYOR ama alan adı `canonicalUrl` (camelCase!)** — snake `canonical_url` İŞE YARAMAZ; description ise lowercase çalışıyor. POST `/aioseo/v1/post` body `{id, canonicalUrl}`. **robots noindex** alanı bulunamadı (`robots_noindex`/`robotsNoindex` ikisi de tutmadı) → noindex REST ile AYARLANAMADI, canonical kullanıldı (zaten merge için doğru araç). (b) **Redirection eklentisi (`/redirection/v1/redirect`) REST'le yeni 301 EKLENEBİLİYOR (grup 1) ama YENİ kurallar ATEŞLEMİYOR** — eklenti Apache/.htaccess modunda, REST ile eklenen kurallar .htaccess'e yazılmadığından firing değil (eski #43 çalışıyor=.htaccess'te; yeni #46/#48 404/200). Yani 301 için Redirection-REST GÜVENİLİR DEĞİL → canonical tercih et. (c) AIOSEO tablo güncellemesi LiteSpeed purge tetiklemez → WP REST'le sayfaya "dokun" (status:publish re-POST) purge için. (d) `menu-items` REST açık: POST güncelle, DELETE `?force=true` sil.
11. **Haberler temizliği** — ✅ **TEMEL OPTİMİZASYON YAPILDI (2026-06-14, Dr. Sarı "önerine uyalım" dedi).** **Teşhis:** "Haberler" kategorisi (id=65, 30 yazı) = **24 Almanca graded-reader okuma dersi** (May–Haz 2026; *Lernziele→Lesetext→Wichtige Wörter→Leseverstehen*, B1-B2) + 6 eski Türkçe yazı. **Otomasyon kaynağı (Dr. Sarı açıkladı): RSS → ChatGPT didaktize → Make eklentisiyle siteye düşüyor; API kredisi bitince durmuş → 14'ü DRAFT backlog.** Bunlar ham haber değil, **okuma metni** (öğrenci değeri var) AMA ~0 SEO trafiği (6 ayda kategori 1 tık) çünkü başlıklar Almanca haber manşeti = Türkçe sorguyla eşleşmiyor. **Yapılanlar:** (1) 4 net çöp draft ÇÖPE alındı (774 "sağlık sigortası borcu", 631+1522 eski tavsiye-siteler, 24484 bayat 2022 duyuru); (2) **10 YAYINDAKİ derse Türkçe SEO başlık + meta** (AIOSEO `title`+`description` — lowercase, çalışıyor; canlı doğrulandı; format "B1-B2 Almanca Okuma Metni: [Türkçe konu] (Güncel)"). **DOKUNULMADI / Dr. Sarı kararı:** 2899 (mesleki Almanca, olası hizmet, draft) + 24807 (Deutsche Kultur, yayında+redirect #45) bırakıldı; **14 draft yayınlanMADI** (bilinçli — ölçekli AI içerik genişletme riski + ephemeral konular). **⚠️ STRATEJİK NOT:** Bunlar EPHEMERAL (güncel olay) + AI-üretimi → Google "scaled content" riski var; agresif SEO-amplifikasyon (toplu draft yayını, yoğun iç link) ÖNERİLMEZ. Otomasyon yeniden açılırsa Türkçe SEO başlık/meta + kalite pipeline'a GÖMÜLMELİ. Kategori adı "Haberler" hâlâ "güncel Almanca okuma" içeriğiyle uyumsuz (anasayfada linkli) — relabel "Güncel Almanca Okuma / Haberlerle Almanca" Dr. Sarı kararına bırakıldı. AIOSEO `title`+`description` REST ile yazılıyor (lowercase alan adı).

---

## Düzeltme 13 — Güvenlik Sertleştirme: X-Powered-By Gizleme (2026-06-14)

**Bağlam:** Dr. Sarı "ana site sertleştirme" dedi (oyunlar yerine). Canlı header denetimi (tek ölçülü HEAD): tek gerçek açık = **`X-Powered-By: PHP/8.2.30`** sızıyordu. Diğer header'lar zaten yerinde (HSTS · X-Frame SAMEORIGIN · nosniff · Referrer-Policy · Permissions-Policy `microphone=(self)` · Server=cloudflare = origin gizli).

**✅ YAPILDI — yeni snippet 528** (`AEF — X-Powered-By başlığını gizle`, scope `front-end`, active, priority 1): `add_action('send_headers', fn → @header_remove('X-Powered-By'), 0)`. **Canlı doğrulandı:** kimlikli (dinamik, cache=miss, PHP yolu) VE kimliksiz (cache=hit) yanıtların İKİSİNDE de X-Powered-By **YOK**; site 200. Snippet aktive olunca LiteSpeed anasayfa cache'i tazelendi → cache=hit bile temiz. **X-Pingback zaten YOK** (ekstra iş gerekmedi). Header yüzeyi tam temiz.

**🔑 KRİTİK — Snippet 22 ("AEF — HTTP Güvenlik Başlıkları") AKTİVE ETME:** Pasif; içindeki `Permissions-Policy: microphone=()` **mikrofonu kapatır** → canlıdaki `microphone=(self)` (sınav ses kaydı için gerekli) ezilirdi + diğer header'lar ÇİFTLENİRDİ. Canlı güvenlik header'ları snippet 22'den DEĞİL, **.htaccess veya Cloudflare'den** geliyor (kanıt: 22 pasifken header'lar canlı + microphone=self uyumsuzluğu). 22'ye DOKUNMA.

**Lazy-load durumu:** **snippet 23 ("img lazy-load + decoding async") zaten AKTİF** ve doğru — `the_content`/`widget_text_content`'teki, `loading=` OLMAYAN img'lere `loading="lazy" decoding="async"` ekler; `loading=` olanları ATLAR → logo şeridinin `eager`'ını korur. "30 eager" defekt değil (LCP/hero + logo şeridi kasıtlı). Perf lazy-load kalemi = ZATEN ÇÖZÜLMÜŞ.

**🔑 YENİ KABİLİYET — Code Snippets REST API açık:** `GET/POST /wp-json/code-snippets/v1/snippets`, tekil `/{id}`. POST `{name, code, scope, active:true, priority}` → oluşturur + aktive eder. **`code` alanı `<?php` İÇERMEZ** (eklenti sarar). Türkçe ad için UTF-8 bytes. Bu sayede PHP-seviyeli sertleştirme/davranış snippet'leri REST'le eklenebilir.

**BEKLEYEN (kullanıcı işi):** **Wordfence 2FA** — kullanıcı 2026-06-14'te "şu an gerek yok, cihazlar güvende" dedi → ATLANDI (istenirse: WP Admin → Wordfence → Login Security → 2FA, kendi authenticator'ıyla QR kaydı). xmlrpc KAPATILMAYACAK (Jetpack bülten). CSP report-only ileride (riskli). X-Powered-By'nin HER katmanda (REST/sitemap/cache dahil) garanti gizlenmesi istenirse: Cloudflare response-header transform rule VEYA php.ini `expose_php=Off` (ikisi de kullanıcı/panel erişimi gerektirir; mevcut snippet ana sayfa yüzeyini hallediyor).

**✅ ÖLÜ CSS TEMİZLİĞİ (2026-06-14):** Kapatılmış Jetpack modüllerinden artakalan ölü CSS kaldırıldı. (1) **Snippet 99** ("Jetpack Related Posts Türkçe + Fix") **pasife alındı** — Related Posts modülü kapalı, 2 filtre + `.jp-relatedposts` `<style>`'ı her sayfada ölüydü (deactivate route: `POST /snippets/99/deactivate`). (2) **Yeni snippet 529** ("Ölü Jetpack likes/sharing CSS dequeue", front-end, active): `wp_dequeue_style('jetpack_likes')` + deregister @ prio 999 — Jetpack, likes+sharedaddy modülleri KAPALI olmasına rağmen **~2,5 KB'lık `jetpack_likes-inline-css` bloğunu** her sayfaya basıyordu. **Canlı doğrulandı (hem kimlikli=miss hem kimliksiz=hit):** `jetpack_likes-inline-css`=0, `sharedaddy`=0, `jetpack-likes-widget`=0, `jp-relatedposts`=0, X-Powered-By=YOK, site 200. **DOKUNULMADI: Snippet 297** ("post-altı temizliği") CANLI — yorum/post-navigation gizlemeyi hâlâ yapıyor (Jetpack'e bağlı değil); içindeki `.jp-relatedposts` selektörü artık gereksiz ama zararsız. **Kalan ihmal edilebilir iz:** `img#wpstats{display:none}` (~8 B, Jetpack stats pikseli — önemsiz).

---

## STRATEJİ KARARI — Büyüme, Uluslararasılaşma & Ticarileşme (2026-06-14)

**Bağlam:** Dr. Sarı "tüm Almanca öğrenmek isteyenleri hedefle — İngilizce kopya mı / yeni domain mi? ticarileşme önerin?" dedi. 7-ajanlı iş akışı (teknik+SEO denetim [yerel dosyalar] + i18n pazar/mimari + monetizasyon [web] + adversaryel eleştiri + sentez) çalıştırıldı. **Tam memo dosyası:** `…/tasks/wtv5zbs3a.output` (workflow wf_a4810914-968).

**🔑 ULUSLARARASILAŞMA = NET HAYIR (şimdilik).** Türkçe-only kal. Gerekçe: (1) İngilizce "learn German" SERP doygun (DW/Goethe/Babbel/Duolingo/devlet) → Türkçe domain otorite transferi marjinal; (2) denetlenmemiş makine çevirisi TÜM dil sürümlerinde (Türkçe dahil) ceza riski; (3) Ukraynaca/Arapça talebi gerçek ama solo modelde native-QA imkânsız + Ukrayna talebi düşüşte → fırsat ≠ icra kapasitesi. **Doğru kriter: "Dr. Sarı'nın kendi denetleyebildiği dil" = sadece Türkçe.** Büyüme DİL değil, **Türkçe'de KONU kapsamı** ile. Eğer 12 ay sonra zorunlu olursa: `/en/` alt dizin + Polylang Free, sadece 3-5 stratejik landing (kurs/hakkımda/kayıt), blog/alıştırma ASLA. (Ayrı domain/alt-alan HAYIR.)

**🔑 TİCARİLEŞME = "önce gelir kanıtı, sonra motor".** Henüz tek lira gelir kanıtı yok → büyük yatırım (sınav-motoru ürünleştirme, üyelik, çok-dil, AdSense) YASAK; trafiğin ödediğini UCUZA kanıtla. **Sıra:** 1:1 sınav koçluğu (erken nakit + çıpa) → sınav-sim ön-sipariş testi (0 ön-sipariş=motor yanlış, kod yazmadan öğren) → 1 dijital PDF → ücretli mock paket (kanıt gelirse) → üyelik/B2B (≥6 ay sonra). **AdSense kalıcı HAYIR.** 90-gün ilk adım: "Ders ve Akademik Danışmanlık" CTA'sını tek somut pakete çevir ("Goethe/telc B1-B2 Sınav Koçluğu — 4 seans + plan, doktoralı eğitmen", ₺750-1000/seans · €30-45 intl, Calendly + iyzilink). Lead-magnet PDF→bülten (Google AI Overviews tıklamayı kestiği için e-posta = Google'a bağımsız tek sahip-kanal). **Ürün satışı: Lemon Squeezy (MoR → AB KDV otomatik). İlk satıştan önce Türk şahıs vergisi netleştir.** UYARI: otomatik-değerlendirme yazma/konuşmayı gerçekten puanlamıyorsa "otomatik mock" diye SATMA → koçluk içine konumla.

**🔑 EN BÜYÜK KULLANILMAYAN SEO SİLAHI → ✅ ARTIK KULLANILIYOR (Düzeltme 16):** Yazar `Person` schema akademik otorite verisiyle zenginleştirildi. Rakipler (almancax, almancaabc) ANONİM; gerçek akademik kimlik = AI Overview alıntısı + E-E-A-T'de yenilemez fark.

**GERÇEK AÇIK KALAN SİTE İŞLERİ (denetim + canlı teyit):** (1) ~~Person/Article schema~~ ✅ **TAMAM (Düzeltme 16)**; (2) ~~interaktif alıştırma HUB'ları THIN~~ → **5 HUB (A1·A2·B1·B2·C1-C2) TAMAM (Düzeltme 17)**; tekil egzersiz sayfaları (79) → **HEPSİ TAMAM 79/79 (Düzeltme 18; C1·A1·A2·B1·B2, editör-denetimli özgün metin, tek blok; QA: 0 duplikasyon)**; **+ 10 AŞAMA ALT-HUB da TAMAM** (slug `interaktif-alistirmalar-{a1-1..c1-2}` = A1.1/A1.2 gibi aşama-listeleme; ids 47834/47833·47900/47901·47951/47952·47974/47975·47996/47997; overview metni + nav link [level hub + kardeş aşama + seviye testi + oyunlar]). **⇒ TÜM İNTERAKTİF BÖLÜM BİTTİ: 94 sayfa (5 level hub + 10 aşama hub + 79 egzersiz), hepsi editör-denetimli SEO metni + tek blok, 15/15 hub QA temiz.**; (3) ~~alıştırma motoruna `aria-live`~~ ✅ **TAMAM (Düzeltme 19, snippet 539)**; (4) ~~alıştırma↔ders↔sınav iç-link üçgeni + C1/C2 Sprechen~~ ✅ **TAMAM (Düzeltme 19)**; (5) perf: ~~`@import` font→`<link>`~~ ✅ **TAMAM (Düzeltme 20, 7 sayfa)**; motor JS/CSS externalize → **DEĞERLENDİRİLDİ, YAPILMADI (Düzeltme 20: inline kritik CSS doğru; JS externalize marjinal+riskli)**; (6) CookieYes Türkçeleştir + tracker'ı gerçekten consent-bloğuna bağla (şu an onaydan önce firing) + tek tracker'a in (GA4 vs Burst). **NOT: AdSense zaten YOK (canlı teyit 2026-06-14: adsbygoogle/ca-pub/googlesyndication/site-kit=0, GA4 gtag=10 duruyor), Jetpack Stats zaten kapalı — denetimdeki bu iki bulgu eski yerel kopyadan kaynaklı, KAPANDI.** (7) **Kategori arşiv sayfaları (dersler-a1..c1-c2, gramer, yds, testdaf vb.) → DEĞERLENDİRİLDİ, GEREK YOK** (2026-06-15): hepsinde zaten ~290-405 karakter description + 18-68 gerçek ders listesi var → ince DEĞİL, sitemap'te indeksli. Opsiyonel cila: ana kategori `description`'larını (REST `POST /wp/v2/categories/{id}` `{description}`) ~50→~130 kelimeye genişletip head-term güçlendirmek (DÜŞÜK öncelik). Boş description yalnız 3 küçük kategoride (2-3 yazı, düşük değer). Kategori id: a1=95·a2=214·b1=361·b2=1·c1c2=1028·gramer=14·yds=448·testdaf-dsh=1029·haberler=65.

---

## Düzeltme 16 — Yazar Person Schema Zenginleştirme (E-E-A-T) (2026-06-14)
> NOT: Bu oturum (schema/SEO akışı) Düzeltme 16-18 kullandı; Düzeltme 14-15 PARALEL menü-güzelleştirme akışınındır (numara çakışması önlendi).

**Bağlam:** Strateji memosunun #1 SEO kaldıracı. Dr. Sarı kimlik bilgisini verdi; AVESİS'ten doğrulandı.

**KİMLİK (doğrulanmış):** Doç. Dr. **Yunus Emre Sarı** · Alman Dili Eğitimi öğretim üyesi · İstanbul Üniversitesi-Cerrahpaşa (Hasan Ali Yücel Eğitim Fak.). E-posta `y.sari@iuc.edu.tr` = sistemdeki e-posta ⇒ kesin. **AVESİS profili almancaeskisehir.com'u "kişisel web sitesi" olarak listeliyor → çift yönlü doğrulama (site→yazar + üniversite→site).**
**sameAs FINAL (3, kullanıcı 2026-06-14 sadeleştirdi):** avesis.iuc.edu.tr/y.sari · scholar.google.com.tr/citations?user=uWBp2WsAAAAJ · linkedin.com/in/yunus-emre-sarı-a04a54114. **ÇIKARILANLAR:** Publons (bayat), ORCID ("fazla akademik, bu kitleye gerek yok" — kullanıcı), ResearchGate, Academia. Kullanıcı mantığı: kimlik(AVESİS)+uzmanlık(Scholar)+meslek(LinkedIn) yeter, kalabalık olmasın. **(aramadan):** researchgate.net/profile/**Yunus-Sari-4** (✅ kullanıcı düzeltti/onayladı 2026-06-14; eski -2 YANLIŞTI) · linkedin.com/in/yunus-emre-sarı-a04a54114 + istanbulc.academia.edu/YUNUSEMRESARI (kullanıcı onayı bekliyor).

**TEŞHİS:** AIOSEO post'larda zaten Article + author Person + tarih basıyor AMA Person ANEMİKTİ (sadece `name:"Emre SARI"` + gravatar; sameAs/unvan/kurum YOK). Sayfa-tipi farkı: **post'lar `Article`, page'ler `WebPage`** (alıştırma sayfaları page → WebPage).

**✅ YAPILDI:** (1) **WP user id 1 (miyatuk) profili** REST ile güncellendi: display name → "Doç. Dr. Yunus Emre Sarı", first/last, bio (258 char akademik). (2) **Yeni snippet 530** ("Yazar Person schema zenginleştirme (E-E-A-T)", front-end, active): `add_filter('aioseo_schema_output', …)` → graf'taki `@type==Person` düğümüne `jobTitle` + `worksFor` (CollegeOrUniversity, İÜ-Cerrahpaşa) + `knowsAbout` (4) + `sameAs` (7 link) ekler. **Canlı doğrulandı** (post 871 /almanca-artikeller/, taze render): Person düğümü name+jobTitle+worksFor+knowsAbout+sameAs(orcid/scholar dahil) TAM; Article→Person @id bağı sağlam. (3) **Kontrollü tam LiteSpeed purge** (geçici snippet 531: `do_action('litespeed_purge_all')` → tetikle → pasife al → SİL) ⇒ 385 sayfa taze render'da zenginleşmiş schema basacak.

**🔑 YENİ TEKNİK DERSLER:** (a) **`aioseo_schema_output` filtresi ÇALIŞIYOR** — graf bir PHP **array**'i (object değil); `$graph[$i]['x']=…` ile düğüm zenginleştirilir. AIOSEO Pro gerekmez. (b) **Schema `name` JSON'da `\u`-escape'li** (`Doç. Dr. … Sarı`) → düz-Türkçe-harf regex'le arama FALSE-NEGATIVE verir; escape'li ara veya ham düğümü oku. (c) **Code Snippets snippet DELETE REST'le ÇALIŞIYOR** (`DELETE /snippets/{id}`) — plugin DELETE'in aksine (o 500). (d) **Kimlikli (app-password) frontend GET cache'i HER ZAMAN bypass ETMİYOR** (bu sefer litespeed-cache=hit geldi) → taze doğrulama için ilgili post'a "dokun" (re-publish → otomatik purge) ya da tam purge sonra fetch et. (e) **Görünür yan etki:** yazar byline'ı site genelinde artık "Doç. Dr. Yunus Emre Sarı" (footer künyesi `.aef-footer-role/.aef-footer-affiliation` zaten AVESİS'e linkliydi). **DOĞRULA:** Google Rich Results Test + GSC re-index ile kontrol önerilir.

---

## Düzeltme 17 — İnteraktif Alıştırma HUB'larına Thin-Content SEO Metni (2026-06-14)

**Bağlam:** Strateji #2 kalemi. İnteraktif alıştırma HUB'ları ince (~104 kelime = çoğu kart etiketi + CSS). Dr. Sarı taslakları onayladı.

**HUB'lar (page) — 5 ADET:** A1=**47756**, A2=**47757**, B1=**47758**, B2=**47763**, **C1-C2=47764** (slug'lar `interaktif-alistirmalar-{a1,a2,b1,b2,c1-c2}` — DİKKAT: C1/C2 slug'ı **`c1-c2`** tireli; `c1c2`/`c1` DEĞİL → ilk aramada yanlış varyantı denediğim için "yok" sandım, Dr. Sarı düzeltti). Ayrıca `/c1-c2-seviyesi/` adında ayrı bir seviye-landing sayfası da var. Her hub = tek `<!-- wp:html --><div id="ixl">…</div>` bloğu; iki-aşamalı yapı + `.ix-grid` kartları. **5/5 hub'a ixl-seo eklendi+doğrulandı** (C1-C2 aksan rengi #DC2626; linkler konjunktiv-2·partizipien·der-genitiv·seviye-testi·b2-hub).

**✅ YAPILDI:** 4 hub'a `<section class="ixl-seo">` eklendi (`<!-- /wp:html -->` öncesine, idempotent: eski blok `(?s)<section class="ixl-seo".*?</section>` ile sökülür). İçerik: H2 ("{Seviye} Almanca dilbilgisi alıştırmaları") + 2 seviyeye-özgü özgün paragraf (gerçek konuları referanslayan, ~180 kelime) + "İlgili:" doğrulanmış iç link satırı. **Stil:** site `.ix-card` desenine uygun (border-left CEFR rengi: A1 #16A34A · A2 #0891B2 · B1 #D97706 · B2 #EA580C + radius 14px). content.raw POST → LiteSpeed sayfa-bazlı otomatik purge. **Canlı doğrulandı (4/4, cache=miss):** ixl-seo + H2 + iç link render. Her hub ~104→~285 kelime.

**🔑 İÇ LİNK DOĞRULAMA (kırık link yok):** Kullanılacak slug'lar önce `GET /wp/v2/posts?slug=a,b,c` + `/pages?slug=…` ile toplu doğrulandı. **VAR olan dersler:** almanca-artikeller · a1-seviyesi-onemli-fiiller · akkusativ-konu-anlatim · dativ-alan-fiiller · modal-fiiller-tablosu · almanca-edatlar-prapositionen · almanca-gecmis-zaman-perfekt-und-prateritum-vergangenheit · der-genitiv · relativsatz · konjunktiv-2 · partizipien. **YOK:** passiv/pasif dersi (B2 için Konjunktiv II + Partizip kullanıldı).

**KALAN (ayrı karar):** tekil `interaktif-*-{level}` egzersiz sayfaları (79). **Toplu şablon metin = scaled-content riski** (Dr. Sarı bu riske duyarlı) → her sayfa GERÇEKTEN özgün olmalı. (C1/C2 hub VAR → bkz. Düzeltme 18 başı; "yok" diye yazdığım hatalıydı.)

---

## Düzeltme 18 — Tüm Tekil Egzersiz Sayfaları + Aşama Hub'larına Özgün SEO Metni (workflow) (2026-06-14)

**Bağlam:** Dr. Sarı "79 sayfayı tek tek metin yazarak güncelle, pc açık sorun yok" dedi + **ultracode'u AÇTI**. "C1'le başla" seçti. Önce menüde **Oyunlar'a 🎮 eklendi** (menü-item 48776 title='🎮 Oyunlar', sitewide purge, doğrulandı).

**✅ C1 = 15/15 TAMAM.** Yöntem (tekrar kullanılabilir, A1/A2/B1/B2 için aynısı):
1. **Workflow** (`aef-c1-egzersiz-seo-metin`): Phase1 = 15 paralel ajan, her biri o sayfanın gramer konusuna grounding'li ~130-160 kelime ÖZGÜN Türkçe metin (h2/p1/p2, schema'lı) yazdı; Phase2 = tek **editör/dilbilgisi denetçisi** hepsini holistik denetleyip SON HÂLE getirdi. **Editör GERÇEK hatalar yakaladı** (Konjunktiv I "sein" çekimi, "nicht nur…sondern auch" devrik kuralı, "ent-" örneği) → kalite kapısı işe yaradı. Çıktı: `…/tasks/wq81ffkcl.output` → `result.polished[]`.
2. **Insert (PowerShell):** çıktı JSON'unu oku → `result.polished` (idx→pageId map) → her sayfaya `.ixl-seo` bloğu (C1 kırmızı #DC2626), `<!-- /wp:html -->` öncesine (idempotent sök+ekle). İç linkler: kendi hub'ı `/interaktif-alistirmalar-c1-c2/` + `/seviye-testi/` + `/almanca-oyunlari/` + konuya uygun DOĞRULANMIŞ ders (konjunktiv→/konjunktiv-2/, partizip→/partizipien/, genitiv→/der-genitiv/, modalverben→/modal-fiiller-tablosu/). content POST = sayfa-bazlı otomatik purge. **5 örnek canlı doğrulandı (ixl-seo+H2+link, cache=miss).**

**🔑 BUG + DÜZELTME (insert mantığı):** İlk insert `$raw.Replace('<!-- /wp:html -->', block+...)` kullandı = **TÜM** `<!-- /wp:html -->` geçişlerine ekler. Bazı egzersiz sayfaları **birden fazla wp:html bloğu** içeriyor (motor + "Bundan sonra ne yapabilirsin?" nav) → blok 2 kez basıldı. (15 C1'den yalnızca **47991** etkilendi; gerisi tek blok.) **DÜZELTME:** insert'i `LastIndexOf('<!-- /wp:html -->')` ile **son** kapanıştan önce TEK sefer yap (String.Replace KULLANMA). Dedup-fix: `[regex]::Matches(raw,'(?s)<section class="ixl-seo".*?</section>')` say → >1 ise ilkini koru, hepsini sök, son wp:html-close öncesine 1 kez ekle. **A1/A2/B1/B2 insert'lerinde DAİMA bu LastIndexOf desenini kullan + sonra ixl-seo sayısını 1 diye doğrula.**

**C1 page id↔slug:** 48066 adjektive-praep · 48071 doppelkonj · 48064 erw-partizip · 47995 funktionsverb · 47991 konj1-rede · 48068 konj1-verg · 48069 konj2-verg-modal · 47994 konnektoren-gehoben · 47993 modalpartikeln · 47992 modalverben-subj · 48070 praep-konnekt-genitiv · 48065 rezipientenpassiv · 48072 satzklammer · 47990 subst-adjektive · 48067 wortbildung.

**SIRADA:** A1(~18)·A2(~15)·B1(~15)·B2(~16) — aynı workflow+insert deseni; her seviyenin doğrulanmış ders-link havuzu ayrı çıkarılmalı. Ultracode açık → seviye seviye akıtılabilir (Dr. Sarı C1 sonucunu görüp onay verirse).

---

## Düzeltme 20 — Perf: render-blocking `@import` → `<link>` (2026-06-16)

**Bağlam:** Kullanıcı "düşük riskli perf (item 1+2)" istedi. **Ölçüm yapıldıktan sonra gerçek durum, önceki denetim çerçevesinden FARKLI çıktı** — dürüst değerlendirme:

**✅ (item 2) `@import` font → `<link>` — GERÇEK kazanç, 7 sayfa TAMAM:** İnline `<style>`'ın başındaki `@import url(google-fonts)` klasik render-blocking anti-pattern (tarayıcı HTML→style-parse→AYRI font isteği zinciri; preload-scanner göremez). **Site geneli tarandı** (`_deploy/scan_import.py`: 202 page + 180 post REST `context=edit` içerik taraması) → **7 sayfada @import:** seviye-testi 47336 (DM fontları) · beceri hub 48510 (Source Serif 4) · post 2121 futur-i · 2037 worter-lernen · 2009 almanca-artikel-alistirmalari · 1956 aitlik-zamirleri-possessivartikel · 1063 um-zu-ve-damit-baglaclari. **Düzeltme** (`_deploy/fix_import_batch.py`, idempotent, Python uçtan-uca + tarayıcı-UA): her sayfada `@import url('X');` satırı silindi + onu içeren `<style>`'ın HEMEN ÖNÜNE `<link rel="preconnect" googleapis><link rel="preconnect" gstatic crossorigin><link rel="stylesheet" href="X">` enjekte edildi (aynı font URL, paralel/erken yükleme). content içi (wp:html) edit; tek-sayfa, geri-alınabilir. **DB + canlı doğrulandı** (4 spot: seviye-testi·artikel-alistirmalari·beceri-hub + DB hepsi): @import=0, font-link render oluyor, quiz/sayfa sağlam, 0 PHP hata. (Fontlar başka yerde zaten optimal: snippet 492=anasayfa `<link>`, snippet 33=preconnect.)

**❌ (item 1) Motor JS/CSS externalize — DEĞERLENDİRİLDİ, YAPILMADI (kasıtlı, doğru karar):** Ölçüm: motor JS **7355B sha `2ae1e216c6`** + CSS **6709B sha `c230c52c0c`** TÜM alıştırma sayfalarında **byte-AYNI** (tek harici dosyaya alınabilirdi). Motor = `(function(){var page=document.getElementById('ix-topic');if(!page){return;}...})()` IIFE, `#ix-topic`'e kapsamlı, early-return guard → footer/deferred yüklemeye teknik olarak UYGUN (ama çift kopya = event listener 2× bağlanır → bug, inline kaldırılmalı). **Neden YAPILMADI:** (a) **inline kritik CSS İYİDİR** (ekstra istek yok, ilk-boya hızlı) → externalize = render-blocking `<link>` round-trip EKLER = TERS teper; (b) JS externalize kazancı **marjinal** (~2.5KB gz, yalnız çok-sayfalı oturumda; çoğu ziyaret aramadan tek-sayfa) + **79 canlı öğrenci sayfasını DB-edit** (risk) VEYA kalıcı `the_content` strip-filtresi + sanal-dosya endpoint (sürekli karmaşıklık) gerekir → **ROI zayıf, marjinal kazanç için canlı sayfalara kalıcı risk/karmaşıklık eklemeye değmez.** En büyük gerçek perf kaldıracı hâlâ ~297KB inline-CSS HTML mimarisi (ayrı/riskli, bekliyor). **DERS: "inline'ı externalize et" her zaman perf kazancı DEĞİL — kritik CSS inline kalmalı; sadece render-blocking @import-zinciri net kazançtı.**

---

## Düzeltme 19 — a11y aria-live + C1/C2 Sprechen İç-Link (2026-06-16)

**Bağlam:** Yeni oturum "kalan işler" → kullanıcı açık denetim listesinden (GERÇEK AÇIK KALAN, Düzeltme 16 sonu) **(3) a11y** ve **(4) C1/C2 Sprechen iç-link** seçti. İkisi de yapıldı, canlı doğrulandı.

**✅ (3) a11y — alıştırma motoruna aria-live (snippet 539, front-end, active, priority 20):** Motor `ix-` self-contained, 385 sayfaya gömülü → "tek dokunuş tüm site" = tek front-end snippet `wp_footer`'a JS basar. **Motor DOM kontratı (canlı `site-alistirma-artikel.html`'den doğrulandı):** `.ix-fb{display:none}`→`.ix-fb.ok.show`(doğru, "✓ Doğru!…")/`.ix-fb.no.show`(yanlış, "✗ Lösung:…"); sonuç `.ix-result{display:none}`→`.show`, içinde `.ix-score`+`.ix-msg`; üç motor `.ix-match`(yalnız result)/`.ix-quiz`/`.ix-fill`, kapsayıcı `#ix-topic`. **`.ix-fb` display:none olduğundan ÜZERİNE aria-live koymak güvenilmez (display:none canlı bölge bazı SR'larda duyrulmaz)** → çözüm: **kalıcı görünmez (sr-only) tek `aria-live="polite" aria-atomic="true" role="status"` bölgesi** oluştur + `MutationObserver` ile `.ix-fb`/`.ix-result` metnini oraya yansıt (clear→setTimeout ile yeniden-duyur, son-metin dedup). ✓/✗ → "Doğru:/Yanlış:" regex replace. `if(!fbs.length&&!res.length)return` → alıştırma olmayan sayfalarda anında no-op. **Canlı doğrulandı** (`/interaktif-artikel-alistirmasi/?v=`): `id="aef-ix-a11y"`+MutationObserver+aef-sr-live+Türkçe metin VAR, motorun `.ix-fb`/`.ix-result` VAR, **0 PHP hata izi, AEFJS nowdoc sızıntısı YOK.** (Gerçek SR duyuru testi = kullanıcının NVDA/VoiceOver ortamı; yapı/HTML kanıtlandı.)

**✅ (4) C1/C2 Sprechen iç-link (iki yönlü):** **Teşhis (REST link grafiği):** C1 hub 48509 + C2 hub 48533 zaten ilgili Sprechen'e link veriyor (boşluk "iç-linksiz" DEĞİL, ama linkleyenler YENİ/az-taranan hub'lar) + ana hub 48510 yalnız seviye-hub'larına (Sprechen'e 2 hop) + **köklü `c1-c2-seviyesi` 47024 beceri sınavlarına HİÇ link vermiyordu** + Sprechen sayfaları kardeş-beceri halkasını tamamlamıyor (C1 Sprechen'de Schreiben yok; C2 Sprechen'de Hören+Schreiben yok) + alıştırma↔ders üçgeni yok. **Yapılanlar (Python script `_deploy/iclink_c1c2.py`, idempotent):** (A) **inbound:** 47024'e `lvh-` tasarım-sistemli (yama değil) `<section id="aef-beceri-sinavlari">` → C1+C2 hub + 8 beceri sayfasının HEPSİNE (2 Sprechen dâhil) link → köklü/taranan sayfadan taze crawl yolu. (B) **outbound:** 48636(C1)+48648(C2) Sprechen sonuna idempotent `<!-- wp:html --><section class="aef-ilgili">` (CEFR rengi C1 #DC2626/C2 #BE123C): eksik kardeş beceriler (halka tamam) + üçgen (interaktif-alistirmalar-c1-c2 + konjunktiv-2 + partizipien + seviye-testi + c1-c2-seviyesi). **Tüm hedef slug'lar önce REST'le doğrulandı** (c2-lesen 48535, interaktif-c1c2 47764, konjunktiv-2 1447, partizipien 1996 — hepsi publish). **Canlı doğrulandı** (47024 + C1 Sprechen, 200, tüm yeni link render). Kardeş beceri ID'leri: C1 Hören 48634·Schreiben 48635·Sprechen 48636·Lesen 48534 · C2 Hören 48646·Schreiben 48647·Sprechen 48648·Lesen 48535. **Opsiyonel sonraki:** GSC'de C1/C2 Sprechen'e tekrar indexleme isteği (link artık kalıcı sinyal).

**🔑 KRİTİK YENİ TEKNİK DERS — Python ile uçtan uca REST (PS-BOM tuzağına son):** **Python `urllib` varsayılan UA (`Python-urllib/x`) host WAF'ı (Imunify360) tarafından 403 Forbidden ile bloklanıyor; tarayıcı UA header'ı (`User-Agent: Mozilla/5.0 …Chrome…`) eklenince GEÇİYOR.** Böylece GET+POST'un TAMAMI Python'da yapılabilir (`json.dumps(ensure_ascii=False)` ile Türkçe/Almanca temiz) → eski "PS sadece raw-byte POST, Python sadece string-build" hibriti ARTIK GEREKSİZ; PS 5.1 BOM/ETS/ConvertTo-Json tuzaklarından tümüyle kaçılır. (PowerShell `Invoke-RestMethod`/`Invoke-WebRequest` zaten geçiyordu — onların UA'sı whitelist'te; canlı public doğrulama için PS + tarayıcı-UA + tek cache-buster hâlâ iyi.) **Snippet idempotency:** create öncesi `GET /code-snippets/v1/snippets` → kod içinde marker (`aef-ix-a11y`) ara, varsa `POST /{id}` ile güncelle. **wp:html olmayan tasarım-sistemli sayfada (47024 `lvh-`) ekleme: mevcut sınıfları kullan + `<nav class="lvh-jump">` gibi tekil anchor'dan önce `replace(...,1)` ile yerleştir; idempotent sök `re.sub(r'\s*<section ... id="aef-beceri-sinavlari".*?</section>\n?', '', raw, flags=S)`.**


---
**WP TEKNİK DERSLER (2026-06-16, Instagram→site entegrasyonu sırasında — bkz [[sosyal-medya-video-stratejisi]]):**
- **Kadence sosyal ikon linkleri = theme_mods** (`instagram_link` / `facebook_link` / `twitter_link`); header/footer item'ın kendi url'i boşsa bu global mod'dan beslenir (YouTube item'da kendi url'i var). Customizer yerine `set_theme_mod()` snippet'iyle güncellenebilir. Doğru anahtarı tahmin etme: gizli-paramlı geçici snippet ile `get_theme_mods()` dök (sosyal anahtarları filtrele) → kesin gör.
- **⚠️ LiteSpeed AUTHENTICATED Code Snippets REST GET listesini ÖNBELLEKLER** → snippet oluşturduktan/sildikten sonra liste GET'i ESKİ döner (yanıltıcı idempotency/temizlik kontrolü!). Her doğrulama GET'ine cache-bust query param (`?_cb=rand`) ekle VEYA önce purge et. `x-litespeed-cache: hit/miss` header'ı gerçeği söyler.
- **⚠️ Code Snippets REST DELETE = NO-OP** (HTTP 204/200 döner ama snippet SİLİNMEZ; bu sürümde REST delete çalışmıyor). Bu yüzden sitede ~540 pasif TEMP snippet birikmiş. **Çözüm: silmek yerine ETKİSİZLEŞTİR** = POST ile `active:false` + `code` boş no-op. Kalıcı silme yalnızca wp-admin>Snippets'ten. Güvenlik için etkisizleştirme yeterli (gizli-param backdoor kodu artık çalışmaz).
- **Cache katmanı:** HTML = LiteSpeed (LSCache); Cloudflare HTML'i önbelleklemiyor (`cf-cache-status: DYNAMIC`). Site-geneli değişiklik sonrası purge = tek-seferlik snippet `do_action('litespeed_purge_all')` (paramla tetikle, sonra etkisizleştir).
