#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PRISMA 2020 flow diagram (database searches) — two streams:
bibliometric corpus (broad) + nested synthesis subset (focused). PNG + PDF + SVG."""
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG=os.path.join(ROOT,"outputs","figures"); os.makedirs(FIG,exist_ok=True)

ACC="#2b6cb0"; DARK="#1a365d"; GREY="#4a5568"; BG="#eef4fb"; EXC="#fbeae8"; EXCB="#c05621"
GREEN="#276749"; GREENBG="#e6f4ea"

fig,ax=plt.subplots(figsize=(12.5,13)); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis("off")

def box(x,y,w,h,text,fc=BG,ec=ACC,tc="#1a202c",fs=10.5,bold=False):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle="round,pad=0.4,rounding_size=1.2",
        linewidth=1.6,edgecolor=ec,facecolor=fc))
    ax.text(x,y,text,ha="center",va="center",fontsize=fs,color=tc,
            fontweight=("bold" if bold else "normal"),wrap=True)
def arrow(x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=16,
        linewidth=1.5,color=GREY,shrinkA=2,shrinkB=2))
def stage(y,label):
    ax.add_patch(FancyBboxPatch((0.5,y-4.5),5.5,9,boxstyle="round,pad=0.2",
        linewidth=0,facecolor=DARK))
    ax.text(3.2,y,label,ha="center",va="center",fontsize=11,color="white",
            fontweight="bold",rotation=90)

ax.text(50,98,"PRISMA 2020 Akış Diyagramı — Veri Tabanı Aramaları",
        ha="center",fontsize=15,fontweight="bold",color=DARK)
ax.text(50,95.2,"GenAI × Yabancı Dil Eğitimi · WoS Core Collection + Scopus · 2018–2026 · 19.06.2026",
        ha="center",fontsize=9.5,color=GREY)

# Stage bands
stage(82,"Tanımlama")
stage(58,"Tarama")
stage(28,"Dahil Etme")

LX=40   # left column x (broad / bibliometric)
RX=78   # right column exclusions

# IDENTIFICATION
box(LX,86,52,8,"Veri tabanlarından tanımlanan kayıtlar (geniş katman, A∧D)\nWeb of Science (n = 1.936)  ·  Scopus (n = 2.824)\nToplam n = 4.760",fc="#dbeafe",bold=False)
box(LX,75.5,52,7,"İkilemeden arındırma öncesi çıkarılan mükerrer kayıtlar\nDOI + normalleştirilmiş başlık-yıl eşleşmesi:  n = 1.706",fc=EXC,ec=EXCB,tc="#7b341e")
arrow(LX,82,LX,79)

# SCREENING
box(LX,64,52,7,"İkilemeden arındırılmış kayıtlar (taramaya giren)\nn = 3.054",bold=True)
arrow(LX,72,LX,67.6)
box(RX,54,34,8,"Taramada çıkarılan kayıtlar\nGeri çekilmiş yayınlar (retracted):  n = 4\n(Yıl 2018–2026, İngilizce, makale/derleme/\nbildiri sınırı dışa aktarımda uygulandı)",fc=EXC,ec=EXCB,tc="#7b341e",fs=9.5)
arrow(LX,60.5,LX,54)
arrow(LX,54,RX-17,54)

# INCLUDED (bibliometric)
box(LX,44,52,8,"BİBLİYOMETRİK KORPUS (dahil edilen)\nn = 3.050\nPerformans + bilim haritalama + tematik evrim",fc=GREENBG,ec=GREEN,tc=GREEN,bold=True)
arrow(LX,50,LX,48)

# NESTED SYNTHESIS SUBSET
ax.text(50,36.5,"— Sentez alt-kümesi (odaklı katman, A∧D∧C) —",ha="center",fontsize=10,
        fontweight="bold",color=DARK)
box(28,30,40,8,"Sentez için tanımlanan kayıtlar (A∧D∧C)\nWoS (n = 174) · Scopus (n = 303)\nToplam n = 477 → ikilemeden arındırma → n = 329",fc="#dbeafe",fs=9.5)
box(72,30,38,7,"Mükerrer kayıtlar çıkarıldı\nn = 148",fc=EXC,ec=EXCB,tc="#7b341e",fs=9.5)
arrow(48,30,53,30)

box(28,19,40,7.5,"Uygunluk için (tam metin) değerlendirilen\nn = 329",bold=True,fs=10)
arrow(28,26,28,22.8)
box(72,19,38,8,"Uygunluk değerlendirmesi — SONRAKİ ADIM\nTam metin tarama + κ; dahil/dışla gerekçeleri\nHedef nitel sentez: 20–60 çalışma",fc="#fff7e6",ec="#b7791f",tc="#744210",fs=9)
arrow(48,19,53,19)

box(28,9,40,7,"Nitel sentez için dahil edilecek çalışmalar\n(uygunluk taraması beklemede)",fc="#edf2f7",ec=GREY,tc=GREY,fs=9.5,bold=False)
arrow(28,15.2,28,12.6)

ax.text(50,2.2,"Not: Eş-atıf ve bibliyografik eşleşme yalnızca atıflanan referansı bulunan WoS kayıtlarıyla (n = 1.929) kurulmuştur.",
        ha="center",fontsize=8.5,color=GREY,style="italic")

plt.tight_layout()
for ext in ("png","pdf","svg"):
    plt.savefig(os.path.join(FIG,f"fig0_PRISMA_flow.{ext}"),bbox_inches="tight",dpi=200)
plt.close()
print("PRISMA diagram written: fig0_PRISMA_flow.{png,pdf,svg}")
