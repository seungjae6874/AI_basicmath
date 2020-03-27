#!/usr/bin/env python
# coding: utf-8

# In[76]:


import numpy as np
a = np.ones(5)
print("1-a:",a)
b = np.zeros(5)
print("1-b:",b)
c = np.full((5), 5)
print("1-c:",c)
d = np.arange(1,6)
print("1-d:",d)
e = np.arange(1,10,2)
print("1-e:",e)
f = np.array([1, 5, 2, 3, 9])
print("1-f:",f)

print("\n")

a = np.array([1, 2, 1, 5, 4])
b = np.array([1, 2, 3, 4, 5])
print("2-a",a + b)

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
print("2-b",a + b)

a = np.array([3, 3, 3, 3, 3, 3, 3, 3, 3])
b = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
print("2-c",a - b)

a = np.array([4, 5, 6])
b = np.array([3, 2, 1])
print("2-d",a - b)

a = np.array([1, 1, 1, 1])
print("2-e",2 * a)

a = np.array([0, 4, 2, 3])
print("2-f",3 * a)

a = np.array([2, 4, 6, 8, 10])
print("2-g",1/2 * a)

print("\n")

def DP(a, b):
    dot = 0
    for i in range(0,3):
        dot = dot + (a[i] * b[i])
    return dot

a = [1, 2, 3]
b = [9, 8, 7]
print("3-a:", DP(a, b))

a = np.array([1, 2, 3])
b = np.array([9, 8, 7])
print("3-b:",np.sum(a*b))

print("\n")

c = np.array([6, 2, 4])
print("4:",(sum(c*c))**0.5)

print("\n")

a = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
b = np.array([[-2, 1, 4], [1, 2, 0], [2, -1, 1.25]])
print("5-a:", sum(a[0] * a[1]), sum(a[0] * a[2]), sum(a[1] * a[2]), sum(a[0] * a[0]))
print("5-b:", sum(b[0] * b[1]), sum(b[0] * b[2]), sum(b[1] * b[2]), sum(b[0] * b[0]))

c = np.array([6, 4, 2])
print ("5-c:", np.round(np.dot(c, (np.dot(a, np.linalg.inv(b)))), 2))

c = np.array([1, 0, 0])
print ("5-d:", np.round(np.dot(c, (np.dot(a, np.linalg.inv(b)))), 2))

c = np.array([2, 2, 2])
print ("5-e:", np.round(np.dot(c, (np.dot(a, np.linalg.inv(b)))), 2))

c = np.array([1, 2, 3])
print ("5-f:", np.round(np.dot(c, (np.dot(b, np.linalg.inv(a)))), 2))

c = np.array([4, 1, 7])
print ("5-g:", np.round(np.dot(c, (np.dot(b, np.linalg.inv(a)))), 2))

c = np.array([0, -1, 2])
print ("5-h:", np.round(np.dot(c, (np.dot(b, np.linalg.inv(a)))), 2))


# In[ ]:





# In[ ]:




