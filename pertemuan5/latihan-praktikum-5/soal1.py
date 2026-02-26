stok_barang = [15, 40, 30, 10, 25]

#a
print(stok_barang.index(10))
stok_barang[3] = 50

#b
stok_barang.append(5)
print(stok_barang)
stok_barang.sort(reverse=True)
print(stok_barang)

#c
total = sum(stok_barang)
print(total)

#d
rata = sum(stok_barang) / len(stok_barang)
nilai = "stok aman" if rata >20 else "waspada"
print(nilai)