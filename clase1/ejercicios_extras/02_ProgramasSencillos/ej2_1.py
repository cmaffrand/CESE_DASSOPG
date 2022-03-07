m = input("Ingrese monto: ")
i = input("Ingrese interez porcentual: ")
a = input("Ingrese periodos: ")

print(f"El dinero al pasar {a} periodos es: {str(float(m)*(1+(float(i))/100)**float(a))}")