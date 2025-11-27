import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

veri = pd.read_csv("eTicaretMusteriDavranisi.csv")

veri["Yas"] = pd.to_numeric(veri["Age"], errors="coerce")

plt.figure(figsize=(10, 6))

sns.histplot(
    data=veri,
    x="Yas",
    bins=15,
    kde=True,              
    color="#ff9eb5",       
    edgecolor="black",     
    linewidth=1
)

plt.title("Yaş Dağılımı")
plt.xlabel("Yaş")
plt.ylabel("Kişi Sayısı")

plt.xticks(range(int(veri["Yas"].min()), int(veri["Yas"].max()) + 1))

plt.show()
