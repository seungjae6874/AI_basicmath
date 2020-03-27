#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
a = np.ones((1,5))
b = np.zeros((1,5))
c = np.full((1,5),5)
d = np.array((1,2,3,4,5))
e = np.arange(1, 10, 2)
f = np.array((1,5,2,3,9))
print("1-a:",a)
print("1-b:",b)
print("1-c:",c)
print("1-d:",d)
print("1-e:",e)
print("1-f:",f)

print('\n')

print("2-a:",np.array((1,2,3,4,5))+np.array((1,2,1,5,4)))
print("2-b:",np.array((1,2,3,4,5))+np.array((5,4,3,2,1)))
print("2-c:",np.array((3.0,3,3,3,3,3,3,3,3))-np.array((1,1,1,1,1,1,1,1,1)))
print("2-d:",np.array((4,5,6))-np.array((3,2,1)))
print("2-e:",2*np.array((1.0,1,1,1)))
print("2-f:",3*np.array((0,4,2,3)))
print("2-g:",1/2*np.array((2.0,4,6,8,10)))

print('\n')

def DP(a,b):
    return np.dot(a,b)

a = (1,2,3)
b = (9,8,7)
print("3-a:",DP(a,b))

c = np.array([1,2,3])
d = np.array([9,8,7])
print("3-b:",sum(c*d))

print('\n')

def vec_size(a,b,c):
    return ((a*a)+(b*b)+(c*c))**0.5
c = np.array((6,2,4))
print("4:", vec_size(6,2,4))

print('\n')

import numpy.linalg as lin

ax = np.array((1,0,0))
ay = np.array((0,1,0))
az = np.array((0,0,1))
r_a = np.array((6,4,2))

bx = np.array((-2,1,4))
by = np.array((1,2,0))
bz = np.array((2,-1,1.25))

#a번
print("5-a)",sum(ax*ay),sum(ax*az),sum(ay*az),sum(ax*ax))
#b번
print("5-b)",sum(bx*by),sum(bx*bz),sum(by*bz),sum(bx*bx))
#c번 
np.set_printoptions(precision=2)
b_all = np.array(((-2,1,4),(1,2,0),(2,-1,1.25)))
p = np.linalg.solve(b_all.T, r_a)
print("5-c)",np.round(p,2))
#d번
np.set_printoptions(precision=2)
q = np.linalg.solve(b_all.T, ax)
print("5-d)",q)
#e번
np.set_printoptions(precision=2)
r = np.linalg.solve(b_all.T, 2*(ax+ay+az))
print("5-e)",r)
#f번
a_all = np.array(((1,0,0),(0,1,0),(0,0,1)))
np.set_printoptions(precision=2)
t = np.linalg.solve(a_all.T, (1,2,3))
print("5-f)",t)
#g번
np.set_printoptions(precision=2)
u = np.linalg.solve(a_all.T, (4,1,7))
print("5-g)", u)
#h번
np.set_printoptions(precision=2)
v = np.linalg.solve(a_all.T, (0,-1,2))
print("5-h)",v)




