import numpy as np


def solve(d, part2=False):
    m = np.array(d, dtype=bool)
    h, w = m.shape
    vr, hr = 0, 0
    for i in range(w-1):
        n = min(i+1, w-i-1)
        if part2:
            if 1 == np.count_nonzero(np.invert(m[:,i-n+1:i+1] == np.flip(m[:,i+1:i+n+1], axis=1))):
                vr += i + 1
        elif np.all(m[:,i-n+1:i+1] == np.flip(m[:,i+1:i+n+1], axis=1)):
            vr += i+1
    for i in range(h-1):
        n = min(i+1, h-i-1)
        if part2:
            if 1 == np.count_nonzero(np.invert(m[i-n+1:i+1] == np.flip(m[i+1:i+n+1], axis=0))):
                hr += 100 * (i + 1)
        elif np.all(m[i-n+1:i+1] == np.flip(m[i+1:i+n+1], axis=0)):
            hr += 100 * (i+1)
    return hr + vr


if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(tuple(map(lambda x: 0 if x == '.' else 1, l.strip())) for l in f.readlines())

    p1, p2 = 0, 0
    i, j = 0, 0
    for j in range(len(data)):
        if len(data[j]) == 0:
            p1 += solve(data[i:j])
            p2 += solve(data[i:j], part2=True)
            i = j+1
    p1 += solve(data[i:j+1])
    p2 += solve(data[i:j+1], part2=True)
    print('1:', p1)
    print('2:', p2)