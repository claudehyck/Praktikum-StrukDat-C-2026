barang = ("B001", "Laptop Gaming", 15000000)

(kode, nama, harga) = barang
print(f"Kode : {kode}")
print(f"Nama : {nama}")
print(f"Harga : {harga}")

print(barang[2])

y = list(barang)
y[3] = 14000000
barang = tuple(y)