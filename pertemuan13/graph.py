class Graph:
    def __init__(self):
        self.adj_list = {}

    def tambah_kota(self, nama):
        if nama not in self.adj_list:
            self.adj_list[nama] = []

    def tambah_jalan(self, u, v, jarak):
        self.tambah_kota(u)
        self.tambah_kota(v)
        self.adj_list[u].append((v, jarak))
        self.adj_list[v].append((u, jarak))

    def tampilkan_graph(self):
        print("\n[INFO] Struktur Jaringan Distribusi:")
        for kota in self.adj_list:
            tetangga = ", ".join([f"{t[0]} ({t[1]})" for t in self.adj_list[kota]])
            print(f"   {kota} terhubung ke: {tetangga}")

    def dijkstra(self, kota_asal):
        jarak = {kota: float('inf') for kota in self.adj_list}
        jarak[kota_asal] = 0

        dikunjungi = []
        kota_belum_dikunjungi = list(self.adj_list.keys())

        print(f"\n[PROSES] Menghitung rute terpendek dari: {kota_asal}...")

        while kota_belum_dikunjungi:
            kota_sekarang = None
            for kota in kota_belum_dikunjungi:
                if kota_sekarang is None:
                    kota_sekarang = kota
                elif jarak[kota] < jarak[kota_sekarang]:
                    kota_sekarang = kota

            if jarak[kota_sekarang] == float('inf'):
                break

            kota_belum_dikunjungi.remove(kota_sekarang)

            for tetangga, bobot in self.adj_list[kota_sekarang]:
                jalur_baru = jarak[kota_sekarang] + bobot
                if jalur_baru < jarak[tetangga]:
                    jarak[tetangga] = jalur_baru

        return jarak

navigasi = Graph()

print("SISTEM NAVIGASI LOGISTIK \"KILAT MAJU\"")
print("======================================")

print(f"[INPUT] Menambahkan jalan: Jakarta - Bandung (150 km)")
navigasi.tambah_jalan("Jakarta", "Bandung", 150)

print(f"[INPUT] Menambahkan jalan: Jakarta - Cirebon (200 km)")
navigasi.tambah_jalan("Jakarta", "Cirebon", 200)

print(f"[INPUT] Menambahkan jalan: Bandung - Tasikmalaya (100 km)")
navigasi.tambah_jalan("Bandung", "Tasikmalaya", 100)

print(f"[INPUT] Menambahkan jalan: Bandung - Cirebon (130 km)")
navigasi.tambah_jalan("Bandung", "Cirebon", 130)

print(f"[INPUT] Menambahkan jalan: Cirebon - Semarang (250 km)")
navigasi.tambah_jalan("Cirebon", "Semarang", 250)

print(f"[INPUT] Menambahkan jalan: Tasikmalaya - Semarang (200 km)")
navigasi.tambah_jalan("Tasikmalaya", "Semarang", 200)

navigasi.tampilkan_graph()

hasil_dijkstra = navigasi.dijkstra("Jakarta")

print(f"\n[HASIL] Jarak Terpendek dari Jakarta:")
i = 1
for kota, dist in hasil_dijkstra.items():
    if kota != "Jakarta":
        print(f"{i}. Ke {kota}: {dist} km")
        i += 1

print("============================")
print("\nSimulasi Navigasi Selesai!")
