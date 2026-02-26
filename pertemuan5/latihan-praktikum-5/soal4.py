gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5}, 
{"item": "Keyboard", "harga": 400000, "stok": 12}, 
{"item": "Mouse", "harga": 250000, "stok": 20} 
]

#a
for produk in gudang_pc:
    if produk["item"] == "Keyboard" : produk["kategori"] = "Aksesoris"

#b
gudang_pc.append({"item":"Headset", "harga":350000, "stok":8})

#c
for produk in gudang_pc :
    total_aset = produk["harga"] * produk["stok"]
    print(f"item:{produk["item"]} | total_aset : {total_aset}")