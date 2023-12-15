from functools import reduce


def hash(s):
    return reduce(lambda a, b: (a + b) * 17 % 256, [0] + s)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(list(map(ord, s)) for s in f.read().split(','))
    print('1:', sum([hash(h) for h in data]))

    lab = [s[:-(2 if s[-1] != 45 else 1)] for s in data]
    op = [s[-(2 if s[-1] != 45 else 1)] for s in data]
    foc = [s[-1] for s in data]

    hm = {i: {} for i in range(256)}
    for i, b in enumerate([hash(h) for h in lab]):
        lab_str = ''.join([chr(c) for c in lab[i]])
        if op[i] == 45:  # dash
            if lab_str in hm[b]:
                del hm[b][lab_str]
        elif op[i] == 61:  # equal
            hm[b][lab_str] = int(chr(foc[i]))

    s = 0
    for b, lens in hm.items():
        sn = 0
        for _, l in lens.items():
            s += reduce(lambda a, b: a * b, ([b + 1, (sn := sn + 1), l]))
    print('2:', s)
