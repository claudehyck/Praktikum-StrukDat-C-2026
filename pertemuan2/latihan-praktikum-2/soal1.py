stok = [15, 50, 30, 25, 40]

stok.append(100)
print(stok)

stok.insert(2, 75)
print(stok)

stok.sort()
print(stok)

total = sum(stok)
jumlah_stok = len(stok)
rata_rata = total // jumlah_stok
print(f"Rata - rata : {rata_rata}")