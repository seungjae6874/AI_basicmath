#2020 인공지능 기초수학 1주차 실습 Q1
import numpy as np
#1-a
a = np.ones((1,5))
print("1-a :",a)

#1-b
b = np.zeros((1,5))
print("1-b :",b)

#1-c
c = np.full((1,5),5)
print("1-c :",c)

#1-d
d = np.arange(1,6)
print("1-d :",d)

#1-e
e = np.arange(1,10)
n = e[e % 2 == 1]
print("1-e :",n)

#1-f
lst = [1,5,2,3,9]
f = np.array(lst)
print("1-f :",f)

#2020 인공지능 기초수학 1주차 실습 Q2
import numpy as np
#2-a
A = np.array((1,2,1,5,4))
a = np.array((1,2,3,4,5))
q = A + a
print("2-a :",q)

#2-b
B = np.array((1,2,3,4,5))
b = np.array((5,4,3,2,1))
p = B + b
print("2-b :",p)

#2-c
C = np.full((1,9), 3, dtype = float)
c = np.full((1,9), 1, dtype = float)
r = a - b
print("2-c :",r)

#2-d
D = np.array((4,5,6))
d = np.array((3,2,1))
m = D - d
print("2-d :",m)

#2-e
E = np.array((1,1,1,1))
e = 2. * E
print("2-e :",e)

#2-f
F = np.array((0,4,2,3))
f = 3 * F
print("2-f :",f)

#2-g
G = np.array((2,4,6,8,10))
g = 1/2 * G
print("2-g :",g)

#2020 인공지능 기초수학 1주차 실습 Q3, Q4
import numpy as np
#3-a
import operator
a = [1,2,3]
b = [9,8,7]
def DP(A,B):
    mul = map(operator.mul,A,B)
    result = sum(mul)
    return result
print("3-a :",DP(a,b))

#3-b
A = np.array((1,2,3))
B = np.array((9,8,7))
C = np.sum(A * B)
print("3-b :",C)

#Q4
import math
c = np.array((6,2,4))
def ver_size(a):
    b = sum(a * a)
    result = math.sqrt(b)
    return result
print("4 :",ver_size(c))

#2020 인공지능 기초수학 1주차 실습 Q5
import numpy as np
#5-a
ax = np.array((1,0,0))
ay = np.array((0,1,0))
az = np.array((0,0,1))
print("5-a :",sum(ax * ay), sum(ax * az), sum(ay * az), sum(ax * ax))

#5-b
bx = np.array((-2,1,4))
by = np.array((1,2,0))
bz = np.array((2,-1,1.25))
print("5-b :",sum(bx * by), sum(bx * bz), sum(by * bz), sum(bx * bx))

#5-c
A = np.array([[-2,1,2],[1,2,-1],[4,0,1.25]])
B = np.array([6,4,2])
C = np.linalg.solve(A,B)
D = np.round_(C,2)
print("5-c :",D)

#5-d
a = np.array([[-2,1,2],[1,2,-1],[4,0,1.25]])
b = np.array([1,0,0])
c = np.linalg.solve(a,b)
d = np.round_(c,2)
print("5-d :",d)

#5-e
e = np.array([[-2,1,2],[1,2,-1],[4,0,1.25]])
f = np.array([2,2,2])
g = np.linalg.solve(e,f)
h = np.round_(g,2)
print("5-e :",h)

#5-f
a = np.array([[-2,1,2],[1,2,-1],[4,0,1.25]])
b = np.array([1,2,3])
c = []
for j in range(3):
    r = 0
    for i in range(3):
        s = b[i] * a[j][i]
        r = r + s
    c.append(r)
d = np.round_(c,2)
print("5-c :",d)

#5-g
a = np.array([[-2,1,2],[1,2,-1],[4,0,1.25]])
b = np.array([4,1,7])
c = []
for j in range(3):
    r = 0
    for i in range(3):
        s = b[i] * a[j][i]
        r = r + s
    c.append(r)
d = np.round_(c,2)
print("5-g :",d)

#5-h
a = np.array([[-2,1,2],[1,2,-1],[4,0,1.25]])
b = np.array([0,-1,2])
c = []
for j in range(3):
    r = 0
    for i in range(3):
        s = b[i] * a[j][i]
        r = r + s
    c.append(r)
d = np.round_(c,2)
print("5-h :",d)
