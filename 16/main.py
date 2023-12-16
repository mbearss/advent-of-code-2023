import numpy as np

dup = {'n': (-1, 0), 's': (1, 0), 'e': (0, 1), 'w': (0, -1)}
ref = {'\\': {'n': 'w', 's': 'e', 'e': 's', 'w': 'n'},
       '/': {'n': 'e', 's':'w', 'e': 'n', 'w': 's'}}

def solve(loc, dir):
    beams = np.zeros(shape=(h, w), dtype=int)
    light, direction = [np.array(loc, dtype=int)], [dir]

    for t in range(600):    # arbitrarily chosen, long enough to complete sim
        new_light, new_dir, rem = [], [], []
        for i in range(len(light)):
            d = direction[i]
            light[i] += dup[d]
            c = tuple(light[i])
            if not (0 <= c[0] < h and 0 <= c[1] < w):
                continue
            beams[c] += (1 if d in ('e', 'w') else 2 if d in ('n', 's') else 0)
            if mirrors[c] == '|' and d in ('e', 'w'):
                if beams[c] // 2 == 0:  # haven't tried this beam yet
                    new_light.extend([np.array(c), np.array(c)])
                    new_dir.extend(['n', 's'])
                rem.append(i)
            if mirrors[c] == '-' and d in ('n', 's'):
                if beams[c] % 2 == 0:  # haven't tried this beam yet
                    new_light.extend([np.array(c), np.array(c)])
                    new_dir.extend(['e', 'w'])
                rem.append(i)
            if mirrors[c] in ('\\', '/'):
                ndir = ref[mirrors[c]][d]
                new_light.append(np.array(c))
                new_dir.append(ndir)
                rem.append(i)
        for i in rem[::-1]:
            del light[i]
            del direction[i]
        light.extend(new_light)
        direction.extend(new_dir)
        i = 0
        while i < len(light):
            if light[i][0] < 0 or light[i][0] >= h:
                del light[i]
                del direction[i]
            elif light[i][1] < 0 or light[i][1] >= w:
                del light[i]
                del direction[i]
            else:
                i += 1
    return np.sum(beams > 0)

if __name__ == '__main__':
    with open('input.txt') as f:
        mirrors = tuple(list(l.strip()) for l in f.readlines())
    mirrors = np.array(mirrors)

    h, w = len(mirrors), len(mirrors[0])

    print('1:', solve(np.array([0, -1]), 'e'))
    max_eng = 0
    for i in range(h):
        max_eng = max(solve(np.array([i, -1]), 'e'), max_eng)
        max_eng = max(solve(np.array([i, w]), 'w'), max_eng)
    for i in range(w):
        max_eng = max(solve(np.array([-1, i]), 's'), max_eng)
        max_eng = max(solve(np.array([h, i]), 'n'), max_eng)
    print('2:', max_eng)

