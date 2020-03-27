#!/usr/bin/env python
# coding: utf-8

# In[68]:


import numpy as np
print("1-a:",np.ones(5))
print("1-b:",np.zeros(5))
print("1-c:",np.full(5,5))
print("1-d:",np.arange(1,6,1))
print("1-e:",np.arange(1,10,2))
print("1-f:",np.array([1,5,2,3,9]))


# In[69]:


import numpy as np
print("2-a:",np.array([1,2,1,5,4])+np.array([1,2,3,4,5]))
print("2-b:",np.arange(1,6,1)+np.array([5,4,3,2,1]))
print("2-c:",np.full(9,3)-np.ones(9))
print("2-d:",np.array([4,5,6])-np.array([3,2,1]))
print("2-e:",2*np.ones(4))
print("2-f:",3*np.array([0,4,2,3]))
print("2-g:",(1/2)*np.arange(2,11,2))


# In[66]:


def dot(a,b):
    return sum(a_i * b_i for a_i, b_i in zip(a,b))
print("3-a:",dot([1,2,3],[9,8,7]))

import numpy as np
a=np.array([1,2,3])
b=np.array([9,8,7])
print("3-b:", np.dot(a,b))


# In[73]:


import numpy as np
def vec_size(a):
    return (sum(a**2))**(1/2)
c=np.array([6,2,4])
print ("4:",vec_size(c))


# In[74]:


import numpy as np
a_x=np.array([1,0,0])
a_y=np.array([0,1,0])
a_z=np.array([0,0,1])
print("5-a:",np.dot(a_x,a_y),np.dot(a_x,a_z),np.dot(a_y,a_z),np.dot(a_x,a_x))


# In[75]:


import numpy as np
b_x=np.array([-2,1,4])
b_y=np.array([1,2,0])
b_z=np.array([2,-1,1.25])
print("5-b:",np.dot(b_x,b_y),np.dot(b_x,b_z),np.dot(b_y,b_z),np.dot(b_x,b_x))


# In[76]:


import numpy as np
b_x=np.array([-2,1,4])
b_y=np.array([1,2,0])
b_z=np.array([2,-1,1.25])
r=np.array([6,4,2])
X=np.dot(b_x,r)/sum(np.square(b_x))
Y=np.dot(b_y,r)/sum(np.square(b_y))
Z=np.dot(b_z,r)/sum(np.square(b_z))
print("5-c:",np.array([X,Y,Z]))


# In[77]:


import numpy as np
import math
b_x=np.array([-2,1,4])
b_y=np.array([1,2,0])
b_z=np.array([2,-1,1.25])
r=np.array([1,0,0])
X=np.dot(b_x,r)/sum(np.square(b_x))
Y=np.dot(b_y,r)/sum(np.square(b_y))
Z=np.dot(b_z,r)/sum(np.square(b_z))
X=round(X,2)
Y=round(Y,2)
Z=round(Z,2)
print("5-d:",np.array([X,Y,Z]))


# In[78]:


import numpy as np
import math
b_x=np.array([-2,1,4])
b_y=np.array([1,2,0])
b_z=np.array([2,-1,1.25])
r=np.array([2,2,2])
X=np.dot(b_x,r)/sum(np.square(b_x))
Y=np.dot(b_y,r)/sum(np.square(b_y))
Z=np.dot(b_z,r)/sum(np.square(b_z))
X=round(X,2)
Y=round(Y,2)
Z=round(Z,2)
print("5-e:",np.array([X,Y,Z]))


# In[79]:


import numpy as np
a=np.array([[1,0,0],
           [0,1,0],
           [0,0,1]])
b=np.array([[-2,1,4],
           [1,2,0],
            [2,-1,1.25]])
r=np.array([1,2,3])
A=np.linalg.inv(a)
R=np.dot(A,b)
print("5-f:",np.dot(r,R))


# In[80]:


import numpy as np
a=np.array([[1,0,0],
           [0,1,0],
           [0,0,1]])
b=np.array([[-2,1,4],
           [1,2,0],
            [2,-1,1.25]])
r=np.array([4,1,7])
A=np.linalg.inv(a)
R=np.dot(A,b)
print("5-g:",np.dot(r,R))


# In[81]:


import numpy as np
a=np.array([[1,0,0],
           [0,1,0],
           [0,0,1]])
b=np.array([[-2,1,4],
           [1,2,0],
            [2,-1,1.25]])
r=np.array([0,-1,2])
A=np.linalg.inv(a)
R=np.dot(A,b)
print("5-h:",np.dot(r,R))


# In[ ]:




