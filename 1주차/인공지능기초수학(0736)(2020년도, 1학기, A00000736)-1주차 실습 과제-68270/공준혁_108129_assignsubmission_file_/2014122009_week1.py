#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import math

#1번문제
vec_data = [1,5,2,3,9]

arr1a = np.ones(5) #1-a
arr1b = np.zeros(5) #1-b
arr1c = np.full(5,5) #1-c
arr1d = np.arange(1,6) #1-d
arr1e = np.arange(1,10,2) #1-e
arr1f = np.array([1,5,2,3,9]) #1-f

print('1-a:',arr1a)
print('1-b:',arr1b)
print('1-c:',arr1c)
print('1-d:',arr1d)
print('1-e:',arr1e)
print('1-f:',arr1f)

print('\n')

#2번문제
arr2a = np.array([1,2,1,5,4])+np.array([1,2,3,4,5]) #2-a
arr2b = np.arange(1,6)+np.arange(5,0,-1) #2-b
arr2c = np.full(9,3)-np.ones(9) #2-c
arr2d = np.arange(4,7)-np.arange(3,0,-1) #2-d
arr2e = 2*np.ones(4) #2-e
arr2f = 3*np.array([0,4,2,3]) #2-f
arr2g = (1/2)*np.arange(2,11,2) #2-g

print('2-a:',arr2a)
print('2-b:',arr2b)
print('2-c:',arr2c)
print('2-d:',arr2d)
print('2-e:',arr2e)
print('2-f:',arr2f)
print('2-g:',arr2g)

print('\n')

#3번문제

#3-a
vec_a = [1,2,3]
vec_b = [9,8,7]
sum = 0

def DP(va,vb):
    return va[0]*vb[0]+va[1]*vb[1]+va[2]*vb[2]

print('3-a:',DP(vec_a,vec_b))

#3-b
np_a = np.arange(1,4)
np_b = np.arange(9,6,-1)
dotP = np_a*np_b
npsum = np.sum(dotP)
                                  
print('3-b:',npsum)

print('\n')

#4번문제

c = np.array([6,2,4])

def vec_size(vc):
    return math.sqrt(vc[0]**2+vc[1]**2+vc[2]**2)

print('4:',vec_size(c))

print('\n')

#5번문제

ax = np.array([1,0,0])
ay = np.array([0,1,0])
az = np.array([0,0,1])

bx = np.array([-2,1,4])
by = np.array([1,2,0])
bz = np.array([2,-1,1.25])

r_a = np.array([6,4,2]) #5-c

axay = np.dot(ax,ay)
axaz = np.dot(ax,az)
ayaz = np.dot(ay,az)
axax = np.dot(ax,ax)

bxby = np.dot(bx,by)
bxbz = np.dot(bx,bz)
bybz = np.dot(by,bz)
bxbx = np.dot(bx,bx)

print('5-a:',axay,axaz,ayaz,axax)
print('5-b:',bxby,bxbz,bybz,bxbx)

arr_a = np.array([ax,ay,az])
arr_b = np.array([bx,by,bz])

r2_ax = axax
r2_ay = ay[0]*ay[0]+ay[1]*ay[1]+ay[2]*ay[2]
r2_az = az[0]*az[0]+az[1]*az[1]+az[2]*az[2]

r2_bx = bxbx
r2_by = by[0]*by[0]+by[1]*by[1]+by[2]*by[2]
r2_bz = bz[0]*bz[0]+bz[1]*bz[1]+bz[2]*bz[2]

def coor_atob(ravec): #5-c,d,e
    result = np.array([np.dot(bx,ravec)/r2_bx,
                   np.dot(by,ravec)/r2_by,
                   np.dot(bz,ravec)/r2_bz])
    return result

def coor_btoa(ravec): #5-f,g,h
    result = np.array([np.dot(ravec,arr_b[:,0])/r2_ax,
                   np.dot(ravec,arr_b[:,1])/r2_ay,
                   np.dot(ravec,arr_b[:,2])/r2_az])
    return result

arr5c = coor_atob(r_a)
arr5d = coor_atob(np.array([1,0,0]))
arr5e = coor_atob(np.array([2,2,2]))

arr5f = coor_btoa(np.array([1,2,3]))
arr5g = coor_btoa(np.array([4,1,7]))
arr5h = coor_btoa(np.array([0,-1,2]))

print('5-c:',arr5c)
print('5-d:',arr5d)
print('5-e:',arr5e)

print('5-f:',arr5f)
print('5-g:',arr5g)
print('5-h:',arr5h)


# In[ ]:




