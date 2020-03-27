#!/usr/bin/env python
# coding: utf-8

# In[54]:


import numpy as np

#1번
array11 = np.zeros(5)
array12 = np.ones(5)
array13 = np.full(5,5)
array14 = np.arange(1,6,1)
array15 = np.arange(1,10,2)
array16 = np.array([1,5,2,3,9])


print('1-a :', array11)
print('1-b :', array12)
print('1-c :', array13)
print('1-d :', array14)
print('1-e :', array15)
print('1-f :', array16,'\n\n')

#2번
array211 = np.array([1,2,1,5,4])
array212 = np.array([1,2,3,4,5])

array221 = np.array([1,2,3,4,5])
array222 = np.array([5,4,3,2,1])

array231 = np.array([3,3,3,3,3,3,3,3,3])
array232 = np.array([1,1,1,1,1,1,1,1,1])

array241 = np.array([4,5,6])
array242 = np.array([3,2,1])

array25 = np.array([1,1,1,1])

array26 = np.array([0,4,2,3])

array27 = np.array([2,4,6,8,10])


print('2-a :' ,array211+array212)
print('2-b :' ,array221+array222)
print('2-c :' ,array231-array232)
print('2-d :' ,array241-array242)
print('2-e :' ,2*array25)
print('2-f :' ,3*array26)
print('2-g :' ,1/2*array27,'\n\n')

#3-a
a = [1,2,3]
b = [9,8,7]
c = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print('3-a :',c)

#3-b
a = np.array([1,2,3])
b = np.array([9,8,7])
c = np.dot(a,b)
print('3-b :',c,'\n\n')

#4
c = np.array([6,2,4])

def vec_size(c):
    a = (c[0]**2+c[1]**2+c[2]**2)**0.5
    return a

b = vec_size(c)
print('4 : ',b,'\n\n')


#5
ax = np.array([1,0,0])
ay = np.array([0,1,0])
az = np.array([0,0,1])

bx = np.array([-2,1,4])
by = np.array([1,2,0])
bz = np.array([2,-1,1.25])

#5-a
axy = ax@ay
axz = ax@az
ayz = ay@az
axx = ax@ax

#5-b
bxy = bx@by
bxz = bx@bz
byz = by@bz
bxx = bx@bx

#5-c
a3 = 6*ax + 4*ay + 2*az
a3x = (a3@bx) / (bx[0]**2 + bx[1]**2 + bx[2]**2)
a3y = (a3@by) / (by[0]**2 + by[1]**2 + by[2]**2)
a3z = (a3@bz) / (bz[0]**2 + bz[1]**2 + bz[2]**2)
ac = np.array([a3x, a3y, a3z])

#5-d
a4 = 1*ax + 0*ay + 0*az
a4x = (a4@bx) / (bx[0]**2 + bx[1]**2 + bx[2]**2)
a4y = (a4@by) / (by[0]**2 + by[1]**2 + by[2]**2)
a4z = (a4@bz) / (bz[0]**2 + bz[1]**2 + bz[2]**2)
adx = round(a4x,2)
ady = round(a4y,2)
adz = round(a4z,2)
ad = np.array([adx, ady, adz])

#5-e
a5 = 2*ax + 2*ay + 2*az
a5x = (a5@bx) / (bx[0]**2 + bx[1]**2 + bx[2]**2)
a5y = (a5@by) / (by[0]**2 + by[1]**2 + by[2]**2)
a5z = (a5@bz) / (bz[0]**2 + bz[1]**2 + bz[2]**2)
aex = round(a5x,2)
aey = round(a5y,2)
aez = round(a5z,2)
ae = np.array([aex, aey, aez])

#5-f
b6 = 1*bx + 2*by + 3*bz
b6x = (b6@ax) / (ax[0]**2 + ax[1]**2 + ax[2]**2)
b6y = (b6@ay) / (ay[0]**2 + ay[1]**2 + ay[2]**2)
b6z = (b6@az) / (az[0]**2 + az[1]**2 + az[2]**2)
bfx = round(b6x,2)
bfy = round(b6y,2)
bfz = round(b6z,2)
bf = np.array([bfx, bfy, bfz])

#5-g
b7 = 4*bx + 1*by + 7*bz
b7x = (b7@ax) / (ax[0]**2 + ax[1]**2 + ax[2]**2)
b7y = (b7@ay) / (ay[0]**2 + ay[1]**2 + ay[2]**2)
b7z = (b7@az) / (az[0]**2 + az[1]**2 + az[2]**2)
bgx = round(b7x,2)
bgy = round(b7y,2)
bgz = round(b7z,2)
bg = np.array([bgx, bgy, bgz])

#5-h
b8 = 0*bx + (-1)*by + 2*bz
b8x = (b8@ax) / (ax[0]**2 + ax[1]**2 + ax[2]**2)
b8y = (b8@ay) / (ay[0]**2 + ay[1]**2 + ay[2]**2)
b8z = (b8@az) / (az[0]**2 + az[1]**2 + az[2]**2)
bhx = round(b8x,2)
bhy = round(b8y,2)
bhz = round(b8z,2)
bh = np.array([bhx, bhy, bhz])


print('5-a :', axy, axz, ayz, axx)
print('5-b :', bxy, bxz, byz, bxx)
print('5-c :',ac)
print('5-d :',ad)
print('5-e :',ae)
print('5-f :',bf)
print('5-g :',bg)
print('5-h :',bh)

