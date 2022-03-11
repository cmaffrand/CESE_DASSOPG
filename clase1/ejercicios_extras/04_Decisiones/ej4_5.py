
def bisiesto(a):
    if (a % 4 == 0):
        if (a % 100 == 0):
            if (a % 400 == 0):
                return True
            return False
        return True
    return False

def diasmes(m):
    if (m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12):
        return 31
    elif (m == 4) or (m == 6) or (m == 9) or (m == 11):
        return 30
    elif (m == 2):
        return 28
    else:
        return 0
    
def validdate(d):
    if (int(d[1]) < 1) or (int(d[1]) > 12):
        return False    
    if (int(d[0]) < 1) or (int(d[0]) > diasmes(int(d[1]))):
        if bisiesto(int(d[2])) and int(d[0]) == 29:
            return True
        return False
    return True

def daystonextmonts(d):
    if not (validdate(d)):
        return False
    if int(d[1]) == 2 and bisiesto(int(d[2])):
        return 29-int(d[0])
    else:
        return diasmes(int(d[1])) - int(d[0])
    
def daysoftheyear(d):
    if not (validdate(d)):
        return False
    daux = 0
    for i in range(1,int(d[1])):
        daux = daux + diasmes(i)    
    daux = daux + int(d[0])
    if bisiesto(int(d[2]))and int(d[2]) < 2:
        daux = daux + 1
    return daux
    
def daystonextyear(d):    
    if not (validdate(d)):
        return False             
    if bisiesto(int(d[2])):
        return 366-daysoftheyear(d)
    else:
        return 365-daysoftheyear(d)
    
def daysfrom0(d):
    if not (validdate(d)):
        return False
    days = 0
    for i in range(0,int(d[2])):
        if bisiesto(i):
            days = days + 366
        else:
            days = days + 365
    return days + daysoftheyear(d)
    
def timebetweendates(d1,d2):
    if not (validdate(d1) or not (validdate(d2))):
        return False
    time = []
    maux = 0
    yaux = 0
    if daysfrom0(d1) >= daysfrom0(d2):
        if int(d1[0]) >= int(d2[0]):
            time.append(int(d1[0]) - int(d2[0]))
        else:
            time.append(diasmes(int(d2[1])) + int(d1[0]) - int(d2[0]))
            maux = 1
        if int(d1[1]) >= int(d2[1]):
            time.append(int(d1[1]) - int(d2[1]) - maux)
        else:
            time.append(12 + int(d1[1]) - int(d2[1]) - maux)
            yaux = 1
        time.append(int(d1[2]) - int(d2[2]) - yaux)
    else:
        if int(d2[0]) >= int(d1[0]):
            time.append(int(d2[0]) - int(d1[0]))
        else:
            time.append(diasmes(int(d1[1])) + int(d2[0]) - int(d1[0]))
            maux = 1
        if int(d2[1]) >= int(d1[1]):
            time.append(int(d2[1]) - int(d1[1]) - maux)
        else:
            time.append(12 + int(d2[1]) - int(d1[1]) - maux)
            yaux = 1
        time.append(int(d2[2]) - int(d1[2]) - yaux)
    return time    
       
print(bisiesto(1900))
print(bisiesto(1901))
print(bisiesto(1996))
print(bisiesto(2000))
print(bisiesto(2004))

for m in range(0,13):
    print(diasmes(m+1))

date = [0, 1, 1]
print(f"Dia: {date} Resultado: {validdate(date)}")
print(f"Dia: {date} Dias para proximo mes: {daystonextmonts(date)}")
print(f"Dia: {date} Dias para proximo año: {daystonextyear(date)}")
date = [1, 0, 1]
print(f"Dia: {date} Resultado: {validdate(date)}")
date = [32, 1, 1]
print(f"Dia: {date} Resultado: {validdate(date)}")
date = [1, 13, 1]
print(f"Dia: {date} Resultado: {validdate(date)}")
date = [1, 1, 1]
print(f"Dia: {date} Resultado: {validdate(date)}")
print(f"Dia: {date} Dias para proximo mes: {daystonextmonts(date)}")
print(f"Dia: {date} Dias para proximo año: {daystonextyear(date)}")
date = [31, 12, 2000]
print(f"Dia: {date} Resultado: {validdate(date)}")
print(f"Dia: {date} Dias para proximo mes: {daystonextmonts(date)}")
print(f"Dia: {date} Dias para proximo año: {daystonextyear(date)}")
date = [28, 2, 2000]
print(f"Dia: {date} Resultado: {validdate(date)}")
print(f"Dia: {date} Dias para proximo mes: {daystonextmonts(date)}")
print(f"Dia: {date} Dias para proximo año: {daystonextyear(date)}")
date = [29, 2, 2000]
print(f"Dia: {date} Resultado: {validdate(date)}")
print(f"Dia: {date} Dias para proximo mes: {daystonextmonts(date)}")
print(f"Dia: {date} Dias para proximo año: {daystonextyear(date)}")
date = [29, 2, 2004]
print(f"Dia: {date} Resultado: {validdate(date)}")
print(f"Dia: {date} Dias para proximo mes: {daystonextmonts(date)}")
print(f"Dia: {date} Dias para proximo año: {daystonextyear(date)}")
date = [29, 2, 1800]
print(f"Dia: {date} Resultado: {validdate(date)}")
print(f"Dia: {date} Dias para proximo mes: {daystonextmonts(date)}")
print(f"Dia: {date} Dias para proximo año: {daystonextyear(date)}")
date = [1, 1, 4]
print(f"Dia: {date} Resultado: {validdate(date)}")
print(f"Dia: {date} Dias para proximo mes: {daystonextmonts(date)}")
print(f"Dia: {date} Dias para proximo año: {daystonextyear(date)}") 

date = [1,1,0]
print(f"Days since [1, 1, 0] of {date} = {daysfrom0(date)}")
date = [2,1,0]
print(f"Days since [1, 1, 0] of {date} = {daysfrom0(date)}")
date = [1,2,0]
print(f"Days since [1, 1, 0] of {date} = {daysfrom0(date)}")
date = [31,12,0]
print(f"Days since [1, 1, 0] of {date} = {daysfrom0(date)}")
date = [1,1,1]
print(f"Days since [1, 1, 0] of {date} = {daysfrom0(date)}")
date = [2,1,1]
print(f"Days since [1, 1, 0] of {date} = {daysfrom0(date)}")

date1 = [10,1,1]
date2 = [5,1,1]
print(timebetweendates(date1,date2))
date1 = [10,1,1]
date2 = [15,1,1]
print(timebetweendates(date1,date2))
date1 = [10,2,1]
date2 = [5,1,1]
print(timebetweendates(date1,date2))
date1 = [10,2,2]
date2 = [5,12,1]
print(timebetweendates(date1,date2))
date1 = [5,2,2]
date2 = [5,12,1]
print(timebetweendates(date1,date2))
date1 = [3,2,2]
date2 = [5,12,1]
print(timebetweendates(date1,date2))
date1 = [28,2,5]
date2 = [31,12,1]
print(timebetweendates(date1,date2))