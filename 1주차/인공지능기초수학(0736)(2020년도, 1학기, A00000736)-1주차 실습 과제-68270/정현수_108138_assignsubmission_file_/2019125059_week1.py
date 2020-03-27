#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

a = np.ones((1,5))
print("1-a:",a)

b = np.zeros((1,5))
print("1-b:",b)

c = np.full((1,5),5)
print("1-c:",c)

d = np.arange(1,6)
print("1-d:",d)

e = np.array((1,3,5,7,9))
print("1-e:",e)

f = np.array((1,5,2,3,9))
print("1-f:",f)


# In[2]:



a = np.array((1,2,1,5,4))
b = np.array((1,2,3,4,5))
print("2-a:",np.add(a,b))

c = (5,4,3,2,1)
print("2-b:",np.add(b,c))

a = np.full((1,8),3)
b = np.full((1,8),1)
print("2-c:",np.subtract(a,b))

a = np.array((4,5,6))
b = np.array((3,2,1))
print("2-d:",np.subtract(a,b))

e = np.full((1,4),1)
print("2-e:",np.multiply(e,2))

f = np.array((0,4,2,3))
print("2-f:",np.multiply(f,3))

g = np.array((2,4,6,8,10))
print("2-g:",np.multiply(g,0.5))


# In[3]:


def DP(a,b):
    c =0
    for i in range(len(a)):
        c = c+ (int(a[i])*int(b[i]))
    return c


a =(1,2,3)
b =(9,8,7)
print("3-a:",DP(a,b))

import numpy as np

a = np.array((1,2,3))
b = np.array((9,8,7))
c = a*b
d = np.sum((c),axis=0)
print("3-b:",d)



# In[4]:


def vec_size(a):
    res = (a[0]**2 + a[1]**2 + a[2]**2)**0.5
    return res

vector_c =(6,2,4)

print("4:",vec_size(vector_c))


# In[5]:



import numpy as np
ax = np.array((1,0,0))
ay = np.array((0,1,0))
az = np.array((0,0,1))
x =np.sum(ax*ay)
y =np.sum(ax*az)
z =np.sum(ay*az)
k =np.sum(ax*ax)
print("5-a:",x,y,z,k)

bx = np.array((-2,1,4))
by = np.array((1,2,0))
bz = np.array((2,-1,1.25))
x = np.sum(bx*by)
y = np.sum(bx*bz)
z = np.sum(by*bz)
k = np.sum(bx*bx)
print("5-b:",x,y,z,k)

k = np.array((6,4,2))
num1 = k*bx
num1 = np.sum(num1)
a = bx**2
a = np.sum(a)
r1 = num1/a

num2 = k*by
num2 = np.sum(num2)
b = by**2
b = np.sum(b)
r2 = num2/b

num3 = k*bz
num3 = np.sum(num3)
c = bz**2
c = np.sum(c)
r3 = num3/c

tot = (r1,r2,r3)
print("5-c:",tot)




k = np.array((1,0,0))
num1 = k*bx
num1 = np.sum(num1)
a = bx**2
a = np.sum(a)
r1 = num1/a

num2 = k*by
num2 = np.sum(num2)
b = by**2
b = np.sum(b)
r2 = num2/b

num3 = k*bz
num3 = np.sum(num3)
c = bz**2
c = np.sum(c)
r3 = num3/c

tot = (r1,r2,r3)
print("5-d:",tot)




k = np.array((2,2,2))
num1 = k*bx
num1 = np.sum(num1)
a = bx**2
a = np.sum(a)
r1 =(num1/a)


num2 = k*by
num2 = np.sum(num2)
b = by**2
b = np.sum(b)
r2 = num2/b

num3 = k*bz
num3 = np.sum(num3)
c = bz**2
c = np.sum(c)
r3 = num3/c


tot = (r1,r2,r3)
print("5-e:",tot)



q = np.array((-2,1,2))
w = np.array((1,2,-1))
e = np.array((4,0,1.25))
re = np.array((1,2,3))

a = re*q
r1 = np.sum(a)
b = re*w
r2 = np.sum(b)
c = re*e
r3 = np.sum(c)

tot = np.array((r1,r2,r3))
print("5-f:",tot)


q = np.array((-2,1,2))
w = np.array((1,2,-1))
e = np.array((4,0,1.25))
re = np.array((4,1,7))

a = re*q
r1 = np.sum(a)
b = re*w
r2 = np.sum(b)
c = re*e
r3 = np.sum(c)

tot = np.array((r1,r2,r3))
print("5-g:",tot)


q = np.array((-2,1,2))
w = np.array((1,2,-1))
e = np.array((4,0,1.25))
re = np.array((0,-1,2))

a = re*q
r1 = np.sum(a)
b = re*w
r2 = np.sum(b)
c = re*e
r3 = np.sum(c)

tot = np.array((r1,r2,r3))
print("5-h:",tot)






# In[ ]:




