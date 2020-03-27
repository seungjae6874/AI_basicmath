# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:17:14 2020

@author: WRL
"""
import numpy as np
np.set_printoptions(precision=2)
#import scipy.linalg as la

#1문제
list1 = np.ones((1,5))
print('1-a:',list1)

list3 = np.zeros((1,5))
print('1-b:',list3)

list2 = np.full((1,5),5)
print('1-c:',list2)

list4 = np.arange(1,6)
print('1-d:',list4)

list5 = np.arange(1,10,2)
print('1-e:',list5)

list6 = [1, 5, 2, 3, 9]
a=np.array(list6)
print('1-f:',a)

print('')
print('')

#2문제
in_arr1 = np.array([1,2,1,5,4])
in_arr2 = np.array([1,2,3,4,5])

out_arr = np.add(in_arr1, in_arr2)
print ('2-a:',out_arr)

in_arr3 = np.array([1,2,3,4,5])
in_arr4 = np.array([5,4,3,2,1])

out_arr_b = np.add(in_arr3, in_arr4)
print ('2-b:',out_arr_b)

in_arr5 = np.full((1,9),3)
in_arr6 = np.full((1,9),1)

out_arr_c = np.subtract(in_arr5, in_arr6)
print ('2-c:',out_arr_c)

in_arr7 = np.array([4,5,6])
in_arr8 = np.array([3,2,1])

out_arr_d = np.subtract(in_arr7, in_arr8)
print ('2-d:',out_arr_d)

in_arr9 = np.array([2])
in_arr10 = np.full((1,4),1)

out_arr_e = np.multiply(in_arr9, in_arr10)
print ('2-e:',out_arr_e)

in_arr11 = np.array([3])
in_arr12 = np.array([0,4,2,3])

out_arr_f = np.multiply(in_arr11, in_arr12)
print ('2-f:',out_arr_f)

in_arr13 = np.array([2])
in_arr14 = np.array([2,4,6,8,10])

out_arr_g = np.divide(in_arr14, in_arr13)
print ('2-g:',out_arr_g)

print('')
print('')

#3a문제
a = [1,2,3]
b = [9,8,7]

def DP(l1, l2):
    sum = 0
    for i in range(len(l1)):
        sum = sum + l1[i]*l2[i]
    return sum

ans = DP(a,b)
print('3-a:',ans)

#3b문제
a = np.array([1,2,3])
b = np.array([9,8,7])

def DP(l1, l2):
    sum = 0
    
    ans=l1*l2
    sum=np.sum(ans)
    
    return sum

print('3-b:',DP(a,b))

print('')
print('')

#4문제
c = np.array([6,2,4])

def vec_size(vec):
    s_vec = vec*vec
    ln = np.sum(s_vec)
    ln = np.sqrt(ln)
    return ln

print('4:',vec_size(c))

print('')
print('')

#5ab문제
ax = np.array([1,0,0])
ay = np.array([0,1,0])
az = np.array([0,0,1])

bx = np.array([-2,1,4])
by = np.array([1,2,0])
bz = np.array([2,-1,1.25])

print('5-a:', np.sum(ax*ay), ',', np.sum(ax*az), ',',np.sum(ay*az), ',',np.sum(ax*ax))
print('5-b:', np.sum(bx*by), ',', np.sum(bx*bz), ',',np.sum(by*bz), ',',np.sum(bx*bx))
    
#5c
a= np.array([[-2, 1, 2],[1, 2, -1],[4, 0, 1.25]])
b=np.array([[6],[4],[2]])

M= np.hstack([a,b])
x= np.linalg.solve(a,b)
y= np.transpose(x)
print('5-c:',y)

#5d
a= np.array([[-2, 1, 2],[1, 2, -1],[4, 0, 1.25]])
b= np.array([[1],[0],[0]])

M= np.hstack([a,b])
x= np.linalg.solve(a,b)
y= np.transpose(x)
print('5-d:',y)

#5e

a= np.array([[-2, 1, 2],[1, 2, -1],[4, 0, 1.25]])
b=np.array([[2],[2],[2]])

M= np.hstack([a,b])
x= np.linalg.solve(a,b)
y= np.transpose(x)
print('5-e:',y)

#5f

a= np.array([[1, 0, 0],[0, 1, 0],[0,0,1]])
b= np.array([[1],[2],[3]])

M= np.hstack([a,b])
x= np.linalg.solve(a,b)
y= np.transpose(x)
print('5-f:',y)

#5g

a= np.array([[1, 0, 0],[0, 1, 0],[0,0,1]])
b=np.array([[4],[1],[7]])

M= np.hstack([a,b])
x= np.linalg.solve(a,b)
y= np.transpose(x)
print('5-g:',y)

#5h

a= np.array([[1, 0, 0],[0, 1, 0],[0,0,1]])
b=np.array([[0],[-1],[2]])

M= np.hstack([a,b])
x= np.linalg.solve(a,b)
y= np.transpose(x)
print('5-h:',y)

print('')
print('')























