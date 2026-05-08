class BukuHash:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, kode):
        total_unicode = sum(ord(char) for char in kode)
        return total_unicode % self.size

    def insert(self, kode, judul):
        index = self._hash_function(kode)
        bucket = self.table[index]
        
        for i, item in enumerate(bucket):
            if item[0] == kode:
                bucket[i] = (kode, judul) 
                return
        
        bucket.append((kode, judul))

    def search(self, kode):
        index = self._hash_function(kode)
        bucket = self.table[index]
        
        for item in bucket:
            if item[0] == kode:
                print(f"Hasil Pencarian {kode}: {item[1]}")
                return item[1]
        
        print(f"Hasil Pencarian {kode}: Buku tidak ditemukan")
        return None

    def delete(self, kode):
        index = self._hash_function(kode)
        bucket = self.table[index]
        
        for i, item in enumerate(bucket):
            if item[0] == kode:
                bucket.pop(i)
                print(f"Buku dengan kode {kode} berhasil dihapus.")
                return
        
        print(f"Gagal menghapus: Kode {kode} tidak ditemukan.")

    def display(self):
        print("\n--- Isi Hash Table Perpustakaan ---")
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")
        print("-----------------------------------\n")

perpustakaan = BukuHash()

perpustakaan.insert("BK111", "Mahir C++ Dalam Satu Jam")
perpustakaan.insert("BK222", "Python Dasar")
perpustakaan.insert("BK333", "Matematika Diskrit")
perpustakaan.insert("BK444", "Atomic Habits")

perpustakaan.display()

perpustakaan.insert("BK045", "Mein Kampf")
perpustakaan.insert("BK111", "Bumi Manusia")

perpustakaan.display()

perpustakaan.search("BK222")
perpustakaan.search("BK999")

perpustakaan.delete("BK333")

perpustakaan.display()
