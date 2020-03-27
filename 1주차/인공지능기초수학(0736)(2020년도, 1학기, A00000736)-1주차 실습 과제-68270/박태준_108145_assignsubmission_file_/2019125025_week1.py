# In[92]:


import numpy as np

#1번
a1 = np.ones((1,5))
print("1-a:",a1)

a2 = np.zeros((1,5))
print("1-b:",a2)

a3 = np.full((1,5),5)
print("1-c:",a3)

a4 = np.array(range(5)).reshape((1,5))
print("1-d:",a4+1)

a5 = np.arange(1,10,2)
print("1-e:",a5)
 
a6 = np.array([1,5,2,3,9])
print("1-f:",a6,'\n')

#2번
b11 = np.array([1,2,1,5,4])
b12 = np.array([1,2,3,4,5])
b1 = b11+b12
print("2-a:",b1)

b22 = np.array([5,4,3,2,1])
b2 = b12+b22
print("2-b:",b2)

b31 = np.full((1,9),3)
b32 = np.ones((1,9))
b3 = b31-b32
print("2-c:",b3)

b41 = np.array([4,5,6])
b42 = np.array([3,2,1])
b4 = b41-b42
print("2-d:",b4)

b51 = np.ones((1,4))
b5 = 2*b51
print("2-e:",b5)

b61 = np.array([0,4,2,3])
b6 = 3*b61
print("2-f:",b6)

b71 = np.array([2,4,6,8,10])
b7 = b71/2
print("2-g:",b7, '\n')

#3번
a = [1,2,3]
b = [9,8,7]

c11 = []
c12 = ''
for i in b:
    c12 = i*(b.index(i)+1)
    c11.append(c12)
print("3-a:",sum(c11))

c21 = np.multiply(a,b)
c2 = np.sum(c21)
print("3-b:",c2,'\n')

#4번
c = [6,2,4]

def vec_size(f):
    r = np.multiply(f,f)
    result = sum(r)
    return result**0.5

d1 = vec_size(c)
print("4:",d1,'\n')

#5번

# a coordinate
𝑎𝑥 = [1, 0, 0]
𝑎𝑦 = [0, 1, 0]
𝑎𝑧 = [0, 0, 1] 
# b coordinate
𝑏𝑥 = [-2, 1, 4]
𝑏𝑦 = [1, 2, 0]
𝑏𝑧 = [2, -1, 1.25]

e11 = sum(np.multiply(𝑎𝑥,𝑎𝑦))
e12 = sum(np.multiply(𝑎𝑥,𝑎𝑧))
e13 = sum(np.multiply(𝑎𝑦,𝑎𝑧))
e14 = sum(np.multiply(𝑎𝑥,𝑎𝑥))
print("5-a:",e11,e12,e13,e14)

e21 = sum(np.multiply(𝑏𝑥,𝑏𝑦))
e22 = sum(np.multiply(𝑏𝑥,𝑏𝑧))
e23 = sum(np.multiply(𝑏𝑦,𝑏𝑧))
e24 = sum(np.multiply(𝑏𝑥,𝑏𝑥))
print("5-b:",e21,e22,e23,e24)

e31 = [6,4,2]
x1 = [[-2,1,2],[1,2,-1],[4,0,1.25]]
result3 = np.linalg.solve(x1,e31)
print("5-c:",result3)

e41 = [1,0,0]
result4 = np.linalg.solve(x1,e41)
print("5-d:",result4)

e51 = [2,2,2]
result5 = np.linalg.solve(x1,e51)
print("5-e:",result5)

e61 = [1,2,3]
#e62 = np.add(𝑏𝑥*1,𝑏𝑦*2,𝑏𝑧*3)
x2 = [[1,0,0],[0,1,0],[0,0,1]]
result6 = np.linalg.solve(x2,e61)
print("5-f:",result6)

e71 = [4,1,7]
result7 = np.linalg.solve(x2,e71)
print("5-g:",result7)

e81 = [0,-1,2]
result8 = np.linalg.solve(x2,e81)
print("5-h:",result8)

