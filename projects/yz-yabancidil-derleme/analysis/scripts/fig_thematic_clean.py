#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Honest AS3 figure (clean lexicon): conversation framing decline + emergent
production framing (absolute growth & rising ratio). Overwrites fig11."""
import os,json,matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG=os.path.join(ROOT,"outputs","figures")
R=json.load(open(os.path.join(ROOT,"outputs","_as3_sensitivity.json")))
S=["2018-2021","2022-2023","2024-2026"]
conv=[R[s]["conv_pct"] for s in S]
ps=[R[s]["ps_pct"] for s in S]; pb=[R[s]["pb_pct"] for s in S]
prod_abs=[R[s]["prod_broad"] for s in S]; ratio=[R[s]["ratio_broad"] for s in S]
ACC="#2b6cb0"; ACC2="#dd6b20"; GREY="#718096"
plt.rcParams.update({"figure.dpi":150,"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(13,5.2))
# Panel A: framing prevalence (%)
ax1.plot(S,conv,'-o',color=ACC,lw=2.6,label="Conversation/tutoring frame")
ax1.plot(S,pb,'-s',color=ACC2,lw=2.6,label="Production/material frame (broad)")
ax1.plot(S,ps,'--^',color=ACC2,lw=1.6,alpha=0.7,label="Production frame (strict)")
for x,v in zip(S,conv): ax1.text(x,v+1.6,f"{v:.1f}%",ha="center",color=ACC,fontsize=9)
for x,v in zip(S,pb): ax1.text(x,v+1.6,f"{v:.1f}%",ha="center",color=ACC2,fontsize=9)
ax1.set_ylim(0,66); ax1.set_ylabel("% of documents in slice"); ax1.grid(alpha=.25)
ax1.set_title("(a) Frame prevalence",fontweight="bold"); ax1.legend(fontsize=8.5,loc="upper right")
# Panel B: absolute production + rising ratio
b=ax2.bar(S,prod_abs,color=ACC2,alpha=.8,label="Production docs (abs., broad)")
for x,v in zip(S,prod_abs): ax2.text(x,v+0.8,str(v),ha="center",fontsize=9,color=ACC2)
ax2.set_ylabel("Production documents (count)",color=ACC2); ax2.set_ylim(0,60)
ax2b=ax2.twinx(); ax2b.plot(S,ratio,'-o',color=ACC,lw=2.6,label="Production / conversation ratio")
for x,v in zip(S,ratio): ax2b.text(x,v+0.004,f"{v:.2f}",ha="center",fontsize=9,color=ACC)
ax2b.set_ylabel("Production : conversation ratio",color=ACC); ax2b.set_ylim(0,0.16)
ax2b.spines["top"].set_visible(False)
ax2.set_title("(b) Emergent production turn",fontweight="bold")
fig.suptitle("Thematic evolution (clean lexicon): conversation framing recedes; production framing emergent but rising",
             fontsize=12.5,fontweight="bold")
plt.tight_layout(rect=[0,0,1,0.96])
plt.savefig(os.path.join(FIG,"fig11_thematic_evolution.png"),bbox_inches="tight"); plt.close()
print("fig11 regenerated (honest).")
