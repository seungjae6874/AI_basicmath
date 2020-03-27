import numpy as np


def p1():
    results = []

    results.append(np.ones(5))  # 1-a
    results.append(np.zeros(5))  # 1-b
    results.append(np.full(5, 5))  # 1-c
    results.append(np.arange(1, 6))  # 1-d
    results.append(np.arange(1, 10, 2))  # 1-e
    results.append(np.array([1, 5, 2, 3, 9]))  # 1-f

    print_results(1, results)


def p2():
    results = []

    a = np.array([1, 2, 1, 5, 4])
    b = np.arange(1, 6)
    results.append(a + b)  # 2-a

    a = np.arange(1, 6)
    b = np.arange(5, 0, -1)
    results.append(a + b)  # 2-b

    a = np.full(9, 3)
    b = np.ones(9)
    results.append(a - b)  # 2-c

    a = np.arange(4, 7)
    b = np.arange(3, 0, -1)
    results.append(a - b)  # 2-d

    a = np.ones(4)
    results.append(2 * a)  # 2-e

    a = np.array([0, 4, 2, 3])
    results.append(3 * a)  # 2-f

    a = np.arange(2, 11, 2)
    results.append(1 / 2 * a)  # 2-g

    print_results(2, results)


def p3():
    results = []

    a = [1, 2, 3]
    b = [9, 8, 7]

    def DP(a, b):
        result = 0
        for i in range(3):
            result += a[i] * b[i]
        return result

    results.append(DP(a, b))  # 3-a

    a = np.array(a)
    b = np.array(b)
    results.append(np.sum(a * b))  # 3-b

    print_results(3, results)


def p4():
    c = np.array([6, 2, 4])

    def vec_size(vector):
        return np.linalg.norm(vector)

    print(f'4: {vec_size(c)}')  # 4


def p5():
    ax = np.array([1, 0, 0])
    ay = np.array([0, 1, 0])
    az = np.array([0, 0, 1])
    bx = np.array([-2, 1, 4])
    by = np.array([1, 2, 0])
    bz = np.array([2, -1, 1.25])

    print(f'5-a: {ax.dot(ay)} {ax.dot(az)} {ay.dot(az)} {ax.dot(ax)}')  # 5-a
    print(f'5-b: {bx.dot(by)} {bx.dot(bz)} {by.dot(bz)} {bx.dot(bx)}')  # 5-b

    def change_3basis(v, nx, ny, nz):
        rx = np.round(v.dot(nx) / np.sum(np.square(nx)), 2)
        ry = np.round(v.dot(ny) / np.sum(np.square(ny)), 2)
        rz = np.round(v.dot(nz) / np.sum(np.square(nz)), 2)
        return np.array([rx, ry, rz])

    v = np.array([6, 4, 2])
    print(f'5-c: {change_3basis(v, bx, by, bz)}')  # 5-c
    v = np.array([1, 0, 0])
    print(f'5-d: {change_3basis(v, bx, by, bz)}')  # 5-d
    v = np.array([2, 2, 2])
    print(f'5-e: {change_3basis(v, bx, by, bz)}')  # 5-e
    m = np.array([bx, by, bz])
    v = np.array([1, 2, 3])
    v = np.array([v.dot(m[:, 0]), v.dot(m[:, 1]), v.dot(m[:, 2])])
    print(f'5-f: {v}')  # 5-f
    v = np.array([4, 1, 7])
    v = np.array([v.dot(m[:, 0]), v.dot(m[:, 1]), v.dot(m[:, 2])])
    print(f'5-g: {v}')  # 5-g
    v = np.array([0, -1, 2])
    v = np.array([v.dot(m[:, 0]), v.dot(m[:, 1]), v.dot(m[:, 2])])
    print(f'5-h: {v}')  # 5-h


def print_results(num, results):
    for i in range(len(results)):
        print(f'{num}-{chr(ord("a") + i)}: {results[i]}')


if __name__ == '__main__':
    problems = [p1, p2, p3, p4, p5]
    for solve in problems:
        solve()
        print('\n')
