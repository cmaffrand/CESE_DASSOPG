n = input("Ingrese N para generar un domino de NxN: ")


for i in range(0,int(n)+1):
    for j in range(0,int(n)+1):
        if j>=i:
            print(f"{i}-{j}")