#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np
import math
### 1. 

#1-a (1,1,1,1,1)
arr1 = np.ones(5)
print('1-a: ', arr1)

#1-b (0,0,0,0,0)
arr2 = np.zeros(5)
print('1-b: ', arr2)

#1-c (5,5,5,5,5)
arr3 = np.full(5,5)
print('1-c: ',arr3)

#1-d (1,2,3,4,5)
arr4 = np.arange(1,6)
print('1-d: ',arr4)

#1-e (1,3,5,7,9)
arr5 = np.arange(1,10,2)
print('1-e: ',arr5)
 
#1-f (1,5,2,3,9)
arr6 = np.array([1,5,2,3,9])
print('1-f: ',arr6)

print("\n\n")



### 2.

#2-a (1, 2, 1, 5, 4) + (1, 2, 3, 4, 5) 
arr1 = np.array([1,2,1,5,4])
arr2 = np.array([1,2,3,4,5])
print('2-a: ',arr1 + arr2)

#2-b (1, 2, 3, 4, 5) + (5, 4, 3, 2, 1) 
arr1 = np.arange(1,6)
arr2 = np.arange(5,0,-1)
print('2-b: ',arr1 + arr2)

#2-c (3, 3, 3, 3, 3, 3, 3, 3, 3) – (1, 1, 1, 1, 1, 1, 1, 1, 1) 
arr1 = np.full(8,3)
arr2 = np.full(8,1)
print('2-c: ',arr1 - arr2)

#2-d (4, 5, 6) – (3, 2, 1) 
arr1 = np.array([4,5,6])
arr2 = np.array([3,2,1])
print('2-d: ',arr1 - arr2)

#2-e 2*(1, 1, 1, 1) 
arr = np.ones(4)
print('2-e: ',2 * arr)

#2-f 3*(0,4,2,3)
arr = np.array([0,4,2,3])
print('2-f: ',3 * arr)

#2-g 1/2*(2, 4, 6, 8, 10) 
arr = np.arange(2,11,2)
print('2-g: ',1/2 * arr)

print("\n\n")



###3.

#3-a
list1 = [1,2,3]
list2 = [9,8,7]
def DP(listA, listB):
    total = 0
    i = 0
    while(i < len(listA)):
        total += listA[i] * listB[i]
        i += 1
    return total
    
print('3-a: ',DP(list1, list2))

#3-b
arr1 = np.array([1,2,3])
arr2 = np.array([9,8,7])
print('3-b: ',np.sum(arr1 * arr2))

print("\n\n")



###4.
c = np.array([6,2,4])
def vec_size(vec):
    siz = math.sqrt(sum(vec * vec))
    return siz

print('4: ',vec_size(c))



print("\n\n")



###5.

# a coordinate
a_x = np.array([1,0,0])
a_y = np.array([0,1,0])
a_z = np.array([0,0,1])

# b coordinate
b_x = np.array([-2,1,4])
b_y = np.array([1,2,0])
b_z = np.array([2,-1,1.25])

#5-a
print("5-a: ", np.dot(a_x, a_y), np.dot(a_x, a_z), np.dot(a_y, a_z), np.dot(a_x, a_x))

#5-b
print("5-b: ", np.dot(b_x, b_y), np.dot(b_x, b_z), np.dot(b_y, b_z), np.dot(b_x, b_x))

#5-c to 5-h 이함수 만드느라 너무 힘들었습니다.... 
def equationB(va,vb,vc,cons): #coA 에서 바라본 cons 를 coB
    A = np.array([[va[0],vb[0],vc[0]],
                 [va[1],vb[1],vc[1]],
                 [va[2],vb[2],vc[2]]])
    
    X = np.linalg.inv(A).dot(cons)
    n = np.array([round(X[0],2), round(X[1],2), round(X[2],2) ])
    return n

def equationA(va,vb,vc,cons): #coB 에서 바라본 cons 를 coA
    A = np.array([[va[0],vb[0],vc[0]],
                 [va[1],vb[1],vc[1]],
                 [va[2],vb[2],vc[2]]])
    Ai = np.linalg.inv(A)
    X = np.linalg.inv(Ai).dot(cons)
    n = np.array([round(X[0],2), round(X[1],2), round(X[2],2) ])
    return n

#5-c
con = np.array([6,4,2])
print("5-c: ", equationB(b_x,b_y,b_z,con))

#5-d
con = np.array([1,0,0])
print("5-c: ", equationB(b_x,b_y,b_z,con))

#5-e
con = np.array([2,2,2])
print("5-c: ", equationB(b_x,b_y,b_z,con))

#5-f
con = np.array([1,2,3])
print("5-c: ", equationA(b_x,b_y,b_z,con))

#5-g
con = np.array([4,1,7])
print("5-c: ", equationA(b_x,b_y,b_z,con))

#5-h
con = np.array([0,-1,2])
print("5-c: ", equationA(b_x,b_y,b_z,con))



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




