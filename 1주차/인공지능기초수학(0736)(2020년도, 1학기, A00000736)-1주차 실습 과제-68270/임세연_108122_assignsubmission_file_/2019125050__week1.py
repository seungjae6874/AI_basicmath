#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
#1
a=np.ones(5)
print('1-a:',a)

b=np.zeros(5)
print('1-b:',b)

c=np.full((5),5)
print('1-c:',c)

d=np.arange(1,6)
print('1-d:',d)

e=np.array((1,3,5,7,9))
print('1-e:',e)

list1=[1,5,2,3,9]
f=np.array(list1)
print('1-f:',f)

#2
a=np.array([1,2,1,5,4])
b=np.arange(1,6)
print('2-a:',a+b)

c=np.arange(1,6)
d=np.array([5,4,3,2,1])
print('2-b:',c+d)

e=np.ones(9)
print('2-c:',3*e-e)

f=np.arange(4,7)
g=np.arange(3,0,-1)
print('2-d:',f-g)

h=np.ones(4)
print('2-e:',2*h)

i=np.array([0,4,2,3])
print('2-f:',3*i)

j=np.arange(1,6)
k=2*j
print('2-g:',1/2*k)

#3
import math
def DP(a,b):
    product=a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    return product
a=[1,2,3]
b=[9,8,7]
print('3-1:',DP(a,b))

def dp(a,b):
    product=np.dot(a,b)
    return product
a=np.array([1,2,3])
b=np.array([9,8,7])
print('3-2:',dp(a,b))


#4
def vec_size(a):
    len_a=len(a)
    b=0
    b=sum(a*a)
    result=math.sqrt(b)
    return result
c=np.array([6,2,4])
print('4:',vec_size(c))

#5
a=np.array([[1,0,0],
           [0,1,0],
           [0,0,1]])
b=np.array([[-2,1,4],
            [1,2,0],
            [2,-1,1.25]])
print('5-a:',sum(a[0]*a[1]),sum(a[0]*a[2]),sum(a[1]*a[2]),sum(a[0]*a[0]))
print('5-b:',sum(b[0]*b[1]),sum(b[0]*b[2]),sum(b[1]*b[2]),sum(b[0]*b[0]))

A=np.array([[1,0,0],
         [0,1,0],
         [0,0,1]])
B=np.array([[-2,1,2],
            [1,2,-1],
           [4,0,1.25]])
a1=np.array([6,4,2])
a2=np.array([1,0,0])
a3=np.array([2,2,2])
b1=np.array([1,2,3])
b2=np.array([4,1,7])
b3=np.array([0,-1,2])
l=np.linalg.solve(B,a1)
k=np.linalg.solve(B,a2)
m=np.linalg.solve(B,a3)
n=np.linalg.solve(A,b1)
o=np.linalg.solve(A,b2)
p=np.linalg.solve(A,b3)
print('5-c:',l)
print('5-d:',k)
print('5-e:',m)
print('5-f:',n)
print('5-g:',o)
print('5-h:',p)


# In[ ]:




