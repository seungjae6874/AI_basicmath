#!/usr/bin/env python
# coding: utf-8

# In[66]:


import numpy as np

#1

print("1-a: ", np.ones(5))

print("1-b: ", np.zeros(5))

print("1-c: ", np.full(5,5))

print("1-d: ", np.arange(1,6))

print("1-e: ", np.arange(1,10, 2))

print("1-f: ", np.array([1, 5, 2, 3, 9]))

#2

print("\n2-a: ", np.array([1, 2, 1, 5, 4]) + np.arange(1,6))

print("2-b: ", np.arange(1,6) + np.arange(5,0, -1))

print("2-c: ", np.full(9,3) - np.full(9,1))

print("2-d: ", np.arange(4,7)-np.arange(3,0, -1))

print("2-e: ", 2*np.full(4,1))

print("2-f: ", 3*np.array([0, 4, 2, 3]))

print("2-g: ", 1/2*np.arange(2, 11, 2))

#3

def DP(a, b):
    
    return sum([a[i]*b[i] for i in range(len(b))] )

a=[1,2,3]
b=[9,8,7]

print("\n3-a: ",DP(a, b))

a = np.array([1,2,3])
b = np.array([9,8,7])

print("3-b: ",np.sum(a*b))

#4

c = [6,2,4]

def vec_size(Inp_vec):
    return (np.sum(Inp_vec*Inp_vec))**(1/2)

vec = np.array(c)

print("\n4: ",vec_size(vec))

#5

# a coordinate
ax=np.array([1, 0, 0])
ay=np.array([0, 1, 0])
az=np.array([0, 0, 1])

# b coordinate
bx=np.array([-2, 1, 4])
by=np.array([1, 2, 0])
bz=np.array([2, -1, 1.25])

print("\n5-a: ",np.sum(np.array(ax)*np.array(ay))
      ,np.sum(np.array(ax)*np.array(az))
      ,np.sum(np.array(ay)*np.array(az))
      ,np.sum(np.array(ax)*np.array(ax))
     )
print("5-b: ",np.sum(np.array(bx)*np.array(by))
      ,np.sum(np.array(bx)*np.array(bz))
      ,np.sum(np.array(by)*np.array(bz))
      ,np.sum(np.array(bx)*np.array(bx))
     )

MAT_A = np.array([[1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1]])
MAT_B = np.array([[-2, 1, 4],
                  [1, 2, 0],
                  [2, -1, 1.25]])

#역함수를 통해 BASIS를 구함

MAT_X_a = np.dot(np.linalg.inv(MAT_B),MAT_A)

#주어진 벡터

arr = np.array([6,4,2])
print("5-c: ",np.round(np.dot(arr, MAT_X_a), 2))

arr = np.array([1,0,0])
print("5-d: ",np.round(np.dot(arr, MAT_X_a), 2))

arr = np.array([2, 2, 2])
print("5-e: ",np.round(np.dot(arr, MAT_X_a), 2))

#역함수를 통해 BASIS를 구함

MAT_X_b = np.dot(np.linalg.inv(MAT_A),MAT_B)

#주어진 벡터
arr = np.array([1,2,3])
print("5-f: ",np.round(np.dot(arr, MAT_X_b), 2))

arr = np.array([4,1,7])
print("5-g: ",np.round(np.dot(arr, MAT_X_b), 2))

arr = np.array([0,-1,2])
print("5-h: ",np.round(np.dot(arr, MAT_X_b), 2))





