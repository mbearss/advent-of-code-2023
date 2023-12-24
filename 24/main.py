from itertools import combinations
from sympy import var, Eq, solve


def get_coef(p, v):
    a = v[1] / v[0]
    b = p[1] - (p[0] * v[1]) / v[0]

    return a, b


def get_time(d, d0, v):
    return (d - d0) / v


lower_limit = 200000000000000
upper_limit = 400000000000000

if __name__ == '__main__':
    with open('input.txt') as f:
        pos, vel = zip(
            *tuple(tuple(tuple(map(int, x.split(','))) for x in l.strip().split('@')) for l in f.readlines()))

    N = len(pos)
    total = 0
    for i, j in combinations(range(N), 2):
        c1 = get_coef(pos[i], vel[i])
        c2 = get_coef(pos[j], vel[j])

        x = (c2[1] - c1[1]) / (c1[0] - c2[0]) if c1[0] != c2[0] else -1
        y = c1[0] * x + c1[1]

        tx1 = get_time(x, pos[i][0], vel[i][0])
        tx2 = get_time(x, pos[j][0], vel[j][0])

        if tx1 >= 0 and tx2 >= 0 and lower_limit <= x <= upper_limit and lower_limit <= y <= upper_limit:
            total += 1

    print('1:', total)

    sx = var("sx")
    sy = var("sy")
    sz = var("sz")

    vx = var("vx")
    vy = var("vy")
    vz = var("vz")

    eq = []

    # only need 3 points
    t = [var('t' + str(x)) for x in range(9)]
    for i in range(3):
        eq.append(Eq(sx + vx * t[i], pos[i][0] + vel[i][0] * t[i]))
        eq.append(Eq(sy + vy * t[i], pos[i][1] + vel[i][1] * t[i]))
        eq.append(Eq(sz + vz * t[i], pos[i][2] + vel[i][2] * t[i]))

    ans = solve(eq)[0]
    print('2:', ans[sx] + ans[sy] + ans[sz])
