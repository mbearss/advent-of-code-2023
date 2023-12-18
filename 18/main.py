from functools import reduce

import numpy as np
from itertools import pairwise

direction = {'L': np.array((0, -1)), 'R': np.array((0, 1)), 'U': np.array((-1, 0)), 'D': np.array((1, 0))}


def solve(vertices, perimeter):
    # shoelace formula
    area = abs(reduce(lambda a, p: a + (p[1][1] + p[1][1]) * (p[1][0] - p[0][0]), [0] + list(pairwise(vertices)))) // 2
    return area - perimeter // 2 + 1 + perimeter


if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip() for l in f.readlines())

    c = [np.zeros(shape=2, dtype=int), np.zeros(shape=2, dtype=int)]
    vertices = ([], [])
    perimeter = [0, 0]
    for line in data:
        d1, l, color = line.split()
        d2 = int(color[2:-2], 16)
        c[0] += direction[d1] * int(l)
        c[1] += direction['RDLU'[int(color[-2])]] * d2
        vertices[0].append(tuple(c[0]))
        vertices[1].append(tuple(c[1]))
        perimeter[0] += int(l)
        perimeter[1] += int(d2)

    print('1:', solve(vertices[0], perimeter[0]))
    print('2:', solve(vertices[1], perimeter[1]))
