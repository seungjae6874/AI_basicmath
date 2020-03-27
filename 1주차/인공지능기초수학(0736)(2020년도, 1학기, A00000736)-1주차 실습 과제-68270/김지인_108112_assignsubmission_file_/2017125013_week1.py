import numpy as np

#1-a
a1 = np.ones(5)
print('1-a: {}'.format(a1))

#1-b
a2 = np.zeros(5)
print('1-b: {}'.format(a2))

#1-c
a3 = np.full(5,5)
print('1-c: {}'.format(a3))

#1-d
a4 = np.arange(1,6)
print('1-d: {}'.format(a4))

#1-e
a5 = np.arange(1,10,2)
print('1-e: {}'.format(a5))

#1-f
a6 = np.array([1, 5, 2, 3, 9])
print('1-f: {}\n\n'.format(a6))

#2-a
a = np.array([1,2,1,5,4])
b = np.array([1,2,3,4,5])
c = np.add(a,b)
print('2-a: {}'.format(c))

#2-b
a = np.arange(1,6)
b = np.arange(5,0,-1)
c = np.add(a,b)
print('2-b: {}'.format(c))

#2-c
a = np.full(9,3)
b = np.ones(9)
c = np.subtract(a,b)
print('2-c: {}'.format(c))

#2-d
a = np.arange(4,7)
b = np.arange(3,0,-1)
c = np.subtract(a,b)
print('2-d: {}'.format(c))

#2-e
a = np.ones(4)
b = 2*a
print('2-e: {}'.format(b))

#2-f
a = np.array([0,4,2,3])
b = 3*a
print('2-f: {}'.format(b))

#2-g
a = np.arange(2,11,2)
b = 1/2*a
print('2-g: {}\n\n'.format(b))

#3-a
def DP(a,b):
    total = 0 
    for i in range(0,3):
        total += a[i] * b[i]
    return total

a1 = [1,2,3]
b1 = [9,8,7]

print('3-a: {}'.format(DP(a1,b1)))

#3-b
a2 = np.array([1,2,3])
b2 = np.array([9,8,7])
c2 = np.dot(a2,b2)
print('3-b: {}\n\n'.format(c2))

#4
def vec_size(a):
    size = 0
    size = np.linalg.norm(a)
    return size 
c = np.array([6,2,4])
print('4: {}\n\n'.format(vec_size(c)))

#5-a
a_x = np.array([1,0,0])
a_y = np.array([0,1,0])
a_z = np.array([0,0,1])

ans1 = np.dot(a_x,a_y)
ans2 = np.dot(a_x,a_z)
ans3 = np.dot(a_y,a_z)
ans4 = np.dot(a_x,a_x)


print('5-a: {} {} {} {}'.format(ans1,ans2,ans3,ans4))

#5-b
b_x = np.array([-2,1,4])
b_y = np.array([1,2,0])
b_z = np.array([2,-1,1.25])

ans1 = np.dot(b_x,b_y)
ans2 = np.dot(b_x,b_z)
ans3 = np.dot(b_y,b_z)
ans4 = np.dot(b_x,b_x)

print('5-b: {} {} {} {}'.format(ans1,ans2,ans3,ans4))

#5-c~h
a = np.array([[1,0,0],
              [0,1,0],
              [0,0,1]])
b = np.array([[-2,1,4],
              [1,2,0],
              [2,-1,1.25]])
p = np.dot(np.linalg.inv(b),a)

vector = np.array([6,4,2])
ans = np.round(np.dot(vector,p), 2)
print('5-c: {}'.format(ans))

vector = np.array([1,0,0])
ans = np.round(np.dot(vector,p), 2)
print('5-d: {}'.format(ans))

vector = np.array([2,2,2])
ans = np.round(np.dot(vector,p), 2)
print('5-e: {}'.format(ans))

p_r = np.dot(np.linalg.inv(a),b)

vector = np.array([1,2,3])
ans = np.round(np.dot(vector,p_r), 2)
print('5-f: {}'.format(ans))

vector = np.array([4,1,7])
ans = np.round(np.dot(vector,p_r), 2)
print('5-g: {}'.format(ans))

vector = np.array([0,-1,2])
ans = np.round(np.dot(vector,p_r), 2)
print('5-h: {}'.format(ans))

