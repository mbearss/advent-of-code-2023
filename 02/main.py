from functools import reduce

cube_num = {'red': 12, 'green': 13, 'blue': 14}

if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip() for l in f.readlines())
    s = 0
    m = 0
    for line in data:
        pos = True
        min_cube = {'red': 0, 'green': 0, 'blue': 0}
        rest = line.split(':')
        gid = int(rest.pop(0)[5:])
        for g in [g.split(',') for g in rest[0].split(';')]:
            for v, k in [c.split() for c in g]:
                if cube_num[k] < int(v):
                    pos = False
                min_cube[k] = max(min_cube[k], int(v))
        s += gid if pos else 0
        m += reduce(lambda x, y: x*y, min_cube.values())
    print('1:', s)
    print('2:', m)