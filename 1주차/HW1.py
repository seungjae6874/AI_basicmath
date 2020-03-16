#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1주차 1번 과제


# In[36]:


import numpy as np


# In[38]:


a = np.ones(5,int)
b = np.zeros(5,int)
c = np.full((5),5)
d = np.arange(1,6)
e = np.arange(1,10,2)
f = np.array([1,5,2,3,9])


# In[41]:


print("1-a : ",a)
print("1-b : ",b)
print("1-c : ",c)
print("1-d : ",d)
print("1-e : ",e)
print("1-f : ",f)


# In[ ]:


#1주차 과제 2번


# In[76]:


#2-a 
a = np.array([1,2,1,5,4])
b = np.arange(1,6)
c = np.arange(5,0,-1)
d = np.full((9),3)
e = np.full((9),1)
f = np.arange(4,7)
g = np.arange(3,0,-1)
h = np.ones(4,int)
i = np.array([0,4,2,3],int)
j = np.arange(2,11,2,int)
k = j/2
k = k.astype('uint64')


# In[78]:


print('2-a:',a+b)
print('2-b:',b+c)
print('2-c:',d-e)
print('2-d:',f-g)
print('2-e:',2*h)
print('2-f:',3*i)
print('2-g:',k)


# In[138]:


#1주차 과제3번
a = list(range(1,4))
b = list(range(9,6,-1))
def DP(a,b):
    c = 0
    for i in range(len(a)):
        c += a[i]*b[i]
    return c


# In[140]:


print('3-a:',DP(a,b))


# In[141]:


a = np.arange(1,4)
b = np.arange(9,6,-1)
c= np.dot(a,b)
print('3-b: ',c)


# In[142]:


#1주차 4번 문제


# In[143]:


def vec_size(c):
    return np.size(c)


# In[147]:


c = np.array([6,2,4],int)
print('4: ',vec_size(c))


# In[148]:


#1주차 5번 문제


# In[150]:


a_x = np.array([1,0,0])
a_y = np.array([0,1,0])
a_z = np.array([0,0,1])
b_x = np.array([-2,1,4])
b_y = np.array([1,2,0])
b_z = np.array([2,-1,1.25])
print('5-a: ',np.dot(a_x,a_y),np.dot(a_x,a_z)
      ,np.dot(a_y,a_z),np.dot(a_x,a_x))
print('5-b: ',np.dot(b_x,b_y),np.dot(b_x,b_z)
      ,np.dot(b_y,b_z),np.dot(b_x,b_x))


# In[163]:


def change(x): 
    change_matrix= np.array([[-2,1,4],[1,2,0],[2,-1,1.25]],float)
    return np.matmul(change_matrix,x)
a = np.array([6,4,2],float)
b = np.array([1,0,0],float)
c = np.array([2,2,2],float)
print('5-c: ',change(a))
print('5-d: ',change(b))
print('5-e: ',change(c))


# In[165]:


def btoa(x):
    change_matrix = np.linalg.inv(np.array([[-2,1,4],[1,2,0],[2,-1,1.25]],float))
    return np.matmul(change_matrix,x)
d = np.array([1,2,3],float)
e = np.array([4,1,7],float)
f = np.array([0,-1,2],float)
print('5-f: ',change(d))
print('5-g: ',change(e))
print('5-h: ',change(f))


# In[ ]:




