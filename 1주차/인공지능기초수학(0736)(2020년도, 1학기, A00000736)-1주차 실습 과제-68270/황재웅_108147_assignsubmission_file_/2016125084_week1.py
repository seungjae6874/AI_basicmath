#!/usr/bin/env python
# coding: utf-8

# In[95]:


import numpy as np


# In[114]:


a=np.ones(5)
b=np.zeros(5)
c=np.full(5,5)
d=np.arange(1,6,1)
e=np.arange(1,10,2)
f=np.array([1,5,2,3,9])

print ("1-a:",a)
print ("1-b:",b)
print ("1-c:",c)
print ("1-d:",d)
print ("1-e:",e)
print ("1-f:",f)
print("\n\n")

a1=(1,2,1,5,4)
a2=(1,2,3,4,5)#arange
a=np.array(a1)+np.array(a2)

b1=(1,2,3,4,5)#arange
b2=(5,4,3,2,1)#arange
b=np.array(b1)+np.array(b2)

c1=np.full(9,3)
c2=np.ones(9)
c=c1-c2

d1=(4,5,6)#arange
d2=(3,2,1)#arange
d=np.array(d1)-np.array(d2)

e1=np.ones(4)
e=e1*2

f1=(0,4,2,3)
f=np.array(f1)*3

g1=(2,4,6,8,10)#arange
g=np.array(g1)/2

print ("1-a:",a)
print ("1-b:",b)
print ("1-c:",c)
print ("1-d:",d)
print ("1-e:",e)
print ("1-f:",f)
print ("1-g:",g)
print("\n\n")

a=[1,2,3]
b=[9,8,7]


def DP(list1,list2):
    result=0
    for i in range(3):
        result+=list1[i]*list2[i]
    return result

c=DP(a,b)
print ("3-a:",c)

a=np.arange(1,4,1)
b=np.arange(9,6,-1)
c=np.sum(a*b)
print("3-b:",c)
print("\n\n")

c=(6,2,4)
c=np.array(c)

def vec_size(vec):
    re=(vec[0]**2+vec[1]**2+vec[2]**2)**0.5
    return re #혹은 np.linalg.norm(vec)


result=vec_size(c)
print ("4:",result)
print("\n\n")

ax=np.array([1,0,0])
ay=np.array([0,1,0])
az=np.array([0,0,1])

bx=np.array([-2,1,4])
by=np.array([1,2,0])
bz=np.array([2,-1,1.25])

a=np.array([ax,ay,az])
b=np.array([bx,by,bz])

xca=np.array([6,4,2])
xda=np.array([1,0,0])
xea=np.array([2,2,2])
xfb=np.array([1,2,3])
xgb=np.array([4,1,7])
xhb=np.array([0,-1,2])


def basis_trans(basis,vec):
    return basis@vec/(np.linalg.norm(basis)**2)

vecF=np.array(bx*xfb[0]+by*xfb[1]+bz*xfb[2])
vecG=np.array(bx*xgb[0]+by*xgb[1]+bz*xgb[2])
vecH=np.array(bx*xhb[0]+by*xhb[1]+bz*xhb[2])


print("5-a:",ax@ay,ax@az,ay@az,ax@ax)
print("5-b:",bx@by,bx@bz,by@bz,bx@bx)
print("5-c:",format(basis_trans(bx,xca),".2f"),format(basis_trans(by,xca),".2f"),format(basis_trans(bz,xca),".2f"))
print("5-d:",format(basis_trans(bx,xda),".2f"),format(basis_trans(by,xda),".2f"),format(basis_trans(bz,xda),".2f"))
print("5-e:",format(basis_trans(bx,xea),".2f"),format(basis_trans(by,xea),".2f"),format(basis_trans(bz,xea),".2f"))
print("5-f:",format(basis_trans(ax,vecF),".2f"),format(basis_trans(ay,vecF),".2f"),format(basis_trans(az,vecF),".2f"))
print("5-g:",format(basis_trans(ax,vecG),".2f"),format(basis_trans(ay,vecG),".2f"),format(basis_trans(az,vecG),".2f"))
print("5-h:",format(basis_trans(ax,vecH),".2f"),format(basis_trans(ay,vecH),".2f"),format(basis_trans(az,vecH),".2f"))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




