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

    def hapus_kendaraan(self, plat):
        current = self.head

        while current:
            if current.data == plat:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None

                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                    else:
                        self.head = None

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                
                return
            
            current = current.next

    def tampilkan_maju(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

parkir = DoubleLinkedList()

parkir.tambah_kendaraan("B 1111 AA")
parkir.tambah_kendaraan("D 2222 BB")
parkir.tambah_kendaraan("A 3333 CC")
parkir.tambah_kendaraan("B 4444 DD")

print("Sebelum:")
parkir.tampilkan_maju()

parkir.hapus_kendaraan("A 3333 CC")

print("\nSesudah:")
parkir.tampilkan_maju()