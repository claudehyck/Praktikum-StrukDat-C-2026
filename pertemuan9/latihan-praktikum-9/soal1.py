class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self, plat):
        new_node = Node(plat)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def tampilkan_maju(self):
        print("[Maju]")
        current = self.head
        if current is None:
            print("Parkiran Kosong")
            return
        
        while current:
            print(current.data)
            current = current.next
        print()

    def tampilkan_mundur(self):
        print("[Mundur]")
        current = self.tail
        if current is None:
            print("Parkiran Kosong")
            return
        
        while current:
            print(current.data)
            current = current.prev
        print()

parkir = DoubleLinkedList()

parkir.tambah_kendaraan("B 1234 ABC")
parkir.tambah_kendaraan("D 5678 XYZ")
parkir.tambah_kendaraan("A 9999 TUV")

parkir.tampilkan_maju()
parkir.tampilkan_mundur()