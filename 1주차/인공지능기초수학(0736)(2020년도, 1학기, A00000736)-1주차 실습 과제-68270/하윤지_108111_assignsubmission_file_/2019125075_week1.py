#!/usr/bin/env python
# coding: utf-8

# In[70]:


import numpy as np
a=[1,5,2,3,9]
print('1-a:',np.ones(5))
print('1-b:',np.zeros(5))
print('1-c:',np.full((5),5))
print('1-d:',np.arange(1,6))
print('1-e:',np.arange(1,10,2))
print('1-f:',np.array(a))


# In[23]:


import numpy as np
a=np.array([1,2,1,5,4])
b=np.array([1,2,3,4,5])
c=np.array([5,4,3,2,1])
d=np.full((9),3)
e=np.full((9),1)
f=np.array([4,5,6])
g=np.array([3,2,1])
h=np.array([1,1,1,1])
i=np.array([0,4,2,3])
j=np.array([2,4,6,8,10])
print('2-a:',a+b)
print('2-b:',b+c)
print('2-c:',d-e)
print('2-d:',f-g)
print('2-e:',2*h)
print('2-f:',3*i)
print('2-g:',1/2*j)


# In[33]:


a=[1,2,3]
b=[9,8,7]
print('3-a:',a[0]*b[0]+a[1]*b[1]+a[2]*b[2])


# In[32]:


import numpy as np
a=[1,2,3]
b=[9,8,7]
u=np.array(a)
v=np.array(b)
w=np.dot(u,v)
print('3-b:',w)


# In[69]:


c=[6,2,4]
a=c[0]**2+c[1]**2+c[2]**2
b=a**0.5
print('4:',b)


# In[68]:


import numpy as np
ax=np.array([1,0,0])
ay=np.array([0,1,0])
az=np.array([0,0,1])
bx=np.array([-2,1,4])
by=np.array([1,2,0])
bz=np.array([2,-1,5/4])

vc=6*ax+4*ay+2*az
a1=(vc@bx)/(bx[0]**2+bx[1]**2+bx[2]**2)
a2=(vc@by)/(by[0]**2+by[1]**2+by[2]**2)
a3=(vc@bz)/(bz[0]**2+bz[1]**2+bz[2]**2)
ansc=np.array([a1,a2,a3])

vd=1*ax+0*ay+0*az
b1=(vd@bx)/(bx[0]**2+bx[1]**2+bx[2]**2)
b2=(vd@by)/(by[0]**2+by[1]**2+by[2]**2)
b3=(vd@bz)/(bz[0]**2+bz[1]**2+bz[2]**2)
ansd=np.array([round(b1,2),b2,round(b3,2)])

ve=2*ax+2*ay+2*az
c1=(ve@bx)/(bx[0]**2+bx[1]**2+bx[2]**2)
c2=(ve@by)/(by[0]**2+by[1]**2+by[2]**2)
c3=(ve@bz)/(bz[0]**2+bz[1]**2+bz[2]**2)
anse=np.array([round(c1,2),c2,round(c3,2)])

vf=1*bx+2*by+3*bz
d1=(vf@ax)/(ax[0]**2+ax[1]**2+ax[2]**2)
d2=(vf@ay)/(ay[0]**2+ay[1]**2+ay[2]**2)
d3=(vf@az)/(az[0]**2+az[1]**2+az[2]**2)
ansf=np.array([d1,d2,d3])

vg=4*bx+1*by+7*bz
e1=(vg@ax)/(ax[0]**2+ax[1]**2+ax[2]**2)
e2=(vg@ay)/(ay[0]**2+ay[1]**2+ay[2]**2)
e3=(vg@az)/(az[0]**2+az[1]**2+az[2]**2)
ansg=np.array([e1,e2,e3])

vh=0*bx+(-1)*by+2*bz
f1=(vh@ax)/(ax[0]**2+ax[1]**2+ax[2]**2)
f2=(vh@ay)/(ay[0]**2+ay[1]**2+ay[2]**2)
f3=(vh@az)/(az[0]**2+az[1]**2+az[2]**2)
ansh=np.array([f1,f2,f3])

print('5-a:',ax@ay,ax@az,ay@az,ax@ax)
print('5-b;',bx@by,bx@bz,by@bz,bx@bx)
print('5-c:',ansc)
print('5-d:',ansd)
print('5-e:',anse)
print('5-f:',ansf)
print('5-g:',ansg)
print('5-h:',ansh)

