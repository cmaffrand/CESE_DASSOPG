
import time

def password(np):
    if np == "caramelo":
        return True
    else:
        return False

s = ""
t = 0
while(not(password(s))):
    if t == 3:
        print("Cantidad de intentos permitidos superada.")
        exit()
    time.sleep(t)
    s = input("Enter Password: ")
    t = t + 1    
    
print("Password correcta!") 