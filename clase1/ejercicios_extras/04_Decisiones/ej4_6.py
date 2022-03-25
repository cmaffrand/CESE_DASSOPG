
def dayoftheweek(day,startday="Lunes"):
    if day < 1 or day > 366:
        return False
    
    aux = day % 7
    if aux == 0:
        return "Domingo"
    elif aux == 1:
        return "Lunes"
    elif aux == 2:
        return "Martes"
    elif aux == 3:
        return "Miercoles"
    elif aux == 4:
        return "Jueves"
    elif aux == 5:
        return "Viernes"
    elif aux == 6:
        return "Sabado"

for i in range(51,58):
    print(f"{i} -> {i%7} -> {dayoftheweek(i)}")

print(f"{0} -> {dayoftheweek(0)}")
print(f"{367} -> {dayoftheweek(367)}")