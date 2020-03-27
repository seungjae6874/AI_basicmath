#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.ones(5)
print("1-a:", a)
b=np.zeros(5)
print("1-b:", b)
c=np.full(5,5)
print("1-c:", c)
d=np.arange(1,6)
print("1-d:", d)
e=np.array([1,3,5,7,9])
print("1-e:", e)
f=np.array([1,5,2,3,9])
print("1-f:", f)


# In[2]:


a=np.array([1,2,1,5,4])+np.array([1,2,3,4,5])
print("2-a:", a)
b=np.array([1,2,3,4,5])+np.array([5,4,3,2,1])
print("2-b:", b)
c=np.full(9,3)-np.full(9,1)
print("2-c:", c)
d=np.array([4,5,6])-np.array([3,2,1])
print("2-d:", d)
e= 2*np.full(4,1)
print("2-e:", e)
f=3*np.array([0,4,2,3])
print("2-f:", f)
g= 1/2*np.array([2,4,6,8,10])
print("2-g:", g)


# In[3]:


#3-a
a=[1,2,3]
b=[9,8,7]
def DP(a,b):
    return sum([ai*bi for ai,bi in zip(a,b)])
print("3-a:",DP(a,b))
#3-b
a=np.array([1,2,3])
b=np.array([9,8,7])
print("3-b:",np.dot(a,b.T))


# In[4]:


c=np.array([6,2,4])
def vec_size(c):
    return np.sum(c**2)**0.5
print("4:",vec_size(c))


# In[23]:


np.set_printoptions(precision=2)
# a coordiante
ax = np.array([1,0,0])
ay = np.array([0,1,0])
az = np.array([0,0,1])
# b coordinate
bx = np.array([-2,1,4])
by = np.array([1,2,0])
bz = np.array([2,-1,1.25])
b=np.array([[-2,1,4],
             [1,2,0],
             [2,-1,1.25]])

def r_b(n):
    x = np.dot(n,bx)/np.dot(bx,bx)
    y = np.dot(n,by)/np.dot(by,by)
    z = np.dot(n,bz)/np.dot(bz,bz)
    return np.array([x,y,z])

print("5-a:", np.dot(ax,ay), np.dot(ax,az), np.dot(ay,az), np.dot(ax,ax),)
print("5-b:", np.dot(bx,by), np.dot(bx,bz), np.dot(by,bz), np.dot(bx,bx),)
print("5-c:", r_b(np.array([6,4,2])))
print("5-d:", r_b(np.array([1,0,0])))
print("5-e:", r_b(np.array([2,2,2])))
print("5-f:", np.dot(b.T,np.array([1,2,3])))
print("5-g:", np.dot(b.T,np.array([4,1,7])))
print("5-h:", np.dot(b.T,np.array([0,-1,2])))


# In[ ]:




