## Crear variable
a = 9
b = "hola"
c = True
## determinar el tipo de una variable
type(a)
type(b)
## Imprimir
print(a)
## Comparacion
var1 = 9
var2 = 6
cmp = var1 > var2

## Ejemplo filmina

mi_variable = 27
mi_flag = True

if mi_flag:
    while mi_variable > 0:
        print(mi_variable)
        mi_variable -= 1

## Condicional IF filmina
flag1 = True
flag2 = True
flag3 = True
flag4 = True
flag5 = True
flag6 = True
if (flag1 and flag2 or flag3) and not flag4:
    ##Tal Cosa
    flag1 = False
elif flag5:
    ##Tal Cosa
    flag2 = False
elif flag6:
    ##Tal Cosa
    flag4 = False
else:
    ##Tal Cosa
    flag3 = False

##Representaciones de datos
varIntHexa = 0xFF
varIntOctal = 0o321
varIntBin = 0b1100
hex(varIntOctal)

##Strings
msg = "hola mundo"
msg[0:4]
msg[5:]
msg[-1]
msg2 = "chau"
msg3 = msg + msg2 
len(msg3)

## Byte Array
byte = bytearray()
byte.append(0x02)
byte.append(0x10)
byte.append(0x05)
byte.append(0x10)
byte[0]

##Enteros: Con signo, sin límite
##Punto flotante
## Complejos

nint = 27
nfloat = 3.14
print(type(nint))
print(type(nfloat))

##Booleans
flag1 = True
flag2 = False
print(type(flag1))
print(flag2)
if flag1:
    print("verdadero!")

##Cadenas (strings)
msg = "Hola mundo"
msg = 'Hola mundo'
print(msg)
print(msg[2])
print(msg[5:10]) ## Slice Notation

##Cadenas: Operaciones
msg = "Hola"
msg2 = " mundo"
print(msg+msg2)
print(msg*2)
print("Hola" in msg)

##Cadenas: Formatting
age=35
name="Ernesto"
msg = "Hola, {1}. Tenes {0}.".format(age,name)
msg = "Hola, {1}. Tenes {0:03d}.".format(age,name)
print(msg)

##Cadenas: Formatting
age=35
name="Ernesto"
msg = "Hola, %s. Tenes %d." % (name,age)
print(msg)

##Cadenas: Formatting: f strings
age=35
name="Ernesto"
msg = f"Hola, {name}. tenes {age}."
msg = f"Hola, {name}. tenes {age*2}."
msg = f"Hola, {name}. tenes {age:03}."
msg = f"Hola, {name}. tenes {age:02x}."

##bytearray
b = bytearray()
b.append(0x02)
b.append(0x10)
b.append(0x05)
b.append(0x10)
b.append(0x03)
print(b)
print(b[3])
print(len(b))
b.remove(2) #por valor
del b[3] #por posición
item = b.pop(3) #remueve y devuelve por posición