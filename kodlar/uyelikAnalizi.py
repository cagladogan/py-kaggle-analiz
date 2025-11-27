import pandas as pd
import matplotlib.pyplot as plt

# 1) Veriyi oku
musteriVerisi = pd.read_csv("eTicaretMusteriDavranisi.csv")

musteriVerisi = musteriVerisi.rename(columns={
    "Membership Type": "uyelikTipi"
})

uyelikSayilari = musteriVerisi["uyelikTipi"].value_counts()

print("Üyelik tipine göre müşteri sayıları:")
print(uyelikSayilari)

etiketler = []
for uyelik, sayi in uyelikSayilari.items():
    etiket = uyelik + " (" + str(sayi) + ")"
    etiketler.append(etiket)

plt.figure(figsize=(6, 6))
plt.pie(
    uyelikSayilari.values,  
    labels=etiketler,       
    autopct="%1.1f%%",      
    startangle=90
)
plt.title("Üyelik Tipine Göre Müşteri Dağılımı")
plt.axis("equal")           
plt.show()
