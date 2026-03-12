class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def tampilkan_antrean(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def sisipkan_vip(head, plat_baru, position):
  if position == 1:
    plat_baru.next = head
    return plat_baru

  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  plat_baru.next = currentNode.next
  currentNode.next = plat_baru
  return head

node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")
node4 = Node("B 2022 EFG")

node1.next = node2
node2.next = node3
node3.next = node4

print("Setelah kendaraan bertambah:")
tampilkan_antrean(node1)

plat_baru = Node("E 555 AIO")
node1 = sisipkan_vip(node1, plat_baru, 3)

print("\nSetelah dihapus:")
tampilkan_antrean(node1)