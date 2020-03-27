import numpy as np

a = input().split()
a = list(map(int, a))

b = input().split()
b = list(map(int, b))

dot_product = 0

for i in range(len(a)):
    dot_product += int(a[i]) * int(b[i])
    
    
print("3 - a)", dot_product)


v_a = np.array([1, 2, 3])
v_b = np.array([9, 8, 7])

print("3 - b)", np.sum(v_a*v_b))
        




