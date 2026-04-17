class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.current_turn = None 

    def tambah_petugas(self, nama):
        new_node = Node(nama)
        temp = self.head

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            self.current_turn = self.head
            return

        while temp.next != self.head:
            temp = temp.next
        
        temp.next = new_node
        new_node.next = self.head

    def giliran_berikutnya(self, n):
        if self.head is None:
            print("Belum ada petugas.")
            return

        for i in range(1, n + 1):
            print(f"Giliran {i}: {self.current_turn.data}")

            self.current_turn = self.current_turn.next

valet = CircularLinkedList()

valet.tambah_petugas("Andi")
valet.tambah_petugas("Budi")
valet.tambah_petugas("Citra")
valet.tambah_petugas("Dewi")

valet.giliran_berikutnya(6)