import numpy as np
from scipy import ndimage

if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(tuple(l.strip()) for l in f.readlines())

    for i, line in enumerate(data):
        if 'S' in line:
            S = (line.index('S'), i)

    rocks = np.array(tuple(tuple(1 if x == '#' else 0 for x in line) for line in data), dtype=bool)

    mat = np.zeros(rocks.shape, dtype=bool)
    mat[S] = 1

    is_adj = np.zeros((3, 3))
    for p in ((0, 1), (1, 0), (1, 2), (2, 1)):
        is_adj[p] = 1

    for _ in range(64):
        mat = ndimage.generic_filter(mat, np.sum, footprint=is_adj, mode='constant')
        mat = mat & np.invert(rocks)

    print('1:', np.sum(mat))
    inner_even_pos = {tuple(x) for x in np.argwhere(mat)}

    mat = np.zeros(rocks.shape, dtype=bool)
    mat[S] = 1
    for _ in range(65):
        mat = ndimage.generic_filter(mat, np.sum, footprint=is_adj, mode='constant')
        mat = mat & np.invert(rocks)

    inner_odd_pos = {tuple(x) for x in np.argwhere(mat)}

    N = mat.shape[0]
    reachable = {tuple(x) for x in np.argwhere(np.invert(rocks))}
    all_odd_pos = {(x, y) for x in range(N) for y in range(not x % 2, N, 2)} & reachable
    all_even_pos = {(x, y) for x in range(N) for y in range(x % 2, N, 2)} & reachable

    square_length = (2 * 26501365 + 1) // N
    outer_odd_pos = all_odd_pos - inner_odd_pos
    outer_even_pos = all_even_pos - inner_even_pos
    outer_pve_pos = {c for c in outer_odd_pos if (c[0] - 65) * (c[1] - 65) > 0} | {c for c in outer_even_pos if
                                                                                       (c[0] - 65) * (
                                                                                                   c[1] - 65) < 0}
    outer_nve_pos = {c for c in outer_odd_pos if (c[0] - 65) * (c[1] - 65) < 0} | {c for c in outer_even_pos if
                                                                                       (c[0] - 65) * (
                                                                                                   c[1] - 65) > 0}

    AO = len(inner_odd_pos)
    AE = len(inner_even_pos)
    BP = len(outer_pve_pos) - 1
    BN = len(outer_nve_pos)
    even_half, odd_half = sorted([square_length // 2, -((-square_length) // 2)], key=lambda x: x % 2)
    p2 = odd_half ** 2 * AO + even_half * odd_half * (BN + BP) + even_half ** 2 * AE

    print("2:", p2)



