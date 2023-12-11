import numpy as np

def solve(part2=False):
    psum = 0
    g = np.argwhere(data == 1)
    gmap = {i: g[i] for i in range(len(g))}
    chk = set()
    for g1 in gmap:
        for g2 in gmap:
            if g1 == g2 or (g2, g1) in chk:
                continue
            chk.add((g1, g2))
            psum += np.abs(gmap[g1] - gmap[g2]).sum()
            if part2:
                x1, x2 = min(gmap[g1][0], gmap[g2][0]), max(gmap[g1][0], gmap[g2][0]) + 1
                y1, y2 = min(gmap[g1][1], gmap[g2][1]), max(gmap[g1][1], gmap[g2][1]) + 1
                x = data[x1:x2, y1:y2]
                x[x == 1] = 0
                c = np.sum(np.sum(x, axis=0) // 2 == x.shape[0])
                r = np.sum(np.sum(x, axis=1) // 2 == x.shape[1])
                psum += (1000000 - 2) * (r + c)
    return psum

if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(tuple(map(lambda x: 0 if x == '.' else 1, l.strip())) for l in f.readlines())
    data = np.array(data)

    c = 0
    for i in range(data.shape[0]):
        if np.count_nonzero(data[i+c] != 1) == data.shape[1]:
            data = np.insert(data, i+c+1,2, axis=0)
            c+= 1
    c = 0
    for i, cs in enumerate(np.sum(data, axis=0)):
        if cs == 0:
            data = np.insert(data, i+c+1,0, axis=1)
            c += 1
    for i in range(data.shape[1]):
        if np.count_nonzero(data[:,i+c] != 1) == data.shape[0]:
            data = np.insert(data, i+c+1,2, axis=1)
            c+= 1


    print('1:', solve())
    print('2:', solve(True))
