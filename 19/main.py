def ranges_outer(f):
    return ranges_inner(wf[f])


def ranges_inner(w):
    it = w[0]
    if it[0] == 'True':
        it = it[1]
    if it == "R":
        return []
    if it == "A":
        return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
    if isinstance(it, str):
        return ranges_outer(it)

    test = it[0]
    gt = ">" in test
    ch = test[3]
    val = int(test[7:])
    val_p = val + 1 if gt else val - 1
    if_true = split_ranges(ch, gt, val, ranges_inner([it[1]]))
    if_false = split_ranges(ch, not gt, val_p, ranges_inner(w[1:]))
    return if_true + if_false


def split_ranges(ch, gt, val, ranges):
    ch = 'xmas'.index(ch)
    nx = [(r[i] if i != ch or ((lo := max(r[i][0], val + 1)) < (hi := min(r[i][1], val - 1)))
           else (lo, r[i][1]) if gt else (r[i][0], hi)) for r in ranges
          for i in range(4)]
    return [nx[i:i+4] for i in range(0, len(nx), 4)]



if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip() for l in f.readlines())
    wf = {}
    sa = 0
    for line in data:
        if len(line) > 0 and not line.startswith('{'):
            r = line[:-1].split('{')
            n = r.pop(0)
            wf[n] = []
            for t in r[0].split(','):
                rule, result = t.split(':') if ':' in t else ('True', t)
                if rule != 'True':
                    rule = ('p["' + rule[0] + '"]' + rule[1:]).replace('=', '==')
                wf[n].append((rule, result))
        elif len(line) > 0:
            p = {}
            for t in line[1:-1].split(','):
                k, v = t.split('=')
                p[k] = int(v)

            s, i = 'in', 0
            while True:
                test = wf[s][i][0]
                if eval(test):
                    s, i = wf[s][i][1], 0
                    if s in 'RA':
                        break
                else:
                    i += 1
            if s == 'A':
                sa += sum(v for v in p.values())

    print('1:', sa)

    sa = 0
    for rng in ranges_outer('in'):
        v = 1
        for l, h in rng:
            v *= h - l + 1
        sa += v
    print('2:', sa)
