total_harga = 0
karakter_salah = []
while True :
    jml_barang = int(input("Entrikan jumlah barang yang dibeli : "))
    harga_barang = float(input("Entrikan harga satuan barangnya : "))
    total_harga += jml_barang * harga_barang

    tambahan_item = input("Apakah ada lagi item barang yang dientrikan atau tidak? [y]/[t] ")
    while tambahan_item != "y" and tambahan_item != "t" :
        karakter_salah.append (tambahan_item)
        tambahan_item = input("Apakah ada lagi item barang yang dientrikan atau tidak? [y]/[t] ")

    if tambahan_item == "t":
        break
        
print ("Total pembayaran : Rp.", total_harga)        
for i in range(len(karakter_salah)):
    print("Karakter salah index ke ",i," adalah " , (karakter_salah[i]))
