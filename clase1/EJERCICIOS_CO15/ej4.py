import random

def es_par(num):
    """Funcion para detectar si un numero es par

    Args:
        num (int): Entero

    Returns:
        Bool: True si el numero es par
    """
    if (num % 2 == 0):
        return True
    return False

lista = []
for i in range (10):
    lista.append(random.randrange(0,100))
    #print(len(lista))
    #print(lista)
    print(f"Numero: {lista[i]} -> Es Par: {es_par(lista[i])}")
