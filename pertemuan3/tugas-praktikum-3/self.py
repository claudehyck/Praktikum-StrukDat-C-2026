class Person:
  def __init__(self, name):
    self.name = name #menyimpan nilai parameter 'name' ke variabel milik objek (self.name)

  def printname(self): #mendefinisikan sebuah Method bernama printname
    print(self.name) #perintah untuk mencetak nama yang tersimpan di dalam objek tersebut

p1 = Person("Tobias") #membuat objek pertama (p1) dengan nama "Tobias"
p2 = Person("Linus") #membuat objek kedua (p2) dengan nama "Linus"

p1.printname() #memanggil method printname untuk p1
p2.printname() #memanggil method printname untuk p2
print()

#parameter tidak harus dibuat dengan nama self
#tetapi nama tersebut harus menjadi parameter pertama dari metode apa pun di dalam kelas tersebut
class Person:
  def __init__(myobject, name, age):
    myobject.name = name #contohnya bisa diganti dengan myobject.
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()
print()

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self): #method untuk menampilkan informasi lengkap mobil
    print(f"{self.year} {self.brand} {self.model}") #mengakses properti di dalam f-string (data akan diambil sesuai dari memori objek)

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info() #memanggil Method pada baris 35 yang otomatis berisi 'car1'
print()

#memanggil suatu metode dari metode lain
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self): #metode pertama : "greet"
    return "Hello, " + self.name #mengembalikan string "Hello, " ditambah nama dari properti objek

  def welcome(self): #metode kedua : "welcome", memanggil metode "greet" di dalamnya
    message = self.greet() #menggunakan 'self.greet()' untuk menjalankan metode di baris 47 dan menyimpan hasilnya ke variabel 'message'
    print(message + "! Welcome to our website.") #mencetak hasil gabungan dari metode "greet" dengan pesan tambahan

p1 = Person("Tobias")
p1.welcome() #menjalankan metode "welcome"