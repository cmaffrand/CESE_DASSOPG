import math

def primefactors(num):
    aux = num
    l = []
    for i in range(2,int(math.sqrt(num))+1):
        while (aux % i == 0):
           l.append(i)
           aux = aux / i
           if aux == 1:
               return l
           
    if len(l) == 0:
        l.append(num)
        
    return l

print(primefactors(121))
print(primefactors(101))
print(primefactors(720))

