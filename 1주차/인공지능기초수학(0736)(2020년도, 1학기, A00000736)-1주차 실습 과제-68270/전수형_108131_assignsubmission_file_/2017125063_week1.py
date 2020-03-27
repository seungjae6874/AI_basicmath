#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
arr=np.ones(5)
print('1-a: {}'.format(arr))


# In[28]:


import numpy as np
arr=np.zeros(5)
print('1-b: {}'.format(arr))


# In[108]:


import numpy as np
ary=np.full((1,5),5)
print('1-c: {}'.format(ary))


# In[47]:


import numpy as np
arr=np.arange(1,6)
print('1-d: {}'.format(arr))


# In[49]:


import numpy as np
ary=([1,3,5,7,9])
arr=np.array(ary)
print('1-e: {}'.format(arr))


# In[50]:


import numpy as np
ary=([1,5,2,3,9])
arr=np.array(ary)
print('1-f: {}'.format(arr))


# In[93]:


import numpy as np
ary=([1,2,1,5,4])
arr=([1,2,3,4,5])
ary2=np.array(ary)
arr2=np.array(arr)
a=ary2+arr2
print('2-a: {}'.format(a))


# In[95]:


import numpy as np
ary=([1,2,3,4,5])
arr=([5,4,3,2,1])
ary2=np.array(ary)
arr2=np.array(arr)
a=ary2+arr2
print('2-b: {}'.format(a))


# In[119]:


import numpy as np
ary=[3,3,3,3,3,3,3,3,3]
arr=[1,1,1,1,1,1,1,1,1]
a=np.array(ary2)-np.array(arr2)
b=1/1*a
print('2-c: {}'.format(b))


# In[115]:


import numpy as np
ary=([4,5,6])
arr=([3,2,1])
a=np.array(ary)-np.array(arr)
print('2-d: {}'.format(a))


# In[121]:


import numpy as np
ary=([1,1,1,1])
a=np.array(ary)
b=2*a
c=1/1*b
print('2-e: {}'.format(c))


# In[1]:


import numpy as np
ary=([0,4,2,3])
a=np.array(ary)
b=3*a
print('2-g: {}'.format(b))


# In[2]:


import numpy as np
ary=([2,4,6,8,10])
a=np.array(ary)
b=1/2*a
print('2-g: {}'.format(b))


# In[79]:


def DP():
    sum=0
    list_1=[]
    list_2=[]
    count=0
    while(count<3):
        a=input("vector a 3개 입력: ")
        b=list_1.append(a)
        count=count+1
    count=0
    while(count<3):
        a=input("vector b 3개 입력: ")
        b=list_2.append(a)
        count=count+1;
    count=0
    while(count<3):
        sum=sum+(int(list_1[count])*int(list_2[count]))
        count=count+1
    print("3-a: ",sum)
    
DP()


# In[11]:


import numpy as np
arr=([1,2,3])
ary=([9,8,7])
arr2=np.array(arr)
ary2=np.array(ary)
ace=ary2*arr2
sum=np.sum(ace)
print("3-b: ",sum)


# In[12]:


import numpy as np 
index=0
list_1=0
def vec_size(a):
    global index
    global list_1
    list_1=list[0]*list[0]+list[1]*list[1]+list[2]*list[2]
    return list_1**0.5

index=0
list_1=0
list=([6,2,4])
vec_size(list)
e=vec_size(list)
print("4: ",e)


# In[1]:


import numpy as np
ax=([1,0,0])
ay=([0,1,0])
az=([0,0,1])
ax2=np.array(ax)
ay2=np.array(ay)
az2=np.array(az)
print("5-a: ",np.sum(ax2*ay2),np.sum(ax2*az2),np.sum(ay2*az2),np.sum(ax2*ax2))


# In[16]:


import numpy as np
bx=([-2,1,4])
by=([1,2,0])
bz=([2,-1,1.25])
bx2=np.array(bx)
by2=np.array(by)
bz2=np.array(bz)
print("5-b: ",np.sum(bx2*by2),np.sum(bx2*bz2),np.sum(by2*bz2),np.sum(bx2*bx2))


# In[67]:


import numpy as np
np.set_printoptions(formatter={'float_kind':lambda x:"{0:0.2f}".format(x)})
a=np.array([6,4,2])
ars=np.array([[-2,1,4],[1,2,0],[2,-1,1.25]])
ars_inv=np.linalg.inv(ars)
ars2=np.array(ars_inv)
b=np.dot(a,ars2)
print("5-c: ",b)


# In[69]:


import numpy as np
np.set_printoptions(formatter={'float_kind':lambda x:"{0:0.2f}".format(x)})
a=np.array([1,0,0])
ars=np.array([[-2,1,4],[1,2,0],[2,-1,1.25]])
ars_inv=np.linalg.inv(ars)
ars2=np.array(ars_inv)
b=np.dot(a,ars2)
print("5-d: ",b)


# In[70]:


import numpy as np
np.set_printoptions(formatter={'float_kind':lambda x:"{0:0.2f}".format(x)})
a=np.array([2,2,2])
ars=np.array([[-2,1,4],[1,2,0],[2,-1,1.25]])
ars_inv=np.linalg.inv(ars)
ars2=np.array(ars_inv)
b=np.dot(a,ars2)
print("5-e: ",b)


# In[75]:


import numpy as np
np.set_printoptions(formatter={'float_kind':lambda x:"{0:0.2f}".format(x)})
a=np.array([1,2,3])
ars=np.array([[-2,1,4],[1,2,0],[2,-1,1.25]])
c=np.dot(a,ars)

print("5-f: ",c)


# In[76]:


import numpy as np
np.set_printoptions(formatter={'float_kind':lambda x:"{0:0.2f}".format(x)})
a=np.array([4,1,7])
ars=np.array([[-2,1,4],[1,2,0],[2,-1,1.25]])
c=np.dot(a,ars)

print("5-g: ",c)


# In[1]:


import numpy as np
np.set_printoptions(formatter={'float_kind':lambda x:"{0:0.2f}".format(x)})
a=np.array([0,-1,2])
ars=np.array([[-2,1,4],[1,2,0],[2,-1,1.25]])
c=np.dot(a,ars)

print("5-h: ",c)

