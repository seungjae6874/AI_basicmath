#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[6]:


a1 = np.ones(5)
print("1-a:", a1)


# In[7]:


b1 = np.zeros(5)
print("1-b:", b1)


# In[8]:


c1 = np.full(5,5)
print("1-c:", c1)


# In[13]:


d1 = np.arange(1,6)
print("1-d:", d1)


# In[14]:


e1 = np.arange(1,10,2)
print("1-e:", e1)


# In[16]:


f1 = (1, 5, 2, 3, 9)
ff = np.array(f1)
print("1-f:", ff)


# In[18]:


print("\n\n")


# In[19]:


a21 = (1, 2, 1, 5, 4)
a22 = (1, 2, 3, 4, 5)
aa21 = np.array(a21)
aa22 = np.array(a22)
print("2-a:", aa21 + aa22)


# In[21]:


b21 = (1, 2, 3, 4, 5)
b22 = (5, 4, 3, 2, 1)
bb21 = np.array(b21)
bb22 = np.array(b22)
print("2-b:", bb21 + bb22)


# In[29]:


c21 = (3, 3, 3, 3, 3, 3, 3, 3, 3)
cc21 = np.array(c21)
c22 = np.ones(9)
print("2-c:", cc21 - c22)


# In[30]:


d21 = (4, 5, 6)
d22 = (3, 2, 1)
dd21 = np.array(d21)
dd22 = np.array(d22)
print("2-d:", dd21 - dd22)


# In[31]:


e21 = np.ones(4)
print("2-e:", 2 * e21)


# In[32]:


f21 = (0, 4, 2, 3)
ff21 = np.array(f21)
print("2-f:", 3 * ff21)


# In[33]:


g21 = (2, 4, 6, 8, 10)
gg21 = np.array(g21)
print("2-g:", 1/2 * gg21)


# In[34]:


print("\n\n")


# In[37]:


a31 = [1, 2, 3]
a32 = [9, 8, 7]

def DP(x, y):
    return x[0]*y[0] + x[1]*y[1] + x[2]*y[2]

res3 = DP(a31, a32)
print("3-a:", res3)


# In[39]:


b31 = (1, 2, 3)
b32 = (9, 8, 7)
bb31 = np.array(b31)
bb32 = np.array(b32)
bb33 = np.sum(bb31*bb32)
print("3-b:", bb33)


# In[40]:


print("\n\n")


# In[44]:


c4 = (6, 4, 2)
cc41 = np.array(c4)

def vec_size(z):
    return np.sum(z*z)**0.5

cc42 = vec_size(cc41)
print("4:", cc42)


# In[45]:


print("\n\n")


# In[13]:


ax1 = (1, 0, 0)
ay1 = (0, 1, 0)
az1 = (0, 0, 1)
bx1 = (-2, 1, 4)
by1 = (1, 2, 0)
bz1 = (2, -1, 1.25)

ax = np.array(ax1)
ay = np.array(ay1)
az = np.array(az1)
bx = np.array(bx1)
by = np.array(by1)
bz = np.array(bz1)

axy = np.sum(ax*ay)
axz = np.sum(ax*az)
ayz = np.sum(ay*az)
axx = np.sum(ax*ax)
print("5-a:", axy, axz, ayz, axx)

bxy = np.sum(bx*by)
bxz = np.sum(bx*bz)
byz = np.sum(by*bz)
bxx = np.sum(bx*bx)
print("5-b:", bxy, bxz, byz, bxx)

def a_to_b(z, q, w, e):
    return (np.sum(z*q)/np.sum(q*q), np.sum(z*w)/np.sum(w*w), np.sum(z*e)/np.sum(e*e))

ra1 = (6, 4, 2)
ra = np.array(ra1)
c5 = a_to_b(ra, bx, by, bz)
cc51 = np.array(c5)
cc5 = np.round(cc51, 2)
print("5-c:", cc5)

d51 = (1, 0, 0)
d5 = np.array(d51)
dd51 = a_to_b(d5, bx, by, bz)
dd51 = np.array(dd51)
dd5 = np.round(dd51, 2)
print("5-d:", dd5)

e51 = (2, 2, 2)
e5 = np.array(e51)
ee51 = a_to_b(e5, bx, by, bz)
ee52 = np.array(ee51)
ee5 = np.round(ee52, 2)
print("5-e:", ee5)

def b_to_b(z, q, w, e):
    bx11 = q*z[0]
    by11 = w*z[1]
    bz11 = e*z[2]
    bx1 = bx11[0] + by11[0] + bz11[0]
    by1 = bx11[1] + by11[1] + bz11[1]
    bz1 = bx11[2] + by11[2] + bz11[2]
    return (bx1,by1,bz1)

f51 = (1, 2, 3)
f5 = np.array(f51)
ff51 = b_to_b(f5, bx, by, bz)
ff5 = np.array(ff51)
fff51 = a_to_b(ff5, ax, ay, az)
fff52 = np.array(fff51)
ff5 = np.round(fff52, 2)
print("5-f:", fff5)


g51 = (4, 1, 7)
g5 = np.array(g51)
gg51 = b_to_b(g5, bx, by, bz)
gg5 = np.array(gg51)
ggg51 = a_to_b(gg5, ax, ay, az)
ggg52 = np.array(ggg51)
ggg5 = np.round(ggg52, 2)
print("5-g:", ggg5)

h51 = (0, -1, 2)
h5 = np.array(h51)
hh51 = b_to_b(h5, bx, by, bz)
hh5 = np.array(hh51)
hhh51 = a_to_b(hh5, ax, ay, az)
hhh52 = np.array(hhh51)
hhh5 = np.round(hhh52)
print("5-h:", hh5)

