#Python Lists
#list digunakan untuk menyimpan banyak item dalam satu variabel
thislist = ["apple", "banana", "cherry", "banana"] #mengizinkan duplikat
print(thislist)
print(len(thislist)) #cetak jumlah item
list1 = ["abc", 34, True, 40, "male"]
print(list1) #berisi nilai berbagai tipe data
print(type(list1)) #mengetahui tipe data
print()

#Access List Items
#item dalam daftar diindeks dan dapat diakses dengan merujuk pada nomor indeks
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #cetak item kedua
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #cetak item terakhir dengan pengindeksan negatif
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #kembalikan item ketiga, keempat, dan kelima
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #mengembalikan item dari awal hingga sebelum indeks 4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #mengembalikan item dari indeks 2 hingga akhir
print()

#Change List Items
#untuk mengubah nilai item tertentu, lihat nomor indeksnya
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #ubah item kedua
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) #ganti nilai "banana" dan "cherry" menjadi nilai "blackcurrant" dan "watermelon"
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #menyisipkan item baru tanpa mengganti nilai yang sudah ada
print(thislist)
print()

#Add List Items
#untuk menambahkan item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") #untuk menambahkan item ke akhir daftar
print(thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #untuk menambahkan elemen dari daftar lain ke daftar saat ini
print(thislist)
print()

#Remove List Items
#hapus item yang ditentukan
thislist = ["apple", "cherry", "banana"]
thislist.remove("banana") #untuk menghapus "banana"
print(thislist)
thislist.pop(1) #menghapus indeks yang ditentukan
print(thislist)
del thislist[0] #menghapus item pertama berdasarkan indeks
print(thislist)
print()

#Loop Lists
#mengulang melalui item daftar
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)): #cetak semua item dengan merujuk pada nomor indeks
  print(thislist[i])
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist): #cetak semua item menggunakan perulangan while untuk menelusuri semua indeks
  print(thislist[i])
  i = i + 1
print()

#List Comprehension
#menawarkan sintaks yang lebih singkat ketika ingin membuat daftar baru berdasarkan nilai-nilai dari daftar yang sudah ada
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits: #tanpa list comprehension harus menggunakan for
  if "a" in x:
    newlist.append(x)
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] #dengan comprehension
print(newlist)
print()

#Sort List
#metode yang akan mengurutkan daftar secara alfanumerik, manaik, secara default
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"] #mengurutkan secara alfabetis
thislist.sort()
print(thislist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) #mengurutkan secara menurun
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower) #mengurutkan secara alfabetis dari huruf awal yang kecil
print(thislist)
print()

#Copy List
#dapat dilakukan dengan metode copy(), list(), operator slice[:]
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
print()

#Join Lists
#untuk menggabungkan, atau menyatukan, dua atau lebih daftar di Python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2 #menggabungkan dua daftar
print(list3)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x) #menambahkan semua item dari daftar2 ke daftar1
print(list1)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2) #menambahkan elemen dari satu daftar ke daftar lain
print(list1)
