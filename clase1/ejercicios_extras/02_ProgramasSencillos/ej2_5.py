usrnum = input("Ingrese un numero:")
acc = 0

for value in range(1,int(usrnum)+1):
    acc = acc + value
    print(f"{value} - {acc}")
    
for value in range(1,int(usrnum)+1):
    print(f"{value} - {int(value*(value+1)/2)}")
    