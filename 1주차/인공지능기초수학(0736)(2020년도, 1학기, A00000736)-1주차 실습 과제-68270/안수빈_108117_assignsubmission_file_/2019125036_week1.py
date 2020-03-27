import numpy as np
import math

#1
a1 = np.ones(5)
print('1-a:', a1)
a2 = np.zeros(5)
print('1-b:', a2)
a3 = np.full(5, 5)
print('1-c:', a3)
a4 = np.arange(1,6)
print('1-d:', a4)
a5 = np.arange(1,10,2)
print('1-e:', a5)
a6 = np.array([1,5,2,3,9])
print('1-f:', a6)
print('\n')

#2-a
a = np.array([1,2,1,5,4])
b = np.array([1,2,3,4,5])
print('2-a:', a+b)
#2-b
a = np.array([1,2,3,4,5])
b = np.array([5,4,3,2,1])
print('2-b:', a+b)
#2-c
a = np.ones(9)
print('2-c:', 3*a-a)
#2-d
a = np.array([4, 5, 6])
b = np.array([3, 2, 1])
print('2-d:', a-b)
#2-e
a = np.ones(4)
print('2-e:', 2*a)
#2-f
a = np.array([0, 4, 2, 3])
print('2-f:', 3*a)
#2-g
a = np.arange(2, 11, 2)
print('2-g:', 0.5*a)
print('\n')

#3-a
def dp(list1, list2):
    dot = list1[0]*list2[0] + list1[1]*list2[1] + list1[2]*list2[2]
    return dot
a = [1, 2, 3]
b = [9, 8, 7]
print('3-a:', dp(a, b))

#3-b
a = np.array([1, 2, 3])
b = np.array([9, 8, 7])
print('3-b:', np.sum(np.dot(a, b)))
print('\n')

#4
def vec_size(x):
    s = 0
    s = sum(x*x)
    result = math.sqrt(s)
    return result
c = np.array([6, 2, 4])
print('4:', vec_size(c))
print('\n')

#5-a
a = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print('5-a:', sum(a[0]*a[1]), sum(a[0]*a[2]), sum(a[1]*a[2]), sum(a[0]*a[0]))
#5-b
b = np.array([[-2, 1, 4], [1, 2, 0], [2, -1, 1.25]])
print('5-b:', '%.1d'%sum(b[0]*b[1]), sum(b[0]*b[2]), sum(b[1]*b[2]), '%.d'%sum(b[0]*b[0]))
#5-c
A = np.array([[-2, 1, 2], [1, 2, -1], [4, 0, 1.25]])
B = np.array([6, 4, 2])
z = np.linalg.solve(A, B)
print('5-c:', z)
#5-d
A = np.array([[-2, 1, 2], [1, 2, -1], [4, 0, 1.25]])
B = np.array([1, 0, 0])
np.set_printoptions(precision=2)
z = np.linalg.solve(A, B)
print('5-d:', z)
#5-e
A = np.array([[-2, 1, 2], [1, 2, -1], [4, 0, 1.25]])
B = np.array([2, 2, 2])
np.set_printoptions(precision=2)
z = np.linalg.solve(A, B)
print('5-e:', z)
#5-f
A = np.array([[-2, 1, 2], [1, 2, -1], [4, 0, 1.25]])
B = np.array([1, 2, 3])
np.set_printoptions(precision=2)
C = np.dot(A, B)
print('5-f:', C)
#5-g
A = np.array([[-2, 1, 2], [1, 2, -1], [4, 0, 1.25]])
B = np.array([4, 1, 7])
np.set_printoptions(precision=2)
C = np.dot(A, B)
print('5-g:', C)
#5-h
A = np.array([[-2, 1, 2], [1, 2, -1], [4, 0, 1.25]])
B = np.array([0, -1, 2])
np.set_printoptions(precision=2)
C = np.dot(A, B)
print('5-h:', C)
