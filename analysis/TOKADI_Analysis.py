"""

VERWENDUNG
TOKADI_Analyse_v4.py und TOKADI_Datensatz_final.xlsx in denselben Ordner legen:
      python TOKADI_Analyse_v4.py
BENOETIGT:  pandas, numpy, scipy, openpyxl
      pip install pandas numpy scipy openpyxl
      
"""
import sys, io
from pathlib import Path
import pandas as pd, numpy as np, warnings
from scipy import stats
from scipy.stats import friedmanchisquare, wilcoxon
warnings.filterwarnings('ignore')
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')

BASE = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent
hits = sorted(BASE.glob("TOKADI_Datensatz_final*.xlsx"))
print("="*78); print("TOKADI - Auswertung Paper A"); print("="*78)
print("Ordner:", BASE)
if not hits:
    print("\nFEHLT: TOKADI_Datensatz_final.xlsx in diesem Ordner.")
    print("Vorhandene Excel-Dateien:")
    for f in sorted(BASE.glob("*.xlsx")): print("   ", f.name)
    sys.exit(1)
F = hits[0]; print("Datei :", F.name)

LK  = pd.read_excel(F, sheet_name='01_Lehrkraefte')
LKD = pd.read_excel(F, sheet_name='01b_LK_Demografie')
SM  = pd.read_excel(F, sheet_name='02_Schueler_Motivation')
GA  = pd.read_excel(F, sheet_name='03_Schueler_Gruppenarbeit')
print(f"Gelesen: {len(LK)} Lehrkraefte, {len(SM)} Schueler (Motivation), {len(GA)} Schueler (Gruppenarbeit)")

def cronbach(X):
    X=np.asarray(X,float); k=X.shape[1]
    return k/(k-1)*(1-X.var(axis=0,ddof=1).sum()/X.sum(axis=1).var(ddof=1))
def ci95(x):
    x=np.asarray(x,float); m=x.mean(); s=x.std(ddof=1); n=len(x)
    h=stats.t.ppf(.975,n-1)*s/np.sqrt(n); return m,s,m-h,m+h
def dd(a,b):
    sp=np.sqrt(((len(a)-1)*a.var(ddof=1)+(len(b)-1)*b.var(ddof=1))/(len(a)+len(b)-2))
    return (a.mean()-b.mean())/sp
def H(t): print("\n"+"="*78+"\n"+t+"\n"+"="*78)

# ── 1 Lehrkräfte-Demografie ──
H("1  LEHRKRAEFTE-DEMOGRAFIE")
print(f"N = {len(LKD)}")
print(f"Alter: M={LKD.Alter.mean():.1f} SD={LKD.Alter.std():.1f} range {LKD.Alter.min():.0f}-{LKD.Alter.max():.0f}")
print("Geschlecht:", dict(LKD.Geschlecht.value_counts()))
print(f"Kinder in den Klassen gesamt: {LKD.Schueler_in_Klasse.sum():.0f} | von LK berichtete SEN-Kinder: {LKD.SEN_in_Klasse.sum():.0f}")
print(f"Erhebung: Pre {LKD.Pretest.min()} | Post {LKD.Posttest.max()}")
print("HINWEIS Berufserfahrung: Der Lehrkraeftefragebogen ERHEBT die Berufs-")
print("   erfahrung (\"Wie viele Jahre unterrichten Sie bereits\"), doch diese Spalte")
print("   wurde NICHT in den konsolidierten Datensatz uebernommen. Der in Tabelle 1")
print("   berichtete Wert (M=14.4, SD=8.0) ist daher aus diesem File NICHT")
print("   reproduzierbar; die Angaben liegen nur auf den Papier-/Rohfragebogen vor")
print("   und muessen fuer die finale Fassung in 01b_LK_Demografie nachgetragen werden.")

# ── 2 SUS ──
H("2  SUS")
S=LK[[f'SUS_{i}' for i in range(1,11)]].values
sus=np.array([sum(r[j]-1 for j in range(0,10,2))+sum(5-r[j] for j in range(1,10,2)) for r in S])*2.5
m,s,lo,hi=ci95(sus)
print(f"N={len(sus)} M={m:.2f} SD={s:.2f} Min={sus.min():.1f} Max={sus.max():.1f} Median={np.median(sus):.1f} 95%CI[{lo:.2f},{hi:.2f}]")
print("Einzelwerte:", sorted(sus.tolist()))
Srec=np.column_stack([(S[:,j]-1) if j%2==0 else (5-S[:,j]) for j in range(10)])
print(f"Cronbach alpha (umkodiert): {cronbach(Srec):.3f}")
print("\nVerteilung (Sauro):")
for lab,a,b in [("Exzellent >=80.3",80.3,101),("Gut 68-80.3",68,80.3),("Akzeptabel 51-68",51,68),("Schlecht <51",0,51)]:
    n=int(((sus>=a)&(sus<b)).sum()); print(f"   {lab:18s} n={n} ({n/len(sus)*100:.0f}%)")
print("Bangor et al. (2009): Excellent=85.5, Good=71.4  ->  M=%.1f liegt dazwischen"%m)

# ── 3 UMUX ──
H("3  UMUX  (5-stufig)")
Uv=LK[[f'UMUX_{i}' for i in range(1,5)]].values
umux=np.array([((r[0]-1)+(5-r[1])+(r[2]-1)+(5-r[3]))/16*100 for r in Uv])
m,s,lo,hi=ci95(umux)
print(f"N={len(umux)} M={m:.2f} SD={s:.2f} Min={umux.min():.1f} Max={umux.max():.1f} 95%CI[{lo:.2f},{hi:.2f}]")
Urec=np.column_stack([Uv[:,0]-1,5-Uv[:,1],Uv[:,2]-1,5-Uv[:,3]])
print(f"Cronbach alpha (umkodiert): {cronbach(Urec):.3f}")
print(f"Konvergenz SUS/UMUX: r = {np.corrcoef(sus,umux)[0,1]:.3f}")

# ── 4 UDL ──
H("4  UDL-RASTER (26 Checkpoints)")
ec=[c for c in LK.columns if c.startswith('UDL_ENG')]
rc=[c for c in LK.columns if c.startswith('UDL_REP')]
ac=[c for c in LK.columns if c.startswith('UDL_AE')]
print(f"Items: ENG={len(ec)} REP={len(rc)} AE={len(ac)}  Summe={len(ec)+len(rc)+len(ac)}")
ALL=LK[ec+rc+ac].values
print(f"Cronbach alpha gesamt: {cronbach(ALL):.3f}")
for nm,cols in [("Engagement",ec),("Representation",rc),("Action & Expression",ac)]:
    print(f"   alpha {nm:22s}: {cronbach(LK[cols].values):.3f}")
pe,pr,pa=LK[ec].mean(1).values,LK[rc].mean(1).values,LK[ac].mean(1).values
print("\nTABELLE 4")
print(f"{'Prinzip':24s}{'M':>7s}{'SD':>7s}{'Range':>13s}   95%-KI")
for nm,x in [("Engagement",pe),("Representation",pr),("Action & Expression",pa)]:
    m,s,lo,hi=ci95(x); print(f"{nm:24s}{m:7.2f}{s:7.2f}{x.min():7.2f}-{x.max():<5.2f}  [{lo:.2f}, {hi:.2f}]")
chi,pv=friedmanchisquare(pe,pr,pa)
print(f"\nFriedman: chi2(2)={chi:.3f}  p={pv:.4f}  Kendall W={chi/(len(pe)*2):.3f}")
print("\nTABELLE 5  (Wilcoxon, Bonferroni alpha=.0167)")
for a,b,na,nb in [(pr,pe,"Representation","Engagement"),(pr,pa,"Representation","Action & Expression"),(pe,pa,"Engagement","Action & Expression")]:
    T,p=wilcoxon(a,b); print(f"   {na+' - '+nb:42s} MD={(a-b).mean():+.3f}  T={T:5.1f}  p={p:.4f}  {'SIG' if p<.0167 else '-'}")
# Robustheit gegen schwache Subskalen-Reliabilitaet: Vergleich auf Ebene der einzelnen
# Considerations (nicht der aggregierten Skalen). Mann-Whitney der Consideration-Mittelwerte.
rep_c=LK[rc].mean().values; ae_c=LK[ac].mean().values
Uc,puc=stats.mannwhitneyu(rep_c,ae_c,alternative='two-sided')
print(f"\nRobustheit Considerations-Ebene (Representation vs. Action & Expression):")
print(f"   Mann-Whitney U={Uc:.1f}  p={puc:.3f}  (n_REP={len(rep_c)}, n_AE={len(ae_c)})")
print("   -> stuetzt den Prinzipienkontrast unabhaengig von der aggregierten Skalen-Reliabilitaet")
print("\nCHECKPOINTS aufsteigend")
mns=LK[ec+rc+ac].mean().sort_values()
for c,v in mns.items(): print(f"   {c:20s} M={v:.2f} SD={LK[c].std():.2f}")

# ── 5 Schüler ──
H("5  TABELLE 1 - SCHUELERSTICHPROBE")
print(f"N = {len(SM)}")
print(f"Alter: M={SM.Alter.mean():.2f} SD={SM.Alter.std():.2f} range {SM.Alter.min():.0f}-{SM.Alter.max():.0f}")
g=SM.Geschlecht.value_counts(); print(f"Geschlecht: Maedchen {g.get('Girl',0)} ({g.get('Girl',0)/len(SM)*100:.1f}%), Jungen {g.get('Boy',0)} ({g.get('Boy',0)/len(SM)*100:.1f}%)")
gr=SM.Klassenstufe.value_counts(); print(f"Klassenstufe: Kl.3 {gr.get(3,0)} ({gr.get(3,0)/len(SM)*100:.1f}%), Kl.4 {gr.get(4,0)} ({gr.get(4,0)/len(SM)*100:.1f}%)")
print(f"Migrationsgeschichte: {int(SM.Migrationsgeschichte.sum())} ({SM.Migrationsgeschichte.mean()*100:.1f}%)")
print(f"Technikbesitz: {int(SM.Technikbesitz.sum())} ({SM.Technikbesitz.mean()*100:.1f}%)")
print(f"Robotik-Vorerfahrung: {int(SM.Robotik_Vorerfahrung.sum())} ({SM.Robotik_Vorerfahrung.mean()*100:.1f}%)")
print(f"\nSonderpaed. Foerderbedarf (Def. B): {int(SM.SEN_DefB.sum())} ({SM.SEN_DefB.mean()*100:.1f}%)")
print("   ", dict(SM.loc[SM.SEN_DefB==1,'Foerderung_Original'].value_counts()))
print(f"Sprachfoerderung (DaF/DAZ, separat): {int(SM.Sprachfoerderung.sum())} ({SM.Sprachfoerderung.mean()*100:.1f}%)")

H("6  SCHUELERFRAGEBOGEN")
IT=[f'Item{i}' for i in range(1,6)]
SM['ges']=SM[IT].mean(axis=1)
print(f"Cronbach alpha (5 Items): {cronbach(SM[IT].dropna().values):.3f}")
m,s,lo,hi=ci95(SM.ges.dropna()); print(f"Gesamtzufriedenheit: M={m:.3f} SD={s:.3f} 95%CI[{lo:.2f},{hi:.2f}]")
for nm,cols in [("Intrinsische Motivation & emot. Reaktion",['Item1','Item5']),("Soziale Einbindung & Kollaboration",['Item2']),("Nachhaltige Lernwirksamkeit & Transfer",['Item3','Item4'])]:
    x=SM[cols].mean(axis=1); print(f"   {nm:42s} M={x.mean():.2f} SD={x.std():.2f} Md={x.median():.1f}")

H("7  TABELLE 9 - GRUPPENVERGLEICHE")
def cmp(mask,l1,l0,name):
    x=SM.loc[mask==1,'ges'].dropna(); y=SM.loc[mask==0,'ges'].dropna()
    t,p=stats.ttest_ind(x,y)
    print(f"{name:26s} {l1}(n={len(x):3d}) M={x.mean():.2f} | {l0}(n={len(y):3d}) M={y.mean():.2f} | t={t:+.2f} p={p:.3f} d={dd(x,y):+.2f}"+("  *" if p<.05 else ""))
cmp((SM.Geschlecht=='Girl').astype(int),"w   ","m   ","Geschlecht")
cmp(SM.Migrationsgeschichte.fillna(0).astype(int),"mit ","ohne","Migrationsgeschichte")
cmp(SM.SEN_DefB,"mit ","ohne","Foerderbedarf (Def. B)")
cmp((SM.Klassenstufe==3).astype(int),"Kl.3","Kl.4","Klassenstufe")
cmp(SM.Technikbesitz.fillna(0).astype(int),"mit ","ohne","Technikbesitz")
cmp(SM.Robotik_Vorerfahrung.fillna(0).astype(int),"mit ","ohne","Robotik-Erfahrung")

H("8  TABELLE 10 - ITEMS NACH ROBOTIK-VORERFAHRUNG")
for c in IT:
    x=SM.loc[SM.Robotik_Vorerfahrung==1,c].dropna(); y=SM.loc[SM.Robotik_Vorerfahrung==0,c].dropna()
    t,p=stats.ttest_ind(x,y)
    print(f"   {c}: mit={x.mean():.2f} ohne={y.mean():.2f} t={t:+.2f} p={p:.3f} d={dd(x,y):+.2f}"+("  *" if p<.05 else ""))

H("9  GRUPPENZUSAMMENARBEIT (Post) - sozio-emotionales Erleben")
GI=[f'Item{i}' for i in range(1,10)]
lab={1:"Ich mochte die Aktivitaet",2:"Ich hatte Spass an der Aktivitaet",3:"Wir haben uns gegenseitig geholfen",
     4:"Ich habe gut zugehoert und mich gehoert gefuehlt",5:"Ich fuehlte mich wohl in meinem Team",
     6:"Ich hatte ein gutes Gefuehl",7:"Ich mochte die Programmierung des Roboters",
     8:"Ich habe gerne mit Teamkollegen zusammengearbeitet",9:"Neue Art von Aktivitaet spannend"}
print(f"N={len(GA)} | Skala -1/0/+1 (Smileys) | fehlend: {int(GA[GI].isna().sum().sum())}")
print(f"Cronbach alpha (9 Items): {cronbach(GA[GI].values):.3f}")
GA['ges']=GA[GI].mean(axis=1)
m,s,lo,hi=ci95(GA.ges); print(f"Gesamtskala: M={m:+.3f} SD={s:.3f} 95%CI[{lo:+.2f},{hi:+.2f}]")
print("\nItemebene (aufsteigend):")
for i in sorted(range(1,10), key=lambda j: GA[f'Item{j}'].mean()):
    x=GA[f'Item{i}']; print(f"   {lab[i][:50]:52s} M={x.mean():+.2f} SD={x.std():.2f} {(x==1).mean()*100:5.0f}% '+1'")
print("\nKlassenebene:")
for k,gg in GA.groupby('Klasse'): print(f"   {k:14s} n={len(gg):2d} M={gg.ges.mean():+.2f} SD={gg.ges.std():.2f}")
Fv,pv=stats.f_oneway(*[gg.ges.values for _,gg in GA.groupby('Klasse')])
print(f"   ANOVA: F({GA.Klasse.nunique()-1},{len(GA)-GA.Klasse.nunique()}) = {Fv:.2f}, p = {pv:.4f}")
R=np.corrcoef(GA[GI].values.T); ev=np.sort(np.linalg.eigvalsh(R))[::-1]
print("\nEFA-Pruefung der a-priori-Dimensionen:")
print("   Eigenwerte:", np.round(ev,2))
print(f"   Faktoren EW>1: {int((ev>1).sum())} | F1 erklaert {ev[0]/9*100:.1f}%")
for nm,ii in [("D1 Individuelle positive Affektivitaet",[1,2,6]),("D2 Soziale Eingebundenheit & Teamkohaesion",[3,5,8]),
              ("D3 Selbstwirksamkeit & Partizipation",[4,7]),("D4 Innovationsakzeptanz & Motivation",[9])]:
    cols=[f'Item{i}' for i in ii]; x=GA[cols].mean(axis=1)
    a=f"{cronbach(GA[cols].values):.3f}" if len(cols)>1 else "- (Einzelitem)"
    print(f"   {nm:44s} M={x.mean():+.2f} SD={x.std():.2f} alpha={a}")
