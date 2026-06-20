# İŞ AKIŞI NOTU — Chrome eklentisiyle WoS/Scopus'ta çalışma (ÖNEMLİ, unutma)

**Kritik nokta:** Claude'un `navigate` ile webofscience.com / scopus.com'a GİTMESİ eklenti
allowlist'i nedeniyle engelli. AMA bu, "veri tabanında çalışılamaz" demek DEĞİL.

**Doğru iş akışı:**
1. KULLANICI, kurumsal erişim izni olan veri tabanını (WoS / Scopus) kendi tarayıcısında
   kendisi açar ve arama sayfasına getirir (oturum + İÜC erişimi onun tarafında).
2. CLAUDE, `tabs_context_mcp` ile o ZATEN AÇIK sekmeyi alır ve orada çalışır:
   `read_page` ile arama kutusunu bulur, `computer`/`form_input` ile dizgeyi yazar,
   arama başlatır, export adımlarını sürer.
3. Yani Claude sekmeyi AÇMAZ; kullanıcının açtığı sekme ÜZERİNDE işlem yapar.

**Sonuç:** Erişim izni gereken her veri tabanı işinde önce kullanıcı sayfayı açar, sonra
Claude talimatları o sekmede uygular. (navigate engeli ≠ etkileşim engeli.)
