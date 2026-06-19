#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stage 2 driver: performance analysis + science mapping + thematic evolution.
Imports parsed DATA from biblio_analysis.py and writes Excel, figures, VOSviewer files.
Run:  python3 scripts/run_full.py
"""
import os, re, csv, json, math, itertools
from collections import Counter, defaultdict
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ba", os.path.join(HERE, "biblio_analysis.py"))
ba = importlib.util.module_from_spec(spec); spec.loader.exec_module(ba)

ROOT, OUT, FIG, VOS = ba.ROOT, ba.OUT, ba.FIG, ba.VOS
BROAD = ba.DATA['broad']; FOCUS = ba.DATA['focus']

PLOT_BG = "#ffffff"
plt.rcParams.update({"figure.dpi":150, "font.size":11, "axes.grid":True,
                     "grid.alpha":0.25, "axes.spines.top":False, "axes.spines.right":False})
ACCENT = "#2b6cb0"; ACCENT2 = "#dd6b20"; GREY="#718096"

# ----------------------------------------------------------------------------
# KEYWORD NORMALISATION (light) — merge obvious variants
# ----------------------------------------------------------------------------
KW_CANON = {
 'chatgpt':'chatgpt','chat gpt':'chatgpt','chat-gpt':'chatgpt','openai chatgpt':'chatgpt',
 'generative ai':'generative artificial intelligence','genai':'generative artificial intelligence',
 'generative artificial intelligence (ai)':'generative artificial intelligence',
 'generative artificial intelligence':'generative artificial intelligence',
 'large language model':'large language models','large language models (llms)':'large language models',
 'large language models':'large language models','llm':'large language models','llms':'large language models',
 'artificial intelligence (ai)':'artificial intelligence','artificial intelligence':'artificial intelligence',
 'ai':'artificial intelligence',
 'efl':'efl','english as a foreign language':'efl','english as a foreign language (efl)':'efl',
 'esl':'esl','english as a second language':'esl',
 'second language acquisition':'second language acquisition','sla':'second language acquisition',
 'computer-assisted language learning':'computer-assisted language learning',
 'computer assisted language learning':'computer-assisted language learning','call':'computer-assisted language learning',
 'language learning':'language learning','foreign language learning':'foreign language learning',
 'language teaching':'language teaching','foreign language education':'foreign language education',
 'language education':'language education','english language teaching':'english language teaching',
 'writing':'writing','l2 writing':'l2 writing','academic writing':'academic writing',
 'feedback':'feedback','automated feedback':'automated feedback','corrective feedback':'corrective feedback',
 'speaking':'speaking','pronunciation':'pronunciation','vocabulary':'vocabulary','vocabulary learning':'vocabulary learning',
 'chatbot':'chatbot','chatbots':'chatbot','conversational agent':'conversational agent','conversational agents':'conversational agent',
 'intelligent tutoring system':'intelligent tutoring systems','intelligent tutoring systems':'intelligent tutoring systems',
 'machine translation':'machine translation','natural language processing':'natural language processing','nlp':'natural language processing',
 'higher education':'higher education','educational technology':'educational technology',
 'student perception':'student perceptions','student perceptions':'student perceptions',
 'motivation':'motivation','self-regulated learning':'self-regulated learning',
 'prompt engineering':'prompt engineering','generative ai (genai)':'generative artificial intelligence',
}
def canon_kw(k):
    k = re.sub(r'\s+', ' ', k.strip().lower())
    return KW_CANON.get(k, k)

def rec_keywords(r):
    ks = [canon_kw(k) for k in r['de_keywords']]
    return [k for k in ks if k and len(k) > 1]

# ----------------------------------------------------------------------------
# 1. PERFORMANCE ANALYSIS
# ----------------------------------------------------------------------------
def annual_production(ds):
    c = Counter(r['year'][:4] for r in ds if r['year'][:4].isdigit())
    yrs = sorted(c)
    return [(y, c[y]) for y in yrs]

def top_counter(ds, field, n=20, splitlist=True):
    c = Counter()
    for r in ds:
        vals = r.get(field, [])
        if splitlist:
            for v in set(vals):           # count once per document
                if v: c[v]+=1
        else:
            v=r.get(field,'')
            if v: c[v]+=1
    return c.most_common(n)

def top_sources(ds, n=20):
    c = Counter(r['source_title'] for r in ds if r['source_title'])
    return c.most_common(n)

def top_cited_docs(ds, n=20):
    rows = sorted(ds, key=lambda r:r['tc'], reverse=True)[:n]
    return [(r['title'][:120], r['source_title'], r['year'][:4], r['tc'], r['db']) for r in rows]

def doctype_dist(ds):
    return Counter((r['doctype'] or 'Unknown').title() for r in ds).most_common()

def bradford(ds):
    c = Counter(r['source_title'] for r in ds if r['source_title'])
    items = c.most_common()
    total = sum(v for _,v in items)
    third = total/3.0
    zones=[]; cum=0; zone=1; zb=[]
    for src,v in items:
        zb.append((src,v)); cum+=v
        if cum>=zone*third and zone<3:
            zones.append(zb); zb=[]; zone+=1
    if zb: zones.append(zb)
    return [(i+1, len(z), sum(v for _,v in z)) for i,z in enumerate(zones)], items

def lotka(ds):
    pa = Counter()
    for r in ds:
        for a in set(r['authors']):
            pa[a]+=1
    dist = Counter(pa.values())       # n_papers -> n_authors
    tot = sum(dist.values())
    return sorted(((k, dist[k], dist[k]/tot) for k in dist)), len(pa)

# ----------------------------------------------------------------------------
# 2. SCIENCE MAPPING
# ----------------------------------------------------------------------------
def cooccurrence(ds, getter, top_nodes=50, min_edge=2):
    freq = Counter(); co = Counter(); avgyear=defaultdict(list)
    for r in ds:
        items = sorted(set(getter(r)))
        yr = r['year'][:4]
        for it in items:
            freq[it]+=1
            if yr.isdigit(): avgyear[it].append(int(yr))
        for a,b in itertools.combinations(items,2):
            co[(a,b)]+=1
    keep = [k for k,_ in freq.most_common(top_nodes)]
    keepset=set(keep)
    G = nx.Graph()
    for k in keep:
        ay = sum(avgyear[k])/len(avgyear[k]) if avgyear[k] else 0
        G.add_node(k, weight=freq[k], avgyear=round(ay,2))
    for (a,b),w in co.items():
        if a in keepset and b in keepset and w>=min_edge:
            G.add_edge(a,b,weight=w)
    return G, freq, co

# cited-reference normalisation for co-citation
def norm_ref(cr):
    cr = cr.strip()
    m = re.search(r'DOI\s+(?:\[)?(?:DOI\s+)?(10\.[^\s,\]]+)', cr, re.I)
    if m:
        return ('doi:'+ ba.nd(m.group(1)))
    # fallback: first author + year + source
    parts = [p.strip() for p in cr.split(',')]
    au = parts[0] if parts else cr
    yr = ''
    for p in parts[1:3]:
        if re.fullmatch(r'(19|20)\d{2}', p.strip()): yr=p.strip(); break
    src = parts[2] if len(parts)>2 else ''
    key = f"{au} {yr} {src}".strip().lower()
    return ('lit:'+re.sub(r'\s+',' ',key)) if (au and yr) else None

def cocitation(ds, top_nodes=40, min_edge=3):
    refcount = Counter(); labels={}
    perdoc=[]
    for r in ds:
        if not r['cited_refs']: continue
        keys=set()
        for cr in r['cited_refs']:
            k = norm_ref(cr)
            if not k: continue
            keys.add(k)
            if k not in labels:
                # short readable label
                parts=[p.strip() for p in cr.split(',')]
                lab = ', '.join(parts[:3])[:48]
                labels[k]=lab
        for k in keys: refcount[k]+=1
        perdoc.append(keys)
    keep=[k for k,_ in refcount.most_common(top_nodes)]; keepset=set(keep)
    co=Counter()
    for keys in perdoc:
        inter=[k for k in keys if k in keepset]
        for a,b in itertools.combinations(sorted(inter),2):
            co[(a,b)]+=1
    G=nx.Graph()
    for k in keep: G.add_node(k, weight=refcount[k], label=labels.get(k,k))
    for (a,b),w in co.items():
        if w>=min_edge: G.add_edge(a,b,weight=w)
    return G, refcount, labels

def country_collab(ds, top_nodes=30, min_edge=2):
    freq=Counter(); co=Counter()
    for r in ds:
        cs=sorted(set(r['countries']))
        for c in cs: freq[c]+=1
        for a,b in itertools.combinations(cs,2): co[(a,b)]+=1
    keep=[k for k,_ in freq.most_common(top_nodes)]; keepset=set(keep)
    G=nx.Graph()
    for k in keep: G.add_node(k, weight=freq[k])
    for (a,b),w in co.items():
        if a in keepset and b in keepset and w>=min_edge:
            G.add_edge(a,b,weight=w)
    return G, freq, co

# ----------------------------------------------------------------------------
# 3. THEMATIC EVOLUTION (AS3) — conversation -> production
# ----------------------------------------------------------------------------
SLICES = [("2018-2021",(2018,2021)),("2022-2023",(2022,2023)),("2024-2026",(2024,2026))]
CONV_LEX = ['chatbot','chatbots','conversational agent','conversational agents','conversational ai',
            'dialogue system','dialogue systems','dialog system','intelligent tutoring','spoken dialogue',
            'voice assistant','virtual assistant','pronunciation','conversation practice',
            'speech recognition chatbot','speech-recognition chatbot','dialogue-based']
PROD_LEX = ['materials development','material development','materials design','material design',
            'content creation','content generation','courseware','lesson plan','lesson plans',
            'instructional design','test generation','item generation','question generation',
            'task generation','exercise generation','authoring','automatic item','automatic question']
import re as _re
_CONV_PAT=[_re.compile(r'\b'+_re.escape(t)+r'\b') for t in CONV_LEX]
_PROD_PAT=[_re.compile(r'\b'+_re.escape(t)+r'\b') for t in PROD_LEX]
def _hit(text,pats): return any(p.search(text) for p in pats)
def slice_of(y):
    if not y[:4].isdigit(): return None
    yi=int(y[:4])
    for name,(a,b) in SLICES:
        if a<=yi<=b: return name
    return None
def text_blob(r):
    return ' '.join(rec_keywords(r))
def lex_share(ds):
    out={}
    for name,_ in SLICES:
        recs=[r for r in ds if slice_of(r['year'])==name]
        n=len(recs) or 1
        conv=sum(1 for r in recs if _hit(text_blob(r),_CONV_PAT))
        prod=sum(1 for r in recs if _hit(text_blob(r),_PROD_PAT))
        out[name]=(len(recs), conv, prod, conv/n, prod/n)
    return out
def slice_top_keywords(ds, n=15):
    out={}
    for name,_ in SLICES:
        c=Counter()
        for r in ds:
            if slice_of(r['year'])==name:
                for k in set(rec_keywords(r)): c[k]+=1
        out[name]=c.most_common(n)
    return out

# ----------------------------------------------------------------------------
# OUTPUT: VOSviewer (map + network) and Pajek .net
# ----------------------------------------------------------------------------
def export_vosviewer(G, name, label_attr=None):
    nodes=list(G.nodes())
    idx={n:i+1 for i,n in enumerate(nodes)}
    with open(os.path.join(VOS, f"{name}_map.txt"),"w",encoding="utf-8") as f:
        f.write("id\tlabel\tweight<Occurrences>\tscore<Avg. year>\n")
        for n in nodes:
            lab = G.nodes[n].get(label_attr,n) if label_attr else n
            w = G.nodes[n].get('weight',1)
            ay = G.nodes[n].get('avgyear','')
            f.write(f"{idx[n]}\t{lab}\t{w}\t{ay}\n")
    with open(os.path.join(VOS, f"{name}_network.txt"),"w",encoding="utf-8") as f:
        for a,b,d in G.edges(data=True):
            f.write(f"{idx[a]}\t{idx[b]}\t{d.get('weight',1)}\n")
    # Pajek .net (labels inline) for portability
    H=nx.relabel_nodes(G, {n:(G.nodes[n].get(label_attr,n) if label_attr else n) for n in nodes})
    try: nx.write_pajek(H, os.path.join(VOS, f"{name}.net"))
    except Exception: pass

def draw_network(G, title, path, label_attr=None, cmap_year=False):
    if G.number_of_nodes()==0:
        return
    plt.figure(figsize=(12,9))
    deg=dict(G.degree(weight='weight'))
    sizes=[300+ G.nodes[n].get('weight',1)*8 for n in G.nodes()]
    pos=nx.spring_layout(G, k=0.6, seed=42, weight='weight')
    if cmap_year:
        years=[G.nodes[n].get('avgyear',0) or 0 for n in G.nodes()]
        nc=nx.draw_networkx_nodes(G,pos,node_size=sizes,node_color=years,cmap='viridis',alpha=0.9)
        plt.colorbar(nc,label='Average publication year',shrink=0.6)
    else:
        # colour by community
        try:
            comms=nx.algorithms.community.greedy_modularity_communities(G, weight='weight')
            cmap={}
            for ci,com in enumerate(comms):
                for nn in com: cmap[nn]=ci
            colors=[cmap.get(n,0) for n in G.nodes()]
        except Exception:
            colors=ACCENT
        nx.draw_networkx_nodes(G,pos,node_size=sizes,node_color=colors,cmap='tab10',alpha=0.9)
    ew=[d['weight'] for _,_,d in G.edges(data=True)]
    mw=max(ew) if ew else 1
    nx.draw_networkx_edges(G,pos,width=[0.3+2.5*w/mw for w in ew],alpha=0.25,edge_color=GREY)
    labels={n:(G.nodes[n].get(label_attr,n) if label_attr else n) for n in G.nodes()}
    nx.draw_networkx_labels(G,pos,labels,font_size=8)
    plt.title(title, fontsize=14, fontweight='bold'); plt.axis('off'); plt.tight_layout()
    plt.savefig(path, bbox_inches='tight'); plt.close()

# ============================================================================
# RUN (broad set is the main corpus per the brief)
# ============================================================================
ds = BROAD
print(f"Analysing BROAD corpus n={len(ds)}")

annual = annual_production(ds)
srcs   = top_sources(ds, 20)
auths  = top_counter(ds, 'authors', 20)
ctrys  = top_counter(ds, 'countries', 20)
insts  = top_counter(ds, 'institutions', 20)
cited  = top_cited_docs(ds, 20)
dtypes = doctype_dist(ds)
zones, src_items = bradford(ds)
lot, n_authors = lotka(ds)

kw_top = Counter()
for r in ds:
    for k in set(rec_keywords(r)): kw_top[k]+=1
kw_top20 = kw_top.most_common(30)

Gkw,_,_   = cooccurrence(ds, rec_keywords, top_nodes=55, min_edge=4)
Gcc,_,_   = cocitation(ds, top_nodes=38, min_edge=3)
Gco,_,_   = country_collab(ds, top_nodes=28, min_edge=2)

lexshare  = lex_share(ds)
sl_kw     = slice_top_keywords(ds, 15)

# ---- FIGURES ----
# annual production
yrs=[y for y,_ in annual]; vals=[v for _,v in annual]
plt.figure(figsize=(10,5.5))
plt.bar(yrs, vals, color=ACCENT)
for x,v in zip(yrs,vals): plt.text(x, v+8, str(v), ha='center', fontsize=9)
plt.title("Annual scientific production (GenAI × Foreign Language Education)", fontweight='bold')
plt.xlabel("Year"); plt.ylabel("Documents"); plt.tight_layout()
plt.savefig(os.path.join(FIG,"fig1_annual_production.png")); plt.close()

def barh(data, title, path, color=ACCENT, maxn=15):
    data=data[:maxn][::-1]
    labels=[d[0][:46] for d in data]; vals=[d[1] for d in data]
    plt.figure(figsize=(10, 0.45*len(data)+1.5))
    plt.barh(labels, vals, color=color)
    for i,v in enumerate(vals): plt.text(v+0.3, i, str(v), va='center', fontsize=8)
    plt.title(title, fontweight='bold'); plt.xlabel("Documents"); plt.tight_layout()
    plt.savefig(path); plt.close()

barh(srcs,  "Most productive sources (Top 15)",      os.path.join(FIG,"fig2_top_sources.png"))
barh(ctrys, "Most productive countries (Top 15)",    os.path.join(FIG,"fig3_top_countries.png"), color=ACCENT2)
barh(auths, "Most productive authors (Top 15)",      os.path.join(FIG,"fig4_top_authors.png"))
barh(insts, "Most productive institutions (Top 15)", os.path.join(FIG,"fig5_top_institutions.png"), color=ACCENT2)
barh(kw_top20,"Most frequent author keywords (Top 15)",os.path.join(FIG,"fig6_top_keywords.png"))

draw_network(Gkw, "Author-keyword co-occurrence network (Top 55, clusters)",
             os.path.join(FIG,"fig7_keyword_cooccurrence.png"))
draw_network(Gkw, "Keyword co-occurrence — overlay by average publication year",
             os.path.join(FIG,"fig8_keyword_overlay_year.png"), cmap_year=True)
draw_network(Gcc, "Co-citation network of cited references (WoS, Top 38)",
             os.path.join(FIG,"fig9_cocitation.png"), label_attr='label')
draw_network(Gco, "Country collaboration network (Top 28)",
             os.path.join(FIG,"fig10_country_collaboration.png"))

# thematic evolution figure
plt.figure(figsize=(9,5.5))
xs=[s for s,_ in SLICES]
conv=[lexshare[s][3]*100 for s in xs]; prod=[lexshare[s][4]*100 for s in xs]
plt.plot(xs, conv, '-o', color=ACCENT, lw=2.5, label='Conversation/tutor frame')
plt.plot(xs, prod, '-s', color=ACCENT2, lw=2.5, label='Production/material frame')
for x,c,p in zip(xs,conv,prod):
    plt.text(x,c+1.2,f"{c:.0f}%",ha='center',fontsize=9,color=ACCENT)
    plt.text(x,p+1.2,f"{p:.0f}%",ha='center',fontsize=9,color=ACCENT2)
plt.title("Thematic evolution: conversation vs. production framing (% of documents)", fontweight='bold')
plt.ylabel("% of documents in time slice"); plt.legend(); plt.tight_layout()
plt.savefig(os.path.join(FIG,"fig11_thematic_evolution.png")); plt.close()

# ---- VOSviewer exports ----
export_vosviewer(Gkw, "keyword_cooccurrence")
export_vosviewer(Gcc, "cocitation", label_attr='label')
export_vosviewer(Gco, "country_collaboration")

# ---- persist computed objects for the Excel/report step ----
def net_stats(G):
    return {"nodes":G.number_of_nodes(),"edges":G.number_of_edges(),
            "density":round(nx.density(G),4),
            "components":nx.number_connected_components(G),
            "avg_degree":round(sum(dict(G.degree()).values())/max(G.number_of_nodes(),1),2)}

RESULTS = {
 "n_broad":len(BROAD), "n_focus":len(FOCUS),
 "annual":annual, "sources":srcs, "authors":auths, "countries":ctrys,
 "institutions":insts, "cited":cited, "doctypes":dtypes,
 "bradford_zones":zones, "bradford_items":src_items[:40],
 "lotka":lot, "n_authors":n_authors,
 "keywords":kw_top.most_common(40),
 "lexshare":lexshare, "slice_keywords":sl_kw,
 "net_keyword":net_stats(Gkw), "net_cocit":net_stats(Gcc), "net_country":net_stats(Gco),
}
with open(os.path.join(OUT,"_results.json"),"w",encoding="utf-8") as f:
    json.dump(RESULTS, f, ensure_ascii=False, indent=1, default=str)
print("Figures + VOSviewer files + _results.json written.")
print("Net stats:", RESULTS["net_keyword"], RESULTS["net_cocit"], RESULTS["net_country"])
print("Lex share:", lexshare)