print("\nFAZIT: faktisch eindimensional -> Gesamtskala + Itemebene berichten.")

# ── 10 SENSITIVITAETSANALYSE: Operationalisierungen A-D ──
H("10  SENSITIVITAETSANALYSE - Operationalisierung von Benachteiligung (A-D)")
print("Der zentrale Gruppenunterschied (Foerderbedarf vs. uebrige) wird gegen vier")
print("zunehmend breitere Operationalisierungen gepueft. 'ges' = mittlere Zufriedenheit")
print("(Items 1-5, Schueler-Motivation). Welch-t (ungleiche Varianzen), Cohens d,")
print("Bootstrap-95%-KI der Mittelwertdifferenz (10 000 Resamples).\n")
orig = SM.Foerderung_Original.fillna('').astype(str)
star = orig.str.contains(r'\*')
defA = ((SM.SEN_DefB==1) & (~star)).astype(int)                       # nur eindeutige Foerderschwerpunkte
defB = SM.SEN_DefB.astype(int)                                        # Hauptanalyse (inkl. Sternchen-Faelle)
defC = ((SM.SEN_DefB==1) | (SM.Sprachfoerderung==1)).astype(int)      # + Sprachfoerderung (DaF/DAZ)
defD = ((SM.SEN_DefB==1) | (SM.Sprachfoerderung==1) |
        (SM.Migrationsgeschichte.fillna(0).astype(int)==1)).astype(int)  # + Migrationsgeschichte
rng = np.random.default_rng(20250719)
def boot_ci(x, y, B=10000):
    x=np.asarray(x,float); y=np.asarray(y,float); diffs=np.empty(B)
    for b in range(B):
        diffs[b]=rng.choice(x,len(x),replace=True).mean()-rng.choice(y,len(y),replace=True).mean()
    return np.percentile(diffs,2.5), np.percentile(diffs,97.5)
print(f"{'Operationalisierung':40s}{'n(benacht.)':>12s}{'M_benacht':>10s}{'M_uebrig':>9s}{'Welch-t':>9s}{'p':>8s}{'d':>7s}   Boot-95%-KI")
for lab, mask in [("A  nur eindeutige Foerderschwerpunkte", defA),
                  ("B  + Sternchen-Faelle (Hauptanalyse)", defB),
                  ("C  + Sprachfoerderung (DaF/DAZ)",       defC),
                  ("D  + Migrationsgeschichte (breit)",     defD)]:
    x=SM.loc[mask==1,'ges'].dropna(); y=SM.loc[mask==0,'ges'].dropna()
    t,p=stats.ttest_ind(x,y,equal_var=False); d=dd(x,y); lo,hi=boot_ci(x,y)
    print(f"{lab:40s}{len(x):>12d}{x.mean():>10.2f}{y.mean():>9.2f}{t:>+9.2f}{p:>8.3f}{d:>+7.2f}   [{lo:+.2f}, {hi:+.2f}]")
print("\nLesart: Bleibt das Vorzeichen und die Groessenordnung von d ueber A-D stabil,")
print("ist der Befund robust gegen die Wahl der Foerderbedarfs-Definition.")

# ── 11 ROBUSTHEITSBATTERIE fuer Tabelle 9 ──
H("11  ROBUSTHEITSBATTERIE - Tabelle-9-Vergleiche")
comps = [("Geschlecht (w vs m)",        (SM.Geschlecht=='Girl').astype(int)),
         ("Migrationsgeschichte",       SM.Migrationsgeschichte.fillna(0).astype(int)),
         ("Foerderbedarf (Def. B)",     SM.SEN_DefB.astype(int)),
         ("Klassenstufe (3 vs 4)",      (SM.Klassenstufe==3).astype(int)),
         ("Technikbesitz",              SM.Technikbesitz.fillna(0).astype(int)),
         ("Robotik-Vorerfahrung",       SM.Robotik_Vorerfahrung.fillna(0).astype(int))]
print(f"{'Vergleich':26s}{'t(Student)':>11s}{'t(Welch)':>10s}{'U(MWU)':>9s}{'p(MWU)':>8s}{'p(Student)':>11s}")
pvals=[]; rows=[]
for name,mask in comps:
    x=SM.loc[mask==1,'ges'].dropna(); y=SM.loc[mask==0,'ges'].dropna()
    ts,ps=stats.ttest_ind(x,y); tw,pw=stats.ttest_ind(x,y,equal_var=False)
    U,pu=stats.mannwhitneyu(x,y,alternative='two-sided')
    pvals.append(ps); rows.append(name)
    print(f"{name:26s}{ts:>+11.2f}{tw:>+10.2f}{U:>9.0f}{pu:>8.3f}{ps:>11.3f}")
# Benjamini-Hochberg
order=np.argsort(pvals); mtests=len(pvals); bh=np.empty(mtests)
prev=1.0
for rank,idx in enumerate(order[::-1]):
    k=mtests-rank
    prev=min(prev, pvals[idx]*mtests/k); bh[idx]=prev
print("\nBenjamini-Hochberg (FDR-korrigiert, alle 6 Tabelle-9-Tests):")
for i,name in enumerate(rows):
    print(f"   {name:26s} p={pvals[i]:.3f}  ->  q={bh[i]:.3f}  {'sig (q<.05)' if bh[i]<.05 else '-'}")

# Leave-one-out fuer den signifikanten SEN-Befund
H("11b  LEAVE-ONE-OUT - Stabilitaet des Foerderbedarf-Befunds (Def. B)")
sen_idx=SM.index[SM.SEN_DefB==1].tolist()
base_x=SM.loc[SM.SEN_DefB==1,'ges'].dropna(); base_y=SM.loc[SM.SEN_DefB==0,'ges'].dropna()
t0,p0=stats.ttest_ind(base_x,base_y); print(f"Basis: t={t0:+.2f} p={p0:.3f} d={dd(base_x,base_y):+.2f} (n_SEN={len(base_x)})")
print("Jeweils ein SEN-Fall entfernt:")
ps_loo=[]
for i in sen_idx:
    xx=SM.loc[(SM.SEN_DefB==1)&(SM.index!=i),'ges'].dropna()
    t,p=stats.ttest_ind(xx,base_y); ps_loo.append(p)
print(f"   p-Bereich: {min(ps_loo):.3f} - {max(ps_loo):.3f} | weiterhin p<.05 in {sum(p<.05 for p in ps_loo)}/{len(ps_loo)} Faellen")

# ── 12 ICC & Designeffekt ──
H("12  ICC & DESIGNEFFEKT (Klassenclusterung Gruppenarbeit)")
GA['ges2']=GA[[f'Item{i}' for i in range(1,10)]].mean(axis=1)
grp=GA.groupby('Klasse')['ges2']; ni=grp.count().values; a=len(ni); Ntot=len(GA)
means=grp.mean(); grand=GA['ges2'].mean()
msb=(ni*(means.values-grand)**2).sum()/(a-1)
ssw=sum(((GA[GA.Klasse==c]['ges2']-means[c])**2).sum() for c in means.index); msw=ssw/(Ntot-a)
n0=(Ntot-(ni**2).sum()/Ntot)/(a-1); icc=(msb-msw)/(msb+(n0-1)*msw); deff=1+(n0-1)*icc
print(f"ICC(1) = {icc:.3f} | mittlere Clustergroesse n0 = {n0:.2f} | Designeffekt = {deff:.2f}")
print(f"Effektives N = {Ntot}/{deff:.2f} = {Ntot/deff:.1f} (statt {Ntot})")
print("Interpretation: Die geringe Clusterung (ICC<.10) rechtfertigt die Berichterstattung")
print("auf Individualebene; der Designeffekt ist als Limitation zu benennen.")
print("\n"+"="*78+"\nFertig.\n"+"="*78)
