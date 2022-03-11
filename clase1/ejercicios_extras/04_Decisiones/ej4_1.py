import math

def ispair(num):
    if num % 2:
        return True
    else:
        return False
    
def isprime(num):
    if num < 4:
        return True
    elif (num % 2 == 0 or num % 3 == 0):
        return False
	#Itera para todos los 5k y saca el resto de ese numero y del ese numero mas 2.
	#Si encuentra un numero en que el resto es cero sale.
    for i in range(5,int(math.sqrt(num))+1,6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

print(isprime(257))
print(isprime(10000600009))
print(isprime(100123456789))
print(isprime(7))