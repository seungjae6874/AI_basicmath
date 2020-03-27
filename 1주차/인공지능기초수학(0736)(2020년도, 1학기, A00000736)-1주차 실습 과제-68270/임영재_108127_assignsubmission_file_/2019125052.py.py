#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
 
a= np.ones(5)
print(a)


# In[11]:


import numpy as np

a= np.zeros(5)
print(a)


# In[12]:


import numpy as np

a= np.full((5),5)
print(a)


# In[13]:


import numpy as np

a= np.arange(1,6)
print(a)


# In[14]:


import numpy as np

list1=[1,3,5,7,9]
a= np.array(list1)
print(a)


# In[15]:


import numpy as np

list1=[1,5,3,4,9]
a= np.array(list1)
print(a)


# In[16]:


import numpy as np
 
a = np.array([1,2,1,5,4])
b = np.array([1,2,3,4,5])
 
c = np.add(a, b)
print(c)


# In[17]:


import numpy as np
 
a = np.array([1,2,3,4,5])
b = np.array([5,4,3,2,1])
 
c = np.add(a, b)
print(c)


# In[18]:


import numpy as np
 
a = 3*np.ones(9)
b = np.ones(9)
 
c = np.subtract(a, b)
print(c)


# In[19]:


import numpy as np
 
a = np.array([4,5,6])
b = np.array([3,2,1])
 
c = np.subtract(a, b)
print(c)


# In[20]:


import numpy as np
 
a = 2*np.ones(4)

print(a)


# In[21]:


import numpy as np
 
a = 3*np.array([0,4,2,3])

print(a)


# In[22]:


import numpy as np
 
a = np.array([2,4,6,8,10])/2

print(a)


# In[23]:


def DP(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

a=[]
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
b=[]
b.append(int(input()))
b.append(int(input()))
b.append(int(input()))

print(DP(a,b))


# In[24]:


import numpy as np
def DP(a,b):
    c = np.multiply(a, b)
    a = np.array(c)
 
    s = np.sum(a)
    return s
a=[]
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
b=[]
b.append(int(input()))
b.append(int(input()))
b.append(int(input()))
print(DP(a,b))


# In[9]:


import math
import numpy as np
a=[]
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
c=np.array(a)
d=np.multiply(c, c)
def vec_size(d):
    return math.sqrt(np.sum(d)) 
print(vec_size(d))


# In[ ]:




