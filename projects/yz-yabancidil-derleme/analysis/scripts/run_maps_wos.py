#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Science-mapping maps built STRICTLY on WoS Cited References (CR).
Rationale: Scopus export carried no/dirty references (503 at export), so naive
merging would corrupt co-citation & bibliographic coupling. Per methodological
review, intellectual-structure maps use WoS CR only; Scopus contributes to
performance + keyword layers (run_full.py).
Also writes a VOSviewer thesaurus + a raw-file mapping guide (VOSviewer's own
parser produces cleaner maps directly from raw WoS/Scopus files).
"""
import os, re, json, itertools
from collections import Counter, defaultdict
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import importlib.util
HERE=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location("ba",os.path.join(HERE,"biblio_analysis.py"))
ba=importlib.util.module_from_spec(spec); spec.loader.exec_module(ba)
OUT,FIG,VOS=ba.OUT,ba.FIG,ba.VOS
WOS=[r for r in ba.DATA['broad'] if r['db']=='WoS' and r['cited_refs']]
print(f"WoS records with CR used for intellectual-structure maps: {len(WOS)}")

GREY="#718096"
def norm_ref(cr):
    m=re.search(r'DOI\s+(?:\[)?(?:DOI\s+)?(10\.[^\s,\]]+)',cr,re.I)
    if m: return 'doi:'+ba.nd(m.group(1))
    parts=[p.strip() for p in cr.split(',')]
    au=parts[0] if parts else cr; yr=''
    for p in parts[1:3]:
        if re.fullmatch(r'(19|20)\d{2}',p.strip()): yr=p.strip(); break
    return ('lit:'+re.sub(r'\s+',' ',f"{au} {yr}".lower())) if (au and yr) else None

# ---- CO-CITATION (WoS) ----
refcount=Counter(); labels={}; perdoc=[]
for r in WOS:
    keys=set()
    for cr in r['cited_refs']:
        k=norm_ref(cr)
        if not k: continue
        keys.add(k)
        if k not in labels:
            parts=[p.strip() for p in cr.split(',')]; labels[k]=', '.join(parts[:3])[:46]
    for k in keys: refcount[k]+=1
    perdoc.append(keys)
TOPN=40; keep=[k for k,_ in refcount.most_common(TOPN)]; ks=set(keep)
co=Counter()
for keys in perdoc:
    inter=[k for k in keys if k in ks]
    for a,b in itertools.combinations(sorted(inter),2): co[(a,b)]+=1
Gcc=nx.Graph()
for k in keep: Gcc.add_node(k,weight=refcount[k],label=labels.get(k,k))
for (a,b),w in co.items():
    if w>=10: Gcc.add_edge(a,b,weight=w)

# ---- BIBLIOGRAPHIC COUPLING of COUNTRIES (WoS) ----
# two countries coupled if WoS docs from them cite common references
ctry_refs=defaultdict(Counter)
for r in WOS:
    refs={norm_ref(c) for c in r['cited_refs']}; refs.discard(None)
    for c in set(r['countries']):
        for ref in refs: ctry_refs[c][ref]+=1
ctry_docs=Counter()
for r in WOS:
    for c in set(r['countries']): ctry_docs[c]+=1
topc=[c for c,_ in ctry_docs.most_common(25)]
Gbc=nx.Graph()
for c in topc: Gbc.add_node(c,weight=ctry_docs[c])
pairs=[]
for a,b in itertools.combinations(topc,2):
    sa=set(ctry_refs[a]); sb=set(ctry_refs[b]); shared=len(sa&sb)
    if shared<10: continue
    assoc=shared/ (ctry_docs[a]*ctry_docs[b])   # association strength
    pairs.append((a,b,shared,assoc))
pairs.sort(key=lambda x:x[3],reverse=True)
for a,b,shared,assoc in pairs[:45]:
    Gbc.add_edge(a,b,weight=shared)

def draw(G,title,path,label_attr=None):
    if G.number_of_nodes()==0: return
    plt.figure(figsize=(12,9))
    sizes=[300+G.nodes[n].get('weight',1)*6 for n in G.nodes()]
    pos=nx.spring_layout(G,k=0.7,seed=42,weight='weight')
    try:
        comms=nx.algorithms.community.greedy_modularity_communities(G,weight='weight')
        cm={}; [cm.update({n:i for n in com}) for i,com in enumerate(comms)]
        colors=[cm.get(n,0) for n in G.nodes()]
    except Exception: colors="#2b6cb0"
    nx.draw_networkx_nodes(G,pos,node_size=sizes,node_color=colors,cmap='tab10',alpha=0.9)
    ew=[d['weight'] for *_,d in G.edges(data=True)]; mw=max(ew) if ew else 1
    nx.draw_networkx_edges(G,pos,width=[0.3+2.5*w/mw for w in ew],alpha=0.25,edge_color=GREY)
    lab={n:(G.nodes[n].get(label_attr,n) if label_attr else n) for n in G.nodes()}
    nx.draw_networkx_labels(G,pos,lab,font_size=8)
    plt.title(title,fontsize=14,fontweight='bold'); plt.axis('off'); plt.tight_layout()
    plt.savefig(path,bbox_inches='tight'); plt.close()

draw(Gcc,f"Co-citation network of cited references — WoS only (n={len(WOS)} docs, Top {TOPN})",
     os.path.join(FIG,"fig9_cocitation.png"),label_attr='label')
draw(Gbc,"Bibliographic coupling of countries — WoS only (shared references)",
     os.path.join(FIG,"fig12_biblio_coupling_countries.png"))

def stats(G): return {"nodes":G.number_of_nodes(),"edges":G.number_of_edges(),
    "density":round(nx.density(G),4),"components":nx.number_connected_components(G)}
json.dump({"wos_docs_with_CR":len(WOS),"cocitation":stats(Gcc),
           "biblio_coupling_countries":stats(Gbc)},
          open(os.path.join(OUT,"_results_maps.json"),"w"),indent=1)
print("co-citation:",stats(Gcc)," | coupling:",stats(Gbc))
