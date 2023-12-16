def transpose(m):
    return map(''.join, zip(*m))

def tilt(m, reverse=False):
    r = ('O.', '.O') if reverse else ('.O', 'O.')
    for _ in range(width):
        m = map(lambda x: x.replace(*r), m)
    return m

def spin(m):
    for i in range(4):
        m = tilt(transpose(m), i >= 2)
    return m

def score(m):
    s = 0
    for col in m:
        s += sum([i*(c == 'O') for i, c in enumerate(col[::-1], 1)])
    return s


if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip() for l in f.readlines())
    height, width = len(data), len(data[0])

    p1 = tilt(transpose(data))
    print('1:', score(p1))

    i = 0
    states = {}
    found_cycle = False
    while i < 1_000_000_000:
        data = list(spin(data))
        h = '\n'.join(data)
        i += 1
        if not found_cycle and (found_cycle := h in states):
            cycle_length = i - states[h]
            i += cycle_length * ((1_000_000_000 - i) // cycle_length)
        else:
            states[h] = i

    print('2:', score(transpose(data)))

