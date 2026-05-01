class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        if self.root is None:
            self.root = Node(id_buku, judul)
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
        else:
            self._insert_recursive(self.root, id_buku, judul)

    def _insert_recursive(self, current, id_buku, judul):
        if id_buku < current.id_buku:
            if current.left is None:
                current.left = Node(id_buku, judul)
                print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            else:
                self._insert_recursive(current.left, id_buku, judul)
        elif id_buku > current.id_buku:
            if current.right is None:
                current.right = Node(id_buku, judul)
                print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            else:
                self._insert_recursive(current.right, id_buku, judul)

    def search(self, id_buku):
        return self._search_recursive(self.root, id_buku)

    def _search_recursive(self, current, id_buku):
        if current is None:
            return None
        if id_buku == current.id_buku:
            return current
        if id_buku < current.id_buku:
            return self._search_recursive(current.left, id_buku)
        return self._search_recursive(current.right, id_buku)

    def traversal_inorder(self):
        print("[INFO] Koleksi Buku (In-Order Traversal):")
        self._count = 0
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current):
        if current:
            self._inorder_recursive(current.left)
            self._count += 1
            print(f"{self._count}. {current.id_buku} - {current.judul}")
            self._inorder_recursive(current.right)

    def get_min(self):
        current = self.root
        while current and current.left:
            current = current.left
        return current.id_buku if current else None

    def get_max(self):
        current = self.root
        while current and current.right:
            current = current.right
        return current.id_buku if current else None

    def height(self, node):
        if node is None:
            return -1
        left_h = self.height(node.left)
        right_h = self.height(node.right)
        return max(left_h, right_h) + 1

print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("===========================================")

perpustakaan = BST()

perpustakaan.insert(50, "Dasar Pemrograman")
perpustakaan.insert(30, "Struktur Data")
perpustakaan.insert(70, "Kecerdasan Buatan")
perpustakaan.insert(20, "Matematika Diskrit")
perpustakaan.insert(40, "Basis Data")
perpustakaan.insert(60, "Jaringan Komputer")
perpustakaan.insert(80, "Sistem Operasi")

print()

perpustakaan.traversal_inorder()

print(f"\n[SEARCH] Mencari ID 60...", end=" ")
hasil60 = perpustakaan.search(60)
if hasil60:
    print(f"Ditemukan! Judul: {hasil60.judul}")
else:
    print("Data tidak ditemukan.")

print(f"[SEARCH] Mencari ID 100...", end=" ")
hasil100 = perpustakaan.search(100)
if hasil100:
    print(f"Ditemukan! Judul: {hasil100.judul}")
else:
    print("Data tidak ditemukan.")

print(f"\n[STATISTIK] ID Terkecil: {perpustakaan.get_min()}")
print(f"[STATISTIK] ID Terbesar: {perpustakaan.get_max()}")

print(f"[INFO] Tinggi (Height) Tree: {perpustakaan.height(perpustakaan.root)}")

print("===========================================")
print("Simulasi Selesai!")