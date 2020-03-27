#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a = np.ones(5)
b = np.zeros(5)
c = np.full(5, 5)
d = np.arange(1, 6)
e = np.arange(1, 11, 2)
f = np.array([1, 5, 2, 3, 9])
print("1-a: ",a)
print("1-b: ",b)
print("1-c: ",c)
print("1-d: ",d)
print("1-e: ",e)
print("1-f: ",f)


# In[2]:


import numpy as np
list1 = [1, 2, 1, 5, 4]
lsit2 = [0, 4, 2, 3]
a = np.array(list1)
b = np.arange(1, 6)
c = np.arange(5, 0, -1)
d = np.full(9, 3)
e = np.full(9, 1)
f = np.arange(4, 7)
g = np.arange(3, 0, -1)
h = np.full(4, 1)
i = np.array(lsit2)
j = np.arange(2, 12, 2)
print("2-a:", a+b)
print("2-b:", b+c)
print("2-c:", d-e)
print("2-d:", f-g)
print("2-e:", 2*h)
print("2-f:", 3*i)
print("2-g:", 1/2*j)


# In[3]:


a=[]
b=[]
for i in range(0,3):
    t=int(input('a벡터값을 입력하세요'))
    a.append(t)
for e in range(0,3):
    k=int(input('b벡터값을 입력하세요'))
    b.append(k)
def dp(c, d):
    return sum(x * y for x, y in zip(c, d))
print("3-a:", dp(a, b)) 
import numpy as np
a = np.array([1, 2, 3])
b = np.array([9, 8, 7])
s = np.sum(a*b)
print("3-b:", s)


# In[4]:


import numpy as np
c = np.array([6, 2, 4])
def vec_size(b):
    return sum(x * y for x, y in zip(b, b))**0.5
d = vec_size(c)
print("4:", d)


# In[5]:


import numpy as np
a = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
b = np.array([[-2, 1, 4], [1, 2, 0], [2, -1, 1.25]])
c = np.array([6, 4, 2])
d = np.array([1, 0, 0])
e = np.array([2, 2, 2])
f = np.array([1, 2, 3])
g = np.array([4, 1, 7])
h = np.array([0, -1, 2])
print("5-a:", np.sum(a[(0,)]*a[(1,)]), np.sum(a[(0,)]*a[(2,)]), np.sum(a[(1,)]*a[(2,)]), np.sum(a[(0,)]*a[(0,)]))
print("5-a:", int(np.sum(b[(0,)]*b[(1,)])), np.sum(b[(0,)]*b[(2,)]), np.sum(b[(1,)]*b[(2,)]), int(np.sum(b[(0,)]*b[(0,)])))
print("5-c:", np.round_(np.vstack([np.linalg.solve(np.vstack([b]).T, np.dot(np.stack(a).T,np.vstack([c]).T))]).T, 2))
print("5-d:", np.round_(np.vstack([np.linalg.solve(np.vstack([b]).T, np.dot(np.stack(a).T,np.vstack([d]).T))]).T, 2))
print("5-e:", np.round_(np.vstack([np.linalg.solve(np.vstack([b]).T, np.dot(np.stack(a).T,np.vstack([e]).T))]).T, 2))
print("5-f:", np.round_(np.vstack([np.linalg.solve(np.vstack([a]).T, np.dot(np.stack(b).T,np.vstack([f]).T))]).T, 2))
print("5-g:", np.round_(np.vstack([np.linalg.solve(np.vstack([a]).T, np.dot(np.stack(b).T,np.vstack([g]).T))]).T, 2))
print("5-h:", np.round_(np.vstack([np.linalg.solve(np.vstack([a]).T, np.dot(np.stack(b).T,np.vstack([h]).T))]).T, 2))


# In[ ]:




