#Python Tuples
#kumpulan yang terurut dan tidak dapat diubah
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) #tuple mengizinkan nilai duplikat
thistuple = ("apple",) #tambahkan koma setelah item, jika tidak maka Python tidak akan mengenalinya sebagai tuple
print(type(thistuple))
print()

#Access Tuple Items
#dapat mengakses item tuple dengan merujuk pada nomor indeks
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #cetak item kedua dalam tuple
print()
#penggunaan rentang indeks sama seperti lists

#Update Tuples
#dapat mengubah tuple menjadi list, mengubah list tersebut, dan mengubah list tersebut kembali menjadi tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y #menambahkan tuple ke tuple
print(thistuple)
print()

#Unpack Tuples
#di Python, kita juga diperbolehkan untuk mengekstrak nilai kembali ke dalam variabel
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits #menggunakan * agar nilai diberikan ke variabel sebagai daftar
print(green)
print(yellow)
print(red)
print()

#Loop Tuples
#dapat looping melalui item tuple dengan for atau while
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
print()

#Join Tuples
#untuk menggabungkan dua atau lebih tuple dapat menggunakan operator +
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#mengalikan tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
