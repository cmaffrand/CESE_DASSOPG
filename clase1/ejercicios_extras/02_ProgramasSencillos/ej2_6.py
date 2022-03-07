
def factorial(a):
    f = 1
    for i in range(1,a+1):
        f = f * i
    return f

n = []
m = input("Ingrese la cantidad de numeros con los que se va a trabajar: ")
for value in range(1,int(m)+1):
    n.append(int(input(f"Ingrese el {str(value)} numero: ")))
    
for value in range(1,int(m)):
    print(f"Numero: {n[value-1]} factorial: {factorial(n[value-1])}")
    