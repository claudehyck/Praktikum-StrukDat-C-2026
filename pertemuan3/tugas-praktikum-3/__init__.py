class Person:
  def __init__(self, name, age): #metode __init__ dilakukan untuk menetapkan nilai untuk nama dan usia
    self.name = name #mengambil nilai 'name' dari input dan menyimpannya ke variabel milik objek
    self.age = age #mengambil nilai 'age' dari input dan menyimpannya ke variabel milik objek

p1 = Person("Emil", 36) #membuat objek p1 dari Person dengan nama "Emil" dan usia 36

print(p1.name)
print(p1.age)