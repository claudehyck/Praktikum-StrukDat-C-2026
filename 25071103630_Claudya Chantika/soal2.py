stok_gadget = [ 
{'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000}, 
{'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000}, 
{'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000}, 
{'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000}, 
] 

def filter_harga(data, min_harga, max_harga):
    hasil_filter = []
    for gadget in data:
        if gadget['harga'] >= min_harga and gadget['harga'] <= max_harga:
            hasil_filter.append(gadget)
    return hasil_filter

batas_bawah = int(input("Masukkan batas bawah harga: "))
batas_atas = int(input("Masukkan batas atas harga: "))

hasil = filter_harga(stok_gadget, batas_bawah, batas_atas)

if len(hasil) > 0:
    print("Hasil filter gadget:")
    for g in hasil:
        print(f"- {g['merk']} {g['tipe']} (Rp {g['harga']})")
else:
    print("Tidak ada gadget dalam rentang harga tersebut.")