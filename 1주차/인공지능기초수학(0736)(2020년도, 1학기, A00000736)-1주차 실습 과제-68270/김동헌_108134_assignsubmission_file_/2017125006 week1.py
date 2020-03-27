#!/usr/bin/env python
# coding: utf-8

# In[164]:


import numpy as np

array1=np.ones(5)
print("1-a:", array1)


array2=np.zeros(5)
print("1-b:", array2)

array3=np.full(5,5)
print("1-c:", array3)

array4=np.arange(1,6)
print("1-d:", array4)

listd = [1, 3, 5, 7, 9]
array5=np.array(listd)
print("1-e:", array5)

listd = [1, 5, 2, 3, 9]
array6=np.array(listd)
print("1-f:", array6)

array1 = [1, 2, 1, 5, 4]
list1 = np.array(array1)
list2 = np.arange(1,6)
print("2-a:", list1+list2)

array1 = [5, 4, 3, 2, 1]
list1 = np.arange(1,6)
list2 = np.array(array1)
print("2-b:", list1+list2)

list1=np.full(9,3)
list2=np.ones(9)
print("2-c:", list1-list2)

list1=np.arange(4,7)
array1=[3, 2, 1]
list2=np.array(array1)
print("2-d:", list1-list2)

print("2-e:", 2*np.ones(4))

list1=[0, 4, 2, 3]
print("2-f:",3*np.array(list1))

list1=[2,4,6,8,10]
print("2-g:",(1/2)*np.array(list1))


vectora=[1,2,3]
vectorb=[9,8,7]
def DP(x, y):
    sum0=x[0]*y[0]
    sum1=x[1]*y[1]
    sum2=x[2]*y[2]
    ans=sum0+sum1+sum2
    return ans
print("3-a:",DP(vectora,vectorb))


list1=[1,2,3]
list2=[9,8,7]
array1=np.array(list1)
array2=np.array(list2)
list3=array1*array2
print("3-b:", np.sum(list3))


vectorc=[6,2,4]
def vec_size(a):
    sum0=a[0]*a[0]
    sum1=a[1]*a[1]
    sum2=a[2]*a[2]
    sum3=sum0+sum1+sum2
    return sum3**(1/2)
print("4:",vec_size(vectorc))

import numpy as np
def mul(a,b):
    x=a[0]*b[0]
    y=a[1]*b[1]
    z=a[2]*b[2]
    newvec=x+y+z
    return newvec

ax=[1,0,0]
vax=np.array(ax)
ay=[0,1,0]
vay=np.array(ay)
az=[0,0,1]
vaz=np.array(az)
bx=[-2,1,4]
vbx=np.array(bx)
by=[1,2,0]
vby=np.array(by)
bz=[2,-1,1.25]
vbz=np.array(bz)
print("5-a:", mul(ax,ay),mul(ax,az),mul(ay,az),mul(ax,ax))
print("5-b:", mul(bx,by), mul(bx,bz), mul(by,bz), mul(bx,bx))

def trunc(answer,decs=0):
    return np.trunc(answer*10**decs)/(10**decs)

va=np.array([[1,0,0],[0,1,0],[0,0,1]])
vb=np.array([[-2,1,4],[1,2,0],[2,-1,1.25]])
vbva=np.dot(np.linalg.inv(vb),va)
array = np.array([6,4,2])
print("5-c:",trunc(np.dot(array,vbva),decs=2))

vbva=np.dot(np.linalg.inv(vb),va)
array = np.array([1,0,0])
print("5-d:",trunc(np.dot(array,vbva),decs=2))

vbva=np.dot(np.linalg.inv(vb),va)
array = np.array([2,2,2])
print("5-e:",trunc(np.dot(array,vbva),decs=2))

vbva=np.linalg.inv(va)
array=np.array([1,2,3])
dotp=np.dot(va,array)
print("5-f:",np.dot(dotp,vb))

vbva=np.linalg.inv(va)
array=np.array([4,1,7])
dotp=np.dot(va,array)
print("5-g:",np.dot(dotp,vb))

vbva=np.linalg.inv(va)
array=np.array([0,-1,2])
dotp=np.dot(va,array)
print("5-h:",np.dot(dotp,vb))


# In[ ]:




