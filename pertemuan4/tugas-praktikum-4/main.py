from tabulate import tabulate # type: ignore
from kurs import data_kurs
from konverter import konversi_ke_idr, konversi_dari_idr

def tampilkan_tabel():
    print("\n=== KONVERTER MATA UANG ===")
    tabel = [[kode, f"{nilai:,}"] for kode, nilai in data_kurs.items()]
    print(tabulate(tabel, headers=["Kode", "Kurs"], tablefmt="grid"))

def main():
    tampilkan_tabel()
    
    # Input user
    dari = input("\nDari (IDR/USD/EUR/SGD/JPY): ").upper()
    ke = input("Ke   (IDR/USD/EUR/SGD/JPY): ").upper()
    jumlah = float(input("Jumlah: "))
    
    # Proses konversi (Logika: Asal -> IDR -> Tujuan)
    jumlah_idr = konversi_ke_idr(dari, jumlah)
    hasil = konversi_dari_idr(ke, jumlah_idr)
    
    # Output hasil
    if dari == "IDR":
        print(f"\nRp {jumlah:,.0f} = {hasil:.2f} {ke}")
    else:
        print(f"\n{jumlah} {dari} = {hasil:,.2f} {ke}")

if __name__ == "__main__":
    main()