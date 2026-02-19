class MyClass: #membuat kelas bernama MyClass, nama kelas menggunakan awalan huruf kapital
  x = 5 #properti bernama x
p1 = MyClass() #menggunakan kelas untuk membuat objek bernama p1 
print(p1.x) #mencetak nilai x
#bisa juga membuat beberapa objek dari kelas yang sama
p2 = MyClass()
p3 = MyClass()
print(p2.x)
print(p3.x)
#jika kelas tidak memiliki isi maka bisa ditambahkan pass untuk menghindari eror (kelas tidak boleh kosong)
class Person:
  pass