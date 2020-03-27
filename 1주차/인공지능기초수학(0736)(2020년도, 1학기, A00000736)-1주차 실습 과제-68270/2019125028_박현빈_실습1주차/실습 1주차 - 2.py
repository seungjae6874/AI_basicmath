import numpy as np

a = np.array([1, 2, 1, 5, 4])
b = np.array([1, 2, 3, 4, 5])
print("2 - a)", a + b)

c = np.array([1, 2, 3, 4, 5])
d = np.array([5, 4, 3, 2, 1])
print("2 - b)", c + d)

e = np.array([3, 3, 3, 3, 3, 3, 3, 3, 3])
f = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
print("2 - c)", e - f)

g = np.array([4, 5, 6])
h = np.array([3, 2, 1])
print("2 - d)", g - h)

i = np.array([1, 1, 1, 1])
print("2 - e)", 2 * i)

j = np.array([0, 4, 2, 3])
print("2 - f)", 3 * j)

k = np.array([2, 4, 6, 8, 10])
print("2 - g)", k / 2)
