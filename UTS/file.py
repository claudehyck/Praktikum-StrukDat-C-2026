#Soal1
print("# Soal 1")
pengunjung_hari_ini = [ 
    {"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi", "kembali": False},
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True}, 
    {"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi", "kembali": False}, 
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True}, 
    {"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains", "kembali": False}, 
    {"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum", "kembali": False}, 
]

def tampilkan_pengunjung():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID    | Nama   | Usia | Kategori | Status Kembali")
    print("-------------------------------------------------------")

    nomor = 1
    for p in pengunjung_hari_ini:
        status = "Sudah Kembali" if p["kembali"] else "Belum Kembali"
        print(f"{nomor}  |  {p['id']} | {p['nama']}  |  {p['usia']}  |  {p['kategori']}  |  {status}")
        nomor += 1
    print()

def filter_belum_kembali():
    list_nama = [p["nama"] for p in pengunjung_hari_ini if p["kembali"] == False]
    list_nama.sort()
    
    print("===== PENGUNJUNG BELUM KEMBALI =====")
    nomor = 1
    for nama in list_nama:
        print(f"{nomor}. {nama}")
        nomor += 1
    
    print(f"Total belum kembali: {len(list_nama)} pengunjung")

tampilkan_pengunjung()
filter_belum_kembali()
print()

#Soal2
print("# Soal 2")

def info_perpustakaan():
    detail_perpus = ("Perpustakaan Kampus Terpadu", "Jl. Pendidikan No. 5, Pekanbaru", "0761-54321")
    
    print("Info Perpustakaan:")
    print(f"Nama   : {detail_perpus[0]}")
    print(f"Alamat : {detail_perpus[1]}")
    print(f"Telp   : {detail_perpus[2]}\n")

def rekap_kategori():
    kategori_buku_unik = {p["kategori"] for p in pengunjung_hari_ini}
    
    print(f"Kategori Buku Unik: {kategori_buku_unik}")
    print(f"Jumlah kategori: {len(kategori_buku_unik)}\n")

    rekap = {}
    for kategori in kategori_buku_unik:
        count = 0
        for p in pengunjung_hari_ini:
            if p["kategori"] == kategori:
                count += 1
        rekap[kategori] = count
    
    print("Rekap per kategori:")
    for x in rekap:
        print(f"{x} : {rekap[x]} pengunjung")

    max_pengunjung = 0
    for x in rekap:
        if rekap[x] > max_pengunjung:
            max_pengunjung = rekap[x]

    terbanyak = []
    for x in rekap:
        if rekap[x] == max_pengunjung:
            terbanyak.append(x)

    hasil_nama = ""
    for i in range(len(terbanyak)):
        hasil_nama += terbanyak[i]
        if i < len(terbanyak) - 1:
            hasil_nama += ", "
    
    print(f"\nKategori terbanyak: {hasil_nama} ({max_pengunjung} pengunjung)")

info_perpustakaan()
rekap_kategori()
print()

#Soal3
print("# Soal 3")
class Pengunjung:
  hitung_pengunjung = 0

  def __init__(self, id, nama, kategori):
    self.__id = id
    self.__nama = nama
    self.__kategori = kategori
    Pengunjung.hitung_pengunjung += 1

  def tampilkan_info(self):
    print("ID        :", self.__id)
    print("Nama      :", self.__nama)
    print("Kategori  :", self.__kategori)

class PengunjungPrioritas(Pengunjung):
  def __init__(self, id, nama, kategori, prioritas):
    super().__init__(id, nama, kategori)
    self.prioritas = prioritas

  def tampilkan_info(self):
    super().tampilkan_info()
    print("Prioritas :", self.prioritas)
    if self.prioritas == "Mendesak":
      print("** Layani Segera! **")

p1 = Pengunjung("M001", "Rina", "Fiksi")
p1.tampilkan_info()
print()

p2 = PengunjungPrioritas("M007", "Gilang", "Referensi", "Mendesak")
p2.tampilkan_info()
print()

print("Total pengunjung terdaftar:", Pengunjung.hitung_pengunjung)
print()

#Soal4
print("# Soal 4")
print("===== ANTRIAN PEMINJAMAN ===== ")
print("[1] M001 - Rina   | Fiksi")
print("[2] M002 - Hendra | Sains")
print("[3] M003 - Siti   | Fiksi")
print("{4] M004 - Taufik | Hukum")
print("Total antrian: 4")
print()
print("Memanggil pengunjung berikutnya...")
print("Silakan masuk: Rina (M001) - Fiksi")
print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M003 - Siti   | Fiksi")
print("[3] M004 - Taufik | Hukum")
print("Total antrian: 3 ")
print()
print("Menghapus pengunjung dengan ID M003...")
print("Siti (M003) berhasil dihapus dari antrian.")
print()
print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M004 - Taufik | Hukum")
print("Total antrian: 2")
print()
print("Mencari 'Taufik'...")
print("Ditemukan: M004 - Taufik | Hukum (posisi ke-2)")
print()
print("Total antrian: 2")