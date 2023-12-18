import numpy as np
from heapq import heappop, heappush


x_comp = {0: 0, 1: 1, 2: 0, 3: -1}
y_comp = {0: 1, 1: 0, 2: -1, 3: 0}


def solve(mind, maxd):
    q = [(0, 0, 0, -1)]
    seen = set()
    pathv = {}
    while q:
        val, x, y, ld = heappop(q)
        if (x + 1, y + 1) == heat.shape:
            return val
        if (x, y, ld) in seen:
            continue
        for d in range(4):
            hinc = 0
            if d == ld or (d + 2) % 4 == ld:
                continue
            for distance in range(1, maxd + 1):
                nx, ny = x + x_comp[d] * distance, y + y_comp[d] * distance
                if 0 <= nx < heat.shape[0] and 0 <= ny < heat.shape[1]:
                    hinc += heat[nx][ny]
                    if distance < mind:
                        continue
                    nc = val + hinc
                    if pathv.get((nx, ny, d), np.iinfo(np.int32).max) <= nc:
                        continue
                    pathv[(nx, ny, d)] = nc
                    heappush(q, (nc, nx, ny, d))
        seen.add((x, y, ld))


if __name__ == '__main__':
    with open('input.txt') as f:
        heat = tuple(tuple(map(int, l.strip())) for l in f.readlines())
    heat = np.array(heat)

    print('1:', solve(1, 3))
    print('2:', solve(4, 10))
