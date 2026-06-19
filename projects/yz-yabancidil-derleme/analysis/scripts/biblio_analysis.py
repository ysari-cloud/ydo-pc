#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GenAI x Foreign Language Education -- FULL BIBLIOMETRIC ANALYSIS (Stage 2)
Re-parses FULL metadata from raw WoS plaintext + Scopus CSV, merges/dedups,
then computes performance analysis + science mapping + thematic evolution.
Outputs: outputs/tables.xlsx, outputs/figures/*.png, outputs/vosviewer/*.

Reproducible. Source integrity: every number derives from the raw exports.
Run from project root:  python3 scripts/biblio_analysis.py
"""
import csv, re, os, sys, json
from collections import Counter, defaultdict
import math

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW  = os.path.join(ROOT, "raw_data")
OUT  = os.path.join(ROOT, "outputs")
FIG  = os.path.join(OUT, "figures")
VOS  = os.path.join(OUT, "vosviewer")
for d in (OUT, FIG, VOS):
    os.makedirs(d, exist_ok=True)

# ---------- normalisation helpers ----------
def nd(d):
    if not d: return ""
    d = d.strip().lower()
    d = re.sub(r'^https?://(dx\.)?doi\.org/', '', d)
    return d.strip()

def nt(t):
    if not t: return ""
    t = t.lower(); t = re.sub(r'[^a-z0-9]+', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()

# country normalisation
_COUNTRY_FIX = {
    'usa':'USA','united states':'USA','united states of america':'USA','u s a':'USA',
    'peoples r china':'China','china':'China','hong kong':'China','taiwan':'Taiwan',
    'macau':'China','england':'United Kingdom','scotland':'United Kingdom',
    'wales':'United Kingdom','north ireland':'United Kingdom','northern ireland':'United Kingdom',
    'uk':'United Kingdom','united kingdom':'United Kingdom','u arab emirates':'United Arab Emirates',
    'united arab emirates':'United Arab Emirates','uae':'United Arab Emirates',
    'south korea':'South Korea','korea':'South Korea','republic of korea':'South Korea',
    'czech republic':'Czech Republic','russia':'Russia','russian federation':'Russia',
    'viet nam':'Vietnam','vietnam':'Vietnam','iran':'Iran','iran (islamic republic of)':'Iran',
    'saudi arabia':'Saudi Arabia','trinid & tobago':'Trinidad and Tobago',
    'bosnia & herceg':'Bosnia and Herzegovina','turkiye':'Turkey','turkey':'Turkey',
}
def fix_country(c):
    if not c: return ""
    c = c.strip().strip('.').strip().lower()
    c = re.sub(r'\s+', ' ', c)
    return _COUNTRY_FIX.get(c, c.title())

def country_from_wos_c1(piece):
    """Last comma-separated chunk of a C1 address = country (maybe with 'NY 10027 USA')."""
    seg = piece.strip().strip('.').split(',')[-1].strip()
    toks = seg.split()
    if toks and toks[-1].upper() == 'USA':
        return 'USA'
    return fix_country(seg)

def country_from_scopus_aff(piece):
    return fix_country(piece.strip().split(',')[-1])

_INST_STOP = {'university','university of','univ','department of english','faculty of education',
    'school of education','college of education','department of education','faculty of arts',
    'department of english language and literature','graduate school','faculty of humanities'}
_ORG_KEYS = ('universit','institut','polytechnic','academy','ecole','escuela','hochschule','college')
def org_from_affiliation(aff):
    """Pick the parent-organisation chunk from a Scopus affiliation string."""
    chunks=[c.strip() for c in aff.split(',') if c.strip()]
    cand=[c for c in chunks if any(k in c.lower() for k in _ORG_KEYS)]
    pref=[c for c in cand if 'universit' in c.lower()]
    pick=(pref or cand or chunks[:1])
    if not pick: return ''
    org=pick[0].strip()
    return org if org.lower() not in _INST_STOP and len(org)>4 else ''
def clean_inst(name):
    n=re.sub(r'\s+',' ',name.strip())
    return n if n.lower() not in _INST_STOP and len(n)>4 else ''

# ---------- WoS parser (full record) ----------
def parse_wos(files):
    recs = []
    for fn in files:
        cur = {}; tag = None
        for line in open(fn, encoding='utf-8-sig'):
            line = line.rstrip('\n')
            if line.startswith('ER'):
                if cur: recs.append(cur); cur = {}
                tag = None; continue
            if line.startswith('   ') and tag:          # continuation
                cur[tag].append(line.strip()); continue
            if len(line) >= 2 and line[:2].strip():       # new tag
                tag = line[:2]; cur.setdefault(tag, []).append(line[3:].strip())
        if cur: recs.append(cur)
    out = []
    for r in recs:
        de = ';'.join(r.get('DE', [])); idk = ';'.join(r.get('ID', []))
        de_terms  = [k.strip().lower() for k in de.split(';')  if k.strip()]
        id_terms  = [k.strip().lower() for k in idk.split(';') if k.strip()]
        crs = [c.strip() for c in r.get('CR', []) if c.strip()]
        countries = []
        for c1line in r.get('C1', []):
            countries.append(country_from_wos_c1(c1line))
        if not countries:
            for rp in r.get('RP', []):
                countries.append(country_from_wos_c1(rp))
        authors = [a.strip() for a in r.get('AF', []) if a.strip()] or \
                  [a.strip() for a in r.get('AU', []) if a.strip()]
        # institutions from C3 (org-enhanced), ';' separated
        insts = []
        for c3 in r.get('C3', []):
            for x in c3.split(';'):
                ci=clean_inst(x)
                if ci: insts.append(ci)
        tc = 0
        if r.get('TC'):
            try: tc = int(re.sub(r'\D','',r['TC'][0]) or 0)
            except: tc = 0
        out.append({
            'db':'WoS',
            'doi': nd(r.get('DI',[''])[0] if r.get('DI') else ''),
            'title': ' '.join(r.get('TI', [])),
            'year': (r.get('PY',[''])[0] if r.get('PY') else ''),
            'source_title': ' '.join(r.get('SO', [])).strip(),
            'doctype': (r.get('DT',[''])[0] if r.get('DT') else ''),
            'authors': authors,
            'de_keywords': de_terms,
            'id_keywords': id_terms,
            'countries': [c for c in countries if c],
            'institutions': insts,
            'cited_refs': crs,
            'tc': tc,
        })
    return out

# ---------- Scopus parser (full record) ----------
def parse_scopus(fn):
    out = []
    for row in csv.DictReader(open(fn, encoding='utf-8-sig')):
        authors = [a.strip() for a in row.get('Authors','').split(';') if a.strip() and a.strip()!='[No author name available]']
        de = [k.strip().lower() for k in row.get('Author Keywords','').split(';') if k.strip()]
        idk = [k.strip().lower() for k in row.get('Index Keywords','').split(';') if k.strip()]
        countries = []; insts = []
        for aff in row.get('Affiliations','').split(';'):
            aff = aff.strip()
            if not aff: continue
            c = country_from_scopus_aff(aff)
            if c: countries.append(c)
            org=org_from_affiliation(aff)
            if org: insts.append(org)
        try: tc = int(row.get('Cited by','') or 0)
        except: tc = 0
        out.append({
            'db':'Scopus',
            'doi': nd(row.get('DOI','')),
            'title': row.get('Title',''),
            'year': str(row.get('Year','')).strip(),
            'source_title': row.get('Source title','').strip(),
            'doctype': row.get('Document Type','').strip(),
            'authors': authors,
            'de_keywords': de,
            'id_keywords': idk,
            'countries': countries,
            'institutions': insts,
            'cited_refs': [],
            'tc': tc,
        })
    return out

# ---------- merge + dedup (WoS preferred -> retains CR) ----------
def merge_dedup(wos, scopus):
    records = wos + scopus
    seen_doi=set(); seen_tt=set(); uniq=[]; dup=0
    for r in records:
        kd = r['doi'] or None
        kt = (nt(r['title']), str(r['year'])[:4]) if r['title'] else None
        if (kd and kd in seen_doi) or (kt and kt in seen_tt):
            dup += 1; continue
        if kd: seen_doi.add(kd)
        if kt: seen_tt.add(kt)
        uniq.append(r)
    return uniq, dup

print("Parsing WoS ...")
wos_b = parse_wos([os.path.join(RAW, f"wos_broad_{i}.txt") for i in (1,2,3,4)])
wos_f = parse_wos([os.path.join(RAW, "wos_focus.txt")])
print("Parsing Scopus ...")
sco_b = parse_scopus(os.path.join(RAW, "scopus_broad.csv"))
sco_f = parse_scopus(os.path.join(RAW, "scopus_focus.csv"))

broad, dup_b = merge_dedup(wos_b, sco_b)
focus, dup_f = merge_dedup(wos_f, sco_f)
print(f"BROAD raw WoS {len(wos_b)} + Scopus {len(sco_b)} -> unique {len(broad)} (dups {dup_b})")
print(f"FOCUS raw WoS {len(wos_f)} + Scopus {len(sco_f)} -> unique {len(focus)} (dups {dup_f})")

DATA = {'broad': broad, 'focus': focus,
        'wos_broad': wos_b, 'scopus_broad': sco_b,
        'wos_focus': wos_f, 'scopus_focus': sco_f}

if __name__ == '__main__':
    for _name, _dset in (('broad', broad), ('focus', focus)):
        _yrs = Counter(r['year'][:4] for r in _dset if r['year'])
        _wos = sum(1 for r in _dset if r['db'] == 'WoS')
        _cr = sum(1 for r in _dset if r['cited_refs'])
        print(f"[{_name}] n={len(_dset)} WoS={_wos} Scopus={len(_dset)-_wos} CR={_cr}")
