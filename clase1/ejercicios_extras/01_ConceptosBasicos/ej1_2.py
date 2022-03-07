import math

def arearec(base,altura):
    return base*altura

def perimetrocir(radio):
    return math.pi*radio*2

def volumenesfera(radio):
    return 4/3*math.pi*radio**3

def areareccoord(x1,x2,y1,y2):
    area = (x1-x2)*(y1-y2)
    if area >= 0:
        return area
    else:
        return -area    

def hipotenusa(c1,c2):
    return math.sqrt(c1*c1+c2*c2)

b = 10
a = 22
x1 = 5
x2 = 10
y1 = 3
y2 = 10

print(f"Area del rectanculo: {arearec(b,a)}")
print(f"Perimetro del circulo: {perimetrocir(b)}")
print(f"Volumen de la esfera: {volumenesfera(b)}")
print(f"Area del rectanculo coordenadas: {areareccoord(x1,x2,y1,y2)}")
y1 = 10
y2 = 3
print(f"Area del rectanculo coordenadas: {areareccoord(x1,x2,y1,y2)}")
print(f"Hipotenusa: {hipotenusa(b,a)}")
