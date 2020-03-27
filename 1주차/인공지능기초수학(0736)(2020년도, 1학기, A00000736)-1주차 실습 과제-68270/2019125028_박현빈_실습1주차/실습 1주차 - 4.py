import numpy as np

c = np.array([6, 2, 4])

def vec_size(c):
    return len(c)

size = vec_size(c)

print("4 - 1)", size)

c = input().split()
c = list(map(int, c))

size = vec_size(c)

print("4 - 2)", size)
