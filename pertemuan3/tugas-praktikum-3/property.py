class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")
car1.brand = "Daihatsu" #memodifikasi nilai properti pada objek
del car1.model #menghapus properti dari objek
#mengakses properti objek menggunakan notasi titik
print(car1.brand)
# print(car1.model) (akan eror)
print()

class Person:
  species = "Human"  #class property, milik kelas dan semua objek

  def __init__(self, name):
    self.name = name  #instance property : milik setiap objek

p1 = Person("Emil")
p2 = Person("Tobias")

p1.city = "Pekanbaru"

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
print(p1.city)
print()

class Person:
  lastname = "" #variabel 'lastname' didefinisikan di luar __init__. (semua objek Person akan berbagi nilai yang sama untuk variabel ini)

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes" #mengubah 'lastname' langsung melalui nama Class, perubahan ini berlaku secara otomatis untuk semua objek

print(p1.lastname)
print(p2.lastname) 