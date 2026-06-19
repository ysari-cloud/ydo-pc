#!/usr/bin/env python3
"""
GenAI x Foreign Language Education -- Bibliometric study
Stage 1: Identification + within/cross-source de-duplication + PRISMA counts.
Run from project root:  python3 scripts/dedup_prisma.py
Reads:  raw_data/*.txt (WoS plaintext), raw_data/*.csv (Scopus)
Writes: outputs/merged_broad_dedup.csv, outputs/merged_focus_dedup.csv
"""
import csv, re, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW=os.path.join(ROOT,"raw_data"); OUT=os.path.join(ROOT,"outputs"); os.makedirs(OUT,exist_ok=True)
def nd(d):
    if not d: return ""
    d=d.strip().lower(); d=re.sub(r'^https?://(dx\.)?doi\.org/','',d); return d.strip()
def nt(t):
    if not t: return ""
    t=t.lower(); t=re.sub(r'[^a-z0-9]+',' ',t); return re.sub(r'\s+',' ',t).strip()
def parse_wos(files):
    recs=[]
    for fn in files:
        cur={}; tag=None
        for line in open(fn,encoding='utf-8-sig'):
            line=line.rstrip('\n')
            if line.startswith('ER'):
                if cur: recs.append(cur); cur={}
                tag=None; continue
            if len(line)>=2 and line[:2].strip() and not line.startswith('  '):
                tag=line[:2]; cur.setdefault(tag,[]).append(line[3:].strip())
            elif line.startswith('   ') and tag: cur[tag].append(line.strip())
    return [{'doi':nd(r.get('DI',[''])[0] if r.get('DI') else ''),'title':' '.join(r.get('TI',[])),
             'year':(r.get('PY',[''])[0] if r.get('PY') else ''),'source_title':' '.join(r.get('SO',[])),
             'doctype':(r.get('DT',[''])[0] if r.get('DT') else ''),'db':'WoS'} for r in recs]
def parse_scopus(fn):
    return [{'doi':nd(row.get('DOI','')),'title':row.get('Title',''),'year':row.get('Year',''),
             'source_title':row.get('Source title',''),'doctype':row.get('Document Type',''),'db':'Scopus'}
            for row in csv.DictReader(open(fn,encoding='utf-8-sig'))]
def dedup(records):
    sd=set(); st=set(); uniq=[]; dup=0
    for r in records:
        kd=r['doi'] or None; kt=(nt(r['title']),str(r['year'])[:4]) if r['title'] else None
        if (kd and kd in sd) or (kt and kt in st): dup+=1; continue
        if kd: sd.add(kd)
        if kt: st.add(kt)
        uniq.append(r)
    return uniq,dup
def overlap(a,b):
    return len({r['doi'] for r in a if r['doi']} & {r['doi'] for r in b if r['doi']})
def write(fn,recs):
    with open(os.path.join(OUT,fn),'w',newline='',encoding='utf-8-sig') as f:
        w=csv.writer(f); w.writerow(['db','doi','year','source_title','doctype','title'])
        for r in recs: w.writerow([r['db'],r['doi'],r['year'],r['source_title'],r['doctype'],r['title']])
wos_b=parse_wos([os.path.join(RAW,f"wos_broad_{i}.txt") for i in (1,2,3,4)])
wos_f=parse_wos([os.path.join(RAW,"wos_focus.txt")])
sco_b=parse_scopus(os.path.join(RAW,"scopus_broad.csv"))
sco_f=parse_scopus(os.path.join(RAW,"scopus_focus.csv"))
ub,db_=dedup(wos_b+sco_b); uf,df_=dedup(wos_f+sco_f)
write('merged_broad_dedup.csv',ub); write('merged_focus_dedup.csv',uf)
print(f"BROAD: WoS {len(wos_b)} + Scopus {len(sco_b)} = {len(wos_b)+len(sco_b)} | DOI-overlap {overlap(wos_b,sco_b)} | dups {db_} -> unique {len(ub)}")
print(f"FOCUS: WoS {len(wos_f)} + Scopus {len(sco_f)} = {len(wos_f)+len(sco_f)} | DOI-overlap {overlap(wos_f,sco_f)} | dups {df_} -> unique {len(uf)}")
