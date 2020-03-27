#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import numpy.linalg as lin
import math

#1
a = np.ones(5)
print("1-a:",a)

a = np.zeros(5)
print("1-b:",a)

a = np.full(5,5)
print ("1-c:",a)

a = np.arange(1,6,1)
print("1-d:",a)

a = np.arange(1,10,2)
print("1-e:",a)

a = np.array([1,5,2,3,9])
print ("1-f:",a)
print ("\n")
#2
a= np.array([1,2,1,5,4])
b= np.array([1,2,3,4,5])
print("2-a:",a+b)

a= np.array([1,2,3,4,5])
b= np.array([5,4,3,2,1])
print("2-b:",a+b)

a=np.array([3, 3, 3, 3, 3, 3, 3, 3, 3])
b=np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
print("2-c:",a-b)

a=np.array([4,5,6])
b=np.array([3,2,1])
print("2-d:",a-b)

a=np.array([1,1,1,1])
print("2-e:",2*a)

a=np.array([0,4,2,3])
print("2-f:",3*a)

a=np.array([2,4,6,8,10])
print("2-g:",1/2*a)
print("\n")
#3
a = [1,2,3]
b = [9,8,7]  
def DP(a,b):
    temp = 0
    for i in range(3):
        temp += a[i]*b[i]
    return temp

print("3-a:",DP(a,b))

a = np.array([1,2,3])
b = np.array([9,8,7])
print("3-b:",np.sum(a*b))
print("\n")

#4
c = np.array([6,2,4])
def vec_size(vec):
    return np.linalg.norm(vec)
print("4:", vec_size(c))
print("\n")

#5
ax = np.array([1, 0, 0])
ay = np.array([0, 1, 0])
az = np.array([0, 0, 1])
bx = np.array([-2, 1, 4])
by = np.array([1, 2, 0])
bz = np.array([2, -1, 1.25])

print("5-a:", np.dot(ax,ay),np.dot(ax,az),np.dot(ay,az),np.dot(ax,ax))
print("5-b:", np.dot(bx,by),np.dot(bx,bz),np.dot(by,bz),np.dot(bx,bx))

n1 = np.array([6,4,2])
n2 = np.array([1,0,0])
n3 = np.array([2,2,2])
n4 = np.array([1,2,3])
n5 = np.array([4,1,7])
n6 = np.array([0,-1,2])
coora = (ax,ay,az)
coorb = (bx,by,bz)
c_invab = np.matmul(lin.inv(coora),coorb)
c_invba = np.matmul(coora,lin.inv(coorb))

print("5-c:",np.round(np.dot(n1,c_invba),2))
print("5-d:",np.round(np.dot(n2,c_invba),2))
print("5-e:",np.round(np.dot(n3,c_invba),2))
print("5-f:",np.round(np.dot(n4,c_invab),2))
print("5-g:",np.round(np.dot(n5,c_invab),2))
print("5-h:",np.round(np.dot(n6,c_invab),2))



# In[ ]:




