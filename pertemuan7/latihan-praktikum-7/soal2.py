class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def tambah_kendaraan(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode

  currentNode = head
  for _ in range(position-2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

def hapus_kendaraan(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next
  currentNode= head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentBode = currentNode.next

  if currentNode.next is None:
    return head
  
  currentNode.next = currentNode.next.next
  
  return head

node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")
node4 = Node("B 2022 EFG")

node1.next = node2
node2.next = node3
node3.next = node4

newNode = Node ("E 6697 LMN")
node1 = tambah_kendaraan(node1, newNode, 5)

print("\nSetelah kendaraan bertambah :")
traverseAndPrint(node1)

node1 = hapus_kendaraan(node1, node4)

print("\nSetelah dihapus:")
traverseAndPrint(node1)