#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keyword sensitivity test — DELTA computation.
DELTA = (augmented broad search) MINUS (existing broad corpus, n≈3050).
NO fabrication: reads only real WoS/Scopus exports. Run LOCALLY (cowork PC) where
analysis/raw_data/ holds both the ORIGINAL and the AUGMENTED exports.

Inputs (place in analysis/raw_data/):
  ORIGINAL  : wos_broad_1..4.txt , scopus_broad.csv          (existing 3050 corpus)
  AUGMENTED : wos_aug_1..N.txt   , scopus_aug.csv            (new run, augmented A block)
Output:
  analysis/sensitivity_delta.csv
  cols: doi,title,year,journal,new_term_hit,relevant,modal,recency
Run: python3 analysis/scripts/sensitivity_delta.py
"""
import os, re, csv, glob, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # .../analysis
RAW  = os.path.join(ROOT, "raw_data")
OUT  = os.path.join(ROOT, "sensitivity_delta.csv")
SNAPSHOT_DATE = "2026-06-19"   # original corpus snapshot; recency boundary

# --- terms introduced ONLY by the augmented A block (for new_term_hit tagging) ---
NEW_TERMS = [
 "gen ai","gai","gpt-","conversational agent","ai assistant","gemini","bard","claude",
 "copilot","ernie bot","ernie","qwen","wenxin","doubao","llama","perplexity","grok","sora",
 "dall-e","dalle","midjourney","stable diffusion","text-to-image","image generation",
 "ai-generated","ai-generated content","generative model",
]
MODAL_TERMS = ["dall-e","dalle","midjourney","stable diffusion","text-to-image",
               "image generation","multimodal","visual","image-generation"]

def norm_doi(d):
    if not d: return ""
    d = d.strip().lower()
    d = re.sub(r'^https?://(dx\.)?doi\.org/','',d)
    return d.strip()

def norm_title(t):
    return re.sub(r'[^a-z0-9]+',' ', (t or "").lower()).strip()

# ---------- WoS plain-text parser (DI/TI/PY/SO/AB/DE/DT/early-access date) ----------
def parse_wos(files):
    recs=[]
    for fn in files:
        if not os.path.exists(fn): continue
        rec=None; field=None
        for line in open(fn, encoding='utf-8-sig'):
            tag=line[:2]; val=line[3:].rstrip('\n')
            if tag=='PT': rec={'db':'WoS','title':'','doi':'','year':'','journal':'','abstract':'','keywords':''}
            elif tag=='TI': rec['title']=val; field='TI'
            elif tag=='SO': rec['journal']=val; field='SO'
            elif tag=='DI': rec['doi']=val
            elif tag=='PY': rec['year']=val
            elif tag=='AB': rec['abstract']=val; field='AB'
            elif tag in ('DE','ID'): rec['keywords']+=" "+val; field='K'
            elif tag=='EA' and not rec.get('year'): rec['year']=val  # early access
            elif tag=='ER':
                if rec: recs.append(rec); rec=None; field=None
            elif tag=='  ' and rec is not None and field:
                if field=='TI': rec['title']+=" "+val.strip()
                elif field=='AB': rec['abstract']+=" "+val.strip()
                elif field=='K': rec['keywords']+=" "+val.strip()
    return recs

# ---------- Scopus CSV parser ----------
def parse_scopus(fn):
    recs=[]
    if not os.path.exists(fn): return recs
    for row in csv.DictReader(open(fn, encoding='utf-8-sig')):
        g=lambda *ks: next((row[k] for k in ks if k in row and row[k]), "")
        recs.append({'db':'Scopus',
            'title':g('Title'),'doi':g('DOI'),'year':g('Year'),
            'journal':g('Source title'),
            'abstract':g('Abstract'),
            'keywords':" ".join([g('Author Keywords'),g('Index Keywords')])})
    return recs

def key(r):
    d=norm_doi(r.get('doi'))
    return ("doi:"+d) if d else ("ti:"+norm_title(r.get('title'))[:80])

def load(prefix_wos, scopus_name):
    wos=parse_wos(sorted(glob.glob(os.path.join(RAW, prefix_wos))))
    sco=parse_scopus(os.path.join(RAW, scopus_name))
    return wos+sco

def main():
    orig = load("wos_broad_*.txt", "scopus_broad.csv")
    aug  = load("wos_aug_*.txt",   "scopus_aug.csv")
    if not aug:
        sys.exit("HATA: analysis/raw_data/ içinde AUGMENTED export yok "
                 "(wos_aug_*.txt / scopus_aug.csv). Önce dizgeleri çalıştırıp export koyun.")
    orig_keys={key(r) for r in orig}
    # dedup augmented, then subtract original
    seen={}; 
    for r in aug:
        seen.setdefault(key(r), r)
    delta=[r for k,r in seen.items() if k not in orig_keys]

    def blob(r): return " ".join([r.get('title',''),r.get('abstract',''),r.get('keywords','')]).lower()
    rows=[]
    for r in delta:
        b=blob(r)
        hits=[t for t in NEW_TERMS if t in b]
        modal = any(t in b for t in MODAL_TERMS)
        yr=re.sub(r'[^0-9]','',(r.get('year') or ''))[:4]
        recency = "?"  # date-precise recency requires the export's date field; flagged for manual check
        rows.append({
            'doi':norm_doi(r.get('doi')),'title':(r.get('title') or '').strip(),
            'year':yr,'journal':(r.get('journal') or '').strip(),
            'new_term_hit':"; ".join(hits) if hits else "(other)",
            'relevant':"",          # human-reviewed downstream
            'modal':"Y" if modal else "N",
            'recency':recency,
        })
    rows.sort(key=lambda x:(x['year'], x['journal']))
    with open(OUT,'w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f, fieldnames=['doi','title','year','journal','new_term_hit','relevant','modal','recency'])
        w.writeheader(); w.writerows(rows)
    print(f"Original corpus records : {len(orig)}  (unique keys {len(orig_keys)})")
    print(f"Augmented records       : {len(seen)} unique")
    print(f"DELTA (new, not in orig): {len(rows)}  -> {OUT}")
    print(f"  of which modal(image) : {sum(1 for r in rows if r['modal']=='Y')}")

if __name__=='__main__':
    main()
