katalog = [
    {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok': 2},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5}
]

def update_stok(katalog, sn_target, jumlah_tambah):
    ditemukan = False
    for gadget in katalog:
        if gadget['sn'] == sn_target:
            if 'stok' in gadget:
                gadget['stok'] += jumlah_tambah
            else:
                gadget['stok'] = jumlah_tambah
            ditemukan = True
            print(f"Stok untuk SN {sn_target} berhasil ditambah sebanyak {jumlah_tambah}.")
            break
    
    if not ditemukan:
        print(f"Gadget dengan SN {sn_target} tidak ditemukan.")

def dapatkan_merk_unik(katalog):
    daftar_merk = set()
    for gadget in katalog:
        daftar_merk.add(gadget['merk'])
    return daftar_merk

update_stok(katalog, 'SAM01', 10)
update_stok(katalog, 'OPP01', 3)
update_stok(katalog, 'XIA01', 5)  

daftar_merk = dapatkan_merk_unik(katalog)
print("\nDaftar Merk Unik di Katalog :")
print(daftar_merk)

print("\nData Katalog Terbaru :")
for item in katalog:
    print(item)