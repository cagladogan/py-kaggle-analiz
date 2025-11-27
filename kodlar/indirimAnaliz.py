import pandas as pd
import matplotlib.pyplot as plt

musteriVerisi = pd.read_csv("eTicaretMusteriDavranisi.csv")

musteriVerisi = musteriVerisi.rename(columns={"Discount Applied": "IndirimUygulandi"})

musteriVerisi["Indirim"] = musteriVerisi["IndirimUygulandi"].map({True: "Evet", False: "Hayır"})

indirimSayilari = musteriVerisi["Indirim"].value_counts()

print("İndirim kullanımına göre müşteri sayıları:")
print(indirimSayilari)

indirimEtiketleri = [indirim + " (" + str(sayi) + ")" for indirim, sayi in indirimSayilari.items()]

plt.figure(figsize=(6, 6))
plt.pie(
    indirimSayilari.values,
    labels=indirimEtiketleri,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("İndirim Kullanımına Göre Müşteri Dağılımı")
plt.axis("equal")
plt.show()
