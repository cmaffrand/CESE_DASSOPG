from re import S


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        
print("Inicio del programa figuras")
r = Rectangle(10,20)
print(f"Rectangulo: Area = {r.area()} Perimetro = {r.perimeter()} ")
print(type(r))


c = Square(10)
print(f"Cuadrado: Area = {c.area()} Perimetro = {c.perimeter()} ")
print(type(c))

print(f" R es Rectangle? -> {isinstance(r, Rectangle)}")
print(f" R es Square? -> {isinstance(r,Square)}")
print(f" C es Rectangle? -> {isinstance(c, Rectangle)}")
print(f" C es Square? -> {isinstance(c,Square)}")