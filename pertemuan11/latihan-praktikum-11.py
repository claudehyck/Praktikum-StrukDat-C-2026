class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self.count})")

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.count -= 1
        return temp

    def peek(self):
        return self.head

    def size(self):
        return self.count

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    def display_all(self):
        if self.is_empty():
            return
        
        print("[ANTRIAN SAAT INI]")
        current = self.head
        i = 1
        while current:
            print(f"{i}. {current.nama} → {current.keluhan}")
            current = current.next
            i += 1

print("SISTEM ANTRIAN POLI UMUM") 
print("RS Sehat Bersama") 
print("========================\n")

rs_queue = Queue()

print(f"[CEK] Apakah antrian kosong? → {'YA, antrian masih kosong.' if rs_queue.is_empty() else 'TIDAK'}")

rs_queue.enqueue("Budi", "demam tinggi")
rs_queue.enqueue("Ani", "batuk pilek")
rs_queue.enqueue("Citra", "sakit kepala") 

print(f"[INFO] Jumlah pasien menunggu: {rs_queue.size()} orang")

p_next = rs_queue.peek()
if p_next:
    print(f"[PEEK] Pasien berikutnya: {p_next.nama.upper()} - {p_next.keluhan}")

p_panggil = rs_queue.dequeue()
if p_panggil:
    print(f"[PANGGIL] Dokter memanggil: {p_panggil.nama.upper()} (keluhan: {p_panggil.keluhan})")

rs_queue.enqueue("Dodi", "nyeri perut")

rs_queue.display_all()

p_panggil2 = rs_queue.dequeue()
if p_panggil2:
    print(f"[PANGGIL] Dokter memanggil: {p_panggil2.nama.upper()} (keluhan: {p_panggil2.keluhan})")

print(f"[INFO] Jumlah pasien masih menunggu: {rs_queue.size()} orang")

rs_queue.clear()

print(f"[CEK] Apakah antrian kosong? → {'YA, antrian sudah kosong.' if rs_queue.is_empty() else 'TIDAK'}")

print("\nSimulasi Selesai!")