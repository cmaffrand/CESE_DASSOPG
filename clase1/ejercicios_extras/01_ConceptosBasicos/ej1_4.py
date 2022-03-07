
def printbasicoperations(a,b):
    print(f"Suma: {a+b}")
    print(f"Resta: {a-b}")
    print(f"Multiplicacion: {a*b}")
    print(f"Division: {a/b}")
    
def tablademultiplicar(a):
    for i in range(11):
        print(f"{a} molitplicado por {i} es igual a {a*i}")      

def factorial(a):
    f = 1
    for i in range(1,a+1):
        f = f * i
    print(f"El factorial de {a} es {f}")

a = 32
b = 10
printbasicoperations(a,b)
tablademultiplicar(a)
factorial(a)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                      