import numpy as np

def identity(num):
    m = np.zeros((num,num), dtype=int)
    for i in range(0,num):
        for j in range(0,num):
            if i==j:
                m[i,j] = 1
    print(m)

identity(5)