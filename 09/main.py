import numpy as np

if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(tuple(map(int, l.strip().split())) for l in f.readlines())

    s1, s2 = 0, 0
    for line in data:
        diff = [np.array(line)]
        while np.any(diff[-1] != 0):
            diff.append(np.diff(diff[-1]))

        x, y = 0, 0
        for d in diff[::-1]:
            x += d[-1]
            y = d[0] - y
        s1 += x
        s2 += y

    print('1:', s1)
    print('2:', s2)
