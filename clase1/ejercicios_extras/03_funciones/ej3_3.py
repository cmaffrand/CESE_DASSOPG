import math
import re
import numpy as np 

def normavector(x,y):
    return math.sqrt(x*x+y*y)

def vectorresta(x1,x2,y1,y2):
    r = []
    r.append(x1-x2)
    r.append(y1-y2)
    return r

def distanciapuntos(x1,x2,y1,y2):
    aux = vectorresta(x1,x2,y1,y2)
    return normavector(aux[0],aux[1])

def normalizar(x,y):
    r = []
    r.append(x/normavector(x,y))
    r.append(y/normavector(x,y))
    return r

def normaresta(x1,x2,y1,y2):
    r = vectorresta(x1,x2,y1,y2)
    return normalizar(r[0],r[1])

def proyec(x,y,cx,cy):
    dif = vectorresta(x,cx,y,cy)
    dxdy = normalizar(cx,cy)
    p11 = dxdy[0]*dxdy[0]
    p12 = dxdy[0]*dxdy[1]
    p21 = dxdy[1]*dxdy[0]
    p22 = dxdy[1]*dxdy[1]
    rx = x*p11+y*p12
    ry = x*p21+y*p22
    
def areatriangulo(x1,y1,x2,y2,x3,y3):
    x = [x1,x2,x3,x1]
    y = [y1,y2,y3,y1]
    return (x1*y2+x2*y3+x3*y1-x1*y3-x3*y2-x2*y1)/2

def productocruz(x,y):
    vx = np.array(x)
    vy = np.array(y)
    print(vx)
    print(vy)
    return vx[0]*vy[1]-vx[1]*vy[0]

def areatriangulofunc(x1,y1,x2,y2,x3,y3):
    r12 = vectorresta(x1,x2,y1,y2)
    r13 = vectorresta(x1,x3,y1,y3)
    print(r12)
    print(r13)
    return productocruz(r12,r13)/2   

x1 = -2
y1 = 3
x2 = 3
y2 = -1
x3 = 5
y3 = 6 
        
print(f"Area triangulo: {areatriangulo(x1,y1,x2,y2,x3,y3)}")
print(f"Area triangulo Funciones: {areatriangulofunc(x1,y1,x2,y2,x3,y3)}")