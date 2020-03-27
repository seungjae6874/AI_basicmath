import numpy as np


#1
a = np.ones(5, float)
print("1-a: ",a)
b = np.zeros(5)
print("1-b: ",b)
c = np.full(5,5)
print("1-c: ",c)
d = np.arange(1,6)
print("1-d: ",d)
e = np.array([1,3,5,7,9])
print("1-e: ",e)
f = np.array([1,5,2,3,9])
print("1-f: ",f)


#2
a1 = np.array([1,2,1,5,4])
a2 = np.array([1,2,3,4,5])
print("2-a: ",a1+a2)

b1 = np.array([1,2,3,4,5])
b2 = np.array([5,4,3,2,1])
print("2-b: ",b1+b2)

c1 = np.array([3,3,3,3,3,3,3,3,3])
c2 = np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.])
print("2-c: ",c1-c2)

d1 = np.array([4,5,6])
d2 = np.array([3,2,1])
print("2-d: ",d1-d2)

e = np.array([1.,1.,1.,1.])
print("2-e: ",2*e)

f = np.array([0,4,2,3])
print("2-f: ",3*f)

g = np.array([2.,4.,6.,8.,10.])
print("2-g: ",1/2*g)


#3

def DP(v1, v2):
    return sum([a*b for a,b in zip(v1, v2)])

a = [1,2,3]
b = [9,8,7]

print("3-a: ",DP(a,b))


a= np.array([1,2,3])
b = np.array([9,8,7])

c = a*b

d = np.sum(a*b)

print("3-b: ",d)


#4
def size_vec(input):

    return np.sqrt(np.sum(np.square(input)))

c = np.array([6,2,4])


print(size_vec(c))


#5
def X(c,a,b):
    i = np.dot(c,a)
    inv = np.linalg.inv(b)
    i2 = np.dot(i,inv)
    i2 = np.round(i2,2)
    return i2

a1 = np.array([1,0,0])
a2 = np.array([0,1,0])
a3 = np.array([0,0,1])
r_a = np.array([6,4,2])
r_a2 = np.array([2,2,2])

b1 = np.array([-2,1,4])
b2 = np.array([1,2,0])
b3 = np.array([2,-1,1.25])
r_b = np.array([1,2,3])
r_b1 = np.array([4,1,7])
r_b2 = np.array([0,-1,2])

print("5-a: ",np.dot(a1,a2), np.dot(a1,a3), np.dot(a2,a3), np.dot(a1,a1))
print("5-b: ",np.dot(b1,b2), np.dot(b1,b3), np.dot(b2,b3), np.dot(b1,b1))

a = np.array([a1,a2,a3])
b = np.array([b1,b2,b3])

c = np.array([6,4,2])
print("5-c: ", X(c,a,b))

c = np.array([1,0,0])
print("5-d: ", X(c,a,b))

c = np.array([2,2,2])
print("5-e: ", X(c,a,b))

c = np.array([1,2,3])
print("5-f: ", X(c,b,a))

c = np.array([4,1,7])
print("5-g: ", X(c,b,a))

c = np.array([0,-1,2])
print("5-h: ", X(c,b,a))
