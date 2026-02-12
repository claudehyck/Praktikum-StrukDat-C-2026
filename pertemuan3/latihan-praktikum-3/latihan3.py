class Cake:
  def __init__(self, cake, flavor="Sweet", diameter=16):
    self.cake = cake
    self.flavor = flavor
    self.diameter = diameter
    
  def greet(self):
    print(f"My favorite cake is : {self.cake}")

  def change_menu(self, new_cake):
    self.cake = new_cake
    print(f"Our new cake is : {new_cake}")

p1 = Cake("Choco Berry")
p2 = Cake("Mocca Tart", "Bitter", 20)
p3 = Cake("Tiramisu Cake", "Bitter", 15)

p1.greet()
print(p1.cake, p1.flavor, p1.diameter)
print(p2.cake, p2.flavor, p2.diameter)
print(p3.cake, p3.flavor, p3.diameter)
p1.change_menu("Burnt Cheese Cake")