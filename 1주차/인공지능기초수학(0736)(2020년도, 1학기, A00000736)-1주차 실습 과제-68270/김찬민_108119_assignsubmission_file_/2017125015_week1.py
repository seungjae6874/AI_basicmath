import numpy as np

a_1 = np.ones(5, int);
a_2 = np.zeros(5, int);
a_3 = np.full(5, 5, int);
a_4 = np.arange(1, 6);
a_5 = np.arange(1,10,2);
a_6 = np.array([1,5,2,3,9]);

print('{} {}'.format("1-a)", a_1));
print('{} {}'.format("1-b)", a_2));
print('{} {}'.format("1-c)", a_3));
print('{} {}'.format("1-d)", a_4));
print('{} {}'.format("1-e)", a_5));
print('{} {}'.format("1-f)", a_6));

b_1 = np.array([1,2,1,5,4]) + np.arange(1, 6);
b_2 = np.arange(1,6) + np.sort(np.arange(1, 6))[::-1];
b_3 = np.full(9, 3, int) - np.full(9, 1, int);
b_4 = np.arange(4,7) - np.sort(np.arange(1,4))[::-1];
b_5 = 2 * np.full(4, 1, int);
b_6 = 3 * np.array([0,4,2,3]);
b_7 = 1/2 * np.arange(2, 11, 2, int);

print('{} {}'.format("2-a)", b_1));
print('{} {}'.format("2-b)", b_2));
print('{} {}'.format("2-c)", b_3));
print('{} {}'.format("2-d)", b_4));
print('{} {}'.format("2-e)", b_5));
print('{} {}'.format("2-f)", b_6));
print('{} {}'.format("2-g)", b_7));

a = [1,2,3];
b = [9,8,7];
def DP(a, b):
    dotSum = 0;
    for idx in range(0,3):
        dotSum += a[idx] * b[idx];
    return dotSum;
    
print('{} {}'.format("3-a)", DP(a, b)));

a = np.arange(1,4);
b = np.sort(np.arange(7,10))[::-1];
print('{} {}'.format("3-b)", np.sum(a * b)));

c = np.array([6,2,4]);
def vec_size(vec):
    return np.linalg.norm(vec)
print('{} {}'.format("4)", vec_size(c)));

a_x = np.array([1,0,0]);
a_y = np.array([0,1,0]);
a_z = np.array([0,0,1]);

b_x = np.array([-2, 1, 4]);
b_y = np.array([1, 2, 0]);
b_z = np.array([2,-1, 1.25]);

a = np.array([a_x, a_y, a_z]);
b = np.array([b_x, b_y, b_z]);
a_inv = np.linalg.inv(a);
b_inv = np.linalg.inv(b);

print('{} {} {} {} {}'.format("5-a)", np.dot(a_x, a_y), np.dot(a_x, a_y), np.dot(a_y, a_z), np.dot(a_x, a_x)));
print('{} {} {} {} {}'.format("5-b)", np.dot(b_x, b_y), np.dot(b_x, b_y), np.dot(b_y, b_z), np.dot(b_x, b_x)));

v = np.array([6,4,2]);
p = np.dot(b_inv, a);
print('{} {}'.format("5-c)", np.round(np.dot(v, p), 2)));
v = np.array([1,0,0]);
print('{} {}'.format("5-d)", np.round(np.dot(v, p), 2)));
v = np.array([2,2,2]);
print('{} {}'.format("5-e)", np.round(np.dot(v, p), 2)));

p = np.dot(a_inv, b);
v = np.array([1,2,3]);
print('{} {}'.format("5-f)", np.round(np.dot(v, p), 2)));
v = np.array([4,1,7]);
print('{} {}'.format("5-g)", np.round(np.dot(v, p), 2)));
v = np.array([0,-1,2]);
print('{} {}'.format("5-h)", np.round(np.dot(v, p), 2)));

