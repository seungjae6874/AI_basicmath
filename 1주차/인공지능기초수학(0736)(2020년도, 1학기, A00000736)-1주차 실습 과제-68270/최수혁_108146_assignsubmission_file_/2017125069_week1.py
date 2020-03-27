#!/usr/bin/env python
# coding: utf-8
import numpy as np 
import numpy.linalg as lin


# 1번
# 1-a
a=np.ones(5,float)
print("1-a:",a)

# 1-b
a=np.zeros(5)
print("1-b:",a)

# 1-c:
a=np.full(5,5)
print("1-c:",a)

# 1-d
a=np.arange(1,6)
print("1-d:",a)

# 1-e
a=np.arange(1,10,2)
print("1-e:",a)

# 1-f
a=[1,5,2,3,9]
a=np.array(a)
print("1-f:",a)
print("\n")


# 2번
# 2-a
p_1=[1,2,1,5,4]
p_2=[1,2,3,4,5]
p_1=np.array(p_1)
p_2=np.array(p_2)
print("2-a:",(p_1+p_2))


# 2-b
p_1=[1,2,3,4,5]
p_2=[5,4,3,2,1]
p_1=np.array(p_1)
p_2=np.array(p_2)
print("2-b:",(p_1+p_2))


# 2-c
p_1=[3,3,3,3,3,3,3,3,3]
p_2=[1,1,1,1,1,1,1,1,1]
p_1=np.array(p_1,float)
p_2=np.array(p_2)
print("2-c:",(p_1-p_2))


# 2-d
p_1=[4,5,6]
p_2=[3,2,1]
p_1=np.array(p_1)
p_2=np.array(p_2)
print("2-d:",(p_1-p_2))

# 2-e:
p_1=[1,1,1,1]
p_1=np.array(p_1,float)
print("2-e:",2*(p_1))


# 2-f
p_1=[0,4,2,3]
p_1=np.array(p_1)
print("2-f:",3*(p_1))


# 2-g
p_1=[2,4,6,8,10]
p_1=np.array(p_1)
p_1=((1/2)*(p_1))
p_1=np.array(p_1,float)
print("2-g:",p_1)
print("\n")


# 3번
#3-a
a=[1,2,3]
b=[9,8,7]
def DP(i,j):
    sum1=a[0]*b[0]
    sum2=a[1]*b[1]
    sum3=a[2]*b[2]
    sum4=sum1+sum2+sum3
    return sum4

print("3-a:",DP(a,b))


# 3-b
a=np.array([1,2,3])
b=np.array([9,8,7])
c=a*b
print("3-b:",np.sum(c))
print("\n")

# 4번
pre_def=np.array([6,2,4])
a=np.linalg.norm(pre_def)
print("4:",a)
print("\n")


# 5번
# a coordinate
a_x=np.array([1,0,0])
a_y=np.array([0,1,0])
a_z=np.array([0,0,1])

# b coordinate
b_x=np.array([-2,1,4])
b_y=np.array([1,2,0])
b_z=np.array([2,-1,1.25])

# 5-a
print("5-a:",sum(a_x*a_y),sum(a_x*a_z),sum(a_y*a_z),sum(a_x*a_x))


# 5-b
print("5-b:",sum(b_x*b_y),sum(b_x*b_z),sum(b_y*b_z),sum(b_x*b_x))

# 5-c
sum_b_array=np.vstack((b_x,b_y,b_z))
v=np.array([6,4,2])
v = np.linalg.solve(sum_b_array.T,v)
print("5-c:",np.around(v,2))

# 5-d
v=np.array([1,0,0])
v = np.linalg.solve(sum_b_array.T,v)
print("5-d:",np.around(v,3))

# 5-e
v=np.array([2,2,2])
v = np.linalg.solve(sum_b_array.T,v)
print("5-e:",np.around(v,2))

# 5-f
v=np.array([1,2,3])
v=np.dot(sum_b_array.T,v)
print("5-f:",v)

# 5-g
v=np.array([4,1,7])
v=np.dot(sum_b_array.T,v)
print("5-g:",v)

# 5-h
v=np.array([0,-1,2])
v=np.dot(sum_b_array.T,v)
print("5-h:",v)


