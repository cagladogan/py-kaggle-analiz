import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

veri = pd.read_csv("eTicaretMusteriDavranisi.csv")

sehir_sayilari = veri["City"].value_counts()

plt.figure(figsize=(10,5))
ax = sns.barplot(x=sehir_sayilari.index, y=sehir_sayilari.values, color="#86c5da")

plt.title("Şehirlere Göre Müşteri Dağılımı")
plt.xticks(rotation=45)

for i, v in enumerate(sehir_sayilari.values):
    ax.text(i, v + 1, str(v), ha="center", fontweight="bold")

plt.show()
