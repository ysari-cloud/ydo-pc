#!/usr/bin/env bash
# OA tam-metin toplu indirici — YEREL PC'de / cowork'te çalıştır (ağı açık ortamda).
# Bu BULUT ortamında çalışmaz (egress allowlist). Kullanım:  bash pdf_indir.sh
# Çıktı: ./pdf/<n>_<Yazar>_<Yil>.pdf
set -u
OUT="pdf"; mkdir -p "$OUT"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
ok=0; fail=0; faillist=()

get () {  # get <dosyaadı> <url>
  local f="$OUT/$1" u="$2"
  echo "→ $1"
  if curl -L -f -s --retry 3 --retry-delay 2 -A "$UA" -e "https://scholar.google.com" \
        --max-time 120 -o "$f" "$u" && [ -s "$f" ] && head -c4 "$f" | grep -q "%PDF"; then
    echo "  ✓ indi ($(du -h "$f" | cut -f1))"; ok=$((ok+1))
  else
    echo "  ✗ BAŞARISIZ → tarayıcı/Zotero gerek"; rm -f "$f"; fail=$((fail+1)); faillist+=("$1")
  fi
}

# ---- Güvenilir doğrudan-PDF OA kaynakları ----
get "08_Park_2026.pdf"        "https://link.springer.com/content/pdf/10.1186/s40468-026-00429-5.pdf"
get "11_Michelson_2026.pdf"   "https://escholarship.org/content/qt08z2t1mq/qt08z2t1mq.pdf"
get "12_Bataineh_2026.pdf"    "https://jite.org/documents/Vol25/JITE-IIPv25Art07Bataineh13018.pdf"
get "16_Karakaya_2025.pdf"    "https://files.eric.ed.gov/fulltext/EJ1484591.pdf"
get "17_Setiyawan_2025.pdf"   "https://ejournal.uin-malang.ac.id/index.php/ijazarabi/article/download/35367/12922"
get "25_Mizumoto_2025.pdf"    "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/631312E8DD4EB9CE558EFF6FD16C6520/S0272263125100934a.pdf/automated-analysis-of-common-errors-in-l2-learner-production-prototype-web-application-development.pdf"
get "26_Pack_2023.pdf"        "https://files.eric.ed.gov/fulltext/EJ1397173.pdf"
get "32_Williyan_2024.pdf"    "https://files.eric.ed.gov/fulltext/EJ1435643.pdf"
get "37_GetinoDiez_2026.pdf"  "https://www.castledown.com.au/journals/tltl/article/download/tltl.2026.103327/1088"
get "39_NguyenPT_2024.pdf"    "https://systems.enpress-publisher.com/index.php/jipd/article/viewFile/7011/3880"
get "43_Haristiani_2021.pdf"  "https://ejournal.upi.edu/index.php/ijost/article/download/39150/16342"
get "44_Haristiani_2019.pdf"  "https://jestec.taylors.edu.my/Vol%2014%20issue%206%20December%202019/14_6_7.pdf"
get "46_Li_2023.pdf"          "https://www.mdpi.com/2226-471X/8/3/197/pdf"
get "47_Bonner_2023.pdf"      "https://files.eric.ed.gov/fulltext/EJ1383526.pdf"
get "48_Huang_2022.pdf"       "https://onlinelibrary.wiley.com/doi/am-pdf/10.1111/jcal.12610"
get "50_Mageira_2022.pdf"     "https://www.mdpi.com/2076-3417/12/7/3239/pdf"

echo
echo "================ ÖZET ================"
echo "İndi: $ok | Başarısız: $fail"
[ $fail -gt 0 ] && printf 'Tarayıcı/Zotero gerekenler: %s\n' "${faillist[*]}"
cat <<'NOT'

NOT-İNEN GERİSİ (bot-korumalı OA + kapalı) → Zotero Connector + vetis girişi ile:
  Bot-korumalı OA: 03 Ngo, 07 Lenko-Szymanska, 14 Zheng, 23 Wu, 28 Ursa, 34 Zaiarna,
                   38 Law, 41 Haristiani20, 51 Zhai, 54 Katsarou, 22 Wardat
  Kapalı (vetis):  1,2,4,5,6,9,15,18,20,21,27,29,30,31,40,45,52,53
NOT
