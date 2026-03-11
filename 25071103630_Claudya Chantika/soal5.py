inventaris = [
    {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000, 'sn': 'SAM01', 'stok': 2},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000, 'sn': 'OPP01', 'stok': 5}
]

skema_komisi = (
    (100000000, 10), (50000000, 5), (20000000, 2), (0, 0)
)

def registrasi_gadget():
    print("\n--- Tambah Gadget Baru ---")
    merk = input("Merk: ")
    tipe = input("Tipe: ")
    harga = int(input("Harga: "))
    sn = input("Serial Number (SN): ")
    stok = int(input("Stok Awal: "))
    return {'merk': merk, 'tipe': tipe, 'harga': harga, 'sn': sn, 'stok': stok}

def update_stok(katalog, sn_target, jumlah_tambah):
    ditemukan = False
    for gadget in katalog:
        if gadget['sn'] == sn_target:
            gadget['stok'] += jumlah_tambah
            ditemukan = True
            print(f"Berhasil! Stok {gadget['merk']} {gadget['tipe']} sekarang {gadget['stok']}.")
            break
    if not ditemukan:
        print("Error: Serial Number tidak ditemukan.")


def hitung_komisi(total_penjualan, skema, index=0):
    if total_penjualan >= skema[index][0]:
        return skema[index][1]
    return hitung_komisi(total_penjualan, skema, index + 1)

while True:
    print("\n=== PyGadget Hub ===")
    print("1. Tambah Gadget")
    print("2. Daftar Inventaris")
    print("3. Update Stok")
    print("4. Cek Komisi")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        gadget_baru = registrasi_gadget()
        inventaris.append(gadget_baru)
        print("Gadget berhasil ditambahkan ke inventaris!")

    elif pilihan == '2':
        print("\n--- Daftar Inventaris Produk ---")
        print(f"{'Merk':<12} | {'Tipe':<12} | {'Harga':<12} | {'SN':<8} | {'Stok':<5}")
        print("-" * 60)
        for g in inventaris:
            print(f"{g['merk']:<12} | {g['tipe']:<12} | {g['harga']:<12} | {g['sn']:<8} | {g['stok']:<5}")

    elif pilihan == '3':
        sn_input = input("Masukkan SN gadget: ")
        tambah = int(input("Masukkan jumlah tambahan stok: "))
        update_stok(inventaris, sn_input, tambah)

    elif pilihan == '4':
        nama = input("Nama Sales: ")
        penjualan = int(input("Total Penjualan: "))
        persen = hitung_komisi(penjualan, skema_komisi)
        nominal = penjualan * persen / 100
        print(f"\nSales: {nama} | Komisi: {persen}% | Total: Rp {nominal:,}")

    elif pilihan == '5':
        print("Terima kasih telah menggunakan PyGadget Hub. Sampai jumpa!")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.")