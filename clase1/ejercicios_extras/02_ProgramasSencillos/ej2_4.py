usrnum1 = input("Ingrese un numero:")
usrnum2 = input("Ingrese otro numero:")

if usrnum1 >= usrnum2:
    maximo = int(usrnum1)
    minimo = int(usrnum2)
else:
    maximo = int(usrnum2)
    minimo = int(usrnum1)
    
for value in range(minimo+1,maximo):
    if value % 2 == 0:
        print(value)