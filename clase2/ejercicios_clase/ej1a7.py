from personas import Persona
#import personas
#p = personas.Persona

p = Persona()
print(type(p))
#print(p.nombre) # No hacer
#print(p.edad) # No hacer

p.set_edad(35)
print(p.get_edad())

p.set_nombre("Carlos")
print(p.get_nombre())

p.print_persona()

if p.es_mayor_de_edad():
    print("Es Mayor.")
else:
    print("Al Jardin!")
    
p2 = Persona("Guido",32)

if p.es_mayor_que(p2):
    print("Si es mayor")
else:
    print("No, es menor")
    
p1 = Persona("Carlos",27)
p2 = Persona("Leandro",27)
p3 = Persona("Ernesto",15)
p4 = Persona("Hernan",47)

l = []
l.append(p1)
l.append(p2)
l.append(p3)
l.append(p4)

for p in l:
    if p.es_mayor_de_edad():
        p.print_persona()

print(f"El mayor entre {p1.get_nombre()} y {p2.get_nombre()} es {p1.get_mayor(p2)}")

Persona.dump_csv("datos.csv",l)

loadlist = Persona.load_csv("datos.csv")
for p in loadlist:
    p.print_persona()


