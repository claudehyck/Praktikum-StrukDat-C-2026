#Python Sets
#untuk menyimpan beberapa item dalam satu variabel
#item yang ditetapkan tidak berurutan, tidak dapat diubah, dan tidak mengizinkan nilai duplikat
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) #duplikat tidak diizinkan, true dan 1 dianggap memiliki nilai yang sama
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #cetak jumlah item dalam satu set
thisset = set(("apple", "banana", "cherry")) #menggunakan konstruktor set() untuk membuat himpunan
print(thisset)
print()

#Access Set Items
#menanyakan apakah nilai tertentu ada dalam himpunan, dengan menggunakan in kata kunci
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) #memeriksa apakah "banana" ada dalam himpunan
print()

#Add Set Items
#setelah sebuah set dibuat, tidak dapat mengubah item di dalamnya, tetapi dapat menambahkan item baru
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") #menambahkan item ke dalam suatu set
print(thisset)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) #menambahkan elemen dari tropical ke dalam thisset
print(thisset)
print()

#Remove Set Items
#untuk menghapus item dalam suatu set, gunakan metode remove() atau discard()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #menghapus "banana" dengan metode remove()
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #menghapus "banana" dengan metode discard()
print(thisset)
print()
#bisa juga dengan metode pop(), clear(), dan del sama seperti tipe data bawaan dictionaries ataupun lists

#Loop Sets
#melakukan perulangan melalui item-item dalam himpunan
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
print()

#Join Sets
#metode union() dan update() menggabungkan semua item dari kedua himpunan
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)
#metode intersection(), hanya menyimpan data duplikat
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
#metode difference() mempertahankan item dari himpunan pertama yang tidak ada di himpunan lainnya
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
#metode symmetric_difference() menyimpan semua item kecuali item duplikat
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
print()

#Frozenset
#versi himpunan yang tidak dapat diubah
#berisi elemen-elemen unik, tidak berurutan, dan tidak dapat diubah
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
