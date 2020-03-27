#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

#1번 문제
a = np.ones(5)
print ("1-a:",a)

b = np.zeros(5)
print ("1-b:",b)

c = np.full((5),5)
print ("1-c:",c)

d = np.arange((1),6)
print ("1-d:",d)

e = np.array([1,3,5,7,9])
print ("1-e:",e)

f = np.array([1,5,2,3,9])
print ("1-f:",f,'\n\n')

#2번 문제
aa = np.array([1,2,1,5,4])
ab = np.array([1,2,3,4,5])
print ("2-a:",aa+ab)

ba = np.array([5,4,3,2,1])
print ("2-b:",ba+ab)

ca = np.full(9,3)
cb = np.ones(9)
print ("2-c:",ca-cb)

da = np.array([4,5,6])
db = np.array([3,2,1])
print ("2-d:",da-db)

ea = np.ones(4)
print("2-e:",2*ea)

fa = np.array([0,4,2,3])
print("2-f:",3*fa)

ga = np.array([2,4,6,8,10])
print("2-g:",(1/2)*ga,'\n\n')

#3번 문제
a = [1,2,3]
b = [9,8,7]
def DP(x,y) :
    sum = 0
    for i in range(len(x)) :
        sum = sum + x[i]*y[i]
    return (sum)

print("3-a:",DP(a,b))

a = np.array([1,2,3])
b = np.array([9,8,7])
c = np.multiply(a,b)
print("3-b:",np.sum(c),'\n\n')

#4번 문제
c = np.array([6,2,4])

def vec_size(vec) :
    vec=np.square(vec)
    sum=np.sum(vec)
    ans=np.sqrt(sum)
    return (ans)

print ("4:",vec_size(c))
print ('\n')

#5번 문제
import numpy.linalg as lin
a = np.array([[1,0,0],[0,1,0],[0,0,1]])
b = np.array([[-2,1,4],[1,2,0],[2,-1,1.25]])
PA = np.dot(a,lin.inv(b))
PB = np.dot(b,lin.inv(a))
ao_c = np.array([6,4,2])
ao_d = np.array([1,0,0])
ao_e = np.array([2,2,2])

bo_f = np.array([1,2,3])
bo_g = np.array([4,1,7])
bo_h = np.array([0,-1,2])

print ("5-a:",np.dot(a[0,:],a[1,:]),np.dot(a[0,:],a[2,:]),np.dot(a[1,:],a[2,:]),np.dot(a[0,:],a[0,:]))
print ("5-b:",np.dot(b[0,:],b[1,:]),np.dot(b[0,:],b[2,:]),np.dot(b[1,:],b[2,:]),np.dot(b[0,:],b[0,:]))

print ("5-c:",np.round(np.dot(ao_c,PA),2))
print ("5-d:",np.round(np.dot(ao_d,PA),2))
print ("5-e:",np.round(np.dot(ao_e,PA),2))
print ("5-f:",np.round(np.dot(bo_f,PB),2))
print ("5-g:",np.round(np.dot(bo_g,PB),2))
print ("5-h:",np.round(np.dot(bo_h,PB),2))


# In[ ]:




