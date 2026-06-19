#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AS3 sensitivity: conversation vs production framing under STRICT vs BROAD
production lexicons; word-boundary matching; absolute + proportional + ratio.
Plus a corroborating top-keyword-by-slice readout. All from data; no fabrication."""
import os,re,json,importlib.util
from collections import Counter
HERE=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location("ba",os.path.join(HERE,"biblio_analysis.py"))
ba=importlib.util.module_from_spec(spec);spec.loader.exec_module(ba)
b=ba.DATA['broad']
def canon(k): return re.sub(r'\s+',' ',k.strip().lower())
def blob(r): return ' '.join(canon(k) for k in r['de_keywords'])
def sl(y):
    yi=int(y[:4]) if y[:4].isdigit() else 0
    return "2018-2021" if 2018<=yi<=2021 else "2022-2023" if yi in(2022,2023) else "2024-2026" if yi>=2024 else None

CONV=['chatbot','chatbots','conversational agent','conversational agents','conversational ai',
 'dialogue system','dialogue systems','dialog system','intelligent tutoring','spoken dialogue',
 'voice assistant','virtual assistant','pronunciation','conversation practice',
 'speech recognition chatbot','speech-recognition chatbot','dialogue-based']
PROD_STRICT=['materials development','material development','materials design','material design',
 'content creation','content generation','courseware','lesson plan','lesson plans',
 'instructional design','test generation','item generation','question generation',
 'task generation','exercise generation','authoring','automatic item','automatic question']
PROD_BROAD=PROD_STRICT+['teaching materials','learning materials','instructional materials',
 'content development','ai-generated content','text generation','worksheet','worksheets',
 'syllabus design','curriculum design','curriculum development','material creation',
 'automated item generation','reading materials','authoring tool','authoring tools']
def pats(L): return [re.compile(r'\b'+re.escape(t)+r'\b') for t in L]
CP,PSP,PBP=pats(CONV),pats(PROD_STRICT),pats(PROD_BROAD)
def hit(t,P): return any(p.search(t) for p in P)

slices=["2018-2021","2022-2023","2024-2026"]
rows={}
for s in slices:
    recs=[r for r in b if sl(r['year'])==s]; n=len(recs)
    cv=sum(1 for r in recs if hit(blob(r),CP))
    ps=sum(1 for r in recs if hit(blob(r),PSP))
    pb=sum(1 for r in recs if hit(blob(r),PBP))
    rows[s]=dict(n=n,conv=cv,prod_strict=ps,prod_broad=pb,
                 conv_pct=100*cv/n,ps_pct=100*ps/n,pb_pct=100*pb/n,
                 ratio_strict=ps/cv if cv else 0, ratio_broad=pb/cv if cv else 0)
print("SLICE | n | conv (%) | prodStrict (%) | prodBroad (%) | prodB/conv")
for s in slices:
    d=rows[s]
    print(f"{s} | {d['n']} | {d['conv']} ({d['conv_pct']:.1f}%) | {d['prod_strict']} ({d['ps_pct']:.1f}%) | {d['prod_broad']} ({d['pb_pct']:.1f}%) | {d['ratio_broad']:.2f}")

# corroborating: conversation-specific top keywords share among top-15 per slice
print("\nTop-8 author keywords by slice (independent corroboration):")
for s in slices:
    c=Counter()
    for r in b:
        if sl(r['year'])==s:
            for k in set(canon(x) for x in r['de_keywords']):
                if k and len(k)>1: c[k]+=1
    print(f"  {s}:", "; ".join(f"{k}({v})" for k,v in c.most_common(8)))

json.dump(rows,open(os.path.join(ba.OUT,"_as3_sensitivity.json"),"w"),indent=1)
print("\nsaved _as3_sensitivity.json")
