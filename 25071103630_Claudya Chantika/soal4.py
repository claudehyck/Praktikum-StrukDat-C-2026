skema_komisi = (
    (100000000, 10), # Penjualan >= 100jt -> 10%
    (50000000, 5),   # Penjualan >= 50jt  -> 5%
    (20000000, 2),   # Penjualan >= 20jt  -> 2%
    (0, 0)           # Di bawah 20jt     -> 0%
)

def hitung_komisi(total_penjualan, skema, index=0):
    target = skema[index][0]
    persen = skema[index][1]

    if total_penjualan >= target:
        return persen
    else:
        return hitung_komisi(total_penjualan, skema, index + 1)

nama_sales = input("Masukkan Nama Sales: ")
total_penjualan = int(input("Masukkan Total Penjualan: "))

persen_komisi = hitung_komisi(total_penjualan, skema_komisi)

nominal_komisi = total_penjualan * persen_komisi / 100

# Menampilkan Rincian
print("\n Rincian Komisi ")
print(f"Nama Sales      : {nama_sales}")
print(f"Total Penjualan : Rp {total_penjualan:,}")
print(f"Persen Komisi   : {persen_komisi}%")
print(f"Nominal Komisi  : Rp {nominal_komisi:,}")