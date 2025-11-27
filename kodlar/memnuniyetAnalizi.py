import pandas as pd
import matplotlib.pyplot as plt

musteriVerisi = pd.read_csv("eTicaretMusteriDavranisi.csv")

musteriVerisi = musteriVerisi.rename(columns={"Satisfaction Level": "Memnuniyet"})

memnuniyetSayilari = musteriVerisi["Memnuniyet"].value_counts()

print("Memnuniyet düzeyine göre müşteri sayıları:")
print(memnuniyetSayilari)

etiketler = [durum + " (" + str(sayi) + ")" for durum, sayi in memnuniyetSayilari.items()]

plt.figure(figsize=(6, 6))
plt.pie(
    memnuniyetSayilari.values,
    labels=etiketler,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Memnuniyet Düzeyine Göre Müşteri Dağılımı")
plt.axis("equal")
plt.show()
