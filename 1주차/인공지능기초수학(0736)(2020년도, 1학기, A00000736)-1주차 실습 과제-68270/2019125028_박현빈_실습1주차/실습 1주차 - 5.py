import numpy as np

a_x = np.array([1, 0, 0])
a_y = np.array([0, 1, 0])
a_z = np.array([0, 0, 1])

b_x = np.array([-2, 1, 4])
b_y = np.array([1, 2, 0])
b_z = np.array([2, -1, 1.25])

print("5 - a)\n", a_x * a_y, "\n", a_x * a_z, "\n", a_y * a_z, "\n", a_x * a_x)

print("5 - b)\n", b_x * b_y, "\n", b_x * b_z, "\n", b_y * b_z, "\n", b_x * b_x)

a = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1]).reshape((3,3))

b = np.array([-2, 1, 4, 1, 2, 0, 2, -1, 1.25]).reshape((3,3))

def location_a(a, b, c):    
    doted_a = np.dot(c, a)
    inversed_b = np.linalg.inv(b)
    location_a = np.dot(doted_a, inversed_b)
    location_a = np.round(location_a, 2)

    return location_a

def location_b(a, b, c):
    doted_b = np.dot(c, b)
    inversed_a = np.linalg.inv(a)
    location_b = np.dot(doted_b, inversed_a)
    location_b = np.round(location_b, 2)

    return location_b


c = np.array([6, 4, 2])
answer_c_d_e = location_a(a, b, c)
print("5 - c)", answer_c_d_e)

c = np.array([1, 0, 0])
answer_c_d_e = location_a(a, b, c)
print("5 - d)", answer_c_d_e)

c = np.array([2, 2, 2])
answer_c_d_e = location_a(a, b, c)
print("5 - e)", answer_c_d_e)

c = np.array([1, 2, 3])
answer_f_g_h = location_b(a, b, c)
print("5 - f)", answer_f_g_h)

c = np.array([4, 1, 7])
answer_f_g_h = location_b(a, b, c)
print("5 - g)", answer_f_g_h)

c = np.array([0, -1, 2])
answer_f_g_h = location_b(a, b ,c)
print("5 - h)", answer_f_g_h)


