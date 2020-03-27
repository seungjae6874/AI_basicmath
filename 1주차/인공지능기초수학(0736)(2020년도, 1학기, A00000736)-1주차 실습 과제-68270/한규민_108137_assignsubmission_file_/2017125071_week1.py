#!/usr/bin/env python
# coding: utf-8

# In[139]:


import numpy as np

print("1-a:",np.ones(5))
print("1-b:",np.zeros(5))
print("1-c:",np.full(5,5))
print("1-d:",np.arange(1,6))
print("1-e:",np.arange(1,10,2))
print("1-f:",np.array([1,5,2,3,9]))

print("\n")

a = np.array([[1,2,1,5,4],[1,2,3,4,5]])
print("2-a:",a[0] + a[1])
a = np.array([[1,2,3,4,5],[5,4,3,2,1]])
print("2-b:",a[0] + a[1])
a = np.array([np.full(9,3),np.full(9,1)])
print("2-c:",a[0]-a[1])
a = np.array([[4,5,6],[3,2,1]])
print("2-d:",a[0] - a[1])
a = np.array([1,1,1,1])
print("2-e:", a * 2)
a = np.array([0,4,2,3])
print("2-f:",a * 3)
a = np.array([2,4,6,8,10])
print("2-g:",a/2)

print("\n")

a = [1,2,3]
b = [9,8,7]
def DP(lst1,lst2):
    c = 0
    for i in range(3):
        c += lst1[i] * lst2[i]
    return c
print("3-a:",DP(a,b))
a = np.array([1,2,3])
b = np.array([9,8,7])
c = a * b
print("3-b:",np.sum(c,axis = 0))

print("\n")

c = np.array([6,2,4])
def vec_size(c):
    temp = c[0]*c[0] + c[1]*c[1] + c[2]*c[2]
    return np.sqrt(temp)
    #return temp**0.5
print("4:",vec_size(c))

print("\n")

np.set_printoptions(formatter={'float_kind':lambda x: "{0:0.2f}".format(x)})
ax = np.array([1,0,0])
ay = np.array([0,1,0])
az = np.array([0,0,1])
bx = np.array([-2,1,4])
by = np.array([1,2,0])
bz = np.array([2,-1,1.25])
r_a = np.array([6,4,2])
def DP(lst1,lst2):
    c = 0
    turn = 0
    while(turn < 3):
        c += lst1[turn] * lst2[turn]
        turn += 1
    return c
print("5-a:",DP(ax,ay),DP(ax,az),DP(ay,az),DP(ax,ax))
print("5-b:",DP(bx,by),DP(bx,bz),DP(by,bz),DP(bx,bx))

def NewDP(lst1,lst2,lst3,lst4,lst5,lst6,vec):
    dot = np.dot(np.array([lst1,lst2,lst3]),vec)
    rev = np.linalg.inv(np.array([lst4,lst5,lst6]))
    return np.around(np.dot(dot,rev),2)

#a1 = np.linalg.inv(np.array([bx,by,bz]))
#a2 = np.dot(a1,r_a)
print("5-c:",NewDP(ax,ay,az,bx,by,bz,np.array([6,4,2])))
print("5-d:",NewDP(ax,ay,az,bx,by,bz,np.array([1,0,0])))
print("5-e:",NewDP(ax,ay,az,bx,by,bz,np.array([2,2,2])))

def NewDP2(lst1,lst2,lst3,vec):
    return np.dot(vec,[lst1,lst2,lst3])
print("5-f:",NewDP2(bx,by,bz,np.array([1,2,3])))
print("5-g:",NewDP2(bx,by,bz,np.array([4,1,7])))
print("5-h:",NewDP2(bx,by,bz,np.array([0,-1,2])))
#print(np.round(np.dot(np.linalg.inv([[1,0],[0,1]]),[1.44,5.44]),1))


# In[ ]:




