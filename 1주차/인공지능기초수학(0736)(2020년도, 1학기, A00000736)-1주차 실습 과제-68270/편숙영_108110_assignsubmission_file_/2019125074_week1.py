#1번
import numpy as np

A = np.ones(5)
print("1-a :",A)

B = np.zeros(5)
print("1-b :",B)

C = np.full((5),5)
print("1-c :",C)

D = np.arange(1,6)
print("1-d :",D)

E = np.arange(1,6)
print("1-e :",2*E-1)

F = np.array([1, 5, 2, 3, 9])
print("1-f :", F)


#2번
import numpy as np

A = np.array([1, 2, 1, 5, 4])
B = np.array([1, 2, 3, 4, 5])
print("2-a :",A+B)

C = np.array([1, 2, 3, 4, 5])
D = np.array([5, 4, 3, 2, 1])
print("2-b :",C+D)

E = np.ones(9)
print("2-c :",3*E-E)

F = np.arange(4,7)
G = np.arange(1,4)
print("2-d :", F-(4-G))

H = np.ones(4)
print("2-e :", 2*H)

I = np.array([0, 4, 2, 3])
print("2-f :", 3*I)

J = np.arange(1,6)
k = 2*J
print("2-g :", 1/2*k)


#3번
def DP(x, y):
    len_x = len(x)
    result = 0
    for i in range(0,len_x):
        result += x[i]*y[i]
    return result

a = (1, 2, 3)
b = (9, 8, 7)

print("3-a :",DP(a,b))

import numpy as np
np_a = np.array([1, 2, 3])
np_b = np.array([9, 8, 7])
print("3-b :",sum(np_a*np_b))


#4번
import numpy as np
import math

def vec_size(x):
    s = sum(x*x)
    result = math.sqrt(s)
    return result

c = np.array([6, 2, 4])
print("4 :", vec_size(c))


#5번
import numpy as np
import math

a_coo = np.array([[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]])
b_coo = np.array([[-2, 1, 4],
                [1, 2, 0],
                [2, -1, 1.25]])

print("5-a :",np.dot(a_coo[0],a_coo[1]), np.dot(a_coo[0],a_coo[2]), np.dot(a_coo[1],a_coo[2]), np.dot(a_coo[0],a_coo[0]))
print("5-b :",np.dot(b_coo[0],b_coo[1]), np.dot(b_coo[0],b_coo[2]), np.dot(b_coo[1],b_coo[2]), np.dot(b_coo[0],b_coo[0]))

a = np.array([[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]])
b = np.array([[-2, 1, 2],
            [1, 2, -1],
            [4, 0, 1.25]])

c = np.array([6, 4, 2])
c_lin = np.linalg.solve(b, c)
print("5-c :", np.round(c_lin,2))

d = np.array([1, 0 ,0])
d_lin = np.linalg.solve(b,d)
print("5-d :", np.round(d_lin,2))

e = np.array([2, 2, 2])
e_lin = np.linalg.solve(b, e)
print("5-e :", np.round(e_lin,2))

f = np.array([1, 2, 3])
print("5-f :", np.dot(b,f))

g = np.array([4, 1, 7])
print("5-g :", np.dot(b,g))

h = np.array([0, -1, 2])
print("5-h :", np.dot(b,h))