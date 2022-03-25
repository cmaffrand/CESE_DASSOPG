
m = 0
acc = 0
calc = True

while calc:
    new = input("Ingrese un numero para agregarlo al promedio :")
    m = m + 1
    try:
        acc = acc + int(new)
        print(f"Promedio: {acc/m} Muestras: {m}")
    except:
        print("Excepcion -> Debe ingresar un valor numerico.")
        calc = False
  