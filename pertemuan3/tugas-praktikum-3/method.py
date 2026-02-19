class Calculator:
  def add(self, a, b):
    return a + b #menggunakan parameter, mengembalikan hasil penjumlahan dari nilai 'a' dan 'b'

  def multiply(self, a, b):
    return a * b ##menggunakan parameter, mengembalikan hasil perkalian dari nilai 'a' dan 'b'

calc = Calculator()
print(calc.add(5, 3)) #memanggil metode add dan mengirimkan angka 5 dan 3
print(calc.multiply(4, 7)) #memanggil metode multiply dengan angka 4 dan 7
print()

#memodifikasi nilai properti
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1 #menggunakan 'self.age += 1' untuk menambah nilai properti age sebanyak 1 setiap kali metode ini dipanggil
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday() #p1.age berubah dari 25 menjadi 26
p1.celebrate_birthday() #p1.age berubah dari 26 menjadi 27