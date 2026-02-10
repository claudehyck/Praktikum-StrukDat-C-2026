#Python Dictionaries
#item-item dalam dictionary dapat diurutkan, dapat diubah, dan tidak mengizinkan duplikasi
thisdict = {  
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) #tidak dapat memiliki dua item yang sama, jadi nilai duplikat akan menimpa nilai yang awal
print(len(thisdict)) #untuk mencetak berapa jumlah item dalam dictionary
print(type(thisdict)) #dictionary dapat didefinisikan sebagai objek dengan tipe data 'dict'
print()

#Access Items
#kita dapat mengakses item-item dalam dictionary dengan merujuk pada nama kuncinya, yang berada di dalam tanda kurung siku
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model") #merupakan metode lain yang akan memberi output yang sama
print(x)
x = thisdict.keys() #mengembalikan daftar semua kunci dalam dictionary tersebut
print(x)
x = thisdict.values() #mengembalikan daftar semua nilai dalam dictionary tersebut
print(x)
x = thisdict.items() #mengembalikan setiap item dalam dictionary sebagai tuple dalam sebuah daftar
print(x)
print()

#Change Items
#mengubah nilai item tertentu dengan merujuk pada nama kuncinya
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
thisdict.update({"year": 2020}) #memperbarui kamus dengan item-item dari argumen yang diberikan
print(thisdict)
print()

#Add Items
#menambahkan item kedalam kamus dilakukan dengan menggunakan kunci indeks baru dan menetapkan nilai padanya
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
print()

#Remove Items
#ada beberapa metode, antara lain pop(), del, dan clear()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") #menghapus item dengan nama kunci yang ditentukan
print(thisdict)
del thisdict["brand"] #menghapus item dengan nama kunci yang ditentukan juga
print(thisdict)
thisdict.clear() #untuk mengosongkan dictionary
print(thisdict)
print()

#Loop Dictionaries
#saat melakukan perulangan, nilai yang dikembalikan adalah kunci-kunci dictionary tersebut, tetapi ada juga metode untuk mengembalikan nilai-nilainya
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for n in thisdict:
  print(n) #cetak semua nama kunci
for n in thisdict:
  print(thisdict[n]) #cetak semua nilai
for n in thisdict.values():
  print(n) #mengembalikan nilai-nilai
for n in thisdict.keys():
  print(n) #mengembalikan kunci-kunci
for n, o in thisdict.items():
  print(n, o) #melakukan perulangan melalui kunci dan nilai
print()

#Copy Dictionaries
#dalam menyalin kamus, kita tidak dapat melakukannya dengan cara mengetik dict2=dict1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy() #menyalin dengan metode copy()
print(mydict)
mydict = dict(thisdict) #menyalin dengan metode dict()
print(mydict)
print()

#Nested Dictionaries
#sebuah dictionary dapat berisi dictionaries lain yang disebut sebagai nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])
