import numpy as np

#q_1

_1a = np.ones(5)
print('1-a : ', _1a)

_1b = np.zeros(5)
print('1-b : ', _1b)

_1c = np.full(5,5)
print('1-3 : ', _1c)

_1d = np.arange(1,6)
print('1-d : ', _1d)

_1e = np.arange(1,10,2)
print('1-e : ', _1e)

list_1f = [1,5,2,3,9]
_1f = np.array(list_1f)
print('1-f : ' , _1f)

#q_2

_2a = np.array([1,2,1,5,4]) + np.array([1,2,3,4,5])
print('2-a: ', _2a)

_2b = np.array([1,2,3,4,5]) + np.array([5,4,3,2,1])
print('2-b: ', _2b)

_2c = np.full(9,3) - np.full(9,1)
print('2-c: ', _2c)

_2d = np.array([4,5,6]) - np.array([3,2,1])
print('2-d: ', _2d)

_2e = 2 * np.array([1,1,1,1])
print('2-e: ', _2e)

_2f = 3 * np.array([0,4,2,3])
print('2-f: ', _2f)

_2g = 1/2 * np.arange(2,11,2)
print('2-g: ', _2g)

#q_3

def DP(vector1,vector2):
    vector_dot = sum([i*j for (i,j) in zip(vector1, vector2)])
    return vector_dot
vector_a1 = [1,2,3]
vector_b1 = [9,8,7]
_3a = DP(vector_a1,vector_b1)
print('3-a: ', _3a)
