import pandas as pd
import matplotlib.pyplot as plt

veri = pd.read_csv("eTicaretMusteriDavranisi.csv")

veri = veri.rename(columns={"Gender": "Cinsiyet"})

cinsiyet_sayi = veri["Cinsiyet"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    cinsiyet_sayi,
    labels=cinsiyet_sayi.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#66b3ff", "#ff9999"]  
)

plt.title("Cinsiyet Dağılımı (Pasta Grafiği)")
plt.axis("equal")   
plt.show()
