
import random

num = random.randrange(0,1000)
usernum = -1

while(num != usernum):
    usernum = int(input("Ingrese un numero: "))
    if num > usernum:
        print("Mayor")
    elif num < usernum:
        print("Menor")
    else:
        print("Correcto")